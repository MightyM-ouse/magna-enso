# 01 — Repository Census

> Read-only discovery. No reviewed repository was modified. Generated 2026-06-21.
> Evidence: `git` read-only commands run with `git -C <path>` (no branch changes).

## 1. Summary

Three Git repositories and several non-Git working folders are relevant to the
Magna program. They fall into **three distinct codebases**:

| # | Path | Git? | Role (evidence-based) |
|---|---|---|---|
| A | `<LOCAL_USER_HOME>/Projects/AI/magna-command-center` | Yes | The **existing, substantially-built Magna app** ("Trinity": Magna/HELIX/Cosmos; Pre-SGN belt). The de-facto "HELIX/Magna" repo. |
| B | `<MAGNA_LOCAL_ROOT>/magna-enso` | Yes | The **new, clean, TRACE-governed rebuild** (Hermes-based runtime, Enso→Beyond stages). Governance docs + uncommitted Sprint-5 policy engine. |
| C | `<LOCAL_USER_HOME>/Projects/AI/TRACE` | Yes | The **open-source TRACE methodology + observability dashboard** (FastAPI + React). |
| — | `<MAGNA_LOCAL_ROOT>/planning` | No | Sprint-0 planning package for Enso (charter, roadmap, sprint plan, worker model, risk register, templates). |
| — | `<MAGNA_LOCAL_ROOT>/trace` | No | Holds `TRACE_STRATEGIC_BLUEPRINT_v1.0.md` (the TRACE strategic source-of-truth). |
| — | `<MAGNA_LOCAL_ROOT>/brand-assets` | No | Visual identity (Enso mark, evolution roadmap image) — referenced by docs, not directly inspected as images. |
| — | `<CHATGPT_REVIEW_SOURCE>` | No | Local-only review-memory + per-sprint review packages (deliberately outside Git, EH-0012). **This report is written here.** |

`find <LOCAL_USER_HOME>/Projects -maxdepth 4 -name .git -type d` returned exactly three
`.git` directories (A, B, C). No other repositories were found beneath the Magna /
AI parents at depth ≤ 4.

---

## 2. Repository A — `magna-command-center`

| Field | Value |
|---|---|
| Absolute path | `<LOCAL_USER_HOME>/Projects/AI/magna-command-center` |
| Purpose | Desktop-first, local-first AI command center; the existing implemented "Magna" (product + persona). The canonical "HELIX/Magna" cognitive-architecture repo. |
| Current branch | `main` |
| Working-tree status | 2 untracked dirs: `agent-logs/hermes-magna-v1-feasibility/`, `agent-logs/magna-lite-hermes-capability-governance/` (no tracked modifications) |
| Latest commit | `68981c8a540d5b99fc91f92bc4e290b09d81fccd` — `docs: add MAGNA_BLUEPRINT.md — single consolidated project blueprint` (2026-06-15) |
| Local branches | `main` (current) + ~55 feature/layer branches (`codex/*`, `layer-*`, `claude/*`, `validate-durable-runtime-linkage`) |
| Remote branches | `origin/main`, `origin/HEAD -> origin/main` |
| Tags | 23 stable tags `v0.6-*` … `v0.10.8.1-web-search-answer-polish-stable` |
| Remotes | `origin = https://github.com/MightyM-ouse/magna-command-center.git` (fetch+push) |
| Main directories | `backend/` (FastAPI app: `domains`, `core`, `providers`, `agents`, `models`, `schemas`, `db`, `api`, `services`, `orchestrator`), `src/` (Vite frontend), `docs/` (102 files), `project-knowledge/` (canon), `agent-logs/`, `scripts/`, `exports/`, `data/` (`magna.db`) |
| Technology stack | React 19 + TypeScript 6 + Vite 8; Tailwind 4; Framer Motion 12 + Three.js 0.184 (`@react-three/fiber`/`drei`); Zustand; FastAPI + SQLite; Python 3.14; Ollama local model |
| Package/dependency files | `package.json`, `package-lock.json`, `backend/.venv`, backend requirements (in venv), `tsconfig*.json`, `vite.config.ts`, `tailwind.config.ts` |
| Agent instructions | `AGENTS.md`, `CLAUDE.md`, `project-knowledge/MAGNA_AGENT_EXECUTION_PROTOCOL.md`, `project-knowledge/AGENT_GOVERNANCE.md` |
| Status documents | `MAGNA_PROJECT_STATUS_AND_NEXT_STEPS.md`, `project-knowledge/runtime_state.json`, `project-knowledge/02_COMPLETED_LAYERS.md`, `03_PENDING_LAYERS.md`, `09_CURRENT_KNOWN_ISSUES.md` |
| Architecture/product docs | `MAGNA_BLUEPRINT.md`, `project-knowledge/identity/MAGNA_ARCHITECTURE_CONSTITUTION.md`*, `THE_COSMOS.md`*, `PROTECTED_BOUNDARIES_REGISTRY.md`*, `MAGNA_EVOLUTIONARY_ARCHITECTURE_MAP.md`, `docs/FULL_PRODUCT_VISION.md`, `project-knowledge/pre-sgn-stabilization/`* |
| Backlog/sprint records | `agent-logs/project-status-and-roadmap/PROJECT_STATUS_AND_AGILE_ROADMAP.md` (referenced); per-layer `agent-logs/<feature>/` |
| Tests/validation | `backend/tests/` (~40 test modules incl. `test_atm_01_boundary_rules`, `test_csf_01_*`, `test_core_*`, `test_risk_policy_engine`); `scripts/verify_command_router.mjs` |
| CI/CD & deployment | `start-magna.sh`; `docs/DOCKER_SETUP.md` (doc only); no `.github/workflows` confirmed at root |
| Environment config | `.env`, `.env.example`, `MAGNA_LOCAL_ACCESS_POLICY.md` |
| DB schemas/migrations | `data/magna.db` + `backend/data/magna.db`; `docs/DATABASE_SCHEMA.md`; `backend/app/db/` (Alembic listed as *recommended*, not confirmed adopted) |
| TRACE artifacts | None native. `MAGNA_TASK_ORCHESTRATION_AND_TRACEABILITY_ARCHITECTURE.md` describes an internal traceability model (distinct from TRACE-the-methodology). `test_magna_prepare_task` / `test_magna_close_task` suggest prepare/close-task utilities. |

