# 11 — Implementation Index (evidence-based)

> Index of what is actually in the repositories. Status uses the readiness vocabulary.
> Symbols/tests cited are observed via directory + test-name inspection (not all re-run).

## A. magna-command-center

### APIs / routes
- FastAPI app `backend/app/main:app` (uvicorn :8010). System routes (`test_system_routes`),
  provider settings, review/scoring, saved-runs/tasks, web-search (mock). — *IMPLEMENTED,
  NOT VERIFIED now.*

### Runtime services & classes (by test evidence)
| Area | Evidence (test module) | Status |
|---|---|---|
| Event bus | `test_core_event_bus` | IMPL, not verified now |
| Workflow engine | `test_core_workflow_engine` | IMPL |
| Approval engine | `test_core_approval_engine` | IMPL |
| Orchestration runtime | `test_core_orchestration_runtime` | IMPL |
| Websocket dispatcher | `test_core_websocket_dispatcher` | IMPL |
| Audit logger | `test_core_audit_logger` | IMPL |
| Risk classifier / policy engine | `test_core_risk_classifier`, `test_risk_policy_engine` | IMPL |
| Attention | `test_core_attention` | IMPL |
| Agent protocol + permission profiles | `test_core_agent_protocol`, `test_agent_permission_profiles` | IMPL |
| ATM-01 boundary | `test_atm_01_boundary_rules`, `test_authorization_boundary` | IMPL/landed |
| CSF-01 self-model | `test_csf_01_conscious_self_model`, `_command_integration` | IMPL/frozen |
| Persistence + completion gate + dual-read/boot recovery | `test_persistence_completion_gate`, `test_phase_2_dual_read`, `test_phase_3b_boot_recovery` | IMPL |
| Task prepare/close (traceability) | `test_magna_prepare_task`, `test_magna_close_task` | IMPL |
| Cognitive explorer / runtime observability | `test_cognitive_explorer`, `test_runtime_observability` | IMPL |
| Local + cloud review, feedback learning, rules | `test_local_review*`, `test_cloud_review_persistence`, `test_real_openai_review_service`, `test_feedback_learning`, `test_local_review_rules` | IMPL (gated) |
| Evolutionary naming guardrails | `test_evolutionary_naming_guardrails` | IMPL |

### UI routes/components
10-tab shell (`src/`), Presence avatar (Three.js). — IMPL (HAB-01 landed).

### DB
SQLite `magna.db` (×2 locations); `docs/DATABASE_SCHEMA.md`. Migration "phases"
(dual-read, boot recovery) in tests. No Alembic confirmed (recommended only).

### Scripts/lifecycle
`start-magna.sh`, `scripts/magna_self_heal.sh` (SessionStart hook), `scripts/verify_command_router.mjs`,
`scripts/start-codex.sh`, `start-antigravity.sh`.

### Status/ownership
Owner Vinay; workers Claude/Codex/Antigravity/Ollama. Latest area: Explorer/Phase-E.

## B. magna-enso

| Item | Path | Status |
|---|---|---|
| Policy engine (8 modules, 883 LOC) | `policy/` | PARTIALLY IMPLEMENTED, **untracked**, NOT VERIFIED (C-6/C-7) |
| Policy tests (11 modules) | `tests/policy/` | PRESENT, cannot collect (C-7) |
| TRACE engineering instance (12 artifacts) | `trace/` | DONE |
| Light Curves ENSO-0001..0005 | `trace/evidence/` | 0001–0004 human-approved; **0005 untracked/draft** |
| Inert Hermes baseline | `vendor/hermes/` | DONE (inert) |
| Entry docs | `AGENTS.md`,`CLAUDE.md`,`CODEX.md`,`ANTIGRAVITY.md`,`README.md` | DONE (README stale, C-5) |

Key symbols (policy): `CapabilityGate.authorize`, `PolicyHarness.invoke`,
`PolicyEvaluator.evaluate`, `ApprovalCoordinator.{create_pending,consume}`,
`SecureAuditSink.append`, `canonical_json`, `HumanDecisionProvider`/`NullDecisionProvider`,
`Outcome.{ALLOW,DENY,HOLD_FOR_APPROVAL}`, `Decision`, `CapabilityRequest`, `PolicyRecord`.

## C. TRACE

| Item | Path | Status |
|---|---|---|
| Telemetry server | `src/server/{main,ingest,db,models,paths}.py` | CURRENT |
| Dashboard | `src/ui/src/{App,api,main}.jsx` | CURRENT |
| Roles + context routing | `agent-context/` | CURRENT (advisory) |
| Hooks + safety rules | `.claude/` | CURRENT |
| e2e test | `tests/test_server.py` | CURRENT (claimed 6/6) |
| Proposed orchestration loop | `proposed-governed-loop/` | UNTRACKED/PROPOSED |

## D. Events & contracts
- command-center: internal event bus + agent protocol contracts (`docs/API_CONTRACTS.md`).
- enso: `CapabilityRequest`/`Decision` contract; audit JSONL event schema (`capability_decision`).
- TRACE: telemetry payload Pydantic models; hook → ingest contract.

## E. Model integrations
- command-center: Ollama (local, default), OpenAI/ChatGPT (gated), Tavily (gated/mock).
- enso: none yet (providers are human-decision only at the policy layer).
- TRACE: model-agnostic (observes Claude Code sessions).
