# HERMES-TECH-001 — Claude Four-Eyes Review

**Reviewer:** Claude (independent architecture and technical-assessment reviewer)  
**Review branch:** `claude/HERMES-TECH-001-review`  
**Target branch:** `chatgpt/HERMES-TECH-001-assessment`  
**Target commit:** `36e5e46` (latest known at review time)  
**Review date:** 2026-06-30  
**Parent task:** HERMES-TECH-001, Issue #36  
**Review packet:** `trace/tasks/HERMES-TECH-001-CLAUDE-REVIEW.md`  
**Local evidence amendment:** `trace/tasks/HERMES-TECH-001-LOCAL-EVIDENCE-AMENDMENT.md`

---

## 1. SYNC Verdict

**SYNC_PASS**

| Check | Result |
|---|---|
| Working directory | `/Users/vinay/Projects/AI/Magna/magna-enso` ✓ |
| Active branch | `claude/HERMES-TECH-001-review` ✓ |
| Branch tracks | `origin/chatgpt/HERMES-TECH-001-assessment` (review target) ✓ |
| HEAD commit | `44e7d83` — "Register HERMES-TECH-001 assessment task" ✓ |
| Registry status for HERMES-TECH-001 | `PUSHED_FOR_REVIEW`, blocked on `claude_independent_review` ✓ |
| Review output paths conflict check | `trace/reviews/HERMES-TECH-001-CLAUDE-REVIEW.md`, `trace/evidence/HERMES-TECH-001-CLAUDE-HANDOFF.*` — no active task owns these paths ✓ |
| Untracked local files noted | `policy/`, `tests/policy/`, `trace/evidence/ENSO-0005_LIGHT_CURVE.md` — documented in Local Magna Workspace Findings section ✓ |

Claude is authorized to produce the review report and handoff files per `trace/tasks/HERMES-TECH-001-CLAUDE-REVIEW.md`. No activation of Hermes, no runtime code modification, no final sprint scope, no story finalization, no merge.

---

## 2. Evidence Files Reviewed

### 2.1 ACCEPTED_GITHUB_EVIDENCE

Files present on `main` or on task branches registered in `ACTIVE_WORK_REGISTRY.yaml` and fully pushed to GitHub:

| File | Source | Evidence class |
|---|---|---|
| `AGENTS.md` | main | Canonical governance |
| `CLAUDE.md` | main | Worker adapter |
| `HERMES.md` | main (GOV-005 branch) | Worker adapter |
| `trace/STAR_MAP.md` | main | Project state |
| `trace/ACTIVE_WORK_REGISTRY.yaml` | main (GOV-005 branch) | Task registry |
| `trace/CELESTIAL_INDEX.json` | main | Context routing |
| `trace/tasks/HERMES-TECH-001.md` | chatgpt/HERMES-TECH-001-assessment | Task packet |
| `trace/tasks/HERMES-TECH-001-CLAUDE-REVIEW.md` | chatgpt/HERMES-TECH-001-assessment | Review packet |
| `trace/tasks/HERMES-TECH-001-LOCAL-EVIDENCE-AMENDMENT.md` | chatgpt/HERMES-TECH-001-assessment | Amendment |
| `trace/assessments/MAGNA_VERSION_ENSO_TECHNICAL_ASSESSMENT_SEED.md` | chatgpt/HERMES-TECH-001-assessment | Seed under review |
| `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md` | chatgpt/HERMES-ADOPT-brief | Planning brief |
| `trace/planning/MAGNA_VERSION_ENSO_TECHNICAL_ASSESSMENT_SCOPE.md` | chatgpt/HERMES-ADOPT-brief | Assessment scope |
| `trace/reviews/HERMES-001-SANDBOX-READINESS.md` | hermes/HERMES-001-sandbox-readiness | Prior Hermes assessment |
| `trace/evidence/HERMES-001-HANDOFF.md` | hermes/HERMES-001-sandbox-readiness | Prior evidence |
| `trace/evidence/HERMES-001-HANDOFF.json` | hermes/HERMES-001-sandbox-readiness | Prior evidence |
| `vendor/hermes/README.md` | main (Sprint 4) | Quarantine documentation |
| `vendor/hermes/retained/RETAINED_SURFACE_STATES.yaml` | main (Sprint 4) | Capability classification |
| `vendor/hermes/provenance/UPSTREAM_PYPROJECT.toml.source.txt` | main (Sprint 4) | Hermes capability manifest |
| `vendor/hermes/provenance/UPSTREAM_PACKAGE.json.source.txt` | main (Sprint 4) | Hermes capability manifest |

