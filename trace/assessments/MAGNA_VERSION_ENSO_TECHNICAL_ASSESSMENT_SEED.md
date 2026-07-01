# Magna version enso — Technical Assessment Seed

Status: corrected assessment seed — Claude ACCEPT_WITH_CORRECTIONS applied 2026-06-30
Task: `HERMES-TECH-001`
Issue: #36
Prepared by: ChatGPT/System Architect
Corrections applied by: Claude (HERMES-TECH-001-CORRECTIONS, branch `claude/HERMES-TECH-001-corrections`)

---

## Purpose

This seed starts the governed technical assessment for `Magna version enso`.

It does not replace the prior Hermes capability assessment. The Product Owner clarified that a detailed assessment of safe Hermes capability adoption was already done before the `magna-enso` repository was started. Therefore, the first assessment action is evidence recovery and correction, not reinvention.

Magna version enso supports the Epic 1 loop with **local Magna-controlled orchestration as the primary flow**: user instruction, known-instruction matching, safety classification, bounded CLI worker dispatch, worker result capture, GitHub evidence update, Magna review and verification, short chat verdict summary, complete GitHub verdict and next-action suggestions, and user approval/redirection/stop. Telegram remote intake is activation-gated and is not part of the default Epic 1 automatic execution path.

---

## Product Story Baseline Status

Formal product user stories for the Magna-Hermes Runtime Adoption epic were reviewed, corrected per Product Owner CHANGES_REQUIRED, and merged to `main` in PR #35 (squash merge 2026-06-30, commit `454c91950b22106d9d88faa7e567a0ba3330d8b2`).

The merged product story baseline (`trace/product/PRODUCT_STORY_INDEX.md` and 10 stories under `trace/product/user-stories/`) establishes:

- The RETAIN_DISABLED_BY_DEFAULT capability model for advanced non-default capabilities.
- Epic 1 local-first 13-step primary flow (local Magna-controlled orchestration first).
- Telegram remote intake as activation-gated with 5 required authorization gates.
- Telegram User ID allowlist as the approved sender boundary (unknown user IDs are rejected or paused, never executed).
- Strong Internal TRACE requirement: TRACE inside Magna (live) and in GitHub (durable).
- Split verdict/next-action output: short chat verdict summary + complete GitHub record.
- PR #33 (Magna animated identity/branding) remains an unresolved dependency for Story 001.

The next step for this assessment is to reconcile the assessment findings with the merged product story baseline.

---

## Architecture premise

```text
Magna Enso = product identity, governance authority, TRACE authority, and user experience.
Hermes = candidate runtime provider for selected capabilities.
```

Hermes must not replace Magna identity or authority. Hermes capabilities must be exposed only through Magna-controlled envelopes.

---

## RETAIN_DISABLED_BY_DEFAULT Capability Model

Advanced Hermes-derived capabilities that are not part of the default Epic 1 flow are **RETAIN_DISABLED_BY_DEFAULT** in Magna version enso. This means:

- The capability remains in the Magna capability model.
- It is **disabled by default** and not part of Epic 1 automatic execution.
- It may be enabled later by explicit Product Owner or user action from Magna UI.
- Any enablement must still pass Magna permissions, policy gates, audit, and TRACE requirements.
- RETAIN_DISABLED_BY_DEFAULT capabilities must appear in the Magna Command Center UI with their status (disabled by default), reason, required activation gates, and whether the user can request enablement.

RETAIN_DISABLED_BY_DEFAULT replaces the prior `DEFER` classification where evidence confirms the capability should remain in the model but not activate automatically.

---

## Epic 1 Primary Flow (Local Magna-Controlled Orchestration First)

Epic 1 prioritizes local Magna-controlled orchestration:

