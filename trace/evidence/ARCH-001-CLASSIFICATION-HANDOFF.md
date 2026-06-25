# ARCH-001A Classification Handoff

## Provenance
- Instruction prepared by: ChatGPT / System Architect
- Instruction approved by: Product Owner (authority required before launch and merge)
- Intended reviewer: ChatGPT / System Architect
- Review status: `PENDING` (no review of this classification has occurred yet)
- Agent and role: `claude / architecture source classifier (classification + recommendation only)`

## Identity and state
| Field | Value |
|---|---|
| Task | `ARCH-001A` |
| Status | `PUSHED_FOR_REVIEW` |
| Branch | `claude/ARCH-001-source-classification` |
| Base commit | `4afeb0ceec14262c8bbafd86f41a7734fac5e0ae` (main) |
| Final commit (pre-handoff) | null (live branch head is authoritative) |
| Pull request | draft PR targeting `main` (URL in chat) |
| Synchronization | `SYNC_PASS` — main head verified; no conflicting branch/PR |

## Outcome
Classified `archive/chatgpt-review-history/` (406 files, 24 packages) into the 10 required categories and
produced a recommended promotion map. Headlines: the **corrected** architecture/spec package is the candidate
canonical architecture + technical specifications; the **draft** package is superseded (archive-only); the
diagrams package provides editable `.drawio` sources + generated SVG/HTML; `magna-program-evidence-completion`
is the accepted evidence baseline; the program-level Antigravity validation is a **rejected** source
(archive-only). Five conflicts (C1–C5) require System Architect / Product Owner decision. **Nothing promoted,
rewritten, or accepted.**

## Allowed outputs produced
- `trace/reviews/ARCH-001-SOURCE-CLASSIFICATION.md`
- `trace/evidence/ARCH-001-SOURCE-INVENTORY.json`
- `trace/evidence/ARCH-001-CLASSIFICATION-HANDOFF.md` (this file)
- `trace/evidence/ARCH-001-CLASSIFICATION-HANDOFF.json`

## Method
Read-only inspection of the archive tree and key package contents (corrected/draft spec packages, diagrams
package README + structure, evidence-completion master report, GOV-004 source manifest). Classification grounded
in each package's own status/provenance statements; no content rewritten.

## Downloads and dependencies
None.

## Validation
| Check | Result |
|---|---|
| Inventory JSON parses | PASS |
| Handoff JSON parses | PASS |
| Allowed-output scope (only the 4 permitted files created) | PASS |
| No `docs/architecture/` or `docs/technical-specifications/` move | PASS (those folders not created) |
| No edit to GOV-005/GOV-006/runtime/workflows/validators/schemas/canonical docs | PASS |

## Deviations and decisions
No deviations. Decisions required: C1 canonical diagram source; C2 corrected-vs-draft; C3 rejected Antigravity
package; C4 capability-design vs GOV-005; C5 authorize/defer ARCH-001 promotion. Plus record Mermaid CLI version
and viewer-QA status before promoting rendered diagrams.

## Architecture, security, and integration impact
No architecture change; classification/recommendation only. Promotion to canonical folders is ARCH-001 work,
Product Owner approval required. Integration: this branch stacks on `main` for review; it moves nothing.

## Recommended next action
System Architect reviews the classification and resolves C1–C5 with the Product Owner; ARCH-001 then performs
any approved promotion. Do not merge or promote based on this task alone. No acceptance is claimed.

Companion JSON: `trace/evidence/ARCH-001-CLASSIFICATION-HANDOFF.json`.
