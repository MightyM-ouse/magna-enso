---
document: 00_MASTER_FOUNDATION_SUMMARY
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT — informs and proposes; decides nothing; grants no approval on Vinay's behalf
scope: Program-wide architecture + Magna Enso technical-specification foundation (corrected)
current_vs_target: Mixed — separated explicitly throughout
date: 2026-06-21
evidence_sources:
  - magna-program-evidence-completion/ (accepted baseline)
  - planning/ canonical docs (roadmap, charter, sprint plan, repo strategy, TRACE adoption)
  - TRACE_SOURCE_RESOLUTION.md; CORRECTION_REPORT.md
change_control: Corrected package; the -draft package is preserved. Governed; nothing deleted.
---

# 00 — Master Foundation Summary (corrected)

> **Status: DRAFT_FOR_HUMAN_REVIEW.** Prepares architecture + technical-specification foundations. Does **not**
> implement, create a repository, modify any reviewed repository, start/number sprints, activate Hermes,
> accept BRS-01, select a policy engine, or unblock SGN-01. Vinay is final authority; nothing here approves.

## Human table of contents
1. What changed (corrected package)
2. The one-paragraph truth
3. The repository model (corrected)
4. Three buckets: current / target / reuse
5. Top decisions for Vinay
6. Hard boundaries preserved
7. Reading order
8. Open decisions
9. Change-control note

## AI navigation index
- `whats_changed` → §1 (CORRECTION_REPORT.md) · `truth` → §2 · `repo_model` → §3 · `buckets` → §4
- `decisions` → §5 (`17`; `registries/MAGNA_OPEN_DECISIONS.yaml`) · `boundaries` → §6

## 1. What changed (corrected package)
This corrects the `-draft` package per 13 corrections (full list: `CORRECTION_REPORT.md`). Headlines:
`magna-enso` **is** the forward Enso repo (no new clean repo); TRACE sources resolved (`TRACE_SOURCE_RESOLUTION.md`);
stage model rebuilt from the approved roadmap; Pre-SGN vs evolution separated; five-dimension status model;
full component IDs; all-52 traceability; state machines + outcome taxonomy; Hermes scope plan (0/6); HELIX
versioning options. The `-draft` package is preserved unchanged.

## 2. The one-paragraph truth (evidence-grounded)
**Magna** is a single-user, local-first, governed, replay-safe cognitive orchestration runtime and the
user-facing organism. **HELIX** is its read-only genome (informs/constrains, never mutates runtime).
**Cosmos** is the ratified chronicle; **Identity** the current truthful self-model (distinct). The strongest
**verified** runtime is **Magna Command Center** (ten-tab UI, FastAPI/SQLite, durable event/workflow/approval/
orchestration, replay; backend 701/701, router 65/65, build PASS) — a **reuse donor**. **`magna-enso`** is the
**forward Enso stage repository** (branch `sprint/05-policy-engine`, HEAD `4d5c203`); its Sprint 5 policy
control is **harness-level, IN_REVIEW, not accepted, not runtime-integrated** (49 unittest pass; pytest broken).
**Hermes** is 0/6 active. **TRACE** governs engineering (partly current) and a planned runtime plane.

## 3. The repository model (corrected — human decision 4)
- `magna-enso` = current forward Enso repo (continue it). Architecture package integrated **into it** after
  approval (the four C13 gates). Command Center = reuse donor.
- Future stages = **separate repos** (`magna-satori`, `magna-kenosha`, `magna-bodhi`, `magna-prabhava`,
  `magna-beyond` after a separate decision). **KENOSHA** is the official third-stage spelling ("Kensho"
  superseded). Repo-creation gates apply only to **future-stage** repos. (Supersedes the historical one-repo
  decision — `04`.)

## 4. Three buckets
| Bucket | Contents | Source |
|---|---|---|
| Verified-current | Command Center primitives (validated); Enso Sprint 5 harness (IN_REVIEW); TRACE template; HAB/ATM/CSF accepted, BRS validated-not-accepted | `05`, `04 ec` |
| Target | Enso target built into magna-enso; TRACE runtime plane; cross-plane contract; environments beyond local/test | `06`, `09`, `13` |
| Reuse candidate | MCC primitives; Enso policy/fingerprint/audit; TRACE artifacts; Hermes metadata only | `15`, `16 ts` |

## 5. Top decisions for Vinay (full: `17`)
ADR-R1 engine (compose vs select — **not chosen**); ADR-R2 repo-strategy + KENOSHA supersession Event Horizon
ID; ADR-R3 TRACE contract; ADR-R4 BRS-01; ADR-R5 MEM/NRV; ADR-R7 CSF drift; ADR-R8 Enso pytest + review;
ADR-R9 environments; ADR-R10 UX baseline; ADR-R12 consent; HELIX-repo question (`HELIX_VERSIONING_OPTIONS.md`);
the four C13 approval gates. **SGN-01 stays BLOCKED.**

## 6. Hard boundaries preserved
Single-user/local-first; privacy-first; human final authority; default-deny; **fail-closed for consequential
actions** (read-only ops use the outcome taxonomy, `19 ts`); no hidden autonomy; no bypass (R-06 OPEN); durable
lineage; replay-safe; provider/worker replaceable; explicit consent; separate runtime/engineering evidence;
independent verification; governed memory; reversibility; minimal context; TRACE repo sovereignty; separate
stage repos; no cognitive monolith. **SGN-01 BLOCKED; Hermes 0/6; ten tabs frozen.**

## 7. Reading order
`CORRECTION_REPORT` → `00`,`01`,`02` → `03`,`04`,`16`,`PRESGN_TO_EVOLUTION_RELATIONSHIP_MATRIX` →
`05`,`06`,`07` → `08`,`09`,`TRACE_SOURCE_RESOLUTION`,`10`–`15`,`HERMES_DERIVED_CAPABILITY_PLAN`,
`HELIX_VERSIONING_OPTIONS` → `17`,`18` → `technical-specifications/` → `registries/` → `validation/` → `learning/`.

## 8. Open decisions
- OD-00.1 — Accept this corrected package as the basis for the four C13 approval gates.
- OD-00.2 — Sprint 5 isolated-branch disposition (ADR-R11).

## 9. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. `-draft` preserved. Governed; superseded content marked, never deleted. No repo modified.
