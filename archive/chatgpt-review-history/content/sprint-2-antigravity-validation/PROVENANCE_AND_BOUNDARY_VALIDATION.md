# PROVENANCE_AND_BOUNDARY_VALIDATION.md
# Magna Enso — Sprint 2 Hermes Read-Only Audit
# Provenance and Boundary Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Independently verify the Hermes clone provenance claims in HERMES_PROVENANCE.md and
confirm all Sprint 2 governance boundaries held.

---

## 2. Provenance Verification

### 2.1 Claimed vs Verified

| Field | Claimed in HERMES_PROVENANCE.md | Independently Verified | Match? |
|---|---|---|---|
| Source repo URL | https://github.com/nousresearch/hermes-agent | git remote -v: origin https://github.com/nousresearch/hermes-agent | YES |
| Audited commit SHA | 33b1d144590a211100f42aa911fd7f91ba031507 | git rev-parse HEAD: 33b1d144590a211100f42aa911fd7f91ba031507 | YES (exact) |
| Clone path | <MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/ | ls confirmed directory exists | YES |
| Branch audited | main | git rev-parse --abbrev-ref HEAD: main | YES |
| Clone git status | Clean (implied) | git status --short: empty output | CONFIRMED |
| License file | LICENSE (MIT) | head -5 LICENSE: "MIT License, Copyright (c) 2025 Nous Research" | YES |
| Top-level layout | agent/, tools/, cron/, gateway/, etc. | ls hermes-clone/ confirms key dirs | YES |

Assessment: All provenance claims verified independently. No discrepancies.

### 2.2 Clone Path Safety

The Hermes clone is at:
  <MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/

The magna-enso repo is at:
  <MAGNA_LOCAL_ROOT>/magna-enso/

The clone is in _scratch/ — a sibling directory to magna-enso/, completely separate.
It is not inside magna-enso/ and has no cross-reference coupling.

Result: Clone is in the approved scratch workspace. PASS.

### 2.3 Shallow Clone Note

HERMES_PROVENANCE.md correctly notes: "This was a shallow clone of the current default
branch head, not a full history audit." This is appropriate for a read-only architectural
audit. The SHA is pinned and verified, which is sufficient for Sprint 2 scope.

---

## 3. magna-enso Integrity Verification

| Check | Expected | Actual | Status |
|---|---|---|---|
| HEAD SHA | e0a28d4a0d50e5107392ae6bacfbdec52080487e | e0a28d4a0d50e5107392ae6bacfbdec52080487e | MATCH |
| Branch | main | main | MATCH |
| Git working tree | Clean | Clean (empty git status) | MATCH |
| .py files in magna-enso/ | 0 | 0 | MATCH |
| docs/audit/ directory | Absent | Absent | MATCH |
| Hermes source directories | Absent | Absent (only .git/ and trace/) | MATCH |
| src/ directory | Absent | Absent | MATCH |
| New branches | None | None | MATCH |
| EH-0005B in DECISION_LOG | PROPOSED | PROPOSED | MATCH |
| Number of commits | 1 (Sprint 1) | 1 (e0a28d4 only) | MATCH |

Assessment: magna-enso is completely unchanged by Sprint 2 audit. CONFIRMED.

---

## 4. Governance Gates Verification

