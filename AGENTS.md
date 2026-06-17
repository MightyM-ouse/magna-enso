# AGENTS.md — Magna Enso

This repository is **Magna Enso** — the first operational form of Magna (the living cognitive
orchestration environment built on the DNA of HELIX). It is governed by **TRACE**
(Template · Route · Assign · Check · Evidence) from day one.

> **Status:** Sprint 1 — TRACE Project Skeleton. No runtime code yet. This repo currently contains
> only the TRACE operating instance and project-entry files.

## Before you do anything

1. Read `trace/TRACE_ONBOARDING.md` — how to operate inside this TRACE repository.
2. Read `trace/STAR_MAP.md` — the current project status and next steps.
3. Identify your **role** (`trace/ROLE_REGISTRY.yaml`) and your **mode**
   (Discovery / Investigation / Execution / Review / Mixed — see `trace/WORKFLOWS.yaml`).
4. Load **only** the context your task needs via `trace/CELESTIAL_INDEX.json`. Do not scan the whole repo.
5. Work from a **task packet** (`trace/TASK_PACKET_TEMPLATE.md`). Produce **evidence**
   (`trace/EVIDENCE_TEMPLATE.md`) into `trace/evidence/`.
6. Log material decisions in `trace/DECISION_LOG.md` (Event Horizon).

## Hard rules (frozen in Sprint 0)

- **Human owner (Vinay) is the final authority.** Nothing material ships without human approval.
- **No auto-commit. No auto-push. No force-push.**
- **Local-first, LAN-first, safe-by-default.** No public exposure by default. No cloud execution by default.
- **No hidden autonomous execution. No silent memory mutation. No auto-activation of skills.**
- **The existing Magna / HELIX repository is never modified.**
- **No Hermes source is cloned or copied into this repo.** (A read-only Hermes audit is a *future*
  sprint — Sprint 2 — performed in a separate scratch workspace after explicit human approval.)
- **Future stages (Satori → Beyond) are releases/tags, not copied code folders.**
- **Repository sovereignty:** the repository is the source of truth, not any chat session.

## Model-specific bridges

Thin adapter files exist for convenience and **must not** become separate sources of truth:
`CLAUDE.md`, `CODEX.md`, `ANTIGRAVITY.md`. They all point back here.

## Source of truth

- Project identity & governance: `../planning/MAGNA_ENSO_PROJECT_CHARTER.md`
- Repo/branch/tag strategy: `../planning/MAGNA_ENSO_FOLDER_AND_REPO_STRATEGY.md`
- TRACE methodology: `../trace/TRACE_STRATEGIC_BLUEPRINT_v1.0.md`
- Worker model: `../planning/MAGNA_ENSO_WORKER_MODEL.md`
