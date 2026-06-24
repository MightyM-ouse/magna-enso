# GOV-005 — Claude Correction Matrix (CF-1 … CF-6)

## Provenance and scope

- Correction task: `GOV-005-CLAUDE-CORRECTIONS` (packet `trace/tasks/GOV-005-CLAUDE-CORRECTIONS.md`)
- Instruction prepared by: ChatGPT / System Architect — approved by: Product Owner (Vinay)
- Implementer: Claude (correction implementer — **not** the independent validator)
- Independent validator after correction: **Antigravity**
- Branch: `claude/GOV-005-corrections`, created from verified implementation head `2796b4a`
- Correction PR base: `codex/GOV-005-multi-agent-governance` — **do not merge; do not self-approve**

## Synchronization verdict — `SYNC_PASS`
PR #16 (Claude review) **MERGED** into the implementation branch; PR #13 **open/draft**; implementation head
`2796b4a` contains this corrections packet and is **not** behind `main`; no existing correction branch/PR.

## Finding → correction matrix

| Finding | Correction | Files | Proof |
|---|---|---|---|
| **CF-1** validator not enforced by CI | CI now installs a pinned dependency and runs `validate_multi_agent_governance.py`; required-files check extended to GOV-005 canonical files; trigger broadened to stacked correction/review PR bases (no `main`-protection change) | `.github/workflows/governance-validation.yml`, `scripts/governance-requirements.txt` | validator step + `--require-hashes` pinned `PyYAML==6.0.2`; AC #1/#2/#3 |
| **CF-2** commit-pointer drift / impossible self-reference | Live GitHub branch head declared the synchronization authority; `final_commit`/`latest_known_commit` redefined as point-in-time pointers (schema description, policy, registry notes); stale `latest_known_commit` refreshed to the truthful pre-correction head | schema, `MULTI_AGENT_EXECUTION_POLICY.md`, `ACTIVE_WORK_REGISTRY.yaml`, `GOV-005_HANDOFF.md/.json` | AC #4 |
| **CF-3** status disagreement | One canonical live status authority (registry) with explicit roles for packet/Star Map/handoff; all aligned to the governed vocabulary | `ACTIVE_WORK_REGISTRY.yaml` (`status_authority`), policy, `GOV-005_HANDOFF.*` | AC #5 |
| **CF-4** unconstrained `task.status` | Schema `task.status` now an enum = `$defs/task_status`; validator cross-checks the schema enum **equals** the registry `status_vocabulary` and that every task/handoff status is in-vocabulary | `agent_handoff.schema.json`, `validate_multi_agent_governance.py` | negative test N1; AC #6/#7 |
| **CF-5** handoff files outside ownership | GOV-005 `writable_paths` now include `GOV-005_HANDOFF.json/.md`; new git-aware `check_changed_path_ownership.py` fails on any changed path outside declared ownership + governance allowlist, wired into CI | registry, `scripts/check_changed_path_ownership.py`, workflow | negative test N4; positive N5; AC #8 |
| **CF-6** provenance claims review before it occurs | Provenance replaces `reviewed_by` with `intended_reviewer` + `review_status` (`PENDING`/`COMPLETED`) + `review_completed_by`; schema and validator forbid asserting a completed review without a named reviewer | schema, validator, policy, template, `GOV-005_HANDOFF.*` | negative tests N2, N3; AC #9 |

Related nonblocking weaknesses also addressed: validator dependency reproducibility (pinned
`governance-requirements.txt`, NB-1); git-aware changed-path enforcement (CF-5/NB-3); commit
self-reference semantics (CF-2/NB-2); stacked-PR validation without weakening `main` (CF-1).

## Validation evidence (exact; local)

| Check | Command | Result |
|---|---|---|
| Governance validator (positive) | `python3 scripts/validate_multi_agent_governance.py` | PASS — 4 active tasks; schema enum matches 9-value vocabulary |
| N1 out-of-vocabulary `task.status` | mutated handoff | FAIL (exit 1) — "not in governed vocabulary" |
| N2 legacy `reviewed_by` provenance | mutated handoff | FAIL (exit 1) — provenance contract rejected |
| N3 `COMPLETED` review without reviewer | mutated handoff | FAIL (exit 1) — "review_completed_by must name the reviewer" |
| N4 forbidden runtime changed path | `check_changed_path_ownership.py --paths src/runtime/app.py …` | FAIL (exit 1) — unauthorized path |
| N5 governance-only changed paths | `check_changed_path_ownership.py --paths …governance…` | PASS (exit 0) |
| JSON/YAML parse | `python3 json.load`, `ruby -ryaml` | PASS |

Local validator dependency: **PyYAML 6.0.2** installed into an isolated venv (`/tmp/gov005venv`); source
PyPI; license MIT; not committed to the repo. CI installs the same pinned version from
`scripts/governance-requirements.txt`. GitHub CI result for this branch is recorded on the correction PR.

## Boundaries honored
No merge, no self-approval. Push only to `claude/GOV-005-corrections`. Not modified: `trace/tasks/GOV-005.md`
(immutable), the merged Claude review report/handoffs (historical evidence — preserved unchanged, AC #10),
GOV-006, runtime/product code, ARCH-001, Sprint 5, Hermes activation, HELIX, SGN-01. Independent validation is
delegated to Antigravity; Claude does not approve its own corrections.

## Residual risks / decisions required
- The git-aware ownership check uses the union of declared ownership plus a governance allowlist; tightening it
  to strict per-branch task ownership is a possible future hardening.
- Product Owner / ChatGPT decisions: accept the correction set; schedule Antigravity independent validation;
  the Q1 namespace-exception and merge decisions from the review remain open.
