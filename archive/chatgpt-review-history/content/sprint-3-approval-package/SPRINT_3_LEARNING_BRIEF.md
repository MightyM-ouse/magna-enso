# SPRINT_3_LEARNING_BRIEF.md
# Magna Enso — Sprint 3 Learning Brief
# Type: Local-only approval package (educational)
# Date: 2026-06-17
# Audience: Human owner learning professional software delivery while building Magna.

---

## 1. Why this brief exists

Sprint 3 is where Magna Enso designs its **safety architecture**. This is the most important governance
work in the whole project, so it is worth understanding the principles, not just approving them.

## 2. What capability governance means

A **capability** is anything the system can *do* that has an effect: run a command, write memory, send a
message, call a cloud API, load a plugin, schedule a task. **Capability governance** is the discipline of
deciding, for each capability, **whether it may run, under what conditions, and who must approve it** — and
enforcing that decision at a single, auditable point. It is the difference between "the agent can do things"
and "the agent can do *exactly these* things, *this* way, with *this* approval, and we can prove it."

## 3. Why default-deny matters

> If it is not explicitly allowed, it is denied.

The opposite — default-allow — means every capability anyone forgot to lock down is open. With default-deny,
a forgotten capability is **safe** (denied), not dangerous (open). New capabilities arrive disabled and must
be *promoted* deliberately. This single inversion turns "did we remember to block X?" into "did we
deliberately enable X?" — which is far easier to get right and to audit. (Directly addresses risk R-06.)

## 4. Why external tools cannot be trusted by default

Hermes-derived surfaces (terminal, browser, messaging, cloud, plugins/MCP, remote backends) are powerful
*because* they reach outside the system — which is exactly why they are dangerous. An external tool can:
exfiltrate data, take irreversible real-world actions, or execute attacker-controlled input. So the default
posture for anything with external or persistent side effects is **off** until a human deliberately enables
it within tight bounds. Trust is *earned per capability*, not granted wholesale by adopting a codebase.

## 5. Why policy must cover ALL execution paths, not just the happy path

The Sprint 2 audit's central finding: Hermes has **no single complete chokepoint** — capabilities can be
reached via dispatch, startup, scheduler, gateway, provider, memory, skill, ACP, plugin, and MCP paths. If
policy only guards the obvious "happy path" (e.g. registry dispatch), every other path is an **open back
door**. Professional safety design enumerates *every* entry point and proves each one is gated. A control
that covers 9 of 10 paths provides roughly the security of covering 0 — the attacker uses the 10th.

## 6. Why approval systems must be unified

If terminal approval, file-transfer approval, memory-write approval, and cloud-call approval are each
implemented separately, you get inconsistent rules, duplicated bugs, and gaps. A **unified approval engine**
— one path all sensitive actions flow through — gives you one place to define rules, one audit log, and one
thing to test for bypass-resistance. Consistency is a security property.

## 7. Why "disabled" must be defined clearly

"Disabled" is ambiguous. Disabled *where*? A capability blocked only at dispatch may still be importable,
registrable, or reachable by another path. So Sprint 3 defines **disablement tiers** (process / module /
registration / dispatch / config). The strongest disablement removes the capability from existence
(not loaded, not registered); the weakest merely blocks one call site. You must say which you mean.

## 8. Why Sprint 3 must happen before Sprint 4

You design the safety architecture **before** you build or fork the thing it governs — otherwise you import
ungoverned execution paths and try to bolt safety on afterward (which never fully works). Sprint 3 decides
what is retained, removed, disabled, or gated; Sprint 4 forks *to that design*. Building first and securing
later is how systems ship with back doors.

## 9. How professional teams design safety architecture before implementation

- **Threat-model first:** list capabilities and what could go wrong with each.
- **Default-deny baseline:** start from "nothing runs," then justify each exception.
- **Single chokepoint:** route all sensitive actions through one auditable gate.
- **States, not booleans:** "on/off" is too coarse; use states like read-only, draft-only, approval-required.
- **Reversibility & evidence:** every sensitive action is logged and, where possible, reversible.
- **Validate bypass-resistance:** actively try to reach a capability *around* the gate; if you can, the design fails.
- **Human authority:** a person approves anything material; the system never self-approves.

## 10. The through-line

Sprint 3 converts the Sprint 2 finding ("powerful, but no complete chokepoint") into an enforceable,
default-deny control model — *on paper, first* — so that Sprint 4 can fork onto a foundation that is safe by
construction rather than safe by hope.
