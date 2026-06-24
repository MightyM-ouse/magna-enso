---
document: technical-specifications/15_RELEASE_BACKUP_AND_ROLLBACK
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Release packaging, backup, rollback for local-first Enso
current_vs_target: Release concepts present; release readiness 25% (target)
date: 2026-06-21
evidence_sources: [10 of evidence-completion; package 13]
change_control: Tags are not releases. Governed; nothing deleted.
---

# Spec 15 — Release, Backup, and Rollback

## Human ToC
1. Purpose/Scope/Non-goals 2. Release packaging (MAG-OPS-004) 3. Backup (MAG-OPS-002) 4. Rollback (MAG-OPS-003)
5. Failure/recovery 6. Acceptance/testing 7. Status/Open 8. Change-control

## AI navigation index
- `release` → §2 · `backup` → §3 · `rollback` → §4

## 1. Purpose/Scope/Non-goals
**Purpose:** low-regret release/backup/rollback locally. **Non-goals:** cloud release pipelines; treating tags
as releases.

## 2. Release packaging (MAG-OPS-004)
A release requires: build artifact + **signed human acceptance** + environment evidence + backup proof.
**Tags do not establish releases** (`10`). Release readiness today = **3/12 (25%)**.

## 3. Backup (MAG-OPS-002)
Local Production: scheduled backup of DB + audit log + config (secrets excluded/secured); UAT: snapshot before
promotion. Restore verified by replay.

## 4. Rollback (MAG-OPS-003)
- Source-control: work on isolated branch; rollback = discard/reset branch; `main` untouched until reviewed
  merge; nothing force-pushed/auto-merged.
- Runtime: restore snapshot + replay from append-only log; resting default-deny; evidence trail retained even
  on rollback.

## 5. Failure / recovery
Failed release ⇒ revert to last accepted; corrupted backup ⇒ DENY new ALLOWs until integrity re-established.

## 6. Acceptance / testing
Acceptance: rollback rehearsed; backup restorable + replay-verified; no tag-as-release. Testing: backup/restore
+ rollback rehearsal (target).

## 7. Status / Open decisions
Status: concepts present; full release/DR `PLANNED`. Open: ADR-R9 env/release topology; OD-13.2 backup
standard.

## 8. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Tags ≠ releases. Governed; nothing deleted.
