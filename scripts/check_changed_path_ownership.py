#!/usr/bin/env python3
"""Git-aware changed-path ownership check (GOV-005-CLAUDE-CORRECTIONS, CF-5 / AC #8).

Detects changed files that fall outside declared ownership. A changed path is authorized
only if it is covered by:
  - the union of every active task's `writable_paths` + `shared_paths` in
    trace/ACTIVE_WORK_REGISTRY.yaml; or
  - the governance allowlist below (control files that govern the contract itself and the
    per-task packets/evidence namespaces that workers legitimately add).

This does not weaken protected-`main`; it only flags unauthorized paths (for example, a
runtime/product or ARCH-001 change appearing on a governance branch).

Usage:
  check_changed_path_ownership.py --base <ref>     # diff <ref>...HEAD via git
  check_changed_path_ownership.py --paths a b c     # explicit list (for negative tests)
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required. Install: python3 -m pip install -r scripts/governance-requirements.txt"
    ) from exc

ROOT = Path(__file__).resolve().parents[1]

# Governance control + per-task namespaces that workers may legitimately change.
GOVERNANCE_ALLOWLIST = [
    ".github/workflows/governance-validation.yml",
    "scripts/validate_multi_agent_governance.py",
    "scripts/check_changed_path_ownership.py",
    "scripts/governance-requirements.txt",
    "docs/governance/",
    "trace/schemas/",
    "trace/templates/",
    "trace/reviews/",
    "trace/tasks/",
    "trace/evidence/",
    "trace/ACTIVE_WORK_REGISTRY.yaml",
    "trace/CELESTIAL_INDEX.json",
    "trace/DECISION_LOG.md",
    "trace/ROLE_REGISTRY.yaml",
    "trace/WORKFLOWS.yaml",
    "trace/STAR_MAP.md",
    "AGENTS.md", "CHATGPT.md", "CODEX.md", "CLAUDE.md", "ANTIGRAVITY.md", "HERMES.md",
]


def allowed_prefixes() -> list[str]:
    registry = yaml.safe_load((ROOT / "trace/ACTIVE_WORK_REGISTRY.yaml").read_text(encoding="utf-8"))
    allowed: set[str] = set(GOVERNANCE_ALLOWLIST)
    for task in registry.get("active_tasks", []):
        allowed.update(task.get("writable_paths", []))
        allowed.update(task.get("shared_paths", []))
    return sorted(allowed)


def is_covered(path: str, allowed: list[str]) -> bool:
    for entry in allowed:
        if entry.endswith("/") and path.startswith(entry):
            return True
        if path == entry:
            return True
    return False


def changed_via_git(base: str) -> list[str]:
    out = subprocess.check_output(
        ["git", "diff", "--name-only", f"{base}...HEAD"], cwd=ROOT, text=True
    )
    return [line for line in out.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base")
    parser.add_argument("--paths", nargs="*")
    args = parser.parse_args()

    if args.paths is not None:
        changed = args.paths
    elif args.base:
        changed = changed_via_git(args.base)
    else:
        parser.error("provide --base <ref> or --paths <files...>")

    allowed = allowed_prefixes()
    unauthorized = [p for p in changed if not is_covered(p, allowed)]
    if unauthorized:
        print("changed-path ownership: FAIL", file=sys.stderr)
        for p in unauthorized:
            print(f"  unauthorized changed path (outside declared ownership): {p}", file=sys.stderr)
        return 1
    print(f"changed-path ownership: PASS ({len(changed)} changed file(s) all within declared ownership)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
