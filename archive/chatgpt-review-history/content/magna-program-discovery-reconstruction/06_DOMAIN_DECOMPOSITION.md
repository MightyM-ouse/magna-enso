# 06 — Domain Decomposition

> Domains/modules grouped by codebase, with status. Evidence = files/tests observed.

## A. magna-command-center domains (`backend/app/`)

| Domain/package | Responsibility (inferred from names + tests) | Status |
|---|---|---|
| `core` | Runtime primitives: event bus, workflow engine, approval engine, orchestration runtime, websocket dispatcher, audit logger, risk classifier, attention, agent protocol, consolidation, types | PARTIALLY IMPLEMENTED, tests present (not re-run) |
| `orchestrator` | Higher-level orchestration runtime + observability | IMPLEMENTED (per `test_core_orchestration_runtime`, `test_runtime_observability`) |
| `domains` | Bounded business domains incl. bounded approvals | IMPLEMENTED (`test_domains_bounded_approvals`) |
| `providers` | Provider-neutral adapters (OpenAI review/scoring, local Ollama, web-search mock) | IMPLEMENTED; live calls disabled by default (`test_provider_settings`, `test_real_openai_review_service`) |
| `agents` | Agent roster + permission profiles | IMPLEMENTED (`test_agent_permission_profiles`, `test_web_search_agent` mock) |
| `services` | App services (review export, feedback learning, local review rules) | IMPLEMENTED (`test_review_export`, `test_feedback_learning`, `test_local_review_rules`) |
| `api` | FastAPI routes (system routes, etc.) | IMPLEMENTED (`test_system_routes`) |
| `models`/`schemas` | Pydantic/data models | IMPLEMENTED |
| `db` | SQLite persistence + completion gate + dual-read/consolidation migration phases | IMPLEMENTED (`test_persistence_completion_gate`, `test_phase_2_dual_read`, `test_phase_3b_boot_recovery`) |
| CSF-01 self-model | Conscious self-model + command integration | IMPLEMENTED/FROZEN (`test_csf_01_*`) |
| ATM-01 boundary | Permission/approval boundary rules | IMPLEMENTED (`test_atm_01_boundary_rules`, `test_authorization_*`) |
| Task orchestration/traceability | `magna_prepare_task` / `magna_close_task`, evolutionary naming guardrails | IMPLEMENTED (`test_magna_prepare_task`, `test_magna_close_task`, `test_evolutionary_naming_guardrails`) |
| Cognitive Explorer / Phase-E observability | Read-only runtime-cognition visualization | IMPLEMENTED (`test_cognitive_explorer`) |
| Risk policy engine | Risk classification + envelope subset | IMPLEMENTED (`test_risk_policy_engine`, `test_phase_3a_envelope_subset`) |

> ~40 backend test modules exist; **"498 passed" is a status-doc claim, not verified now.**

## B. magna-enso modules

| Module | Responsibility | Status |
|---|---|---|
| `policy/schema.py` | Strict JSON policy-record loader | IMPLEMENTED (untracked), imports OK |
| `policy/canonical.py` | Canonical invocation normalization + SHA-256 binding (NFC, sorted keys, path resolution) | IMPLEMENTED (untracked) |
| `policy/evaluator.py` | Pure, state-aware default-deny evaluator | IMPLEMENTED (untracked) |
| `policy/provider.py` | `HumanDecisionProvider` protocol; prod Null/Deny only | IMPLEMENTED (untracked) |
| `policy/approval.py` | In-memory, serialized, single-use approval coordination | IMPLEMENTED (untracked) |
| `policy/audit.py` | Append-only JSONL audit sink, `0600`, hash-chain | IMPLEMENTED (untracked) |
| `policy/gate.py` | Fail-closed `CapabilityGate` + inert `PolicyHarness` | IMPLEMENTED (untracked) |
| `policy/models.py` | `CapabilityRequest`, `Decision`, `Outcome`, `PolicyRecord` | IMPLEMENTED (untracked) |
| `tests/policy/*` (11) | Unit + security-contract tests | PRESENT; **cannot run (C-7)** |
| `trace/*` | TRACE engineering instance (12 artifacts + 5 Light Curves) | DONE (governance) |
| `vendor/hermes/*` | Inert provenance baseline | DONE (inert) |

**All Enso runtime is in one module set (`policy/`).** No identity, profiles, memory,
scheduler, LAN, UI, or capture modules exist yet (Sprints 6–15, PLANNED).

## C. TRACE modules

| Module | Responsibility | Status |
|---|---|---|
| `src/server/main.py`,`ingest.py`,`db.py`,`models.py`,`paths.py` | FastAPI telemetry ingest + SQLite + SSE | CURRENT |
| `src/ui/src/{App.jsx,api.js,main.jsx}` | React dashboard | CURRENT |
| `agent-context/roles/{planner,builder,validator}.md` + `permission-profiles.json` + `AGENT_CONTEXT_INDEX.json` | Role + context routing | CURRENT (advisory) |
| `.claude/` hooks + settings | Lifecycle hooks + universal deny-rules | CURRENT |
| `tests/test_server.py` | e2e ("6/6" claimed) | CURRENT (not re-run) |
| `proposed-governed-loop/` | Proposed orchestration changeset (subagents, runs) | UNTRACKED / PROPOSED |

## D. Cross-codebase shared concepts (candidates for a shared component)

- **Policy/approval gating** exists *twice*: command-center `risk_policy_engine` +
  ATM-01, and Enso `policy/`. These are independent implementations of the same idea.
- **Traceability** exists *three* ways: command-center internal task traceability,
  Enso TRACE engineering instance, TRACE dashboard telemetry. No shared library.
- **Provider-neutral adapters** exist in command-center; Enso plans its own. Reuse
  candidate (see `13_REUSE_AND_REBUILD_ASSESSMENT.md`).
