# RISKS_GAPS_AND_RECOMMENDATIONS.md
# Magna Enso — Sprint 1 TRACE Skeleton
# Risks, Gaps, and Recommendations
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Identify any risks, gaps, drift, or issues surfaced by this review. Rate severity.
Provide recommendations for the human owner.

---

## 2. Risks and Gaps Table

| # | Risk / Gap | Severity | Type | Evidence | Required Action |
|---|---|---|---|---|---|
| RG-01 | Light Curve not yet written for ENSO-F-0101 | LOW | Gap | evidence/ has only README.md | Write ENSO-0001_LIGHT_CURVE.md after human review; before marking DONE |
| RG-02 | EH-0005B could be accidentally escalated to ACCEPTED by a future worker | LOW | Governance risk | Decision currently PROPOSED — temptation to "promote" it | Human owner must be the only authority to change EH-0005B to ACCEPTED |
| RG-03 | Git initialization timing is an open question | LOW | Open question | STAR_MAP.md notes "none yet"; no decision logged | Human owner to decide: when to init git, branch model, .gitignore scope |
| RG-04 | ChatGPTReview/ path in ROLE_REGISTRY.yaml could drift if folders move | LOW | Maintenance risk | external_memory: ../../ChatGPTReview/AGENT_OUTPUT_REVIEW_SOURCE_DATA.md | If folder structure changes, update the relative path |
| RG-05 | Hermes Agent vs Hermes Desktop naming could confuse future workers | LOW | Clarity risk | ROLE_REGISTRY uses both hermes_agent and hermes_desktop_grok | Consider adding a brief naming note to TRACE_ONBOARDING.md in Sprint 2 |
| RG-06 | No .gitignore exists — when git is initialized, ChatGPTReview/ must be excluded | MEDIUM | Governance risk | ChatGPTReview/ is an external review-memory store; must not be git-tracked | When git is initialized, create .gitignore that excludes ChatGPTReview/ or parent paths |
| RG-07 | AGENT_OUTPUT_REVIEW_SOURCE_DATA.md source data tables are still template placeholders | LOW | Process gap | Fields like Current Sprint, Last Accepted Commit are empty/template | Human owner to update ChatGPT source data after accepting Sprint 1 |

---

## 3. Severity Assessment

| Severity | Count | Items |
|---|---|---|
| CRITICAL | 0 | None |
| HIGH | 0 | None |
| MEDIUM | 1 | RG-06 (git initialization + .gitignore scope) |
| LOW | 6 | RG-01 through RG-05, RG-07 |

No critical or high-severity risks introduced by Sprint 1 skeleton.

---

## 4. Drift Assessment

| Drift Type | Level | Evidence |
|---|---|---|
| Architecture drift | NONE | Skeleton precisely implements Sprint 0 blueprint |
| Governance drift | NONE | All EH decisions correctly reflected |
| Scope drift | NONE | No Sprint 2+ work started; no runtime code |
| Hermes boundary drift | NONE | No source code; EH-0005B PROPOSED only |
| HELIX boundary drift | NONE | Existing repo untouched |

---

## 5. Detailed Risk Notes

### RG-01 — Missing Light Curve (Non-blocking)

The FEATURE_TRACKER.md acceptance criteria explicitly lists this as the remaining open item:
  "[ ] Human owner reviews and approves the skeleton (then status → DONE)"

The evidence/README.md explicitly says:
  "Empty at Sprint 1. The first Light Curve will be the Sprint 1 skeleton evidence package
   (ENSO-0001_LIGHT_CURVE.md), produced for human review of feature ENSO-F-0101."

This gap is by design and correctly acknowledged. The Light Curve should be written as
the first task after human review — it documents this very skeleton delivery.

### RG-06 — Git Initialization and .gitignore Scope (Medium — prepare now)

When the human owner decides to initialize git for magna-enso/, the following must be
planned:

1. The ChatGPTReview/ directory is at:
   <CHATGPT_REVIEW_SOURCE>/

2. The magna-enso/ repo root is at:
   <MAGNA_LOCAL_ROOT>/magna-enso/

3. If the git repo is initialized at magna-enso/ level, ChatGPTReview/ is in the sibling
   directory (one level up) and would NOT be inside the git tracking scope by default.
   This is safe.

4. If the git repo is initialized at the parent level <MAGNA_LOCAL_ROOT>/,
   then ChatGPTReview/ WOULD be inside the tracking scope and needs to be in .gitignore.

5. Recommendation: Initialize git at magna-enso/ level (not parent), which naturally
   excludes ChatGPTReview/. Alternatively, if git is initialized at parent level, add
   ChatGPTReview/ to .gitignore before first commit.

6. This review output folder (antigravity-sprint-1-trace-skeleton-review/) is inside
   ChatGPTReview/ and also must not be committed.

---

## 6. Recommendations for Human Owner

### Immediate (before accepting Sprint 1)

1. READ: Review the 8 Antigravity review files in:
   <CHATGPT_REVIEW_SOURCE>/antigravity-sprint-1-trace-skeleton-review/

2. DECIDE: Approve or request corrections on the Sprint 1 skeleton.

3. If approved: Ask Claude (or preferred worker) to write the Sprint 1 Light Curve:
   trace/evidence/ENSO-0001_LIGHT_CURVE.md
   This should document the files created, validation performed, and link this review.

4. After Light Curve is written and reviewed: Mark ENSO-F-0101 as DONE in FEATURE_TRACKER.md
   and update STAR_MAP.md sprint status to Accepted.

### Before Sprint 2

5. DECIDE: Git initialization — when and at what directory level. Plan .gitignore accordingly.
   (See RG-06 above.)

6. CONFIRM: Explicit human approval to start Sprint 2 — Hermes read-only audit.
   Per AGENTS.md: "A read-only Hermes audit is a future sprint — Sprint 2 — performed
   in a separate scratch workspace after explicit human approval."

7. UPDATE: ChatGPT source data (AGENT_OUTPUT_REVIEW_SOURCE_DATA.md) with Sprint 1
   completion after freeze.

### For Future Sprints

8. Do NOT change EH-0005B from PROPOSED to ACCEPTED without explicit human decision.
   This must remain PROPOSED until Hermes Agent is actually validated as a safe E2E worker.

9. When Sprint 2 Hermes audit is authorized, ensure it uses a SEPARATE scratch workspace —
   the hermes clone never enters magna-enso/.

10. Consider adding a brief Hermes naming disambiguation note to TRACE_ONBOARDING.md.

---

## 7. What Is NOT a Risk

The following items were confirmed absent and are NOT risks:

- No hidden autonomy (config confirmed)
- No auto-commit (config confirmed + structural: no git)
- No auto-push (config confirmed + structural: no git)
- No Hermes source code (structural confirmation)
- No public network listener (no runtime code)
- No policy bypass (no policy engine yet — Sprint 5)
- No silent memory mutation (config confirmed)
- No sprint 2 work (CELESTIAL_INDEX all PLANNED areas are empty)
