# TERMINAL_CODE_APPROVAL_REQUIRED_MODEL.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 10 of 17 — Terminal & Code Execution Approval-Required Model
# Type: Design-only governance report. No code.
# Date: 2026-06-17
# Status: Design only. Human owner is final authority (EH-0010).

---

## 1. Purpose

Define governance for terminal execution (C-06) and code execution (C-07): the most powerful **retained**
capabilities. State = **`approval_required`, disabled by default**, with every invocation gated and logged.

## 2. Model

```text
terminal/code call → policy gate (state = approval_required, off by default)
        │ (if capability enabled by explicit human policy)
        ▼
unified approval engine → human approves ONE action, scoped → execute once → log
```

If the capability is not explicitly enabled, it is `disabled` (default-deny). Even when enabled, **no
invocation runs without a per-action human approval.**

## 3. Hermes binding (@ 33b1d144)

- `tools/terminal_tool.py::terminal_tool` already calls `tools/approval.py::check_all_command_guards`.
- `tools/code_execution_tool.py::execute_code` already calls `tools/approval.py::check_execute_code_guard`.
- These primitives are reused but **routed into the unified approval engine** — not trusted as independent gates.
- **Bypass paths must be closed** (the audit's key warning): block reaching terminal/code via
  `cron/scheduler.py::run_job` `no_agent` (removed), remote execution backends `tools/environments/*`
  (removed/disabled), gateway runs (`gateway/...` listener off), and agent-owned/ACP paths
  (routed through the same gate, P-04/P-07).

## 4. Rules

1. Default state = `disabled`; enabling requires explicit human policy + Event Horizon entry.
2. When enabled, state = `approval_required` — **every** invocation gated per action.
3. **All bypass paths closed**: no terminal/code via cron no_agent, remote backends, gateway, ACP, or plugin.
4. Long-running/background processes (`tools/process_registry.py`) are `approval_required` and tracked.
5. `side_effect_type = irreversible`, `evidence_required = full`; every run logged with full detail.
6. Network scope is LAN/local only; no remote execution backend.

## 5. Why approval-required (not removed, not active)

Terminal/code are essential for a real agent but are also the highest-impact, often-irreversible
capabilities (R-06). Removing them would gut utility; leaving them active would be reckless. Per-action human
approval with all bypass paths closed is the safe retention model.

## 6. Boundaries

Design only. Enforcement (gate + approval routing + bypass closure) is Sprint 5 (engine) and Sprint 4
(remove bypass paths in the fork). No code in Sprint 3.
