# ARCH-001A — Claude Architecture Source Classification

Status: `PLANNED`
Agent: Claude
Assigned branch: `claude/ARCH-001-source-classification`
Base recommendation: current `main` at launch time, unless ARCH-001 branch is explicitly selected by Product Owner
Instruction authority: ChatGPT / System Architect
Product Owner authority: required before launch and merge

## Goal

Classify archived architecture-related materials now available in the repository and recommend which files should later be promoted to canonical architecture, technical specifications, diagram sources, rendered diagrams, trace evidence, review evidence, or archive-only history.

## Outcome-oriented requirement

Claude must independently inspect the archived materials and repository context. The task is a classification and recommendation task only. Claude must not promote, rewrite, or canonicalize architecture during this task.

## Allowed outputs

Claude may create or update only:

```text
trace/reviews/ARCH-001-SOURCE-CLASSIFICATION.md
trace/evidence/ARCH-001-SOURCE-INVENTORY.json
trace/evidence/ARCH-001-CLASSIFICATION-HANDOFF.md
trace/evidence/ARCH-001-CLASSIFICATION-HANDOFF.json
```

## Allowed actions

Claude may:

- Read archived ChatGPTReview materials and architecture/diagram packages in the repository.
- Compare architecture, technical specification, diagram, review, and evidence materials.
- Identify duplicates, generated files, raw artifacts, missing sources, and conflicting claims.
- Recommend future canonical destinations.
- Commit and push only to `claude/ARCH-001-source-classification`.
- Open a draft PR targeting `main`, unless launch prompt specifies another base.

## Protected paths and forbidden actions

Claude must not:

- Move files into `docs/architecture/` or `docs/technical-specifications/`.
- Rewrite or accept architecture.
- Modify ARCH-001 task authority, GOV-005, GOV-006, runtime code, workflows, validators, schemas, or existing canonical documents.
- Modify another agent branch.
- Push to `main`.
- Merge, close issues, delete branches, force-push, or mark architecture accepted.
- Access private/system paths outside the repository unless explicitly approved.

## Required classification categories

The Markdown report must classify relevant files into:

1. Candidate canonical architecture.
2. Candidate technical specification.
3. Candidate diagram source.
4. Candidate rendered diagram.
5. Trace/evidence material.
6. Review material.
7. Archive-only historical material.
8. Duplicate or generated material.
9. Missing input or unresolved dependency.
10. Conflict requiring Product Owner or System Architect decision.

## JSON evidence requirements

The JSON inventory must include:

- `task_id`
- `agent`
- `branch`
- `base_commit`
- `generated_at`
- `sources_examined`
- `classification_matrix`
- `duplicates`
- `missing_inputs`
- `conflicts`
- `recommended_promotion_map`
- `decisions_required`

## Handoff contract

The final chat response from Claude must be short and include:

- Branch and final commit.
- Draft PR link.
- Files examined summary.
- Evidence paths.
- Decisions required.

Detailed reasoning and classification must stay in the repository.
