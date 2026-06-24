# ARCH-001 Architecture Conflict and Duplication Register

## Status

`PRELIMINARY_BLOCKED_MISSING_INPUTS`

Only evidence-backed conflicts are listed as confirmed. Potential conflicts remain
`REQUIRES_SOURCE_COMPARISON`.

| ID | Type | Sources | Finding | Impact | Required resolution |
|---|---|---|---|---|---|
| AC-001 | Authority gap | GitHub vs ARCH-SRC-01 | GitHub has no accepted architecture tree; the corrected package is accepted only as a migration input | Architecture claims could be mistaken for canonical repository truth | Preserve input status until reviewed Phase B import |
| AC-002 | Status conflict | Static Star Map vs Issue #8/PR #9 | Star Map still names GOV-003 active; GitHub issue/PR state is newer under source precedence | Current task status can appear stale | Reconcile Star Map in the final reviewed ARCH-001 change, not through another self-referential closeout task |
| AC-003 | Strategy supersession | EH-0003 vs EH-0017 | Release/tag stage strategy was superseded by separate repository per stage | Imported documents may carry obsolete single-repository assumptions | Flag every stage-strategy occurrence; use EH-0017 |
| AC-004 | Naming supersession | Historical `Kensho` vs EH-0018 | Canonical active spelling is `KENOSHA` | Terminology drift in architecture and diagrams | Correct active imports; preserve historical evidence unchanged |
| AC-005 | Design/runtime ambiguity | Sprint 3 designs vs repository runtime | EH-0014 accepts design/report-only; runtime enforcement is not confirmed | Architecture may overstate implementation | Label intended, planned, implemented, and verified states explicitly |
| AC-006 | Hermes boundary | Architecture claims vs `vendor/hermes/` | Vendor baseline is inert provenance only | Import could imply executable Hermes adoption or policy enforcement | Retain quarantine language and EH-0015 boundary |
| AC-007 | Policy engine | Package design vs open decision | Canonical policy engine is not selected | A source may prematurely bind technology or implementation | Record candidates, not a selected engine |
| AC-008 | Package overlap | ARCH-SRC-01 vs GOV-SRC-01 | Corrected package may consolidate the 17 accepted Sprint 3 reports, but contents are unavailable | Duplicate or diverging governance architecture may be imported | Compare requirement/decision provenance before choosing targets |
| AC-009 | Diagram synchronization | ARCH-SRC-01 views vs DIAG-SRC-01 | Reported 22 architecture views versus 25 diagram artifacts; relationship is unverified | Orphan, duplicate, or behavior-only diagrams may exist | Validate manifest-to-source-to-render mapping |
| AC-010 | License boundary | Magna-owned package vs open product license decision | Repository is public but Magna-owned license is not selected | Import may create unclear reuse rights | Product Owner selects license or explicitly records interim notice |
| AC-011 | HELIX contract | Enso package vs separate HELIX authority | Exact HELIX doctrine/version used by corrected package is unavailable | Imported contracts may embed stale or copied doctrine | Reference a versioned HELIX contract; do not copy or modify HELIX silently |
| AC-012 | Provenance gap | External local folders vs GitHub | Local ChatGPTReview paths are staging, not canonical | Audit chain breaks if files are copied without manifests | Capture source checksums and a migration manifest in Phase B |

## Potential duplication classes requiring package access

- Foundation summaries versus repository README/governance summaries.
- Capability-governance reports versus architecture policy sections.
- Requirement registry versus feature tracker and Event Horizon decisions.
- Mermaid blocks versus Draw.io sources and SVG renders.
- Evolution-stage contracts versus EH-0017/EH-0018.
- Security and public-exposure sections versus EH-0019 and governance policies.

No duplicate may be deleted or silently selected until exact file comparison is available.
