# SOURCE_ISOLATION_AND_PROVENANCE_PLAN.md
# Magna Enso — Source Isolation and Provenance Plan
# Type: Local-only approval package
# Date: 2026-06-17
# Status: PLAN for Sprint 4 execution (if approved). No source imported now.

---

## 1. Purpose

Define exactly how, if Sprint 4 is approved, Hermes source is isolated and its provenance recorded — so that
every imported byte is traceable and nothing enters by a hidden path.

## 2. Exact source identity

| Field | Value |
|---|---|
| Source repo | `https://github.com/nousresearch/hermes-agent` |
| Source SHA (pin) | `33b1d144590a211100f42aa911fd7f91ba031507` (the Sprint 2 audited SHA) |
| Source location (existing, read-only) | `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/` (Sprint 2 scratch clone) |
| Upstream license | MIT (top-level verified in Sprint 2; transitive review pending — R-02) |

> If the existing scratch clone's HEAD differs from the pinned SHA, Sprint 4 must re-pin to `33b1d144` (or a
> newer SHA only with explicit human approval + a new Event Horizon entry).

## 3. Exact target (if approved, under Option C)

| Field | Value |
|---|---|
| Target area | an isolated vendor area inside the baseline, e.g. `magna-enso/vendor/hermes/` (created only on approval) |
| Import scope | **only** the Sprint 3 *retained* modules (allowlist) — see `MVP_RETAINED_SURFACES_PLAN.md` |
| Excluded | all removed/disabled surfaces — never imported (see `DANGEROUS_SURFACE_REMOVAL_PLAN.md`) |

## 3a. Vendor import quarantine (C-03)

If a target such as `magna-enso/vendor/hermes/` is used, the imported source must be **inert / quarantined**:

- **Not wired into runtime** — no startup/app path imports it.
- **Not imported by application code** — nothing in Magna Enso `import`s the vendored modules.
- **Not exposed through CLI/UI** — no command or screen invokes it.
- **Not executable** — it does not run; no entry points are hooked up.
- **Not registered as tools** — import-time self-registration is severed (Sprint 2: tool modules self-register
  at import); the vendored code registers nothing.
- **Not package-discovered as active code** — excluded from package discovery / plugin discovery / test
  collection so no mechanism auto-loads it.

The vendored source exists as **quarantined reference material for later, governed wiring (Sprint 5+)** — it
is present but cannot act.

## 3b. Branch / baseline-path isolation (C-04)

If Sprint 4 is later approved, execution runs in an **isolated branch or an approved baseline path** and
**must not directly mutate `main` without review**:

- Work on an isolated branch (e.g. `sprint/04-governed-baseline`) or an approved baseline location.
- Merge to `main` only via a human-reviewed review-package (Light Curve) — never a direct push to `main`.
- No auto-commit/auto-push; no force-push (frozen governance, EH-0008).

## 4. No-hidden-copy rules

1. **Allowlist only:** import only files on the explicit retained inventory. No "grab the folder" imports.
2. **No transitive surprise:** if a retained module imports a removed surface, that is a finding — resolve it
   (stub/sever) before import; do not silently pull the dependency in.
3. **No binaries/secrets/credentials** imported.
4. **Every imported file is listed** in the inventory (no untracked additions).
5. **Diff is reviewable:** the import is presented as a reviewable change set, not an opaque drop.

## 5. Required artifacts (Sprint 4 outputs)

- **File inventory** (`SOURCE_IMPORT_INVENTORY.md`): every imported file, with source path → target path.
- **Provenance manifest** (`HERMES_SOURCE_PROVENANCE_MANIFEST.md`): source repo + SHA + per-file origin +
  import date + tool/method; ideally per-file hash for verification.
- **Diff report**: what changed vs. upstream (e.g. severed imports, removed calls).
- **License preservation**: upstream LICENSE/attribution carried with the imported source; `NOTICE`/attribution
  updated.

## 6. License preservation rule

The upstream MIT license text and copyright notice **must** be preserved alongside any imported source, and
attribution recorded. No imported file loses its license header. (Ties to `LICENSE_DEPENDENCY_AND_SBOM_PLAN.md`.)

## 7. No source import without approval

No Hermes source is copied into `magna-enso/` until the human owner signs the Sprint 4 approval block and the
baseline option is chosen. This package imports nothing.

## 8. Boundaries

Plan only. The Sprint 2 scratch clone is read-only reference; it is not modified by this package, and the
target vendor area does not exist yet.
