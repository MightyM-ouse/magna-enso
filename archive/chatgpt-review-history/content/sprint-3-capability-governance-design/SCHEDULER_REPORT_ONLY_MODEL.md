# SCHEDULER_REPORT_ONLY_MODEL.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 8 of 17 — Scheduler Report-Only Model
# Type: Design-only governance report. No code.
# Date: 2026-06-17
# Status: Design only. Human owner is final authority (EH-0010).

---

## 1. Purpose

Define how scheduler/background execution (C-13) is governed as **`report_only`**: it may **propose** what
*would* run, but it **never auto-executes** (R-10). The high-risk **direct-script cron path is removed**.

## 2. Model

```text
schedule fires (tick)
        │
        ▼
generate a REPORT/PROPOSAL ("at T, capability X would run with params Y")
        │
        ▼
surface to human  ── approve → route through unified approval engine (one-shot) → run + log
                  └─ ignore  → nothing executes
```

The scheduler produces **metadata/report objects**, not executed jobs. Any actual execution must go through
the normal capability gate + unified approval engine, per action.

## 3. Hermes binding (@ 33b1d144)

- `tools/cronjob_tools.py::cronjob_tool` → may create **draft/report** schedule objects only.
- `cron/scheduler.py::tick` and `run_job` → **execution disabled** (T3); they do not launch agents, scripts,
  provider calls, tools, or delivery.
- `cron/scheduler.py::run_job` **`no_agent` (direct script) path → REMOVED** (T1/T2). The audit classified
  this as "needs removal or approval-required"; for MVP it is removed — running scripts without an LLM and
  without a per-action gate is unacceptable.
- `cron/scheduler.py::_deliver_result` (outbound delivery from scheduler) → **disabled** (see messaging model).

## 4. Rules

1. Default state for scheduler = `report_only`.
2. The scheduler **never** executes a capability directly; it emits proposals.
3. **Direct-script cron (`no_agent`) is removed**, not merely disabled.
4. Any execution resulting from a proposal is a **fresh, per-action** approval (no standing auto-run).
5. Schedules cannot escalate capability level (a scheduled terminal action is still `approval_required`).
6. All proposals and any resulting executions are logged.

## 5. Why report-only

A scheduler that auto-acts is autonomous execution off the human-visible turn — exactly what Magna forbids.
Report-only preserves the usefulness (reminders, proposed routines) while keeping a human in the loop for
every actual effect.

## 6. Boundaries

Design only. The report-only scheduler is implemented in Sprint 9, behind the policy gate.
