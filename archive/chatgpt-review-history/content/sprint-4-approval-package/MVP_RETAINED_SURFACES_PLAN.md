# MVP_RETAINED_SURFACES_PLAN.md
# Magna Enso — MVP Retained Surfaces Plan
# Type: Local-only approval package
# Date: 2026-06-17
# Status: PROPOSAL for human approval. No surface imported/activated now.

---

## 1. Purpose

Define the minimal set of surfaces the MVP baseline would **retain**, and the **state** each is allowed —
the import allowlist for Option C. Everything not listed here is removed/disabled.

## 2. Retained surfaces and allowed states

| Surface | Allowed state | Notes |
|---|---|---|
| Local safe status read | `active_safe` | Health/status metadata, capability/project status labels; no file/session/user data (C-01a) |
| Local sensitive read | `read_only` | File reads, session search, memory inspection; audit-visible; no mutation (C-01b) |
| Project metadata / status | `active_safe` | Non-sensitive status surfaces |
| Memory write | `draft_only` **only** | Staged; persists only on human acceptance; external sync removed |
| Skill write | `draft_only` **only** | Staged; no auto-activation |
| Scheduler metadata | `report_only` **only** | Schedules as report objects; no execution; direct-script cron removed |
| Browser snapshot | `read_only` **only if privacy-gated** | Snapshot/observe only; actions disabled; off until privacy gate exists |
| Terminal / code | `approval_required` **but DISABLED until policy engine exists** | Retained as source; not wired to run; gate is Sprint 5 |

## 3. Supporting/retained infrastructure (non-capability)

To make the above usable later, the baseline may also retain (behind no active execution):
- Agent loop & orchestration pattern (`run_agent.py`, `agent/conversation_loop.py`, `agent/tool_executor.py`).
- Tool registry (`tools/registry.py`) — with import-time self-registration **severed/controlled**.
- Approval & write-staging primitives (`tools/approval.py`, `tools/write_approval.py`) — reused later by the
  unified approval engine, not trusted as standalone gates.

(Exact file-level inventory is produced as Sprint 4's first task: `SOURCE_IMPORT_INVENTORY.md`.)

## 3a. Retained source is quarantined (C-03)

Even retained surfaces are imported as **inert / quarantined** source in Sprint 4 — present but unable to act:
- not wired into runtime; not imported by application code; not exposed through CLI/UI;
- not executable; not registered as tools; not package-discovered as active code.

Retained = "kept as governed reference for later wiring," **not** "available now." The states in §2
(read_only / draft_only / report_only / approval_required-but-off) describe the *intended* posture once the
Sprint 5 policy engine wires them in — they are recorded as metadata in Sprint 4, not made live.

## 4. Hard constraints on retained surfaces

- **Terminal/code stay OFF** in the baseline (no execution) until the Sprint 5 policy engine exists.
- **Memory/skill are draft-only** — never auto-persist; external sync removed.
- **Scheduler is report-only** — never executes.
- **Browser** retained as snapshot/read-only only, and only if a privacy gate is in place; otherwise disabled.
- No retained surface is **wired to run** in Sprint 4; states are recorded as metadata/docs, not enforced.

## 5. Why this minimal set

These are the surfaces with genuine MVP value whose risk can be bounded by a **non-running** posture
(read-only, draft-only, report-only, or off). Everything with external reach or autonomous behavior is
removed/disabled (see removal plan + remove/disable matrix). The result is a baseline that is useful to build
on yet incapable of acting.

## 6. Boundaries

Plan only. No surface is imported or activated by this package. Retained import + state recording happens in
Sprint 4 (Option C), validated by Antigravity; activation/enforcement is Sprint 5+.
