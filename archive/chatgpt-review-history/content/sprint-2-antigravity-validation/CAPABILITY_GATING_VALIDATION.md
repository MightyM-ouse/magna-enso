# CAPABILITY_GATING_VALIDATION.md
# Magna Enso — Sprint 2 Hermes Read-Only Audit
# Capability Gating Feasibility Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Validate Codex's assessment of whether Hermes capabilities can be mapped to Magna Enso
capability states (disabled, read_only, draft_only, report_only, approval_required,
active_safe) and whether the "conditionally governable" conclusion is accurate.

---

## 2. Capability State Mapping Validation

CAPABILITY_GATING_FEASIBILITY.md maps Hermes capabilities to 6 Magna states:

### 2.1 disabled

Claimed mappings: Messaging gateways, external memory, cloud providers, MCP, background
review, cron execution.
Feasibility claim: "High if enforced at registration and startup."

Antigravity Validation:
- Messaging gateways: Correct — must be disabled at gateway launch, not just tool registry
- External memory: Correct — on_memory_write hook and sync_all must be bypassed
- Cloud providers: Correct — provider resolution must fail to an approved local-only provider
- MCP: Correct — dynamic registration must be blocked at startup, not just blacklisted
- Background review: Correct — daemon thread must not be spawned
- Cron execution: Correct — scheduler tick and run_job must not execute (report-only)

FEASIBILITY ASSESSMENT: HIGH — but requires enforcement at startup and registration,
not just at dispatch time. The report correctly flags this multi-layer requirement.

One refinement: "disabled" at startup vs "disabled at dispatch" are different. A capability
that starts but is blocked at dispatch can still consume resources, generate logs, or expose
side-channel state. Sprint 3 should specify whether disablement is at the module/process
level or at the dispatch level.

### 2.2 read_only

Claimed mappings: File reads/search, session search, browser snapshot, web fetch/search
with privacy checks.
Feasibility claim: "Medium-high; browser/web require privacy and navigation limits."

Antigravity Validation:
- File reads: Correct — non-mutating file operations are separable from writes
- Session search: Correct — pure retrieval from local state
- Browser snapshot: Correct — separable from navigation/action in browser_tool.py
- Web fetch/search: Correct — but data exfiltration risk requires a privacy gate

The "medium-high" confidence for browser/web is appropriately conservative.
Browser navigation (even GET requests) can carry authentication tokens, reveal visited
URLs to providers, or trigger server-side logging. A strict read_only gate needs to bound
network destinations as well.

FEASIBILITY ASSESSMENT: MEDIUM-HIGH — correctly calibrated.

### 2.3 draft_only

Claimed mappings: Memory writes, skill writes, file writes/patches.
Feasibility claim: "Medium; tools/write_approval.py supports staging for memory/skills
but must be mandatory."

Antigravity Validation:
The write_approval.py staging mechanism is a genuine reusable primitive. The concern
that it is "configurable and not guaranteed default" is correct. In a governed fork,
the write gate must be:
- Enabled at startup (not opt-in)
- Applied to ALL write paths (including external memory providers and the no-agent cron path)
- Non-bypassable via config (the approval mode must not be settable to "off")

FEASIBILITY ASSESSMENT: MEDIUM — higher than medium only if the fork explicitly makes
the write gate mandatory at all write paths. The report is appropriately conservative.

### 2.4 report_only

Claimed mappings: Cron schedules, background review, curator suggestions.
Feasibility claim: "Medium; execution must be bypassed and replaced by report generation."

Antigravity Validation:
This is the most novel of the Magna capability states. Hermes does not natively support
"report-only" as a mode — the cron scheduler runs jobs, it doesn't just report them.
Implementing report-only requires either:
(a) Replacing cron/scheduler.py::tick/run_job with a metadata-generation path, or
(b) Stubbing the execution side while preserving the schedule metadata model

The cron/jobs.py job metadata model (cited in MAGNA_ENSO_REUSE_RECOMMENDATION.md as
"reusable as report-only reference") is a correct identification of what can be preserved.

FEASIBILITY ASSESSMENT: MEDIUM — correctly calibrated. The implementation effort for
report_only is higher than disabled because the data model must be preserved while
execution is stripped.

### 2.5 approval_required

Claimed mappings: Terminal, process, execute_code, browser actions, file transfer,
cloud model calls, messaging.
Feasibility claim: "Medium-high; terminal/code already have approval primitives, but
policy must cover all paths."

Antigravity Validation:
The existing tools/approval.py provides:
- check_all_command_guards (terminal)
- check_execute_code_guard (code execution)

