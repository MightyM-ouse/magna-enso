# HERMES_BASELINE_STRATEGY.md
# Magna Enso — Hermes Baseline Strategy
# Type: Local-only approval package
# Date: 2026-06-17
# Status: OPTIONS for human decision. No baseline created.

---

## 1. Purpose

Present the strategic options for how (and whether) Sprint 4 establishes a Hermes-derived baseline, and
recommend one.

> **Terminology note (C-01).** "Clean governed Hermes fork baseline" is the **historical sprint name**. The
> recommended path (Option C below) is more accurately a **Hermes-derived governed baseline through selective
> vendor import** — a full *fork* (Option B) is explicitly *not* recommended for MVP.

## 2. Options

### Option A — No fork yet; keep Hermes reference-only
- Do not import any source. Continue using the read-only audit references.
- **Pros:** zero source risk; nothing to maintain; maximal caution.
- **Cons:** no progress toward a runtime base; defers the inevitable.
- **When:** if license/dependency uncertainty is still high, or you want to pause.

### Option B — Clean fork baseline in an isolated scratch/repo branch
- Fork/branch the retained baseline in isolation; strip dangerous surfaces.
- **Pros:** real progress; isolated; reversible (branch/location can be discarded).
- **Cons:** "fork the whole thing then strip" risks carrying more than needed; heavier review.

### Option C — Selective vendor import of retained modules only
- Import **only** the Sprint 3 *retained* modules into an isolated `vendor/`-style area, with provenance +
  license preserved; never bring in removed surfaces at all.
- **Pros:** minimal surface (dangerous modules never enter); clearest provenance/traceability; easiest to
  review; best governance fit (you import the allowlist, not the denylist).
- **Cons:** requires a precise file-level retained inventory first (which is a good thing).

### Option D — Delay Sprint 4 until more dependency/license review is complete
- Do the transitive dependency/SBOM review first; then revisit A/B/C.
- **Pros:** removes the biggest open risk (R-02) before any import.
- **Cons:** slower; the review can also be done as Sprint 4's first task under Option C.

## 3. Comparison

| Criterion | A reference-only | B full fork | C selective vendor | D delay |
|---|---|---|---|---|
| Source risk now | none | medium-high | low | none |
| Progress | none | high | high | none |
| Minimal surface | n/a | weak | strong | n/a |
| Provenance clarity | n/a | medium | strong | n/a |
| Reviewability | n/a | medium | strong | n/a |
| License exposure | none | high | controlled | lowest |
| Governance fit | n/a | medium | strong | n/a |

## 4. Recommendation

**Option C — selective vendor import of retained modules only**, with the **license/SBOM review as a
precondition or the first task** (absorbing Option D's safety into C). Rationale: it imports the *allowlist*
(only retained, danger-stripped modules), gives the cleanest provenance and the easiest Antigravity review,
and never lets removed surfaces enter the repo. If the human owner prefers maximum caution, **Option D
(delay)** is the safe alternative; **Option A** if pausing entirely.

> Not recommended for MVP: **Option B (full fork)** — it carries the whole dangerous surface in before
> stripping, which is riskier and harder to review than importing only what is retained.

## 5. Boundaries

Strategy only. No baseline, fork, branch, or import is created by this package. The chosen option is
executed only after the human owner signs the Sprint 4 approval block.
