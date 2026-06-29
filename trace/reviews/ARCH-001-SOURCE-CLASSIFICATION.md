# ARCH-001 — Architecture Source Classification (ARCH-001A)

## Provenance and scope

- Task: `ARCH-001A` (packet `trace/tasks/ARCH-001A-CLAUDE-SOURCE-CLASSIFICATION.md`, branch
  `chatgpt/PAR-001-parallel-agent-task-packets`)
- Instruction authority: ChatGPT / System Architect — Product Owner authority required before launch and merge
- Agent: Claude — branch `claude/ARCH-001-source-classification`, base `main` @ `4afeb0c`
- **Classification and recommendation only.** No promotion, rewrite, canonicalization, or acceptance. No file
  moved into `docs/architecture/` or `docs/technical-specifications/`. Machine inventory:
  `trace/evidence/ARCH-001-SOURCE-INVENTORY.json`.

## Synchronization / preflight

- `main` @ `4afeb0ceec14262c8bbafd86f41a7734fac5e0ae`; packet branch not behind `main` (0).
- No existing `claude/ARCH-001-source-classification` branch or PR.
- `docs/architecture/` and `docs/technical-specifications/` **do not exist** on `main` (future canonical
  destinations owned by ARCH-001, not created here).
- Sources examined: `archive/chatgpt-review-history/` — **406 files**, **24 content packages**
  (md 308, html 26, svg 25, drawio 25, yaml 11, json 7, js 2, py 1, css 1). Per-file provenance:
  `archive/chatgpt-review-history/_migration/GOV-004_SOURCE_MANIFEST.json`.

## 1. Candidate canonical architecture
- `magna-enso-architecture-technical-specification-corrected/` docs **00–18** plus the supplemental reports
  `CORRECTION_REPORT.md`, `FINAL_CONSISTENCY_CORRECTION_REPORT.md`, `TRACE_SOURCE_RESOLUTION.md`,
  `PRESGN_TO_EVOLUTION_RELATIONSHIP_MATRIX.md`, `HERMES_DERIVED_CAPABILITY_PLAN.md`,
  `HELIX_VERSIONING_OPTIONS.md`. **Status:** `DRAFT_FOR_HUMAN_REVIEW`, not accepted. **Recommend →**
  `docs/architecture/` (future, via ARCH-001 + PO approval). This is the latest corrected package and
  supersedes the `-draft` package.

## 2. Candidate technical specification
- `…-corrected/technical-specifications/00–19` (20 specs incl. **18** state machines and **19** failure/outcome
  taxonomy). **Recommend →** `docs/technical-specifications/`.
- `…-corrected/registries/*.yaml` (architecture status / requirement / component / interface / traceability /
  open-decisions). **Recommend →** `docs/technical-specifications/registries/` or `docs/architecture/registries/`
  as supporting machine-readable data.

## 3. Candidate diagram source
- `magna-enso-architecture-diagrams-draft/drawio/*.drawio` (25: DIAG-01..22 + DIAG-S1..S3) — native editable.
- `magna-enso-architecture-diagrams-draft/DIAGRAM_INDEX.json` — machine index (registry-derived).
- **Note (conflict C1):** the Mermaid blocks inside the corrected-package docs plus
  `18_ARCHITECTURE_DIAGRAM_MANIFEST.md` are the upstream source-of-truth from which these `.drawio` were
  derived. Two editable representations exist; one must be designated canonical. **Recommend →**
  `docs/architecture/diagrams/src/`.

## 4. Candidate rendered diagram
- `magna-enso-architecture-diagrams-draft/svg/*.svg` (25) — Mermaid-CLI-rendered, one per diagram. **Recommend →**
  `docs/architecture/diagrams/rendered/`. Regenerable from source (Mermaid CLI 11.15.0 — external toolchain).

## 5. Trace / evidence material
- `…-corrected/validation/*.md` (registry/ID/link/mermaid/completeness) + `FOUNDATION_EVIDENCE_INDEX.json`.
- `…-diagrams-draft/validation/*.md` (semantic comparison, drawio editability, mermaid render, html viewer, manifest).
- `magna-program-evidence-completion/**` (the **accepted** technical evidence baseline + raw-command-output).
- `sprint-2-hermes-audit/`, `sprint-4-governed-hermes-baseline/` (Hermes audit/baseline; Hermes inactive 0/6).
- `_migration/` (GOV-004 migration report + source manifest = archive provenance). **Recommend →**
  `trace/evidence/` (future) or archive-only.

