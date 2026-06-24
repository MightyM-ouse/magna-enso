# RISKS_GAPS_AND_CORRECTIONS.md
# Magna Enso — Sprint 3 Capability Governance Design
# Risks, Gaps, and Corrections
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Enumerate all risks, gaps, and required or recommended corrections found during the
Sprint 3 validation. Provide severity ratings and action guidance.

---

## 2. Issues Register

| ID | Severity | Type | Description | Blocking? | Required Action |
|---|---|---|---|---|---|
| VN-01 | MEDIUM | Design ambiguity | C-01 (local_read) has dual default state "active_safe / read_only" in CAPABILITY_TAXONOMY.md. Status queries should be active_safe; file reads and session search should be read_only. Ambiguous specification may cause Sprint 4 implementation to default incorrectly. | NO | Recommend splitting C-01 into C-01a (local_safe_status_read → active_safe) and C-01b (local_sensitive_read → read_only) before Sprint 4 fork uses taxonomy as build spec |
| VN-02 | LOW | Documentation ambiguity | C-10 (web_network_access) default state listed as "read_only w/ privacy gate / disabled" in taxonomy header. BROWSER_WEB_READ_ONLY_MODEL.md correctly resolves to disabled for MVP. The taxonomy is slightly misleading. | NO | Add footnote to C-10: "MVP default: disabled. read_only with privacy gate is future state; privacy gate does not yet exist in Sprint 4." |
| VN-03 | LOW | Section naming deviation | CAPABILITY_TAXONOMY.md does not have an explicit "## Boundaries" section. Uses "## 5. Design rules" and "## 6. Output usage" instead. All boundary-equivalent content is present. | NO | Add a "## 7. Boundaries" section or rename §5/§6 for template consistency |
| VN-04 | LOW | Taxonomy overlap | C-02 (local_write) and C-05 (file_mutation) overlap significantly — both cover writing local files. C-05 adds "ACP edit approval" as a distinguishing context. The distinction is functional but not crisp. | NO | Sharpen C-02 vs C-05 distinction: propose C-02 = agent-direct writes (no ACP); C-05 = ACP/edit-gated writes with different governance path |
| VN-05 | LOW | Surface model gap | BROWSER_WEB_READ_ONLY_MODEL.md §6 says "Browser/web governance is implemented when those capabilities are introduced (post-baseline)." However, browser snapshot (read_only) is listed as a retained Sprint 4 surface in the matrix. The implementation sprint should be clarified: Sprint 4 retains and gates browser snapshot; later sprint enables action/web capabilities. | NO | Clarify §6: Sprint 4 retains browser_snapshot (read_only); browser actions and web access are post-baseline capabilities enabled in a later sprint |
| VN-06 | LOW | Blocking rule in SPRINT_4_READINESS_GATES | §4 states: "Sprint 4 must not start until G-04…G-17 are satisfied." This is correct but the wording could be clearer that G-04…G-14 are per-model human acceptances, not a single aggregate acceptance. The design is correct; the presentation could be misread as requiring only one acceptance. | NO | Add: "G-04 through G-14 each require individual explicit human acceptance of the named model — not a single aggregate Sprint 3 acceptance." |
| VN-07 | INFO | Pre-Sprint-5 policy engine gap | CAPABILITY_POLICY_SCHEMA.md and DEFAULT_DENY_MODEL.md define the policy engine as a Sprint 5+ artifact. Sprint 4 (fork baseline) predates the policy engine. The Sprint 4 fork will operate without a runtime policy engine — relying on T1-T3 disablement as its primary safety layer. This is correct but should be explicitly documented in the fork design. | NO | Sprint 4 design specification should state: "Sprint 4 fork operates under T1-T3 disablement-only governance. The Sprint 5 policy engine is the future runtime governance layer. Sprint 4 must prove bypass-resistance without the engine." |
| VN-08 | INFO | Cloud providers future state | Cloud providers are listed with future state "approval_required (maybe)." This is the only surface whose future path is marked with "(maybe)." The ambiguity is acceptable for MVP design but should be resolved as an explicit decision before any cloud capability is contemplated. | NO | Future sprint: explicitly decide whether cloud providers will ever be approval_required or remain permanently disabled in Magna |
| VN-09 | INFO | Background review future state | Background review listed as future state "report_only (maybe)." The "(maybe)" qualifier is appropriate for MVP design. However, background self-improvement is the highest-autonomy surface in Hermes; even report-only requires careful design. | NO | If background review is ever reconsidered, require a separate full governance design sprint with human approval before any state change |
| VN-10 | INFO | Skill write no-auto-activation rule | MEMORY_SKILL_DRAFT_ONLY_MODEL.md correctly states "no auto-activation" for skills. The HERMES_SURFACE_GOVERNANCE_MATRIX.md row for skill writes says "force staging; no auto-activation." This is consistent. However, skill activation is a capability state change (from staged → active), which should itself go through the unified approval engine — not just the staging gate. | NO | Ensure Sprint 4 design specifies: skill activation (not just staging) routes through unified approval engine as an explicit approve_once event |

