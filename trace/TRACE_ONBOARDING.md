# TRACE Onboarding

## Startup

1. Read `AGENTS.md` and `trace/STAR_MAP.md` from the applicable branch.
2. Read the active GitHub issue/PR and task packet under `trace/tasks/`.
3. Confirm role, workflow mode, allowed scope, forbidden scope, and evidence level.
4. Route context through `trace/CELESTIAL_INDEX.json`.
5. Record branch, HEAD, and working-tree preflight before changes.

## TRACE execution

- **Template:** one task packet with objective and acceptance criteria.
- **Route:** load declared context; record any justified expansion.
- **Assign:** one accountable worker and an independent reviewer where risk requires it.
- **Check:** execute exact tests and retain failures, skips, and limitations.
- **Evidence:** produce a Light Curve linked to issue, PR, commit, and artifacts.

## GitHub lifecycle

Work is performed on one isolated task branch/worktree. The task packet may authorize
commit and push to that branch. Direct `main` pushes, force pushes, self-merge, and silent
scope changes remain forbidden. The Product Owner accepts functionality and merges.

## Honest status

Distinguish planned, implemented, tested, verified now, deployable, released, and
production-confirmed. Do not infer one state from another. Missing evidence is reported as
not confirmed.

## Missing information

Inspect routed repository evidence first. Ask only for decisions or information that cannot
be derived safely. Never invent dates, acceptance, percentages, environments, or users.

