# PRODUCT BACKLOG ID RULES

Status: `PROPOSED`
Purpose: Keep Magna product stories separate from engineering and agent execution tasks

## Principle

Product story IDs must identify user-facing Magna functionality.

Engineering task IDs must identify delivery work required to implement or validate that functionality.

Do not use one ID family for everything.

## ID families

| ID Family | Meaning | Owner | Example |
|---|---|---|---|
| MAG-EPIC-### | Product epic / large capability group | Product Owner / Product Manager | MAG-EPIC-001 |
| MAG-US-### | Product user story | Product Owner / Product Analyst | MAG-US-001 |
| DES-### | Design task | UX / Product Design | DES-001 |
| ARCH-### | Architecture task or decision | Solution Architect | ARCH-001 |
| FE-### | Frontend implementation task | Frontend Engineering | FE-001 |
| BE-### | Backend/runtime implementation task | Backend Engineering | BE-001 |
| AGT-### | Agent behavior / orchestration task | Agent engineering / orchestration owner | AGT-001 |
| VAL-### | Independent validation task | Validation / QA / Antigravity | VAL-001 |
| GOV-### | Governance/project execution task | Governance owner / System Architect | GOV-005 |
| STAT-### | Repository status reconciliation task | System Architect / Codex | STAT-001 |
| PLAN-### | Planning/backlog/system task | Product Owner / System Architect | PLAN-001 |

## ID assignment rules

1. Product user stories receive `MAG-US-###` IDs.
2. Epics receive `MAG-EPIC-###` IDs.
3. Downstream tasks receive separate IDs according to work type.
4. A user story may reference many downstream tasks.
5. A downstream task may support multiple user stories only when explicitly linked.
6. Governance tasks must not be used as user-story IDs.
7. Agent task packets must not replace product user stories.
8. Validation tasks must be created from acceptance criteria, not from assumptions.

## How to pre-fill downstream work

When a story is drafted, suggested downstream work may be pre-filled using these rules:

### Design Task
Pre-fill `DES-###` when the story changes or introduces:

- screens,
- tabs,
- layout,
- navigation,
- user interaction,
- visual hierarchy,
- user-facing wording,
- status presentation.

### Architecture Task
Pre-fill `ARCH-###` when the story needs:

- new domain model,
- new system boundary,
- new data flow,
- canonical decision,
- integration between subsystems,
- replay/safety/privacy reasoning,
- durable state design.

### Frontend Task
Pre-fill `FE-###` when the story requires:

- UI component changes,
- route/tab behavior,
- visual state rendering,
- user input handling,
- frontend data binding,
- responsiveness/accessibility.

### Backend Task
Pre-fill `BE-###` when the story requires:

- API changes,
- persistent data,
- runtime state,
- event processing,
- backend services,
- local storage or SQLite changes.

### Agent Task
Pre-fill `AGT-###` when the story requires:

- agent behavior,
- orchestration behavior,
- task lifecycle signaling,
- approval-aware agent behavior,
- agent status events,
- agent handoff behavior visible to the user.

### Validation Task
Pre-fill `VAL-###` when the story has acceptance criteria that must be independently verified.

Every `READY_FOR_AGENT_TASKING` story should normally have at least one `VAL-###` placeholder.

### Governance Dependency
Pre-fill `GOV-###` only when the story depends on governance being present, visible, or enforced.

Do not turn GOV tasks into product stories unless the governance behavior is directly user-visible in Magna.

## Validation task identification rules

Validation tasks should be derived from acceptance criteria.

Example acceptance criterion:

```text
The user can see when an agent is blocked and why.
```

Possible validation task:

```text
VAL-012 — Validate blocked-agent status visibility and explanation accuracy.
```

The validation task should check:

- whether the UI shows the blocked state,
- whether the explanation is understandable,
- whether the state is accurate,
- whether the user can identify the required next decision,
- whether misleading or stale states are prevented.

## Status values

Use these status values for product backlog items:

| Status | Meaning |
|---|---|
| DRAFT | Initial story, not yet refined |
| NEEDS_REFINEMENT | Story exists but lacks clarity or criteria |
| READY_FOR_REFINEMENT | Ready for team review/refinement |
| READY_FOR_AGENT_TASKING | Confirmed and ready to split into execution tasks |
| IN_DELIVERY | Downstream implementation/validation tasks active |
| ACCEPTED | Product Owner accepted outcome |
| DEFERRED | Not in current planning window |
| BLOCKED | Cannot proceed until dependency/decision resolves |

## Separation examples

### Correct product story

```text
MAG-US-014 — Agent Blocked State Explanation
As a Magna user, I want Magna to explain why an agent is blocked, so that I know what decision or correction is required.
```

### Correct downstream tasks

```text
DES-014 — Design blocked-agent explanation panel
FE-014 — Implement blocked-agent status display
BE-014 — Expose blocked-agent reason state
AGT-014 — Emit blocked reason metadata
VAL-014 — Validate blocked-state explanation accuracy
GOV-005 — Governance dependency for agent task boundaries
```

### Incorrect product story

```text
As a developer, I want GitHub governance CI to run so that PRs are protected.
```

This belongs to a GOV or CI task, not to `MAG-US-###`.
