# ARCH-001 Diagram Package Assessment

## Verdict

`AUTHENTICATED_CANDIDATE_SOURCE_NOT_APPROVED_FOR_IMPORT`

Package: `magna-enso-architecture-diagrams-draft-corrected.zip`
Verified SHA-256: `04471f54baf64b23e96365ee1232ed6f1ab2ed0c859111845620fcc53dac4577`
Assessment date: 2026-06-24

## Verified inventory

| Artifact class | Count | Proposed evidence tier |
|---|---:|---|
| Draw.io native sources | 25 | Candidate canonical diagram source |
| SVG renders | 25 | Derived review artifacts |
| HTML diagram views | 25 | Generated viewer artifacts |
| Mermaid sources | 25 | Validation/source-derivation evidence pending architecture package |
| Architecture diagrams | 22 | Candidate architecture views |
| Behavioural diagrams | 3 | Candidate contract/state views |
| Curated validation files | 7 | Curated review evidence |
| Raw validation entries | 78 | Raw evidence; Actions artifact/local archive, not source tree |
| Total ZIP entries | 166 | Mixed source, derived, viewer and raw evidence |

The diagram index parses as 25 unique records. All records report semantic match, render
pass and Draw.io validation pass. The package correction report records 362 validation
passes and zero failures, while browser QA remains human-review-pending.

## State distribution

| Diagram state | Count |
|---|---:|
| Current | 4 |
| Target | 8 |
| Both | 5 |
| Current and target | 8 |

## Referenced architecture sources

The diagram index depends on 17 source documents, including:

- `03_MAGNA_PROGRAM_ARCHITECTURE.md`
- `04_EVOLUTION_AND_REPOSITORY_ARCHITECTURE.md`
- `05_CURRENT_VERIFIED_ARCHITECTURE.md`
- `06_MAGNA_ENSO_TARGET_ARCHITECTURE.md`
- `08_GOVERNANCE_POLICY_AND_APPROVAL.md`
- `09_TRACE_DUAL_PLANE_ARCHITECTURE.md`
- `16_EVOLUTION_STAGE_CONTRACTS.md`
- `technical-specifications/18_STATE_MACHINE_SPECIFICATIONS.md`
- `technical-specifications/19_FAILURE_AND_OUTCOME_TAXONOMY.md`

Those normative sources are expected in ARCH-SRC-01 and are not yet available. Diagram
semantic validation proves consistency with the package's accepted sources at generation
time; it does not prove consistency with the current `magna-enso` repository.

## Material findings

### DA-001 - Mixed canonicality

The ZIP mixes native sources, derived renders, a JavaScript/HTML viewer, validation reports,
generation scripts, raw logs and screenshots. Importing the entire ZIP would collapse
distinct evidence tiers and add 78 raw validation entries to the source tree.

Required treatment:

- Curate Draw.io sources after architecture reconciliation.
- Regenerate or selectively retain SVG renders.
- Keep raw validation output outside source, preferably as an Actions artifact.
- Treat the HTML viewer as optional generated tooling, not architecture authority.

### DA-002 - Current-state claims require repository proof

Examples include `DIAG-04` ("Current verified Command Center") and `DIAG-05`
("Current Magna Enso harness"). The canonical Enso repository states runtime enforcement is
not confirmed on `main` and Sprint 5 remains unaccepted.

Required treatment:

- Compare every `current` or `current+target` diagram with exact repository/runtime
  evidence.
- Classify Command Center views as cross-repository references where applicable.
- Do not import a diagram under a current-state label until its claims are reproduced.

### DA-003 - Evolution and naming reconciliation

Repository/versioning and evolution diagrams may predate EH-0017 and EH-0018.

Required treatment:

- Enforce separate repositories per stage.
- Use canonical `KENOSHA` spelling in active material.
- Preserve original package provenance in the migration manifest.

### DA-004 - Source dependency

The index maps diagrams to requirements, components, decisions and source-line references.
Without ARCH-SRC-01, the 25 diagrams cannot be independently checked against their
normative text, registries or traceability matrix.

## Import recommendation

Do not import the ZIP wholesale. In Phase B, import only the approved native Draw.io files,
a machine-readable diagram index, selected SVG renders, and concise validation evidence.
Store raw logs, screenshots, repeated manifests and the generated viewer outside canonical
source unless separately justified.

The final diagram import list remains blocked until ARCH-SRC-01 is supplied and the
current/target claims are reconciled.
