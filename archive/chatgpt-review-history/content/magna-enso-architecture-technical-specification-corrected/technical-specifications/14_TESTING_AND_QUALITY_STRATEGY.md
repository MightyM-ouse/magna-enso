---
document: technical-specifications/14_TESTING_AND_QUALITY_STRATEGY
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Testing categories, bypass coverage, independent validation, honesty rule, acceptance gate
current_vs_target: Enso harness tests verified (unittest); pytest correction required
date: 2026-06-21
evidence_sources: [05,09,10 of evidence-completion]
change_control: No worker self-approves. Governed; nothing deleted.
---

# Spec 14 — Testing and Quality Strategy

## Human ToC
1. Purpose/Scope/Non-goals 2. Test categories (kept separate) 3. Bypass coverage 4. Independent validation
5. Honesty rule 6. Acceptance gate 7. Status/Open 8. Change-control

## AI navigation index
- `categories` → §2 · `bypass` → §3 · `independent` → §4 · `honesty` → §5 · `gate` → §6

## 1. Purpose/Scope/Non-goals
**Purpose:** prove behavior honestly before acceptance. **Non-goals:** claiming runtime protection from
harness tests; self-certification.

## 2. Test categories (keep separate)
1. **Executable behavior** (allow/deny/approve/fail-closed). 2. **Absence assertions** (dangerous surface not
present). 3. **Structural checks** (single chokepoint; JSON loader; provider boundary). 4. **Independent
review** (human/external judgement; tamper-proofing NOT claimed). Each finding states its category.

## 3. Bypass coverage
Executable deny-tests for testable classes; absence/structural/review for the rest; **P-01…P-13 chokepoint
matrix** labels testable-now vs deferred. **Completeness for real entry points is deferred (R-06 OPEN).**
Current gap: **Enso standard pytest collection fails (7 errors)** — must be corrected (ADR-R8).

## 4. Independent validation (MAG-TRC-004)
Independent reviewer/process (separate identity, read-only) recomputes/validates; **no worker self-approves**;
Magna cannot self-certify. Recommended: senior security/QA architect with no authorship in MCC/Enso Sprint 5.

## 5. Honesty rule
Results are real run logs. Passing the harness means "enforcement core works against the harness" — **not**
"the live system is protected." That distinction must appear in evidence.

## 6. Acceptance gate
Accept only when categories pass, independent validation has no blocking issues, evidence (Light Curve) is
written, **and Vinay signs off**. A blocked gate is expected, not a failure. R-06 stays OPEN; end-to-end
validation recurs per real capability.

## 7. Status / Open decisions
Status: Enso unittest `IMPLEMENTED_VALIDATED` (49 pass); pytest `BLOCKED` (7 errors). Open: ADR-R8 pytest
correction + independent Sprint 5 review.

## 8. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. No self-approval. Governed; nothing deleted.
