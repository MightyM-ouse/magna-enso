# Canonical Magna Direct Read

## Authority and source mapping

No files named `MAGNA_PROJECT_RULES.md`, `MAGNA_GOVERNANCE.md`, or `MAGNA_SCOPE.md` exist at the active root. Current equivalents are:

| Requested name | Current equivalent |
|---|---|
| Project rules | `AGENTS.md` plus `project-knowledge/MAGNA_AGENT_EXECUTION_PROTOCOL.md` |
| Governance | `project-knowledge/AGENT_GOVERNANCE.md` |
| Scope | `project-knowledge/contracts/00_DEPLOYMENT_SCOPE.md` |
| Current roadmap | `MAGNA_PROJECT_STATUS_AND_NEXT_STEPS.md`, constrained by the Pre-SGN belt and direct source truth |

`MAGNA_BLUEPRINT.md` is explicitly a subordinate compilation (`Authority note` and front matter), not the deciding source.

## Canonical truth

- **Magna:** “a single-user, local-first, governed, replay-safe cognitive orchestration runtime,” and the user-facing organism/product/persona. Evidence: `MAGNA_BLUEPRINT.md` §§1–2; `project-knowledge/identity/MAGNA_ARCHITECTURE_CONSTITUTION.md` §1.
- **HELIX:** encoded genome/doctrine/architecture/constraints and a read-only observability surface. It informs and visualizes, but never mutates runtime. Evidence: Constitution §1 and Law III; Blueprint §2.
- **Cosmos:** canonical, ratified evolutionary memory/chronicle. It is append-only with respect to history; agents propose and Vinay ratifies. Evidence: `project-knowledge/identity/THE_COSMOS.md` §§0–3; `AGENT_GOVERNANCE.md` §F.
- **Identity:** Magna’s truthful self-model and capability claims, not its history. Evidence: `project-knowledge/pre-sgn-stabilization/CSF_01_CONSCIOUS_SELF_MODEL_TRUTH_REGISTRY.md` §§1–7.
- **Boundary:** Identity answers what Magna is/can do now; Cosmos records ratified evolution. Neither is runtime authority, and Cosmos is not self-updating.
- **Presence:** a user-facing embodiment/projection of Magna, not HELIX and not an autonomous runtime author. Evidence: `HAB_01_HABITABLE_SURFACES_UI_SURFACE_FREEZE.md` §Presence Rule; Constitution §9.
- **Cognition:** bounded command/orchestration intelligence; model workers do not own architecture or governance. Evidence: Constitution §§5, 9; `MAGNA_EVOLUTIONARY_ARCHITECTURE_MAP.md` stage table.
- **Memory:** traceability/recall access and later governed working memory; first-class working memory remains deferred. Evidence: `MEM_01_MEMORY_FORMATION_TRACEABILITY_ACCESS_MODEL.md` §§0–4; Constitution §9.
- **Nervous system:** event bus, telemetry, observability, and orchestration signals visible without granting control. Evidence: `NRV_01_NERVOUS_SYSTEM_VISIBILITY_RUNTIME_STATUS.md` §§0–4; Evolutionary Map stage 9.

## Protected boundaries

The active registry protects runtime authority separation, event/replay integrity, approval/governance, identity documents, credentials, database/migrations, and governed documentation/log areas. Evidence: `project-knowledge/identity/PROTECTED_BOUNDARIES_REGISTRY.md`, especially the boundary entries and `Identity Systems`; Constitution Laws I–XII.

## Current capabilities and drift

Direct source verifies the ten-tab shell, FastAPI/SQLite backend, real REST/WebSocket communication, event/workflow/approval/orchestration primitives, durable event lineage/replay, local Ollama adapter, opt-in OpenAI review, mock/default-disabled web search, push-to-talk browser voice, presence UI, and task traceability utilities. These are development capabilities, not production certification.

The CSF registry still says governed Ollama UI execution is unavailable (`backend/app/core/csf/capability_registry.py`, `ollama_through_governed_ui` record), while `backend/app/services/ollama_service.py` and local-model routes implement it. This is capability-truth drift requiring a later governed correction, not an audit edit.