## 6. Review material
- `antigravity-sprint-1-trace-skeleton-review/`, `sprint-2/3/4/5-antigravity-validation/`,
  `sprint-5-antigravity-security-revalidation/` — sprint-level independent validations.
- `…-corrected/learning/*` (reviewer checklists + learning guide); `AGENT_OUTPUT_REVIEW_*` + `PromptStyle/`
  (review templates). **Recommend →** `trace/reviews/` (future) or archive-only.

## 7. Archive-only historical material
- `magna-enso-architecture-technical-specification-draft/**` — **superseded** by corrected (preserved).
- `magna-program-discovery-reconstruction/**` — preliminary; "materially wrong" per the evidence baseline.
- `sprint-2/3/4/5-approval-package/`, `git-initialization-decision-package/`, `README.md` — decision history.
- **Recommend →** retain in `archive/` only; do not promote.

## 8. Duplicate or generated material
- `…-technical-specification-draft/**` = duplicate/superseded of the corrected package (keep archive-only).
- `…-diagrams-draft/svg/*.svg`, `…/html/**` (viewer `index.html`, `views/*.html`, `assets/app.js|app.css|data.js`)
  = **generated** from the diagram sources; regenerable; not authoritative.
- `GOV-004_SOURCE_MANIFEST.json` already flags machine-generated/excluded files (e.g. `.DS_Store`,
  `EXCLUDE_MACHINE_NOISE`).

## 9. Missing input or unresolved dependency
- **Mermaid CLI 11.15.0** lives outside all repos (`<MAGNA_LOCAL_ROOT>/Tools/mermaid-cli/`) → rendered SVGs are
  not reproducible from the repo alone; record as a build dependency if SVGs are promoted.
- **Diagram viewer interactive browser QA = `HUMAN_REVIEW_PENDING`** (per the diagram package README); not verified.
- **Sibling-link dependency:** the viewer's "Source Markdown" links resolve only when the corrected spec package
  sits beside the diagram package; promoting them to different canonical folders breaks the relative links.

## 10. Conflict requiring Product Owner / System Architect decision
- **C1** — Canonical diagram source: Mermaid-in-docs + `18_…MANIFEST.md` **vs** `.drawio` files (two editable sources).
- **C2** — Confirm `corrected` supersedes `draft` for promotion; `draft` stays archive-only.
- **C3** — `magna-program-antigravity-independent-validation/` is an **explicitly rejected** evidence source yet
  archived alongside **accepted** sprint-level Antigravity validations; must not be promoted or cited.
- **C4** — `sprint-3-capability-governance-design/` overlaps current **GOV-005** governance; reconcile before any reuse.
- **C5** — Nothing is accepted: all materials are `DRAFT_FOR_HUMAN_REVIEW`; promotion needs ARCH-001 + PO approval.

## Recommended promotion map (recommendation only — ARCH-001 performs any move)
| Future destination | Source (archive) |
|---|---|
| `docs/architecture/` | corrected 00–18 + supplemental reports |
| `docs/technical-specifications/` | corrected `technical-specifications/00–19` + `registries/*.yaml` |
| `docs/architecture/diagrams/src/` | `diagrams-draft/drawio/*.drawio` + `DIAGRAM_INDEX.json` |
| `docs/architecture/diagrams/rendered/` | `diagrams-draft/svg/*.svg` |
| `trace/evidence/` | corrected `validation/*` + `FOUNDATION_EVIDENCE_INDEX.json`; `diagrams-draft/validation/*`; `magna-program-evidence-completion/*` |
| `trace/reviews/` | sprint-level Antigravity validations; corrected `learning/*`; review templates |
| `archive/` only | draft spec package; discovery; **rejected** Antigravity program package; approval packages; generated HTML viewer; `_migration`; README |

## Boundaries honored
No promotion, rewrite, or canonicalization. No move into `docs/architecture/` or `docs/technical-specifications/`.
No modification of ARCH-001 task authority, GOV-005, GOV-006, runtime code, workflows, validators, schemas,
canonical documents, or any other agent branch. No push to `main`. No merge, no issue close, no acceptance.

## Decisions required
C1 (canonical diagram source), C2 (corrected vs draft), C3 (rejected Antigravity package), C4 (capability-design
vs GOV-005), C5 (authorize/defer ARCH-001 promotion). Plus: record Mermaid CLI version + viewer-QA status as
prerequisites for promoting rendered diagrams.
