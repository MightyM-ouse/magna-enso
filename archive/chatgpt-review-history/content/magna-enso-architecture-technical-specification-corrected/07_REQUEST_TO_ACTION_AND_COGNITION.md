---
document: 07_REQUEST_TO_ACTION_AND_COGNITION
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Request-to-action pipeline; sensory/attention/reflex/cognition/routing; event bus & orchestration
current_vs_target: Pipeline is target; routing pattern reuses verified Command Center CSF→BRS
date: 2026-06-21
evidence_sources: [03_CURRENT_SOURCE_ARCHITECTURE_VERIFICATION.md, 02_CANONICAL_MAGNA_DIRECT_READ.md]
change_control: Superseding changes require a governed decision. Do not delete or silently rewrite.
---

# 07 — Request-to-Action and Cognition

## Human table of contents
1. Request-to-action pipeline (DIAG-07)
2. Sensory / attention / reflex / cognition / routing (DIAG-08)
3. Event bus, workflow, orchestration (DIAG-09)
4. Where the human-approval points sit
5. Bounded-cognition guarantees
6. Open decisions
7. Change-control note

## AI navigation index
- `pipeline` → §1 (DIAG-07, MAG-INT-001 MAG-COG-001 MAG-GOV-001 MAG-ORC-001)
- `sensory_cognition` → §2 (DIAG-08, MAG-COG-001)
- `event_orchestration` → §3 (DIAG-09, MAG-ORC-001)
- `approval_points` → §4 (MAG-GOV-001)

## 1. Request-to-action pipeline (DIAG-07) — `Status: TARGET (routing pattern reuses verified MCC)`

> **Corrected (C1/C4/C10):** no consequential execution can begin before
> `AUTHORIZED_PENDING_AUDIT → AUDIT_CONFIRMED → EXECUTION_STARTED`. There is **no direct gate/approval→execute
> edge.** Outcomes use the taxonomy in `technical-specifications/19` (not "everything → DENY"); state names
> follow `technical-specifications/18` §1.

```mermaid
flowchart LR
  IN["Command in - MAG-INT-001"] --> PARSE["Interpret to structured intent - MAG-INT-002"]
  PARSE --> VAL{"Valid + unambiguous?"}
  VAL -->|malformed| INV["INVALID_REQUEST + log"]
  VAL -->|ambiguous| CLR["NEEDS_CLARIFICATION + log"]
  VAL -->|ok| ROUTE["Route - CSF then BRS - MAG-COG-001"]
  ROUTE --> GATE["Capability gate - default-deny - MAG-GOV-001"]
  GATE -->|no record / forbidden| DP["DENY_POLICY + log"]
  GATE -->|evaluator error| EERR["EXECUTION_ERROR / UNAVAILABLE => no effect"]
  GATE -->|approval_required| HOLD["HOLD_FOR_APPROVAL - MAG-GOV-003"]
  HOLD -->|absent provider / deny / timeout| DP
  HOLD -->|cancelled| CAN["CANCELLED"]
  HOLD -->|approve once| APA["AUTHORIZED_PENDING_AUDIT"]
  GATE -->|allow, no approval needed| APA
  APA --> AUD["Durable audit written + flushed - MAG-SEC-202"]
  AUD -->|sink down| UNAV["UNAVAILABLE => no effect"]
  AUD -->|confirmed| AC["AUDIT_CONFIRMED"]
  AC --> ES["EXECUTION_STARTED - via governed adapter - MAG-TOL-001"]
  ES -->|adapter fails| EE2["EXECUTION_ERROR => RECOVERY_REQUIRED"]
  ES --> EC["EXECUTION_COMPLETED via workflow/orchestration - MAG-ORC-001"]
  EC -->|post-check fails| VF["VALIDATION_FAILED => RECOVERY_REQUIRED"]
  EC --> DONE["ALLOW completed + emit runtime evidence - MAG-OBS-001"]
  DP --> REPLAY["Replay-safe reconstruction - MAG-OBS-001"]
  DONE --> REPLAY
```

**Invariants:**
1. No path reaches `EXECUTION_STARTED` without `AUTHORIZED_PENDING_AUDIT` **then** `AUDIT_CONFIRMED` — an
   `ALLOW` decision alone never triggers an effect. Every branch logs.
