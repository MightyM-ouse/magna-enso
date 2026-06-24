# SPRINT_2_OUTPUT_REPORTS_SPEC.md
# Magna Enso — Sprint 2 Output Reports Specification
# Type: Local-only approval package
# Date: 2026-06-17
# Status: SPEC for reports to be produced AFTER approval. None produced yet.

---

## 1. Where the reports live

Per Decision 8, the default is **local-only first** (drafted in the scratch `notes/`, finalized to a
review folder under `ChatGPTReview/sprint-2-hermes-audit/`), then optionally committed later as
`magna-enso/docs/audit/` **only on a separate human decision**. No `docs/audit/` is created now.

## 2. Report set

| # | Report | Answers questions | Key contents |
|---|---|---|---|
| 1 | `HERMES_PROVENANCE.md` | (pre-req) | Source repo URL, exact commit SHA audited, default branch, clone date |
| 2 | `LICENSE_AND_DEPENDENCY_REVIEW.md` | (pre-req), 12 | Top-level license (confirm), dependency licenses, copyleft/ToS flags, attribution obligations |
| 3 | `HERMES_CODE_MAP.md` | 1, 2 | Architecture overview, layering, module inventory (one-line purpose each), entry points |
| 4 | `ACTION_DISPATCH_MAP.md` | 5 | Action-dispatch chokepoints — the function(s) all actions flow through (gate candidates) |
| 5 | `AUTONOMY_ENTRY_POINT_MAP.md` | 6, 7, 8 | Memory-write paths, skill-write/activation paths, scheduler/cron/timed triggers |
| 6 | `EXTERNAL_SURFACE_MAP.md` | 4, 9, 10, 11, 12 | Messaging gateways, terminal backends, browser/web tools, cloud/provider integrations; risk tags |
| 7 | `CAPABILITY_GATING_FEASIBILITY.md` | 13 | Per-surface: gateable? at which chokepoint? gaps/ungated paths; default-deny enforceability |
| 8 | `MAGNA_ENSO_REUSE_RECOMMENDATION.md` | 3, 14 | Keep/rebuild/exclude per module; Go / conditional-go / no-go for Sprint 4 base; rationale + confidence |
| 9 | `SPRINT_2_LIGHT_CURVE.md` | — | Evidence package: what was inspected (paths+SHA), reports produced, risks, validation, human sign-off pending |

## 3. Common report standard (TRACE Documentation Standard)

Each report includes: metadata header, purpose, scope, findings, evidence (file paths + commit SHA),
confidence levels, and a "facts vs. judgments" separation. Reports **cite identifiers only** — no Hermes
source is pasted into any report or into `magna-enso/`.

## 4. The reuse recommendation format (report 8)

```md
## Module-by-module
| Module | Relevance | Risk | Gateable? | Recommendation | Confidence |
|--------|-----------|------|-----------|----------------|------------|
| ...    | high/med/low | R-id(s) | yes/partial/no | KEEP / REBUILD / EXCLUDE | high/med/low |

## Overall verdict for Sprint 4 base
Decision: GO / CONDITIONAL-GO / NO-GO
Conditions (if conditional): ...
Rationale: ...
Confidence: ...
```

## 5. Light Curve (report 9) requirements

- Mode History: investigation → review.
- Files inspected (with SHA), reports produced, risks (link R-01…R-15), validation results (Antigravity).
- Final Status: in_review; Human Approval: pending. **No self-approval.**

## 6. Acceptance flow

Reports drafted (Codex) → validated (Antigravity) → governance/second-opinion review (Claude/Grok) →
continuity update (ChatGPT) → `SPRINT_2_LIGHT_CURVE.md` written → **human owner reviews and accepts**.
Only then is Sprint 2 DONE, and only then may Sprint 3 be considered (separately).

## 7. Optional later step (separate decision)

If the human owner later wants the audit findings version-controlled, they may approve copying the
**reports** (never the Hermes source) into `magna-enso/docs/audit/` and committing them — a distinct
decision, logged as a new Event Horizon entry, outside this package's scope.
