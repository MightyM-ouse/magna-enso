# TRACE Validation Checklist

## Every task

- [ ] Applicable repository, branch, HEAD, issue, PR, and task packet verified.
- [ ] Allowed scope respected; unrelated/user changes preserved.
- [ ] No direct `main` push, force push, self-merge, or hidden scope expansion.
- [ ] Claims distinguish planned, implemented, tested, verified, released, and production use.
- [ ] Exact failures, skipped checks, and limitations recorded.
- [ ] Light Curve and material decisions updated.

## Public-source security

- [ ] Gitleaks scanned changed content before push.
- [ ] No secrets, `.env`, cookies, browser profiles, private keys, or personal data committed.
- [ ] Dependency provenance and licenses reviewed where applicable.
- [ ] Public GitHub visibility was not treated as authorization for public runtime exposure.

## Runtime and capability work

- [ ] Default-deny and one governed capability entry path demonstrated.
- [ ] Audit confirmation occurs before consequential effect.
- [ ] Negative tests demonstrate blocked bypass paths.
- [ ] Partial-effect failures enter recovery; they are not reported as clean denial.
- [ ] Memory, skills, scheduler, external tools, network, cloud, and messaging respect policy.

## UI/browser work

- [ ] Critical workflows automated in Chromium.
- [ ] Desktop/tablet/mobile states captured.
- [ ] Console, failed network requests, keyboard, accessibility, loading/error states checked.
- [ ] Visual regression evidence produced when a baseline exists.
- [ ] Product Owner asked only for product/functional or subjective UX acceptance.

## Evidence quality

- [ ] Commands, versions, SHA, environment, results, and artifact links are reproducible.
- [ ] Large/raw output is stored as an Actions artifact; curated evidence is committed.
- [ ] Percentages include numerator, denominator, method, and limitations.