### 2.2 STALE_OR_NONCANONICAL_EVIDENCE (archive, routed per CELESTIAL_INDEX)

Routed with justification: these are the pre-repository capability assessments the task packet requires recovery of. Treated as historical design reference, not canonical current-state authority. Status per `CELESTIAL_INDEX.json`: `CURRENT_NONCANONICAL_AFTER_GOV_004`.

| File | Sprint | Content |
|---|---|---|
| `archive/.../sprint-2-hermes-audit/HERMES_CODE_MAP.md` | Sprint 2 | Hermes module architecture map, risky module identification |
| `archive/.../sprint-3-capability-governance-design/HERMES_SURFACE_GOVERNANCE_MATRIX.md` | Sprint 3 | Per-surface MVP state, enforcement tier, Sprint 4 actions |
| `archive/.../sprint-3-approval-package/HERMES_SURFACE_GOVERNANCE_PLAN.md` | Sprint 3 | Proposed per-surface posture, rationale, retain/remove framing |
| `archive/.../sprint-4-governed-hermes-baseline/HERMES_SOURCE_PROVENANCE_MANIFEST.md` | Sprint 4 | Import manifest, SHA verification, imported artifact inventory |
| `archive/.../magna-program-discovery-reconstruction/07_CAPABILITY_AND_HERMES_ADOPTION_INVENTORY.md` | Reconstruction | Capability-by-capability inventory, EH-0005A/EH-0013/EH-0014/EH-0015 decision trail |
| `archive/.../magna-enso-architecture-technical-specification-corrected/HERMES_DERIVED_CAPABILITY_PLAN.md` | Arch spec | 8-capability table, four adoption layers, activation gate, open decisions |

### 2.3 LOCAL_ONLY_UNVERIFIED_UNTIL_COMMITTED

| Item | Description |
|---|---|
| `policy/` | Sprint 5 Magna-owned policy engine (9 Python modules, README) |
| `tests/policy/` | Sprint 5 policy engine tests (6 modules, helpers, simulated provider — 49 tests) |
| `trace/evidence/ENSO-0005_LIGHT_CURVE.md` | Sprint 5 implementation and validation evidence |

---

## 3. Local Magna Workspace Findings

**Local location checked:** `/Users/vinay/Projects/AI/Magna/magna-enso`  
**Git branch:** `claude/HERMES-TECH-001-review`  
**Git status summary:** 3 untracked items — `policy/`, `tests/policy/`, `trace/evidence/ENSO-0005_LIGHT_CURVE.md`; no staged changes; no uncommitted modifications to tracked files.

### 3.1 Sprint 5 Policy Engine (policy/ and tests/policy/)

**What it is:** A Magna-owned default-deny policy engine, implemented locally as Sprint 5 work. The implementation is complete and locally validated.

**Content:**
- `policy/models.py` — typed records (`Outcome`, `PolicyRecord`, `CapabilityRequest`, `Decision`)
- `policy/schema.py` — strict JSON policy loader
- `policy/canonical.py` — canonicalization, fingerprinting (SHA-256)
- `policy/evaluator.py` — pure default-deny evaluator
- `policy/provider.py` — `HumanDecisionProvider`/`NullDecisionProvider` boundary
- `policy/approval.py` — `ApprovalCoordinator` (in-memory, single-use, monotonic expiry)
- `policy/audit.py` — `SecureAuditSink` (POSIX `0600`, JSONL hash chain)
- `policy/gate.py` — `CapabilityGate.authorize` (fail-closed)
- `tests/policy/` — 49 standard-library `unittest` tests, `simulated_provider.py` (approve-capable, test-only)

