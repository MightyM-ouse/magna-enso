# LICENSE_DEPENDENCY_AND_SBOM_PLAN.md
# Magna Enso — License, Dependency, and SBOM Plan
# Type: Local-only approval package
# Date: 2026-06-17
# Status: PLAN. No scan run; no dependencies installed.

---

## 1. Purpose

Define the license/dependency/SBOM checks that must happen **before or during** Sprint 4, because they can
independently block source import (R-02). Recommended: make these a **precondition or the first task** of
Sprint 4.

## 1a. Mandatory pre-import gate (C-02)

License/SBOM review is a **mandatory gate that must occur before any imported source is committed.** Rules:

- **Static source/manifest/license review may happen first** (reading files, manifests, `LICENSE`, and
  dependency declarations) — this is allowed and expected.
- **No Hermes runtime execution** to perform the review.
- **No Hermes build** to perform the review.
- **No runtime dependency install** unless separately approved (a static manifest read does not require installing).
- **Incompatible license OR unclear dependency status = STOP** — halt the import and escalate to the human owner.

No retained module is committed into the baseline until it has cleared this gate.

## 2. What must be checked

| Check | Description |
|---|---|
| MIT license preservation | Carry upstream MIT text + copyright notice with any imported source; update attribution/NOTICE |
| Dependency license scan | Identify licenses of every dependency a retained module needs |
| Plugin dependency review | Review dependencies of any retained plugin-related code (most plugins are removed in MVP) |
| SBOM generation | Produce a Software Bill of Materials for the retained baseline (components + versions + licenses) |
| Package inventory | List every third-party package the baseline would pull in |
| Third-party attribution | Record required attributions/notices |
| Incompatible-license stop condition | If a retained module requires a copyleft/incompatible/ToS-restricted dependency → **STOP and escalate** |

## 3. Important scoping note

Because **Option C imports only retained modules**, the dependency surface is **much smaller** than the full
Hermes dependency set — most heavy/risky dependencies (cloud providers, messaging platforms, remote backends,
MCP/plugins) belong to **removed** surfaces and are not imported. The SBOM is therefore for the *retained*
baseline, not all of Hermes.

## 4. Stop conditions (halt + escalate to human)

- A retained module requires a **copyleft** dependency that would force unwanted obligations.
- A dependency's **license is incompatible** with Magna's intended distribution.
- A bundled provider/tool carries **ToS restrictions** on use.
- Top-level MIT differs from what Sprint 2 verified, or a sub-component is **unlicensed**.

## 5. Sequencing options

- **Recommended:** license/SBOM review is the **first task inside Sprint 4** (before any import is committed),
  so import only proceeds for cleanly-licensed modules.
- **Alternative (Option D):** do the full transitive review **before** approving Sprint 4 at all (maximum caution).

## 6. Output

`LICENSE_AND_DEPENDENCY_BASELINE.md` (Sprint 4 report): MIT preservation confirmation, dependency license
table, SBOM, attributions, and any stop-condition findings.

## 7. Boundaries

Plan only. **No dependency is installed**, no scan run, no package fetched by this package. Sprint 2 verified
**top-level MIT only**; the transitive review remains open (R-02) and is scheduled here.
