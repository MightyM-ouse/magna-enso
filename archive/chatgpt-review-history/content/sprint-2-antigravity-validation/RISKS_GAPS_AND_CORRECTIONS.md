# RISKS_GAPS_AND_CORRECTIONS.md
# Magna Enso — Sprint 2 Hermes Read-Only Audit
# Risks, Gaps, and Corrections
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Enumerate all risks, gaps, and required or recommended corrections found during this
validation. Provide severity ratings and action guidance.

---

## 2. Issues Register

| ID | Severity | Type | Description | Source | Blocking? | Action |
|---|---|---|---|---|---|---|
| VA-01 | LOW | Structural gap | SPRINT_2_LIGHT_CURVE.md uses custom section structure, not EVIDENCE_TEMPLATE format. Missing explicit "Files Inspected" and "Evidence" section headers. Content present under different headings. | ANTIGRAVITY_SPRINT_2_VALIDATION.md V-01 | NO | Add format note or restructure headers before DONE |
| VA-02 | LOW | Scope gap (by design) | Full plugin-by-plugin threat modeling not performed. Acknowledged in reports with medium-high confidence. | HERMES_CODE_MAP.md, CAPABILITY_GATING_FEASIBILITY.md | NO — Sprint 3 input | Sprint 3 must assess plugin risk depth before fork |
| VA-03 | LOW | Scope gap (by design) | Transitive dependency license analysis not performed. Correctly deferred as Sprint 4 pre-fork requirement. | LICENSE_AND_DEPENDENCY_REVIEW.md | NO | Mandatory before Sprint 4 — flagged correctly |
| VA-04 | LOW | Scope gap (by design) | Independent SBOM scan not performed. Correctly flagged as open question. | LICENSE_AND_DEPENDENCY_REVIEW.md open questions | NO | Consider SBOM before Sprint 4 fork acceptance |
| VA-05 | INFO | Worker assignment | Claude interpretation, Grok challenge, ChatGPT continuity review steps not confirmed in artifact set. These are planned subsequent steps, not Sprint 2 audit failures. | WORKER_ASSIGNMENT_RECOMMENDATION.md §4 | NO — Sprint 2 IN_REVIEW correct | Complete remaining review chain before DONE |
| VA-06 | LOW | Minor counting note | AUTONOMY_ENTRY_POINT_MAP.md title says 12 entry points but table has 13 rows (background review through outbound delivery). Non-blocking minor inconsistency. | AUTONOMY_ENTRY_POINT_MAP.md | NO | Clarify count in summary (13 is the correct number) |
| VA-07 | MEDIUM | Forward risk for Sprint 3 | "Disabled by default" is not defined to mean process-level vs dispatch-level disablement. Sprint 3 must specify enforcement level (module not imported vs dispatch blocked vs config disabled). | CAPABILITY_GATING_FEASIBILITY.md | NO (Sprint 3) | Sprint 3 governance design must define disablement tiers |
| VA-08 | MEDIUM | Forward risk for Sprint 3 | No unified approval engine exists in Hermes — approval.py covers terminal/code; write_approval.py covers memory/skills; no common audit log. Sprint 3 must design a unified approval layer. | ACTION_DISPATCH_MAP.md, CAPABILITY_GATING_FEASIBILITY.md | NO (Sprint 3) | Sprint 3 must specify unified approval architecture |
| VA-09 | MEDIUM | Forward risk for Sprint 4 | Remote execution backends (Modal/Daytona/SSH) are classified "disabled by default" but have enough coupling that "disable" may not be sufficient — they may need to be removed from the fork. Sprint 4 must decide: disable vs remove. | EXTERNAL_SURFACE_MAP.md, MAGNA_ENSO_REUSE_RECOMMENDATION.md | NO (Sprint 4) | Sprint 4 fork baseline decision: remove remote backends |
| VA-10 | LOW | License caveats not cleared | Plugin-level license files not individually verified. HERMES_PROVENANCE.md notes plugin LICENSE files exist. LICENSE_AND_DEPENDENCY_REVIEW.md correctly flags this as requiring separate legal review. | LICENSE_AND_DEPENDENCY_REVIEW.md | NO (Sprint 4) | Legal review of plugin licenses before Sprint 4 fork ships |
| VA-11 | INFO | Process clarity | The outbound send_message delivery path (cron/_deliver_result) creates a disablement gap: send_message tool not registered does NOT prevent outbound delivery via cron/gateway paths. This is documented correctly but is the highest operational risk in the "outbound messaging" surface. | EXTERNAL_SURFACE_MAP.md, ACTION_DISPATCH_MAP.md | NO | Sprint 3 must require disablement at all 3 outbound delivery paths |
| VA-12 | INFO | Multi-level delegation recursion | delegate_tool.py can spawn AIAgents that themselves delegate. Classification "approval-required or disabled" may be insufficient — in Magna MVP, multi-level delegation should be DISABLED (not approval-required) to bound recursion risk. | AUTONOMY_ENTRY_POINT_MAP.md entry 8 | NO (Sprint 3) | Sprint 3 governance design should clarify: delegation = DISABLED in MVP |

