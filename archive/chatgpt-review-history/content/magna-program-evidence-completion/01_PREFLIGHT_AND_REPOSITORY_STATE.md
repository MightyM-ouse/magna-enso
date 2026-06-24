# Preflight and Repository State

Audit date: 2026-06-21. Inspection was read-only in all reviewed repositories. Raw validation records are under `raw-command-output/`.

## Repositories

| Repository | Branch | HEAD | State | Read-only inspection safety |
|---|---|---|---|---|
| `<LOCAL_USER_HOME>/Projects/AI/magna-command-center` | `main` | `68981c8a540d5b99fc91f92bc4e290b09d81fccd` — `docs: add MAGNA_BLUEPRINT.md — single consolidated project blueprint` | `main` ahead of `origin/main` by 1; modified `.codex/config.toml`, `AGENTS.md`; two untracked audit-report trees | Safe with qualification: HEAD, working-tree evidence, and release claims are separated. Existing changes were not caused by this audit. |
| `<MAGNA_LOCAL_ROOT>/magna-enso` | `sprint/05-policy-engine` | `4d5c203cc236be84bd4b9bd8004cb88e8797a34d` — `docs(trace): refresh post-Sprint 4 project state` | Untracked `policy/`, `tests/`, `trace/evidence/ENSO-0005_LIGHT_CURVE.md` | Safe and required by scope; Sprint 5 is working-tree evidence, not committed or accepted state. |
| `<LOCAL_USER_HOME>/Projects/AI/TRACE` | `main` | `c6b4bbd3679ff3d7a3580c48af67b3b5d78b5884` — `fix: address review — honest CI/validation, doc accuracy, hardening, e2e tests` | Clean tracked tree; untracked `proposed-governed-loop/` | Safe; proposed loop is assessed as proposed, never as shipped TRACE. |

Remotes: Command Center and TRACE each use the recorded GitHub `origin`; Enso has no configured remote. Exact `remote -v`, untracked inventories, and before/after states are preserved in the raw records.

## Non-Git evidence roots

Inspected `<MAGNA_LOCAL_ROOT>/planning`, `<MAGNA_LOCAL_ROOT>/trace`, and review packages under `<CHATGPT_REVIEW_SOURCE>`. The authorized output location was available and is the only location this audit wrote.

## Reliability rule

Committed HEAD proves repository history; it does not prove current working-tree behavior, acceptance, release, or production operation. Working-tree source can prove code presence and local validation, but not human acceptance. Tags alone are not release evidence.

