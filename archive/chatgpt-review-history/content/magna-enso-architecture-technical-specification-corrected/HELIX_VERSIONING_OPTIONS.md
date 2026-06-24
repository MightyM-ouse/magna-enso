---
document: HELIX_VERSIONING_OPTIONS
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT — presents options; decides nothing
scope: Proposed models for preserving HELIX doctrine across separate stage repositories
date: 2026-06-21
evidence_sources:
  - 02_CANONICAL_MAGNA_DIRECT_READ.md (HELIX read-only doctrine; Cosmos; Identity)
  - planning/MAGNA_EVOLUTION_ROADMAP.md (HELIX→Magna→Evolution)
change_control: No HELIX-repo decision made. Governed; nothing deleted. Resolves Correction 12.
---

# HELIX Versioning and Stage Inheritance — Options (Correction 12)

> Human decision 4 makes each stage a **separate repository**. That raises a question the `-draft` package did
> not address: **how is HELIX doctrine preserved across separate repos without copying uncontrolled or stale
> doctrine?** This document presents **options and trade-offs only**. It does **not** decide whether HELIX
> becomes its own repository — that is reserved for Vinay.

## Human table of contents
1. What HELIX is (and is not)
2. The problem: doctrine across separate repos
3. Required elements (all options must provide these)
4. Option A / B / C with trade-offs
5. Version-pinning, compatibility, supersession, migration
6. Proof, Cosmos, Identity
7. Open decisions
8. Change-control note

## 1. What HELIX is (and is not)
HELIX = Magna's encoded genome/doctrine/architecture/constraints + **read-only** observability; it **informs
and constrains, never mutates runtime** (`02`; Constitution Law III). The roadmap frames it as "HELIX (the
Blueprint/DNA) → Magna (the Living Intelligence) → Evolution." HELIX as an executable runtime surface beyond
docs/observability is `PLANNED/UNKNOWN` and not asserted here.

## 2. The problem
If each stage repo embeds its own copy of HELIX doctrine, copies drift and go stale — violating "compatibility
without uncontrolled duplication" and "no cognitive monolith." Some controlled inheritance mechanism is needed.

## 3. Required elements (every option must provide)
- **Canonical HELIX source** — one authoritative doctrine origin.
- **Immutable constitutional invariants** — the non-negotiables (human authority, default-deny, fail-closed,
  no hidden autonomy, no bypass, separate evidence) that **no stage may weaken**.
- **Stage-specific HELIX profile** — the subset/parameters a stage actually implements.
- **Version pinning** — each stage records exactly which HELIX version it implements.
- **Compatibility contract** — how a stage declares compatibility without copying the whole doctrine.
- **Supersession & migration** — how doctrine changes propagate without deleting history.

## 4. Options

### Option A — HELIX as its own sovereign repository (versioned doctrine)
- **Model:** `magna-helix` repo holds canonical doctrine; stages depend on a pinned HELIX version (tag/commit)
  via a contract file, not a source copy.
- **Pros:** single source of truth; clean version pinning; no drift; mirrors TRACE repository sovereignty.
- **Cons:** adds a repo + release process; requires a dependency/pinning mechanism; **repo-creation is a
  reserved decision** (not made here).

### Option B — HELIX profile files inside each stage repo, generated from a canonical source
- **Model:** canonical doctrine lives in one place; each stage repo carries a **generated, hash-pinned**
  `helix-profile.yaml` (invariants + implemented subset + source hash), never hand-edited.
- **Pros:** no new top-level repo required; explicit per-stage pin; drift detectable by hash mismatch.
- **Cons:** needs a generation/verification step; canonical source location still must be chosen.

### Option C — Shared contract package (versioned) consumed by stages
- **Model:** a versioned **contracts** artifact (the invariants + interface contracts) is published and
  consumed by each stage (like `MAGNA_INTERFACE_REGISTRY` made into a release).
- **Pros:** aligns with the existing "contracts not code-duplication" principle; language-neutral.
- **Cons:** packaging/distribution mechanism required; governance of the contract release needed.

| Criterion | A (own repo) | B (generated profile) | C (contract package) |
|---|---|---|---|
| Single source of truth | strong | strong | strong |
| Drift control | strong | medium-strong (hash) | strong |
| New infrastructure | repo+release | generator | packaging |
| Reversible/low-regret to start | medium | high | medium |
| Touches reserved repo decision | **yes** | no | no |

## 5. Version-pinning, compatibility, supersession, migration (common design, PROPOSED)
- **Pin:** each stage stores `helix_version` + `helix_source_hash` (e.g. in `trace/` or a `helix-profile`).
- **Compatibility contract:** stage declares `implements: invariants>=vX; profile=stageY`; CI/Spectrometer
  check fails if an invariant is missing or weakened.
- **Supersession:** doctrine changes get a new HELIX version + Event Horizon entry; prior version marked
  `SUPERSEDED`, never deleted; stages migrate by re-pinning.
- **Migration:** a stage upgrades HELIX version deliberately, records the change (Cosmos ratification), and
  re-runs invariant checks before acceptance.

## 6. Proof, Cosmos, Identity
- **A stage proves which HELIX version it implements** via the pinned `helix_version` + `helix_source_hash`,
  verified independently (not self-certified).
- **Cosmos** records *ratified* evolution: each HELIX version adoption is a ratified chronicle entry (Vinay
  ratifies; agents propose) — append-only w.r.t. history.
- **Identity** reports *current capability truth* per stage (what it can do now under its pinned HELIX), kept
  distinct from Cosmos (history).

## 7. Open decisions
- OD-HLX.1 — **Reserved for Vinay:** does HELIX become its own repository (Option A) or stay as profile/
  contract (B/C)? Not decided here.
- OD-HLX.2 — Canonical HELIX source location + immutable-invariant list ratification.
- OD-HLX.3 — Generation/verification mechanism for pins (if B/C).

## 8. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Options only; HELIX-repo decision reserved for Vinay. Governed; nothing deleted.
