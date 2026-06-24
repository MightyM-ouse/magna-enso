# 16 — Decisions Required From Vinay

> Each is a decision only the human owner can make. Workers must not resolve these
> silently. Recommended option marked, but the choice is yours.

## D-1 — Terminology: "Kensho" vs "Kenosha" (resolves C-1)
- **Evidence:** every repository spells the 3rd stage **"Kensho"** (Zen term: "seeing
  true nature"), matching the stage's meaning. Your prompt said "Kenosha."
- **Recommendation:** adopt **"Kensho"** (repo-consistent, semantically correct).
- **If you really mean Kenosha:** a global rename + an Event Horizon decision is needed.
- **Impact:** brand, tags (`v3.0-kensho`), all docs.

## D-2 — Repository model: one repo + tags vs separate repo per stage (resolves C-2)
- **Evidence:** **frozen EH-0003 (ACCEPTED)** = one `magna-enso` repo; stages are
  tags/releases; "no copied stage folders." Your prompt #5 said separate repo per stage.
- **Recommendation:** keep **one repo + tags** (preserves continuity & TRACE Repository
  Sovereignty; avoids drift). If you want separate repos, EH-0003 must be **SUPERSEDED**
  by a new decision — and the folder strategy + roadmap rewritten.
- **Impact:** the entire branch/tag/release strategy.

## D-3 — Program identity: which Magna is "the project"? (resolves C-3) ★ highest priority
- **Options:**
  - **(a)** Continue **magna-command-center** (finish Pre-SGN belt → SGN-01).
  - **(b)** Build the clean **magna-enso** rebuild (TRACE + governed Hermes) and treat
    command-center as legacy/HELIX donor.
  - **(c) (Recommended)** Run **both with an explicit relationship**: command-center =
    HELIX genome + reuse donor + historical evidence; magna-enso = the clean forward
    build. Reconcile the two evolution models into one canonical spine.
- **Why it gates everything:** the "clean, professionally-designed Magna project" you
  asked about **does not exist yet** and must not be created until this is set.

## D-4 — HELIX as repo or canon? (resolves C-4)
- **Evidence:** planning assumes a `Magna/magna-helix/` repo that doesn't exist; HELIX is
  currently *canon inside* `magna-command-center/project-knowledge/`.
- **Options:** (i) HELIX stays canon inside command-center; (ii) extract a dedicated
  `magna-helix` repo; **(iii, Recommended)** extract HELIX governance canon into a
  versioned `magna-helix` repo *as part of the clean build*, and fix EH-0002's path.

## D-5 — Enso Sprint-5 status truth (resolves C-6) 
- **Evidence:** uncommitted `policy/` + `tests/` + draft `ENSO-0005_LIGHT_CURVE.md` exist
  while all status docs say "Sprint 5 NOT STARTED."
- **Options:** **(a, Recommended)** acknowledge Sprint 5 is *in progress*, update
  STAR_MAP/DECISION_LOG honestly, and gate it through normal acceptance; **(b)** treat
  the code as exploratory and quarantine it until a real Sprint-5 approval; **(c)**
  discard it.
- **Note:** whichever you choose, the status docs and the working tree must agree —
  TRACE's whole point is that the repo tells the truth.

## D-6 — Authorize read-only validation? (addresses C-7, C-10)
- **Request:** allow a follow-up worker to (1) run `magna-command-center` backend tests
  + router smoke (deps present, no installs) and (2) **not** fix C-7 but report it, so
  "claimed" test states become "verified." No repo modification beyond ignored caches.
- **Recommendation:** **Approve** — it converts the weakest column ("verified now") into
  fact.

## D-7 — Hermes wording (resolves C-8)
- **Evidence:** nothing is "adopted/active"; only an inert baseline exists.
- **Recommendation:** in future docs, say Hermes is a **"candidate base, audited, not yet
  adopted"** rather than "Enso adopts Hermes capabilities." Low effort, prevents overclaim.

## D-8 — Single policy engine & single traceability spine (from `13`)
- **Evidence:** two policy engines (command-center risk engine + Enso `policy/`) and three
  traceability systems exist.
- **Decision needed:** which is canonical going forward?
- **Recommendation:** Enso `policy/` as the canonical **safety** engine (cleaner
  default-deny) *after* it is committed, test-fixed, and verified; TRACE as the canonical
  **engineering** traceability; one merged **runtime** audit/replay surface (adopting
  command-center's replay/lineage strengths).

## Decision summary table

| ID | Question | Recommended | Blocks |
|---|---|---|---|
| D-1 | Kensho vs Kenosha | Kensho | branding/tags |
| D-2 | one-repo+tags vs per-stage repos | one repo + tags | repo strategy |
| D-3 | which Magna is the project | (c) both, related | **everything** |
| D-4 | HELIX repo vs canon | extract `magna-helix` in clean build | structure |
| D-5 | Sprint-5 status truth | acknowledge + update docs | Enso integrity |
| D-6 | authorize validation | approve | verification |
| D-7 | Hermes wording | "candidate, not adopted" | accuracy |
| D-8 | canonical policy/trace spine | Enso policy + TRACE + merged runtime | clean build |