These are genuine governance primitives. The caveats are:
- Approval state must be non-bypassable via cron/no-agent script paths
- Gateway-triggered runs must also go through the same approval chain
- Cloud model calls do not currently have an approval.py equivalent

FEASIBILITY ASSESSMENT: MEDIUM-HIGH — correct. The main risk is that approval gates
are scattered (tools/approval.py for terminal/code; write_approval.py for memory/skills)
with no unified approval engine. Sprint 3 must design a unified approval engine that
covers all approval_required surfaces through a single auditable decision path.

### 2.6 active_safe

Claimed mappings: Local status, non-mutating UI state, clarify, selected task metadata.
Feasibility claim: "High, but should remain narrow."

Antigravity Validation:
CORRECT. "Active safe" should be reserved for capabilities with no external side effects
and no persistent state changes. Status queries, UI state reads, and clarification prompts
qualify. Any capability that reads external data (even web fetch) should not be active_safe.

FEASIBILITY ASSESSMENT: HIGH — correctly identified as a narrow category.

---

## 3. Central Chokepoint Assessment Validation

CLAIM: "There is no single complete policy chokepoint because memory/delegation/session
tools, cron scripts, gateways, ACP tools, plugin/MCP registration, and background review
have additional paths."

VALIDATION:
This claim is CONFIRMED by cross-referencing with ACTION_DISPATCH_MAP.md and
AUTONOMY_ENTRY_POINT_MAP.md:
- agent-loop tools bypass registry: CONFIRMED (model_tools.py _AGENT_LOOP_TOOLS)
- cron direct script path bypasses LLM: CONFIRMED (cron/scheduler.py no_agent)
- gateway creates runs independently: CONFIRMED (api_server.py)
- ACP tools map independently: CONFIRMED (acp_adapter/tools.py)
- background review is a daemon: CONFIRMED (background_review.py spawn)
- MCP registration can change runtime surface: CONFIRMED (mcp_tool.py)

The required multi-point policy layer identified in CAPABILITY_GATING_FEASIBILITY.md
matches the required chokepoints from ACTION_DISPATCH_MAP.md. The reports are CONSISTENT
with each other.

---

## 4. "Conditionally Governable" Conclusion Validation

CLAIM: "Hermes is conditionally governable."

ANTIGRAVITY ASSESSMENT: CONFIRMED ACCURATE.

Supporting evidence:
- Hermes HAS: tool registry, toolset grouping, approval.py primitives, write_approval.py
  staging, typed schemas — all are reusable governance foundations
- Hermes LACKS: unified policy engine, single approval audit log, mandatory write gates,
  default-disable for all high-risk surfaces
- The gap is substantial but bridgeable — it requires Sprint 3 governance design work
  before Sprint 4 fork

The "conditional" qualifier is essential and must not be dropped or weakened.

Counter-risk assessment (what would make Hermes ungovernable):
- If ACP tools or background review paths cannot be completely disabled without breaking
  core functionality → governance would require removing those modules entirely
- If plugin/MCP dynamic loading cannot be blocked without replacing the plugin system →
  the entire plugin architecture may need to be stripped
Neither of these is confirmed by the audit, but they are correctly flagged as Sprint 3
design risks.

---

## 5. Open Questions Forwarded to Sprint 3

The following open questions from CAPABILITY_GATING_FEASIBILITY.md must be addressed
in Sprint 3 governance design:
1. Should Magna enforce policy through a new central capability engine before importing
   tool modules? (Recommended: YES — process-level enforcement is stronger)
2. Should active toolsets be generated from Magna policy instead of Hermes config?
   (Recommended: YES — policy-first toolset generation)
3. Should all dynamic plugin/MCP loading be removed from the first fork baseline?
   (Recommended: YES — dynamic loading is incompatible with default-deny in MVP)

These are confirmed as the right questions. They are Sprint 3 scope, not Sprint 2 gaps.

---

## 6. Capability Gating Verdict

```
6-state Magna mapping:     VALIDATED — all 6 states correctly mapped
Chokepoint gap finding:    CONFIRMED — registry dispatch alone is insufficient
"Conditionally governable" conclusion: CONFIRMED ACCURATE
Feasibility confidence ratings: All correctly calibrated (High/Medium-High/Medium)
Sprint 3 open questions:   Correctly identified and forwarded

CAPABILITY GATING VALIDATION: PASS
This is the central finding that drives Sprint 3 scope.
The assessment is substantive, accurate, and appropriately conservative.
```
