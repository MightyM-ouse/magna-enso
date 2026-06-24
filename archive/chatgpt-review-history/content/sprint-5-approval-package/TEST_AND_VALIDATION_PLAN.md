# TEST_AND_VALIDATION_PLAN.md
# Magna Enso — Sprint 5 Test and Validation Plan
# Type: Local-only approval package
# Date: 2026-06-20
# Status: FOR HUMAN APPROVAL. Sprint 5 NOT started.

---

## 1. Purpose

Define the tests that must pass **before** Sprint 5 acceptance. The acceptance bar (plan + ENSO-F-0501 card):
no-policy ⇒ deny; approve-required ⇒ HOLD pending a provider decision; Sprint 5 tests use programmatically
simulated decisions, while a missing production provider ⇒ DENY; **no path bypasses the gate** at the harness
level; all outcomes logged.

> **Scope caveat (Correction 2).** "No path bypasses the gate" is provable in Sprint 5 only at the **harness
> level** — the gate and the calls that reach it are Magna-owned test surfaces. It **does not** prove that
> future *real* capability entry points cannot bypass the gate, because no real runtime exists yet. **R-06
> stays OPEN**, and end-to-end chokepoint validation **recurs** whenever a real capability is integrated
> (D-5; see §3a P-01…P-13 matrix).

## 2. Test categories

### 2.1 Allow-path tests
- `active_safe` capability ⇒ ALLOW, logged.
- `read_only` ⇒ ALLOW read, DENY mutate.
- `report_only` ⇒ ALLOW report, DENY execute.

### 2.2 Deny-path tests (default-deny)
- Unknown capability / no policy ⇒ DENY (T-2).
- Path not in `paths_covered` ⇒ DENY (T-1, F-8).
- `disabled` state ⇒ DENY.

### 2.3 Approval-path tests (`ENSO-F-0502`)
- `approval_required` ⇒ HOLD; no execution until the test-only provider returns a simulated `approve_once`.
- Production provider is absent in Sprint 5; production approval-required requests ⇒ DENY.
- Approve_once ⇒ single ALLOW, then exhausted.
- Simulated deny / timeout / no-response ⇒ DENY; absent production provider ⇒ DENY (F-6, F-7).

### 2.4 Negative / bypass coverage by **category** (not all are deny-tests)

The bypass classes T-1…T-12 are **not** uniformly executable deny-tests. Some are **absence assertions**
(the surface does not exist), some are **structural/review checks**, and some are **deferred** until a real
capability surface exists. Honest mapping:

| Class | Category | Sprint 5 check | Notes |
|---|---|---|---|
| T-1 uncovered path | Executable (harness) **+ deferred (real)** | Harness: call around the gate ⇒ denied. **Real entry points cannot be proven here** — deferred to per-capability integration. | This is why R-06 stays OPEN. |
| T-2 missing-policy allow | Executable deny-test | unknown capability ⇒ DENY | testable now |
| T-3 input-driven escalation | Executable deny-test | payload claiming privilege ⇒ DENY | testable now |
| T-4 self-approval | Executable (harness) | worker/config/self-approval bypass ⇒ rejected; only the explicit test-provider seam may return simulated decisions | test-only simulation is not authenticated production approval; absent production provider ⇒ DENY |
| T-5 config bypass | Executable deny-test | config flip ⇒ still gated/denied | testable now |
| T-6 plugin/MCP self-registration | **Absence assertion** | assert no dynamic loader / registration path exists | not a deny-test — surface absent |
| T-7 fail-open on error | Executable deny-test | evaluator/store/log error ⇒ DENY | testable now |
| T-8 TOCTOU/race & restart HOLD | Executable (partial) | concurrency single-use; restart ⇒ fresh decision | timing-dependent; best-effort |
| T-9 approval replay | Executable deny-test | reuse expired/consumed ⇒ DENY | testable now |
| T-10 silent decision / log tampering | **Split** | *silent decision*: executable (every outcome logged). *log tampering*: **review-only / NOT protected** (not tamper-proof; local admin can edit) | do not claim tamper-proof |
| T-11 delegation privilege | **Absence assertion** | assert delegation surface absent (MVP) | not a deny-test — surface absent |
| T-12 vendor-metadata-as-enforcer | **Review check** | reviewer confirms engine (not YAML) decides | structural/review |

### 2.5 Audit/logging tests (executable)
- Every outcome (allow/deny/hold/approve/reject) emits a **durable** append-only audit record (T-10 silent-decision half; D-8 atomic append + flush).
- Malformed-tail recovery, corruption detection (hash-chain), duplicate handling, approval consumption behave per D-8.
- Records contain the approval-record fields where applicable.

### 2.6 Reversibility tests (executable)
- `draft_only` decision stages, does not persist without approval; discard is clean.

### 2.7 Security-correction tests (Antigravity-required; explicit)

**Provider isolation (C1 / Gap 1 / T-4):**
- **Structural:** production package (`policy/`) contains **no** simulated/approve-returning provider — only the
  contract + the Null/Deny provider (AST/grep assertion).
- **Structural:** **no import from `tests/`** appears anywhere under `policy/` (import-graph/AST assertion).
- **Executable:** with no provider configured (default), an `approval_required` call **DENIES** (Null/Deny).
- **Executable:** an unrecognized/unresolved provider id **DENIES**.