```
1.  User starts Magna.
2.  User gives instruction to Magna.
3.  Magna understands and routes the instruction.
4.  Magna checks for a known instruction match.
5.  Magna classifies the action.
6.  Magna calls Claude or Codex according to approved worker policy.
7.  Claude or Codex performs the task.
8.  Worker output and evidence are written or proposed in GitHub.
9.  Magna reviews worker changes and evidence.
10. Magna verifies the task outcome.
11. Magna provides a short verdict summary in chat.
12. Magna writes or proposes the complete verdict and next-action suggestions in GitHub.
13. Magna summarizes recommended next actions and waits for user approval, redirection, or stop.
```

Telegram remote-triggered execution is activation-gated and not part of this default flow. It requires all 5 activation gates (see Telegram Activation Gates below) before real execution can proceed.

---

## Strong Internal TRACE Requirement

TRACE is enforced inside Magna itself (live internal state) as well as in GitHub (durable evidence record):

```
If it happened in Magna, it must be traceable in Magna.
If it matters for project history, it must also be durable in GitHub.
```

Every meaningful Magna action must create or update a TRACE event before the action can proceed. No worker dispatch, evidence write, verdict, next-action suggestion, continuation, or closure can occur without an active TRACE envelope. GitHub evidence links to the Magna TRACE task ID. Chat summaries reference the TRACE/evidence ID.

---

## Telegram Activation Gates

Telegram remote-triggered execution requires all 5 of the following authorization gates to be satisfied before real execution can proceed:

1. R-06 runtime policy chokepoint is fixed and verified.
2. Messaging gateway surface is explicitly re-authorized by Product Owner (currently DISABLED/REMOVE per Sprint 3/4 MVP design).
3. An approved sender boundary exists: Telegram User ID allowlist (commands from unknown or unlisted user IDs are rejected or paused immediately, never executed; token-only authentication is not sufficient).
4. An authenticated approval-channel design is accepted (OD-HRM.3 resolved).
5. TRACE evidence and audit for the messaging surface are verified.

Until all 5 gates are satisfied, Telegram is intake-only: Magna may receive and acknowledge commands but must not trigger worker execution.

---

## Evidence Recovery Requirement

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

## Prior Assessment Evidence Recovered

Claude's independent review (2026-06-30, `trace/reviews/HERMES-TECH-001-CLAUDE-REVIEW.md`) recovered the following prior Hermes capability assessment evidence from the archive and vendor provenance:

**Sprint 2 — Source architecture audit:**
`archive/.../sprint-2-hermes-audit/HERMES_CODE_MAP.md` — Full Hermes source architecture audit at SHA `33b1d144`. Identified 9 module categories, flagged risky modules (messaging gateways, terminal execution, memory writes, skills/self-improvement, MCP dynamic loading). Classification: `STALE_OR_NONCANONICAL_EVIDENCE` (historical design reference).

**Sprint 3 — Per-surface governance design (primary prior assessment):**
`archive/.../sprint-3-capability-governance-design/HERMES_SURFACE_GOVERNANCE_MATRIX.md` and `HERMES_SURFACE_GOVERNANCE_PLAN.md` — Per-surface MVP state, enforcement tier, and Sprint 4 actions (retain/disable/remove). This is the most detailed prior capability assessment. Key decisions:
- Messaging gateways: `disabled / REMOVE` (T1 — highest disablement tier).
- Terminal execution: `approval_required`, disabled by default (T4 gate).
- Memory: `draft_only` (writes staged, never auto-activate; external memory sync disabled/REMOVE).
- Skills/self-improvement: `draft_only` (skill writes); background review `disabled/REMOVE`; curator `report_only`.
- Scheduler/cron: `report_only` (proposals only, never auto-executes). Direct script cron: `REMOVE`.
- Delegation/subagents: `disabled` in MVP.
- MCP/tool integrations: `disabled unless signed allowlist`.
Classification: `STALE_OR_NONCANONICAL_EVIDENCE` (historical design reference, decisions carried forward into Sprint 4 canonical state).

