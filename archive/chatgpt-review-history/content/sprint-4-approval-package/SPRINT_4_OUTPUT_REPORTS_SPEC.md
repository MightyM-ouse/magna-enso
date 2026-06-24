# SPRINT_4_OUTPUT_REPORTS_SPEC.md
# Magna Enso — Sprint 4 Output Reports Specification
# Type: Local-only approval package
# Date: 2026-06-17
# Status: SPEC for reports produced AFTER approval. None produced yet.

---

## 1. Where the reports live

Default: drafted local-only first under `ChatGPTReview/sprint-4-clean-governed-baseline/`. The **baseline
itself** (if Option C/B) would live in `magna-enso/` only on approval; the **reports** are committed into the
repo only by a separate human decision. No baseline or `docs/` is created now.

## 2. Report set (if Sprint 4 is approved)

| # | Report | Purpose |
|---|---|---|
| 1 | `SPRINT_4_PRE_IMPLEMENTATION_REPORT.md` | Plan-of-record before any import; option chosen; preconditions met |
| 2 | `HERMES_SOURCE_PROVENANCE_MANIFEST.md` | Source repo + SHA `33b1d144` + per-file origin + hashes + date |
| 3 | `SOURCE_IMPORT_INVENTORY.md` | Every imported file (retained allowlist), source→target paths |
| 4 | `REMOVED_SURFACES_REPORT.md` | Each removed surface confirmed absent (with checks) |
| 5 | `DISABLED_SURFACES_REPORT.md` | Each disabled surface + tier + how disabled |
| 6 | `RETAINED_SURFACES_REPORT.md` | Each retained surface + allowed state + off/draft/read posture |
| 7 | `LICENSE_AND_DEPENDENCY_BASELINE.md` | MIT preservation, dependency licenses, SBOM, attributions, stop-condition findings |
| 8 | `NO_NETWORK_VALIDATION.md` | Static confirmation of no active network surface |
| 9 | `DEFAULT_DENY_BASELINE_REPORT.md` | Confirms the default-deny baseline requirements are met structurally |
| 10 | `SPRINT_4_LIGHT_CURVE.md` | Evidence package; human approval pending |
| 11 | `FINAL_RECOMMENDATION.md` | Sprint 4 closeout recommendation |

## 3. Common standard

TRACE Documentation Standard: metadata, purpose, scope, findings, evidence (paths + SHA), confidence,
facts-vs-judgment separation. Every report must include the honesty statement: **"structurally safe / not
runtime-enforced; retained risky capabilities remain disabled until Sprint 5."**

## 4. Mandatory contents

- **Provenance + inventory** must together account for **every** imported file (no untracked source).
- **Removed/disabled/retained** reports must collectively cover **every** surface in the Sprint 3 matrix.
- **License/SBOM** must record any stop-condition finding (and Sprint 4 halts if one fires).
- **No-network** validation must state it is static (baseline does not run).

## 5. Acceptance flow

Reports drafted (executor) → **Antigravity validates** (provenance complete, removed surfaces absent, no
network surface, no false enforcement claims, license clean) → **Grok** second opinion → ChatGPT continuity →
`SPRINT_4_LIGHT_CURVE.md` → **human owner accepts**. Only then is Sprint 4 DONE; Sprint 5 (policy engine) is
considered separately.

## 6. Boundaries

Spec only. No reports, baseline, or source import produced by this package.
