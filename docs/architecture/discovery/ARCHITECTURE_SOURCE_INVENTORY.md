# ARCH-001 Architecture Source Inventory

## Status

`PARTIAL_COMPLETE_BLOCKED_MISSING_INPUTS`

Inventory date: 2026-06-24
Repository baseline: `20e69cad9edfc71e193de3411f7778a64c041273`
Task branch: `architect/ARCH-001-canonical-architecture-baseline`

## Classification vocabulary

| Classification | Meaning |
|---|---|
| CANONICAL | Accepted repository authority for its stated purpose |
| ACCEPTED_MIGRATION_INPUT | Product Owner accepted it as an input, but it is not canonical in GitHub |
| ACCEPTED_DESIGN_LOCAL_ONLY | Accepted design evidence remains outside GitHub |
| CANDIDATE | Requires comparison and acceptance before canonical use |
| HISTORICAL | Preserved evidence; not an active source |
| GENERATED_TRANSPORT | Reproducible delivery/viewer artifact; not source authority |
| MISSING_INPUT | Exact source is identified but unavailable for inspection |
| OUT_OF_SCOPE | Relevant boundary, not an ARCH-001 migration source |

## Canonical GitHub sources inspected

| Source | Classification | Architecture relevance | Disposition |
|---|---|---|---|
| `AGENTS.md` and model adapters | CANONICAL | Worker boundaries and repository workflow | Retain outside architecture tree |
| `README.md` | CANONICAL_NAVIGATION | High-level verified state and architecture migration warning | Retain; do not treat as architecture specification |
| `docs/governance/` | CANONICAL | Source authority, evidence, security, QA, collaboration | Retain as governance |
| `trace/DECISION_LOG.md` | CANONICAL | Accepted Event Horizon decisions and supersession | Retain as decision authority |
| `trace/FEATURE_TRACKER.md` | CANONICAL | Accepted Sprint 1-4 delivery history | Retain as delivery evidence |
| `trace/RISK_REGISTER.md` | CANONICAL | Open architecture and runtime risks | Retain as risk authority |
| `trace/STAR_MAP.md` | CANONICAL_STATUS_WITH_KNOWN_LAG | Curated status snapshot; Issue #8 and PR #9 are newer | Reconcile only at reviewed task closeout |
| `trace/CELESTIAL_INDEX.json` | CANONICAL_ROUTER | Architecture route is `MIGRATION_PENDING` | Update only after discovery outputs are accepted |
| `trace/evidence/ENSO-0001..0004` | ACCEPTED_EVIDENCE | Proves accepted governance/design/provenance states | Reference, do not relocate |
| `vendor/hermes/` | CANONICAL_INERT_PROVENANCE | Accepted Sprint 4 quarantine only | Retain; never present as runtime architecture |
| `docs/architecture/` | NOT_PRESENT_ON_MAIN | No canonical architecture baseline exists | ARCH-001 discovery is the first proposed content |
| `docs/technical-specifications/` | NOT_PRESENT_ON_MAIN | No canonical technical-specification baseline exists | Phase B candidate target only |

## External migration inputs

Machine-specific paths are represented by logical aliases because the repository is public.

| Input ID | Logical source | Reported evidence | Current classification |
|---|---|---|---|
| ARCH-SRC-01 | `<MAGNA_LOCAL_ROOT>/ChatGPTReview/magna-enso-architecture-technical-specification-corrected/` | Reported 59 files, 22 architecture views, 52 requirements, 52/52 traceability; produced 2026-06-22 | ACCEPTED_MIGRATION_INPUT + MISSING_INPUT |
| DIAG-SRC-01 | Attached `magna-enso-architecture-diagrams-draft-corrected.zip` | SHA-256 verified; 25 Draw.io, 25 SVG, 25 HTML views, 25 Mermaid sources, 7 curated validation files and 78 raw validation entries | AUTHENTICATED_CANDIDATE_SOURCE |
| GOV-SRC-01 | `<MAGNA_LOCAL_ROOT>/ChatGPTReview/sprint-3-capability-governance-design/` | 17 reports accepted as design/report-only under EH-0014 | ACCEPTED_DESIGN_LOCAL_ONLY + MISSING_INPUT |
| HELIX-SRC-01 | Separate Magna HELIX repository/doctrine | Enso is built on HELIX doctrine; repository must never be modified by Enso work | EXTERNAL_AUTHORITY_REFERENCE + exact version missing |

The local path alias is:
`<MAGNA_LOCAL_ROOT> = /Users/<product-owner>/Projects/AI/Magna`.
The username is intentionally redacted from this public repository.

## Known ARCH-SRC-01 manifest entries

These names were reported in the accepted package inventory but cannot yet be read in this
session:

- `00_MASTER_FOUNDATION_SUMMARY.md`
- `06_MAGNA_ENSO_TARGET_ARCHITECTURE.md`
- `16_EVOLUTION_STAGE_CONTRACTS.md`
- `registries/MAGNA_REQUIREMENT_REGISTRY.yaml`
- `technical-specifications/17_REQUIREMENT_TRACEABILITY_MATRIX.md`

The remaining package filenames, contents, checksums, internal links, and cross-package
relationships are not verified.

## Diagram evidence boundary

The corrected diagram ZIP checksum and inventory are verified. Its internal validation reports pass, but no diagram is canonical or synchronized with the current repository until its 17 referenced architecture/specification sources are inspected. See `DIAGRAM_PACKAGE_ASSESSMENT.md`.

## Discovery conclusion

GitHub currently has governance and delivery evidence, not a canonical product architecture
baseline. ARCH-SRC-01 must be supplied before Phase A can complete normative content comparison, per-file mapping, conflict resolution, and a final Phase B recommendation. DIAG-SRC-01 is authenticated and assessed as a candidate source.
