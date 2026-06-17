# CODEX.md — thin bridge

This is a **thin adapter file**, not a source of truth. It exists only to route Codex into the
TRACE operating instance for Magna Enso.

→ Start at **`AGENTS.md`**, then read `trace/TRACE_ONBOARDING.md` and `trace/STAR_MAP.md`.

## Codex's role in this project

Per the Galaxy Catalog (`trace/ROLE_REGISTRY.yaml`), Codex leads the **Builder** role:
implementation and code-level inspection. Codex operates in **Execution / Investigation** modes and
has **scoped** code-modify rights (only within the files a task packet allows).

## Non-negotiables

Codex must not: self-approve commits, activate capabilities, edit governance/policy *design*
unilaterally, or bypass the policy gate. Human owner is final authority. No auto-commit, no auto-push.
No Hermes source cloned/copied here (Sprint 2 audit is separate and human-approved). The existing
Magna / HELIX repo is never modified. See `AGENTS.md`.
