---
document: 03_MAGNA_PROGRAM_ARCHITECTURE
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Program-level architecture; HELIX/Magna relationship; human-authority hierarchy
current_vs_target: Program frame is conceptual; component status markers separate current from target
date: 2026-06-21
evidence_sources: [02_CANONICAL_MAGNA_DIRECT_READ.md, 03_CURRENT_SOURCE_ARCHITECTURE_VERIFICATION.md, 04_PRESGN_STATUS_VERIFICATION.md]
change_control: Superseding changes require a governed decision. Do not delete or silently rewrite.
---

# 03 — Magna Program Architecture

## Human table of contents
1. Program intent
2. HELIX ↔ Magna relationship (constraint, not control)
3. Human authority & governance hierarchy (DIAG-02)
4. Program-level logical layers (DIAG-01)
5. Pre-SGN belt as the program readiness spine
6. What is verified-current vs target at program level
7. Open decisions
8. Change-control note

## AI navigation index
- `helix_relationship` → §2 (MAG-HLX-001, MAG-PRG-001)
- `authority_hierarchy` → §3 (DIAG-02, MAG-GOV-001)
- `program_layers` → §4 (DIAG-01)
- `presgn_spine` → §5 (MAG-GOV-001, MAG-COG-001)

## 1. Program intent
Magna is one **living cognitive orchestration environment** for a single human owner, evolving through named
stages, each governed, replay-safe, and local-first. The program's job is to let Vinay express intent and have
it routed, governed, executed (only when permitted), evidenced, and remembered — **without** hidden autonomy
or capability bypass. HELIX encodes *what Magna is allowed to be*; Magna *decides and acts within that*; Vinay
*ratifies and approves*.

## 2. HELIX ↔ Magna relationship (MAG-HLX-001 → MAG-PRG-001)
- **HELIX is read-only doctrine and observability.** It informs and constrains Magna and can *visualize*
  runtime, but **never mutates** runtime state (Constitution Law III). `Status: ACCEPTED_AND_VALIDATED` as a
  documented principle; HELIX as an executable surface beyond Command Center's documentation/observability is
  `PLANNED`/`UNKNOWN` and must not be described as a running subsystem.
- **Magna is the actor.** It decides, orchestrates, and acts within HELIX's constraints and policy.
- **Cosmos and Identity are distinct** (see `02`, `07 spec`): Identity = current truthful capability; Cosmos =
  ratified evolution.

## 3. Human authority & governance hierarchy (DIAG-02, MAG-GOV-001)

```mermaid
flowchart TD
  V["Vinay - final human authority"]
  GOV["Governance and approval engine - MAG-GOV-001 - default-deny - fail-closed"]
  HLX["HELIX doctrine and boundaries - MAG-HLX-001 - read-only"]
  POL["Policy and capability control - MAG-GOV-001"]
  RUN["Magna runtime actions - MAG-ORC-001 and MAG-TOL-001"]
  AUD["Durable audit and evidence - MAG-TRC-201 and MAG-OBS-001"]
  V -->|approves consequential actions| GOV
  HLX -->|constrains| GOV
  GOV -->|authorizes or denies| POL
  POL -->|gate single chokepoint| RUN
  RUN -->|every outcome logged| AUD
  AUD -->|independent verification| V
  RUN -. no path bypasses .-> POL
```

**Approval points (human-gated):** consequential capability execution, draft persistence, commit/push/merge,
stage promotion, Hermes activation, SGN-01 unblock. **No worker self-approves.**

## 4. Program-level logical layers (DIAG-01)

```mermaid
flowchart TB
  subgraph EXP["Experience - MAG-EXP-001"]
    UI["Ten-tab shell + Presence"]
  end
  subgraph INT["Interface and input - MAG-INT-001"]
    CMD["Command interpretation"]
  end
  subgraph COG["Cognition and routing - MAG-COG-001"]
    RT["Intent routing - bounded"]
  end
  subgraph ORC["Orchestration - MAG-ORC-001"]
    EB["Event bus"]
    WF["Workflow engine"]
    OR["Orchestration runtime"]
  end
  subgraph GOV["Governance - MAG-GOV-001"]
    PG["Policy gate + approvals"]
  end
  subgraph DATA["Memory and evidence - MAG-MEM-001 MAG-TRC-201 MAG-OBS-001"]
    DB["Persistence"]
    AU["Audit and replay"]
  end
  subgraph EXT["External and candidate - MAG-AGT-001 MAG-TOL-001"]
    PR["Provider adapters"]
    HM["Hermes - candidate - inactive"]
  end
  UI --> CMD --> RT --> PG
  PG --> EB --> WF --> OR
  OR --> PR
  PG -. governs .-> PR
  PG -. governs .-> HM
  OR --> DB
  PG --> AU
  OR --> AU
```

Status per layer is in `registries/MAGNA_COMPONENT_REGISTRY.yaml`. Verified-current layers are concentrated in
Command Center (UI, EB/WF/OR, persistence, observability, providers); the **single-chokepoint policy gate** is
the strongest in Enso's harness but is **not yet proven** as a universal runtime chokepoint (`05`).

## 5. Pre-SGN belt as the program readiness spine (MAG-GOV-001, MAG-COG-001)

| Layer | Status (evidence `04`) |
|---|---|
| HAB-01 (habitable surfaces / UI shell freeze) | `ACCEPTED_AND_VALIDATED` |
| ATM-01 (permission/risk/authorization/approval) | `ACCEPTED_AND_VALIDATED` (some boundaries remain advisory) |
| CSF-01 (conscious self-model truth registry) | `ACCEPTED_AND_VALIDATED` |
| BRS-01 (routing layer) | `IMPLEMENTED_VALIDATED` / `AWAITING_HUMAN_ACCEPTANCE` |
| MEM-01 (memory formation) | `IN_PROGRESS` / pending belt layer |
| NRV-01 (nervous-system visibility) | `IN_PROGRESS` / pending belt layer |
| SGN-01 (broad command intelligence) | **`BLOCKED`** |

Accepted readiness = **3/6 (50%)**; code+current-validation = **4/6 (66.7%)** — not interchangeable; never
combined into a single "completion %." **SGN-01 remains blocked under either metric.**

> **Corrected (C4) scope note:** the Pre-SGN Belt is a **Command Center** construct, a **different framework**
> from the Enso→Beyond evolution stages. **SGN-01 is BLOCKED within its canonical Command Center scope and is
> NOT asserted to govern any later evolution-stage repository** (`magna-satori`, `magna-kenosha`, …). See
> `PRESGN_TO_EVOLUTION_RELATIONSHIP_MATRIX.md`.

## 6. Verified-current vs target (program level)
- **Verified-current:** Command Center runtime spine; Pre-SGN HAB/ATM/CSF accepted; BRS implemented+validated.
- **Target:** target architecture within the existing magna-enso repository; HELIX/Cosmos as governed runtime surfaces beyond docs;
  cross-plane TRACE; cognition as a governed routing runtime; environment topology beyond local/test.
- **Never claim:** that the program is "one running Magna" today — it is a program with one strong verified
  runtime (Command Center), one harness-level policy candidate (Enso), and an engineering-governance toolkit
  (TRACE).

## 7. Open decisions
- OD-03.1 — Whether the target program runtime composes Command Center primitives + Enso policy, or selects one
  (after the `05` experiment) — see `17` ADR-R1.
- OD-03.2 — HELIX's target executable scope vs documentation/observability-only scope (`12` item 2).

## 8. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Program framing is conceptual; component status is authoritative per registry.
Changes are governed; superseded content marked, not deleted.
