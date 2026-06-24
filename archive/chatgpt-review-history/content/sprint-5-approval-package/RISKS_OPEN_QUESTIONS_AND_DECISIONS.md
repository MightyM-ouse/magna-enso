# RISKS_OPEN_QUESTIONS_AND_DECISIONS.md
# Magna Enso — Sprint 5 Risks, Open Questions, and Decisions
# Type: Local-only approval package
# Date: 2026-06-20
# Status: FOR HUMAN APPROVAL. Sprint 5 NOT started.

---

## 1. Risks engaged by Sprint 5

| Risk | Current | Sprint 5 relationship |
|---|---|---|
| **R-06 Policy bypass (CRITICAL, OPEN)** | OPEN | Sprint 5 builds the mitigation (the gate). Must **stay OPEN** until enforcement is validated against real capabilities; a passing Sprint 5 reduces likelihood for the covered surface but does not close it. |
| R-04 Cloud/provider creep (OPEN) | OPEN | Engine must not introduce network/cloud; Non-Goal |
| R-05 Public exposure (OPEN) | OPEN | No listener/network in Sprint 5 |
| R-07 Prompt-injection persistence (OPEN) | OPEN | Default-deny rule 4: input cannot raise state |
| R-08/R-09 Memory/skill (OPEN) | OPEN | Engine provides the draft-only *decision* surface; subsystems are Sprint 8 |
| R-10 Scheduler drift (OPEN) | OPEN | No scheduler; Non-Goal |
| R-13 Overengineering (WATCH) | WATCH | Keep the engine minimal (enforcement core + harness only) |
| R-01/R-02 Hermes reuse/license (OPEN) | OPEN | No new Hermes import; no new deps without separate approval |

## 2. Sprint-5-specific risks

| ID | Risk | Mitigation |
|---|---|---|
| S5-R1 | **False sense of enforcement** — engine mistaken for live protection | Mandatory honesty statement: harness-level only, **not** runtime-protected; R-06 stays OPEN; re-validate per real capability |
| S5-R2 | Hidden bypass path at a **real** entry point | Harness cannot prove this; end-to-end chokepoint validation recurs per capability (D-5); P-01…P-13 coverage matrix labels deferred entries |
| S5-R3 | Approval flow weakened to "auto under condition" | Sprint 5 permits programmatically simulated decisions only through a test-only `HumanDecisionProvider`; human-only is a future production invariant; no authenticated production provider exists; missing/default production provider ⇒ DENY (D-7) |
| S5-R4 | Engine pulls in a dependency (license/supply-chain) | Stdlib-only (JSON, not YAML); any dependency (e.g. PyYAML) requires separate approval + license check (R-02, D-3/D-4) |
| S5-R5 | Scope creep into Sprint 6+ (identity/UI/scheduler) | Non-Goals enforced; reviewer gate |
| S5-R6 | Logging gaps / unprotected audit | Audit sink built **before** any ALLOW (D-8); gate deny-only until logging available+validated; **secure audit file** (`0600`, owner/regular/symlink checks; `FAILURE_MODES` §3d); corruption detection; **not** tamper-proof vs local admin (stated) |
| S5-R7 | **Test approve-stub leaks into production** (Antigravity Gap 1) | **Structural** isolation: `policy/` = contract + Null/Deny only; simulated provider only under `tests/policy/`; production never imports `tests/`; **no `TESTING` flag / no "uncatchable exception"**; structural test asserts no approve-provider in `policy/` (D-7) |
| S5-R8 | **Approval argument-swap / replay** (Antigravity Gap 2) | Complete **canonical invocation fingerprint** (SHA-256/canonical JSON) compared in the serialized critical section; any field mismatch/mutation/duplicate/expiry ⇒ DENY (HUMAN_AUTHORITY §4a; D-2/D-7) |
| S5-R9 | **Clock rollback / cross-restart expiry** (Antigravity Gap 4) | Monotonic expiry; pending approvals not carried across restart; rollback/uncertainty ⇒ DENY (`FAILURE_MODES` §3aa; D-2/D-8) |

## 2a. Antigravity blocking corrections — incorporated

The Sprint 5 Antigravity approval validation (verdict **ACCEPTED_WITH_CORRECTIONS**) raised three blocking
gaps and one recommended gap; all are now folded into the package design (no new decision IDs — they
strengthen existing D-2/D-7/D-8):

| Antigravity gap | Severity | Where addressed |
|---|---|---|
| Gap 1 — simulated approval leakage (T-4) | HIGH | **Structural** provider isolation (HUMAN_AUTHORITY §2b) — note: supersedes Antigravity's `TESTING`-flag/"uncatchable exception" suggestion with a sounder package-layout boundary |
| Gap 2 — weak argument binding (T-9) | HIGH | Canonical invocation fingerprint (HUMAN_AUTHORITY §4a; FAILURE_MODES §3c) |
| Gap 3 — weak audit-file permissions (T-10) | MEDIUM | Secure audit file (FAILURE_MODES §3d) |
| Gap 4 — clock expiry drift (F-11) | MEDIUM | Monotonic expiry + no cross-restart (FAILURE_MODES §3aa) |
| Gap 5 — `ENSO-F-0501` linked decisions (OQ-2) | INFO | Tracked as OQ-2; the **separate trace task** that records Sprint 5 acceptance should set linked decision to **EH-0014** |

> Note on Antigravity's wording: its reports suggested gating the test provider via `assert TESTING=True` and
> an "uncatchable initialization exception." This package **intentionally does not** adopt that — an env flag
> is not an authority boundary and Python has no uncatchable exception. Structural isolation (package layout +
> Null/Deny default + import ban) is used instead.

