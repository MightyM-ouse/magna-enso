---
document: technical-specifications/03_BACKEND_AND_API_SPECIFICATION
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Backend services and API surface for target Enso
current_vs_target: MCC FastAPI surface verified-current; target API (within the existing magna-enso repository) is PROPOSED
date: 2026-06-21
evidence_sources: [03 of evidence-completion; package 06,07]
change_control: All new API paths marked PROPOSED. Governed; nothing deleted.
---

# Spec 03 — Backend and API

## Human ToC
1. Purpose/Scope/Non-goals 2. Service responsibilities 3. API surface (PROPOSED + verified-current)
4. Events 5. Failure/recovery 6. Security/observability 7. Acceptance/testing 8. Status/Open decisions 9. Change-control

## AI navigation index
- `services` → §2 (MAG-INT-001, MAG-ORC-001) · `api` → §3 (PROPOSED) · `events` → §4

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
- **PROPOSED (target architecture within the existing magna-enso repository):** exact paths/methods for the target architecture within the existing magna-enso repository are **PROPOSED** and must be defined during
  design, e.g. `POST /command` (PROPOSED), `GET /tasks/{id}` (PROPOSED), `POST /approvals/{id}/decision`
  (PROPOSED), `GET /events` WS (PROPOSED). **No path is asserted as final.** Authorization identity is part of
  ADR-R1.

## 4. Events (PROPOSED schema in `09`)
Durable events carry `event_id`, `correlation_id`, `causation_id`, `actor`, `source`, `occurred_at`, type,
payload-digest. Cross-plane minimum schema: `09` §5.

## 5. Failure / recovery (ten-outcome taxonomy — spec `19`)
A service error is **not** uniformly mapped to `DENY_POLICY`. The outcome is classified honestly, and the
effect rule depends on **when** the failure occurs relative to `EXECUTION_STARTED`:

- **Before execution (authorization / audit / dependency fails):** a **consequential** action produces **no new
  effect** (fail closed). Classify as: no policy / forbidden ⇒ `DENY_POLICY`; store/provider/audit-sink down ⇒
  `UNAVAILABLE`; malformed / over-privileged ⇒ `INVALID_REQUEST`; ambiguous ⇒ `NEEDS_CLARIFICATION`; awaiting
  human ⇒ `HOLD_FOR_APPROVAL`; cancelled ⇒ `CANCELLED`.
- **After `EXECUTION_STARTED`:** a failure may mean a **partial effect already occurred** — `EXECUTION_ERROR`
  (adapter failed mid-effect) or `VALIDATION_FAILED` (post-execution check failed) ⇒ transition to
  `RECOVERY_REQUIRED` (compensation/recovery; default-deny until recovered). Do **not** report these as "no
  effect."
- **Read-only / non-consequential** requests return their own outcome (e.g. `UNAVAILABLE`, `INVALID_REQUEST`)
  and are **not** relabelled as `DENY_POLICY`.

Common rules: audit-before-effect (an `ALLOW` alone never triggers an effect, `18`); restart ⇒ default-deny;
recovery rebuilds from the append-only log (`10`, `13`).

## 6. Security / observability
Local bind by default; consent-gated cloud calls; no secrets in logs/evidence; every decision logged; WS
dispatch for runtime observability (reuse MCC).

## 7. Acceptance / testing
Acceptance: gate reachable only through the single chokepoint; every endpoint that can trigger a capability
routes through the gate; fail-closed proven. Testing: route/runtime integration tests (reuse MCC pattern) +
bypass tests (`14`).

## 8. Status / Open decisions
Status: MCC surface `IMPLEMENTED_VALIDATED`; target API (within the existing magna-enso repository) `PROPOSED`. Open: OD-03a final API contract
(post-ADR-R1); OD-03b authorization identity model.

## 9. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. New APIs are PROPOSED. Governed; nothing deleted.
