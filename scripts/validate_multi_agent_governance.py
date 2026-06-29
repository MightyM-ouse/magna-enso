#!/usr/bin/env python3
"""Validate GOV-005 multi-agent governance contracts without network access.

Corrections (GOV-005-CLAUDE-CORRECTIONS):
- CF-3/CF-4: task/registry status is constrained to one governed vocabulary, and the
  schema enum is cross-checked against that vocabulary (single source of truth).
- CF-6: provenance distinguishes the intended reviewer from a completed review; a handoff
  may not claim a completed review before evidence exists.
- CF-2: the live GitHub branch head is the synchronization authority; commit fields are
  truthful and never required to self-reference.
Companion: scripts/check_changed_path_ownership.py provides the git-aware changed-path
ownership check (CF-5 / AC #8); it is intentionally separate because it needs git.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - explicit environment failure
    raise SystemExit(
        "PyYAML is required by the repository governance validator. "
        "Install it with: python3 -m pip install -r scripts/governance-requirements.txt"
    ) from exc


ROOT = Path(__file__).resolve().parents[1]
SHA = re.compile(r"^[0-9a-f]{40}$")

REQUIRED_GOVERNANCE_FILES = [
    "AGENTS.md",
    "docs/governance/MULTI_AGENT_EXECUTION_POLICY.md",
    "trace/ACTIVE_WORK_REGISTRY.yaml",
    "trace/schemas/agent_handoff.schema.json",
    "scripts/validate_multi_agent_governance.py",
    "scripts/check_changed_path_ownership.py",
]


def fail(message: str) -> None:
    raise AssertionError(message)


def load_json(path: str) -> Any:
    with (ROOT / path).open(encoding="utf-8") as handle:
        return json.load(handle)


def load_yaml(path: str) -> Any:
    with (ROOT / path).open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def require_text(path: str, tokens: list[str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    missing = [token for token in tokens if token not in text]
    if missing:
        fail(f"{path} missing required tokens: {missing}")


def validate_schema_shape(schema: dict[str, Any], status_vocabulary: list[str]) -> None:
    required = set(schema.get("required", []))
    expected = {
        "task",
        "provenance",
        "repository_state",
        "synchronization",
        "outcome",
        "changes",
        "downloads",
        "validation",
        "deviations",
        "impacts",
        "decisions_required",
        "recommended_next_action",
    }
    if not expected.issubset(required):
        fail(f"handoff schema missing required keys: {sorted(expected - required)}")
    # CF-4: the schema task-status enum must equal the governed vocabulary (single source).
    schema_enum = schema["$defs"]["task_status"]["enum"]
    if schema_enum != status_vocabulary:
        fail(
            "schema task_status enum must equal ACTIVE_WORK_REGISTRY status_vocabulary; "
            f"schema={schema_enum} registry={status_vocabulary}"
        )
    # CF-6: provenance must require intended_reviewer + review_status, not a bare reviewed_by.
    prov_required = set(schema["properties"]["provenance"]["required"])
    if "reviewed_by" in prov_required:
        fail("provenance must not require 'reviewed_by'; use intended_reviewer + review_status (CF-6)")
    if not {"intended_reviewer", "review_status", "review_completed_by"}.issubset(prov_required):
        fail("provenance must require intended_reviewer, review_status, review_completed_by (CF-6)")


def validate_handoff(handoff: dict[str, Any], schema: dict[str, Any], status_vocabulary: list[str]) -> None:
    missing = [key for key in schema["required"] if key not in handoff]
    if missing:
        fail(f"handoff missing required keys: {missing}")
    if handoff["schema_version"] != "1.0":
        fail("handoff schema_version must be 1.0")
    # CF-3/CF-4: task status must be in the governed vocabulary.
    if handoff["task"]["status"] not in status_vocabulary:
        fail(f"handoff task.status '{handoff['task']['status']}' not in governed vocabulary")
    if handoff["synchronization"]["verdict"] != "SYNC_PASS":
        fail("published implementation handoff must record SYNC_PASS")
    # CF-6: provenance distinguishes intended reviewer from completed review.
    prov = handoff["provenance"]
    if prov.get("instruction_prepared_by") != "ChatGPT / System Architect":
        fail("provenance instruction_prepared_by must be 'ChatGPT / System Architect'")
    if prov.get("instruction_approved_by") != "Product Owner":
        fail("provenance instruction_approved_by must be 'Product Owner'")
    if prov.get("intended_reviewer") != "ChatGPT / System Architect":
        fail("provenance intended_reviewer must be 'ChatGPT / System Architect'")
    if prov.get("review_status") not in {"PENDING", "COMPLETED"}:
        fail("provenance review_status must be PENDING or COMPLETED")
    if "reviewed_by" in prov:
        fail("provenance must not assert reviewed_by before review (CF-6)")
    completed_by = prov.get("review_completed_by")
    if prov["review_status"] == "PENDING" and completed_by is not None:
        fail("review_completed_by must be null while review_status is PENDING")
    if prov["review_status"] == "COMPLETED" and not completed_by:
        fail("review_completed_by must name the reviewer when review_status is COMPLETED")
    # CF-2: commit fields are truthful; the live branch head is the authority, not these fields.
    if not SHA.fullmatch(handoff["repository_state"]["starting_commit"]):
        fail("handoff starting_commit is not a full SHA")
    final = handoff["repository_state"]["final_commit"]
    if final is not None and not SHA.fullmatch(final):
        fail("handoff final_commit is not null or a full SHA")
    for download in handoff["downloads"]:
        required_download = {
            "source_url", "publisher", "purpose", "version", "destination",
            "size_bytes", "sha256", "license", "executed", "security_checks",
            "resulting_changes",
        }
        if not required_download.issubset(download):
            fail("download entry is missing provenance fields")


def validate_active_work(registry: dict[str, Any], status_vocabulary: list[str]) -> None:
    tasks = registry.get("active_tasks", [])
    ids = [task["task_id"] for task in tasks]
    branches = [task["branch"] for task in tasks]
    if len(ids) != len(set(ids)):
        fail("active-work task IDs must be unique")
    if len(branches) != len(set(branches)):
        fail("active-work branches must be unique")
    for task in tasks:
        if not SHA.fullmatch(task["starting_commit"]):
            fail(f"{task['task_id']} starting_commit must be a full SHA")
        if not task.get("writable_paths"):
            fail(f"{task['task_id']} must declare writable paths")
        # CF-3/CF-4: each task status must be in the governed vocabulary.
        if "status" in task and task["status"] not in status_vocabulary:
            fail(f"{task['task_id']} status '{task['status']}' not in governed vocabulary")
    for index, left in enumerate(tasks):
        for right in tasks[index + 1 :]:
            overlap = set(left["writable_paths"]) & set(right["writable_paths"])
            if overlap:
                declared = set(left.get("shared_paths", [])) & set(right.get("shared_paths", []))
                if not overlap.issubset(declared):
                    fail(
                        f"undeclared writable overlap between {left['task_id']} and "
                        f"{right['task_id']}: {sorted(overlap - declared)}"
                    )


def main() -> int:
    schema = load_json("trace/schemas/agent_handoff.schema.json")
    handoff = load_json("trace/evidence/GOV-005_HANDOFF.json")
    workflows = load_yaml("trace/WORKFLOWS.yaml")
    roles = load_yaml("trace/ROLE_REGISTRY.yaml")
    active = load_yaml("trace/ACTIVE_WORK_REGISTRY.yaml")
    index = load_json("trace/CELESTIAL_INDEX.json")

    status_vocabulary = active["status_vocabulary"]

    validate_schema_shape(schema, status_vocabulary)
    validate_handoff(handoff, schema, status_vocabulary)
    validate_active_work(active, status_vocabulary)

    outcomes = set(workflows["synchronization_gate"]["outcomes"])
    if outcomes != {"SYNC_PASS", "SYNC_BLOCKED", "SYNC_UNVERIFIED_LOCAL_STATE"}:
        fail("workflow synchronization outcomes are incomplete")
    if workflows["git"]["merge_authority"] != "product_owner":
        fail("workflow merge authority must remain Product Owner")
    if roles["meta"]["final_authority"] != "product_owner":
        fail("role registry final authority must remain Product Owner")
    if roles["roles"]["governed_runtime_experiment"]["status"] != "inactive":
        fail("GOV-005 must not activate Hermes")

    # CF-1: required GOV-005 governance files must exist (mirrored in CI).
    for path in REQUIRED_GOVERNANCE_FILES:
        if not (ROOT / path).exists():
            fail(f"required governance file missing: {path}")

    require_text(
        "AGENTS.md",
        [
            "SYNC_PASS",
            "SYNC_BLOCKED",
            "SYNC_UNVERIFIED_LOCAL_STATE",
            "precise outcome, bounded authority, independent method",
            "APPROVE_TO_MERGE",
            "CHANGES_REQUIRED",
        ],
    )
    require_text(
        "docs/governance/MULTI_AGENT_EXECUTION_POLICY.md",
        ["Immutable execution authority", "Downloads and dependencies", "Four-eyes rule"],
    )
    for adapter in ["CHATGPT.md", "CODEX.md", "CLAUDE.md", "ANTIGRAVITY.md", "HERMES.md"]:
        require_text(adapter, ["AGENTS.md"])

    routed = index["areas"]["trace-governance"]["source_files"]
    for path in [
        "trace/ACTIVE_WORK_REGISTRY.yaml",
        "docs/governance/MULTI_AGENT_EXECUTION_POLICY.md",
        "trace/templates/",
        "trace/schemas/",
    ]:
        if path not in routed:
            fail(f"Celestial Index does not route canonical governance path: {path}")

    print("GOV-005 governance validation: PASS")
    print(f"active tasks validated: {len(active['active_tasks'])}")
    print(f"governed status vocabulary: {len(status_vocabulary)} values (schema enum matches)")
    print("handoff schema, status vocabulary, and provenance contract: PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, TypeError, ValueError) as exc:
        print(f"GOV-005 governance validation: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
