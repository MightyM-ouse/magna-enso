# PRODUCT USER STORY SYSTEM

Status: `PROPOSED`
Owner: Product Owner / Product Management
Applies to: Magna product functionality only
Does not apply to: GitHub execution, branch workflow, CI workflow, agent task packets, governance implementation mechanics

## Purpose

This document defines how Magna product user stories are discovered, written, reviewed, and converted into downstream delivery work.

The goal is to separate two different concerns:

1. **Product user stories** — what Magna should do for the user.
2. **Project / agent execution tasks** — how the repository, agents, validators, branches, and implementation work are managed.

A user story must describe a user-facing Magna capability or experience. It must not be a disguised engineering task.

## Professional responsibility model

In a professional IT product environment, user stories are usually owned by the **Product Owner** or **Product Manager**.

They are normally written collaboratively with:

- Product Owner / Product Manager — accountable for product value, priority, acceptance, and scope.
- Business Analyst — helps clarify workflows, rules, edge cases, and acceptance criteria.
- UX / Product Designer — contributes user flows, usability expectations, and interaction details.
- Solution Architect — checks feasibility, boundaries, dependencies, and architectural fit.
- Engineering Lead / Developers — help split stories, estimate effort, identify implementation constraints.
- QA / Validation Engineer — converts acceptance criteria into testable validation scenarios.
- Scrum Master / Delivery Lead — facilitates backlog refinement and sprint readiness, but does not usually own story content.

For Magna, the Product Owner is the final authority. ChatGPT/System Architect may help structure and refine stories, but should not invent product intent without Product Owner confirmation.

## Required chat behavior for user-story discovery

When a new ChatGPT session is used for product user-story discovery, it should:

1. Rename or label the chat conceptually as:

   `Magna — Product User Stories`

2. Read this repository guidance before creating stories:

   - `trace/planning/PRODUCT_USER_STORY_SYSTEM.md`
   - `trace/planning/PRODUCT_USER_STORY_TEMPLATE.md`
   - `trace/planning/PRODUCT_BACKLOG_ID_RULES.md`

3. Interview the Product Owner first.
4. Ask about user goals, workflows, pain points, expected outcomes, and priority.
5. Create product stories only after enough product intent is known.
6. Keep project execution tasks separate from product stories.
7. Mark missing information as open questions instead of assuming.
8. Ask for Product Owner confirmation before finalizing story sets.

## Product story vs project task

### Product user story

A product user story describes what Magna does for the user.

Example:

```text
As a Magna user, I want to see when an agent is blocked and why, so that I know what decision is required from me before work can continue.
```

### Project / agent execution task

A project task describes how the repository or agents implement, validate, or manage the work.

Example:

```text
GOV-005-CF5: Update the ownership validator to reject cross-task file modifications.
```

The project task can support the product story, but it is not itself the user story.

## User-story hierarchy

Use this hierarchy:

```text
MAG-EPIC-###
  MAG-US-###
    DES-###
    ARCH-###
    FE-###
    BE-###
    AGT-###
    VAL-###
    GOV-### only when governance visibility is user-facing or dependency-relevant
```

## Magna capability areas

User stories should be grouped by Magna product areas:

- Command
- Identity
- Agents
- Memory
- Explorer
- Cognition
- Cosmos
- Help
- Settings
- System
- Governance Visibility
- Approval Flow
- Task Awareness

Stories must remain specific to Magna functionality.

## Readiness rules

A product user story is `READY_FOR_REFINEMENT` when it has:

- clear user role,
- user-facing capability,
- user value,
- expected user flow,
- acceptance criteria,
- out-of-scope boundaries,
- known dependencies,
- open questions captured.

A story is `READY_FOR_AGENT_TASKING` only after:

- Product Owner confirms the story,
- acceptance criteria are testable,
- dependencies are known,
- downstream task placeholders are assigned,
- validation expectations are defined.

## Prohibited story patterns

Do not create product user stories like:

```text
As a developer, I want to update a validator script so that CI passes.
```

```text
As Claude, I want to modify a branch so that GOV-005 is completed.
```

```text
As GitHub, I want to merge a PR so that the repository is updated.
```

These are project execution tasks, not Magna product stories.

## Correct story pattern

Use stories like:

```text
As a Magna user, I want to see which agent is waiting for my approval, so that I can decide whether work should continue, pause, or stop.
```

Then link downstream work separately:

```text
Frontend Task: FE-###
Backend Task: BE-###
Agent Task: AGT-###
Validation Task: VAL-###
Governance Dependency: GOV-###
```

## Chat handoff prompt

For a short new-chat prompt, use:

```text
Name this chat: Magna — Product User Stories.
Read the product user-story guidance from the Magna repository, especially trace/planning/PRODUCT_USER_STORY_SYSTEM.md, trace/planning/PRODUCT_USER_STORY_TEMPLATE.md, and trace/planning/PRODUCT_BACKLOG_ID_RULES.md.
Act as a Product Analyst and Product Owner assistant. Interview me first. Create user stories only for Magna product functionality, not project execution or GitHub workflow. Keep downstream engineering, agent, and validation tasks separate from the user stories.
Start by asking me what I want Magna to do for the user.
```
