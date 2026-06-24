# 02 — Product Lineage and Terminology

> Determined from repository evidence, not from the labels' apparent meanings.

## 1. Canonical lineage (from evidence)

```
HELIX            The Blueprint / DNA  — governance genome + cognitive architecture
  │               (lives as canon inside magna-command-center/project-knowledge/)
  ▼
MAGNA            The Living Intelligence — the user-facing cognitive orchestration
  │               environment (product + persona)
  ├── magna-command-center  = the EXISTING implementation (Trinity + Pre-SGN belt)
  └── magna-enso            = the NEW clean rebuild (first operational FORM of Magna)
                              built on a governed Hermes fork, governed by TRACE
  ▼
EVOLUTION        Enso → Satori → Kensho → Bodhi → Prabhava → Beyond
                 (releases/tags of the SAME magna-enso repo)

TRACE            The operating MODEL that governs HOW Magna is built & evidenced
                 (separate open-source repo + strategic blueprint)
Hermes           CANDIDATE technical base for the Enso runtime (audited, not active)
```

Sources: `planning/MAGNA_EVOLUTION_ROADMAP.md` §2; `MAGNA_ENSO_PROJECT_CHARTER.md` §7;
`magna-command-center/MAGNA_BLUEPRINT.md` §2.

## 2. Term-by-term (evidence, not assumption)

| Term | What it actually is | Source |
|---|---|---|
| **Magna** | Local-first, single-user, governed, replay-safe cognitive orchestration runtime + persona. Not a chatbot. | Blueprint §1 |
| **HELIX** | The *genome/blueprint*: doctrine, architecture, constraints, agent knowledge, capability map. Observes/informs; does **not** mutate runtime. Physically = `project-knowledge/` canon, not a separate repo. | Blueprint §2; charter §7 |
| **Cosmos** | The *chronicle*: ratified evolutionary record of what stabilized. Never self-updating. A UI tab also surfaces it. | Blueprint §2/§4 |
| **Identity** | (a) UI tab in the 10-tab shell; (b) CSF-01 "conscious self-model" — honest who/what/capability answers. Distinct from Cosmos (present self vs historical ledger). | Blueprint §4/§5 |
| **Presence** | "Magna Presence" — the 3D avatar / embodiment layer (Three.js). Many `layer-20-*`/`layer-21-*` branches + `docs/LAYER20/21_*` cover presence/avatar. | command-center branches & docs |
| **Cognition** | A UI tab + the "Implementation Index / Observatory" surface; Phase-E "runtime cognition observability" (read-only visualization of runtime). | Blueprint §4/§5; status doc §1 |
| **Memory** | UI tab + MEM-01 ("memory formation / recall access model"). Currently 🟡 partial (read-only recall). | Blueprint §5/§6 |
| **Nervous system** | NRV-01 layer = "runtime/system/worker visibility." 📋 planned. Also the metaphor for the event-bus/router runtime spine. | Blueprint §6 |
| **Agents** | UI tab + the modular agent roster (Orchestrator, Local Reasoning, Reviewer, Scoring, Memory, Voice, UI Workflow, Web-Search[mock]). | command-center README |
| **Router / event bus / workflow engine** | Backend runtime primitives in `backend/app/core` + `orchestrator` (event bus, workflow engine, approval engine, websocket dispatcher, command router). | Blueprint §4; `test_core_*` |
| **Magna Enso** | First operational FORM of Magna; "circle of potential"; keywords Establish·Stabilize·Govern; release `v1.0-enso`. | charter §2 |
| **Satori** | "First awakening / emergent awareness." Stage 2. Observe·Understand·Align. | roadmap §4.2 |
| **Kensho** | "Seeing true nature / clear self-observation." Stage 3. Integrate·Refine·Expand. **Spelled "Kensho," not "Kenosha."** | roadmap §4.3 |
| **Bodhi** | "Mature awakening / wisdom in action." Stage 4. Bounded autonomy. | roadmap §4.4 |
| **Prabhava** | "Source / emergence / manifestation." Stage 5. | roadmap §4.5 |
| **Beyond** | "Continuous evolution" — rolling horizon, not a fixed release. | roadmap §4.6 |
| **Hermes adoption** | `nousresearch/hermes-agent` is the *candidate* runtime base. Status: **inert provenance baseline only** (license + manifests + retained-surface metadata). Zero capabilities active. | `vendor/hermes/`, EH-0005A/0015 |
| **TRACE (methodology)** | Template · Route · Assign · Check · Evidence. Governs how AI builds the product; repo-as-source-of-truth; honest telemetry. | TRACE README; blueprint |
| **TRACE-compatible traceability inside Magna** | Two senses: (1) Enso's TRACE *engineering* instance under `trace/`; (2) a future *runtime* trace surface (the policy engine's audit log is the first instance). | TRACE_CONFIG.yaml; policy/audit.py |

## 3. The astronomy naming layer (Enso TRACE instance)

`magna-enso/trace/TRACE_CONFIG.yaml` maps plain concepts to astronomy names:

| Astronomy name | Plain meaning |
|---|---|
| Star Map | project status (`STAR_MAP.md`) |
| Celestial Index | context routing index |
| Constellation | task packet |
| Light Curve | evidence package |
| Event Horizon | decision log |
| Galaxy Catalog | role registry |
| Spectrometer | validation checklist/engine |
| Orbital Paths | workflow engine |
| Polaris | capability policy / governance layer |
| Observatory | Capability Control UI (Sprint 13) |

Note: the **open-source TRACE repo** uses *plain* role names (Planner/Builder/Validator)
and *plain* algorithm names (Template/Route/Assign/Check/Evidence). The astronomy layer
is the **Magna Enso instance's** house style, defined by the TRACE blueprint's
"Astronomy Naming Standard" (§32).

## 4. Stage entry/exit criteria & inheritance (evidence)

- **Entry/exit:** Only **Enso** has concrete acceptance gates (the Sprint 0–15 plan;
  RC at Sprint 15). Satori→Beyond have **theme + planned-feature-maturity + TRACE
  affinity only** — **no detailed entry/exit criteria yet**. *Not confirmed from
  available evidence* beyond the roadmap's one-line maturity descriptions.
- **What each stage adds:** awareness (Satori) → self-observation (Kensho) → bounded
  action (Bodhi) → creative manifestation (Prabhava) → continuous evolution (Beyond).
  Governance + human-final-authority **persist across all stages** (roadmap §7 guardrail).
- **Inheritance:** stages **inherit everything** — they are *releases of one repo*, so
  code, HELIX-derived governance artifacts, data, and governance carry forward by
  construction (folder strategy §8). No cross-stage migration is needed *because there
  is no fork* in the approved model.
- **HELIX evolution across stages:** roadmap implies the awareness/autonomy ladder and
  TRACE governance maturity "advance together; capability never outruns governance"
  (§6). How the **HELIX genome itself** is versioned across stages is **not specified**
  — *Not confirmed from available project evidence.*

## 5. Was "separate repo per stage" ever decided? 

**No — the opposite was frozen.** `EH-0003` (ACCEPTED, 2026-06-17): *"Future stages
(Satori→Beyond) are releases/tags, not copied code folders."* Folder strategy §8 gives
the rationale (continuity, TRACE Repository Sovereignty, single auditable lineage).
Your canonical statement #5 directly conflicts with this frozen decision → **C-2**.
