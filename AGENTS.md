# AGENTS.md - Magna Enso

This repository is the canonical source for Magna Enso. All workers must use TRACE
(Template, Route, Assign, Check, Evidence) and must verify repository state before
making claims or changes.

## Required startup

1. Read this file.
2. Read `trace/STAR_MAP.md` for current accepted state.
3. Read the active GitHub issue, pull request, and task packet under `trace/tasks/`.
4. Load only the context routes listed in `trace/CELESTIAL_INDEX.json`.
5. Confirm the assigned role in `trace/ROLE_REGISTRY.yaml` and workflow in
   `trace/WORKFLOWS.yaml`.
6. Verify branch, HEAD, and working-tree state before changing anything.

If GitHub or the repository cannot be accessed, state that the project state is not
verified. Do not answer from chat memory as though it were current.

## Authority and source order

1. Human Product Owner decisions recorded in `trace/DECISION_LOG.md`.
2. Accepted requirements, architecture, and technical specifications.
3. Active task packet and linked GitHub issue.
4. Current code, tests, configuration, and migrations.
5. `trace/STAR_MAP.md`, registries, and curated evidence.
6. README files and historical reports.

Conflicts must be reported. Decisions are superseded, never silently deleted.

## GitHub workflow

- `main` is protected. Never push directly to it.
- Every change uses one approved task, one isolated branch/worktree, and one pull request.
- A worker may commit and push only to its assigned task branch when the task packet
  authorizes it.
- Never force-push, rewrite shared history, merge, or self-accept work.
- Preserve user changes and unrelated worktree content.
- The Product Owner approves product scope, functional acceptance, risk acceptance,
  and merge. Review recommendations are inputs, not approval.

## TRACE contract

- **Template:** use a task packet under `trace/tasks/`.
- **Route:** load declared context routes only; broaden with a recorded reason.
- **Assign:** stay inside the assigned role and allowed file scope.
- **Check:** run required validation and preserve exact results.
- **Evidence:** update or create a Light Curve under `trace/evidence/`.

Meaningful work is incomplete without evidence and a reviewable pull request.

## Security and evidence

- Never commit secrets, credentials, cookies, browser profiles, personal data, `.env`
  files, or private keys.
- Run Gitleaks before pushing and in CI when available.
- Commit concise, reproducible evidence. Store large/raw logs, videos, traces, and
  generated packages as GitHub Actions artifacts, not source.
- Public repository visibility does not authorize public runtime/network exposure.
  Magna remains local-first and LAN-first unless an accepted decision says otherwise.
- Do not activate Hermes, tools, skills, memory writes, schedulers, cloud providers,
  messaging, or external execution without an explicit task and applicable policy gate.

## Verification policy

- Workers own automated build, test, security, browser, responsive, accessibility,
  console, network, screenshot, and visual-regression evidence.
- Do not ask the Product Owner to verify layout, alignment, browser-console state, or
  routine UI regressions manually.
- Ask the Product Owner only for functional/product acceptance, subjective UX choices,
  risk acceptance, credentials entered through approved local interfaces, or actions
  that cannot be automated safely.

## Worker adapters

`CLAUDE.md`, `CODEX.md`, `ANTIGRAVITY.md`, `HERMES.md`, and `CHATGPT.md` are thin
role adapters. They may narrow permissions but may not override this file.

## Current boundaries

- Sprint 4's inert Hermes provenance baseline is accepted.
- Sprint 5 implementation exists only as untracked local work until separately reviewed.
- The canonical policy engine is not selected.
- Hermes capabilities are not activated.
- SGN-01 remains blocked.

