# 00 — Master Product Discovery & Reconstruction Report

> **Read-only discovery.** No reviewed repository was modified. Date: 2026-06-21.
> Evidence rules applied: repository evidence outranks conversation memory; current
> source + passing tests outrank status summaries; planned ≠ implemented; nothing is
> called "passing" without confirming evidence.
>
> Companion files: `01`–`17` and `EVIDENCE_INDEX.json` in this directory.

---

## 1. Executive product-owner summary

There is **not one Magna project — there are three distinct codebases**, plus a
planning layer, and the canonical understanding you provided conflates them:

1. **`magna-command-center`** — the *existing, substantially-built* Magna app
   (React + FastAPI + SQLite). This is the codebase that today embodies the
   "Magna / HELIX / Cosmos" Trinity and the "Pre-SGN Stabilization Belt"
   (HAB-01/ATM-01/CSF-01 landed; BRS-01/MEM-01/NRV-01 planned; SGN-01 blocked).
   It has a GitHub remote and 23 release tags.

2. **`magna-enso`** — a *new, clean rebuild* started 2026-06-17, governed by TRACE
   from day one, intended to be built on a *governed Hermes fork*. It uses an
   entirely different evolution vocabulary (Enso → Satori → Kensho → Bodhi →
   Prabhava → Beyond). It is **local-only (no remote)** and currently contains
   governance documents, an inert Hermes provenance baseline, and an
   **uncommitted** Sprint-5 policy engine.

3. **`TRACE`** — the *open-source methodology + observability dashboard* used to
   govern how Magna (Enso) is built. It is its own product with its own GitHub
   remote, plus a 50-section strategic blueprint.

**The cleanest mental model:** *HELIX* (the existing magna-command-center cognitive
architecture/genome) → *Magna* (the living environment) → *Magna Enso* (the first
governed operational rebuild) → built and evidenced *using TRACE*. Hermes is a
**candidate technical base** for Enso's runtime — audited but **not yet activated**.

**Where the program actually is today:** rich, disciplined *planning and governance*,
one genuinely-built legacy app, and a **brand-new rebuild that has not yet shipped a
single runtime feature**. The Enso rebuild has completed four planning/governance
sprints (skeleton, audit, governance design, inert baseline) and has begun — but not
committed or verified — its first real code (the policy engine).

---

## 2. What Magna is (evidence-based)

> *"Magna is a single-user, local-first, governed, replay-safe cognitive orchestration
> runtime. It is not a chatbot, a generic AI wrapper, a Copilot clone, or multi-user
> SaaS."* — `magna-command-center/MAGNA_BLUEPRINT.md` §1.

Magna is a **local-first, single-user, human-governed cognitive orchestration
environment** the owner talks to, designed to plan/validate/evolve work through
**bounded AI workers, traceable sessions, durable runtime state, explicit approvals,
and human final authority** — with *observability before autonomy*. The Enso charter
restates this as "The Living Expansion of Intelligence … every capability
policy-bounded, evidence-tracked, and reversible."

This matches your canonical statement #1. **Confirmed.**

---

## 3. Relationship among Magna, HELIX, Cosmos, Identity and TRACE

From `magna-command-center/MAGNA_BLUEPRINT.md` §2 ("The Trinity") and the Enso charter:

| Concept | Evidence-based meaning | Source |
|---|---|---|
| **Magna** | The organism — the user-facing environment (product + persona). | Blueprint §2 |
| **HELIX** | The *genome*: encoded doctrine, architecture, constraints, agent knowledge, capability map. "Observes and informs; does **not** mutate runtime." | Blueprint §2; Enso charter §7 |
| **Cosmos** | The *chronicle*: the ratified evolutionary record of what has *stabilized*. Never self-updating; workers never mutate it directly. | Blueprint §2; `THE_COSMOS.md` (referenced) |
| **Identity** | A **UI surface/tab** in the magna-command-center 10-tab shell, **and** a self-model concept (CSF-01 "conscious self-model" — honest who/what-I-am). *Distinct from Cosmos.* | Blueprint §4, §5 |
| **TRACE** | The *operating model* that governs **how** Magna is built and evidenced — **not** a part of Magna itself. | Enso charter §7; TRACE blueprint |