---

## 3. Severity Summary

| Severity | Count | Items |
|---|---|---|
| CRITICAL | 0 | None |
| HIGH | 0 | None |
| MEDIUM | 1 | VN-01 (local_read dual state) |
| LOW | 5 | VN-02, VN-03, VN-04, VN-05, VN-06 |
| INFO | 4 | VN-07, VN-08, VN-09, VN-10 |

No critical or high-severity issues. The single medium item (VN-01) is a documentation
ambiguity that should be resolved before Sprint 4 uses the taxonomy — but does not block
Sprint 3 human acceptance review.

---

## 4. Required Corrections for Sprint 3 DONE (Recommended, Not Blocking)

All corrections are recommended but none are blocking:

RC-01 (VN-01): Split C-01 into C-01a and C-01b in CAPABILITY_TAXONOMY.md.
RC-02 (VN-02): Add MVP default clarification footnote to C-10 in CAPABILITY_TAXONOMY.md.
RC-03 (VN-03): Add or rename section for explicit "Boundaries" in CAPABILITY_TAXONOMY.md.
RC-04 (VN-05): Clarify BROWSER_WEB_READ_ONLY_MODEL.md §6 implementation sprint reference.
RC-05 (VN-06): Clarify SPRINT_4_READINESS_GATES.md §4 to explicitly state per-model acceptance.

Corrections RC-01 through RC-05 may be applied before or concurrently with Sprint 3
human acceptance review. They do not require a new validation cycle if the changes are
limited to the items above.

---

## 5. Sprint 4 Risk Inputs

The following items must be addressed in Sprint 4 design specification (not corrections,
but forward requirements):

1. (VN-07) Sprint 4 fork design must document that it operates under T1-T3 disablement
   only (no policy engine until Sprint 5). Must prove bypass-resistance structurally.
2. (VN-10) Skill activation must route through unified approval engine as an explicit
   approve_once event — not just the draft staging gate.

---

## 6. Items That Are NOT Issues

The following were scrutinized and confirmed non-issues:

- "import" in DISABLEMENT_TIERS_MODEL.md and POLICY_CHOKEPOINT_MAP.md: These are
  references to "module import disabled" and provider "import" as a governance mechanism —
  not Python import statements. No executable code.
- YAML in CAPABILITY_POLICY_SCHEMA.md: Explicitly labeled "SKETCH ONLY — not executed."
  No runtime behavior. Correct use of YAML for design artifact illustration.
- "active_safe / read_only" dual default in C-01: Raised as VN-01. Safe-by-default in
  either reading (neither allows mutation or external access). Not a safety issue.
- DEFAULT_DENY_MODEL.md uses "## 1. Principle" not "## 1. Purpose": Equivalent; content
  is complete. Not a structural issue.
- SPRINT_3_LIGHT_CURVE.md does not have a "Boundaries" section: Light Curve format uses
  evidence-package structure; all required content present. Not a structural issue.
- FINAL_RECOMMENDATION.md does not have Purpose/Boundaries sections: Uses recommendation
  box format; all required content present. Not a structural issue.

---

## 7. What Was Confirmed Absent (All Required Absent Items)

- No critical or high-severity issues: CONFIRMED
- No code in any of 17 reports: CONFIRMED
- No Hermes source copied: CONFIRMED (identifier citations only)
- No Sprint 4 started: CONFIRMED
- No EH-0005B promotion: CONFIRMED
- No commits/pushes: CONFIRMED
- magna-enso unchanged: CONFIRMED (SHA 94d63ed; clean status)
