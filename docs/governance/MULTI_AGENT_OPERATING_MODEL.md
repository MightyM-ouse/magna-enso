# Multi-Agent GitHub Operating Model

## Roles

| Actor | Accountable responsibility | May write | Must not |
|---|---|---|---|
| Product Owner | Scope, priority, acceptance, risk, merge | Decisions/comments | Self-certify technical evidence |
| System Architect/SME | Architecture, task design, review, continuity | Governance/docs branch | Merge or make binding PO decisions |
| Claude | Architecture/specification preparation and consistency | Assigned branch/scope | Self-approve or silently change scope |
| Codex | Implementation, testing, tooling, automated browser QA | Assigned branch/scope | Merge, bypass policy, self-accept |
| Antigravity | Independent QA/security/adversarial validation | Review branch and evidence | Implement the feature under review |
| Hermes | Governed local runtime experiment, later worker | None until activated | Self-enable capabilities or repo writes |

## Delivery lifecycle

1. Product Owner approves objective and functional acceptance intent.
2. System Architect creates a GitHub issue and TRACE task packet.
3. One worker receives one isolated branch/worktree and explicit allowed scope.
4. Worker performs preflight, implementation, checks, and evidence capture.
5. Worker commits/pushes only the assigned branch and opens a draft PR.
6. CI and browser automation run; failures remain visible.
7. An independent reviewer records findings and a recommendation.
8. System Architect checks architecture, traceability, and evidence completeness.
9. Product Owner performs only required product/functional acceptance and merges.

## Branches

- `main`: accepted source only; protected.
- `architect/<TASK-ID>-<slug>`: architecture/governance.
- `agent/claude/<TASK-ID>-<slug>`: Claude work.
- `agent/codex/<TASK-ID>-<slug>`: Codex work.
- `agent/antigravity/<TASK-ID>-<slug>`: independent validation.
- `experiment/hermes/<TASK-ID>-<slug>`: future governed experiments only.

No two workers share a mutable branch. A follow-up correction normally stays on the
author's PR branch; an independent review uses comments or its own review branch.

## Merge

`main` requires a PR, resolved conversations, and squash merge. Required status checks
will be added when CI names are stable. Agents do not merge or bypass repository rules.

