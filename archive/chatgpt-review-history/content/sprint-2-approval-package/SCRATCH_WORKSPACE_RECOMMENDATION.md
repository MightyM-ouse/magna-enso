# SCRATCH_WORKSPACE_RECOMMENDATION.md
# Magna Enso — Scratch Workspace Recommendation
# Type: Local-only approval package
# Date: 2026-06-17
# Status: RECOMMENDATION. No scratch workspace created. No Hermes clone.

---

## 1. Recommended location

```
<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/
```

Inside it (created only after approval, when Sprint 2 starts):

```
_scratch/hermes-readonly-audit/
├── hermes-clone/        # read-only clone of Hermes (disposable; never committed)
└── notes/               # working notes (findings drafted here, finalized into reports)
```

## 2. Why this location

- **Outside `magna-enso/`** — so Hermes source can never enter the product repo or its Git history.
- **Outside `magna-helix/`** — so the HELIX repo is never touched.
- **Sibling under `Magna/`, prefixed `_scratch/`** — clearly disposable and easy to delete after Sprint 2.
- **Naturally untracked** — it is not inside the `magna-enso/` repo; additionally the Magna-Enso
  `.gitignore` already lists `*scratch*/` and `*hermes-audit*/` as defensive patterns, so even an
  accidental copy inside the repo would be ignored.

## 3. Rules for the scratch workspace

1. Read-only use: clone, read, inspect. **No edits, no builds, no execution** of Hermes.
2. **Never committed** to any Git repository; **never pushed**.
3. **Never copied into `magna-enso/`** (not even snippets; reports cite identifiers only).
4. Local-only; no remote, no sync.
5. **Disposable** — safe to delete entirely after Sprint 2 acceptance (provenance lives in the reports,
   not in the clone).
6. Created **only** when Sprint 2 is approved and started — **not now**.

## 4. Clone command (for reference only — DO NOT RUN until approved)

> Listed so the human owner can see exactly what would happen. Not executed by this package.

```bash
# AFTER approval only:
mkdir -p <MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit
cd <MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit
git clone --depth 1 <HERMES_SOURCE_URL> hermes-clone   # read-only inspection; no fork
cd hermes-clone && git rev-parse HEAD                   # record SHA into HERMES_PROVENANCE.md
```

- `--depth 1` keeps it lightweight for inspection. The exact Hermes source URL is supplied by the human
  owner at approval time (Decision 2 confirms the path; the URL is needed to actually clone).
- No `git remote add`, no push, no fork on any platform.

## 5. Teardown

After Sprint 2 acceptance, the scratch workspace may be deleted. All durable knowledge is captured in the
Sprint 2 reports (which cite the source URL + SHA), so nothing is lost by removing the clone.

## 6. Confirmation

This recommendation **created no workspace and cloned nothing**. `_scratch/` does not exist yet.
