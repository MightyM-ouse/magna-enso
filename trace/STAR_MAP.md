# Star Map - Current Project State

Last governance review: 2026-06-24

| Field | Current state |
|---|---|
| Repository | `MightyM-ouse/magna-enso` |
| Accepted `main` baseline | `af8c73a` - GOV-002 accepted and squash-merged through PR #5 |
| Delivery state | Sprints 1-4 accepted; Sprint 4 inert provenance baseline only |
| Sprint 5 | Untracked local `policy/`, `tests/`, and ENSO-0005 evidence; not accepted |
| Policy engine | Selection and integration strategy open |
| Runtime enforcement | Not confirmed on `main` |
| Hermes capabilities | Inactive; capability lab not yet authorized |
| Architecture package | Corrected package accepted as migration input; repository integration pending |
| Diagram package | Editable package prepared; repository integration pending |
| ChatGPT project source | GOV-002 four-file GitHub-first replacement accepted |
| TRACE | Applied instance current; GOV-001 and GOV-002 complete |
| SGN-01 | Blocked |
| Product authority | Product Owner |

## Accepted evidence

- `trace/evidence/ENSO-0001_LIGHT_CURVE.md`
- `trace/evidence/ENSO-0002_LIGHT_CURVE.md`
- `trace/evidence/ENSO-0003_LIGHT_CURVE.md`
- `trace/evidence/ENSO-0004_LIGHT_CURVE.md`
- `trace/evidence/GOV-001_LIGHT_CURVE.md`
- `trace/evidence/GOV-002_LIGHT_CURVE.md`
- Inert Hermes provenance metadata under `vendor/hermes/`

## Active work

- GOV-004: noncanonical ChatGPT review-history archive executed on its task branch; draft
  PR #11 awaits review and Product Owner acceptance/merge.

## Next gates

1. Complete GOV-003 review and Product Owner merge.
2. Open ARCH-001 to establish the canonical architecture and technical-specification baseline.
3. Integrate curated editable diagrams through a separate architecture task.
4. Review the untracked Sprint 5 implementation independently; do not assume acceptance.
5. Decide the first bounded Hermes local-model capability-lab scope before activation.

## Open decisions

- Product license for Magna-owned material.
- Canonical policy-engine strategy.
- Architecture open decisions recorded in the accepted package.
- Hermes capability-lab task and containment contract.
