# Magna Version Enso — Technical Specification and Integration Assessment Scope

Status: future technical assessment scope  
Depends on: formal Product Owner approval of Magna-Hermes Runtime Adoption user stories  
Related planning brief: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

---

## 1. Purpose

This document defines the future technical assessment scope for the first integrated version of Magna:

```text
Magna version enso
```

The goal is to assess whether selected capabilities from Hermes Agent can be adopted into the Magna product experience while preserving Magna governance, TRACE traceability, local-first control, user approval authority, and the Magna Command Center surface.

This file is not the final technical specification. It is the assessment scope that should guide the technical specification after the product user stories are created and approved.

---

## 2. Repositories to assess

### 2.1 Hermes Agent

Repository:

```text
https://github.com/NousResearch/hermes-agent
```

Assessment purpose:

```text
Determine which Hermes runtime capabilities can be adopted, adapted, wrapped with governance, rebuilt in Magna, rejected, or deferred.
```

Capability areas to inspect:

```text
- Terminal execution
- Messaging gateway
- Telegram/WhatsApp support
- Memory
- Skills/self-improvement
- Profiles
- Scheduler/cron
- Delegation/subagents
- MCP/tool integrations
- Command approval and safety controls
- Execution capture/logging
```

### 2.2 Magna Command Center

Repository:

```text
https://github.com/MightyM-ouse/magna-command-center
```

Assessment purpose:

```text
Determine how the Magna user-facing command surface, shell, navigation, identity, and runtime status experience should expose Hermes-backed capabilities without breaking the Magna product identity.
```

Capability areas to inspect:

```text
- Command surface
- Identity/presence display
- Runtime status display
- Notifications and approval UI
- Capability Control UI fit
- Evidence/review package visibility
- Mobile/remote command UX implications
```

### 2.3 Magna Enso

Repository:

```text
https://github.com/MightyM-ouse/magna-enso
```

Assessment purpose:

```text
Determine how Magna Enso should act as the governance, orchestration, TRACE, and evidence authority for Hermes-backed runtime actions.
```

Capability areas to inspect:

```text
- TRACE lifecycle
- GitHub evidence updates
- Agent routing and response contract
- Task ownership and active work registry
- Approval model
- Worker dispatch model
- Review package creation
- Local-first constraints
```

---

## 3. Branding and identity dependency

Related PR:

```text
#33 — Add MAG-US-001 animated Magna identity story
```

Assessment requirement:

```text
Magna version enso must include the approved Magna identity direction from PR #33 as a product dependency.
```

The technical specification must decide how the animated Magna identity story affects:

```text
- App launch and loading surface
- Runtime command state
- Thinking/working state
- Notifications
- Remote task status summaries
- Reduced-motion fallback
- Internal distinction between Magna as product identity and Hermes as runtime provider
```

---

## 4. Required assessment outputs

The future technical assessment should produce:

```text
1. Hermes capability inventory
2. Magna compatibility matrix
3. Adopt/adapt/wrap/rebuild/reject/defer decision matrix
4. Runtime architecture proposal
5. Safety and approval model
6. TRACE lifecycle mapping
7. GitHub evidence/update strategy
8. CLI worker dispatch model
9. Messaging gateway strategy
10. Magna Command Center UI integration notes
11. First-version scope for Magna version enso
12. Explicit non-goals and blocked capabilities
```

---

## 5. Decision matrix format

Each Hermes capability should be classified as one of:

```text
ADOPT:
Use substantially as provided.

ADAPT:
Modify behavior or integration surface before use.

WRAP_WITH_GOVERNANCE:
Use Hermes capability only behind Magna/TRACE controls.

REBUILD_IN_MAGNA:
Use Hermes as reference only; implement natively in Magna.

REJECT:
Do not use because it conflicts with safety, scope, or architecture.

DEFER:
Useful later, but not part of Magna version enso.
```

---

## 6. Safety boundaries to preserve

The technical specification must preserve these boundaries:

```text
- Product Owner remains final authority.
- GitHub remains durable source of instruction/evidence state.
- TRACE is mandatory for all governed work.
- Unknown actions pause.
- High-risk actions require approval.
- Terminal access must go through approved wrappers.
- CLI workers must be bounded to assigned tasks and branches.
- Self-improvement, memory writes, skills updates, scheduling, MCP access, and external messaging must be governed.
- Hermes profiles must not be treated as security sandboxes.
- Magna UI/identity must not be replaced by Hermes UI/identity.
```

---

## 7. Initial version boundary

Magna version enso should initially prove the controlled loop:

```text
User instruction
→ ChatGPT system-architect instruction in GitHub
→ Telegram or approved-channel command
→ Magna/Hermes command intake
→ known-instruction matching
→ safety classification
→ approved CLI worker dispatch
→ worker result capture
→ GitHub evidence/assessment update
→ user notification
→ approval or redirection
→ TRACE-compliant continuation or closure
```

Anything outside this loop should be treated as later scope unless explicitly approved by the Product Owner.
