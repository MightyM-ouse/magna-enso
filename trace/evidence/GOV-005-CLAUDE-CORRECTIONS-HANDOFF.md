# GOV-005-CLAUDE-CORRECTIONS Agent Handoff

## Provenance

- Instruction prepared by: ChatGPT / System Architect
- Instruction approved by: Product Owner
- Intended reviewer: ChatGPT / System Architect (independent validator after correction: Antigravity)
- Review status: `PENDING` (no post-correction review has occurred yet — CF-6)
- Review completed by: null
- Agent and role: `claude / correction_implementer`

## Identity and state

| Field | Value |
|---|---|
| Task | `GOV-005` (correction packet `GOV-005-CLAUDE-CORRECTIONS`) |
| Status | `PUSHED_FOR_REVIEW` (governed vocabulary) |
| Branch | `claude/GOV-005-corrections` |
| Starting commit | `2796b4aac9ac32f49d8a5e95f558c161c02d953f` |
| Final commit (pre-handoff) | null (live branch head is authoritative — CF-2) |
| Synchronization authority | live GitHub branch head |
| Pull request | draft correction PR targeting `codex/GOV-005-multi-agent-governance` (URL in chat) |
| Synchronization verdict | `SYNC_PASS` |

## Outcome

Resolved CF-1 through CF-6 (plus related nonblocking weaknesses) from the merged Claude four-eyes review.
Full finding→correction matrix and proofs: `trace/reviews/GOV-005-CLAUDE-CORRECTIONS-MATRIX.md`.

- **CF-1:** CI now runs the substantive validator (pinned PyYAML) and a git-aware ownership check, on the main
  PR and stacked correction/review PRs; required-files check extended to GOV-005 canonical files.
- **CF-2:** live branch head is the synchronization authority; commit fields are point-in-time, never
  self-referential.
- **CF-3/CF-4:** one governed status vocabulary; schema enum equals it; validator rejects out-of-vocabulary status.
- **CF-5:** GOV-005 handoff files added to ownership; git-aware check fails on any unauthorized changed path.
- **CF-6:** provenance distinguishes intended reviewer from completed review; no artifact claims a completed
  review before evidence.

## Method and rationale

Inspected the merged review baseline, then changed only authorized governance contract files. Chose a separate
git-aware ownership script (the pure-file validator cannot diff) and a single governed status vocabulary as the
source of truth for both schema and validator. Existing Claude review findings were preserved unchanged.

## Changes

New (exclusive): `scripts/check_changed_path_ownership.py`, `scripts/governance-requirements.txt`,
`trace/reviews/GOV-005-CLAUDE-CORRECTIONS-MATRIX.md`, `trace/evidence/GOV-005-CLAUDE-CORRECTIONS-HANDOFF.md/.json`.
Corrected (authorized GOV-005-owned governance files): `.github/workflows/governance-validation.yml`,
`scripts/validate_multi_agent_governance.py`, `trace/schemas/agent_handoff.schema.json`,
`docs/governance/MULTI_AGENT_EXECUTION_POLICY.md`, `trace/templates/AGENT_HANDOFF_TEMPLATE.md`,
`trace/ACTIVE_WORK_REGISTRY.yaml`, `trace/evidence/GOV-005_HANDOFF.json/.md`, `trace/evidence/GOV-005_LIGHT_CURVE.md`.

## Downloads and dependencies

| Source | Purpose | Version | Destination | SHA-256 | License | Executed | Security checks | Resulting changes |
|---|---|---|---|---|---|---|---|---|
| PyPI PyYAML | parse governance YAML in validator | 6.0.2 | isolated venv `/tmp/gov005venv` (not committed) | n/a (wheel from PyPI) | MIT | imported (not executed as a program) | pinned version; isolated venv; declared in `scripts/governance-requirements.txt` | added `scripts/governance-requirements.txt` |

## Validation

| Check | Command | Result |
|---|---|---|
| Governance validator (positive) | `python3 scripts/validate_multi_agent_governance.py` | PASS (4 tasks; enum matches) |
| Negative N1 (status vocab) | mutated handoff | FAIL exit 1 (expected) |
| Negative N2 (legacy provenance) | mutated handoff | FAIL exit 1 (expected) |
| Negative N3 (review before evidence) | mutated handoff | FAIL exit 1 (expected) |
| Negative N4 (forbidden path) | `check_changed_path_ownership.py` | FAIL exit 1 (expected) |
| Positive N5 (governance paths) | `check_changed_path_ownership.py` | PASS exit 0 |
| Working-tree ownership | `check_changed_path_ownership.py --paths <changed>` | PASS |
| GitHub CI | governance workflow on the correction PR | recorded on PR after push |

## Deviations and decisions

- A narrowly scoped governance dependency (PyYAML 6.0.2) was added per the packet, pinned and isolated.
- No correction touched the immutable task packet or the merged Claude review evidence (preserved).
- Decisions required: ChatGPT/Product Owner accept the correction set; schedule **Antigravity** independent
  validation; Product Owner merge decision. Claude does not approve its own corrections.

## Architecture, security, and integration impact

Governance/CI contract only; no runtime/product/Sprint-5/Hermes/HELIX/SGN-01/ARCH-001/GOV-006 change. Security
posture strengthened (enforcement now actually runs; ownership and provenance are machine-checked) without
altering `main` branch protection. Integration: correction PR stacks on the GOV-005 implementation branch;
ARCH-001 still resynchronizes after GOV-005.

## Recommended next action

Antigravity performs independent validation of the corrections from a separate context; ChatGPT reviews and the
Product Owner decides the merge. Do not merge until independent validation and Product Owner approval. This
handoff claims no acceptance or merge approval.

The companion JSON `trace/evidence/GOV-005-CLAUDE-CORRECTIONS-HANDOFF.json` conforms to
`trace/schemas/agent_handoff.schema.json`.