2. **Pre-execution non-`ALLOW` outcomes produce NO new effect** (fail closed): `DENY_POLICY`,
   `HOLD_FOR_APPROVAL`, `INVALID_REQUEST`, `NEEDS_CLARIFICATION`, `UNAVAILABLE` (dependency/audit-sink down),
   `CANCELLED`. These occur **before** any effect, so nothing was performed.
3. **Execution / post-validation failures may have produced a partial effect** and therefore require
   compensation/recovery, **not** a "no effect" claim: `EXECUTION_ERROR` (adapter failed after
   `EXECUTION_STARTED`) and `VALIDATION_FAILED` (post-execution check) ⇒ `RECOVERY_REQUIRED` (default-deny
   until recovered).
4. Read-only / non-consequential requests may return `INVALID_REQUEST` / `NEEDS_CLARIFICATION` / `UNAVAILABLE`
   as themselves — **not** relabelled as `DENY_POLICY` (`technical-specifications/19`).

## 2. Sensory / attention / reflex / cognition / routing (DIAG-08) — `Status: PARTLY TARGET`
Mapping to Magna's canonical terms (`02`): the **nervous system** (event bus, telemetry, observability) is the
sensory/attention substrate; **reflex** = deterministic guardrails (default-deny, schema/permission checks)
that act without model reasoning; **cognition** = bounded routing/orchestration intelligence that **does not
own governance**.

```mermaid
flowchart TB
  SENSE["Sensory - event/telemetry intake - MAG-OBS-001"] --> ATTN["Attention - prioritize signals - MAG-COG-001"]
  ATTN --> REFLEX["Reflex - deterministic guardrails default-deny - MAG-GOV-001"]
  REFLEX --> COG["Cognition - bounded routing - MAG-COG-001"]
  COG --> ROUTE["Routing decision - MAG-COG-001"]
  REFLEX -. can deny without cognition .-> ROUTE
  COG -. cannot override .-> REFLEX
```

> Reflex (deterministic deny/guardrails) can stop an action **without** cognition; cognition can **never**
> override reflex/governance. This encodes "no hidden autonomy" and "no capability bypass."

## 3. Event bus, workflow, orchestration (DIAG-09) — `Status: REUSE_AFTER_REFACTOR (verified in MCC)`

```mermaid
flowchart LR
  EVT["Event bus - durable, causal/correlation IDs - MAG-ORC-001"] --> WF["Workflow engine - MAG-ORC-001"]
  WF --> ORR["Orchestration runtime - MAG-ORC-001"]
  ORR --> EVT
  ORR --> OBS["Runtime observability + replay - MAG-OBS-001"]
  WF -. every consequential step .-> GATE["Capability gate - MAG-GOV-001"]
  GATE -. authorizes .-> ORR
```

Command Center already implements durable events with causal/correlation fields, workflow/approval/
orchestration linkage, WebSocket delivery, observability, and replay (`03`, `06`). Target Enso reuses this
pattern with the single-chokepoint gate inserted before every consequential step.

## 4. Human-approval points (MAG-GOV-001)
- `approval_required` capability execution → HOLD until an authenticated human decision (Enso ships only a
  **test-only** provider; **production provider absent ⇒ DENY**).
- Draft persistence (memory/skill) → persists only on human acceptance.
- Commit/push/merge, stage promotion, Hermes activation, SGN-01 unblock → all human-gated; no worker self-approves.

## 5. Bounded-cognition guarantees
- Cognition routes and proposes; it does **not** mint authority, change policy, or bypass the gate.
- Payload content cannot escalate privilege ("input-driven escalation ⇒ DENY").
- Reflex/governance is deterministic and precedes cognition.

## 6. Open decisions
- OD-07.1 — Exact router contract for the target architecture within the existing magna-enso repository (reuse MCC `intent_router` vs reimplement) — links ADR-R1.
- OD-07.2 — Whether reflex guardrails live in the gate only or also at the bus boundary (defense in depth).

## 7. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Pipeline is target; routing/orchestration patterns cite verified MCC. Changes governed.
