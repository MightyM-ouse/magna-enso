# RISK_REGISTER.md — Magna Enso (operating instance)

> Live, in-repo risk tracker. The canonical detail cards (mitigations, owners, links) live in
> `../planning/MAGNA_ENSO_RISK_REGISTER.md`. This file mirrors current status and is updated each sprint.
> Severity: `LOW · MEDIUM · HIGH · CRITICAL` · Status: `OPEN · MITIGATED · ACCEPTED · CLOSED · WATCH`.

## Risk Summary

| ID | Risk | Severity | Likelihood | Status | Owner | Links |
|---|---|---|---|---|---|---|
| R-01 | Hermes reuse / coupling | HIGH | MEDIUM | OPEN | Codex + Human | Sprint 2/4; EH-0005A |
| R-02 | License / dependency / ToS | HIGH | MEDIUM | OPEN | Antigravity + Human | Sprint 2/4 |
| R-03 | Trademark / branding | MEDIUM | MEDIUM | WATCH | Human | Charter §2; brand-assets |
| R-04 | Cloud / provider creep | HIGH | MEDIUM | OPEN | Antigravity | Charter §6; Sprint 5 |
| R-05 | Public exposure | CRITICAL | LOW | OPEN | Antigravity + Human | Sprint 10/11 |
| R-06 | Policy bypass | CRITICAL | MEDIUM | OPEN | Codex + Antigravity | Sprint 3/5 |
| R-07 | Prompt-injection persistence | HIGH | MEDIUM | OPEN | Antigravity + Grok | Sprint 8/11 |
| R-08 | Silent memory mutation | HIGH | LOW | OPEN | Codex + Antigravity | Sprint 8 |
| R-09 | Auto-skill activation | HIGH | LOW | OPEN | Codex + Antigravity | Sprint 8 |
| R-10 | Report-only scheduler drift | MEDIUM | MEDIUM | OPEN | Codex | Sprint 9 |
| R-11 | Fork maintenance | MEDIUM | HIGH | WATCH | Codex | Sprint 4; EH-0005A |
| R-12 | Two-codebase complexity | MEDIUM | MEDIUM | WATCH | Claude + Codex | Sprint 4 |
| R-13 | Overengineering | MEDIUM | HIGH | WATCH | Claude | All sprints |
| R-14 | Scope creep into Satori/Kensho | HIGH | MEDIUM | OPEN | Claude + Human | Roadmap; EH-0009 |
| R-15 | UI/E2E worker feasibility | MEDIUM | MEDIUM | OPEN | Codex + Human | Sprint 13/15; EH-0005B |

## Sprint 1 note

No new risks introduced by the TRACE skeleton. **R-13 (overengineering)** is the one to watch this sprint:
the skeleton is intentionally lean (templates + status + governance only, no speculative structure).
`CRITICAL` risks (R-05 public exposure, R-06 policy bypass) have **no surface yet** — there is no runtime,
no network listener, and no capability path in this repo. They re-activate when runtime work begins (Sprint 4+).

## Sprint 2 note

Sprint 2 read-only audit is accepted. Hermes audited SHA:
`33b1d144590a211100f42aa911fd7f91ba031507`.

Risk posture after Sprint 2:

- R-01 (Hermes reuse / coupling) remains **OPEN**. Hermes is conditionally suitable only and is not approved for direct adoption.
- R-02 (License / dependency / ToS) remains **OPEN**. Top-level MIT was verified in the audit, but full transitive dependency/plugin review remains future work.
- R-06 (Policy bypass) remains **OPEN**. The audit found Hermes lacks one complete policy chokepoint; Sprint 3 governance design is the next recommended preparation step.
- EH-0005B remains **PROPOSED**.
- Sprint 3 remains **NOT STARTED**.
- Sprint 4 remains **NOT STARTED**.
