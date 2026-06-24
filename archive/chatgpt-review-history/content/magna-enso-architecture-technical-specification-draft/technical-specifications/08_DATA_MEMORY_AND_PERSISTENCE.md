---
document: technical-specifications/08_DATA_MEMORY_AND_PERSISTENCE
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Memory model, persistence, schemas, governed working memory
current_vs_target: MCC SQLite persistence verified; governed working memory PLANNED
date: 2026-06-21
evidence_sources: [03,05 of evidence-completion; package 10]
change_control: Governed; nothing deleted. ADR-R1 affects persistence composition.
---

# Spec 08 — Data, Memory, and Persistence

## Human ToC
1. Purpose/Scope/Non-goals 2. Memory model 3. Persistence & schemas 4. Governed working memory
5. Failure/recovery 6. Permission/approval 7. Acceptance/testing 8. Status/Open 9. Change-control

## AI navigation index
- `memory` → §2 (MAG-MEM) · `persistence` → §3 · `governed_memory` → §4

## 1. Purpose/Scope/Non-goals
**Purpose:** durable, governed data + memory. **Non-goals:** first-class autonomous working memory (deferred,
MEM-01 pending); unbounded retention.

## 2. Memory model (MAG-FR-014)
Today: traceability/recall access (`02`). Target: governed memory — persistence beyond a session requires
approval; minimal necessary context; no silent retention.

## 3. Persistence & schemas (MAG-FR-006/015)
Verified-current: SQLite/SQLModel tables, repositories, durable event lineage, approval lifecycle (`03`,`05`).
Schemas (PROPOSED for clean Enso): events, approvals, audit records, draft-state. Compose MCC durability with
Enso secure audit ⇒ `DECISION_REQUIRED` (ADR-R1).

## 4. Governed working memory (MEM-01)
MEM-01 is a pending belt layer; underlying primitives partial (`04`). Acceptance scope is ADR-R5. Until
accepted, working memory remains deferred — **do not describe as implemented.**

## 5. Failure / recovery
Store missing/corrupt ⇒ DENY-all; malformed audit tail truncated/quarantined; replay = recovery source of
truth; resting default-deny; no persistent enabled-state survives restart (`10`).

## 6. Permission / approval
Draft persistence = an approval (human acceptance). Memory writes that persist require approval.

## 7. Acceptance / testing
Acceptance: no unapproved persistence; recovery deterministic; restart carries no pending approval. Testing:
persistence + recovery + draft-discard tests.

## 8. Status / Open decisions
Status: persistence `IMPLEMENTED_VALIDATED` (MCC); governed memory `PLANNED`. Open: ADR-R1 composition; ADR-R5
MEM-01 acceptance; OD-10.3 tamper-evident store.

## 9. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. PROPOSED marks new schemas. Governed; nothing deleted.
