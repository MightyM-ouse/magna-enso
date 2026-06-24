# Agent Routing and Dispatch

## Purpose

Select the smallest capable agent set for each task, preserve independent review, and make
the routing recommendation visible to the Product Owner before dispatch.

ChatGPT owns orchestration and recommends the route. The Product Owner retains scope,
priority, risk, merge, and release authority.

## Agent responsibilities

| Agent | Primary use | Do not use as |
|---|---|---|
| ChatGPT | System architecture, synchronization, task framing, routing, integration sequencing, evidence review, Product Owner briefing | Routine coding worker or self-approver |
| Claude | Architecture, requirements, specifications, governance design, consistency review, four-eyes architecture review | Independent reviewer of work Claude primarily implemented |
| Codex | Repository investigation, implementation, refactoring, migrations, tests, tooling, CI, browser automation | Product/architecture authority or self-reviewer |
| Antigravity | Independent QA, adversarial/security validation, architecture conformance, UI/browser validation, evidence verification | Primary implementer of the feature it validates |
| Hermes | Future bounded local-model experiments, repetitive sandboxed research/verification, governed runtime evaluation | Any task while inactive; canonical authority; unrestricted repository/system actor |

Hermes remains unavailable until a Product Owner-approved capability-lab task activates a
specific sandbox, tools, paths, policy gate, audit trail, and independent reviewer.

## Routing decision

Choose agents in this order:

1. Identify the outcome: architecture, implementation, validation, investigation, or
   governed experiment.
2. Check whether an accepted specification already exists.
3. Determine whether implementation and independent review must be separated.
4. Check current agent activity, ownership, branch state, and integration dependencies.
5. Select the smallest capable primary agent and reviewer.
6. Confirm the selected agent is authorized and active.
7. Explain the recommendation to the Product Owner using the response template.

## Default routing matrix

| Task type | Primary | Independent review | Notes |
|---|---|---|---|
| Product requirement or architecture design | Claude | ChatGPT, plus Antigravity for high-risk conformance | ChatGPT frames and integrates; Product Owner decides |
| Governance policy or operating model | ChatGPT or Claude, whichever did not author the proposal | The other of ChatGPT/Claude | Avoid author-only acceptance |
| Backend/frontend implementation | Codex | Antigravity | Claude participates when architecture or specification changes |
| Refactoring with unchanged behavior | Codex | Antigravity when shared/high-risk | Require tests and contract evidence |
| CI, tooling, migrations, automation | Codex | Antigravity for destructive/security-sensitive work | Preserve rollback and provenance |
| Independent code/security/QA review | Antigravity | ChatGPT synthesizes | Antigravity must not be original implementer |
| Architecture-conformance review | Claude or Antigravity | ChatGPT synthesizes | Choose Claude for design semantics, Antigravity for executable evidence |
| UI implementation | Codex | Antigravity | Claude reviews material UX/information-architecture changes |
| Repository/process status reconciliation | ChatGPT | Claude for material governance changes | No coding agent needed for deterministic status-only reconciliation |
| Exploratory local-model experiment | Hermes after activation | Antigravity, then ChatGPT | Never route while Hermes is inactive |

## Common delivery patterns

### Architecture-to-code

1. ChatGPT verifies state and frames the outcome.
2. Claude develops or reviews architecture/specification.
3. Product Owner accepts the design boundary when required.
4. Codex implements on its own branch.
5. Antigravity independently validates.
6. ChatGPT issues the merge recommendation.
7. Product Owner merges.

### Code defect

1. ChatGPT verifies and routes.
2. Codex investigates root cause and implements the correction.
3. Antigravity validates regression/security behavior when risk warrants it.
4. ChatGPT reviews evidence and recommends the next gate.

### Governance change

1. ChatGPT or Claude authors.
2. The non-author performs four-eyes review.
3. Antigravity is added when enforcement or bypass resistance must be tested.
4. Product Owner merges after ChatGPT synthesis.

### Hermes experiment

1. ChatGPT defines a bounded capability-lab proposal.
2. Claude reviews containment and architecture.
3. Product Owner explicitly activates the limited envelope.
4. Hermes executes only inside that sandbox.
5. Antigravity validates effects and evidence.
6. ChatGPT reports; no result becomes canonical automatically.

## Proactive recommendation rule

ChatGPT must recommend an agent when a task would benefit from a specialized worker. The
recommendation states:

- primary agent and exact purpose;
- independent reviewer and why;
- tasks that may run concurrently;
- dependencies that require sequencing;
- whether the agent is active/authorized; and
- the next repository gate before dispatch.

Do not route an agent merely because it is available. Do not use multiple agents when one
can safely complete the outcome. Do not sacrifice four-eyes independence for speed.

## Dispatch rule

The full worker instruction lives in GitHub. ChatGPT provides the Product Owner only a
short launch message referencing the task path. Before dispatch, verify:

- `SYNC_PASS`;
- repository instruction exists at the stated path;
- accountable-worker branch prefix is correct;
- active ownership does not overlap;
- task authority and escalation boundaries are explicit; and
- the completion handoff is defined.
