# ARCH-001V — Antigravity Archive Validation

Status: `PLANNED`
Agent: Antigravity
Assigned branch: `antigravity/ARCH-001-archive-validation`
Base recommendation: current `main` at launch time
Instruction authority: ChatGPT / System Architect
Product Owner authority: required before launch and merge

## Goal

Independently validate the archived architecture and diagram materials for integrity, consistency, completeness, provenance, and traceability. This is a validation-only task. Antigravity must not correct or reorganize the archive.

## Outcome-oriented requirement

Antigravity must choose its own validation method based on repository evidence. It must actively look for broken indexes, missing files, hash mismatches, duplicate/generated material, raw artifacts, private paths, and traceability gaps.

## Allowed outputs

Antigravity may create or update only:

```text
trace/reviews/ARCH-001-ARCHIVE-VALIDATION-REPORT.md
trace/evidence/ARCH-001-ARCHIVE-VALIDATION-HANDOFF.md
trace/evidence/ARCH-001-ARCHIVE-VALIDATION-HANDOFF.json
```

## Allowed actions

Antigravity may:

- Inspect archived architecture, technical specification, and diagram materials.
- Validate indexes, manifests, hashes, package structure, duplicate separation, generated-file separation, and provenance claims.
- Run read-only checks and local validation scripts where useful.
- Record findings by severity.
- Commit and push only to `antigravity/ARCH-001-archive-validation`.
- Open a draft PR targeting `main`, unless launch prompt specifies another base.

## Protected paths and forbidden actions

Antigravity must not:

- Correct files.
- Move or delete archive material.
- Promote files into canonical architecture/specification folders.
- Modify ARCH-001 task authority, GOV-005, GOV-006, runtime code, workflows, validators, schemas, or existing canonical documents.
- Modify another agent branch.
- Push to `main`.
- Merge, close issues, delete branches, force-push, or mark validation accepted.
- Access private/system paths outside the repository unless explicitly approved.

## Required validation areas

The report must cover:

1. Package structure integrity.
2. Manifest/index consistency.
3. Diagram source/rendered-file consistency.
4. Hash/provenance verification where available.
5. Missing referenced files.
6. Duplicate/generated/raw-file classification.
7. Private path or sensitive-data indicators.
8. Traceability to ARCH-001 needs.
9. Findings by severity.
10. Residual risks and decisions required.

## Handoff contract

The final chat response from Antigravity must be short and include:

- Branch and final commit.
- Draft PR link.
- Validation verdict.
- Evidence paths.
- Residual risks.
- Product Owner decisions required.

Detailed validation must stay in the repository.
