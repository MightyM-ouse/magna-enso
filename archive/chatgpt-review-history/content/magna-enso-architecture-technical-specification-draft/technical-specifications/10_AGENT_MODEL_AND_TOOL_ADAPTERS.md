---
document: technical-specifications/10_AGENT_MODEL_AND_TOOL_ADAPTERS
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Agents/model providers, tool/capability adapters, Hermes-derived capability boundary
current_vs_target: Provider adapters partly verified (MCC); Hermes EXTERNAL/inactive
date: 2026-06-21
evidence_sources: [03,11,10 of evidence-completion]
change_control: Hermes inactive (0/6). Governed; nothing deleted.
---

# Spec 10 — Agent, Model, and Tool Adapters

## Human ToC
1. Purpose/Scope/Non-goals 2. Model providers (MAG-AGT) 3. Tool/capability adapters (MAG-TOL)
4. Hermes boundary 5. Failure/permission 6. Acceptance/testing 7. Status/Open 8. Change-control

## AI navigation index
- `providers` → §2 · `tools` → §3 · `hermes` → §4 (EXTERNAL)

## 1. Purpose/Scope/Non-goals
**Purpose:** provider-neutral, replaceable model/tool integration behind the gate. **Non-goals:** active Hermes
capabilities; load-bearing dependence on any single provider.

## 2. Model providers (MAG-FR-009, MAG-NFR-004)
Verified-current (`03`): local Ollama adapter; env-gated OpenAI review; default-mock web search. Adapters are
replaceable; cloud calls are consent-gated and recorded (digest + local/cloud class).

## 3. Tool/capability adapters (MAG-FR-010)
Every adapter call is **behind the single gate**; an adapter is never a bypass path. Adapter contract
(PROPOSED): `describe()`, `invoke(request)` — invoke reachable only post-authorization.

## 4. Hermes boundary (MAG-TOL, EXTERNAL)
Hermes = audited candidate; **0/6** families active; current value = provenance/license metadata only
(`HISTORICAL_EVIDENCE_ONLY`). Any future activation requires a separate, human-approved governance/policy/
evidence gate. **No Hermes capability is active.**

## 5. Failure / permission
Adapter error/timeout ⇒ DENY; provider unavailable ⇒ degraded mode (local-first); no silent cloud fallback.

## 6. Acceptance / testing
Acceptance: no adapter reachable un-gated; Hermes inert; cloud calls consent-gated + logged. Testing: adapter
gating tests; Hermes-inactivity assertion; consent test.

## 7. Status / Open decisions
Status: providers `IMPLEMENTED_VALIDATED` (MCC); adapters `PLANNED`; Hermes `EXTERNAL/INACTIVE`. Open: OD-11.1
reuse vs reimplement adapters; OD-11.2 Hermes activation gate (future); OD-11.3 worker registry.

## 8. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Hermes inactive. PROPOSED marks new contracts. Governed; nothing deleted.
