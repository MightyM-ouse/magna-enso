# 07 — Capability & Hermes Adoption Inventory

> **Planned Hermes capabilities must not be described as active.** Evidence below shows
> **zero** Hermes capabilities are active. Only an inert provenance baseline exists.

## 1. Hermes source identity & provenance

| Field | Value | Evidence |
|---|---|---|
| Upstream repo | `https://github.com/NousResearch/Hermes-Agent` | `vendor/hermes/README.md`, provenance files |
| Audited SHA | `33b1d144590a211100f42aa911fd7f91ba031507` | EH-0013, STAR_MAP, README |
| License | MIT (preserved as `UPSTREAM_LICENSE.txt`) | vendor README |
| Upstream description | npm manifest: *"AI agent with advanced tool-calling… flexible toolsets"* (v1.0.0); pyproject: *"The self-improving AI agent — creates skills from experience, improves them during use, runs anywhere"* (v0.16.0) | `provenance/UPSTREAM_PACKAGE.json.source.txt`, `UPSTREAM_PYPROJECT.toml.source.txt` |
| Upstream surface (from manifests) | npm workspaces `apps/*`, `ui-tui`, `web`; postinstall mentions **browser tools**; Python deps exact-pinned (security-hardened after "Mini Shai-Hulud" PyPI worm); `agent-browser` dep | provenance manifests |

> Minor provenance note: the npm manifest (v1.0.0) and pyproject (v0.16.0) carry
> different version numbers and descriptions for the same audited SHA — a dual-package
> repo. Not a contradiction, but worth recording.

## 2. Adoption state — what is physically present

`vendor/hermes/` contains **only inert artifacts**:
- `UPSTREAM_LICENSE.txt`
- `provenance/UPSTREAM_PYPROJECT.toml.source.txt`, `UPSTREAM_PACKAGE.json.source.txt`
- `retained/RETAINED_SURFACE_STATES.yaml`, `retained/README.md`

Per `vendor/hermes/README.md`, the baseline is **not imported, not wired to runtime,
not CLI/UI-exposed, not executable, not tool-registered, not package-discovered**, and
is **"not evidence that runtime policy enforcement exists."** No executable Hermes
module, Node package, entry point, gateway, plugin, MCP loader, browser action,
terminal/code path, scheduler path, messaging surface, cloud provider, or memory-sync
module is imported.

## 3. Capability-by-capability inventory

| Hermes capability (candidate) | Business value for Magna | Target stage | State | Source imported? | Risk class | Approval required | Impl/test evidence |
|---|---|---|---|---|---|---|---|
| Terminal / code execution | Local automation | Enso (governed) | **PLANNED / design-only** ("approval-required" per S3) | No | High (RCE) | Yes (human) | None active |
| Browser actions (`agent-browser`) | Web read/automation | Enso+ | **PLANNED** ("read-only" per S3) | No | High (network) | Yes | None |
| Messaging surfaces | Notifications/comms | Later stage | **DISABLED by design** (S3) | No | High | Yes | None |
| Agent / tool-calling | Core orchestration | Enso | **DESIGN-ONLY** (taxonomy + chokepoint map S3) | No | Med-High | Yes | None |
| Memory (self-improving skills) | Durable memory | Enso S8 | **PLANNED** (no silent mutation; draft-only) | No | High | Yes | None |
| Plugin / MCP loader | Extensibility | Enso | **DESIGN-ONLY** (plugin/MCP governance S3) | No | High | Yes | None |
| Scheduler | Timed proposals | Enso S9 | **PLANNED report-only** (never auto-exec) | No | Med | Yes | None |
| Cloud providers | Remote models | Deferred | **DISABLED by default** | No | High | Yes | None |
| Autonomy / delegation | Multi-agent | Bodhi+ | **DEFERRED** (delegation recursion control designed S3) | No | High | Yes | None |

**Net Hermes activation: 0 / 9 capability classes active.** All are *retained as design
intent* or *explicitly disabled*; the only "retained surface" is metadata in
`RETAINED_SURFACE_STATES.yaml`, not running code.

## 4. Adoption governance trail (decisions)

- `EH-0005A` (ACCEPTED): Hermes is the **candidate technical base**, pending audit +
  governance design. *Direction accepted; suitability still to be validated.*
- `EH-0013` (ACCEPTED): audit done; Hermes **"conditionally suitable only"**; **not
  approved** for adoption/activation/build/run/fork/implementation.
- `EH-0014` (ACCEPTED): Sprint-3 capability governance design (17 reports) accepted as
  **design/report-only**; no implementation approved.
- `EH-0015` (ACCEPTED): Sprint-4 inert baseline accepted; **R-06 remains OPEN** because
  runtime enforcement does not exist; no activation; Sprint 5 not authorized by it.
- `EH-0005B` (PROPOSED): "Hermes Agent" as a **candidate UI/E2E test worker** — distinct
  from the runtime base. Still proposed; an approved E2E driver may substitute.

## 5. How Hermes capabilities may evolve across stages (designed intent)

Per worker model §5 and roadmap: capabilities are introduced **behind the policy gate,
default-deny, with reversibility and evidence**, starting in Enso (governed, approval-
gated) and only gaining autonomy in Bodhi+ "within explicit policy envelopes." No
capability is meant to outrun governance maturity.

## 6. Canonical-statement reconciliation

Your statement #6 ("Enso **adopts** carefully selected Hermes capabilities… constrained
to approved purposes") describes the **intended design**. Present reality: **nothing is
adopted/active** — there is only an inert baseline and approved *design*. Statement #7
("Hermes-derived capabilities may continue evolving through later stages") matches the
designed intent but is **not yet exercised by any code**. → recorded as **C-8** (wording
risk: "adopts" overstates current state).

## 7. Risk flags

- The audited Hermes surface includes **browser tools and terminal/code execution** —
  the two highest-risk capability classes. The Sprint-3 design correctly classifies
  these as read-only / approval-required, but **no enforcement code is verified** yet
  (R-06 OPEN). Activating Hermes before the policy engine is committed + verified would
  breach the charter's safe-by-default posture.
