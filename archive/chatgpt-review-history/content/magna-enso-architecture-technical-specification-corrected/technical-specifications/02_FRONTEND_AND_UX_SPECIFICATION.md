---
document: technical-specifications/02_FRONTEND_AND_UX_SPECIFICATION
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Frontend, frozen ten-tab shell, journeys, approval/recovery UX, accessibility & desktop responsiveness
current_vs_target: Shell verified-current (MCC); acceptance baseline target
date: 2026-06-21
evidence_sources: [03,08 of evidence-completion; package 12]
change_control: Ten-tab shell FROZEN. Governed; nothing deleted.
---

# Spec 02 — Frontend and UX

## Human ToC
1. Purpose/Scope/Non-goals 2. Frozen shell & navigation 3. Journeys/Presence/approval/recovery
4. States (loading/empty/error/offline) 5. Accessibility & responsiveness 6. Acceptance/testing
7. Status/Open decisions 8. Change-control

## AI navigation index
- `shell` → §2 (MAG-EXP-001, MAG-UX-001) · `states` → §4 · `a11y` → §5 (MAG-UX-004/005)

## 1. Purpose/Scope/Non-goals
**Purpose:** the user surface for governed command/approval/evidence. **Non-goals:** autonomy controls before
permission architecture approved; mobile; multi-user.

## 2. Frozen shell & navigation (MAG-UX-001) — verified-current (`03`)
Ten tabs, **not** removable/renamable/mergeable/reroutable: Command, Identity, Agents, Memory, Explorer,
Cognition, Cosmos, Help, Settings, System. Navigation: persistent left/tab nav; Presence indicator.
**Interfaces:** UI↔API REST + WebSocket (`apiClient.ts`, `workflowSocket.ts` patterns, reuse).

## 3. Journeys / Presence / approval / recovery (MAG-UX-002)
- **Primary journey:** Command → routing/cognition visibility → governed action → approval/deny → result +
  evidence → history.
- **Presence:** projection only; never implies autonomy.
- **Approval interaction:** explicit human approve-once/deny; shows fingerprint summary (redacted), expiry,
  affected resources; no auto-approve.
- **Active-task & history:** active task panel + collapsed history (reuse MCC).
- **Recovery:** dedicated recovery surface after restart; resting state default-deny.

## 4. States (MAG-UX-003, MAG-UX-006)
Loading, empty, error (normalized via API client), and **offline/degraded** (providers/cloud unavailable ⇒
clear degraded mode; local-first still functions for non-cloud actions). Today these exist **unevenly** in MCC
(`08`) — target requires consistency.

## 5. Accessibility & desktop responsiveness (MAG-UX-004/005/007) — PROPOSED baseline
- PROPOSED: WCAG 2.1 AA target; keyboard-navigable approval flow; defined desktop breakpoints; visual-
  regression baseline; performance budget addressing the 1.85 MB bundle warning. **No current a11y/responsive/
  visual-regression evidence exists** (`08`).

## 6. Acceptance / testing
Acceptance: shell intact (10 tabs); approval flow keyboard-operable; error/empty/offline states present;
bundle within budget; a11y target met. Testing: component + e2e + visual regression (target).

## 7. Status / Open decisions
Status: shell `IMPLEMENTED_VALIDATED` (MCC); acceptance baseline `PLANNED`. Open: OD-12.1 (a11y/responsive/
perf), OD-12.2 (Presence vs approval).

## 8. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. **Shell frozen.** PROPOSED marks unset baselines. Governed; nothing deleted.