**Sprint 4 — Quarantined inert provenance baseline:**
`vendor/hermes/README.md` and `vendor/hermes/retained/RETAINED_SURFACE_STATES.yaml` — Implemented Sprint 3 governance decisions; messaging gateways removed/disabled, terminal disabled by default, memory/skills `draft_only`, scheduler `report_only`. Machine-readable record of what was retained and why. Classification: `ACCEPTED_GITHUB_EVIDENCE` (on `main`).

Decision trail: EH-0005A, EH-0013, EH-0014, EH-0015 (from `archive/.../magna-program-discovery-reconstruction/07_CAPABILITY_AND_HERMES_ADOPTION_INVENTORY.md`).

**HERMES-001 Sandbox Readiness** (`trace/reviews/HERMES-001-SANDBOX-READINESS.md`): Planning-only role assessment for Hermes as a documentation/evidence assistant. Does NOT cover operational runtime capabilities. Classification: `ACCEPTED_GITHUB_EVIDENCE`.

**Architecture draft (noncanonical):** `archive/.../HERMES_DERIVED_CAPABILITY_PLAN.md` — 8-capability table, four adoption layers, open decisions OD-HRM.1 through OD-HRM.3. Classification: `STALE_OR_NONCANONICAL_EVIDENCE`.

**Sprint 5 — Policy engine (local-only, unverified):** 9 Python modules under `policy/` and 49 unit tests under `tests/policy/`, with evidence at `trace/evidence/ENSO-0005_LIGHT_CURVE.md`. Implements Magna-native default-deny policy engine. No Hermes runtime imports. All 49 tests pass locally. Status: `LOCAL_ONLY_UNVERIFIED_UNTIL_COMMITTED` — not on `main`, not accepted, Antigravity validation and human acceptance pending. Classification: `RECOMMENDED_FOR_CURATED_IMPORT` on a dedicated `sprint/05-policy-engine` branch after Antigravity validation.

---

## Preliminary Capability Classification

This table reflects Claude's corrected assessment. It supersedes the original preliminary classification.

