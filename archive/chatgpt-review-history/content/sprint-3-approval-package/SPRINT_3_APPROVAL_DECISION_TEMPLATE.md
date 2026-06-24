# SPRINT_3_APPROVAL_DECISION_TEMPLATE.md
# Magna Enso — Sprint 3 Approval Decision Template
# Type: Local-only approval package
# Date: 2026-06-17
# Status: READY FOR HUMAN OWNER. Fill in, then a worker may begin Sprint 3 within these bounds.

---

## 1. The 14 decisions

| # | Decision | Recommendation | Your choice |
|---|---|---|---|
| 1 | Should Sprint 3 start? | **Yes** — design-only | ☐ Approve ☐ Defer ☐ Amend: ____ |
| 2 | Design-only, or may include schemas? | **Design-only + illustrative schema sketches** (no executable code) | ☐ Design-only ☐ + schema sketches ☐ Amend: ____ |
| 3 | Approve the six capability states? (`disabled`, `read_only`, `draft_only`, `report_only`, `approval_required`, `active_safe`) | **Approve all six** | ☐ Approve ☐ Amend: ____ |
| 4 | Is default-deny mandatory? | **Mandatory** | ☐ Mandatory ☐ Amend: ____ |
| 5 | Plugin/MCP loading — removed or disabled? | **Disabled unless signed allowlist** (remove dynamic loading) | ☐ Remove ☐ Disable-unless-signed ☐ Amend: ____ |
| 6 | Remote execution backends — removed or disabled? | **Remove** (prefer) or process-disable | ☐ Remove ☐ Disable ☐ Amend: ____ |
| 7 | Messaging gateways — removed or disabled? | **Disabled (T1)** / remove | ☐ Remove ☐ Disable ☐ Amend: ____ |
| 8 | Cloud providers disabled by default? | **Yes (T2)** | ☐ Yes ☐ Amend: ____ |
| 9 | Memory/skill writes draft-only? | **Yes** | ☐ Yes ☐ Amend: ____ |
| 10 | Scheduler report-only? | **Yes** | ☐ Yes ☐ Amend: ____ |
| 11 | Terminal/code execution approval-required (off by default)? | **Yes** | ☐ Yes ☐ Amend: ____ |
| 12 | Delegation disabled in MVP? | **Yes** | ☐ Yes ☐ Amend: ____ |
| 13 | Sprint 4 blocked until Sprint 3 accepted? | **Yes — blocked** | ☐ Yes ☐ Amend: ____ |
| 14 | Antigravity must validate Sprint 3 before acceptance? | **Yes** | ☐ Yes ☐ Amend: ____ |

## 2. Worker assignment (recommended)

- **Claude** — lead governance-design author (taxonomy, states, default-deny, approval-engine concept).
- **Codex** — feasibility input from the Sprint 2 code map (no code; advises what is gateable/removable).
- **Antigravity** — validates: default-deny coverage, bypass-resistance, no scope creep, no implementation.
- **Grok** — second opinion: challenges the chokepoint completeness and surface postures.
- **ChatGPT** — continuity review; updates source-data block.
- **Hermes Agent** — NOT used; remains candidate (EH-0005B PROPOSED).

## 3. Ready-to-sign approval block

```text
I approve Sprint 3 — Capability Governance Design.

Approved scope:
- Design-only (illustrative schema sketches allowed; NO executable code)
- Default-deny is mandatory
- Capability states approved: disabled, read_only, draft_only, report_only, approval_required, active_safe
- Plugin/MCP loading: disabled unless signed allowlist
- Remote execution backends: [remove / disable]
- Messaging gateways: [remove / disable]
- Cloud providers: disabled by default
- Memory/skill writes: draft_only
- Scheduler: report_only
- Terminal/code execution: approval_required, disabled by default
- Delegation: disabled in MVP
- Sprint 4 is BLOCKED until Sprint 3 is accepted
- Antigravity must validate Sprint 3 before acceptance

Hard boundaries:
- No implementation / no fork / no runtime code / no UI / no engine code
- No Hermes build/run/clone/modify; no Hermes source in magna-enso
- No commit, no push, no new branches
- Reports/design only; stop after Sprint 3 design + readiness gates
- Human owner is final authority

Approved by (human owner): ____________________
Date: ____________________
```

## 4. What happens after you sign

1. Claude drafts the governance design (15 deliverables) using the Sprint 2 maps; Codex advises feasibility.
2. Antigravity validates (default-deny coverage + bypass-resistance + design-only).
3. Grok challenges; ChatGPT updates continuity.
4. The Sprint 3 design reports are produced, answering the 10 Sprint 4 readiness gates.
5. `SPRINT_3_LIGHT_CURVE.md` is written; you review and accept (or request changes). **Then Sprint 3 stops.**
6. Sprint 4 (clean governed fork) is considered **separately**, and only after Sprint 3 acceptance.

## 5. If you do not approve

Nothing happens. Baseline stays at Sprint 2 closeout (`94d63ed`); Hermes stays un-forked; Sprint 3 remains gated.
