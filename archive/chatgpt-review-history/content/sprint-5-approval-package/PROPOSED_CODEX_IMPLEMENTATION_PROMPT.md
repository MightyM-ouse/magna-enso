# PROPOSED_CODEX_IMPLEMENTATION_PROMPT.md
# Magna Enso — Proposed Codex Implementation Prompt (DRAFT — BLOCKED)
# Type: Local-only approval package
# Date: 2026-06-20
# Status: DRAFT ONLY. BLOCKED. PRQ-1 is cleared at 4d5c203; valid gate still requires resolved D-1…D-8 + explicit human approval.
#         Do NOT run until all three hold.

---

## ⛔ Blocked banner

> This prompt is a **draft**. It must **not** be given to Codex (or any worker) until:
> (1) **PRQ-1 is CLEARED** by `4d5c203cc236be84bd4b9bd8004cb88e8797a34d`;
> (2) the human owner signs the Sprint 5 approval (overview §8); (3) decisions **D-1…D-8** are confirmed
> (notably D-3 = JSON runtime records, D-7 = `HumanDecisionProvider` test-only, D-8 = audit durability).
> Until then, Sprint 5 is **NOT STARTED**.

## 1. Draft prompt (for Codex, once approved)

```text
ROLE: Builder (Codex). Sprint 5 — Policy Engine Foundation (ENSO-F-0501 + ENSO-F-0502).
AUTHORITY: Human owner is final authority (EH-0010). You implement; you do NOT approve, commit, push, or merge.

== STEP 0: MANDATORY PREFLIGHT (run in order; STOP on any unexpected state) ==
  # 0a. Verify clean main at the expected base BEFORE creating any branch:
  cd <MAGNA_LOCAL_ROOT>/magna-enso
  git branch --show-current            # expect: main
  git rev-parse HEAD                    # expect: 4d5c203cc236be84bd4b9bd8004cb88e8797a34d
  git status --short --branch --untracked-files=all   # expect: clean (## main, no changes)
  git log --oneline -5
  # 0b. Verify gates in trace/: R-06 OPEN, EH-0005B PROPOSED, ENSO-F-0501/0502 PLANNED,
  #     STAR_MAP reflects live git (PRQ-1 done).
  # STOP and report if: current branch != main, HEAD != 4d5c203cc236be84bd4b9bd8004cb88e8797a34d, tree not clean, R-06 not OPEN,
  # EH-0005B not PROPOSED, Sprint 5 already started, or STAR_MAP still stale. Do not proceed.

== STEP 1: CREATE BRANCH (only after STEP 0 passes) ==
  git switch -c sprint/05-policy-engine    # create from clean main; never work on main; never push

== STEP 2: VERIFY THE NEW BRANCH AND UNCHANGED BASE ==
  git branch --show-current            # expect: sprint/05-policy-engine
  git rev-parse HEAD                    # expect: still 4d5c203cc236be84bd4b9bd8004cb88e8797a34d (same base commit)
  git status --short --branch          # expect: clean on the new branch
  # STOP and report if the branch name is wrong, the base moved off 4d5c203cc236be84bd4b9bd8004cb88e8797a34d, or the tree is not clean.

== CONTEXT (read first, do NOT modify) ==
  trace/STAR_MAP.md, FEATURE_TRACKER.md, DECISION_LOG.md, RISK_REGISTER.md, TRACE_CONFIG.yaml,
  VALIDATION_CHECKLIST.md, CELESTIAL_INDEX.json
  ../ChatGPTReview/sprint-3-capability-governance-design/ : DEFAULT_DENY_MODEL, UNIFIED_APPROVAL_ENGINE_MODEL,
  POLICY_CHOKEPOINT_MAP, CAPABILITY_POLICY_SCHEMA, CAPABILITY_STATES_PROPOSAL
  ../ChatGPTReview/sprint-5-approval-package/ : all 12 files (esp. ENFORCEMENT_ARCHITECTURE,
  THREAT_MODEL_AND_BYPASS_ANALYSIS, FAILURE_MODES_AND_FAIL_CLOSED_BEHAVIOR, TEST_AND_VALIDATION_PLAN,
  IMPLEMENTATION_SEQUENCE, HUMAN_AUTHORITY_AND_APPROVAL_BOUNDARIES, RISKS_OPEN_QUESTIONS_AND_DECISIONS)

== GOAL ==
  Build a Magna-owned policy engine (enforcement CORE) under policy/, with tests under tests/policy/,
  enforcing DEFAULT-DENY capability gating + an approval-request contract + durable append-only logging.
  Sprint 5 tests use programmatically simulated decisions through a test-only provider. Human-only approval
  is a future production invariant; no authenticated production provider exists, and a missing provider DENIES.
  proven against a Magna-owned gate interface / test harness (NO real runtime exists).

== ALLOWED PATHS (create/modify ONLY these) ==
  policy/**                 (new engine code)
  tests/policy/**           (new tests)
  trace/evidence/ENSO-0005_LIGHT_CURVE.md   (DRAFT evidence only; status IN_REVIEW; do NOT mark DONE)

== FORBIDDEN PATHS (never create/modify) ==
  vendor/**                 (inert baseline — untouched, never imported/run/built)
  src/**, ui/**, scheduler/**, gateway/**, providers/**, plugins/**   (out of scope / non-goals)
  trace/STAR_MAP.md, trace/FEATURE_TRACKER.md, trace/DECISION_LOG.md, trace/RISK_REGISTER.md
                            (status files — a SEPARATE trace task updates these after acceptance)
  AGENTS.md, README.md, CLAUDE.md, CODEX.md, ANTIGRAVITY.md, .gitignore, any planning/** file

== TESTS-FIRST REQUIREMENT ==
  Write failing tests in tests/policy/ BEFORE the corresponding behavior, in this order
  (see IMPLEMENTATION_SEQUENCE S5.1->S5.12):
    1. JSON policy schema + validator tests (D-3; stdlib json; NO YAML/PyYAML).
    2. Default-deny evaluator tests (no record/uncovered/error => DENY).
    3. Audit SINK tests FIRST (atomic append + flush, malformed-tail recovery, hash-chain corruption
       detection, duplicate handling) -- the gate must be DENY-ONLY until the sink is validated (D-8).
    4. Gate tests: ALLOW path enabled ONLY after the audit sink passes; no ALLOW without a durable record.
    5. Provider isolation (STRUCTURAL): policy/ has ONLY the HumanDecisionProvider contract + a fail-closed
       Null/Deny provider (default). The simulated approve/deny provider lives ONLY under tests/policy/.
       production NEVER imports tests/. NO `TESTING` flag and NO "uncatchable exception" as the boundary.
       Tests: (a) structural — no approve-provider in policy/; (b) structural — no import of tests/ from
       policy/; (c) null/missing/unrecognized provider => DENY.
    6. Approval fingerprint binding: compute a canonical invocation fingerprint = SHA-256 over canonical JSON
       (sorted keys) of {approval_id+nonce, capability_id, invocation_path, proposed_action, NORMALIZED
       COMPLETE parameters, affected_resources, caller_context_id, policy_version/policy_record_hash, expiry}.
       Consume inside the SAME serialized critical section; compare the COMPLETE fingerprint. Tests:
       complete match succeeds once; EVERY field mutation => DENY; missing/duplicate/expired/replay => DENY;
       concurrent consumption => at most one success. Redact/hash sensitive values in audit (verification kept).
    7. Audit-file security: create/verify audit file 0600, owner-only, regular-file, refuse symlink, restrictive
       creation with NO permissive intermediate; verify at startup AND before each use; any failure =>
       init failure => gate DENY-all. Document platform-specific handling; never silently weaken. Tests:
       insecure perms / wrong owner / symlink / non-regular path => DENY.
    8. Clock handling: monotonic expiry within the process; pending approvals NOT carried across restart;
       wall-clock kept for audit evidence only; clock rollback/uncertainty invalidates pending => DENY. Tests:
       clock rollback/uncertainty and restart invalidate pending approvals.
    9. Bypass tests by CATEGORY per TEST_AND_VALIDATION_PLAN §2.4/§2.7: executable deny-tests
       (T-2,T-3,T-5,T-7,T-9, harness T-1/T-4/T-8); ABSENCE assertions (T-6,T-11); review-only (T-10 tamper, T-12).
   10. P-01..P-13 coverage matrix: label testable-now vs deferred; do NOT claim end-to-end coverage.

== HARD REQUIREMENTS ==
  - Default-deny: no record OR uncovered path OR any error => DENY.
  - Fail-closed everywhere (store/evaluator/log/provider/file/lock failure => DENY).
  - Audit sink built+validated BEFORE any ALLOW; gate deny-only until then; ALLOW only after a durable,
    flushed, fingerprint-bound audit record under the serialized lock.
  - Provider isolation is STRUCTURAL (package layout), NOT a TESTING flag and NOT an "uncatchable exception".
    policy/ = contract + Null/Deny provider only; simulated provider only under tests/policy/; production never
    imports tests/; missing/unrecognized provider => DENY. No authenticated production provider exists.
  - Approval consumption compares the COMPLETE canonical invocation fingerprint (SHA-256/canonical JSON,
    stdlib) inside the serialized critical section; any missing field/mismatch/mutation/duplicate/expiry/
    replay => DENY. Sensitive values redacted/hashed in audit.
  - Audit file: 0600 owner-only, regular-file, symlink-refused, restrictive atomic creation, verified at
    startup + before use; failure => DENY-all.
  - Expiry uses monotonic time; pending approvals do NOT survive restart; clock rollback/uncertainty => DENY.
  - Runtime policy records are JSON (stdlib json). NO new dependency (PyYAML included) without separate approval.
  - Append-only audit is integrity-DETECTING, NOT tamper-proof; do NOT claim tamper-proof/immutable.

== SCOPE OUT / FORBIDDEN ACTIONS ==
  - No auto-execution of real capabilities; no scheduler/remote/UI/memory-skill subsystem.
  - No importing/running/building Hermes; no installing dependencies.
  - No network, cloud, listeners. No commit, no push, no merge. Do not edit trace status to DONE.
  - Do not promote EH-0005B. Do not start Sprint 6.
  - Do NOT claim: "no bypass" (real), "runtime enforcement exists", "human authenticated", "tamper-proof".

== VALIDATION COMMANDS (run; capture full output into the Light Curve) ==
  cd <MAGNA_LOCAL_ROOT>/magna-enso
  python -m pytest tests/policy -v            # all tests; deterministic; no network
  python -m compileall policy                  # syntax/structure check
  git status --short --branch --untracked-files=all   # show every changed/new file
  git --no-pager diff                          # full unstaged diff
  git --no-pager diff --stat                   # change summary
  # confirm ONLY policy/**, tests/policy/**, trace/evidence/ENSO-0005_LIGHT_CURVE.md changed

== EVIDENCE + STOP ==
  Draft trace/evidence/ENSO-0005_LIGHT_CURVE.md (Full, status IN_REVIEW) with: files changed, full git
  status + diff stat, test run logs, the P-01..P-13 matrix, and an HONESTY section stating: harness-level
  only; not runtime-protected; no authenticated approval (test-only provider); not tamper-proof; R-06 stays
  OPEN; end-to-end validation recurs per real capability.
  Then STOP. Do NOT commit/push/merge. Hand to Antigravity (validation) + Grok (edge cases). Pause for human
  acceptance. A separate trace task records acceptance and flips status.
```