| Capability | Decision | Basis |
|---|---|---|
| Terminal execution | WRAP_WITH_GOVERNANCE | Sprint 3: `approval_required`, disabled by default (T4 gate). Sprint 4: `approval_required_disabled` in `RETAINED_SURFACE_STATES.yaml`. Must add: separate activation gate required; policy engine must be verified before activation. |
| Messaging gateway | WRAP_WITH_GOVERNANCE — requires new explicit activation decision | Sprint 3: messaging gateways `disabled / REMOVE` (T1 — highest disablement tier). Currently DISABLED. Re-enabling any messaging surface (including Telegram) requires explicit Product Owner re-authorization as first gate. |
| Telegram support | WRAP_WITH_GOVERNANCE — requires explicit activation decision and all 5 gates | Telegram is part of `messaging` optional extra in Hermes (`python-telegram-bot`). Not imported in vendor baseline. Epic 1 candidate intake channel; all 5 activation gates must be satisfied before real execution. |
| WhatsApp support | RETAIN_DISABLED_BY_DEFAULT | Sprint 3: messaging gateways disabled. One approved channel is sufficient for Epic 1. Remains in Magna capability model, disabled by default. |
| Memory | WRAP_WITH_GOVERNANCE (`draft_only` staging required) | Sprint 3: `draft_only` — writes staged, never auto-activate. External memory sync `disabled/REMOVE`. ADAPT understates the constraint; memory writes must be staged and non-bypassable. |
| Skills/self-improvement | RETAIN_DISABLED_BY_DEFAULT | Sprint 3: `draft_only` skill writes; background review `disabled/REMOVE`; curator `report_only`. Too risky for Epic 1 default flow. Remains in Magna capability model, disabled by default. |
| Profiles | ADAPT | Hermes profiles are useful for role separation but must be explicitly documented as NOT security sandboxes. Magna governance is the authority boundary. |
| Scheduler/cron | RETAIN_DISABLED_BY_DEFAULT | Sprint 3: `report_only` (proposals only, never auto-executes). Direct script cron: `REMOVE`. Auto-execution remains RETAIN_DISABLED_BY_DEFAULT. Report-only mode acceptable if surfaced at all. |
| Delegation/subagents | RETAIN_DISABLED_BY_DEFAULT | Sprint 3: `disabled` in MVP. Sprint 4: `subagent_delegation` excluded. Excluded from Sprint 3/4 MVP; remains in Magna capability model, disabled by default. |
| MCP/tool integrations | RETAIN_DISABLED_BY_DEFAULT | Sprint 3: `disabled unless signed allowlist`. Sprint 4: `plugin_mcp_dynamic_loading` excluded. Dynamic MCP loading must remain disabled until signed allowlist policy exists. Remains in Magna capability model, disabled by default. |
| Command approval/safety controls | REBUILD_IN_MAGNA | Sprint 3: policy gate (P-03/P-04) designed. Sprint 5 (local, unverified): Magna-native policy engine candidate exists under `policy/`. Sprint 5 must be reviewed and accepted before the policy engine is assumed ready. Ambiguity removed: this is REBUILD_IN_MAGNA, not WRAP_WITH_GOVERNANCE. |
| Execution capture/logging | ADAPT | Sprint 3: TRACE evidence required for every action. Normalize into TRACE format; JSONL audit chain is the Sprint 5 candidate approach. |
| CLI worker dispatch | WRAP_WITH_GOVERNANCE | Sprint 2: `agent/tool_executor.py` is policy insertion point. Sprint 3: tool registry governed. Worker selection must go through known-instruction registry and approved wrappers. |
| GitHub evidence/update flow | REBUILD_IN_MAGNA | Hermes has no GitHub evidence update mechanism. TRACE is Magna authority. GitHub/TRACE evidence is Magna-native. |
| Notification and approval loop | ADAPT | Hermes messaging surfaces are disabled. Notification must re-authorize channel (Telegram). Approval semantics are Magna-owned. Direction correct; depends on messaging re-authorization. |
| Command Center UI integration | REBUILD_IN_MAGNA | Magna Command Center is a separate repository. No Hermes UI is appropriate. UI identity and shell belong to Magna Command Center. |
| PR #33 identity/logo dependency | ADOPT (prerequisite dependency) | PR #33 introduces animated Magna identity; this is a branding prerequisite, not a Hermes capability decision. Must not be assumed merged until GitHub confirms. Story 001 remains dependent on branding acceptance. |

---

## Epic 1 Must-Have Candidates

- Magna identity wrapper around Hermes runtime messages.
- One approved remote command channel (Telegram, activation-gated).
- Known-instruction matching.
- Safety classification.
- Approved CLI worker dispatch wrappers.
- Worker result capture.
- GitHub evidence/assessment update.
- User notification and approval loop.
- TRACE forward/backward traceability.
- Controlled continuation or closure.
- Strong Internal TRACE (live Magna state + durable GitHub record).

---

## RETAIN_DISABLED_BY_DEFAULT Candidates

The following capabilities are retained in the Magna capability model but disabled by default in Magna version enso. They are not part of the Epic 1 default flow. They may be enabled later through explicit Magna UI action, subject to all required activation gates:

- Additional remote channels beyond Telegram (e.g., WhatsApp).
- Full self-improving skill updates (background review, curator).
- Scheduler/cron auto-execution.
- Full memory write automation.
- Multi-level subagent delegation.
- MCP/tool integrations (dynamic loading).
- Browser actions.
- Remote execution backends (cloud, SSH).
- Multi-channel notification fanout.
- Cloud provider activation.
- Telegram-triggered remote execution (intake-only until all 5 authorization gates are met).

---

## Safety Boundaries

The assessment must preserve Product Owner final authority, GitHub as durable instruction/evidence source, mandatory TRACE lifecycle control, pause-on-unknown behavior, approval for high-risk actions, bounded worker execution, governed Hermes memory/skills/scheduling/MCP/messaging, and Magna UI/identity ownership.

