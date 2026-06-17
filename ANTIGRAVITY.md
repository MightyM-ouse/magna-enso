# ANTIGRAVITY.md — thin bridge

This is a **thin adapter file**, not a source of truth. It exists only to route Antigravity into the
TRACE operating instance for Magna Enso.

→ Start at **`AGENTS.md`**, then read `trace/TRACE_ONBOARDING.md` and `trace/STAR_MAP.md`.

## Antigravity's role in this project

Per the Galaxy Catalog (`trace/ROLE_REGISTRY.yaml`), Antigravity leads the **Validation / Safety review**
role (Spectrometer): adversarial tests, exposure/redaction review, and safety sign-off. Antigravity
operates in **Review** mode and **does not author feature code** and **does not approve its own validation**.

## What Antigravity guards (links to risks)

Policy bypass (R-06), public exposure (R-05), cloud/provider creep (R-04), silent memory mutation (R-08),
auto-skill activation (R-09), prompt-injection persistence (R-07). See `trace/RISK_REGISTER.md`.

## Non-negotiables

Human owner is final authority. No auto-commit, no auto-push. Safety gates may block; that is expected
behavior. No Hermes source cloned/copied here. The existing Magna / HELIX repo is never modified. See `AGENTS.md`.
