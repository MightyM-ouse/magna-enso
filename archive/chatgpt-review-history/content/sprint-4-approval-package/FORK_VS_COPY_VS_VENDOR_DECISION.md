# FORK_VS_COPY_VS_VENDOR_DECISION.md
# Magna Enso — Fork vs Copy vs Vendor Decision
# Type: Local-only approval package
# Date: 2026-06-17
# Status: ANALYSIS + recommendation for human decision. No source imported.

---

## 1. Purpose

Compare the concrete mechanisms for bringing (or not bringing) Hermes source into Magna Enso, scored on the
criteria that matter for a governed baseline.

## 2. Mechanisms compared

1. **Full fork** — adopt the whole upstream repo, diverge.
2. **Shallow copy** — copy files in, no upstream history.
3. **Selective vendor import** — copy only retained modules into a `vendor/` area with provenance.
4. **Reference-only** — do not import; read in place.
5. **Submodule** — nested git pointer to upstream.
6. **Patch-based fork** — pristine upstream + your changes as patches.

## 3. Scoring (H = high/good, M = medium, L = low/poor)

| Criterion | Full fork | Shallow copy | Selective vendor | Reference-only | Submodule | Patch-based |
|---|---|---|---|---|---|---|
| Traceability (what came from where) | M | L | **H** | H (nothing imported) | H | H |
| Maintenance burden | L | M | M | H | L | M |
| License visibility | M | L | **H** | H | M | H |
| Safety (dangerous code excluded) | L | M | **H** | H | L | M |
| Reviewability | M | M | **H** | H | M | H |
| Rollback (undo cleanly) | M | M | **H** | H | H | H |
| Governance fit (import allowlist, not denylist) | L | L | **H** | M | L | M |

## 4. Reading the table

- **Reference-only** scores well but makes **no progress** toward a runtime base — it is Option A (pause).
- **Full fork / shallow copy** bring the **whole dangerous surface** in before stripping → poor safety and
  governance fit; shallow copy also loses provenance.
- **Submodule** tightly couples to upstream and pulls *everything* (including dangerous surfaces) → poor
  safety/governance fit for MVP.
- **Patch-based fork** is strong for auditable divergence but assumes you keep the full upstream tree present.
- **Selective vendor import** is the only mechanism that is simultaneously strong on traceability, license
  visibility, safety, reviewability, rollback, and governance fit — because you import **only the retained
  allowlist**, with provenance.

## 5. Recommendation

**Selective vendor import** (the mechanism behind Baseline Strategy Option C): copy only the Sprint 3
*retained* modules into an isolated, provenance-tracked area; never import removed surfaces; preserve license
and record SHA `33b1d144`. Patch-based fork is a reasonable secondary if the human owner wants to track
upstream more tightly later.

## 6. Boundaries

Decision analysis only. No fork, copy, vendor import, submodule, or patch is created by this package.
Execution follows the signed Sprint 4 approval and the chosen baseline option.
