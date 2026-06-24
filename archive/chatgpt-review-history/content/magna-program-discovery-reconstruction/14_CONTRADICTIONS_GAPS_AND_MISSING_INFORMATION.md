# 14 — Contradictions, Gaps & Missing Information

> Every material contradiction is recorded with evidence and a decision owner. Not
> resolved here (per task boundaries).

## 1. Contradictions vs the canonical understanding

| ID | Canon statement | Repository evidence | Severity | Owner |
|---|---|---|---|---|
| **C-1** | #4 "official spelling is **Kenosha**" | All Enso docs spell **"Kensho"** (Zen: "seeing true nature"). `MAGNA_EVOLUTION_ROADMAP.md` §3/§4.3, `FOLDER_AND_REPO_STRATEGY.md` §6, enso `README.md`, `STAR_MAP`. | High (identity/terminology) | Vinay |
| **C-2** | #5 "each stage has a **separate repository**" | **Frozen EH-0003 (ACCEPTED):** stages are **releases/tags on ONE repo, never copied folders.** `FOLDER_AND_REPO_STRATEGY.md` §3/§8, roadmap §5, charter Frozen Decisions. | High (architecture) | Vinay |
| **C-3** | #1 implies a single "Magna" | **Two parallel codebases:** `magna-command-center` (Trinity + Pre-SGN belt, GitHub remote, v0.10.x) and `magna-enso` (clean rebuild, local-only). Different evolution vocabularies. | High (program scope) | Vinay |
| **C-8** | #6/#7 "Enso **adopts** Hermes capabilities (terminal/browser/messaging/agent/memory/tools)" | **Zero adopted/active.** Only an inert provenance baseline (`vendor/hermes/README.md`); EH-0013/0015 explicitly forbid activation. | Medium (wording vs reality) | Vinay (accept wording) |

## 2. Internal contradictions (within the repos)

| ID | Contradiction | Evidence | Owner |
|---|---|---|---|
| **C-4** | Folder strategy & EH-0002 assume `Magna/magna-helix/` exists as a pointer to the HELIX repo. **It does not exist.** The real existing repo is `magna-command-center` one level up at `Projects/AI/`, not under `Projects/AI/Magna/`, and not named `magna-helix`. | `EH-0002`, folder strategy §2; `find` results | Vinay |
| **C-5** | Enso `README.md` "Current sprint: **Sprint 1**" vs `STAR_MAP.md` "**between Sprint 4 and 5**." `TRACE_CONFIG.yaml` also says `current_sprint: 1`. | enso README, STAR_MAP, TRACE_CONFIG | Doc update |
| **C-6** | `STAR_MAP`, `DECISION_LOG` (EH-0015), charter all say **"Sprint 5 NOT STARTED / no policy engine / no runtime code (src/)"**, but `policy/` (8 modules, 883 LOC), `tests/policy/`, and `trace/evidence/ENSO-0005_LIGHT_CURVE.md` **exist (untracked)** on branch `sprint/05-policy-engine`. | `git status`; `policy/*.py`; STAR_MAP §"What does NOT exist yet" | Vinay |
| **C-7** | Sprint-5 test suite **cannot execute** via standard `pytest tests/`: `tests/policy/` is an `__init__`-package literally named `policy`, shadowing the source `policy/` package; no committed `conftest.py`/pytest config. Source modules import fine in isolation. | pytest run → 7 collection ERRORs; direct import OK | Builder |
| **C-9** | TRACE naming is **inconsistent across the program**: open-source TRACE repo uses plain Planner/Builder/Validator + Template/Route/Assign/Check/Evidence; Enso uses astronomy names (Star Map, Light Curve, Polaris…). Same methodology, two vocabularies. | TRACE `CLAUDE.md`/`agent-context/roles` vs `TRACE_CONFIG.yaml` naming map | Low (by design, but document it) |
| **C-10** | command-center status doc (2026-05-23, checkpoint `0acdc12`, "498 passed") is **older than HEAD** (`68981c8`, 2026-06-15). Claimed green state is stale and not re-verified. | status doc header vs `git log` | Validation worker |

## 3. Gaps & missing information ("Not confirmed from available project evidence")

| Topic | Status |
|---|---|
| magna-command-center canon files (`MAGNA_ARCHITECTURE_CONSTITUTION.md`, `PROTECTED_BOUNDARIES_REGISTRY.md`, `THE_COSMOS.md`, `pre-sgn-stabilization/` specs incl. HAB-01/ATM-01/CSF-01/BRS-01/MEM-01/NRV-01 records) | **Referenced by the Blueprint but NOT opened in this pass.** Existence asserted; content unverified. |
| Entry/exit criteria for Satori→Beyond | **Not confirmed** — only theme + planned maturity exist. |
| How the HELIX genome itself versions across stages | **Not confirmed.** |
| Current test pass state (all three repos) | **Not verified now** (only Enso policy suite run → fails to collect). |
| Accessibility / responsive evidence (any UI) | **Not confirmed.** |
| Production / staging / DR environments | **None found.** |
| `runtime_state.json` drift (Blueprint §10 names it as a known drift source) | Noted by the Blueprint; file not opened. |
| TRACE blueprint detail (50 sections) | Only index + executive framing read; section bodies (e.g. v1/v2/v3 Govern definitions, Observatory strategy) not fully read. |
| `.env.local`, `.env`, secrets | Not opened (correctly — secrets policy). |
| `MAGNA_ENSO_RISK_REGISTER.md` / `TRACE_ADOPTION_PLAN_FOR_MAGNA_ENSO.md` full content | Not opened (R-06 OPEN known from STAR_MAP/EH-0015). |
| `proposed-governed-loop/` (TRACE) intent/quality | Listed only; not assessed. |

## 4. Stop-rule check

None of the hard stop conditions were triggered: all repo paths were located, the
report directory was writable, no destructive action was required, and product
identity *can* be described from evidence (though it requires a Vinay decision to
*finalize* — see C-3 and `16`). Proceeding was therefore appropriate; the identity
decision is escalated rather than assumed.
