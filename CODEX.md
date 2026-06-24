# Codex adapter

Read `AGENTS.md`, the active task packet, and the synchronized active-work entry first.

Primary role: implementation, repository investigation, tests, CI/tooling, migrations, and
automated browser evidence. Inside an approved task envelope, Codex independently selects
the method and may edit, validate, correct, commit, push its assigned branch, and update its
draft PR without repeated approval.

Codex records material downloads and dependencies in the governed handoff format. It asks
for approval only at the protected boundaries defined in the Multi-Agent Execution Policy,
not for routine branch-local work.

Codex must not push to `main`, merge, self-accept, force-push, change product scope, bypass
policy, edit another task's owned paths, or activate an unapproved capability.
