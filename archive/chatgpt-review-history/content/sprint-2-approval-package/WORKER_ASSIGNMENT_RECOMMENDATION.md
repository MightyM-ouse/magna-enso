# WORKER_ASSIGNMENT_RECOMMENDATION.md
# Magna Enso — Sprint 2 Worker Assignment Recommendation
# Type: Local-only approval package
# Date: 2026-06-17
# Status: RECOMMENDATION for human approval. Sprint 2 NOT started.

---

## 1. Purpose

Define clear, bounded worker roles for Sprint 2 (Hermes Read-Only Audit) so each worker knows exactly
what it does and does not do. Roles are **advisory / role-guided** in v1 (honored by instruction and
human review), not technically enforced isolation. No worker self-approves; the **human owner is the
final authority** (EH-0010).

## 2. Roles at a glance

| Worker | Sprint 2 role | Modifies code? | Runs Hermes? | Self-approves? |
|---|---|---|---|---|
| **Codex** | Primary code inspector | No | No | No |
| **Antigravity** | Validation & safety reviewer | No | No | No |
| **Claude** | Architecture / governance interpreter | No | No | No |
| **Grok** | Second-opinion reasoning challenger | No | No | No |
| **ChatGPT** | Continuity / orchestration review | No | No | No |
| **Hermes Agent** | **Not used** — candidate only | No | No | No |

## 3. Role definitions

### 3.1 Codex — primary code inspector
- Maps repository structure, modules, and dependencies.
- Maps action dispatch and autonomy paths (memory writes, skill writes, scheduler/cron, external surfaces).
- **Does not modify code. Does not run/build Hermes.** Read-only inspection in the scratch clone only.
- Produces the **draft audit reports** (per `SPRINT_2_OUTPUT_REPORTS_SPEC.md`), citing file paths + commit SHA.

### 3.2 Antigravity — validation & safety reviewer
- Validates the draft reports and that the governance gates held throughout the sprint.
- Checks **no source leakage** (no Hermes source pasted into reports), **no scope creep** (nothing beyond
  the 14 audit questions), and **no Hermes source inside `magna-enso/`**.
- Gates acceptance: Sprint 2 is not accepted until Antigravity validation passes.
- Does not write code; does not approve its own validation.

### 3.3 Claude — architecture / governance interpreter
- Reviews findings against Magna Enso principles (capability-policy gateability, local-first/LAN-first,
  human authority, default-deny feasibility).
- Shapes the reuse recommendation and evidence framing.
- **Does not inspect as an implementation worker** and does not write runtime code.
- **Does not self-approve** — interprets and recommends; the human owner decides.

### 3.4 Grok — second-opinion reasoning challenger
- Independently challenges the reuse recommendation, the risk assumptions, and any **hidden coupling**
  that an inspector close to the code might miss.
- Surfaces abuse cases and alternative interpretations; makes the "is Hermes suitable?" answer robust.
- Does not modify repo artifacts; makes no binding decisions.

### 3.5 ChatGPT — continuity / orchestration review
- Reviews the final Sprint 2 output using the agent review template.
- Updates the external **source-data block** (`../AGENT_OUTPUT_REVIEW_SOURCE_DATA.md`) — local-only memory.
- Checks handoff coherence across workers. Makes no binding governance decisions; modifies no code.

### 3.6 Hermes Agent — not used in Sprint 2
- **Does not perform the audit.** It remains a **candidate** UI/E2E worker only.
- **EH-0005B remains PROPOSED.** Using the artifact-under-evaluation to evaluate itself is a conflict of
  interest and an unjustified activation; explicitly excluded from Sprint 2.

## 4. Separation of duties

Distinct workers **inspect**, **validate**, **interpret**, **challenge**, and **decide** — no single
worker does more than one of these for the same conclusion:
- Inspector (Codex) produces facts → Validator (Antigravity) independently checks facts + safety →
  Governance (Claude) interprets → Challenger (Grok) stress-tests → Continuity (ChatGPT) records →
  **Human owner decides.**
This prevents any worker from both producing and approving its own work.

## 5. Handoff order

```text
1. Codex      — inspect (read-only) → draft audit reports + provenance/SHA
2. Antigravity — validate reports + governance gates (no leakage / no scope creep / no source in magna-enso)
3. Claude      — interpret findings vs Magna Enso principles; shape reuse recommendation
4. Grok        — challenge reuse recommendation, risk assumptions, hidden coupling
5. ChatGPT     — continuity review (agent review template) + update source-data block
6. (worker)    — write SPRINT_2_LIGHT_CURVE.md (evidence; status in_review, human approval pending)
7. Human owner — review and accept (or request changes) → Sprint 2 stops
```

Continuity is preserved in the repository/reports (TRACE Repository Sovereignty); no worker depends on
another worker's chat memory.

## 6. Final acceptance rule

Sprint 2 is accepted **only** when: all audit reports exist, **Antigravity validation passes**, the
`SPRINT_2_LIGHT_CURVE.md` is written, and the **human owner explicitly signs off**. No worker
self-approves; Antigravity's validation is input, not acceptance.

## 7. Human authority statement

**The human owner (Vinay) is the final authority** (EH-0010) for accepting Sprint 2, for any decision to
later commit the reports, and for authorizing Sprint 3. Antigravity recommends; Claude interprets; none of
them approve on the human owner's behalf.
