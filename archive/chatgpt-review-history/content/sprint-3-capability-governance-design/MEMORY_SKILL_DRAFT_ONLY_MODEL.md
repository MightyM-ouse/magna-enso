# MEMORY_SKILL_DRAFT_ONLY_MODEL.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 7 of 17 — Memory & Skill Draft-Only Model
# Type: Design-only governance report. No code.
# Date: 2026-06-17
# Status: Design only. Human owner is final authority (EH-0010).

---

## 1. Purpose

Define how memory writes (C-03) and skill mutations (C-04) are governed as **`draft_only`** so there is
**no silent memory mutation** and **no auto-skill activation** (R-07, R-08, R-09).

## 2. Model

Every memory/skill write is **staged as a draft** and does not persist or activate until the **human owner
accepts** it. The agent may propose; it may not commit.

```text
agent proposes memory/skill change
        │
        ▼
staged draft (not persisted, not active)  ──► visible to human (diff/preview)
        │
   human decision
   ├─ accept → persist (memory) / activate (skill) → log
   └─ reject → discard draft → log
```

## 3. Hermes binding (@ 33b1d144)

- Memory: `tools/memory_tool.py::memory_tool`, `MemoryStore.save_to_disk`; gate via
  `tools/write_approval.py::stage_write` / `_apply_write_gate` — **must be forced ON and non-bypassable**
  (audit found staging exists but is "configurable and not a guaranteed default").
- Skills: `tools/skill_manager_tool.py::skill_manage` / `_apply_skill_write_gate` — staging forced; no
  autonomous skill creation (audit: `skill_manage` "needs draft-only").
- **External memory mirroring is separate and DISABLED** (C-16): `agent/memory_manager.py::on_memory_write`,
  `sync_all` must not run — drafts never sync externally.

## 4. Rules

1. Default state for memory.write and skill.write = `draft_only` (never `disabled`-blind, never auto-persist).
2. Staging is **mandatory and non-bypassable** — no config makes it optional.
3. **No silent persistence**: a write that is not human-accepted never reaches disk/active state.
4. **No auto-activation**: a staged skill is inert until explicitly activated by the human.
5. **Reversible**: drafts can be discarded; accepted writes are logged for audit/rollback.
6. **External content cannot self-accept**: inbound/web/memory content cannot approve its own persistence (R-07).
7. Every stage/accept/reject is logged (Event Horizon / Light Curve).

## 5. Why draft-only (not disabled, not active)

Memory and skills are *useful* — disabling them entirely would cripple the agent. Letting them auto-persist
is dangerous (prompt-injection persistence, silent drift). `draft_only` keeps the usefulness while making
**human acceptance the only path to persistence** — the safe middle state.

## 6. Boundaries

Design only. The staging mechanism is implemented in Sprint 8 (Memory & Skill Governance), enforced through
the policy gate and unified approval engine.
