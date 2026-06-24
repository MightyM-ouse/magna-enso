---
document: learning/MAGNA_ENGINEERING_LEARNING_GUIDE
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Beginner-friendly explanation of every artifact, why it exists, who owns it, how it flows to sprints
current_vs_target: Educational; describes the intended process
date: 2026-06-21
evidence_sources: [package 00-18, technical-specifications, registries]
change_control: Educational. Governed; nothing deleted.
---

# Magna Engineering Learning Guide (plain language first)

## Human ToC
1. The big picture in one breath 2. What each document is (plain → professional) 3. How docs become a backlog
4. How a backlog becomes sprints 5. How code/tests link back to requirements 6. How TRACE keeps continuity
7. What Vinay checks before approving 8. Glossary 9. Change-control

## 1. The big picture in one breath
**Plain:** Before building, you write down *what* you're building, *why*, *what already exists*, and *what
could go wrong* — and a human signs off before code starts. **Professional:** architecture + technical
specification + traceability + governance gates precede backlog and sprint planning.

## 2. What each document is (plain → professional)
- **00 Master Summary** — *plain:* the one-page "where we are." *pro:* executive architecture summary.
- **01 Source/Authority** — *plain:* who/what we trust and in what order. *pro:* authority precedence + source register.
- **02 Terminology** — *plain:* shared words and labels so nobody talks past each other. *pro:* domain model + ID/status taxonomy.
- **03 Program Architecture** — *plain:* how the whole thing fits together. *pro:* program/system context architecture.
- **04 Evolution/Repository** — *plain:* the growth stages and one-repo-per-stage plan. *pro:* product-line + repo/versioning architecture.
- **05 Current Verified** — *plain:* what truly works today. *pro:* as-built architecture with validation evidence.
- **06 Target Enso** — *plain:* what we want Enso to become. *pro:* target logical architecture.
- **07 Request-to-Action** — *plain:* what happens from "you ask" to "it acts." *pro:* runtime pipeline + cognition.
- **08 Governance** — *plain:* the rules that say yes/no and who approves. *pro:* policy/authorization/approval architecture.
- **09 TRACE Dual-Plane** — *plain:* how we record both "how we built it" and "what it did," kept separate. *pro:* engineering vs runtime evidence planes.
- **10 Memory/Data/Replay** — *plain:* what it remembers and how it recovers. *pro:* persistence/evidence/replay.
- **11 Agents/Tools/Hermes** — *plain:* the models/tools, and the off-switch'd Hermes. *pro:* provider adapters + capability boundary.
- **12 UX** — *plain:* the ten screens and how you approve things. *pro:* information architecture + UX acceptance.
- **13 Environments** — *plain:* dev vs test vs the "real" local app. *pro:* environment/release topology.
- **14 Security** — *plain:* keeping it private and locked-down. *pro:* trust boundaries + controls.
- **15 Reuse/Migration** — *plain:* what we keep from old projects. *pro:* reuse classification + migration.
- **16 Stage Contracts** — *plain:* promises each future stage must keep. *pro:* evolution contracts.
- **17 Decisions Required** — *plain:* what only Vinay can decide. *pro:* ADR backlog.
- **18 Diagram Manifest** — *plain:* the list of pictures and how to colour them. *pro:* diagram conversion spec.
- **technical-specifications/** — *plain:* the detailed "how" for Enso. *pro:* component specifications.
- **registries/** — *plain:* the master lists (status, requirements, components, interfaces, decisions). *pro:* machine-readable registers.

## 3. How docs become a backlog
*Plain:* each requirement (a thing the system must do) becomes a backlog item with acceptance criteria.
*Pro:* requirements (MAG-FR/NFR/SEC/UX/TRC/OPS) → backlog candidates with Definition of Ready/Done. **Here we
stop before assigning sprints** — that needs the foundation gate (`13`) and Vinay's go-ahead.

## 4. How a backlog becomes sprints
*Plain:* you group items into short timeboxes once priorities/dependencies are clear. *Pro:* sprint planning
after backlog approval. **Not done in this package** — no sprint numbers assigned.

## 5. How code/tests link back to requirements
*Plain:* every piece of code and every test points to the requirement it satisfies, so you can prove it's
covered. *Pro:* the traceability matrix (`technical-specifications/17`) chains objective→requirement→arch
ID→spec→source module→test→evidence→acceptance.

## 6. How TRACE keeps continuity and evidence
*Plain:* TRACE writes down what was done and proves it, so work survives across people/sessions/models — and
the system can't grade its own homework. *Pro:* dual-plane traceability; an **independent verifier**
recomputes; runtime cannot self-certify (`09`).

## 7. What Vinay checks before approving (short version; full checklists are separate files)
Is current-vs-target honest? Is anything claimed implemented that isn't? Is Hermes still off (0/6)? Is SGN-01
still blocked? Are all ten tabs intact? Are runtime/engineering evidence still separate? Does any document try
to approve on your behalf (it must not)? Is every requirement evidenced or marked PROPOSED?

## 8. Glossary
Magna, HELIX, Cosmos, Identity, TRACE (two planes), Pre-SGN belt, SGN-01, BRS-01, default-deny, fail-closed,
fingerprint, audit (integrity-detecting not tamper-proof), reuse classes — see `02` and `15`.

## 9. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Educational only. Governed; nothing deleted.