No RETAIN_DISABLED_BY_DEFAULT capability may activate without explicit Product Owner or user action through Magna UI after all required activation gates are satisfied.

---

## Open Risks and Unresolved Decisions

| ID | Risk / Decision | Status |
|---|---|---|
| R-06 | Runtime policy chokepoint not verified — no confirmed path from policy engine to real capability enforcement. Blocks Telegram real execution. Carried forward from Sprint 4/5. | OPEN — must be resolved before any real capability activation |
| OD-HRM.3 | Authenticated approval channel for capability activation not designed (required for approval-required capabilities before any activation). | OPEN — unresolved |
| OD-HRM.1 | Local model/provider for Hermes runtime not selected. | OPEN |
| PR #33 | Magna animated identity/branding. Story 001 dependent on acceptance. | OPEN — unresolved dependency; do not assume merged until GitHub confirms |
| Sprint 5 | Policy engine is local-only, unreviewed by Antigravity, not accepted. Informs Epic 1 design but must not be assumed accepted. | OPEN — pending Antigravity validation and human acceptance |
| GOV-005 | Not yet merged to main. Epic 1 technical specification depends on final governance framework being accepted. | OPEN — READY_FOR_PRODUCT_OWNER |
| GOV-006 | Not yet merged to main. Agent routing contract not finalized. | OPEN — PUSHED_FOR_REVIEW |
| HERMES-ADOPT-001 | PR #34 not yet merged. Planning brief not formally accepted; HERMES-TECH-001 is downstream. | OPEN — PUSHED_FOR_REVIEW |

---

## Claude Review Focus

Claude reviewed this seed on 2026-06-30 (`trace/reviews/HERMES-TECH-001-CLAUDE-REVIEW.md`, branch `claude/HERMES-TECH-001-review`). Verdict: **ACCEPT_WITH_CORRECTIONS**. The corrections in this document apply the Claude review findings.

Key review findings applied:
- F-01: Added prior Sprint 2/3/4 archive assessment evidence (section "Prior Assessment Evidence Recovered").
- F-02: Corrected messaging gateway classification (currently DISABLED per Sprint 3/4, not WRAP_WITH_GOVERNANCE).
- F-03: Corrected memory classification (ADAPT → WRAP_WITH_GOVERNANCE, `draft_only` staging).
- F-04: Clarified command approval/safety controls (REBUILD_IN_MAGNA, ambiguity removed).
- F-05/F-06: Updated product user story status (PR #35 merged; Sprint 5 local-only noted).
- F-10: Corrected PR #33 classification (ADOPT_IN_MAGNA → ADOPT, prerequisite dependency).
- F-11: Added OD-HRM.3 to open risks.
- F-12: Added R-06 to open risks.

Post-review corrections also applied per PR #35 merged product story baseline:
- RETAIN_DISABLED_BY_DEFAULT model replaces bare `DEFER` for 5 capabilities.
- Epic 1 local-first 13-step primary flow added.
- Strong Internal TRACE requirement added.
- Telegram activation gates (5 gates) added.
- Telegram User ID allowlist sender boundary added.
- Split verdict/next-action output model noted.

---

## Next Workflow After Assessment Corrections

1. Reconcile merged product user stories (PR #35, `trace/product/PRODUCT_STORY_INDEX.md`) with the corrected assessment findings above.
2. Prepare instruction for Claude or Codex to convert stories into final approved/design-ready stories.
3. Prepare detailed four-sprint planning.
4. Start implementation only after scope, design, and governance gates are aligned.

**Prerequisites before sprint planning:**
- GOV-005 and GOV-006 merged to main.
- HERMES-ADOPT-001 (PR #34) reviewed and accepted by Product Owner.
- Sprint 5 policy engine reviewed and accepted (Antigravity validation + human acceptance).
- Messaging gateway re-authorization decision made.
- R-06 resolved (verified policy-to-capability chokepoint).
- OD-HRM.3 resolved (authenticated approval channel design accepted).
- PR #33 confirmed merged (or branding dependency path resolved).