## 3. Open questions / decisions requiring human approval

**Status: D-1 through D-8 are all PENDING human confirmation.** Recommendations below are not decisions.

| ID | Decision needed | Options | Recommendation |
|---|---|---|---|
| **D-1** | Harness scope — what does the gate integrate into, given no runtime exists? | (a) engine + gate interface + **test harness** only; (b) wait for a real runtime | **(a)** — build enforcement core + harness now; wire real capabilities later |
| **D-2** | Approval persistence/replay model | (a) in-memory decision + append-only audit log, single-use, restart ⇒ fresh human decision; (b) persistent approval store | **(a)** for MVP (simpler, fail-closed); interacts with D-8 audit durability |
| **D-3** | **Runtime** policy record format | (a) **JSON (stdlib `json`)**; (b) YAML (needs PyYAML dependency); (c) Python data | **(a) JSON for runtime policy records.** Stdlib-only (consistent with D-4). **YAML stays reference metadata only** (e.g. `vendor/hermes/RETAINED_SURFACE_STATES.yaml`). **If** YAML is later wanted for *runtime* policy, **PyYAML becomes a proposed dependency requiring separate human approval + license check (R-02).** |
| **D-4** | Language/stack for `policy/` | (a) Python stdlib only; (b) allow a small dep | **(a)** stdlib-only (uses `json`, no YAML parser) to avoid R-02/R-04 |
| **D-5** | Does Sprint 5 acceptance change R-06 status? | (a) keep OPEN; (b) downgrade likelihood note only | **(a) keep OPEN.** A passing Sprint 5 proves **harness-level** enforcement only; **end-to-end chokepoint validation must RECUR whenever a real capability entry point is integrated** (Sprint 8+). R-06 is not closeable by Sprint 5. |
| **D-6** | Worker assignment confirmation | Codex lead / Antigravity validate / Grok edge | per sprint plan — confirm |
| **D-7** | **Human-decision boundary** | (a) `HumanDecisionProvider` interface + **test-only** provider; production provider deferred; (b) build a production human-auth provider now | **(a).** Sprint 5 defines a `HumanDecisionProvider` contract and ships a **test-only** provider that simulates approve/deny. **No production/authenticated human-approval provider exists in Sprint 5.** A missing/default provider **resolves to DENY**. Do not claim authenticated human approval exists. |
| **D-8** | **Audit durability model** | (a) append-only JSONL with atomic append + flush + corruption detection (hash-chain) + malformed-tail recovery; (b) tamper-proof/signed store | **(a).** "Append-only" = **intent + integrity detection**, **not tamper-proof**. Define atomic append, flush/durability expectations, malformed-tail recovery, corruption detection, replay validation, approval-consumption, duplicate handling. **Sprint 5 does NOT protect against a local administrator editing audit files** — a signed/tamper-evident store is a future decision. |

## 3a. Prerequisites before Sprint 5 implementation authorization

| ID | Prerequisite | Why | Owner |
|---|---|---|---|
| **PRQ-1 — CLEARED** | The stale STAR_MAP Sprint 4 branch/commit status was corrected by controlled trace commit `4d5c203cc236be84bd4b9bd8004cb88e8797a34d`. | The Star Map now records `main`, accepted Sprint 4 baseline commit `c7bb2b2`, Sprint 5 NOT STARTED, R-06 OPEN, and EH-0005B PROPOSED. | Completed 2026-06-20 |

PRQ-1 is **CLEARED**. This does not approve or start Sprint 5; D-1 through D-8 and explicit human approval remain required.

## 4. Observed repository inconsistencies

- **OQ-1 — RESOLVED:** `trace/STAR_MAP.md` was refreshed by commit
  `4d5c203cc236be84bd4b9bd8004cb88e8797a34d`. It now records live `main` and correctly labels
  `c7bb2b2` as the accepted Sprint 4 baseline commit. The new Sprint 5 implementation baseline is `4d5c203`.
- **OQ-2:** `ENSO-F-0501` detail card (in the template) lists "Linked Decisions: EH-0012, EH-0013" — these are
  git-init and Sprint-2 audit, almost certainly placeholders. The governing design decision is **EH-0014**.
  Minor; flag for cleanup, not a scope conflict.
- **OQ-3:** Sprint plan Deliverables say "integration into the **runtime gate path**", but no runtime exists
  (vendor inert). Resolved by D-1 (harness-scoped). Labeled assumption, surfaced for explicit confirmation.

## 5. Recommendation (consolidated)

**Approve Sprint 5** as the policy-engine **enforcement core** (`ENSO-F-0501` + `ENSO-F-0502`), under
**D-1(a) / D-2(a) / D-3(a JSON-runtime) / D-4(a) / D-5(a keep-OPEN+recurring) / D-6 / D-7(a test-only
provider) / D-8(a append-only-with-integrity, not tamper-proof)**, on an **isolated branch**, **no
auto-commit/push**, Codex lead + Antigravity validation (mandatory) + Grok edge-case. **PRQ-1 is CLEARED**
at `4d5c203`; D-1 through D-8 remain pending human confirmation. Conditions: keep **R-06 OPEN**
(re-validate end-to-end per real capability); keep **EH-0005B
PROPOSED**; no Hermes import/run/build; no new dependencies (PyYAML included) without separate approval;
honest "harness-level only, not runtime-protected, no authenticated human approval, not tamper-proof"
framing. Alternative: **Hold** until D-1 through D-8 are confirmed. Until you sign the decision block
(overview §8), Sprint 5 stays blocked.
