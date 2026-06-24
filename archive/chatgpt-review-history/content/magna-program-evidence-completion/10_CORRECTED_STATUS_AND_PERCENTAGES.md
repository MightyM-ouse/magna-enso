# Corrected Status and Percentages

All metrics are unweighted item counts unless stated. They are not interchangeable and must not be combined into an overall completion percentage.

| Metric | Numerator / denominator | Result | Source and limitation | Confidence |
|---|---:|---:|---|---|
| Pre-SGN accepted readiness | 3 accepted/frozen layers / 6 belt layers | **50.0%** | HAB, ATM, CSF accepted; BRS implemented/validated but no acceptance; MEM/NRV pending | High |
| Pre-SGN code + current validation | 4 / 6 | **66.7%** | Adds BRS; not a completion/acceptance metric | High |
| Enso accepted-sprint completion | 4 accepted sprints / 15 planned sprints | **26.7%** | Sprints are equal-weighted despite unequal size | High |
| Enso accepted-backlog completion | 4 DONE features / 17 tracked features | **23.5%** | Tracker feature items are equal-weighted | High |
| Enso verified runtime completion | 0 accepted, runtime-integrated features / 13 post-foundation feature items | **0.0%** | Sprint 5 has two locally validated harness features but no real runtime integration or acceptance | High |
| Architecture readiness | 8 satisfied / 12 defined gates | **66.7%** | Gates: identity/scope, UI shell, API, persistence, event lineage, approval, observability, provider adapters satisfied; canonical policy choice, TRACE contract, production deployment, environment model open. Audit-defined equal weights. | Medium |
| UX readiness | 6 / 10 gates | **60.0%** | Shell, active task/history, workflow, approvals/recovery, settings/status, build pass; accessibility, responsive verification, visual regression, production usability evidence open | Medium |
| Environment readiness | 2 / 7 environments | **28.6%** | Local/dev and test evidenced; integration environment, staging, UAT, production, DR absent | High |
| Backlog readiness | 7 / 10 gates | **70.0%** | Enso backlog/AC/evidence/risk/decisions + Command Center roadmap/index present; unified approved backlog, consistent status, full requirement links absent | Medium |
| TRACE core artifact coverage in Enso | 10 core artifacts / 10 blueprint-required | **100%** | Blueprint §12.1; artifact presence only | High |
| TRACE project-extension coverage | 2 / 2 (`FEATURE_TRACKER`, `RISK_REGISTER`) | **100%** | Enso-defined extensions; not effectiveness | High |
| TRACE execution maturity | 3 evidenced practices / 8 audit gates | **37.5%** | Entrypoint/onboarding, status/decision updates, Light Curves evidenced; task instances, route-use proof, handoff proof, efficiency measurement, reproducible raw evidence absent/partial | Medium |
| Current validation coverage | 7 successful targets / 9 attempted targets | **77.8%** | MCC 3, Enso unittest 1, TRACE pytest/lint 2 plus source import behavior; Enso pytest and TRACE build fail/block. Equal command targets. | High |
| Release readiness | 3 / 12 gates | **25.0%** | Local build/tests, governance baseline, rollback concepts present; release artifact, signed acceptance, staging/UAT/prod/DR, deployment/rollback rehearsal, security closure, performance/a11y gates absent | Medium |

Hermes denominator is consistently **six capability families** named by the request: terminal, browser, messaging, agent, memory, tools. Active/integrated in Enso: **0/6 = 0%**. The inert vendor baseline and policy metadata do not count as activation.

Tags are excluded from release proof. “Implemented” is separated from “validated” and “accepted.”

