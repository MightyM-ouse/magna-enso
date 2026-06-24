# Sprint 4 Light Curve

## Purpose

Record Sprint 4 bounded baseline-preparation evidence. This is an IN_REVIEW package, not acceptance.

## Honesty Statement

This baseline is structurally safe / not runtime-enforced. Retained risky capabilities remain disabled until Sprint 5. No Hermes runtime, build, package script, or dependency install was performed.

## Task Metadata

- Feature ID: `ENSO-F-0401`
- Sprint: Sprint 4
- Mode: Bounded baseline preparation
- Branch: `audit/sprint-4-governed-hermes-baseline`
- Status: `IN_REVIEW`
- Human acceptance: pending
- Proposed validation worker: Antigravity

## Source

- Hermes repo: `https://github.com/nousresearch/hermes-agent`
- Approved/audited SHA: `33b1d144590a211100f42aa911fd7f91ba031507`
- Source path used: `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/`

## Files Created In Repository

- `vendor/hermes/README.md`
- `vendor/hermes/UPSTREAM_LICENSE.txt`
- `vendor/hermes/provenance/UPSTREAM_PYPROJECT.toml.source.txt`
- `vendor/hermes/provenance/UPSTREAM_PACKAGE.json.source.txt`
- `vendor/hermes/retained/README.md`
- `vendor/hermes/retained/RETAINED_SURFACE_STATES.yaml`
- `trace/evidence/ENSO-0004_LIGHT_CURVE.md`

## Trace Files Modified

- `trace/FEATURE_TRACKER.md`
- `trace/STAR_MAP.md`
- `trace/RISK_REGISTER.md`

## Local-Only Reports Created

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
| No push | PASS |
| Hermes not run | PASS |
| Hermes not built | PASS |
| No dependencies installed | PASS |
| No runtime execution | PASS |
| No policy engine code | PASS |
| No Sprint 5 work | PASS |
| EH-0005B remains PROPOSED | PASS |
| Hermes Agent not activated | PASS |
| Imported source inert/quarantined | PASS |
| Dangerous surfaces removed/excluded | PASS |
| Static license/dependency review before import | PASS |
| Sprint 4 remains IN_REVIEW, not DONE | PASS |

## Recommendation

Send this Sprint 4 baseline to Antigravity for validation. Do not commit, push, merge, or mark DONE without separate human approval.
