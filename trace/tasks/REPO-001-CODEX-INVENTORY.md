# REPO-001 — Codex Repository Inventory Report

Status: `PLANNED`
Agent: Codex
Assigned branch: `codex/REPO-001-inventory-report`
Base recommendation: current `main` at launch time
Instruction authority: ChatGPT / System Architect
Product Owner authority: required before launch and merge

## Goal

Create a read-only repository inventory report that identifies current repository structure, open work, archived materials, status surfaces, and stale or conflicting project records. The output must help ChatGPT/System Architect decide what should be cleaned up next without Codex correcting anything during this task.

## Outcome-oriented requirement

Codex must inspect the actual repository state and determine the best inventory method. Do not assume the known status from chat is accurate. The task is complete when the repository contains a clear Markdown report and machine-readable JSON inventory.

## Allowed outputs

Codex may create or update only:

```text
trace/reviews/REPO-001-INVENTORY-REPORT.md
trace/evidence/REPO-001-INVENTORY.json
trace/evidence/REPO-001-HANDOFF.md
trace/evidence/REPO-001-HANDOFF.json
```

## Allowed actions

Codex may:

- Inspect files, branches, open PRs, issues, task packets, evidence, reviews, archive folders, workflows, scripts, and status documents.
- Run read-only Git and GitHub commands.
- Identify stale, duplicate, conflicting, or missing status surfaces.
- Record findings and recommendations.
- Commit and push only to `codex/REPO-001-inventory-report`.
- Open a draft PR targeting `main`, unless launch prompt specifies another base.

## Protected paths and forbidden actions

Codex must not:

- Modify GOV-005, GOV-006, ARCH-001, runtime, workflows, validators, schemas, source code, or existing task packets.
- Correct stale files or status drift.
- Modify another agent branch.
- Push to `main`.
- Merge, close issues, delete branches, force-push, or mark work accepted.
- Access private/system paths outside the repository unless explicitly approved.

## Required report sections

The Markdown report must include:

1. Synchronization verdict.
2. Repository baseline: branch, commit, open PRs, open issues.
3. Current task/branch map.
4. Status-surface comparison.
5. Archive inventory summary.
6. Governance files and workflow summary.
7. Duplicates, stale records, and inconsistencies.
8. Non-overlap risk findings.
9. Recommended cleanup candidates.
10. Product Owner decisions required.

## JSON evidence requirements

The JSON inventory must include:

- `task_id`
- `agent`
- `branch`
- `base_commit`
- `generated_at`
- `repository`
- `open_pull_requests`
- `open_issues`
- `branches_examined`
- `status_surfaces`
- `archive_summary`
- `findings`
- `recommended_next_actions`

## Handoff contract

The final chat response from Codex must be short and include:

- Branch and final commit.
- Draft PR link.
- Validation performed.
- Evidence paths.
- Decisions required.

Detailed evidence must stay in the repository.
