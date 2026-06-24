# CANONICAL_SCOPE_AND_NON_GOALS.md
# Magna Enso — Sprint 5 Canonical Scope and Non-Goals
# Type: Local-only approval package
# Date: 2026-06-20
# Status: FOR HUMAN APPROVAL. Sprint 5 NOT started.

---

## 1. Source of truth

Every statement below traces to a repository file. No scope is invented.

| Claim | Evidence |
|---|---|
| Sprint 5 = "Policy Engine Foundation" | `planning/MAGNA_ENSO_SPRINT_PLAN.md` §[SECTION:SPRINT_5] |
| Purpose/Features/Non-Goals/Deliverables/Acceptance/Evidence/Worker/Risk | same section |
| ENSO-F-0501 = "Default-deny capability gate" | `trace/FEATURE_TRACKER.md` master row; `planning/MAGNA_ENSO_FEATURE_TRACKER_TEMPLATE.md` detail card |
| ENSO-F-0502 = "Approval-request flow + logging" | `trace/FEATURE_TRACKER.md` master row |
| Both PLANNED, Sprint 5 | `trace/FEATURE_TRACKER.md` |
| Default-deny design (7 rules, fail-closed) | Sprint 3 `DEFAULT_DENY_MODEL.md` (accepted EH-0014) |
| Approval engine concept + record fields | Sprint 3 `UNIFIED_APPROVAL_ENGINE_MODEL.md` |
| 13 policy boundaries | Sprint 3 `POLICY_CHOKEPOINT_MAP.md` |
| Policy schema fields | Sprint 3 `CAPABILITY_POLICY_SCHEMA.md` |
| 6 capability states | Sprint 3 `CAPABILITY_STATES_PROPOSAL.md` |
| No executable runtime exists yet | `vendor/hermes/RETAINED_SURFACE_STATES.yaml` (`runtime_enforcement: not_implemented`, `executable: false`), `vendor/hermes/README.md` |
| `policy/` + `tests/policy/` are the planned outputs | `trace/CELESTIAL_INDEX.json` "policy-engine" area |
| Human authority + posture gates | `trace/TRACE_CONFIG.yaml` `human_authority`, `posture` |

## 2. Canonical Sprint 5 scope (in-scope)

1. **Policy loading** — load capability-policy records (schema per Sprint 3 `CAPABILITY_POLICY_SCHEMA.md`).
   **Runtime policy records are JSON** (stdlib `json`, D-3); YAML remains reference metadata only (e.g.
   `vendor/hermes/RETAINED_SURFACE_STATES.yaml`). Using YAML for *runtime* policy would require PyYAML — a
   proposed dependency needing separate human approval + license review (R-02).
2. **Capability gating (`ENSO-F-0501`)** — a single gate through which capability calls are evaluated;
   **default-deny**: no matching policy ⇒ DENY; state-aware outcomes (disabled/read_only/draft_only/
   report_only/approval_required/active_safe).
3. **Approval-request flow (`ENSO-F-0502`)** — `approval_required` ⇒ produce an approval request and **block
   pending a decision-provider result**; Sprint 5 uses programmatically simulated test decisions, while the
   future production human-only invariant has no provider yet and therefore resolves to DENY.
4. **Decision / evidence logging** — every outcome (allow/deny/hold/approve/reject) is logged with the
   approval-record fields; audit-complete.
5. **Reversibility checks** — draft_only persistence is reversible; irreversible actions require approval.
6. **Tests** — allow / deny / approve paths, plus **negative/bypass tests** proving no path bypasses the gate
   **at the harness level** (real entry points are deferred/re-validated per-capability; R-06 stays OPEN).
7. **No auto-execution** — the engine decides; it does not itself run real-world side effects.

## 3. Feature mapping

| Feature | Canonical meaning | Acceptance (traced) |
|---|---|---|
| **ENSO-F-0501** Default-deny capability gate | Every capability call passes the gate; no policy ⇒ denied | Canonical acceptance says approve-required blocks pending human; Sprint 5 implements this only as HOLD + programmatically simulated test decision, with absent production provider ⇒ DENY. Harness-level bypass tests only. |
| **ENSO-F-0502** Approval-request flow + logging | Build the request→hold→decision-provider→log path + decision/evidence logging | Test-only provider simulates decisions; human-only is a future production invariant; no authenticated production provider exists. |

> Note (labeled assumption): the ENSO-F-0501 detail card lists "Linked Decisions: EH-0012, EH-0013", which
> are the git-init and Sprint-2-audit decisions — almost certainly a template placeholder, not governing
> Sprint 5. The governing design decision is **EH-0014** (Sprint 3 governance design accepted). Flagged as
> a minor doc inconsistency (see `RISKS_OPEN_QUESTIONS_AND_DECISIONS.md` OQ-3), not a scope conflict.

## 4. Non-goals (explicit, from the plan)

- **No remote control** (Sprint 11).
- **No scheduler** (Sprint 9).
- **No UI / Observatory** (Sprint 13).
- **No auto-execution** of capabilities.
- **No memory/skill subsystems** (Sprint 8) beyond the engine's draft-only *decision* surface.
- **No Hermes run/build/import/activation**; vendor baseline stays inert.

## 5. Forbidden actions (this sprint, when it runs)

No auto-commit/push/force-push; no modifying the HELIX/Magna repo; no importing executable Hermes source;
no installing dependencies without separate approval; no public exposure / cloud / network; no EH-0005B
promotion; no Hermes Agent activation; no Sprint 6; **no claim runtime enforcement exists** until validated.

## 6. The architecture clarification (central)

Because **no executable capability runtime exists** (vendor baseline inert), "integration into the runtime
gate path" (plan Deliverables) has **no live runtime to integrate into**. Canonical interpretation for
Sprint 5: build the engine + a **Magna-owned gate interface (the chokepoint) + a test harness** that drives
representative capability calls, and prove default-deny / approval / no-bypass against that harness. Real
capability wiring (memory Sprint 8, scheduler Sprint 9, etc.) consumes this engine later. This is **open
decision D-1** — the human owner confirms the harness-scoped interpretation before execution.
