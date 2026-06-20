# Hermes Vendor Baseline

This directory is a Sprint 4 quarantined Hermes provenance baseline.

It is **inert**:

- not imported by Magna Enso application code,
- not wired into runtime,
- not exposed through CLI or UI,
- not executable,
- not registered as tools,
- not package-discovered as active code,
- not evidence that runtime policy enforcement exists.

The baseline is structurally safe by absence and quarantine only. There is no Sprint 5 policy engine here.

## Source

- Upstream repository: `https://github.com/nousresearch/hermes-agent`
- Audited SHA: `33b1d144590a211100f42aa911fd7f91ba031507`
- License: MIT, preserved in `UPSTREAM_LICENSE.txt`

## Imported Artifacts

Only inert provenance/license/manifest artifacts are present:

- `UPSTREAM_LICENSE.txt`
- `provenance/UPSTREAM_PYPROJECT.toml.source.txt`
- `provenance/UPSTREAM_PACKAGE.json.source.txt`
- `retained/RETAINED_SURFACE_STATES.yaml`

No executable Hermes Python module, Node package, runtime entry point, gateway, plugin, MCP loader, browser action, terminal/code execution path, scheduler execution path, messaging surface, cloud provider, or external memory sync module is imported.

## Boundary

This baseline is for review and later governed design reference only. Future executable source import requires a separate approval, dependency/license review, and policy-engine readiness.