---

## 3. Severity Summary

| Severity | Count | Items |
|---|---|---|
| CRITICAL | 0 | None |
| HIGH | 0 | None |
| MEDIUM | 3 | VA-07, VA-08, VA-09 |
| LOW | 5 | VA-01, VA-02, VA-03, VA-04, VA-10 |
| INFO | 3 | VA-05, VA-11, VA-12 |

No critical or high-severity issues. Three medium-severity items are all Sprint 3/4
governance design inputs, not Sprint 2 blocking issues.

---

## 4. Required Corrections for Sprint 2 DONE

The following corrections are RECOMMENDED (non-blocking) before marking Sprint 2 DONE:

### RC-01 (VA-01) — Light Curve format alignment
Recommended: Update SPRINT_2_LIGHT_CURVE.md to either:
  (a) Add "Files Inspected" and "Evidence" as explicit section headers, or
  (b) Add a note explaining the structural variation ("This Light Curve uses a different
      section structure than EVIDENCE_TEMPLATE.md due to the audit nature of Sprint 2.
      The required content is present under: Task Metadata, Governance Gates, Validation
      Results.")

### RC-02 (VA-06) — Autonomy count clarification
Recommended: Add a note to AUTONOMY_ENTRY_POINT_MAP.md: "Note: 13 autonomy entry points
are identified. The title references 12 as an approximation."

No other corrections required before Sprint 2 human acceptance review.

---

## 5. What Is NOT a Risk

The following were confirmed absent or correctly handled:

- No Hermes source in magna-enso/ — CONFIRMED absent
- No docs/audit/ created — CONFIRMED absent
- No commits or pushes — CONFIRMED
- No Sprint 3 or Sprint 4 work started — CONFIRMED
- No Hermes run or build — CONFIRMED
- No dependency installation — CONFIRMED
- EH-0005B not promoted — CONFIRMED PROPOSED
- Hermes Agent not activated — CONFIRMED
- No source code pasted into reports — CONFIRMED (no large code blocks)
- magna-enso SHA unchanged — CONFIRMED

---

## 6. Sprint 3 Risk Inputs

The following items from this validation MUST be addressed in Sprint 3 governance design:

1. (VA-07) Define "disabled" enforcement tiers: process-level vs dispatch vs config
2. (VA-08) Design unified approval engine covering all approval_required paths
3. (VA-11) Require disablement at all 3 outbound delivery paths (tool, cron, gateway)
4. (VA-12) Clarify delegation recursion: DISABLED in MVP (not approval-required)
5. (VA-02) Include plugin-level threat modeling in Sprint 3 scope

---

## 7. Sprint 4 Risk Inputs

The following items MUST be addressed before Sprint 4 fork acceptance:

1. (VA-03) Transitive dependency license analysis (mandatory)
2. (VA-04) Independent SBOM scan (recommended)
3. (VA-09) Decision: remove remote execution backends vs disable (remove recommended)
4. (VA-10) Legal review of plugin-level license files