**Validation results (per ENSO-0005_LIGHT_CURVE.md):**
- `python3 -m unittest discover`: PASS — 49 tests, 0 failures
- `python3 -m compileall policy tests/policy`: PASS
- No third-party imports, no Hermes runtime imports, no network surfaces

**Relationship to HERMES-TECH-001 scope:** This directly implements the "Command approval and safety controls" capability identified in the technical assessment scope. It is Magna-native (no Hermes runtime import), default-deny, fail-closed, and TRACE-compatible.

**Curate into GitHub?** YES — conditionally.  
**Recommended destination:** The Sprint 5 policy engine should be reviewed by Antigravity per its ENSO-0005_LIGHT_CURVE.md status (`IN_REVIEW`), then committed and reviewed by the Product Owner before the formal technical specification. It is directly relevant to Epic 1 planning.  
**Recommended GitHub path:** `policy/`, `tests/policy/`, `trace/evidence/ENSO-0005_LIGHT_CURVE.md` on a dedicated `sprint/05-policy-engine` branch (as recorded in the light curve). Do not bulk-copy; follow governed commit process with Antigravity validation.

**Does it change capability decisions?** YES. The seed assessment classifies "Command approval/safety controls" as `REBUILD_IN_MAGNA or WRAP_WITH_GOVERNANCE`. The Sprint 5 local work confirms that REBUILD_IN_MAGNA is the correct and already-in-progress classification. This must be updated in the seed and final technical specification.

### 3.2 ENSO-0005 Light Curve

**What it is:** Sprint 5 implementation evidence package, documenting scope, decisions, test results, risks, and open items for the policy engine.

**Key claims:**
- D-1(a) through D-8(a) approved by human owner for harness-level implementation
- Harness-only: no real runtime or capability integration
- R-06 remains OPEN (no verified real capability chokepoint)
- Antigravity validation and human acceptance remain pending
- Sprint 5 is not DONE

**Curate into GitHub?** YES — along with the policy engine, as evidence.  
**Recommended destination:** `trace/evidence/ENSO-0005_LIGHT_CURVE.md` on the Sprint 5 branch.

---

## 4. Prior Hermes Capability Assessment — What Exists

The Product Owner stated "a detailed Hermes capability assessment was already performed before the magna-enso repository was started." This review confirms that substantial assessment work does exist, across multiple sprints, but it is distributed across the archive (noncanonical) and vendor provenance. The HERMES-001 task was specifically a **sandbox readiness design** (planning-only role for Hermes), not a full operational capability assessment.

### Prior assessment trail (recovered):

**Sprint 2:** Full Hermes source architecture audit (`HERMES_CODE_MAP.md`). Identified 9 module categories, flagged risky modules. This was a read-only audit of the upstream Hermes source at SHA `33b1d144`.

**Sprint 3:** Per-surface governance design (`HERMES_SURFACE_GOVERNANCE_MATRIX.md`, `HERMES_SURFACE_GOVERNANCE_PLAN.md`). This is the most detailed prior capability assessment. It classified every Hermes surface with an MVP state, enforcement tier, and Sprint 4 action (retain/disable/remove). This is the primary prior assessment.

**Sprint 4:** Quarantined inert provenance baseline (`vendor/hermes/`). Implemented Sprint 3 governance decisions: messaging gateways removed/disabled, terminal disabled by default, memory/skills draft_only, scheduler report_only. `RETAINED_SURFACE_STATES.yaml` is the machine-readable record of what was retained and why.

**HERMES-001 Sandbox Readiness:** Planning-only role assessment for Hermes as a documentation/evidence assistant. Does NOT cover operational runtime capabilities like terminal execution, messaging gateway, or memory writes.

**Architecture draft (noncanonical):** `HERMES_DERIVED_CAPABILITY_PLAN.md` documents four adoption layers and an 8-capability table with open decisions (OD-HRM.1, OD-HRM.2, OD-HRM.3). Decision trail records EH-0005A, EH-0013, EH-0014, EH-0015.

### Critical finding:

**The seed assessment does not reference the Sprint 2/3/4 archive evidence.** The most important prior assessment — the Sprint 3 Hermes Surface Governance Matrix, which made per-surface MVP decisions (retain/disable/remove) — is present in the noncanonical archive but was not referenced or integrated by the seed. This is the primary correction required.

