# RISK_REGISTER.md — Magna Enso (operating instance)

> Canonical in-repository risk tracker. Risks must link to requirements, decisions, tasks, tests, and evidence where applicable.
> Severity: `LOW · MEDIUM · HIGH · CRITICAL` · Status: `OPEN · MITIGATED · ACCEPTED · CLOSED · WATCH`.

## Risk Summary

| ID | Risk | Severity | Likelihood | Status | Owner | Links |
|---|---|---|---|---|---|---|
| R-01 | Hermes reuse / coupling | HIGH | MEDIUM | OPEN | Codex + Human | Sprint 2/4; EH-0005A |
| R-02 | License / dependency / ToS | HIGH | MEDIUM | OPEN | Antigravity + Human | Sprint 2/4 |
| R-03 | Trademark / branding | MEDIUM | MEDIUM | WATCH | Human | Charter §2; brand-assets |
| R-04 | Cloud / provider creep | HIGH | MEDIUM | OPEN | Antigravity | Charter §6; Sprint 5 |
| R-05 | Unauthorized public runtime/network exposure | CRITICAL | LOW | OPEN | Antigravity + Human | EH-0019; runtime work |
| R-06 | Policy bypass | CRITICAL | MEDIUM | OPEN | Codex + Antigravity | Sprint 3/5 |
| R-07 | Prompt-injection persistence | HIGH | MEDIUM | OPEN | Antigravity + Grok | Sprint 8/11 |
| R-08 | Silent memory mutation | HIGH | LOW | OPEN | Codex + Antigravity | Sprint 8 |
| R-09 | Auto-skill activation | HIGH | LOW | OPEN | Codex + Antigravity | Sprint 8 |
| R-10 | Report-only scheduler drift | MEDIUM | MEDIUM | OPEN | Codex | Sprint 9 |
| R-11 | Fork maintenance | MEDIUM | HIGH | WATCH | Codex | Sprint 4; EH-0005A |
| R-12 | Two-codebase complexity | MEDIUM | MEDIUM | WATCH | Claude + Codex | Sprint 4 |
| R-13 | Overengineering | MEDIUM | HIGH | WATCH | Claude | All sprints |
| R-14 | Scope creep across stage repositories | HIGH | MEDIUM | OPEN | System Architect + Human | EH-0009; EH-0017 |
| R-15 | UI/E2E worker feasibility | MEDIUM | MEDIUM | OPEN | Codex + Human | Sprint 13/15; EH-0005B |
| R-16 | Public source leaks secrets, personal data, or sensitive evidence | HIGH | LOW | MITIGATED | All workers | EH-0019; GOV-001 |

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

## Sprint 3 note

Sprint 3 — Capability Governance Design accepted as **design/report-only** (EH-0014, 2026-06-17). Antigravity
validated; RC-01…RC-05 applied. No implementation, runtime, or policy-engine code approved.

Risk posture after Sprint 3 (designs exist on paper; nothing enforced yet — enforcement is Sprint 4+):

- R-06 (Policy bypass) remains **OPEN**, but now has an accepted mitigation **design**: default-deny model,
  13-boundary policy chokepoint map, disablement tiers, and a bypass-resistance requirement. Enforcement is
  pending the (separately-approved) Sprint 4 fork + Sprint 5 policy engine.
- R-04 (Cloud creep), R-05 (Public exposure), R-07/R-08/R-09 (memory/skill), R-10 (scheduler drift) each have
  an accepted **governance model** (disabled/draft-only/report-only) but **no enforcement yet** — they
  re-activate as live risks when runtime work begins (Sprint 4+).
- R-01 (Hermes reuse) and R-02 (License/deps) remain **OPEN**; full transitive dependency/plugin review is
  still future work.
- EH-0005B remains **PROPOSED**; Hermes Agent not activated.
- Sprint 4 remains **NOT STARTED / blocked** — requires a separate approval package.

## Sprint 4 note

Sprint 4 baseline preparation is **ACCEPTED** (EH-0015, 2026-06-20). The baseline imports only inert upstream license/manifest
references and Magna-owned retained-surface metadata under `vendor/hermes/`.

Antigravity validation completed with verdict **ACCEPTED_FOR_HUMAN_REVIEW**, 9.8/10, no blocking issues,
and no required corrections. Acceptance does not close enforcement risks.

Risk posture after Sprint 4 acceptance:

- R-01 (Hermes reuse / coupling) remains **OPEN**. The baseline is minimal and inert; no executable Hermes module source is imported.
- R-02 (License / dependency / ToS) remains **OPEN**, but the Sprint 4 static pre-import gate found top-level MIT preserved and no runtime dependencies introduced by the inert baseline.
- R-04/R-05 (cloud/public exposure) remain **OPEN**, with dangerous network surfaces excluded by non-import.
- R-06 (policy bypass) remains **OPEN**. Sprint 4 is structurally safe only; no runtime enforcement exists.
- R-11 (fork maintenance) remains **WATCH**. This is not a full fork; it is a selective vendor provenance baseline.
- EH-0005B remains **PROPOSED**; Hermes Agent not activated.
- Sprint 5 remains **NOT STARTED**.

## GOV-001 note

The source repository is public under EH-0019. This does not close R-05, which concerns runtime exposure. R-16 is mitigated by protected `main`, task-scoped PRs, `.gitignore`, Gitleaks, curated evidence, Actions artifacts for large/raw output, and explicit prohibition on secrets, cookies, browser profiles, and personal data. The initial Gitleaks 8.30.1 history and working-tree scans both passed with exit 0 on 2026-06-24.
