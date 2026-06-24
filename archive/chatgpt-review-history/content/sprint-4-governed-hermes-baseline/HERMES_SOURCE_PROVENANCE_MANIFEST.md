# Hermes Source Provenance Manifest

## Purpose

Record every upstream Hermes-derived artifact imported into the Sprint 4 quarantined baseline.

## Honesty Statement

This baseline is structurally safe / not runtime-enforced. Retained risky capabilities remain disabled until Sprint 5. No Hermes runtime, build, package script, or dependency install was performed.

## Source Identity

| Field | Value |
|---|---|
| Source repo | `https://github.com/nousresearch/hermes-agent` |
| Approved SHA | `33b1d144590a211100f42aa911fd7f91ba031507` |
| Local source path | `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/` |
| Source branch at local clone | `main` |
| Source status | clean |
| License | MIT |

## Imported Upstream Artifacts

| Source path | Target path | SHA-256 | Purpose |
|---|---|---|---|
| `LICENSE` | `vendor/hermes/UPSTREAM_LICENSE.txt` | `821556e6336796450ab852d375117b48a4887e71d255794fd6318d99982a5ab6` | Preserve MIT license and attribution. |
| `pyproject.toml` | `vendor/hermes/provenance/UPSTREAM_PYPROJECT.toml.source.txt` | `65c9bc6521fdeee289fa07fe10c82473f6228e46cca1e7ba9a380f5da6ca3269` | Static dependency/package manifest reference, non-active text. |
| `package.json` | `vendor/hermes/provenance/UPSTREAM_PACKAGE.json.source.txt` | `07b1b0c8d196c93cc4876092907e7350cfc8b04db18ce34debb522aead4ad1c0` | Static Node manifest reference, non-active text. |

## Magna-Owned Baseline Metadata

| Target path | SHA-256 | Purpose |
|---|---|---|
| `vendor/hermes/README.md` | `5380728de7d26fb5cb81f83305b461b5a966bd95e3088ef60b61485b5c1c04f4` | Quarantine and no-runtime documentation. |
| `vendor/hermes/retained/README.md` | `80d012c7d4e72055fb6fc634c4ee50d1af9cf35fe7d1f6ab2615f4490d4de3a7` | Retained-state metadata explanation. |
| `vendor/hermes/retained/RETAINED_SURFACE_STATES.yaml` | `c2ff93741638213285bd1faa0d2d982ff7902da8562bbf117589aa51fb0e3cf1` | Sprint 3 retained surface states, metadata only. |

## Findings

- The local Hermes clone exactly matches the approved SHA.
- No moving upstream branch was used.
- No executable Hermes module source was imported.
- Imported upstream artifacts are license/manifest references only.
- Active package discovery is avoided by using `.source.txt` names for manifests.

## Confidence Level

High.

## Risks

- Future executable imports must repeat provenance and dependency review.
- This baseline does not provide runtime functionality.

## Recommendation

Treat `vendor/hermes/` as an inert provenance baseline pending Antigravity validation and human review.
