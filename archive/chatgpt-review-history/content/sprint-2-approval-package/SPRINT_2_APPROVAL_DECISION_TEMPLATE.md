# SPRINT_2_APPROVAL_DECISION_TEMPLATE.md
# Magna Enso — Sprint 2 Approval Decision Template
# Type: Local-only approval package
# Date: 2026-06-17
# Status: READY FOR HUMAN OWNER. Fill in, then a worker may begin Sprint 2 within these bounds.

---

## 1. The 10 decisions

| # | Decision | Recommendation | Your choice |
|---|---|---|---|
| 1 | Should Sprint 2 start? | **Yes** — read-only audit only | ☐ Approve ☐ Defer ☐ Amend: ____ |
| 2 | Scratch/audit workspace location | `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/` | ☐ Approve ☐ Other: ____ |
| 3 | Create an audit branch? | **No** (reports local-only first; no branch needed) | ☐ No branch ☐ Create `audit/hermes-readonly` |
| 4 | Who performs code inspection? | **Codex** (inspect); **Antigravity** (validate) | ☐ Codex+Antigravity ☐ Other: ____ |
| 5 | Claude governs/reviews only? | **Yes** (no code inspection, no runtime code) | ☐ Yes ☐ Amend: ____ |
| 6 | GitHub remote stays unconfigured? | **Yes** — no remote | ☐ Keep unconfigured ☐ Configure (specify): ____ |
| 7 | No commit / no push remains mandatory? | **Yes** | ☐ Mandatory ☐ Amend: ____ |
| 8 | Sprint 2 output local-only or committed later? | **Local-only first**; commit reports later only by separate decision | ☐ Local-only ☐ Commit reports later ☐ Amend: ____ |
| 9 | Hermes license verification mandatory before Sprint 4? | **Yes** | ☐ Mandatory ☐ Amend: ____ |
| 10 | Antigravity validates Sprint 2 output before acceptance? | **Yes** | ☐ Yes ☐ Amend: ____ |

> Note for Decision 2: please also provide the **Hermes source repository URL** to clone (read-only),
> since the workspace path alone does not specify what to clone.

## 2. Ready-to-sign approval block

```text
I approve Sprint 2 — Hermes Read-Only Audit.

Approved boundaries:
- Read-only clone allowed only in: <MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/
- Hermes source URL (read-only): ____________________
- No fork
- No modification
- No commit
- No push
- No Hermes source copied into magna-enso
- No HELIX modification
- No runtime code
- Reports only
- Stop after audit reports

Worker assignment:
- Inspect: Codex
- Validate: Antigravity
- Govern/review: Claude
- Second opinion: Grok
- Continuity: ChatGPT
- Hermes Agent: NOT used (remains candidate; EH-0005B stays PROPOSED)

Approved by (human owner): ____________________
Date: ____________________
```

## 3. What happens after you sign

1. A worker creates the scratch workspace and read-only clone (records source URL + commit SHA).
2. Codex maps the code; Antigravity flags safety/risk; Claude interprets gateability; Grok challenges.
3. The nine Sprint 2 reports are produced (local-only first).
4. Antigravity validates; `SPRINT_2_LIGHT_CURVE.md` is written.
5. You review the reuse recommendation and accept (or request changes). **Then Sprint 2 stops.**
6. Sprint 3 (governance design) is considered **separately**, later.

## 4. If you do not approve

Nothing happens. The `magna-enso/` baseline stays exactly as committed (`e0a28d4`), Hermes stays
un-cloned, and Sprint 2 remains gated.
