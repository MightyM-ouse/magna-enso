# Source Import Inventory

## Purpose

List every file created in the Sprint 4 vendor baseline and classify whether it is upstream-derived or Magna-owned.

## Honesty Statement

This baseline is structurally safe / not runtime-enforced. Retained risky capabilities remain disabled until Sprint 5. No Hermes runtime, build, package script, or dependency install was performed.

## Inventory

| Target path | Origin | Active code? | Notes |
|---|---|---:|---|
| `vendor/hermes/README.md` | Magna-owned | No | Quarantine documentation. |
| `vendor/hermes/UPSTREAM_LICENSE.txt` | Hermes `LICENSE` | No | MIT license preservation. |
| `vendor/hermes/provenance/UPSTREAM_PYPROJECT.toml.source.txt` | Hermes `pyproject.toml` | No | Non-active manifest reference. |
| `vendor/hermes/provenance/UPSTREAM_PACKAGE.json.source.txt` | Hermes `package.json` | No | Non-active manifest reference. |
| `vendor/hermes/retained/README.md` | Magna-owned | No | Retained metadata documentation. |
| `vendor/hermes/retained/RETAINED_SURFACE_STATES.yaml` | Magna-owned | No | Sprint 3 surface-state metadata only. |

## Explicit Non-Imports

No files were imported from these Hermes runtime/source areas:

- `agent/`
- `tools/`
- `cron/`
- `gateway/`
- `plugins/`
- `providers/`
- `hermes_cli/`
- `acp_adapter/`
- `tui_gateway/`
- `web/`
- `ui-tui/`
- `apps/`
- `optional-mcps/`
- `optional-skills/`

## Findings

- The baseline contains no `.py` files.
- The baseline contains no active `package.json`, `pyproject.toml`, `setup.py`, `__init__.py`, or plugin manifest.
- The baseline contains no executable files.
- Every file under `vendor/hermes/` is accounted for above.

## Confidence Level

High.

## Risks

- The baseline is intentionally minimal and non-runnable.
- Future executable imports require a new inventory.

## Recommendation

Proceed to Antigravity validation with this inventory as the authoritative file list.
