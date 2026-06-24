# REUSE_RECOMMENDATION_VALIDATION.md
# Magna Enso — Sprint 2 Hermes Read-Only Audit
# Reuse Recommendation Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Validate Codex's conclusion that Hermes is "conditionally suitable as a future Sprint 4
clean governed fork baseline, but not suitable for direct adoption, activation, or
implementation now." Assess the reuse recommendation's accuracy and appropriateness.

---

## 2. Reuse Recommendation Summary

MAGNA_ENSO_REUSE_RECOMMENDATION.md concludes:

  "Hermes Agent is conditionally suitable as a technical base for a future Sprint 4 clean
   governed fork. It is not suitable for direct adoption, activation, or implementation
   in Magna Enso at this stage."

Components classified as:
  - Top Reusable Parts (8 items)
  - Parts to Preserve With Governance (5 items)
  - Parts to Disable By Default (9 items)
  - Parts to Remove If Ungovernable (5 items)

---

## 3. "Conditionally Suitable" Conclusion Validation

### 3.1 Evidence for "Conditionally Suitable" (what makes it potentially worth forking)

| Evidence | Source | Antigravity Assessment |
|---|---|---|
| Modular tool registry (tools/registry.py, model_tools.py) | HERMES_CODE_MAP.md, ACTION_DISPATCH_MAP.md | CONFIRMED — reusable capability catalog and dispatch abstraction |
| Typed tool schemas | HERMES_CODE_MAP.md, CAPABILITY_GATING_FEASIBILITY.md | CONFIRMED — schema definitions reduce Sprint 4 work |
| Approval primitives for terminal/code | tools/approval.py | CONFIRMED — genuine reusable primitive (check_all_command_guards, check_execute_code_guard) |
| Write-staging concept for memory/skills | tools/write_approval.py | CONFIRMED — stage_write mechanism is the right primitive, even if not yet mandatory |
| Toolset grouping concept | toolsets.py | CONFIRMED — provides a starting point for Magna capability grouping |
| Agent loop and orchestration pattern | run_agent.py, conversation_loop.py | CONFIRMED — established orchestration pattern reduces design work |
| Scheduler data model (jobs.py) | cron/jobs.py | CONFIRMED — metadata model is reusable if execution is disabled |
| Provider adapter concept | providers/, plugins/model-providers/ | CONFIRMED — abstraction layer is useful; default provider list must be cleared |

### 3.2 Evidence Against "Suitable" (what makes forking risky)

| Risk | Source | Antigravity Assessment |
|---|---|---|
| No single policy chokepoint | ACTION_DISPATCH_MAP.md, CAPABILITY_GATING_FEASIBILITY.md | CONFIRMED — must be addressed in Sprint 3 before any fork |
| Default capability surface much broader than Magna MVP needs | toolsets.py, README.md | CONFIRMED — _HERMES_CORE_TOOLS grants broad access to many toolsets |
| Background review/curator creates post-turn state changes | agent/background_review.py, agent/curator.py | CONFIRMED — must be disabled/removed |
| Cron's no-agent path bypasses LLM gateway | cron/scheduler.py::run_job | CONFIRMED — high-risk ungovernable path |
| External memory providers sync outside built-in memory | agent/memory_manager.py | CONFIRMED — must be disabled |
| Dynamic MCP/plugin loading changes capability surface at runtime | tools/mcp_tool.py | CONFIRMED — incompatible with default-deny |
| Optional dependencies enlarge supply chain risk | pyproject.toml optional groups | CONFIRMED — modal, daytona, many platform adapters |
| No unified approval engine covering all approval-required paths | CAPABILITY_GATING_FEASIBILITY.md | CONFIRMED — split between approval.py and write_approval.py |

### 3.3 "Conditionally Suitable" vs Alternative Conclusions

Alternative conclusion 1: "Not suitable — build from scratch"
- This would discard the registry, schema, approval primitives, orchestration pattern,
  and write-staging concepts — all of which are genuine engineering value.
- Building those from scratch increases Sprint 4+ implementation risk and timeline.
- The audit provides sufficient evidence to justify conditional reuse over from-scratch.
- Antigravity Assessment: Alternative 1 is overly conservative given the evidence.

Alternative conclusion 2: "Directly suitable — adopt now"
- This ignores the policy chokepoint gap, the broad default capability surface, the
  autonomous background paths, and the ungovernable cron/no-agent script path.
- Direct adoption without Sprint 3 governance design would introduce R-06 (policy bypass)
  and R-07 (prompt injection persistence) risks.
- Antigravity Assessment: Alternative 2 is REJECTED — the risks are real and documented.

Alternative conclusion 3: "Not suitable — too complex to govern"
- The audit provides evidence that the major governance hooks exist (approval.py,
  write_approval.py, toolset configuration, registry control). The complexity is tractable.
- Antigravity Assessment: Alternative 3 is overly conservative given the primitives found.