| Gate | Required By | Status | Evidence |
|---|---|---|---|
| No Hermes modification | SPRINT_2_SCOPE_AND_BOUNDARIES §3.1 | CONFIRMED | Clone git status clean |
| No magna-enso modification | SPRINT_2_SCOPE_AND_BOUNDARIES §3.2 | CONFIRMED | git status clean, SHA unchanged |
| No Hermes source in magna-enso/ | SPRINT_2_SCOPE_AND_BOUNDARIES §3.3 | CONFIRMED | 0 .py files, no Hermes dirs |
| No commits | SPRINT_2_SCOPE_AND_BOUNDARIES §3.4 | CONFIRMED | Only Sprint 1 commit in log |
| No pushes | SPRINT_2_SCOPE_AND_BOUNDARIES §3.4 | CONFIRMED | No new remote refs |
| No new branches | SPRINT_2_SCOPE_AND_BOUNDARIES §3.5 | CONFIRMED | Only main branch |
| No runtime code | SPRINT_2_SCOPE_AND_BOUNDARIES §3.6 | CONFIRMED | No src/ or scripts in magna-enso |
| Scratch workspace local-only/uncommitted | SPRINT_2_SCOPE_AND_BOUNDARIES §3.7 | CONFIRMED | _scratch/ not inside magna-enso git repo |
| EH-0005B remains PROPOSED | SPRINT_2_SCOPE_AND_BOUNDARIES, HERMES_AUDIT_PLAN | CONFIRMED | DECISION_LOG.md grep |
| Hermes Agent not activated | WORKER_ASSIGNMENT_RECOMMENDATION §3.6 | CONFIRMED | Light Curve: "Hermes Agent use: Not used" |
| Hermes not built or run | SPRINT_2_RISK_AND_GOVERNANCE_CHECKLIST §1 | CONFIRMED | No build artifacts; confirmed in Light Curve |
| No Sprint 3 started | SPRINT_2_SCOPE_AND_BOUNDARIES §2 | CONFIRMED | No Sprint 3 artifacts |
| No Sprint 4 started | SPRINT_2_SCOPE_AND_BOUNDARIES §2 | CONFIRMED | No fork, no runtime code |

All 13 governance gates: CONFIRMED HELD.

---

## 5. Source Leakage Check

### 5.1 Code Block Analysis

Automated scan of all 9 reports for code blocks exceeding 10 lines:
Result: ZERO code blocks exceeding 10 lines found.

### 5.2 Citation Style Compliance

Checked against HERMES_AUDIT_PLAN.md §6 evidence rules:
"Quote only minimal identifiers (function/file names) — never paste Hermes source into
reports or into magna-enso/."

Observed citation patterns across reports:
- Function citations: tools/registry.py::ToolRegistry.dispatch
- File path citations: agent/tool_executor.py, cron/scheduler.py
- Method name citations: spawn_background_review_thread, _background_review_worker
- Table entries with short descriptive text
- No inline source code blocks with actual Python/JS code

Assessment: All reports correctly use identifier-only citation style. Source leakage: NONE.

---

## 6. License Verification

Hermes top-level license (directly read from clone):
  "MIT License\nCopyright (c) 2025 Nous Research"

This matches:
- pyproject.toml: license = {text = "MIT"} (as reported in LICENSE_AND_DEPENDENCY_REVIEW.md)
- HERMES_PROVENANCE.md claim: "MIT"
- LICENSE_AND_DEPENDENCY_REVIEW.md claim: "Top-level license type verified from local LICENSE: MIT"

The MIT license is permissive and compatible with a governed fork baseline (Sprint 4).
It requires attribution (copyright notice preserved). The Sprint 4 fork plan correctly
notes that "provenance + SHA + MIT attribution" must be recorded (per README.md).

Caveats verified in LICENSE_AND_DEPENDENCY_REVIEW.md:
- Plugin-level license files not assumed identical — correct
- Optional integrations may carry separate terms — correct
- Full transitive dependency analysis deferred — correct

---

## 7. Provenance and Boundary Verdict

```
Provenance:       VERIFIED — all 7 fields confirmed independently
Clone boundaries: CONFIRMED — scratch path is correct; clone is isolated
magna-enso:       CONFIRMED UNCHANGED — SHA, branch, status, content all match
Governance gates: 13/13 CONFIRMED HELD
Source leakage:   NONE — identifier-only citations throughout
License:          MIT CONFIRMED — subject to plugin/dependency caveats
EH-0005B:         PROPOSED — unchanged

PROVENANCE AND BOUNDARY VALIDATION: PASS — no issues found
```
