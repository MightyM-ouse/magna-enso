# SPRINT_3_RISK_AND_GOVERNANCE_CHECKLIST.md
# Magna Enso — Sprint 3 Risk and Governance Checklist
# Type: Local-only approval package
# Date: 2026-06-17
# Status: Gates that MUST hold throughout Sprint 3.

---

## 1. Governance gates (must all stay TRUE for the whole sprint)

- [ ] Design-only — no executable code, no policy-engine/UI/scheduler implementation.
- [ ] No modifying, cloning, building, running, or installing Hermes (or dependencies).
- [ ] No Hermes source copied into `magna-enso/` (reports cite identifiers/paths + SHA `33b1d144` only).
- [ ] No commits, no pushes, no new branches (without separate explicit approval).
- [ ] No Sprint 4 work started.
- [ ] EH-0005B remains PROPOSED; Hermes Agent not activated.
- [ ] Default-deny is the baseline of every model produced.
- [ ] Human owner remains final authority; Antigravity validates before acceptance.

## 2. Risks engaged by Sprint 3 (from the Risk Register)

| Risk | Relevance to Sprint 3 | How the design addresses it |
|---|---|---|
| R-01 Hermes reuse/coupling (OPEN) | Design decides retain/remove postures | Per-surface posture; remove worst offenders; minimal retained surface |
| R-02 License/dependency/ToS (OPEN) | Plugin/MCP/provider dependencies | Plugin/MCP disabled unless signed allowlist; providers disabled (full dep review still future) |
| R-04 Cloud/provider creep | Cloud calls | Cloud providers disabled by default (T2) |
| R-05 Public exposure | API listener / messaging | Listener & gateways process-disabled (T1) — nothing network-reachable by default |
| R-06 Policy bypass (OPEN, CRITICAL) | The core Sprint 2 finding | Chokepoint map covers ALL paths; remove paths that can't be gated; bypass-resistance gate |
| R-07 Prompt-injection persistence | Memory/instruction paths | Memory writes draft_only; external memory disabled/staged |
| R-08 Silent memory mutation | Memory writes | draft_only + human acceptance + logging; no silent persist |
| R-09 Auto-skill activation | Skill writes | Skill writes draft_only; no auto-activation |
| R-10 Scheduler drift | Scheduler | report_only model; never auto-executes |
| R-13 Overengineering | Design could sprawl | Bounded to 15 deliverables + readiness gates; MVP postures |

## 3. New Sprint-3-specific risks to watch

| ID | Risk | Mitigation |
|---|---|---|
| S3-W1 | "Design" quietly becomes implementation | Design-only gate; reviewer checks no executable code produced |
| S3-W2 | A capability path left unmapped (bypass) | Chokepoint map must enumerate ALL paths; bypass-resistance argument required |
| S3-W3 | "Disabled" specified vaguely | Every `disabled` capability must name its disablement tier |
| S3-W4 | Over-trusting dispatch-only blocking | Strongest-feasible tier (remove/process/module) for high-risk surfaces |
| S3-W5 | Schema sketch mistaken for working engine | Sketches labeled "design artifact, not code"; not wired to anything |
| S3-W6 | Scope creep into Sprint 4 retain/remove *code* | Sprint 3 defines postures; Sprint 4 implements, separately approved |

## 4. Stop conditions (halt and escalate to human)

- A high-risk surface cannot be gated or removed (serious R-06 implication).
- The design would require running/modifying/forking Hermes to proceed.
- Pressure to begin Sprint 4, write runtime code, promote EH-0005B, or activate Hermes Agent.
- A dependency/license issue surfaces that blocks a retained surface.

## 5. Acceptance gate

Sprint 3 is accepted **only** when: all design reports exist and answer the 10 Sprint 4 readiness gates,
Antigravity validation passes (default-deny coverage + bypass-resistance + no scope creep), the
`SPRINT_3_LIGHT_CURVE.md` is written, and the **human owner signs off**. No worker self-approves.
