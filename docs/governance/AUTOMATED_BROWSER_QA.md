# Automated Browser QA

UI work must include automated evidence using Chromium through Playwright, Chrome
DevTools MCP, or an approved equivalent.

## Required checks

- Critical user workflow interactions and form behavior.
- Desktop, tablet, and mobile viewports.
- No unexpected console errors or failed application network requests.
- Keyboard navigation and automated accessibility checks.
- Stable loading, empty, error, and permission-denied states.
- Screenshots for key states and visual-regression comparison where a baseline exists.
- Dense-diagram/component readability at applicable zoom levels.

## Evidence

Commit a concise browser-QA report and selected acceptance screenshots. Store full traces,
videos, and bulk captures as Actions artifacts. Record browser/tool versions and commit SHA.

## Product Owner involvement

Do not ask the Product Owner to perform routine alignment, responsive, console, click,
filter, search, or visual-regression checks. Ask only for business-function acceptance,
subjective UX/product choices, or flows that cannot be automated safely.

Use a dedicated automation browser profile. Never attach an agent to the Product Owner's
personal authenticated browser profile.

