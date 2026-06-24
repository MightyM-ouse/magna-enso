---
document: TRACE_SOURCE_RESOLUTION
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Canonical TRACE source resolution (methodology / implementation / applied instance) with hashes & commits
date: 2026-06-21
evidence_sources:
  - Preflight filesystem + git inspection (this session)
  - 06_TRACE_COMPLETE_ASSESSMENT.md (evidence baseline)
  - planning/TRACE_ADOPTION_PLAN_FOR_MAGNA_ENSO.md; MAGNA_ENSO_PROJECT_CHARTER.md; MAGNA_ENSO_FOLDER_AND_REPO_STRATEGY.md
change_control: Governed; nothing deleted. Resolves Correction 2.
---

# TRACE Source Resolution (Correction 2)

## Human table of contents
1. Three TRACE locations and their distinct roles
2. Source-resolution table (hashes / commits / authority)
3. Which one Magna Enso references
4. TRACE dual role (engineering plane + runtime plane)
5. Corrections applied to TRACE claims
6. Open decisions
7. Change-control note

## 1. Three TRACE locations — distinct roles (not ambiguous)

| Location | Role | Git? |
|---|---|---|
| `<MAGNA_LOCAL_ROOT>/trace/TRACE_STRATEGIC_BLUEPRINT_v1.0.md` | **Canonical methodology blueprint** (the program's TRACE source-of-truth document) | Not a git repo — a methodology reference file the Magna program points at |
| `<LOCAL_USER_HOME>/Projects/AI/TRACE` | **Canonical implementation / reference repository** (template + hooks + JSONL→SQLite + FastAPI + React Observatory + tests/CI) | Git repo; remote `https://github.com/MightyM-ouse/trace.git` |
| `<MAGNA_LOCAL_ROOT>/magna-enso/trace/` | **Applied TRACE instance for Enso** (in-repo Core artifacts: STAR_MAP, TRACE_CONFIG, DECISION_LOG, ROLE_REGISTRY, WORKFLOWS, CELESTIAL_INDEX, evidence/) | Lives inside the `magna-enso` repo |

This three-way split is corroborated by `MAGNA_ENSO_FOLDER_AND_REPO_STRATEGY.md` §2: *"the parent-level
`trace/` is the methodology reference; the per-repo `trace/` is the operating instance."* The `-draft` package
conflated these and under-specified them; this resolves them.

## 2. Source-resolution table (hashes / commits / authority)

| ID | Path | Type | Authority level | Commit / SHA-256 | Status |
|---|---|---|---|---|---|
| TRC-SRC-01 | `…/Magna/trace/TRACE_STRATEGIC_BLUEPRINT_v1.0.md` | Methodology blueprint (2855 lines) | **Canonical methodology source of truth** | sha256 `9fff38ab2147e614494bddc8e4098afe57b77502850d8bc00e27f4d3591755f2` | Reference doc (not versioned in a git repo here) |
| TRC-SRC-02 | `<LOCAL_USER_HOME>/Projects/AI/TRACE` | Implementation/reference repo | **Canonical implementation/reference** | git `c6b4bbd3679ff3d7a3580c48af67b3b5d78b5884` @ `main`; remote `github.com/MightyM-ouse/trace.git` | IMPLEMENTED_VALIDATED (template); **UI build not reproducible** (missing rollup binary) |
| TRC-SRC-03 | `…/magna-enso/trace/TRACE_CONFIG.yaml` (instance root file) | Applied Enso instance | **Operating instance (subordinate to TRC-SRC-01)** | enso repo git `4d5c203…`; config sha256 `e4408c70e7e9acb8db11eed4db0adab3787971b2b78939513f4db2fec107476b` | IN_PROGRESS (Enso applies it) |

> Hashes computed this session with `shasum -a 256`; commits with `git rev-parse`. The blueprint file is a
> single canonical document, not a git working tree, so it is pinned by content hash rather than a commit.

## 3. Which one Magna Enso references
- The **charter** and **TRACE adoption plan** cite `../trace/TRACE_STRATEGIC_BLUEPRINT_v1.0.md` (TRC-SRC-01)
  as the TRACE source of truth.
- Magna Enso **applies** TRACE via its in-repo `trace/` instance (TRC-SRC-03).
- The `TRACE` implementation repo (TRC-SRC-02) is the reference implementation/Observatory; it is a
  **separate sovereign repository** (TRACE repository sovereignty preserved).
- No evidence shows the parent-level `trace/` directory is itself a git repo or that `magna-enso` imports the
  `TRACE` repo's code at runtime — those remain `UNKNOWN`/out of scope, not asserted.

## 4. TRACE dual role (decision 6, preserved)
- **Engineering plane:** TRACE governs *how Magna Enso is engineered* (task packets, Light Curves, decisions,
  validation). Implemented as the in-repo instance (TRC-SRC-03) per the blueprint (TRC-SRC-01) and reference
  repo (TRC-SRC-02). `implementation_status: PARTIAL`; **effectiveness NOT established** (`06` baseline).
- **Runtime plane:** TRACE-*compatible* operational traceability *inside Magna* (requests/decisions/approvals/
  actions/failures/memory effects). `implementation_status: NOT_STARTED` (PLANNED); Command Center has rich
  runtime traceability but it is **not** connected to TRACE's schema. Anti-self-certification + independent
  verifier preserved (see `09`, spec `09`).

## 5. Corrections applied to TRACE claims
- Removed the `-draft`'s ambiguous single-"TRACE" treatment; replaced with the three resolved sources above.
- Kept "engineering plane partly current / runtime plane planned"; **no TRACE effectiveness claimed**.
- Blueprint-only / `proposed-governed-loop/` capabilities remain **planned/proposed**, not counted as TRACE today.

## 6. Open decisions
- OD-TRC.1 — Confirm TRC-SRC-01 (blueprint v1.0 @ that hash) as the frozen program TRACE reference (ADR-R3).
- OD-TRC.2 — Canonical cross-plane runtime↔engineering contract + independent verifier identity (ADR-R3).
- OD-TRC.3 — Fix TRACE UI build reproducibility (missing rollup optional binary).

## 7. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Sources pinned by commit/hash. Governed; nothing deleted.
