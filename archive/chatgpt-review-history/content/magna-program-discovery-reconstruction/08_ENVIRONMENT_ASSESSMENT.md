# 08 — Environment Assessment

> Standard environment tiers: local, dev, test, integration, staging/UAT, production,
> recovery. **Finding: only LOCAL exists, everywhere. No dev/test/staging/prod/recovery
> infrastructure is evidenced in any repo.**

## 1. Environment matrix

| Tier | magna-command-center | magna-enso | TRACE |
|---|---|---|---|
| Local | ✅ `start-magna.sh`, Vite :127.0.0.1, uvicorn :8010 | 🟡 not runnable yet (no app) | ✅ `make dev`, :8000 + :5173 |
| Development | ⬜ (= local) | ⬜ | ⬜ (= local) |
| Test | 🟡 venv + `pytest backend/tests` + router smoke | 🟡 `tests/policy` (cannot run, C-7) | 🟡 `tests/test_server.py` |
| Integration | ⬜ | ⬜ | ⬜ |
| Staging / UAT | ⬜ | ⬜ | ⬜ |
| Production | ⬜ (no evidence) | ⬜ | ⬜ (localhost-only by design) |
| Recovery / backup | 🟡 "restart rehydration / boot recovery" in code only | ⬜ | 🟡 JSONL write-ahead fallback |

## 2. Per-concern detail

| Concern | Evidence |
|---|---|
| Configuration | command-center: `.env` + `.env.example` + `MAGNA_LOCAL_ACCESS_POLICY.md`; enso: none in-repo (local-first); TRACE: `agent-context/project.example.json` |
| Secrets handling | "never commit secrets; `.env.example` placeholders only; no `.env` reads by agents" (AGENTS.md, charter). `.env.local` exists under `Magna/` (not inspected — secret). |
| Storage | command-center SQLite `magna.db`; enso audit JSONL (runtime); TRACE SQLite telemetry + JSONL WAL |
| Model providers | command-center: local Ollama (default), OpenAI/ChatGPT (opt-in, gated), Tavily web search (gated, mock by default); enso: none yet; TRACE: n/a |
| External integrations | All **disabled by default**; cloud review opt-in; web search permission-gated/mock |
| Deployment | None automated. `docs/DOCKER_SETUP.md` is documentation only; no compose/k8s/CI deploy evidenced |
| Monitoring | command-center Phase-E runtime observability (in-app, read-only); TRACE dashboard (its purpose); enso none |
| Backup / rollback | command-center "durable runtime linkage / restart rehydration / boot recovery" (code, `test_phase_3b_boot_recovery`); no external backup/DR |
| Network posture | All bind localhost/LAN; no public exposure; enso charter mandates LAN-first, no public by default |
| Evidence of actual use | command-center `data/magna.db` present (suggests real local sessions); `agent-logs/` 116 entries; enso evidence = Light Curves only |

## 3. CI/CD

- **TRACE**: `.github/` present; HEAD commit "honest CI/validation" hardening; branch
  protection *planned* (REPOSITORY_INFO: "main protected — changes via reviewed PRs").
- **magna-command-center**: no `.github/workflows` confirmed at root; validation is
  manual (`npm run build`, `pytest`, router smoke) per AGENTS.md.
- **magna-enso**: none.

## 4. Validation plan (NOT executed — per task boundaries)

To convert "claimed" → "verified" without installing dependencies or modifying repos:

1. **magna-command-center backend tests** (deps already present in `backend/.venv`):
   `cd magna-command-center && PYTHONPATH=backend backend/.venv/bin/python -m pytest backend/tests -q`.
   *May create:* `__pycache__`, `.pytest_cache`. *Git impact:* `.gitignore` covers these.
   Record `git status` before/after.
2. **Router smoke:** `node scripts/verify_command_router.mjs` (needs node + node_modules,
   present).
3. **Frontend build:** `npm run build` — *creates `dist/`* (Tier-1 junk, ignored). Skip
   if avoiding any artifact creation.
4. **magna-enso policy tests:** blocked by C-7 — requires a `conftest.py`/pytest config
   fix (a repo modification) before it can run. **Do not modify;** flag for the Builder.
5. **TRACE e2e:** needs `make dev` + a live session; out of scope for a read-only pass.

> Per task rules: do not install dependencies, do not clean/reset generated files,
> record exact failures without fixing. Items 1–3 are safe read-only-ish runs a future
> validation worker can perform with your approval.
