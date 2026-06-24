# THREAT_MODEL_AND_BYPASS_ANALYSIS.md
# Magna Enso — Sprint 5 Threat Model and Bypass Analysis
# Type: Local-only approval package
# Date: 2026-06-20
# Status: FOR HUMAN APPROVAL. Sprint 5 NOT started.

---

## 1. Purpose

Enumerate how the policy gate could be bypassed or escalated, so Sprint 5 is designed and tested to resist it.
This is the heart of **R-06 (policy bypass, CRITICAL, OPEN)**. Grounded in Sprint 3 `POLICY_CHOKEPOINT_MAP.md`
(13 boundaries) and the Sprint 2 finding that Hermes reaches capabilities by *many* paths.

## 2. Assets to protect

The decision integrity of the gate: that **no capability executes a side effect except via an ALLOW/approved
decision**, and that **deny/hold cannot be turned into allow** by anything other than the human owner.

## 3. Bypass / escalation classes

| ID | Threat | Vector | Required mitigation (Sprint 5) | Check type & Sprint 5 check |
|---|---|---|---|---|
| T-1 | **Uncovered path** | A capability reachable by a path not routed through the gate | Single chokepoint; every call routes through the gate; `paths_covered` must list all paths or DENY | **Harness-testable + DEFERRED**: harness test calls "around" the gate ⇒ denied; **real entry-point validation is deferred** (per-capability, later sprints; R-06 OPEN) |
| T-2 | **Missing-policy allow** | No policy record treated as "allow" | Default-deny rule 1/7: no record ⇒ DENY | **Executable deny-test**: unknown capability ⇒ deny |
| T-3 | **Input-driven escalation** | Request payload / fetched content raises state | Rule 4: external content cannot alter policy/state; evaluator ignores request-supplied "allow" | **Executable deny-test**: malicious payload claiming privilege ⇒ deny |
| T-4 | **Self-approval / test-stub leakage** | A worker/agent approves its own request, or the test approve-stub loads outside tests | **Structural isolation** (HUMAN_AUTHORITY §2b): `policy/` holds only the contract + a fail-closed Null/Deny provider; the simulated provider lives **only** under `tests/policy/`; **production never imports `tests/`**; **no `TESTING` flag and no "uncatchable exception"**; missing/unrecognized provider ⇒ DENY. | **Executable + structural**: test-provider decisions simulated under tests; **structural test asserts no approve-provider exists in `policy/`** and `tests/` is not imported by production; production resolves to Null/Deny ⇒ DENY. |
| T-5 | **Config bypass** | A flag flips a dangerous capability on | Dangerous surfaces disabled at strong tiers / not present; config cannot set approval_required→auto | **Executable deny-test**: config flip ⇒ still gated/denied |
| T-6 | **Plugin/MCP self-registration** | Dynamic code registers an active capability | Loader excluded (Sprint 4 non-import); no dynamic registration path in engine | **Absence assertion**: assert no dynamic loader / registration path exists (not a deny-test) |
| T-7 | **Fail-open on error** | Engine error → action proceeds | Fail-closed: any error/uncertainty ⇒ DENY | **Executable deny-test**: evaluator/store/log error ⇒ deny |
| T-8 | **TOCTOU / race** | Decision and execution diverge under concurrency | Decision bound to the specific action+scope; one approval = one execution; **serialized/locked consumption** (`FAILURE_MODES` §3c) | **Executable (partial)**: concurrent/replay ⇒ single-use; restart ⇒ fresh decision (timing-dependent, best-effort) |
| T-9 | **Approval replay / argument-swap** | An old/other approval reused, or a token granted for a safe action reused for an unsafe one | **Complete canonical invocation fingerprint** (SHA-256 over canonical JSON; HUMAN_AUTHORITY §4a): approval bound to capability+path+**complete normalized params**+resources+caller+policy hash+nonce+expiry; compared **inside the serialized critical section**; any missing field/mismatch/mutation/duplicate/expiry/replay ⇒ DENY; monotonic expiry | **Executable deny-tests**: full-match succeeds once; **every field mutation ⇒ DENY**; reuse/expired/duplicate ⇒ DENY |
| T-10 | **Log tampering / silent decision / insecure audit file** | Outcome not recorded/altered; audit file readable/writable by others or symlinked | Secure audit file (`0600`, owner/regular/symlink checks at startup + before use; `FAILURE_MODES` §3d) — failure ⇒ init failure ⇒ DENY-all; every outcome logged before/with enforcement; hash-chain integrity detection | **Split**: *silent decision* + *insecure-file* = **executable** (insecure perms/owner/symlink/non-regular ⇒ DENY); *tamper resistance* = **review check** — integrity-detecting only, **NOT tamper-proof** (local admin can edit; not defended) |
| T-11 | **Privilege via delegation** | A child/sub-context inherits more than parent | Delegation excluded in MVP (Sprint 3); no escalation surface | **Absence assertion**: assert delegation surface absent (not a deny-test) |
| T-12 | **Vendor metadata trusted as enforcer** | `RETAINED_SURFACE_STATES.yaml` treated as the gate | Metadata ≠ enforcer; engine is sole decider; YAML read as reference only | **Review check**: reviewer confirms the engine (not the YAML) decides |

> **Test-category caveat (Correction 5).** The "Test" column above is the *intended* check, but the classes
> are **not** uniformly executable deny-tests. T-6 and T-11 are **absence assertions** (the surface does not
> exist); T-10 (tampering) and T-12 are **review-only**; T-1 against *real* entry points is **deferred**.
> The authoritative per-class categorization (executable / absence / structural / review / deferred) and the
> P-01…P-13 coverage matrix live in `TEST_AND_VALIDATION_PLAN.md` §2.4 and §3/§3a. Do not claim every class
> has a deny-test.

## 4. The chokepoint completeness obligation

Per `POLICY_CHOKEPOINT_MAP.md`, a capability is only "governed" if **every** path that can reach it is gated
(or the surface is absent). Sprint 5's gate must be the single funnel; the test harness must attempt each
boundary (P-01…P-13 conceptually) and show coverage or denial. **"Mostly covered" = bypassable = fail.**

## 5. Residual risk after Sprint 5 (honest)

- Sprint 5 proves enforcement **against the Magna-owned test harness only** — **not** against any real
  capability runtime (none exists). The harness **cannot** prove that future real capability entry points are
  unable to bypass the gate. Real-capability bypass risk re-opens as each capability is wired in later sprints
  — each must route through this gate and **re-run end-to-end chokepoint validation** before being enabled.
  **R-06 therefore stays OPEN** after a successful Sprint 5 (a likelihood note may be added for the
  harness-covered surface), and is **not** closed until real capabilities are gated and validated end-to-end.
- Sprint 5 also does **not** provide: authenticated human approval (test-only provider), a tamper-proof audit
  log (integrity-detecting only), or protection against a local administrator editing audit files.

## 6. Boundaries

Analysis only. No engine, gate, or test exists yet. Mitigations are requirements for the (separately-approved)
implementation, verified by Antigravity adversarial testing before acceptance.