\* Referenced by `MAGNA_BLUEPRINT.md` front-matter as canonical sources; existence
asserted by the blueprint but the individual files were **not opened** in this pass
(see `14_CONTRADICTIONS...` for "not confirmed by direct read" items).

---

## 3. Repository B — `magna-enso`

| Field | Value |
|---|---|
| Absolute path | `<MAGNA_LOCAL_ROOT>/magna-enso` |
| Purpose | First operational form of Magna ("Magna Enso"), a clean TRACE-governed rebuild on a candidate Hermes base. |
| Current branch | `sprint/05-policy-engine` |
| Working-tree status | **Untracked: `policy/`, `tests/`, `trace/evidence/ENSO-0005_LIGHT_CURVE.md`** (uncommitted Sprint-5 work — see contradiction C-6) |
| Latest commit | `4d5c203cc236be84bd4b9bd8004cb88e8797a34d` — `docs(trace): refresh post-Sprint 4 project state` (2026-06-20) |
| Local branches | `main`, `audit/sprint-4-governed-hermes-baseline`, `sprint/05-policy-engine` (current) |
| Remote branches | **None** |
| Tags | **None** (planned: `v1.0-enso` … `Beyond`) |
| Remotes | **None** (local-only repo) |
| Accepted Sprint-4 baseline commit | `c7bb2b2` (per STAR_MAP) — integrated into `main` |
| Main directories | `trace/` (TRACE operating instance, 17 files incl. `evidence/`), `vendor/hermes/` (inert baseline), `policy/` (untracked engine), `tests/policy/` (untracked tests) |
| Technology stack | Python (policy engine, stdlib-only, runs under 3.14); Markdown/YAML/JSON governance artifacts. No JS runtime yet. |
| Package/dependency files | `.gitignore` only. **No `pyproject.toml`, `setup.cfg`, `pytest.ini`, `requirements.txt`, or `package.json`** in the repo. `vendor/hermes/provenance/` holds upstream manifests as inert `.source.txt` references only. |
| Agent instructions | `AGENTS.md` (entry point) + thin bridges `CLAUDE.md`, `CODEX.md`, `ANTIGRAVITY.md` |
| Status documents | `trace/STAR_MAP.md` (authoritative status), `README.md` (stale — see C-5), `trace/FEATURE_TRACKER.md` |
| Architecture/product docs | Source of truth lives in `../planning/` and `../trace/TRACE_STRATEGIC_BLUEPRINT_v1.0.md` |
| Backlog/sprint records | `trace/FEATURE_TRACKER.md` (ENSO-F-0101…1501), `../planning/MAGNA_ENSO_SPRINT_PLAN.md` (Sprints 0–15) |
| Tests/validation | `tests/policy/` (11 modules, untracked); `trace/VALIDATION_CHECKLIST.md` (Spectrometer). **Suite does not run via standard `pytest tests/`** — see §6 and C-7. |
| CI/CD & deployment | None. |
| Environment config | None in-repo (local-first; no `.env`). |
| DB schemas/migrations | None. `policy/audit.py` writes an append-only JSONL audit sink (runtime artifact, not a schema). |
| TRACE artifacts | Full TRACE operating instance: `TRACE_CONFIG.yaml`, `TRACE_ONBOARDING.md`, `STAR_MAP.md`, `CELESTIAL_INDEX.json`, `ROLE_REGISTRY.yaml`, `WORKFLOWS.yaml`, `TASK_PACKET_TEMPLATE.md`, `EVIDENCE_TEMPLATE.md`, `DECISION_LOG.md`, `FEATURE_TRACKER.md`, `RISK_REGISTER.md`, `VALIDATION_CHECKLIST.md`, `evidence/ENSO-0001..0005_LIGHT_CURVE.md` |

---

## 4. Repository C — `TRACE`

