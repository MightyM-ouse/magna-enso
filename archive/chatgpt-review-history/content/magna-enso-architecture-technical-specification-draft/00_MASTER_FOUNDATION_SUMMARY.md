---
document: 00_MASTER_FOUNDATION_SUMMARY
package: magna-enso-architecture-technical-specification-draft
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT — informs and proposes; decides nothing; grants no approval on Vinay's behalf
scope: Program-wide architecture + Magna Enso technical-specification foundation, pre-backlog and pre-sprint
current_vs_target: Mixed — this document separates verified-current from target/planned explicitly
date: 2026-06-21
evidence_sources:
  - magna-program-evidence-completion/ (ACCEPTED baseline, reports 00-13 + index)
  - magna-program-discovery-reconstruction/ (preliminary supporting only)
  - Preflight git inspection of magna-command-center, magna-enso, TRACE
change_control: Superseding changes require a governed decision (Event Horizon entry). Do not delete or silently rewrite. The Antigravity validation package is NOT an accepted evidence source and is not cited.
---

# 00 — Master Foundation Summary

> **Status: DRAFT_FOR_HUMAN_REVIEW.** This package prepares architecture and technical-specification
> foundations. It does **not** implement code, create a repository, modify any reviewed repository, start a
> sprint, assign sprint numbers, activate Hermes, accept BRS-01, or authorize SGN-01. Vinay remains final
> authority. Nothing here grants an approval.

## Human table of contents
1. What this package is
2. The one-paragraph truth
3. Verified-current vs target vs reuse (the three buckets)
4. Top decisions that require Vinay
5. Hard boundaries preserved
6. How to read the rest of the package
7. Open decisions
8. Change-control note

## AI navigation index
- `program_truth` → §2
- `three_buckets` → §3
- `decisions_required` → §4 (full list in `17_ARCHITECTURE_DECISIONS_REQUIRED.md`, `registries/MAGNA_OPEN_DECISIONS.yaml`)
- `boundaries` → §5
- `reading_order` → §6
- IDs and status model → `02_TERMINOLOGY_AND_DOMAIN_MODEL.md`

## 1. What this package is
A modular, evidence-based architecture and technical-specification foundation for the **Magna program**, its
**HELIX** genome, **TRACE's** dual role, the **evolutionary stages** (Enso → Satori → Kenosha → Bodhi →
Prabhava → Beyond), and the **detailed Magna Enso target**. It is the material a team would prepare *before*
writing a product backlog or planning sprints. It is a draft for human review, not an authorization.

## 2. The one-paragraph truth (evidence-grounded)
**Magna** is a single-user, local-first, governed, replay-safe cognitive orchestration runtime and the
user-facing organism with which Vinay interacts (evidence: `02_CANONICAL_MAGNA_DIRECT_READ.md`; Constitution
§1). **HELIX** is its DNA/genome — encoded architecture, doctrine, capability map, permission model and
evolutionary blueprint — that *informs and constrains* but never mutates runtime. **Cosmos** is the ratified
evolutionary chronicle (append-only with respect to history; agents propose, Vinay ratifies). **Identity** is
Magna's truthful current self-model and capability declaration — distinct from Cosmos. The strongest *verified*
runtime architecture today lives in **Magna Command Center** (ten-tab React UI, FastAPI/SQLite, durable
event/workflow/approval/orchestration, replay/observability; backend 701/701, router 65/65, frontend build
PASS). **Magna Enso** today is an **untracked, harness-level, IN_REVIEW** Sprint 5 policy-control candidate (49
unittest cases pass; standard pytest collection fails with 7 package-shadowing errors); it is **not**
runtime-integrated and **not** accepted. **Hermes** is an audited candidate capability source with **0 of 6**
capability families active. **TRACE** supplies engineering-governance artifacts plus a local telemetry
Observatory; its runtime plane is a target, not a delivered interoperability.

## 3. Verified-current vs target vs reuse (the three buckets)

| Bucket | What is in it | Authoritative source |
|---|---|---|
| **Verified-current** | Command Center runtime primitives (validated green); Enso Sprint 5 harness (unittest green, pytest broken, IN_REVIEW); TRACE template + local Observatory; Pre-SGN HAB/ATM/CSF accepted, BRS implemented+validated (not accepted) | `03`, `04`, `06`, `10` |
| **Target (planned/conceptual)** | The clean Magna Enso target architecture; TRACE runtime plane; cross-plane contract; environment topology beyond local/test; cognition/routing as a governed runtime | `06`, `07`, `13` |
| **Reuse candidate** | Command Center's integrated primitives; Enso's strict policy/fingerprint/audit components; TRACE's artifact schema/Observatory; Hermes provenance metadata only | `05`, `11` |

This document and the whole package **never present target architecture as current implementation.**

## 4. Top decisions that require Vinay (summary — full list in `17`)
1. **Canonical runtime/policy disposition** — compose Command Center primitives with Enso policy controls, or select one, *after* the required integration/bypass/restart experiment (`05`). **Do not pick the canonical policy engine now.**
2. **Stage naming + repository strategy supersession** — record new accepted Event Horizon IDs; mark one-repo/tag decisions `SUPERSEDED`, never delete (`12`).
3. **TRACE dual-plane contract** — runtime↔engineering schema, independent verifier identity, privacy classes, anti-self-certification rule (`07`, `09 spec`).
4. **BRS-01 acceptance/freeze**, and **MEM-01 / NRV-01** acceptance scope; **SGN-01 stays blocked** (`04`).
5. **Environment + release topology** beyond local/dev/test; **UX acceptance baseline** (a11y, responsive, performance); **Enso pytest correction + independent Sprint 5 review** (`08`, `10`, `13`).

## 5. Hard boundaries preserved (verbatim intent)
- Single-user, local-first, privacy-first; **human final authority**; **default-deny**; **fail-closed**; no
  hidden autonomy; no capability bypass; durable lineage; replay-safe; provider/worker replaceability;
  explicit local/cloud consent; **separate runtime and engineering evidence**; independent verification;
  governed memory; reversibility; minimal necessary context; **TRACE repository sovereignty**; **separate
  evolutionary-stage repositories**; compatibility without uncontrolled duplication; **no cognitive monolith**.
- **SGN-01 remains BLOCKED.** **No Hermes capability is active.** **All ten UI tabs remain intact.**

## 6. How to read the rest of the package
- Orientation: `00`, `01` (sources/authority), `02` (terminology, IDs, status model).
- Program & evolution: `03`, `04`, `16`.
- Current vs target architecture: `05` (current verified), `06` (Enso target), `07` (request-to-action).
- Governance/TRACE/data/agents/UX/env/security/reuse: `08`–`15`.
- Decisions + diagram manifest: `17`, `18`.
- Detailed Enso specs: `technical-specifications/`. Registries: `registries/`. Beginner layer: `learning/`.

## 7. Open decisions (this document)
- OD-00.1 — Whether this foundation package is accepted as the basis for backlog creation (gate per `13`).
- OD-00.2 — Whether the "Sprint 5 source on an isolated branch" state is acceptable while unaccepted, or
  should be quarantined pending the independent review (see `05`, `17`).

## 8. Change-control note
This is `DRAFT_FOR_HUMAN_REVIEW`. Any change of status, ID, or decision must be made through a governed
decision and recorded; superseded content is marked `SUPERSEDED`, never deleted. No reviewed Git repository
was modified to produce this package.
