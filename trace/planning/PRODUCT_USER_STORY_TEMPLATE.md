# PRODUCT USER STORY TEMPLATE

Status: `PROPOSED`
Purpose: Standard template for Magna product user stories

## Template

```markdown
# MAG-US-### — <Short story title>

Status: DRAFT | NEEDS_REFINEMENT | READY_FOR_REFINEMENT | READY_FOR_AGENT_TASKING | ACCEPTED | DEFERRED
Epic: MAG-EPIC-### — <Epic name>
Capability Area: <Command | Identity | Agents | Memory | Explorer | Cognition | Cosmos | Help | Settings | System | Governance Visibility | Approval Flow | Task Awareness>
Product Owner: Vinay / Product Owner
Priority: P0 | P1 | P2 | P3

## User Story

As a <Magna user role>, I want <user-facing Magna capability>, so that <user value / outcome>.

## User Value

<Explain why this matters to the user. Focus on product value, trust, control, clarity, productivity, safety, or usability.>

## User Flow

1. <User action or context>
2. <What Magna shows or does>
3. <How the user responds or benefits>
4. <End state / decision / outcome>

## Acceptance Criteria

- [ ] <Observable user-facing result>
- [ ] <Behavior or state that can be validated>
- [ ] <Boundary or error state>
- [ ] <User clarity / visibility requirement>

## Out of Scope

- <What this story does not cover>
- <Implementation details that should not be included in this story>

## Dependencies

- Product dependency: <another story, decision, or capability>
- Architecture dependency: ARCH-### or N/A
- Governance dependency: GOV-### or N/A
- Data/runtime dependency: <dependency or N/A>

## Open Questions

- <Question that needs Product Owner clarification>

## Suggested Downstream Work

These are placeholders only. They are not the product story itself.

### Design Task
DES-### — <UI/UX design work or N/A>

### Architecture Task
ARCH-### — <architecture clarification or N/A>

### Frontend Task
FE-### — <frontend implementation or N/A>

### Backend Task
BE-### — <backend/runtime implementation or N/A>

### Agent Task
AGT-### — <agent/orchestration behavior or N/A>

### Validation Task
VAL-### — <independent validation task or N/A>

### Governance Dependency
GOV-### — <governance dependency or N/A>

## Validation Notes

Validation must confirm the user outcome, not only code completion.

- Can the user understand the feature?
- Does the visible behavior match the acceptance criteria?
- Are blocked/error/approval states clear?
- Is unsafe or confusing behavior prevented?
```

## Example

```markdown
# MAG-US-001 — View Agent Work Status

Status: DRAFT
Epic: MAG-EPIC-001 — Governed Agent Awareness
Capability Area: Agents
Product Owner: Vinay / Product Owner
Priority: P0

## User Story

As a Magna user, I want to see what each agent is currently doing, so that I can understand whether Magna is working safely and under my control.

## User Value

The user can trust Magna because agent activity is visible, understandable, and reviewable.

## User Flow

1. User opens the Agents tab.
2. Magna shows active, blocked, completed, and waiting-for-approval agent work.
3. User selects an agent task.
4. Magna shows task purpose, status, evidence, and required user decision.

## Acceptance Criteria

- [ ] The user can see active agent work.
- [ ] The user can distinguish active, blocked, completed, and waiting-for-approval states.
- [ ] The user can open details for each visible task.
- [ ] The user can see what decision, if any, is required.
- [ ] The user is not shown hidden implementation-only details by default.

## Out of Scope

- Creating new agent tasks.
- Editing GitHub branches.
- Automatically merging pull requests.

## Dependencies

- Product dependency: Agent task awareness model
- Architecture dependency: ARCH-### TBD
- Governance dependency: GOV-005
- Data/runtime dependency: Agent status events

## Open Questions

- Should completed tasks remain visible permanently or only for the current session?
- Should blocked tasks appear in the same list as active tasks?

## Suggested Downstream Work

### Design Task
DES-001 — Design Agents tab task-status layout

### Architecture Task
ARCH-### — Define agent status projection model

### Frontend Task
FE-001 — Implement Agents tab status list

### Backend Task
BE-001 — Expose agent task status data

### Agent Task
AGT-001 — Emit task lifecycle status consistently

### Validation Task
VAL-001 — Validate user-visible task status accuracy

### Governance Dependency
GOV-005 — Multi-agent task boundary and status governance

## Validation Notes

- Can the user understand what is happening?
- Is displayed status accurate?
- Are blocked or approval-required states clearly visible?
```
