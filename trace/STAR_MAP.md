# Star Map - Current Project State

Last governance review: 2026-06-24

| Field | Current state |
|---|---|
| Repository | `MightyM-ouse/magna-enso` |
| Accepted `main` baseline | `4d5c203` before GOV-001 merge |
| Delivery state | Sprints 1-4 accepted; Sprint 4 inert provenance baseline only |
| Sprint 5 | Untracked local `policy/`, `tests/`, and ENSO-0005 evidence; not accepted |
| Policy engine | Selection and integration strategy open |
| Runtime enforcement | Not confirmed on `main` |
| Hermes capabilities | Inactive; capability lab not yet authorized |
| Architecture package | Corrected package accepted as migration input; repository integration pending |
| Diagram package | Editable package prepared; repository integration pending |
| TRACE | Applied instance exists; GOV-001 alignment in progress |
| SGN-01 | Blocked |
| Product authority | Product Owner |

## Accepted evidence

- `trace/evidence/ENSO-0001_LIGHT_CURVE.md`
- `trace/evidence/ENSO-0002_LIGHT_CURVE.md`
- `trace/evidence/ENSO-0003_LIGHT_CURVE.md`
- `trace/evidence/ENSO-0004_LIGHT_CURVE.md`
- Inert Hermes provenance metadata under `vendor/hermes/`

## Active work

- Issue #1 / `trace/tasks/GOV-001.md`: GitHub canonical-source and multi-agent
  governance bootstrap.

## Next gates

1. Review and merge GOV-001.
2. Integrate accepted architecture/specification sources through a separate PR.
3. Integrate curated editable diagrams through a separate PR.
4. Review the untracked Sprint 5 implementation independently; do not assume acceptance.
5. Decide the first bounded Hermes local-model capability-lab scope before activation.

## Open decisions

- Product license for Magna-owned material.
- Canonical policy-engine strategy.
- Architecture open decisions recorded in the accepted package.
- Hermes capability-lab task and containment contract.

