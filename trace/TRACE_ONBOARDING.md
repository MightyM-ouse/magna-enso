# TRACE_ONBOARDING.md — Magna Enso

## Purpose

This file explains how any AI worker should operate inside this **TRACE-governed** repository.
Magna Enso externalizes its operating memory into the repository: you focus on the task; TRACE
preserves context, continuity, governance, and evidence.

## Required startup behavior

1. **Identify the task** — is there an active task packet (Constellation)? If yes, read it.
2. **Identify your role** — `ROLE_REGISTRY.yaml` (Galaxy Catalog). Stay within its boundaries.
3. **Identify your mode** — Discovery / Investigation / Execution / Review / Mixed (`WORKFLOWS.yaml`).
4. **Load minimal context** — use `CELESTIAL_INDEX.json` to load only the files your task needs.
   Do **not** scan the whole repo. Escalate context only when justified.
5. **Check status** — read `STAR_MAP.md` for current state and next steps.
6. **Do the work** within your allowed scope.
7. **Produce evidence** — write a Light Curve (`EVIDENCE_TEMPLATE.md`) into `evidence/`.
8. **Update status & decisions** where permitted — `STAR_MAP.md` and `DECISION_LOG.md`.
9. **Pause for human approval** before any commit, push, or material/irreversible action.

## The TRACE algorithm (applied here)

- **T — Template:** this `trace/` instance is the durable source of truth.
- **R — Route:** `CELESTIAL_INDEX.json` routes you to only the relevant context.
- **A — Assign:** `ROLE_REGISTRY.yaml` bounds your role; `WORKFLOWS.yaml` defines the mode.
- **C — Check:** run the `VALIDATION_CHECKLIST.md` (Spectrometer) before/after material changes.
- **E — Evidence:** every meaningful task leaves a Light Curve for human review.

## Evidence levels

- **Light** — identity/cosmetic/docs changes.
- **Standard** — normal feature/fix.
- **Full** — governance, policy, memory, network, security, or release work.

## Honest data contract

What changed / shipped must be **real** (artifacts, diffs, logs). Any token/cost/effort figures are
**approximate** and must be labeled as such. Never present an estimate as a measurement.
Worker role boundaries are **advisory** in v1 (role-guided), not enforced isolation — respect them anyway.

## Hard rules

Human owner is final authority. No auto-commit/push. Local-first, LAN-first, safe-by-default; no public
exposure or cloud execution by default; no hidden autonomous execution, no silent memory mutation, no
auto-skill activation. No Hermes source in this repo. The existing Magna / HELIX repo is never modified.

## Missing-information behavior

If a required TRACE artifact is incomplete, inspect the repository first, then ask the human owner only
the necessary questions. Do not invent project state.