---

## 5. Findings Table

| # | Finding | Severity | Correction required |
|---|---|---|---|
| F-01 | Seed does not reference prior Sprint 2/3/4 archive assessments | HIGH | Add evidence recovery section citing archive Sprint 2–4 Hermes assessment documents |
| F-02 | Messaging gateways: seed says WRAP_WITH_GOVERNANCE; Sprint 3 governance design says DISABLED/REMOVE for MVP | HIGH | Correct to: messaging gateway is currently DISABLED per Sprint 3 design; re-enabling requires new activation decision; Telegram WRAP_WITH_GOVERNANCE applies only after explicit re-authorization |
| F-03 | Memory: seed says ADAPT; Sprint 3 governance says `draft_only` (staged, never auto-activates) | MEDIUM | Correct to WRAP_WITH_GOVERNANCE with `draft_only` staging requirement |
| F-04 | Command approval/safety controls: seed says "REBUILD_IN_MAGNA or WRAP_WITH_GOVERNANCE" | MEDIUM | Correct to REBUILD_IN_MAGNA; Sprint 5 local candidate implementation exists |
| F-05 | No formal product user stories exist in the repository (`trace/product/` does not exist) | HIGH | Seed must note this prerequisite gap; Epic 1 scope cannot be confirmed until stories exist and are reviewed |
| F-06 | Sprint 5 policy engine is local-only and not referenced in seed assessment | MEDIUM | Seed's "Command approval/safety controls" must reference Sprint 5 local candidate |
| F-07 | HERMES-ADOPT-001 (PR #34) is not yet merged; seed's feed-forward is premature | MEDIUM | Seed must clarify that planning brief is PUSHED_FOR_REVIEW, not accepted |
| F-08 | GOV-005 and GOV-006 are not yet merged to main | MEDIUM | Seed should note these governance dependencies for Epic 1 technical specification |
| F-09 | PR #33 (Magna identity/logo) status not confirmed in seed | LOW | Seed references PR #33 correctly as dependency; status should be checked before final spec |
| F-10 | Seed's ADOPT_IN_MAGNA classification for PR #33 uses a non-standard decision class | LOW | Use ADOPT for the identity direction; note PR #33 as a prerequisite, not a capability decision |
| F-11 | Open decision OD-HRM.3 (authenticated approval channel) is not addressed by seed | LOW | Seed should note this is unresolved for Epic 1 approval loop |
| F-12 | R-06 (runtime policy chokepoint not verified) remains OPEN and is not noted in seed | MEDIUM | Seed must carry R-06 as an open risk for Epic 1 |

---

## 6. Capability Classification Corrections

| Capability | Seed Decision | Archive Evidence | Corrected Decision | Notes |
|---|---|---|---|---|
| Terminal execution | WRAP_WITH_GOVERNANCE | Sprint 3: `approval_required`, disabled by default (T4 gate). Sprint 4: confirmed inert, `approval_required_disabled`. | WRAP_WITH_GOVERNANCE (confirm) | Correct in direction. Must add: disabled by default; separate activation gate required; policy engine must be verified before activation. |
| Messaging gateway | WRAP_WITH_GOVERNANCE | Sprint 3: `disabled / REMOVE` (T1 — highest disablement tier). Messaging gateways and outbound delivery explicitly removed for MVP. | WRAP_WITH_GOVERNANCE — requires new explicit activation decision | Currently DISABLED per Sprint 3 MVP design. Not WRAP_WITH_GOVERNANCE yet; re-authorization needed. |
| Telegram support | WRAP_WITH_GOVERNANCE | Telegram is part of the `messaging` optional extra in Hermes (`python-telegram-bot`). Not imported in vendor baseline. | WRAP_WITH_GOVERNANCE — requires explicit activation decision and policy gate | Epic 1 candidate channel, but must re-authorize messaging gateway surface. |
| WhatsApp support | DEFER | Sprint 3: messaging gateways disabled; Sprint 2: flagged high risk. | DEFER (confirm) | Correct. One approved channel is sufficient for Epic 1. |
| Memory | ADAPT | Sprint 3: `draft_only`. Writes staged; no auto-activation. External memory sync: `disabled/REMOVE`. | WRAP_WITH_GOVERNANCE (`draft_only` staging mode) | ADAPT understates the constraint. Memory writes must be staged and non-bypassable; no silent mutation. |
| Skills/self-improvement | DEFER | Sprint 3: `draft_only` (skill writes); background review `disabled/REMOVE`; curator `report_only`. | DEFER (confirm) | Correct. Background self-improvement must remain disabled. Skills can be `report_only` at most. |
| Profiles | ADAPT | HERMES-001 noted: profiles are NOT a security sandbox. | ADAPT (confirm) | Correct, but must explicitly document: Hermes profiles are not security sandboxes; Magna governance is the authority boundary. |
| Scheduler/cron | DEFER | Sprint 3: `report_only` (proposals only, never auto-executes). Direct script cron: `REMOVE`. Sprint 4: scheduler_metadata is `report_only`. | DEFER for auto-execution; REPORT_ONLY if surfaced at all | Correct to DEFER auto-execution. If any scheduler surface is used, it must propose only, never execute unattended. |
| Delegation/subagents | DEFER | Sprint 3: `disabled` in MVP; delegation recursion control designed. Sprint 4: `subagent_delegation` excluded. | DEFER (confirm) | Correct. Delegation disabled/excluded in Sprint 3/4 MVP. |
| MCP/tool integrations | DEFER | Sprint 3: `disabled unless signed allowlist`. Sprint 4: `plugin_mcp_dynamic_loading` excluded. | DEFER (confirm) | Correct. Dynamic MCP loading must remain disabled until signed allowlist policy exists. |
| Command approval/safety controls | REBUILD_IN_MAGNA or WRAP_WITH_GOVERNANCE | Sprint 3: policy gate (P-03/P-04) designed. Sprint 5 (local): Magna-native policy engine implemented. | REBUILD_IN_MAGNA | Correct direction, ambiguity removed. Sprint 5 local candidate is the implementation path. |
| Execution capture/logging | ADAPT | Sprint 3: TRACE evidence required for every action. | ADAPT (confirm) | Correct. Normalize into TRACE format; JSONL audit chain is Sprint 5 candidate. |
| CLI worker dispatch | WRAP_WITH_GOVERNANCE | Sprint 2: `agent/tool_executor.py` is policy insertion point. Sprint 3: tool registry governed. | WRAP_WITH_GOVERNANCE (confirm) | Correct. Worker selection must go through known-instruction registry and approved wrappers. |
| GitHub evidence/update flow | REBUILD_IN_MAGNA | Hermes has no GitHub evidence update mechanism; TRACE is Magna authority. | REBUILD_IN_MAGNA (confirm) | Correct. GitHub is Magna authority; TRACE lifecycle is Magna-owned. |
| Notification and approval loop | ADAPT | Hermes messaging surfaces are disabled; notification must re-authorize channel. | ADAPT (confirm, but depends on messaging re-authorization) | Correct direction. Notification delivery depends on Telegram re-authorization. Approval semantics are Magna-owned. |
| Command Center UI integration | REBUILD_IN_MAGNA | Magna Command Center is a separate repository; no Hermes UI is appropriate. | REBUILD_IN_MAGNA (confirm) | Correct. |
| PR #33 identity/logo dependency | ADOPT_IN_MAGNA | PR #33 introduces animated Magna identity; not a Hermes capability decision. | ADOPT (prerequisite dependency) | Classification type should be ADOPT; this is a product dependency, not a Hermes capability decision. |

---

## 7. Features That Must Be Adopted for Epic 1

In priority order for the Epic 1 governed remote task loop:

| Feature | Classification | Dependency |
|---|---|---|
| Magna identity wrapper around all runtime messages | ADOPT (via PR #33 direction) | PR #33 acceptance |
| Remote command intake — Telegram only | WRAP_WITH_GOVERNANCE | Messaging gateway re-authorization decision; Telegram activation gate |
| Known-instruction matching (instruction registry) | REBUILD_IN_MAGNA | None (pure Magna) |
| Safety classification / policy engine | REBUILD_IN_MAGNA | Sprint 5 policy engine review + acceptance |
| CLI worker dispatch (approved wrappers) | WRAP_WITH_GOVERNANCE | Known-instruction registry |
| Worker result capture and normalization | ADAPT | TRACE task envelope |
| GitHub evidence/assessment update | REBUILD_IN_MAGNA | TRACE task lifecycle |
| User notification via approved channel | ADAPT (depends on Telegram activation) | Messaging gateway re-authorization |
| TRACE forward/backward traceability enforcement | REBUILD_IN_MAGNA | None (Magna-native) |
| Approval/continuation/closure loop | ADAPT | Notification channel + GitHub update |

---

## 8. Features That Can Be Deferred

| Feature | Classification | Rationale |
|---|---|---|
| WhatsApp support | DEFER | One approved channel is sufficient for Epic 1. |
| Scheduler/cron (auto-execution) | DEFER | Unattended execution adds risk beyond Epic 1 scope. Report-only mode acceptable if needed. |
| Skills/self-improvement (background review, curator) | DEFER | Disabled/removed in Sprint 3/4 MVP. Too risky for first loop. |
| Full memory write automation | DEFER | Draft-only staging acceptable; auto-write unsafe. |
| Multi-level delegation / subagents | DEFER | Excluded in Sprint 3/4 MVP. Delegation recursion control designed but not implemented. |
| MCP/tool integrations (dynamic loading) | DEFER | Dynamic loading disabled pending signed allowlist policy. |
| Browser actions | DEFER | Approval-required in Sprint 3; not needed for first loop. |
| Remote execution backends (Modal, Daytona, SSH) | DEFER | Removed in Sprint 3/4. |
| Multi-channel notification fanout | DEFER | One channel sufficient. |
| Cloud provider activation | DEFER | Disabled at module level in Sprint 3/4. |

---

## 9. Risks and Unresolved Decisions

| ID | Risk / Decision | Status | Impact |
|---|---|---|---|
| R-01 | GOV-005 not yet merged to main | OPEN — READY_FOR_PRODUCT_OWNER | Epic 1 technical specification depends on final governance framework being accepted |
| R-02 | GOV-006 not yet merged to main | OPEN — PUSHED_FOR_REVIEW | Agent routing contract not finalized |
| R-03 | HERMES-ADOPT-001 (PR #34) not yet merged | OPEN — PUSHED_FOR_REVIEW | Planning brief not formally accepted; HERMES-TECH-001 is downstream |
| R-04 | No formal product user stories exist (`trace/product/` absent) | OPEN — critical gap | Epic 1 scope cannot be confirmed; story correctness review cannot proceed |
| R-05 | Messaging gateway surfaces are currently DISABLED per Sprint 3/4 MVP design | OPEN — new decision required | Re-enabling Telegram requires explicit Product Owner decision and activation gate |
| R-06 | R-06: runtime policy chokepoint not verified (carried forward from Sprint 4/5) | OPEN — recurring | No verified path from policy engine to real capability enforcement |
| R-07 | Sprint 5 policy engine is local-only, unreviewed by Antigravity | OPEN — pending validation | Can inform Epic 1 design but must not be assumed accepted |
| R-08 | Local model/provider for Hermes runtime not selected | OPEN — OD-HRM.1 | Required for any operational Hermes capability |
| R-09 | SGN-01 remains blocked | OPEN | Dependency of future Hermes integration planning |
| R-10 | ARCH-001 (architecture baseline) remains blocked and requires resynchronization | OPEN | Technical specification must not assume architecture decisions |
| R-11 | PR #33 (Magna identity) status not confirmed from local evidence | OPEN — external | Epic 1 identity dependency; should be confirmed before final spec |
| R-12 | OD-HRM.3: authenticated approval channel for capability activation not designed | OPEN | Required before any approval-required capability is activated |

---

## 10. Recommended Curated GitHub Destinations for Local-Only Evidence

| Local path | Recommended destination | Rationale | Condition |
|---|---|---|---|
| `policy/` | `policy/` on a dedicated `sprint/05-policy-engine` branch | Sprint 5 approved scope; Magna-native policy engine candidate for Epic 1 | Antigravity validation and human acceptance required first |
| `tests/policy/` | `tests/policy/` on same Sprint 5 branch | Required test evidence for policy engine | Same as above |
| `trace/evidence/ENSO-0005_LIGHT_CURVE.md` | `trace/evidence/ENSO-0005_LIGHT_CURVE.md` on Sprint 5 branch | Sprint 5 implementation evidence; documents scope, decisions, test results, and open risks | Same as above |

Do not bulk-copy. Follow the governed commit process. Antigravity validation must precede Product Owner acceptance. Sprint 5 evidence must not be represented as accepted main state until merged.

---

## 11. Recommended Edits to the Seed Assessment

1. **Add evidence recovery section:** The seed says prior evidence must be recovered but does not itself document what was found. Add a section explicitly listing the Sprint 2/3/4 archive assessments as recovered evidence and summarizing the key decisions: Sprint 3 Governance Matrix, EH-0013, EH-0014, EH-0015.

2. **Correct messaging gateway classification:** Change "WRAP_WITH_GOVERNANCE" to "WRAP_WITH_GOVERNANCE — requires new activation decision (currently DISABLED per Sprint 3/4 MVP)". This is a material distinction.

3. **Correct memory classification:** Change ADAPT to WRAP_WITH_GOVERNANCE (`draft_only` staging required; writes never auto-activate).

4. **Clarify command approval/safety controls:** Change "REBUILD_IN_MAGNA or WRAP_WITH_GOVERNANCE" to "REBUILD_IN_MAGNA". Note that Sprint 5 local candidate implementation exists and is pending acceptance.

5. **Add missing prerequisites:** The seed implies sprint planning follows after user story review. Add explicit prerequisite checklist:
   - GOV-005 and GOV-006 merged to main
   - HERMES-ADOPT-001 (PR #34) reviewed and accepted by Product Owner
   - Formal product user stories created and reviewed
   - Sprint 5 policy engine reviewed and accepted
   - Messaging gateway re-authorization decision made
   - R-06 addressed (verified policy-to-capability chokepoint)

6. **Note that trace/product/ does not exist:** The seed references reconciling product user stories. These do not yet exist.

7. **Fix PR #33 classification type:** Change ADOPT_IN_MAGNA to ADOPT. Note explicitly that this is a branding prerequisite dependency, not a Hermes capability decision.

8. **Add R-06 to risk register:** The Sprint 4/5 open risk (runtime chokepoint not verified) must be carried forward explicitly in the assessment.

---

## 12. Final Verdict

**ACCEPT_WITH_CORRECTIONS**

The seed assessment is directionally correct. The architecture premise, Epic 1 loop definition, safety boundaries, and next-workflow description are sound. The capability classification directions are largely correct.

However, the assessment requires the corrections described in section 11 before it can serve as the basis for final approved/design-ready user stories and sprint planning. The most significant corrections are:

- Reference and integrate the Sprint 2/3/4 prior capability assessment evidence from the archive.
- Correct the messaging gateway classification to reflect that it is currently DISABLED/REMOVED per Sprint 3/4 MVP and requires a new activation decision.
- Correct memory from ADAPT to WRAP_WITH_GOVERNANCE.
- Clarify command approval/safety controls as REBUILD_IN_MAGNA.
- Acknowledge that no formal product user stories exist yet and enumerate the prerequisites that must be resolved before sprint planning.

These are corrections to precision and completeness, not to fundamental product direction. The Product Owner's architecture premise (Magna = product identity and authority, Hermes = candidate runtime provider) is well-founded and preserved.

---

## 13. Traceability

| Direction | Links |
|---|---|
| Backward | HERMES-TECH-001 task packet; Issue #36; PR #37 (target branch); HERMES-ADOPT-001 planning brief; Sprint 2/3/4 archive assessments; vendor/hermes baseline |
| Forward | Product Owner review of this correction report; formal product user story creation; reconciliation of stories with corrected assessment; final approved/design-ready stories; four-sprint planning |

**Handoff:** `trace/evidence/HERMES-TECH-001-CLAUDE-HANDOFF.md`, `trace/evidence/HERMES-TECH-001-CLAUDE-HANDOFF.json`
