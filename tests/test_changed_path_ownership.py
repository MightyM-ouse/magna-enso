#!/usr/bin/env python3
"""Adversarial tests for task-specific changed-path ownership (GOV-005-CF5 hardening).

Proves:
- task A cannot edit task B handoff/evidence paths,
- a change set cannot pass by combining writable paths from multiple tasks,
- broad governance directories do not bypass task-specific ownership,
- missing / ambiguous / inactive task identity fails closed,
- changed governed handoff files are detected for validation and arbitrary status is rejected,
- the real CF-5 task's own change set is authorized under the strict checker.

Runnable as `python tests/test_changed_path_ownership.py` (no pytest required) and via pytest.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_changed_path_ownership as own  # noqa: E402
import validate_multi_agent_governance as gov  # noqa: E402

VOCAB = ["PLANNED", "AUTHORIZED", "IN_PROGRESS", "BLOCKED", "PUSHED_FOR_REVIEW",
         "CHANGES_REQUIRED", "READY_FOR_PRODUCT_OWNER", "MERGED", "CLOSED"]


def _reg():
    return {
        "status_vocabulary": list(VOCAB),
        "active_tasks": [
            {"task_id": "TASK-A", "branch": "agent/task-a", "status": "IN_PROGRESS",
             "starting_commit": "a" * 40,
             "writable_paths": ["trace/evidence/TASK-A-HANDOFF.json", "docs/a/"]},
            {"task_id": "TASK-B", "branch": "agent/task-b", "status": "IN_PROGRESS",
             "starting_commit": "b" * 40,
             "writable_paths": ["trace/evidence/TASK-B-HANDOFF.json", "trace/reviews/TASK-B.md"]},
            {"task_id": "TASK-MERGED", "branch": "agent/task-merged", "status": "MERGED",
             "starting_commit": "c" * 40, "writable_paths": ["x/"]},
            {"task_id": "TASK-DUP1", "branch": "agent/dup", "status": "IN_PROGRESS",
             "starting_commit": "d" * 40, "writable_paths": ["y/"]},
            {"task_id": "TASK-DUP2", "branch": "agent/dup", "status": "IN_PROGRESS",
             "starting_commit": "e" * 40, "writable_paths": ["z/"]},
            {"task_id": "TASK-PHASE", "branch": "agent/phase", "status": "IN_PROGRESS",
             "starting_commit": "f" * 40, "writable_paths": ["trace/evidence/TASK-PHASE-HANDOFF.json"],
             "correction_phase_modifies": {"files": ["scripts/validate_multi_agent_governance.py"]}},
        ],
    }


def test_task_a_cannot_edit_task_b_handoff():
    ok, unauth, _ = own.evaluate(_reg(), "agent/task-a", ["trace/evidence/TASK-B-HANDOFF.json"])
    assert not ok and "trace/evidence/TASK-B-HANDOFF.json" in unauth


def test_cannot_combine_multiple_task_paths():
    ok, unauth, _ = own.evaluate(
        _reg(), "agent/task-a",
        ["trace/evidence/TASK-A-HANDOFF.json", "trace/evidence/TASK-B-HANDOFF.json"])
    assert not ok and unauth == ["trace/evidence/TASK-B-HANDOFF.json"]


def test_broad_governance_dir_does_not_bypass():
    # TASK-A does not own trace/reviews/; a broad reviews path must not pass.
    ok, unauth, _ = own.evaluate(_reg(), "agent/task-a", ["trace/reviews/anything.md"])
    assert not ok and "trace/reviews/anything.md" in unauth


def test_missing_identity_fails():
    ok, _, _ = own.evaluate(_reg(), "", ["docs/a/x"])
    assert not ok
    ok2, _, _ = own.evaluate(_reg(), "agent/does-not-exist", ["docs/a/x"])
    assert not ok2


def test_ambiguous_identity_fails():
    ok, _, reason = own.evaluate(_reg(), "agent/dup", ["y/file"])
    assert not ok and "ambiguous" in reason.lower()


def test_inactive_task_fails():
    ok, _, reason = own.evaluate(_reg(), "agent/task-merged", ["x/file"])
    assert not ok and "not active" in reason.lower()


def test_self_registration_allowed():
    ok, _, _ = own.evaluate(_reg(), "agent/task-a", ["trace/ACTIVE_WORK_REGISTRY.yaml"])
    assert ok


def test_correction_phase_modifies_allowed():
    ok, _, _ = own.evaluate(
        _reg(), "agent/phase", ["scripts/validate_multi_agent_governance.py"])
    assert ok
    # but a non-declared file is still rejected
    bad, _, _ = own.evaluate(_reg(), "agent/phase", ["scripts/check_changed_path_ownership.py"])
    assert not bad


def test_governed_handoff_detection():
    got = own.governed_handoff_files([
        "trace/evidence/X-HANDOFF.json", "trace/evidence/X-HANDOFF.md", "scripts/x.py"])
    assert got == ["trace/evidence/X-HANDOFF.json"]


def test_handoff_rejects_arbitrary_status():
    schema = gov.load_json("trace/schemas/agent_handoff.schema.json")
    handoff = gov.load_json("trace/evidence/GOV-005_HANDOFF.json")
    handoff = dict(handoff)
    handoff["task"] = dict(handoff["task"], status="WILD_STATUS")
    try:
        gov.validate_handoff(handoff, schema, VOCAB)
    except Exception:
        return  # expected: out-of-vocabulary status rejected
    raise AssertionError("arbitrary handoff status was not rejected")


def test_real_cf5_task_envelope_passes():
    reg = gov.load_yaml("trace/ACTIVE_WORK_REGISTRY.yaml")
    changed = [
        "scripts/check_changed_path_ownership.py",
        ".github/workflows/governance-validation.yml",
        "docs/governance/MULTI_AGENT_EXECUTION_POLICY.md",
        "trace/ACTIVE_WORK_REGISTRY.yaml",
        "tests/test_changed_path_ownership.py",
        "trace/tasks/GOV-005-CLAUDE-CF5-HARDENING.md",
        "trace/reviews/GOV-005-CF5-CORRECTION-REPORT.md",
        "trace/evidence/GOV-005-CF5-HANDOFF.md",
        "trace/evidence/GOV-005-CF5-HANDOFF.json",
    ]
    ok, unauth, reason = own.evaluate(reg, "claude/GOV-005-cf5-hardening", changed)
    assert ok, f"CF-5 envelope unexpectedly failed: {reason} {unauth}"


def _run() -> int:
    funcs = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failures = []
    for f in funcs:
        try:
            f()
            print(f"PASS {f.__name__}")
        except Exception as exc:  # noqa: BLE001
            failures.append((f.__name__, exc))
            print(f"FAIL {f.__name__}: {exc}")
    print(f"\n{len(funcs) - len(failures)}/{len(funcs)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(_run())
