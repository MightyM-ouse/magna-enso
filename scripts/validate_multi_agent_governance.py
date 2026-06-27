#!/usr/bin/env python3
"""Validate GOV-005 multi-agent governance contracts without network access."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - explicit environment failure
    raise SystemExit("PyYAML is required by the repository governance validator") from exc


ROOT = Path(__file__).resolve().parents[1]


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


def validate_schema_shape(schema: dict[str, Any]) -> None:
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


def validate_handoff(handoff: dict[str, Any], schema: dict[str, Any]) -> None:
    missing = [key for key in schema["required"] if key not in handoff]
    if missing:
        fail(f"handoff missing required keys: {missing}")
    if handoff["schema_version"] != "1.0":
        fail("handoff schema_version must be 1.0")
    if handoff["synchronization"]["verdict"] != "SYNC_PASS":
        fail("published implementation handoff must record SYNC_PASS")
    if handoff["provenance"] != {
        "instruction_prepared_by": "ChatGPT / System Architect",
        "instruction_approved_by": "Product Owner",
        "reviewed_by": "ChatGPT / System Architect",
    }:
        fail("handoff provenance contract does not match policy")
    sha = re.compile(r"^[0-9a-f]{40}$")
    if not sha.fullmatch(handoff["repository_state"]["starting_commit"]):
        fail("handoff starting_commit is not a full SHA")
    final = handoff["repository_state"]["final_commit"]
    if final is not None and not sha.fullmatch(final):
        fail("handoff final_commit is not null or a full SHA")
    for download in handoff["downloads"]:
        required_download = {
            "source_url", "publisher", "purpose", "version", "destination",
            "size_bytes", "sha256", "license", "executed", "security_checks",
            "resulting_changes",
        }
        if not required_download.issubset(download):
            fail("download entry is missing provenance fields")


def validate_active_work(registry: dict[str, Any]) -> None:
    tasks = registry.get("active_tasks", [])
    ids = [task["task_id"] for task in tasks]
    branches = [task["branch"] for task in tasks]
    if len(ids) != len(set(ids)):
        fail("active-work task IDs must be unique")
    if len(branches) != len(set(branches)):
        fail("active-work branches must be unique")
    for task in tasks:
        if not re.fullmatch(r"[0-9a-f]{40}", task["starting_commit"]):
            fail(f"{task['task_id']} starting_commit must be a full SHA")
        if not task.get("writable_paths"):
            fail(f"{task['task_id']} must declare writable paths")
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

    validate_schema_shape(schema)
    validate_handoff(handoff, schema)
    validate_active_work(active)

    outcomes = set(workflows["synchronization_gate"]["outcomes"])
    if outcomes != {"SYNC_PASS", "SYNC_BLOCKED", "SYNC_UNVERIFIED_LOCAL_STATE"}:
        fail("workflow synchronization outcomes are incomplete")
    if workflows["git"]["merge_authority"] != "product_owner":
        fail("workflow merge authority must remain Product Owner")
    if roles["meta"]["final_authority"] != "product_owner":
        fail("role registry final authority must remain Product Owner")
    if roles["roles"]["governed_runtime_experiment"]["status"] != "inactive":
        fail("GOV-005 must not activate Hermes")

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
    print("handoff schema and representative handoff: PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, TypeError, ValueError) as exc:
        print(f"GOV-005 governance validation: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