**Approval fingerprint binding (C2 / Gap 2 / T-9):**
- **Executable:** a **complete fingerprint match** consumes the approval and ALLOWs **exactly once**; a second
  use ⇒ DENY.
- **Executable:** **every single field mutation** (capability_id, invocation_path, proposed_action, each
  normalized parameter, affected_resources, caller_context_id, policy hash, nonce, expiry) ⇒ DENY.
- **Executable:** missing field, duplicate, expired, or replayed fingerprint ⇒ DENY.
- **Executable:** **concurrent consumption** of one approval allows **at most one** success (the rest DENY).
- **Structural:** audit records store **hashed/redacted** sensitive values, not raw payloads, while still
  verifying the fingerprint.

**Audit-file security (C3 / Gap 3 / T-10):**
- **Executable:** audit path with **insecure permissions** (not `0600`/owner-only) ⇒ init failure ⇒ DENY-all.
- **Executable:** audit path **owned by another user** ⇒ DENY-all.
- **Executable:** audit path is a **symlink** ⇒ refused ⇒ DENY-all.
- **Executable:** audit path is a **non-regular file** (FIFO/dir/device) ⇒ DENY-all.
- **Executable:** secure creation leaves **no permissive intermediate** state (created `0600` atomically).

**Clock handling (C4 / Gap 4):**
- **Executable:** simulated **clock rollback / uncertainty** ⇒ pending approvals invalidated ⇒ DENY.
- **Executable:** **restart** ⇒ pending approvals are **not** carried across; a fresh decision is required;
  resting state is default-deny.

## 3. Test categories (keep them separate)

Do **not** conflate these. Each finding states its category:

1. **Executable behavior tests** — run code, assert allow/deny/approve/fail-closed outcomes.
2. **Absence assertions** — assert a dangerous surface/path is *not present* (T-6, T-11). Proves absence, not "deny".
3. **Structural checks** — code/shape inspection (single chokepoint; JSON loader; provider boundary).
4. **Independent review checks** — human/Antigravity judgement (T-12; tamper-proofing NOT claimed; honesty of evidence).

## 3a. P-01…P-13 chokepoint coverage matrix (canonical `POLICY_CHOKEPOINT_MAP.md`)

Sprint 5 has **no real runtime**, so most boundaries are **DEFERRED** until their surface is built. Honest status:

| Boundary | Surface | Sprint 5 status |
|---|---|---|
| P-01 startup | toolset assembly | **Deferred** (no runtime) — harness models entry only |
| P-02 tool registry | registration | **Absence/structural** — no registry of real tools in MVP |
| P-03 model tool dispatch | dispatch | **Testable now (harness)** — gate represents a capability call |
| P-04 agent-owned tools | memory/delegate/etc. | **Testable now (harness)** for the routing rule; real tools deferred |
| P-05 cron/scheduler | scheduler | **Deferred** → Sprint 9 |
| P-06 gateway/API | listener | **Absence** — excluded by non-import |
| P-07 ACP tools | ACP | **Deferred / absence** |
| P-08 provider/model calls | providers | **Absence** — excluded |
| P-09 memory persistence | memory | **Deferred** → Sprint 8 |
| P-10 skill persistence | skills | **Deferred** → Sprint 8 |
| P-11 plugin loading | plugin loader | **Absence** — excluded |
| P-12 MCP loading | MCP | **Absence** — excluded |
| P-13 outbound delivery | messaging | **Absence** — excluded |

**Rule:** as each deferred boundary's real surface is built (later sprints), end-to-end chokepoint validation
for that boundary **must recur** before that capability may be enabled (D-5). Sprint 5 cannot and does not
prove P-01…P-13 end-to-end.

## 4. Coverage requirement (corrected)

- 100% of the **engine's own decision branches** exercised by executable tests.
- Every **testable** bypass class (T-2, T-3, T-5, T-7, T-9, and harness-level T-1/T-4/T-8) has a deny/assert test.
- **Absence** classes (T-6, T-11) and **review** classes (T-10 tampering, T-12) are covered by absence/review
  checks, **not** claimed as deny-tests.
- The P-01…P-13 matrix labels testable-now vs deferred; deferred boundaries are explicitly **not** proven.
- Tests are deterministic and run locally (`tests/policy/`), no network, no Hermes, no external services.

## 5. Independent validation (mandatory before acceptance)

- **Spectrometer checklist** (`trace/VALIDATION_CHECKLIST.md`) run against the change.
- **Antigravity adversarial validation** — independent attempt to bypass the gate; verdict required
  (does not author code, does not self-approve). See `INDEPENDENT_VALIDATION_BRIEF.md`.
- **Grok** edge-case / second-opinion challenge.
- Validation evidence attached to `ENSO-0005_LIGHT_CURVE.md` (Full).

## 6. Honesty rule for results

Test results are **real** (actual run logs). The engine passing the harness means "enforcement core works
against the harness" — **not** "the live system is protected." That distinction must appear in the evidence.

## 7. Acceptance gate

Sprint 5 is accepted only when all categories pass, Antigravity validation has no blocking issues, the Light
Curve is written, and the **human owner signs off**. No worker self-approves; a blocked gate is expected, not
a failure.

## 8. Boundaries

Plan only. No tests are written or run by this package.
