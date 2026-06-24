# 12 — TRACE Dual-Role Assessment

> TRACE has two roles (your statement #8): (a) Magna must be **built by** TRACE
> (engineering plane); (b) Magna must **contain** TRACE-compatible operational
> traceability (runtime plane). Assessed separately. These two must stay separate:
> *engineering evidence* (how the product was built) ≠ *runtime evidence* (what the
> product did at run time).

## 1. TRACE Engineering Plane — how TRACE is used to build Magna

**Maturity: HIGH (for magna-enso), via documents; partially exercised.**

| TRACE element | Present in magna-enso? | Evidence |
|---|---|---|
| Template (repo structure / Core Standard) | ✅ | `trace/` instance matches folder strategy §4 |
| Route (minimal context, no full-repo scan) | ✅ config | `TRACE_CONFIG.yaml`: `minimal_context: true`, `allow_full_repo_scan: false`; `CELESTIAL_INDEX.json` |
| Assign (role registry / Galaxy Catalog) | ✅ | `ROLE_REGISTRY.yaml`, `MAGNA_ENSO_WORKER_MODEL.md` (advisory in v1) |
| Check (preflight, validation checklist) | ✅ | `VALIDATION_CHECKLIST.md` (Spectrometer); Antigravity reviews |
| Evidence (Light Curves, review packages) | ✅ | `evidence/ENSO-0001..0005_LIGHT_CURVE.md`; per-sprint packages |
| Prepare/close-task utilities | 🟡 templates only | `TASK_PACKET_TEMPLATE.md` (Constellation), `EVIDENCE_TEMPLATE.md`; **no scripted prepare/close in enso** (command-center has code-level `prepare_task`/`close_task`, a different system) |
| Decision tracking | ✅ | `DECISION_LOG.md` (Event Horizon EH-0001…0015) |
| Risk tracking | ✅ | `RISK_REGISTER.md` (R-01…R-15; R-06 OPEN) |
| Repository continuity / handoff | ✅ | "continuity in repo, not chat" (worker model §9); STAR_MAP read-on-entry/update-on-exit |
| Model independence | ✅ | astronomy naming + AGENTS.md entry point routes any model |

**Engineering-plane gaps:**
- Prepare/close-task are **templates, not executable utilities** in Enso.
- Context-routing index (`CELESTIAL_INDEX.json`) exists but its real effect on context
  size is **unmeasured**.
- The discipline is **document-strong but execution-fragile**: the very first coded
  sprint (S5) already shows status drift (C-6) and a non-runnable test suite (C-7),
  which are exactly the failures TRACE is meant to prevent.

## 2. TRACE Runtime Plane — how Magna records its own operation

**Maturity: LOW. Magna does not yet contain working TRACE-compatible runtime
traceability.**

| Runtime trace dimension | magna-enso | magna-command-center |
|---|---|---|
| Request | 🟡 `CapabilityRequest` (uncommitted) | ✅ command/router events |
| Intent | ⬜ | 🟡 router classification |
| Context | ⬜ | 🟡 |
| Decisions | 🟡 `Decision`+audit (uncommitted) | ✅ approval/authorization |
| Routing | ⬜ | ✅ command router + diagnostics |
| Policy | 🟡 policy gate (uncommitted) | ✅ ATM-01 + risk policy engine |
| Approvals | 🟡 ApprovalCoordinator (uncommitted) | ✅ approval engine + visibility |
| Agents | ⬜ | ✅ agent protocol/profiles |
| Tools | ⬜ | 🟡 System Tool, web-search(mock) |
| Results | ⬜ | ✅ saved runs |
| Errors | ⬜ | 🟡 |
| Memory effects | ⬜ | 🟡 read-only recall |
| Replay | ⬜ | ✅ Phase-E replay/event lineage |
| Evidence integrity/retention | 🟡 hash-chained JSONL (uncommitted) | 🟡 audit logger |
| Privacy exclusions | ✅ designed (redaction S12 planned) | ✅ no `.env`, secrets policy |

**Key point:** the most TRACE-*shaped* runtime traceability that actually exists today
is in **magna-command-center** (event lineage, replay, audit logger, approval
visibility) — but that is its **own internal model**, not TRACE-the-methodology and not
wired to the TRACE dashboard. magna-enso's runtime trace surface (the policy audit log)
is **uncommitted and unverified**.

## 3. Is there credible evidence that TRACE "works"?

Your statement #9 asks whether building Magna through TRACE validates TRACE's promises
(continuity, minimal context, evidence, model independence, safe handoffs, human
governance). Evidence so far:

| TRACE promise | Evidence for | Evidence against |
|---|---|---|
| **Continuity** (repo not chat) | STAR_MAP/Light Curves let any worker resume | C-5 (README vs STAR_MAP drift) shows continuity docs can desync |
| **Minimal context** | config + index exist | effect **unmeasured**; no token metrics captured |
| **Evidence** | 4 human-approved Light Curves + review packages | none of the 4 evidence runtime behaviour; C-6 shows code shipped without matching evidence/status |
| **Model independence** | astronomy naming + AGENTS entry; many workers used | — |
| **Safe handoffs** | handoff protocol §9; same Task ID continuity | only exercised across planning sprints, not real code handoffs |
| **Human governance** | every sprint human-gated; no auto-commit/push; final-authority everywhere | **strongest, well-evidenced** result |

**Verdict:** TRACE has credibly demonstrated **human governance and evidence-discipline
at the planning level**. It has **not yet** demonstrated context efficiency (unmeasured),
runtime traceability (unbuilt), or that it prevents status drift during real
implementation (C-6/C-7 are early counter-evidence). The honest reading: **TRACE is
working as a governance ritual; it is not yet validated as a delivery/quality system,
because real delivery has barely started.**

## 4. What must stay separate

- **Engineering evidence** (Light Curves, review packages, decisions) → about *building*.
- **Runtime evidence** (policy audit log, execution capture S12) → about *operating*.
Mixing them would let "we documented it" masquerade as "it ran correctly." The audit
JSONL (runtime) and the Light Curves (engineering) are correctly separate today; keep
the policy audit sink out of the engineering evidence folder.

## 5. Measurable assessment (where possible)
- **Evidence completeness (engineering):** 4/4 accepted sprints have Light Curves = 100%
  artifact coverage; **0/4** include runtime verification.
- **Context efficiency:** **NOT MEASURABLE** from current artifacts (no token telemetry
  captured in Enso; that's the TRACE dashboard's job and it isn't wired in).
- **Handoff success:** qualitatively yes across planning; **0** real code handoffs verified.
- **Governance compliance:** **High** — no auto-commit/push observed; all sprints gated.
