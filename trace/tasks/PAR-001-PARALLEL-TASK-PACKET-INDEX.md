# PAR-001 — Parallel Agent Task Packet Index

Status: `PACKET_PREPARATION`
Instruction authority: ChatGPT / System Architect
Product Owner authorization: prepare packets only
Issue: #19

## Purpose

This index records four non-overlapping task packets that may be launched later in parallel while GOV-005 remains under correction. These packets do not authorize execution by themselves. Execution requires a later Product Owner launch prompt for each agent.

## Packets

| Packet | Agent | Assigned branch | Purpose |
|---|---|---|---|
| `trace/tasks/REPO-001-CODEX-INVENTORY.md` | Codex | `codex/REPO-001-inventory-report` | Read-only repository inventory and stale-status detection |
| `trace/tasks/ARCH-001A-CLAUDE-SOURCE-CLASSIFICATION.md` | Claude | `claude/ARCH-001-source-classification` | Architecture source classification from archived materials |
| `trace/tasks/ARCH-001V-ANTIGRAVITY-ARCHIVE-VALIDATION.md` | Antigravity | `antigravity/ARCH-001-archive-validation` | Independent archive/package validation |
| `trace/tasks/HERMES-001-SANDBOX-READINESS.md` | Hermes planning | `hermes/HERMES-001-sandbox-readiness` | Sandbox-readiness design only; no Hermes activation |

## Global constraints

- No direct push to `main`.
- No merge by any worker.
- No modification of GOV-005, GOV-006, PR #13, PR #17, or CF-5 correction surfaces unless explicitly assigned.
- No runtime, HELIX, SGN-01, Hermes activation, Sprint 5, or product behavior changes.
- Every worker must write only to its assigned output paths and return a short chat summary with repository evidence paths.

## Launch state

`NOT_LAUNCHED`

The Product Owner must review these packets before launch prompts are provided.
