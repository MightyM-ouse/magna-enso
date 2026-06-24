# Hermes Provenance

## Purpose

Record the exact Hermes Agent source snapshot inspected for Sprint 2 and confirm it stayed outside the Magna Enso repository.

## Files Inspected

- `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/.git/config`
- `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/LICENSE`
- `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/README.md`
- `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/pyproject.toml`
- `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/package.json`
- `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/package-lock.json`
- Top-level directory listing of `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/`

## Findings

- Source repository URL: `https://github.com/nousresearch/hermes-agent`
- Clone path: `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/`
- Clone timestamp: `2026-06-17T18:58:13Z` clone initiated.
- Default branch audited locally: `main`
- Exact commit SHA audited: `33b1d144590a211100f42aa911fd7f91ba031507`
- License file detected: `LICENSE`
- Primary Python package files detected: `pyproject.toml`, `uv.lock`, `setup.py`, `hermes_cli/setup.py`, `hermes_cli/subcommands/setup.py`
- Primary Node package files detected: `package.json`, `package-lock.json`, `apps/bootstrap-installer/package.json`, `apps/desktop/package.json`, `apps/shared/package.json`, `scripts/whatsapp-bridge/package.json`, `scripts/whatsapp-bridge/package-lock.json`, `ui-tui/package.json`, `web/package.json`, `website/package.json`, `website/package-lock.json`
- Additional plugin license files detected: `plugins/hermes-achievements/LICENSE`, `plugins/security-guidance/LICENSE`
- Clone remained outside `magna-enso/`; it is under the approved scratch path.

## Evidence Paths

- `LICENSE`
- `README.md`
- `pyproject.toml`
- `uv.lock`
- `package.json`
- `package-lock.json`
- `apps/desktop/package.json`
- `web/package.json`
- `website/package.json`
- `scripts/whatsapp-bridge/package.json`

## Top-Level Directory Summary

Notable top-level directories include:

- Agent core and runtime: `agent/`, `run_agent.py`, `model_tools.py`, `toolsets.py`
- Tools and execution surfaces: `tools/`, `skills/`, `optional-skills/`, `optional-mcps/`
- Scheduling and automation: `cron/`
- Messaging/API gateway: `gateway/`
- Provider/plugin system: `providers/`, `plugins/`
- UI and desktop surfaces: `web/`, `ui-tui/`, `apps/`, `website/`
- Protocol adapters: `acp_adapter/`, `tui_gateway/`, `acp_registry/`
- Packaging and deployment: `docker/`, `nix/`, `packaging/`, `scripts/`
- Tests and docs: `tests/`, `docs/`

## Confidence Level

High. Provenance values were taken from the local Git clone and local manifest/license files at the audited commit.

## Risks

- This was a shallow clone of the current default branch head, not a full history audit.
- Submodule or generated artifact status was not deeply audited because the task scope is source read-only review.

## Open Questions

- Whether Sprint 4 should pin this exact SHA or a later human-approved SHA.
- Whether plugin license files require a separate legal review beyond this engineering provenance review.

## Recommendation

Use `33b1d144590a211100f42aa911fd7f91ba031507` as the only Sprint 2 audited Hermes snapshot. Do not treat any later Hermes commit as covered by this audit without a new provenance pass.
