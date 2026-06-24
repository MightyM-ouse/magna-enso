---
document: technical-specifications/03_BACKEND_AND_API_SPECIFICATION
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Backend services and API surface for target Enso
current_vs_target: MCC FastAPI surface verified-current; clean-Enso API is PROPOSED
date: 2026-06-21
evidence_sources: [03 of evidence-completion; package 06,07]
change_control: All new API paths marked PROPOSED. Governed; nothing deleted.
---

# Spec 03 — Backend and API

## Human ToC
1. Purpose/Scope/Non-goals 2. Service responsibilities 3. API surface (PROPOSED + verified-current)
4. Events 5. Failure/recovery 6. Security/observability 7. Acceptance/testing 8. Status/Open decisions 9. Change-control

## AI navigation index
- `services` → §2 (MAG-INT, MAG-ORC) · `api` → §3 (PROPOSED) · `events` → §4

## 1. Purpose/Scope/Non-goals
**Purpose:** local backend exposing governed command/approval/evidence APIs. **Non-goals:** public/remote API,
multi-tenant auth, cloud-hosted services.

## 2. Service responsibilities
Command intake; routing handoff; capability gate; approval coordination; event bus/workflow/orchestration;
persistence; audit; observability. Verified-current pattern (`03`): FastAPI app registers health, model/review,
provider, policy, authorization, approval, sessions/tasks, agent, system, WebSocket, explorer, observability
routers.

## 3. API surface
- **Verified-current (MCC, reuse candidate):** the router set above exists and validates (`03`).
- **PROPOSED (clean Enso):** exact paths/methods for the clean Enso are **PROPOSED** and must be defined during
  design, e.g. `POST /command` (PROPOSED), `GET /tasks/{id}` (PROPOSED), `POST /approvals/{id}/decision`
  (PROPOSED), `GET /events` WS (PROPOSED). **No path is asserted as final.** Authorization identity is part of
  ADR-R1.

## 4. Events (PROPOSED schema in `09`)
Durable events carry `event_id`, `correlation_id`, `causation_id`, `actor`, `source`, `occurred_at`, type,
payload-digest. Cross-plane minimum schema: `09` §5.

## 5. Failure / recovery
Any service error ⇒ DENY for the affected capability (fail-closed); audit-before-allow; restart ⇒ default-deny;
recovery rebuilds from append-only log (`10`, `13`).

## 6. Security / observability
Local bind by default; consent-gated cloud calls; no secrets in logs/evidence; every decision logged; WS
dispatch for runtime observability (reuse MCC).

## 7. Acceptance / testing
Acceptance: gate reachable only through the single chokepoint; every endpoint that can trigger a capability
routes through the gate; fail-closed proven. Testing: route/runtime integration tests (reuse MCC pattern) +
bypass tests (`14`).

## 8. Status / Open decisions
Status: MCC surface `IMPLEMENTED_VALIDATED`; clean-Enso API `PROPOSED`. Open: OD-03a final API contract
(post-ADR-R1); OD-03b authorization identity model.

## 9. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. New APIs are PROPOSED. Governed; nothing deleted.
