# ARCH-001 - Canonical Architecture and Technical-Specification Baseline

## Status

`TASK_PACKET_PREPARED_DISCOVERY_NOT_STARTED`

## Authority

- GitHub issue: `#8`
- Product Owner authorization: 2026-06-24 ChatGPT session
- Accepted starting baseline: `20e69cad9edfc71e193de3411f7778a64c041273`
- Assigned lead: ChatGPT, System Architect/SME
- Mode: discovery and architecture review
- Assigned branch: `architect/ARCH-001-canonical-architecture-baseline`

## Objective

Establish an evidence-backed canonical architecture and technical-specification baseline
for Magna Enso. Phase A inventories, classifies, compares, and plans migration. It does not
import, rewrite, delete, or supersede architecture sources.

## Why this task exists

The canonical repository records a corrected architecture/specification package and an
editable diagram package as accepted migration inputs, while the architecture route remains
`MIGRATION_PENDING`. Their exact contents, provenance, overlap, conflicts, and target
locations must be established before integration.

## Context routes

Required:

- `architecture`
- `trace-governance`
- `evidence-and-decisions`

Conditional:

- `policy-engine` only to classify references; no selection or acceptance
- `hermes-provenance` only if an architecture artifact makes a Hermes claim that requires
  verification

A broader repository scan requires a written reason in the Light Curve.

## Phase A - Discovery and migration design

### Activities

1. Verify `main`, Issue #8, this task packet, branch state, and applicable governance.
2. Inventory existing GitHub architecture, technical-specification, decision, and diagram
   artifacts using routed paths.
3. Locate the corrected architecture/specification and editable diagram packages recorded
   as accepted migration inputs.
4. Capture for each input:
   - exact name and path or external reference
   - source and owner
   - version/date when evidenced
   - format and editability
   - checksum when available
   - current acceptance/evidence state
5. Classify each artifact:
   - canonical
   - candidate
   - historical
   - duplicate
   - conflicting
   - missing
   - generated/transport-only
6. Compare architecture claims with accepted repository/runtime evidence. A documented
   design must not be presented as implemented runtime behavior.
7. Produce the target information architecture, naming rules, migration matrix, conflict
   register, open decisions, and recommended bounded Phase B scope.
8. Record checks, limitations, and exact missing evidence in the Light Curve.

### Required outputs

- `docs/architecture/discovery/ARCHITECTURE_SOURCE_INVENTORY.md`
- `docs/architecture/discovery/ARCHITECTURE_CONFLICT_REGISTER.md`
- `docs/architecture/discovery/CANONICAL_TARGET_STRUCTURE.md`
- `docs/architecture/discovery/SOURCE_TO_TARGET_MIGRATION_MATRIX.md`
- `docs/architecture/discovery/ARCHITECTURE_OPEN_DECISIONS.md`
- `docs/architecture/discovery/PHASE_B_IMPORT_RECOMMENDATION.md`
- `trace/evidence/ARCH-001_LIGHT_CURVE.md`

If an accepted external package cannot be located, record it as `MISSING_INPUT` and stop
the affected comparison. Do not reconstruct it from chat history or model memory.

## Phase B - Controlled import

`BLOCKED_PENDING_PHASE_A_ACCEPTANCE`

Phase B requires a new Product Owner decision recorded on Issue #8 after review of all
Phase A outputs. Approval must identify the exact bounded import scope, source artifacts,
target paths, conflict resolutions, and required reviewers.

## Allowed changes during Phase A

- `trace/tasks/ARCH-001.md`
- `trace/evidence/ARCH-001_LIGHT_CURVE.md`
- `docs/architecture/discovery/`
- `docs/governance/SOURCE_MIGRATION_REGISTER.md` only for evidence-backed classification
- `trace/STAR_MAP.md` only to record reviewed ARCH-001 status
- `trace/CELESTIAL_INDEX.json` only if required to route newly accepted discovery outputs

Any additional path requires Product Owner approval recorded on Issue #8 before modification.

## Forbidden changes during Phase A

- Architecture/specification source import, rewrite, deletion, or supersession
- Runtime source, application code, tests, dependencies, infrastructure, or environments
- `policy/`, `tests/policy/`, or untracked Sprint 5 material
- Policy-engine selection or acceptance
- Hermes activation, tools, skills, memory, schedulers, or external actions
- HELIX doctrine or SGN-01 status
- Secrets, credentials, private data, environment files, or generated transport archives
- Direct push or merge to `main`
- Unrecorded full-repository scan
- Phase B execution

## Roles

| Responsibility | Role |
|---|---|
| Scope, priority, architecture acceptance, Phase B authorization, merge | Product Owner |
| Discovery lead, coherence analysis, migration design, task/evidence preparation | ChatGPT System Architect/SME |
| Architecture/specification review | Claude, only when separately launched against this task |
| Independent evidence validation | Antigravity, when requested before acceptance |
| Runtime implementation | Out of scope; Codex is not assigned |
| Governed runtime experiment | Out of scope; Hermes remains inactive |

No worker may self-approve or merge.

## Acceptance criteria for Phase A

1. Every discovered input has an exact path/reference and evidence classification.
2. Missing inputs are explicit and are not reconstructed or silently omitted.
3. Duplicates and conflicts are mapped without deletion or unilateral winner selection.
4. Runtime evidence and intended architecture are clearly distinguished.
5. The target structure separates architecture, technical specifications, diagrams,
   decisions, discovery evidence, and historical/superseded material.
6. The migration matrix preserves source provenance and supersession traceability.
7. Open Product Owner decisions are separated from technical recommendations.
8. The Phase B recommendation is bounded and names exact sources and targets.
9. All changes remain inside approved paths.
10. Required checks and governance validation pass.
11. A Light Curve and reviewable pull request exist.
12. Phase B remains blocked until explicit Product Owner approval.

## Required checks

- Confirm branch is based on accepted `main` commit `20e69ca` and is not behind.
- Verify the diff stays inside allowed Phase A paths.
- Parse any changed JSON/YAML with structured parsers.
- Check Markdown links and repository path references.
- Scan committed scope for secrets with repository governance tooling.
- Record unavailable inputs and failed checks exactly.
- Run GitHub Governance validation through the pull request.
- Obtain architecture and independent evidence review when the discovery risk warrants it.

## Delivery and closure

- Use this one issue, task branch, task packet, Light Curve, and pull request for ARCH-001.
- Keep the pull request draft during discovery.
- Do not close Issue #8 when only Phase A is prepared.
- After Phase A review, the Product Owner chooses whether to authorize bounded Phase B,
  revise the discovery, or close the task without import.
- Only the Product Owner may accept and squash-merge the final ARCH-001 pull request.
