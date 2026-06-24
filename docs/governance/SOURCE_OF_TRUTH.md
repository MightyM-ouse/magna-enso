# Source of Truth

## Canonical repository

`MightyM-ouse/magna-enso` is the canonical collaboration and delivery source for Enso.
Chat sessions, local review folders, generated ZIP files, and model memory are not
authoritative project state.

## Precedence

| Priority | Source | Purpose |
|---:|---|---|
| 1 | Accepted Event Horizon decisions | Product Owner authority and supersession |
| 2 | Accepted requirements/architecture/specifications | Intended product contract |
| 3 | Active task packet and GitHub issue | Authorized work scope |
| 4 | Code/tests/configuration/migrations | Implemented behavior |
| 5 | Star Map, registries, curated evidence | Current verified delivery state |
| 6 | README and historical reports | Navigation and history |

An implemented behavior does not automatically supersede an accepted requirement. A
documented requirement does not prove implementation. Report conflicts explicitly.

## Required GitHub check

Before responding about current project state, a worker must inspect the applicable
branch/commit, active issue or PR, `AGENTS.md`, `trace/STAR_MAP.md`, and routed sources.
If access is unavailable, the worker must identify the limitation and avoid presenting
cached context as current.

## External sources

- The TRACE methodology repository is a reference implementation/source, while
  `trace/` is the applied Enso instance.
- Corrected architecture and diagram packages are accepted migration inputs until
  repository integration is completed through a separate pull request.
- Local `ChatGPTReview/` folders are historical staging areas. New operational work must
  be represented in GitHub issues, PRs, repository evidence, or Actions artifacts.