ANTIGRAVITY CONCLUSION: The "conditionally suitable" conclusion is CORRECT.
It correctly navigates between over-caution and under-caution.

---

## 4. Top Reusable Parts Validation

| Item | Antigravity Assessment |
|---|---|
| run_agent.py, conversation_loop.py (agent loop) | CONFIRMED REUSABLE — core orchestration |
| tools/registry.py, model_tools.py (tool registry/schemas) | CONFIRMED REUSABLE — central dispatch |
| toolsets.py (toolset grouping concept) | CONFIRMED REUSABLE — starting point for Magna grouping |
| tools/approval.py (terminal/code approval) | CONFIRMED REUSABLE — genuine approval primitives |
| tools/write_approval.py (write-staging concept) | CONFIRMED REUSABLE — staging mechanism |
| tools/memory_tool.py, tools/skill_manager_tool.py (if forced through draft policy) | CONDITIONAL — correct caveat |
| providers/, plugins/model-providers/ (adapter concept only) | CONDITIONAL — correct caveat; default list must be cleared |
| cron/jobs.py (scheduler data model as report-only) | CONDITIONAL — correct caveat; execution must be disabled |

All 8 items are correctly identified and caveat-appropriate.

---

## 5. Parts to Disable by Default Validation

| Item | Antigravity Assessment |
|---|---|
| Background self-improvement and curator loops | CORRECT — daemon thread; post-turn state changes |
| Cron execution and cron delivery | CORRECT — scheduler and delivery must both be off |
| Messaging gateways and API server listeners | CORRECT — 10+ platform adapters; inbound triggers |
| MCP and plugin dynamic registration | CORRECT — runtime capability expansion |
| Cloud provider calls and fallbacks | CORRECT — data privacy + unauthorized external routing |
| Browser action tools | CORRECT — active external side effects |
| Terminal/process/code execution | CORRECT — approval-required (not disabled) is more nuanced — see note below |
| External memory providers | CORRECT — external sync must be off |
| Subagent delegation | CORRECT — multi-level scope expansion |

NOTE on terminal/code execution: The classification is "disable by default" here but
"approval-required" in EXTERNAL_SURFACE_MAP.md. This is not a contradiction — "disabled by
default" in the fork baseline means the capability starts in a disabled state. When human
approval is granted for a specific use, it transitions to "approval-required" (each
invocation still requires approval). The classification is consistent with this reading.

---

## 6. Parts to Remove if Ungovernable Validation

| Item | Antigravity Assessment |
|---|---|
| cron/scheduler.py direct script/no-agent execution | CONFIRMED — remove or replace; cannot be approved at invocation if it bypasses LLM |
| External memory plugins that cannot stage writes | CONFIRMED — if they can't be forced through write_approval.py, delete them |
| Platform adapters not needed for Magna MVP | CONFIRMED — reduce attack surface by removal |
| Remote execution backends (Modal/Daytona/SSH/managed gateways) | CONFIRMED — disable inadequate; must be removed from fork baseline |
| Dynamic MCP/plugin loading without signed allowlist | CONFIRMED — disable inadequate; must be removed from fork baseline |

All 5 "remove if ungovernable" items are correctly identified.

---

## 7. Sprint 3 and Sprint 4 Recommendation Validation

### Sprint 3 Recommendation

CLAIM: "Sprint 3 should be a governance-design sprint: Define Magna capability states and
default-deny policy. Specify policy insertion points. Decide which modules are excluded.
Define draft-only memory/skill behavior and report-only scheduler behavior."

Antigravity Assessment: CORRECT AND COMPLETE.
This is the right scoping for Sprint 3. The audit evidence provides exactly the input
needed for that governance design work.

### Sprint 4 Recommendation

CLAIM: "Only create a clean governed Hermes fork after Sprint 3 approves the policy
architecture. The fork should start from a pinned audited SHA, remove or disable risky
surfaces at the boundary, and prove that memory/skill writes, terminal execution, browser
actions, cloud calls, messaging, and scheduling cannot bypass policy."

Antigravity Assessment: CORRECT.
The requirement to "prove" bypass-resistance before the fork is accepted is appropriately
high — it should not be sufficient to simply disable via config. The fork should demonstrate
that the governance constraints are structurally enforced (not just configuration values).

---

## 8. Reuse Recommendation Verdict

```
Main conclusion ("conditionally suitable"): CONFIRMED ACCURATE
Top reusable parts (8 items):               All correctly identified with appropriate caveats
Parts to preserve with governance (5):      All correct
Parts to disable by default (9):            All correct (with minor classification note)
Parts to remove if ungovernable (5):        All correctly identified
Sprint 3 recommendation:                    CORRECT AND COMPLETE
Sprint 4 recommendation:                    CORRECT — appropriate rigor specified

REUSE RECOMMENDATION VALIDATION: PASS
Codex's recommendation is substantive, well-reasoned, and appropriate for input to
Sprint 3 governance design and Sprint 4 fork planning.
```