**Cosmos vs Identity (your explicit question):** *Cosmos* = the immutable **history**
of ratified evolution (a chronicle of the project's universe). *Identity* = Magna's
**present self-model + the UI tab** that answers "who/what am I, what can I do" (CSF-01).
One is a historical ledger; the other is a current self-description surface.

Your canonical statement #2 (HELIX = DNA/genome) is **Confirmed**. Note HELIX is
**conceptual canon living inside `magna-command-center/project-knowledge/`**, *not* a
separate `magna-helix/` repository (see contradiction C-4).

---

## 4. Evolution-stage comparison

⚠️ **Two different, unreconciled evolution models exist.** Do not merge them silently.

### 4a. magna-command-center — "Pre-SGN Stabilization Belt" (biological metaphor)
| Layer | Meaning | Status (per Blueprint §6) |
|---|---|---|
| HAB-01 | Habitable 10-tab UI shell | ✅ landed |
| ATM-01 | Permission boundary (nothing acts without approval) | ✅ landed |
| CSF-01 | Conscious self-model (identity truth) | ✅ landed/frozen |
| BRS-01 | Brainstem reflexes (deterministic date/time utils) | 📋 next (plan ready) |
| MEM-01 | Memory formation / recall | 📋 planned |
| NRV-01 | Nervous-system visibility | 📋 planned |
| SGN-01 | Broad command intelligence | 🔒 blocked until belt complete |

### 4b. magna-enso — "Evolution Stages" (Zen/awareness metaphor)
| # | Stage | Keywords | Release tag | Autonomy |
|---|---|---|---|---|
| 1 | **Enso** | Establish · Stabilize · Govern | `v1.0-enso` | **None by default** |
| 2 | **Satori** | Observe · Understand · Align | `v2.0-satori` | Observe-and-suggest |
| 3 | **Kensho** | Integrate · Refine · Expand | `v3.0-kensho` | Governed self-tuning |
| 4 | **Bodhi** | Decide · Act · Evolve | `v4.0-bodhi` | Bounded autonomy under policy |
| 5 | **Prabhava** | Create · Connect · Manifest | `v5.0-prabhava` | High, within governance |
| 6 | **Beyond** | Transcend · Inspire | `Beyond` (rolling) | Continuous |

**Source:** `planning/MAGNA_EVOLUTION_ROADMAP.md`. The repo evidence spells the third
stage **"Kensho"** everywhere — **not "Kenosha"** as in your canonical statement #4
(see contradiction C-1). The repo also explicitly decides stages are **releases/tags
on one repo**, **not separate repositories** — the opposite of your canonical
statement #5 (see contradiction C-2).

---

## 5. Demonstrably working today / implemented-unverified / planned-only / blocked

### ✅ Demonstrably working (or strongly evidenced by code present)
- **magna-command-center**: a real React+FastAPI+SQLite app exists (204 backend
  `.py` files, ~40 test modules, a Python venv, `magna.db`, frontend). Its status doc
  *claims* "Frontend build passes; Backend 498 passed; Router 65/65." **Not re-verified
  in this pass** (see §6 caveat) — code presence is verified, current test pass is not.
- **magna-enso Sprint-5 policy engine source** (untracked): 883 LOC across 8 modules
  implementing a genuine **fail-closed, default-deny, audit-logged, single-use-approval**
  capability gate (`policy/gate.py`, `evaluator.py`, `approval.py`, `audit.py`,
  `canonical.py`, `schema.py`, `provider.py`, `models.py`). Modules **import cleanly**
  under Python 3.14.
- **TRACE dashboard**: real FastAPI + React code present; status claims "e2e 6/6 pass."

### 🟡 Implemented but NOT verified now
- magna-command-center test/build green state (asserted in a 2026-05-23 status doc;
  HEAD is 2026-06-15 — newer than the asserted checkpoint `0acdc12`).
- magna-enso policy engine **behaviour** — its own test suite **cannot execute** via
  `pytest tests/` (package-name collision, no committed config); pass/fail unknown to me.
- TRACE "6/6 e2e" — not re-run.

### 📋 Planned only (design/docs, no runtime)
- All magna-enso capabilities beyond the policy engine: identity layer, profiles/roles,
  memory/skill governance, report-only scheduler, LAN mobile control, remote
  instruction packages, execution capture, Capability Control UI, review-package
  generator (Sprints 6–15, all `PLANNED`).
- Every Hermes-derived capability (terminal/browser/messaging/agent/memory/tools) —
  **design-only**; only an *inert provenance baseline* exists.
- magna-command-center BRS-01, MEM-01, NRV-01.

### 🔒 Blocked
- magna-command-center **SGN-01** (broad command intelligence) — blocked until the
  Pre-SGN belt completes.
- magna-enso **Sprint 5** is governance-"NOT STARTED" (yet has uncommitted code — C-6).
- Hermes runtime adoption — gated behind policy-engine readiness + separate approval.

---

## 6. Lifecycle / readiness scorecard

Classification vocabulary used: `NOT STARTED · INFORMALLY DISCUSSED · DOCUMENTED ·
DESIGNED · APPROVED · PARTIALLY IMPLEMENTED · IMPLEMENTED, NOT VERIFIED · VERIFIED IN
DEVELOPMENT · RELEASE-READY · RELEASED, NOT PRODUCTION-CONFIRMED · PRODUCTION-CONFIRMED ·
BLOCKED · UNKNOWN`.

| Dimension | magna-command-center | magna-enso | TRACE |
|---|---|---|---|
| Current lifecycle stage | **RELEASED, NOT PRODUCTION-CONFIRMED** (tagged `v0.10.x`, single-user local; production use unverified) | **PARTIALLY IMPLEMENTED** (governance done; first runtime module uncommitted/unverified) | **VERIFIED IN DEVELOPMENT** (v1 alpha; claims e2e pass) |
| Architecture readiness | DESIGNED + PARTIALLY IMPLEMENTED | DESIGNED (runtime arch not built) | DESIGNED + PARTIALLY IMPLEMENTED |
| Environment readiness | Local only (DEV). No staging/prod evidence. | Local only; not yet runnable as an app. | Local only (DEV). |
| UX readiness | PARTIALLY IMPLEMENTED (10-tab shell + 3D avatar exist) | NOT STARTED (Capability Control UI is Sprint 13) | DOCUMENTED + PARTIALLY IMPLEMENTED (dashboard) |
| Backlog readiness | DOCUMENTED (two parallel roadmaps to reconcile) | **APPROVED** (Sprints 0–15 frozen; feature tracker live) | DOCUMENTED |
| TRACE engineering maturity | Low (internal traceability ≠ TRACE) | **High** (full TRACE instance, Light Curves, Event Horizon) | n/a (is TRACE) |
| TRACE runtime maturity | Partial internal (event lineage, replay) | None active (policy engine is the first runtime trace surface, unverified) | Real telemetry pipeline (its purpose) |
| Release readiness | Tagged releases exist; no public/prod release | NOT STARTED (RC is Sprint 15) | v1 alpha on GitHub |

---

## 7. Objective percentages (numerator / denominator)

> Per the rules, **no single intuitive overall completion %** is given. Each metric
> below has an explicit denominator. Full weighting/limitations in
> `15_ENGINEERING_LEARNING_BASELINE.md` is *not* the home — see per-metric notes here
> and in `03_PRODUCT_LIFECYCLE_ASSESSMENT.md`.

**magna-enso — implementation completion (sprint count basis)**
- Numerator = sprints with a human-accepted deliverable = **4** (Sprints 1–4).
- Denominator = planned sprints to RC = **15** (Sprints 1–15; Sprint 0 = planning).
- = **27%** of the planned sprint roadmap accepted. *Limitation:* Sprints 1–4 are
  skeleton/audit/design/inert-baseline — **0 runtime features** accepted. Confidence: High.

**magna-enso — runtime-feature completion**
- Numerator = runtime features `DONE` with verified behaviour = **0**.
- Denominator = runtime features in tracker (ENSO-F-0501…1501) = **12**.
- = **0% verified** (1 of 12, the policy gate, is *coded-but-unverified+uncommitted*).
  Confidence: High.

**magna-enso — TRACE engineering-plane adoption (artifact basis)**
- Numerator = required TRACE instance artifacts present = **12 / 12** core artifacts +
  5 Light Curves.
- Denominator = TRACE Core Standard artifact set (per folder strategy §4) = **12**.
- = **100% of the engineering-plane artifact skeleton present.** *Limitation:* artifact
  presence ≠ runtime traceability. Confidence: High.

**magna-command-center — Pre-SGN belt completion**
- Numerator = belt layers landed = **3** (HAB-01, ATM-01, CSF-01).
- Denominator = belt layers before SGN-01 = **6** (HAB/ATM/CSF/BRS/MEM/NRV).
- = **50% of the stabilization belt landed** (per Blueprint §6 self-report; not
  independently re-verified). Confidence: Medium (status self-reported).

**magna-command-center — test pass rate**
- Claimed **498 passed** backend + **65/65** router (status doc 2026-05-23).
- **Verified now: UNKNOWN** (not re-run). Denominator/numerator therefore *as claimed*,
  not *as confirmed*. Confidence: Low (stale + unverified).

**Hermes capability activation**
- Numerator = Hermes capabilities active in Magna = **0**.
- Denominator = capability classes considered (terminal, browser, messaging, agent,
  memory, plugin/MCP, scheduler, cloud) = **8**.
- = **0% active**; 100% are design-only or inert-baseline. Confidence: High.

---

## 8. Main contradictions (full list in `14`)

| ID | Contradiction | Evidence | Decision owner |
|---|---|---|---|
| C-1 | Canon says spelling **"Kenosha"**; all repos say **"Kensho"**. | `MAGNA_EVOLUTION_ROADMAP.md`, `FOLDER_AND_REPO_STRATEGY.md`, `README.md`, `STAR_MAP` | Vinay |
| C-2 | Canon says **separate repo per stage**; repos decide **one repo, stages = tags** (frozen EH-0003). | `EH-0003`, folder strategy §3/§8, roadmap §5 | Vinay |
| C-3 | Canon treats Magna as one product; evidence shows **two parallel codebases** with different evolution vocabularies. | command-center vs enso | Vinay |
| C-4 | Planning assumes a `Magna/magna-helix/` repo; the real existing repo is `magna-command-center` one level up, not under the parent, not named magna-helix. | `EH-0002`, folder strategy §2 | Vinay |
| C-5 | Enso `README.md` says "Sprint 1"; `STAR_MAP.md` says "between Sprint 4 and 5." | enso README vs STAR_MAP | Update doc |
| C-6 | Governance docs say **"Sprint 5 NOT STARTED / no policy engine"**, but `policy/` + `tests/` + `ENSO-0005_LIGHT_CURVE.md` exist (untracked) on `sprint/05-policy-engine`. | git status; `policy/*.py` | Vinay |
| C-7 | Sprint-5 test suite **cannot run** (`tests/policy` shadows `policy`); no committed pytest config. | pytest run (7 collection errors) | Builder fix |
| C-8 | Canon says Enso **"adopts" Hermes capabilities**; evidence = **inert baseline only, zero active**. | `vendor/hermes/README.md`, EH-0015 | Wording |

---

## 9. Decisions required from Vinay (full list in `16`)

1. **Terminology:** Confirm **"Kensho"** (repo-consistent) vs **"Kenosha"** (your prompt).
2. **Repo model:** Confirm **one-repo-with-tags** (frozen EH-0003) vs **separate repo
   per stage** (your prompt #5). These are mutually exclusive.
3. **Program identity:** Is the goal to (a) continue **magna-command-center**, (b) build
   the clean **magna-enso** rebuild, or (c) run both with a defined relationship? The
   "clean professionally-designed Magna project" you mention is *not yet created* and
   must not be started without this decision.
4. **HELIX repo:** Is HELIX (i) canon inside magna-command-center, (ii) a future extracted
   `magna-helix` repo, or (iii) both? The folder strategy assumes a repo that doesn't exist.
5. **Sprint-5 status truth:** Should the uncommitted `policy/` + `tests/` be treated as
   started Sprint-5 work (update STAR_MAP/DECISION_LOG) or discarded/held?
6. **Validation mandate:** May a follow-up worker run the magna-command-center and
   magna-enso test suites (read-only, no installs) to convert "claimed" → "verified"?

---

## 10. Recommended next foundation phase

See `17_RECOMMENDED_FOUNDATION_SEQUENCE.md`. In short:
**(1)** Resolve C-1…C-4 and decision #3 (program identity) — these gate everything.
**(2)** Reconcile the two evolution models and the two roadmaps into one canonical
spine. **(3)** Honestly reconcile Enso Sprint-5 status (C-6) and fix the test-collision
(C-7) before any Sprint-5 acceptance. **(4)** Only then scope the "clean Magna project."
Do **not** create the new repository, fork Hermes, or start a sprint until #1–#3 land.

---

## 11. Confidence & limitations of this report

- **High confidence:** repository inventory, git facts, Enso governance state, the
  existence/shape of the policy engine, the contradictions list.
- **Medium/low confidence:** current test-pass state of either app (not re-run);
  contents of magna-command-center canon files only *referenced* (constitution, REG,
  THE_COSMOS, pre-sgn specs) — asserted by the blueprint but not opened in this pass;
  TRACE blueprint detail beyond its 50-section index + executive framing.
- This pass prioritized **static discovery**. One non-destructive command (the Enso
  policy pytest run) was executed; it created no tracked changes.
