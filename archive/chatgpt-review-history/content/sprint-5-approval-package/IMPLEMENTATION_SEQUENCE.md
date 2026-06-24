# IMPLEMENTATION_SEQUENCE.md
# Magna Enso — Sprint 5 Implementation Sequence
# Type: Local-only approval package (proposed plan; no execution)
# Date: 2026-06-20
# Status: FOR HUMAN APPROVAL. Sprint 5 NOT started.

---

## 1. Purpose

Propose the order of work **if** Sprint 5 is approved, so each step leaves a reviewable, fail-closed
increment. Nothing here is executed by this package.

## 2. Pre-conditions (must hold before step 1)

- **PRQ-1 CLEARED:** STAR_MAP was corrected by controlled trace commit
  `4d5c203cc236be84bd4b9bd8004cb88e8797a34d` (see `RISKS_OPEN_QUESTIONS_AND_DECISIONS.md` §3a).
- Human owner signs the Sprint 5 decision block (overview §8).
- Open decisions **D-1…D-8** resolved (notably D-3 = JSON runtime records, D-7 = `HumanDecisionProvider`
  test-only, D-8 = audit durability model).
- Work happens on an **isolated branch** (e.g. `sprint/05-policy-engine`), no auto-commit/push.

## 3. Sequence (audit sink precedes any ALLOW)

| Step | Work | Output | Fail-closed checkpoint |
|---|---|---|---|
| S5.0 | Branch + scaffold `policy/` and `tests/policy/` (empty, no behavior) | dirs | n/a |
| S5.1 | Define **JSON** policy record schema + validator (code form of Sprint 3 `CAPABILITY_POLICY_SCHEMA.md`) | schema + validator | invalid record ⇒ reject |
| S5.2 | Policy store/loader (read-only at eval; strict validation; **stdlib `json`**) | loader | missing/corrupt store ⇒ deny-all |
| S5.3 | Pure policy evaluator (`(request,policy,ctx)→decision`); default-deny core | evaluator | no record ⇒ DENY; error ⇒ DENY |
| **S5.4** | **Audit sink FIRST** — **secure file** (`0600`, owner/regular/symlink checks at startup + before use; `FAILURE_MODES` §3d); append-only JSONL: **serialized/locked** atomic append + flush, hash-chain head update, corruption detection, malformed-tail recovery, single-use **fingerprint-checked** consumption, duplicate handling (D-8; `FAILURE_MODES` §3c) + failure behavior (F-5/F-5a/F-5b/F-5c/F-12..F-15) | audit sink | insecure file / unwritable / undurable / corrupt / lock-fail ⇒ deny-all |
| S5.5 | Capability gate (single chokepoint) — **deny-only** until the audit sink is validated | gate (deny-only) | uncovered path ⇒ deny; every call logged |
| S5.6 | **Enable ALLOW/state outcomes** through the gate — only after S5.4 audit sink validated | allow-capable gate | no ALLOW without a durable, fingerprint-bound audit record |
| S5.7 | **Structural provider isolation** (`policy/` = contract + Null/Deny only; simulated provider only under `tests/policy/`; production never imports `tests/`; **no `TESTING` flag / no "uncatchable exception"**); approval coordinator: request → HOLD → provider decision → **complete canonical fingerprint** check + single-use, **monotonic expiry** (D-7; HUMAN_AUTHORITY §2b/§4a; `FAILURE_MODES` §3aa) | approval flow (`ENSO-F-0502`) | absent/unrecognized provider ⇒ deny; field mismatch/mutation/replay/expiry ⇒ deny; restart ⇒ no carry-over |
| S5.8 | Reversibility/draft-decision surface (decision only; no memory/skill subsystem) | draft decision | persist only on approval |
| S5.9 | Gate interface / test harness representing capability calls (D-1) | harness | drives testable paths |
| S5.10 | Tests: executable behavior (allow/deny/approve/fail-closed) + **bypass tests for testable classes** + structural/absence/review checks + **P-01…P-13 coverage matrix** | `tests/policy/` green | testable bypass classes deny; deferred labeled |
| S5.11 | Spectrometer checklist + evidence assembly | Light Curve (Full) draft | honest "harness-level only; not runtime-protected; no authenticated approval; not tamper-proof" |
| S5.12 | Hand to Antigravity (adversarial validation) + Grok (edge cases) | validation reports | blockers ⇒ fix before acceptance |

## 4. Order rationale

Default-deny is built **first and at the core** (S5.3). The **audit sink is built and validated before the
gate can ALLOW** (S5.4 before S5.6) — an action that cannot be durably logged is denied. The gate is
**deny-only** (S5.5) until logging is proven. The approval path (S5.7) is reached only *through* the gate, via
a `HumanDecisionProvider` that is **test-only** in Sprint 5 (absent ⇒ DENY). Tests (S5.10) separate executable
behavior, absence assertions, structural checks, and review-only items, and add the P-01…P-13 coverage matrix
labeling which entries are testable now vs deferred.

## 5. Boundaries each step preserves

- No auto-execution of real capabilities (engine decides only).
- No Hermes import/run/build; vendor baseline untouched.
- No network/cloud/UI/scheduler/remote (Non-Goals).
- No commit/push without separate human approval; merge to `main` only via reviewed review-package.
- No `STAR_MAP`/`FEATURE_TRACKER` flip to DONE until human acceptance.

## 6. Definition of done (Sprint 5)

`policy/` engine + gate + approval flow + durable logging exist; `tests/policy/` prove allow/deny/approve
and **all harness-level bypass tests and categorized structural/absence/review checks pass** (executable
deny-tests for T-2/T-3/T-5/T-7/T-9 and harness T-1/T-4/T-8; absence assertions for T-6/T-11; review checks
for T-10 tamper-resistance/T-12; P-01…P-13 matrix with deferred entries labeled); Spectrometer + Antigravity
adversarial validation pass; `ENSO-0005_LIGHT_CURVE.md` (Full) written; human owner accepts. **R-06 stays
OPEN** (not auto-closed; end-to-end validation recurs per real capability). Then Sprint 5 stops.

## 7. Boundaries

Plan only. No step is executed by this package.
