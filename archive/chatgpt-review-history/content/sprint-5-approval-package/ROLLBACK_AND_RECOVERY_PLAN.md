# ROLLBACK_AND_RECOVERY_PLAN.md
# Magna Enso — Sprint 5 Rollback and Recovery Plan
# Type: Local-only approval package
# Date: 2026-06-20
# Status: FOR HUMAN APPROVAL. Sprint 5 NOT started.

---

## 1. Purpose

Define how to undo Sprint 5 cleanly and how the engine recovers from interruption — so approving Sprint 5 is
low-regret. Aligns with EH-0008 (no auto-commit/push; reversible by default) and EH-0012 (branch model).

## 2. Source-control rollback (the work)

- Sprint 5 runs on an **isolated branch** (`sprint/05-policy-engine`); implementation starts from clean
  `main` at `4d5c203cc236be84bd4b9bd8004cb88e8797a34d` and `main` remains untouched until a
  human-reviewed merge.
- `c7bb2b2d695f5ad1ce9c7e22d7dd6f22312c0f46` remains the accepted Sprint 4 baseline commit; PRQ-1 trace
  synchronization at `4d5c203` is the later implementation baseline.
- **Rollback = discard/reset the branch** — no effect on `main`. Nothing is force-pushed; nothing auto-merges.
- Because the engine is **new, additive code** in `policy/` + `tests/policy/` (no modification of existing
  runtime — there is none), removing those directories fully reverts the change.
- The inert `vendor/hermes/` baseline is **not touched** by Sprint 5, so it needs no rollback.

## 3. Rollback conditions (when to revert rather than fix)

| Condition | Action |
|---|---|
| Antigravity finds a **bypass** that cannot be closed within scope | Halt; revert branch; redesign |
| Default-deny cannot be guaranteed (a path can reach a capability un-gated) | Halt; revert; escalate (R-06) |
| The engine requires importing/running Hermes or installing deps to work | Halt; revert; out of scope |
| Scope creep into Sprint 6+ / runtime activation appears | Halt; revert the out-of-scope part |
| License/dependency surprise from any new dependency | Halt; revert; license review |

## 4. Runtime recovery (the engine's own behavior) — see D-8 / FAILURE_MODES §3a

- **Append-only audit log = recovery source of truth.** Decision/approval state is reconstructed from it.
- **Malformed tail recovery:** a partial trailing record (crash mid-append) is detected and truncated/
  quarantined on startup; resting state is default-deny.
- **Corruption detection:** records are hash-chained; a broken chain blocks new ALLOWs and surfaces a hard error.
- **Resting state after any restart = default-deny.** No capability is "remembered as allowed."
- **In-flight HOLDs do not auto-resolve** to ALLOW on restart; **pending approvals are NOT carried across a
  restart** (expiry uses monotonic time, which resets on restart — `FAILURE_MODES` §3aa). A fresh decision via
  the `HumanDecisionProvider` is required (test-only in Sprint 5; absent ⇒ DENY) (F-10, F-11, D-7).
- **Clock rollback / uncertainty** invalidates pending approvals ⇒ DENY; wall-clock is audit evidence only,
  never the expiry authority.
- **Single-use, fingerprint-bound approvals** are marked consumed and cannot be replayed or argument-swapped
  after a crash (complete canonical fingerprint check; T-9, F-9, F-16).
- The engine has **no persistent "enabled" runtime state** that could survive a restart as an open door.
- **Secure audit file required at startup + before use** (`0600`, owner/regular/symlink checks); if the file
  cannot be securely established/verified, initialization fails and the gate DENIES all (`FAILURE_MODES` §3d).
- **Limit (honest):** the audit log is integrity-**detecting**, **not tamper-proof**. Recovery trusts the log
  only insofar as the hash-chain verifies; a local administrator who edits the file (and recomputes the chain)
  is **not** defended against in Sprint 5 (future signed-store decision).

## 5. Data/side-effect rollback

- Sprint 5 performs **no real-world side effects** (no auto-execution) — there is nothing external to undo.
- `draft_only` decisions are **reversible by design** (discard the draft); persistence happens only on human
  approval, which is itself logged and revocable.

## 6. What rollback must preserve

- The TRACE evidence trail (Light Curve, audit log) is **retained** even on rollback — record what happened
  and why it was reverted (an Event Horizon entry if the human decides).
- `R-06` stays OPEN; `EH-0005B` stays PROPOSED; no trace status flipped to DONE on a reverted sprint.

## 7. Boundaries

Plan only. No branch, code, or commit exists; this defines the safety net for the separately-approved
implementation.