| Field | Value |
|---|---|
| Absolute path | `<LOCAL_USER_HOME>/Projects/AI/TRACE` |
| Purpose | Open-source AI-agent orchestration template + local observability dashboard (prevents context rot; measures token/time/effort ROI). |
| Current branch | `main` |
| Working-tree status | 1 untracked dir: `proposed-governed-loop/` (a proposed, unmerged orchestration changeset incl. `claude-agents/`, `orchestration-changeset/`, `run-*` dirs, push scripts) |
| Latest commit | `c6b4bbd3679ff3d7a3580c48af67b3b5d78b5884` — `fix: address review — honest CI/validation, doc accuracy, hardening, e2e tests` (2026-06-09) |
| Local/Remote branches | `main` only (+ `origin/main`) |
| Tags | None |
| Remotes | `origin = https://github.com/MightyM-ouse/trace.git` |
| Main directories | `src/server/` (FastAPI telemetry: `main.py`, `db.py`, `ingest.py`, `models.py`, `paths.py`), `src/ui/` (React + Vite dashboard), `tests/` (`test_server.py`), `agent-context/` (roles + `AGENT_CONTEXT_INDEX.json` + `permission-profiles.json`), `docs/` (+ `adr/0001`), `scripts/`, `agent-logs/` |
| Technology stack | FastAPI (Python 3.11+), SQLite + SSE; React 18 + Vite + Tailwind; ruff/eslint; OpenTelemetry (PLANNED v1.1) |
| Package/dependency files | `pyproject.toml`, `package.json`, `src/server/requirements.txt`, `src/ui/package.json` + lockfile, `Makefile` |
| Agent instructions | `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, `agent-context/roles/{planner,builder,validator}.md` |
| Status documents | `PROJECT_STATUS_AND_NEXT_STEPS.md` (2026-06-08), `README.md` (feature ledger CURRENT/PLANNED) |
| Architecture/product docs | `ARCHITECTURE_REVIEW.md`, `PROJECT_ARCHITECTURE.md`, `IMPLEMENTATION_PLAN.md`, `TECH_STACK.md`, `REPOSITORY_INFO.md`, `docs/adr/0001-evidence-in-github-telemetry-in-sqlite.md` |
| Tests/validation | `tests/test_server.py` ("e2e 6/6 pass" claimed in status — not re-run here) |
| CI/CD & deployment | `.github/` present; `Makefile` (`make dev`); honest-CI hardening noted in HEAD commit |
| Environment config | `agent-context/project.example.json`; localhost-only binding (`127.0.0.1:8000`, `:5173`) |
| TRACE artifacts | This repo *is* the TRACE reference template; the strategic source-of-truth is the separate `TRACE_STRATEGIC_BLUEPRINT_v1.0.md` under `Magna/trace/`. |

---

## 5. Non-Git working folders

| Path | Contents |
|---|---|
| `Magna/planning/` | 9 frozen Sprint-0 docs: `MAGNA_ENSO_PROJECT_CHARTER.md`, `MAGNA_EVOLUTION_ROADMAP.md`, `MAGNA_ENSO_FOLDER_AND_REPO_STRATEGY.md`, `MAGNA_ENSO_SPRINT_PLAN.md`, `MAGNA_ENSO_WORKER_MODEL.md`, `TRACE_ADOPTION_PLAN_FOR_MAGNA_ENSO.md`, `MAGNA_ENSO_RISK_REGISTER.md`, `MAGNA_ENSO_FEATURE_TRACKER_TEMPLATE.md`, `MAGNA_ENSO_DECISION_LOG_TEMPLATE.md`, `README.md`. (Also a stray 1-file `e`.) |
| `Magna/trace/` | `TRACE_STRATEGIC_BLUEPRINT_v1.0.md` (50-section strategic blueprint, 2026-06-09). |
| `Magna/ChatGPTReview/` | `AGENT_OUTPUT_REVIEW_SOURCE_DATA.md` (review memory) + 16 per-sprint review packages (sprint-2 → sprint-5). Local-only by EH-0012. |
| `Magna/` (root) | `MAGNA_ENSO_SKILLS_PLAN.md`, `_scratch/`, `.env.local`. |
| `Projects/Magna/` (separate) | `images/` only — unrelated asset folder, not a code repo. |

## 6. Validation actions performed (read-only)

- `git status/log/branch/tag/remote` on A, B, C (no branch changes; `-C` form).
- Ran the Enso policy suite with an available pytest (from the magna-command-center
  venv, `pytest 9.0.3`, Python 3.14). **Result: 7 collection ERRORS, 0 tests run** —
  `tests/policy/` is itself an `__init__`-package literally named `policy`, which
  **shadows** the source `policy/` package; with no committed `conftest.py`/pytest
  config the imports `from policy.schema import …` fail. The source modules import
  cleanly in isolation (`PYTHONPATH=. python -c "import policy.schema, policy.audit"`
  succeeds). Enso working-tree git status was identical before and after (no leakage).
- Did **not** run the magna-command-center backend suite (~40 modules / "498 passed"
  claimed) — see `08_ENVIRONMENT_ASSESSMENT.md` validation plan.
