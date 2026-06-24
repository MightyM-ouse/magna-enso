---
document: 01_SOURCE_AND_AUTHORITY_REGISTER
package: magna-enso-architecture-technical-specification-draft
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT — records sources and precedence; decides nothing
scope: Authority precedence, inspected repositories, evidence sources, and access gaps
current_vs_target: Records current verified state of sources as of 2026-06-21
date: 2026-06-21
evidence_sources:
  - Preflight git inspection (this session)
  - magna-program-evidence-completion/EVIDENCE_COMPLETION_INDEX.json
change_control: Superseding changes require a governed decision. Do not delete or silently rewrite.
---

# 01 — Source and Authority Register

## Human table of contents
1. Authority precedence (used throughout)
2. Repositories inspected (preflight)
3. Accepted evidence baseline
4. Preliminary / rejected sources
5. Canonical source map (named docs → current equivalents)
6. Access gaps and could-not-verify items
7. Open decisions
8. Change-control note

## AI navigation index
- `authority_precedence` → §1
- `repos_inspected` → §2
- `evidence_baseline` → §3
- `rejected_sources` → §4
- `source_map` → §5
- `access_gaps` → §6

## 1. Authority precedence (applied in every document)
1. Current human-owner decisions in the task prompt (authoritative).
2. Ratified Magna Constitution and Protected Boundaries Registry.
3. Accepted decisions not superseded by (1).
4. Current source and validated evidence.
5. Canonical project status and trackers.
6. Architecture/planning documents.
7. Agent reports and historical summaries.
Every material conflict is reported as an open decision, never silently resolved.

## 2. Repositories inspected (preflight, 2026-06-21)

| Repository | Path | Branch | HEAD (short) | Working tree |
|---|---|---|---|---|
| Magna Command Center | `<LOCAL_USER_HOME>/Projects/AI/magna-command-center` | `main` | `68981c8` | dirty: ` M .codex/config.toml`, ` M AGENTS.md`, untracked `agent-logs/hermes-magna-v1-feasibility/`, `agent-logs/magna-lite-hermes-capability-governance/` |
| Magna Enso | `<MAGNA_LOCAL_ROOT>/magna-enso` | **`sprint/05-policy-engine`** | `4d5c203` | untracked `policy/`, `tests/`, `trace/evidence/ENSO-0005_LIGHT_CURVE.md` |
| TRACE | `<LOCAL_USER_HOME>/Projects/AI/TRACE` | `main` | `c6b4bbd` | untracked `proposed-governed-loop/` |

> **Material finding (FND-01).** Magna Enso is on branch `sprint/05-policy-engine` (not `main`) with untracked
> `policy/`, `tests/`, and a Sprint 5 Light Curve. The accepted evidence baseline records the *same* state
> (`EVIDENCE_COMPLETION_INDEX.json` shows enso branch `sprint/05-policy-engine` @ `4d5c203`). Therefore this is
> the **verified current state**: Sprint 5 source **exists on an isolated branch**, is **IN_REVIEW**,
> harness-level, **not runtime-integrated, and not accepted**. It is recorded as such — not as "Sprint 5
> done." See `05` and `17` (OD). **No repository was modified by this package.**

## 3. Accepted evidence baseline
`<CHATGPT_REVIEW_SOURCE>/magna-program-evidence-completion/` — reports `00`–`13`,
`EVIDENCE_COMPLETION_INDEX.json`, `raw-command-output/`. Used as the authoritative technical evidence.
Key validations recorded there: Command Center frontend build PASS; backend `701 passed`; router `65/65`;
Enso unittest `49 passed`; **Enso pytest `7 collection errors`**; TRACE backend `6 passed`; TRACE lint PASS;
**TRACE frontend build blocked** (missing installed Rollup optional binary).

## 4. Preliminary / rejected sources
- **Preliminary supporting only:** `magna-program-discovery-reconstruction/` — directionally useful but
  materially corrected by the evidence baseline (authority, BRS status, validation, TRACE effectiveness,
  policy-engine selection). Cited only as supporting context, never as deciding authority.
- **REJECTED as an evidence source:** the Antigravity validation package. **Not used, not cited** anywhere in
  this package, per the human-owner instruction.

## 5. Canonical source map (named docs → current equivalents)
From `02_CANONICAL_MAGNA_DIRECT_READ.md`:

| Requested / blueprint name | Current canonical equivalent |
|---|---|
| Project rules | `AGENTS.md` + `project-knowledge/MAGNA_AGENT_EXECUTION_PROTOCOL.md` |
| Governance | `project-knowledge/AGENT_GOVERNANCE.md` |
| Scope | `project-knowledge/contracts/00_DEPLOYMENT_SCOPE.md` |
| Constitution | `project-knowledge/identity/MAGNA_ARCHITECTURE_CONSTITUTION.md` (Laws I–XII) |
| Protected boundaries | `project-knowledge/identity/PROTECTED_BOUNDARIES_REGISTRY.md` |
| Cosmos | `project-knowledge/identity/THE_COSMOS.md` |
| Identity truth | `project-knowledge/pre-sgn-stabilization/CSF_01_CONSCIOUS_SELF_MODEL_TRUTH_REGISTRY.md` |
| Pre-SGN belt | `project-knowledge/pre-sgn-stabilization/` (HAB/ATM/CSF/BRS/MEM/NRV/SGN layer records) |
| Roadmap/status | `MAGNA_PROJECT_STATUS_AND_NEXT_STEPS.md` (subordinate to belt + source truth) |
| Blueprint | `MAGNA_BLUEPRINT.md` — explicitly a **subordinate compilation**, not deciding authority |

## 6. Access gaps and could-not-verify items
- This package read the **accepted evidence baseline** as its primary canonical input (the prompt designates
  it as the accepted technical evidence). Direct re-reading of every Command Center constitution sub-file was
  **not** re-performed line-by-line in this drafting session; where a fact originates from a specific source
  file, the evidence report that verified it is cited. Items not present in the evidence baseline are marked
  `UNKNOWN` rather than invented.
- TRACE Strategic Blueprint v1.0: assessed via `06_TRACE_COMPLETE_ASSESSMENT.md` (which cites §§35–39, 44).
  The full canonical blueprint text was not re-quoted here; claims about it are attributed to `06`.
- Anything marked `UNKNOWN` or `PROPOSED` in later documents reflects a genuine gap, not a hidden assumption.

## 7. Open decisions
- OD-01.1 — Confirm whether the Sprint 5 isolated branch should remain in place or be quarantined pending the
  independent Sprint 5 security/acceptance review (`05`, `13`).
- OD-01.2 — Confirm the canonical location/version of the TRACE Strategic Blueprint to be frozen as the
  program reference (`12` item 9; `09 spec`).

## 8. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Source/authority changes are governed; superseded entries are marked, not deleted.
No reviewed repository was modified.
