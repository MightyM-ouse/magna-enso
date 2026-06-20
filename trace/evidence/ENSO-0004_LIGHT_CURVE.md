# Light Curve — ENSO-0004

Task ID: ENSO-0004
Feature ID: ENSO-F-0401
Sprint: Sprint 4 — Clean Governed Hermes Baseline Preparation
Mode History: bounded baseline preparation → validation → human acceptance
Evidence Level: Full
Date: 2026-06-20
Worker(s): Codex (baseline preparation) · Antigravity (validation) · Human owner (acceptance)

---

## Goal

Prepare a clean, governed, inert Hermes-derived baseline under strict Sprint 4 boundaries. This is baseline preparation only: no runtime activation, no policy engine, no Hermes run/build, no dependency install, no Sprint 5 work.

## Status

**ACCEPTED / DONE** — human-approved on 2026-06-20 as an inert, quarantined provenance baseline only.

## Source

- Hermes repository: `https://github.com/nousresearch/hermes-agent`
- Approved/audited SHA: `33b1d144590a211100f42aa911fd7f91ba031507`
- Local source path: `/Users/vinay/Projects/AI/Magna/_scratch/hermes-readonly-audit/hermes-clone/`
- Branch used: `audit/sprint-4-governed-hermes-baseline`

## Files Created In Repo

| File | Purpose |
|---|---|
| `vendor/hermes/README.md` | Quarantine/no-runtime documentation. |
| `vendor/hermes/UPSTREAM_LICENSE.txt` | Upstream MIT license preservation. |
| `vendor/hermes/provenance/UPSTREAM_PYPROJECT.toml.source.txt` | Inert upstream Python manifest reference. |
| `vendor/hermes/provenance/UPSTREAM_PACKAGE.json.source.txt` | Inert upstream Node manifest reference. |
| `vendor/hermes/retained/README.md` | Retained-state metadata documentation. |
| `vendor/hermes/retained/RETAINED_SURFACE_STATES.yaml` | Sprint 3 surface-state metadata. |
| `trace/evidence/ENSO-0004_LIGHT_CURVE.md` | This IN_REVIEW evidence package. |

## Trace Files Modified

- `trace/FEATURE_TRACKER.md`
- `trace/STAR_MAP.md`
- `trace/DECISION_LOG.md`
- `trace/RISK_REGISTER.md`

## Local-Only Reports Created

Reports under `../../ChatGPTReview/sprint-4-governed-hermes-baseline/`:

- `PRE_IMPLEMENTATION_REPORT.md`
- `HERMES_SOURCE_PROVENANCE_MANIFEST.md`
- `SOURCE_IMPORT_INVENTORY.md`
- `REMOVED_SURFACES_REPORT.md`
- `DISABLED_SURFACES_REPORT.md`
- `RETAINED_SURFACES_REPORT.md`
- `LICENSE_AND_DEPENDENCY_BASELINE.md`
- `NO_NETWORK_VALIDATION.md`
- `DEFAULT_DENY_BASELINE_REPORT.md`
- `SPRINT_4_LIGHT_CURVE.md`
- `FINAL_RECOMMENDATION.md`

## Validation Results

| Check | Result |
|---|---|
| Isolated branch used | PASS |
| Approved SHA used | PASS |
| Hermes run/build avoided | PASS |
| Dependencies not installed | PASS |
| No runtime execution | PASS |
| No policy engine code | PASS |
| No Sprint 5 work | PASS |
| EH-0005B remains PROPOSED | PASS |
| Hermes Agent not activated | PASS |
| Imported baseline inert/quarantined | PASS |
| Dangerous surfaces excluded | PASS |
| Static license/dependency review completed before import | PASS |
| Antigravity validation | PASS — ACCEPTED_FOR_HUMAN_REVIEW, 9.8/10, no blocking issues, no required corrections |
| Human owner acceptance | PASS — accepted 2026-06-20 |
| Sprint 4 status | ACCEPTED / DONE — inert baseline only |
| Sprint 5 status | NOT STARTED |

## Findings

- `vendor/hermes/` contains no executable Hermes Python modules.
- Active package manifests are not imported; upstream manifests are `.source.txt` reference files.
- No Hermes runtime directories such as `agent/`, `tools/`, `cron/`, `gateway/`, `plugins/`, or `providers/` are imported.
- Dangerous surfaces are removed by non-import.
- Retained surfaces are metadata-only state records for future governed wiring.
- Runtime enforcement does not exist.

## Risks

- R-01 remains OPEN: Hermes reuse is still a coupling risk.
- R-02 remains OPEN: this was a static baseline review, not a full transitive dependency scan.
- R-06 remains OPEN: no runtime policy engine exists.
- Future executable source import requires separate approval, dependency review, and policy implementation.

## Human Authority Statement

Codex does not self-approve. Antigravity provided validation input only. The human owner (Vinay) explicitly accepted Sprint 4 and remains final authority under EH-0010.

## Antigravity Validation Outcome

- Verdict: **ACCEPTED_FOR_HUMAN_REVIEW**
- Rating: **9.8/10**
- Blocking issues: none
- Required corrections: none
- Recommended corrections: none
- Informational note: `browser_snapshot_model` state `read_only_if_privacy_gated` is correct and requires no action.
- Local-only validation package: `../../ChatGPTReview/sprint-4-antigravity-validation/`

## Acceptance Boundary

- Acceptance covers only the inert, quarantined Sprint 4 provenance baseline.
- No runtime enforcement or policy engine exists.
- No Hermes activation, run, build, dependency installation, or additional source import is authorized.
- R-06 remains OPEN.
- EH-0005B remains PROPOSED.
- Sprint 5 remains NOT STARTED.

## Final Status

**DONE — human-accepted on 2026-06-20 as an inert baseline only.**

## Next Steps

1. Commit the accepted Sprint 4 baseline and closeout only after separate explicit human commit approval.
2. Do not start Sprint 5 or implement a policy engine without separate approval.
3. Do not push or merge without separate explicit human instruction.
