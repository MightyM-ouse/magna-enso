# Public Repository Security

The source repository is public to support repository rules on the current GitHub plan.
This is a source-control decision, not permission for a public application endpoint.

## Mandatory controls

- Protected `main`; PR-only changes; no force push or deletion.
- Gitleaks scan of history and working tree before first publication: passed on
  2026-06-24 with Gitleaks 8.30.1.
- Gitleaks or equivalent required in CI before merge when CI is established.
- `.env*`, keys, credentials, cookies, browser profiles, and private local data excluded.
- Dependencies and reused source require provenance and license review.
- Security findings use private reporting where disclosure would create risk.

## Licensing

Public visibility alone grants no reuse license to Magna-owned material. A product license
is an open Product Owner decision. Third-party material retains its own license; the inert
Hermes baseline preserves the upstream MIT notice.

## Runtime boundary

Runtime services remain local-first and LAN-first, off by default. Public listeners,
tunnels, cloud execution, external messaging, and outbound actions require explicit
requirements, threat review, policy controls, tests, and Product Owner approval.

