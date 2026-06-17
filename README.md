# Magna Enso

> The first living circle — the first operational form of **Magna**, the living cognitive
> orchestration environment built upon the DNA of **HELIX**.

**Stage keywords:** Establish · Stabilize · Govern · **Release target:** `v1.0-enso`

Magna Enso is a **local-first, LAN-first, human-governed** cognitive orchestration environment.
Every capability is policy-bounded, evidence-tracked, and reversible. It is **TRACE-governed**
(Template · Route · Assign · Check · Evidence) from day one, and the **human owner is the final authority**.

---

## Status

| | |
|---|---|
| Current sprint | **Sprint 1 — TRACE Project Skeleton** |
| Contains | TRACE operating instance + project-entry files only |
| Runtime code | **None yet** (begins with a clean governed Hermes fork baseline at Sprint 4) |
| Operating model | TRACE — AI Project Profile, regulated-leaning governance |

This repository currently holds **no runtime features**. It establishes the governance skeleton that all
later work must pass through.

## Available today (Sprint 1)

- TRACE operating instance under `trace/` (config, onboarding, status, context index, roles,
  workflows, task-packet & evidence templates, decision log, feature tracker, risk register, validation checklist).
- Universal agent entry point (`AGENTS.md`) + thin model bridges.

## Planned (per the Sprint 0 sprint plan)

- Sprint 2 — Hermes read-only audit (separate scratch workspace, after explicit approval).
- Sprint 3 — Capability governance design (the policy model / Polaris).
- Sprint 4 — Clean governed Hermes fork baseline (provenance + SHA + MIT attribution).
- Sprint 5 — Policy engine foundation (default-deny, report-and-approve).
- Sprints 6–15 — identity, profiles/roles, memory & skill governance, report-only scheduler,
  LAN mobile control, remote instruction package, local execution capture, Capability Control UI,
  evidence & review packages, stabilization & release candidate.

## Honest limitations

- Worker roles are **advisory / role-guided** in v1, not technically enforced isolation.
- The **Hermes Agent** UI/E2E worker is a **candidate, subject to validation** (decision `EH-0005B`, PROPOSED).
- What is always real: repository artifacts, decisions, and (later) git diffs, test logs, and review-packages.

## How agents enter

Read **`AGENTS.md`**, then `trace/TRACE_ONBOARDING.md`, then `trace/STAR_MAP.md`.

## Evolution

`v1.0-enso` → `v2.0-satori` → `v3.0-kensho` → `v4.0-bodhi` → `v5.0-prabhava` → `Beyond` (rolling).
Stages are **releases/tags on this one repository**, never copied code folders.

## License

To be set when runtime code is introduced (Sprint 4 baseline preserves upstream attribution).
Until then this repo contains documentation/governance artifacts only.
