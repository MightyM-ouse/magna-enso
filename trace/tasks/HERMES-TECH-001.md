# HERMES-TECH-001 — Magna version enso technical assessment

Status: AUTHORIZED  
Issue: #36  
Branch: `chatgpt/HERMES-TECH-001-assessment`  
Prepared by: ChatGPT/System Architect  
Approved by: Product Owner request in planning chat  

---

## 1. Purpose

Create a governed technical assessment packet for `Magna version enso` that reconciles prior Hermes capability assessment evidence with the current Magna-Hermes Runtime Adoption epic, formal product user stories, and the implementation readiness goal for Epic 1.

This task exists because the Product Owner clarified that a detailed Hermes capability assessment was already performed before the `magna-enso` repository was started. The task must therefore recover and correct existing repository evidence rather than restarting from chat memory.

---

## 2. Required source hierarchy

Workers must treat the following as the source hierarchy for this task:

1. Current GitHub state in `MightyM-ouse/magna-enso`.
2. `AGENTS.md`, `CHATGPT.md`, `CLAUDE.md`, `HERMES.md`, `trace/STAR_MAP.md`, `trace/ACTIVE_WORK_REGISTRY.yaml`, and `trace/CELESTIAL_INDEX.json`.
3. `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`.
4. `trace/planning/MAGNA_VERSION_ENSO_TECHNICAL_ASSESSMENT_SCOPE.md`.
5. Existing repository evidence for prior Hermes capability review, including `vendor/hermes/`, `trace/evidence/`, `trace/reviews/`, `trace/tasks/`, and governed archives when routed.
6. Product user stories under `trace/product/` once available.

Chat memory may guide search terms, but it is not canonical evidence.

---

## 3. Assessment questions

The assessment must answer:

1. Which Hermes capabilities were previously assessed as safe to adopt directly?
2. Which capabilities must be wrapped with Magna governance and TRACE controls?
3. Which capabilities should be rebuilt natively in Magna?
4. Which capabilities should be deferred from Magna version enso?
5. Which capabilities are required for Epic 1 readiness?
6. Which capabilities are useful but not necessary for the first usable Magna version enso?
7. What existing Magna Enso governance or TRACE constraints prevent direct adoption?
8. What gaps must be resolved before sprint planning?

---

## 4. Capability categories to assess

Use the decision classes from the technical assessment scope:

- `ADOPT`
- `ADAPT`
- `WRAP_WITH_GOVERNANCE`
- `REBUILD_IN_MAGNA`
- `REJECT`
- `DEFER`

Minimum capability list:

- Terminal execution
- Messaging gateway
- Telegram/WhatsApp support
- Memory
- Skills/self-improvement
- Profiles
- Scheduler/cron
- Delegation/subagents
- MCP/tool integrations
- Command approval and safety controls
- Execution capture/logging
- CLI worker dispatch
- GitHub evidence/update flow
- Notification and approval loop
- Magna Command Center UI integration
- PR #33 Magna identity/logo dependency

---

## 5. Non-goals

This task must not:

- Activate Hermes capabilities.
- Modify runtime code.
- Start Claude, Codex, Antigravity, or Hermes CLI sessions.
- Change app UI implementation.
- Declare final sprint scope.
- Mark product user stories final or design-ready.
- Treat Hermes profiles as security sandboxes.
- Bypass TRACE or Product Owner authority.

---

## 6. Required outputs

This task creates or prepares:

- `trace/assessments/MAGNA_VERSION_ENSO_TECHNICAL_ASSESSMENT_SEED.md`
- `trace/tasks/HERMES-TECH-001-CLAUDE-REVIEW.md`

Claude will use the review packet to provide independent corrections and improvements before final technical specification and sprint planning.

---

## 7. Acceptance criteria

- The assessment seed explains that previous Hermes capability assessment may already exist and must be recovered from GitHub.
- The assessment seed maps current scope to Epic 1 readiness.
- Claude receives a precise review instruction with bounded authority.
- The task remains planning/assessment only and does not activate runtime behavior.
- The next step is clear: after formal product user stories are reviewed, reconcile stories with assessment findings and prepare final design-ready stories plus sprint planning.

---

## 8. TRACE requirements

Backward traceability must link this task to:

- Product Owner request for Magna-Hermes Runtime Adoption.
- PR #34 planning scope.
- Issue #36.
- Prior Hermes capability assessment evidence once found.

Forward traceability must link this task to:

- Claude review packet.
- Product user story correctness review.
- Final approved/design-ready story preparation.
- Future 4-sprint planning.
- Magna version enso Epic 1 readiness.
