#!/usr/bin/env python3
"""Task-specific changed-path ownership check (GOV-005-CF5 hardening).

CF-5 hardening: a change set is validated against the writable paths of the ONE accountable
active task identified by the branch, NOT a union of all active tasks and NOT a broad
governance directory allowlist. Fails closed when task identity is missing, ambiguous, not
registered, or not active. Also validates every governed handoff file that changed.

Authorization for a change set on branch B:
  1. Identify exactly one active task whose `branch == B`. Missing / ambiguous / inactive /
     unregistered => FAIL (fail closed).
  2. Allowed paths = that task's `writable_paths` + `shared_paths` + declared
     `correction_phase_modifies.files` (explicit, validated sequential-phase exception) +
     the single self-registration file `trace/ACTIVE_WORK_REGISTRY.yaml`.
     Directory entries (ending in '/') are honoured ONLY when the task itself declared them.
  3. Any changed path outside that exact envelope => FAIL.
  4. Every changed governed handoff file (trace/evidence/*HANDOFF*.json) is schema-validated;
     an invalid or out-of-vocabulary handoff => FAIL.

Usage:
  check_changed_path_ownership.py --base <ref> [--branch <name>]
  check_changed_path_ownership.py --branch <name> --paths a b c   # explicit change set (tests)
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required. Install: python3 -m pip install -r scripts/governance-requirements.txt"
    ) from exc

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

INACTIVE_STATUSES = {"MERGED", "CLOSED", "REJECTED"}
# Single self-registration file an active task may always touch (task-scoped, not a broad dir).
SELF_REGISTRATION_PATH = "trace/ACTIVE_WORK_REGISTRY.yaml"
HANDOFF_RE = re.compile(r"^trace/evidence/.*HANDOFF\.json$")


class OwnershipError(Exception):
    """Fail-closed identity/ownership failure."""


def load_registry() -> dict[str, Any]:
    return yaml.safe_load((ROOT / SELF_REGISTRATION_PATH).read_text(encoding="utf-8"))


def active_statuses(registry: dict[str, Any]) -> set[str]:
    vocab = set(registry.get("status_vocabulary", []))
    return vocab - INACTIVE_STATUSES


def identify_active_task(registry: dict[str, Any], branch: str) -> dict[str, Any]:
    if not branch:
        raise OwnershipError("task identity missing: no branch provided")
    tasks = registry.get("active_tasks", [])
    matches = [t for t in tasks if t.get("branch") == branch]
    if not matches:
        raise OwnershipError(f"branch/task mismatch: no registered active task for branch '{branch}'")
    if len(matches) > 1:
        ids = sorted(t.get("task_id", "?") for t in matches)
        raise OwnershipError(f"ambiguous task identity for branch '{branch}': {ids}")
    task = matches[0]
    allowed = active_statuses(registry)
    status = task.get("status")
    if status not in allowed:
        raise OwnershipError(
            f"task '{task.get('task_id')}' is not active (status={status}); refusing change set"
        )
    return task


def allowed_paths_for_task(task: dict[str, Any]) -> set[str]:
    allowed: set[str] = set(task.get("writable_paths", []))
    allowed.update(task.get("shared_paths", []))
    phase = task.get("correction_phase_modifies") or {}
    allowed.update(phase.get("files", []))
    allowed.add(SELF_REGISTRATION_PATH)  # self-registration only
    return allowed


def is_covered(path: str, allowed: set[str]) -> bool:
    for entry in allowed:
        if entry.endswith("/") and path.startswith(entry):
            return True
        if path == entry:
            return True
    return False


def find_unauthorized(changed: list[str], allowed: set[str]) -> list[str]:
    return [p for p in changed if not is_covered(p, allowed)]


def governed_handoff_files(changed: list[str]) -> list[str]:
    return [p for p in changed if HANDOFF_RE.match(p)]


def evaluate(registry: dict[str, Any], branch: str, changed: list[str]) -> tuple[bool, list[str], str]:
    """Return (ok, unauthorized_paths, reason). Fails closed on identity errors."""
    try:
        task = identify_active_task(registry, branch)
    except OwnershipError as exc:
        return (False, list(changed), str(exc))
    allowed = allowed_paths_for_task(task)
    unauthorized = find_unauthorized(changed, allowed)
    if unauthorized:
        return (False, unauthorized, f"paths outside task '{task.get('task_id')}' envelope")
    return (True, [], f"all paths within task '{task.get('task_id')}' envelope")


def validate_changed_handoffs(changed: list[str]) -> list[str]:
    """Schema-validate each changed governed handoff. Returns list of failure messages."""
    handoffs = [p for p in governed_handoff_files(changed) if (ROOT / p).exists()]
    if not handoffs:
        return []
    import validate_multi_agent_governance as gov  # importable; no side effects

    schema = gov.load_json("trace/schemas/agent_handoff.schema.json")
    registry = gov.load_yaml(SELF_REGISTRATION_PATH)
    vocab = registry["status_vocabulary"]
    failures: list[str] = []
    for path in handoffs:
        try:
            handoff = gov.load_json(path)
            gov.validate_handoff(handoff, schema, vocab)
        except Exception as exc:  # AssertionError/KeyError/ValueError from the validator
            failures.append(f"{path}: {exc}")
    return failures


def resolve_branch(explicit: str | None) -> str:
    if explicit:
        return explicit
    env = os.environ.get("GITHUB_HEAD_REF") or os.environ.get("CF5_BRANCH")
    if env:
        return env
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=ROOT, text=True
        ).strip()
        return out
    except Exception:
        return ""


def changed_via_git(base: str) -> list[str]:
    out = subprocess.check_output(
        ["git", "diff", "--name-only", f"{base}...HEAD"], cwd=ROOT, text=True
    )
    return [line for line in out.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base")
    parser.add_argument("--branch")
    parser.add_argument("--paths", nargs="*")
    args = parser.parse_args()

    branch = resolve_branch(args.branch)
    if args.paths is not None:
        changed = args.paths
    elif args.base:
        changed = changed_via_git(args.base)
    else:
        parser.error("provide --base <ref> or --paths <files...>")

    registry = load_registry()
    ok, unauthorized, reason = evaluate(registry, branch, changed)
    if not ok:
        print(f"changed-path ownership: FAIL (branch='{branch}'): {reason}", file=sys.stderr)
        for p in unauthorized:
            print(f"  unauthorized changed path: {p}", file=sys.stderr)
        return 1

    handoff_failures = validate_changed_handoffs(changed)
    if handoff_failures:
        print("changed-path ownership: FAIL (governed handoff validation)", file=sys.stderr)
        for f in handoff_failures:
            print(f"  invalid handoff: {f}", file=sys.stderr)
        return 1

    print(
        f"changed-path ownership: PASS (branch='{branch}', {len(changed)} changed file(s) within the "
        f"accountable task envelope; {len(governed_handoff_files(changed))} governed handoff(s) validated)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
