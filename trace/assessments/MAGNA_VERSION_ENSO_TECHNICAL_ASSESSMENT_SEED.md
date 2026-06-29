# Magna version enso — Technical Assessment Seed

Status: preliminary assessment seed  
Task: `HERMES-TECH-001`  
Issue: #36  
Prepared by: ChatGPT/System Architect  

---

## Purpose

This seed starts the governed technical assessment for `Magna version enso`.

It does not replace the prior Hermes capability assessment. The Product Owner clarified that a detailed assessment of safe Hermes capability adoption was already done before the `magna-enso` repository was started. Therefore, the first assessment action is evidence recovery and correction, not reinvention.

Magna version enso should support the Epic 1 loop: user instruction, GitHub instruction, approved-channel command intake, known-instruction matching, safety classification, bounded CLI worker dispatch, worker result capture, GitHub evidence update, user notification, approval/redirection, and TRACE-compliant continuation or closure.

---

## Architecture premise

```text
Magna Enso = product identity, governance authority, TRACE authority, and user experience.
Hermes = candidate runtime provider for selected capabilities.
```

Hermes must not replace Magna identity or authority. Hermes capabilities must be exposed only through Magna-controlled envelopes.

---

## Evidence recovery requirement

Before final decisions are made, the assessment must recover repository evidence for earlier Hermes analysis.

Search targets:

- `vendor/hermes/`
- `trace/evidence/`
- `trace/reviews/`
- `trace/tasks/`
- `docs/architecture/`
- `docs/technical-specifications/`
- routed archive material only when marked historical/noncanonical

Questions to answer:

- Where is prior Hermes capability assessment recorded?
- Which capability decisions were already made?
- Which decisions remain valid after current governance updates?
- Which decisions are stale, unsafe, or incomplete?
- Which decisions must be corrected before sprint planning?

---

## Preliminary capability classification

This table is a starting point for Claude correction. It is not final.

| Capability | Preliminary decision | Reason |
|---|---|---|
| Terminal execution | WRAP_WITH_GOVERNANCE | Required for CLI worker dispatch, but must stay inside approved task and branch boundaries. |
| Messaging gateway | WRAP_WITH_GOVERNANCE | Useful for remote command intake, but command handling must be classified before action. |
| Telegram support | WRAP_WITH_GOVERNANCE | Candidate first approved remote channel. |
| WhatsApp support | DEFER | Useful later; one approved remote channel is enough for first loop unless stories require both. |
| Memory | ADAPT | Useful for continuity, but writes must be visible, reviewable, and policy-gated. |
| Skills/self-improvement | DEFER | Valuable later; too risky for Epic 1 unless limited to proposal/review mode. |
| Profiles | ADAPT | Useful for role separation, but not a security sandbox. |
| Scheduler/cron | DEFER | Useful later; unattended work should not block first version. |
| Delegation/subagents | DEFER | Useful later; Epic 1 can dispatch bounded CLI workers first. |
| MCP/tool integrations | DEFER | Powerful but expands risk surface; needs allowlist policy. |
| Command approval/safety controls | REBUILD_IN_MAGNA or WRAP_WITH_GOVERNANCE | Magna must own authority and safety classification. |
| Execution capture/logging | ADAPT | Required for evidence, normalized into TRACE. |
| CLI worker dispatch | WRAP_WITH_GOVERNANCE | Required for Epic 1 through approved wrappers and known instructions. |
| GitHub evidence/update flow | REBUILD_IN_MAGNA | GitHub/TRACE evidence is Magna authority. |
| Notification and approval loop | ADAPT | Hermes may help notify; Magna owns approval semantics. |
| Command Center UI integration | REBUILD_IN_MAGNA | UI identity and shell belong to Magna Command Center. |
| PR #33 identity/logo dependency | ADOPT_IN_MAGNA | Approved Magna identity direction must be included. |

---

## Epic 1 must-have candidates

- Magna identity wrapper around Hermes runtime messages.
- One approved remote command channel.
- Known-instruction matching.
- Safety classification.
- Approved CLI worker dispatch wrappers.
- Worker result capture.
- GitHub evidence/assessment update.
- User notification and approval loop.
- TRACE forward/backward traceability.
- Controlled continuation or closure.

---

## Likely deferrable candidates

- Additional remote channels beyond the first approved channel.
- Full self-improving skill updates.
- Scheduler/cron automation.
- Broad MCP integrations.
- Multi-level subagent delegation.
- Full memory write automation.
- Multi-channel notification fanout.

---

## Safety boundaries

The assessment must preserve Product Owner final authority, GitHub as durable instruction/evidence source, mandatory TRACE lifecycle control, pause-on-unknown behavior, approval for high-risk actions, bounded worker execution, governed Hermes memory/skills/scheduling/MCP/messaging, and Magna UI/identity ownership.

---

## Claude review focus

Claude must verify this seed against repository evidence and correct it where needed. Special attention must be given to existing Hermes assessment evidence, inactive Hermes provenance boundaries, product user story status, and the goal that Magna version enso should be usable for all Epic 1 functionality rather than a toy prototype.

---

## Next workflow after Claude review

1. Review Product User Story output in GitHub for correctness.
2. Prepare instruction for Claude or Codex to convert stories into final approved/design-ready stories.
3. Reconcile user stories with technical assessment findings.
4. Prepare detailed four-sprint planning.
5. Start implementation only after scope, design, and governance gates are aligned.
