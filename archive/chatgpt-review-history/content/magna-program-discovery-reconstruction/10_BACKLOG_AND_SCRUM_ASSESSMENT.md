# 10 — Backlog & Scrum Delivery Assessment

> **Scrum artifacts are not invented here.** Only what exists is recorded.

## 1. magna-enso — the most mature, formal backlog

**Product backlog / feature tracker** (`trace/FEATURE_TRACKER.md`): 16 features
ENSO-F-0101…1501, each with Release, Sprint, Owner, Reviewer, Risk, Evidence level,
Status (`PLANNED·IN_DESIGN·IN_PROGRESS·IN_REVIEW·BLOCKED·DONE·DEFERRED`).

| Status | Count | Features |
|---|---|---|
| DONE | 4 | F-0101 (skeleton), F-0201 (audit), F-0301 (gov design), F-0401 (inert baseline) |
| PLANNED | 12 | F-0501/0502 (policy gate+approval), F-0601, F-0701, F-0801/0802, F-0901, F-1001, F-1101, F-1201, F-1301, F-1401, F-1501 |

**Sprint plan** (`planning/MAGNA_ENSO_SPRINT_PLAN.md`): Sprints 0–15, each with Purpose,
Features, Non-Goals, Deliverables, Acceptance Criteria, Evidence Required, Suggested
Worker, Risk. **Release planning:** RC at Sprint 15 (`v1.0-enso-rc1`).

**Definition of Ready / Done:** the **honest-status rule** ("never mark DONE without a
human-approved Light Curve") functions as a DoD; Sprint-4 readiness gates function as
DoR. Per-sprint acceptance criteria are explicit.

**Reviews / retros:** Antigravity validation reports per sprint (review packages under
`ChatGPTReview/sprint-N-*`); ChatGPT continuity review. No formal "retrospective"
artifact, but acceptance + RC-correction cycles (RC-01…RC-05 in S3) play that role.

**Traceability (requirement → code → test → evidence → acceptance):** strong on paper —
Feature → Sprint → Light Curve → Decision (EH-NNNN) → Risk (R-NN) cross-links exist.
**Weak in execution for S5:** the first feature with real code (F-0501) is still
`PLANNED` while uncommitted code exists (C-6), and its tests can't run (C-7).

**Items marked complete without adequate evidence?** S1–S4 each have a human-approved
Light Curve + Antigravity validation → evidence is adequate **for what they are**
(skeleton/audit/design/inert-baseline). **Caveat:** none of those four delivered or
verified *runtime behaviour*, so "4 sprints done" must not be read as "product 27% built."

### Backlog sub-types (Enso)
| Backlog | Present? | Evidence |
|---|---|---|
| Product | ✅ | FEATURE_TRACKER |
| Technical | 🟡 | embedded in sprint deliverables |
| UX | 🟡 | only as Sprint 13 |
| Security | ✅ | RISK_REGISTER (R-01…R-15), Antigravity reviews, security-contract tests |
| Architecture | ✅ | Sprint-3 governance design (17 reports) |

## 2. magna-command-center — informal "layer" backlog

Delivery is organized as **numbered "layers"** (HAB/ATM/CSF/BRS/MEM/NRV/SGN +
`layer-6…layer-21`), not classic sprints. Evidence:
- `project-knowledge/02_COMPLETED_LAYERS.md`, `03_PENDING_LAYERS.md`, `09_CURRENT_KNOWN_ISSUES.md`.
- An **Agile roadmap** exists (`agent-logs/project-status-and-roadmap/PROJECT_STATUS_AND_AGILE_ROADMAP.md`,
  referenced) with S0–S6 framing toward "Release 1 = Belt + SGN-01 v1."
- **Two parallel roadmaps** (the layer/belt model and the agile roadmap) — Blueprint §10
  flags reconciling them as Sprint-0 work. Backlog readiness = DOCUMENTED, not APPROVED.

**DoR/DoD:** the Agent Execution Protocol (PROTO) acts as a process gate (preflight →
pre-impl report → work → validate → report → review package); "Definition of Done
includes Implementation Index updated" (Blueprint §9). Acceptance is per-layer tags.

## 3. TRACE — lightweight backlog

`PROJECT_STATUS_AND_NEXT_STEPS.md` task queue + feature ledger (CURRENT/PLANNED/BLOCKED)
+ v2 plan. ADRs in `docs/adr/`. Conventional Commits + PR-linked review-packages
(REPOSITORY_INFO). Backlog readiness = DOCUMENTED.

## 4. Scrum maturity verdict

| Dimension | Enso | command-center | TRACE |
|---|---|---|---|
| Backlog formality | **High** | Medium (informal layers) | Low-Med |
| Acceptance discipline | **High** (Light Curve + human gate) | Medium (tags + manual verify) | Medium |
| Traceability | **High on paper** | Medium | Medium |
| Execution-vs-status integrity | **At risk (C-6)** | At risk (status drift, Blueprint §10) | Good (honest ledger) |

**Key risk across all three: status drift** — docs asserting states the working tree or
tests don't confirm. This is the single most important Scrum/governance finding.
