---
document: CORRECTION_REPORT
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT — records corrections; decides nothing; grants no approval
scope: What changed from the -draft package and why, per the 13 corrections
date: 2026-06-21
supersedes: none (the -draft package is preserved unchanged)
evidence_sources:
  - magna-program-evidence-completion/ (accepted baseline)
  - <MAGNA_LOCAL_ROOT>/planning/ (roadmap, charter, sprint plan, repo strategy, TRACE adoption, worker model)
  - <MAGNA_LOCAL_ROOT>/trace/TRACE_STRATEGIC_BLUEPRINT_v1.0.md
  - <LOCAL_USER_HOME>/Projects/AI/TRACE (implementation repo)
change_control: Governed. The original -draft package is preserved, not overwritten.
---

# Correction Report — draft → corrected

> This corrected package **adds to and amends** the `-draft` package; the original is preserved at
> `magna-enso-architecture-technical-specification-draft/`. No reviewed Git repository was modified.

## Human table of contents
1. Two material conflicts (resolved by Vinay's decisions, via supersession)
2. Correction-by-correction summary (C1–C13)
3. What was preserved
4. Open decisions still reserved for Vinay
5. Change-control note

## 1. Two material conflicts found in canonical sources (now resolved by supersession)
Both conflicts are between the **historical canonical planning docs** and the **current human-owner decisions
in the correction prompt**. Authority precedence puts current human decisions first, so each historical
decision is marked `SUPERSEDED` (never deleted), per the program's supersession discipline.

| # | Historical canonical source says | Current human decision says | Resolution |
|---|---|---|---|
| Conf-1 | **One repo + tags**: "One product line = one repo… Satori…Beyond are future releases… not new repositories" (`MAGNA_ENSO_FOLDER_AND_REPO_STRATEGY.md` §3/§8; roadmap §5; charter Frozen Decisions) | **Separate repository per stage** (decision 4: `magna-enso`, `magna-satori`, `magna-kenosha`, `magna-bodhi`, `magna-prabhava`, future Beyond) | Separate-repos adopted; one-repo decision marked `decision_status: SUPERSEDED`, retained as historical evidence. Needs a governed Event Horizon ID (ADR-R2). |
| Conf-2 | **"Kensho"** (roadmap/charter/repo-strategy spelling) | **"KENOSHA"** official third-stage spelling (decision 5) | KENOSHA used as official; "Kensho — Seeing True Nature" preserved as the conceptual meaning + historical spelling, marked `SUPERSEDED` pending the same governed entry. |

Neither conflict is a *reserved* architectural decision (Vinay decided both in the prompt), and stage
*meanings* do not conflict — so the corrected package proceeds without stopping, recording both honestly.

## 2. Correction-by-correction summary

- **C1 — Existing Enso repository.** Removed every implication of creating a *new clean Enso repo*.
  `magna-enso` (branch `sprint/05-policy-engine`, HEAD `4d5c203`) **is** the Enso stage repository and the
  forward project; the architecture package is to be *integrated into it* after approval. Command Center is a
  reuse donor. Repository-creation gates now apply only to **future-stage** repos. Updated: `00`, `04`, `06`,
  `13`, `15`, `16`, `17`, registries, `FOUNDATION_EVIDENCE_INDEX.json`.
- **C2 — TRACE source & dual role.** Resolved three TRACE locations to distinct roles; see
  `TRACE_SOURCE_RESOLUTION.md` (with hashes/commits/authority). Corrected `09` and spec `09`. TRACE
  effectiveness still **not** claimed; blueprint-only capabilities marked planned; planes kept separate.
- **C3 — Evolution roadmap.** Reconstructed Enso→Beyond from the **approved roadmap/charter**, with two
  columns (evidence-confirmed meaning vs proposed technical interpretation). No stage silently redefined;
  undocumented capability allocation marked `DECISION_REQUIRED`. Updated `04`, `16`.
- **C4 — Pre-SGN vs evolution.** Added `PRESGN_TO_EVOLUTION_RELATIONSHIP_MATRIX.md` treating them as
  distinct frameworks unless evidence maps them; SGN-01 is **not** claimed to govern later stage repos.
- **C5 — Status model.** Replaced the single overloaded status with five dimensions (implementation /
  acceptance / decision / evidence / reuse). All registries updated; no undeclared enum values.
- **C6 — Architecture IDs.** Every component/diagram node uses a full ID (`MAG-XXX-0NN`). `MAG-UX-*` is now
  **requirement-only**; UX architecture components use `MAG-EXP-*`. Validated in `validation/`.
- **C7 — Full traceability.** Expanded the matrix to **all 52 requirements** (`technical-specifications/17`)
  and added a machine-readable `registries/MAGNA_TRACEABILITY_REGISTRY.yaml`.
- **C8 — Spec depth.** Added `technical-specifications/18_STATE_MACHINE_SPECIFICATIONS.md` (7 required state
  machines) and deepened contracts; ADR-R1 details remain explicitly unresolved/PROPOSED.
- **C9 — Failure & outcome taxonomy.** Added `technical-specifications/19_FAILURE_AND_OUTCOME_TAXONOMY.md`
  with 10 outcomes; consequential actions fail closed, but read-only/non-consequential operations return their
  own outcome (not misrepresented as `DENY_POLICY`). Updated `08`, `13`, spec `06`.
- **C10 — Audit before effect.** Made the 10-step order explicit with intermediate states
  (`AUTHORIZED_PENDING_AUDIT` → `AUDIT_CONFIRMED` → `EXECUTION_*`); an ALLOW alone never triggers an effect.
  In `07`, `08`, and `18`.
- **C11 — Hermes-derived scope.** Added `HERMES_DERIVED_CAPABILITY_PLAN.md` separating source adoption /
  capability adoption / Magna-owned reimplementation / activation; capability table from the sprint plan +
  audit. **Activation remains 0/6.**
- **C12 — HELIX versioning.** Added `HELIX_VERSIONING_OPTIONS.md` (options + trade-offs; no repo decision made).
- **C13 — Foundation/sprint boundary.** Replaced "new Enso repo creation gate" with four separate approvals
  (foundation-baseline / package-integration / backlog-prep / sprint-planning). Updated `13`, `17`.

## 3. What was preserved (per instruction)
Modular structure; 22 architecture views; current/target/reuse separation; ten-tab shell freeze; TRACE
dual-plane distinction; human-authority boundaries; **no policy-engine selection**; **no Hermes activation**;
learning guides; YAML registries; requirement IDs; diagram manifest; change-control/supersession rules.

## 4. Open decisions still reserved for Vinay
ADR-R1 (engine — not chosen), ADR-R2 (repo-strategy + KENOSHA supersession Event Horizon ID), ADR-R3 (TRACE
contract), ADR-R4 (BRS-01), ADR-R5 (MEM/NRV), ADR-R7 (CSF drift), ADR-R8 (Enso pytest + review), ADR-R9
(environments), ADR-R10 (UX baseline), ADR-R12 (consent), plus C12 HELIX-repo question and the four C13
approval gates. SGN-01 stays BLOCKED.

## 5. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. The `-draft` package is preserved. Supersessions are recorded, not deletions.