## 2. Why this prompt is bounded the way it is

- **Preflight + branch** — refuses to start from an unexpected/stale state (PRQ-1, R-06, EH-0005B verified).
- **Allowed vs forbidden paths** — confines changes to `policy/`, `tests/policy/`, and a draft Light Curve;
  status/trace files are updated only by a separate task after acceptance.
- **Tests-first + audit-before-allow** — encodes Corrections 5 & 6: deny-only gate until the validated audit
  sink exists; bypass tests categorized (executable / absence / review / deferred); P-01…P-13 labeled.
- **JSON runtime records / no deps** — Correction 1 / D-3·D-4; PyYAML only via separate approval.
- **`HumanDecisionProvider` test-only, absent ⇒ DENY** — Correction 3 / D-7; no authenticated approval claimed.
- **Audit integrity-detecting, not tamper-proof** — Correction 4 / D-8; explicit non-protection.
- **Exact validation commands + full git status/diff + no commit** — Correction 9; reviewable, reversible.
- **Honesty clause + R-06 OPEN** — defends S5-R1; no "no bypass / runtime-protected / tamper-proof" claims.

## 3. Status

DRAFT / BLOCKED. Not issued. **PRQ-1 is CLEARED** at `4d5c203`. The remaining valid gate is resolved
**D-1…D-8** + **explicit human approval**. Until both hold, Sprint 5 is **NOT STARTED**.
