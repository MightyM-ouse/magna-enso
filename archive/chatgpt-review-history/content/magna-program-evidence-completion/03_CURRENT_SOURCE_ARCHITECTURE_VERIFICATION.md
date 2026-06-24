# Current Source Architecture Verification

## Verified current architecture

```mermaid
flowchart LR
  UI["React ten-tab shell\nfrontend/src/app/App.tsx"] --> REST["REST client\nfrontend/src/services/apiClient.ts"]
  UI --> WS["Workflow/runtime WebSockets\nworkflowSocket.ts"]
  REST --> API["FastAPI app\nbackend/app/main.py"]
  WS --> API
  API --> ROUTER["CSF → BRS → command/provider routing\nroutes_local_model.py + intent_router.py"]
  API --> POLICY["Risk classification + authorization + approvals"]
  API --> RUNTIME["Event bus → workflow engine → orchestration runtime"]
  RUNTIME --> DB["SQLite SQLModel tables\ndb/models.py + repositories.py"]
  POLICY --> DB
  RUNTIME --> OBS["Replay/runtime observability + WebSocket dispatcher"]
  ROUTER --> OLLAMA["Local Ollama adapter"]
  ROUTER --> OPENAI["Explicit env-gated OpenAI review"]
  ROUTER --> WEB["Web-search agent\nmock/default-disabled live providers"]
```

## Source evidence

- Routes and shell: `frontend/src/app/App.tsx`; `frontend/src/utils/navigationRoutes.ts` define Command, Identity, Agents, Memory, Explorer, Cognition, Cosmos, Help, Settings, System.
- Communication: `frontend/src/services/apiClient.ts` performs real fetches and constructs `/ws/workflow/{taskId}` and `/ws/events`; service modules bind UI panels to backend endpoints.
- FastAPI: `backend/app/main.py` registers health, model/review, provider, policy, authorization, approval, sessions/tasks, agent, system, WebSocket, explorer, and observability routers.
- Runtime: `backend/app/core/event_bus.py`, `workflow_engine.py`, `orchestration_runtime.py`, `approval_engine.py`, `runtime_initializer.py`, `runtime_observability.py`, `websocket_dispatcher.py` contain executable classes and durable reads/writes.
- Persistence: `backend/app/db/models.py`, `database.py`, `repositories.py`; default URL in `core/config.py` is SQLite.
- Provider integrations: `services/ollama_service.py` makes local HTTP calls; `services/cloud_review_service.py` gates OpenAI behind explicit configuration; web search is permission-aware and defaults to mock; voice uses browser recognition/synthesis hooks and bounded backend domain scaffolding.
- Traceability: `scripts/magna_prepare_task.py`, `scripts/magna_close_task.py`, `agent-logs/_traceability/task_sessions.jsonl`, and `project-knowledge/MAGNA_TASK_ORCHESTRATION_AND_TRACEABILITY_ARCHITECTURE.md` implement/describe engineering task preparation and closure separately from runtime event lineage.

## Planned or not verified as operational

Ambient voice/wake word, unrestricted runner/device control, autonomous orchestration, first-class working memory, public deployment, multi-user operation, and TRACE-to-Magna runtime interoperability are deferred. Presence is implemented as UI projection; it is not evidence of autonomous cognition. Production/UAT/DR operation was not found.

