# ARCH-001 Architecture Open Decisions

## Status

`DECISIONS_PENDING_EVIDENCE`

No decision below should be made from filenames alone.

| ID | Decision | Why needed | Architect recommendation | Product Owner timing |
|---|---|---|---|---|
| AD-001 | Provide ARCH-SRC-01 to the ARCH-001 review context | Normative Phase A comparison remains blocked; DIAG-SRC-01 is now authenticated | Supply the exact corrected architecture/specification package; do not substitute a regenerated copy | Required now |
| AD-002 | Confirm whether ARCH-SRC-01 is the preferred candidate baseline or one input among Sprint 0/3 sources | Accepted migration input does not equal canonical authority | Treat it as preferred candidate only until conflict comparison passes | After package inspection |
| AD-003 | Select Magna-owned product license or approve an interim copyright notice | Public repository does not grant reuse rights | Resolve before importing substantial Magna-owned architecture | Before Phase B merge |
| AD-004 | Approve the proposed target information architecture | Target paths determine long-term ownership and traceability | Use separated architecture/specification/diagram/decision/archive structure | After full inventory |
| AD-005 | Resolve any EH-0017/EH-0018 conflicts in imported sources | Active strategy and naming are already accepted | Event Horizon decisions prevail; preserve source history in manifest | During comparison |
| AD-006 | Select the exact versioned HELIX contract referenced by Enso | Cross-repository doctrine must not drift | Link to an immutable HELIX version/commit; do not copy doctrine | Before Phase B |
| AD-007 | Decide treatment of HTML diagram viewer | Viewer may add maintenance/security surface | Keep as generated artifact unless a clear repository use case exists | Phase B scope decision |
| AD-008 | Authorize Phase B exact import list | Phase A cannot authorize migration | Approve explicit source hashes, target paths and conflict resolutions only | After Phase A review |

## Immediate Product Owner input

Provide a ZIP of `magna-enso-architecture-technical-specification-corrected/` to this conversation or another explicitly approved ARCH-001-accessible source. DIAG-SRC-01 has been received and its expected SHA-256 verified.

Do not merge PR #9 while Phase A remains blocked.
