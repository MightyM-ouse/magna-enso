# GITIGNORE_SCOPE_REVIEW.md
# Magna Enso — .gitignore Scope Review
# Type: Local-only decision package (planning/governance)
# Date: 2026-06-17
# Status: RECOMMENDATION — no .gitignore was created; no Git initialized.

---

## 1. Purpose

Define what a `.gitignore` for `magna-enso/` must cover (RG-06), and what must be **tracked**.
Advisory only — the file is created (first, before `git init`) as a separate human-approved step.

## 2. What MUST be tracked (do NOT ignore)

The governance scaffold is the product right now — it is all real, reviewable artifacts:

- `AGENTS.md`, `README.md`, `CLAUDE.md`, `CODEX.md`, `ANTIGRAVITY.md`
- `trace/**` — config, onboarding, status, context index, roles, workflows, templates, logs, registers, checklist
- `trace/evidence/**` — Light Curves are **real evidence and must be version-controlled**
  (e.g. `ENSO-0001_LIGHT_CURVE.md`). Do **not** ignore the evidence directory.

## 3. Recommended `.gitignore` contents (for `magna-enso/`)

```gitignore
# --- OS / editor noise ---
.DS_Store
Thumbs.db
*.swp
.idea/
.vscode/

# --- Secrets / environment (defense-in-depth; none exist yet) ---
.env
.env.*
*.key
*.pem
secrets/

# --- Future runtime build artifacts (none exist in Sprint 1) ---
__pycache__/
*.pyc
.venv/
venv/
node_modules/
dist/
build/
*.log

# --- Local-only review memory & scratch (defensive; normally OUTSIDE this repo) ---
# ChatGPTReview/ is a SIBLING of this repo and is naturally excluded when the repo
# root is magna-enso/. These entries are belt-and-suspenders in case anything is ever
# created or symlinked inside the repo by mistake.
ChatGPTReview/
**/ChatGPTReview/
*scratch*/
*hermes-audit*/
```

## 4. If Git is ever initialized at the PARENT `Magna/` level (NOT recommended)

A parent-level repo pulls these into scope and they **must** be handled before any commit:

```gitignore
# MANDATORY exclusions at parent Magna/ level
ChatGPTReview/          # local-only review memory — never track
magna-helix/            # separate repo / blueprint — never nest or track here
# planning/, trace/, brand-assets/ may be tracked or split per a separate decision
```

`magna-helix/` must never be nested/tracked inside another repo (it is the separate HELIX repo and is
**never modified** — EH-0004). Preferred path avoids all of this by rooting Git at `magna-enso/`.

## 5. Defense-in-depth rationale

- Rooting at `magna-enso/` makes `ChatGPTReview/` exclusion **structural** (it is outside the tree).
- The explicit `.gitignore` entries above add a second layer in case of an accidental copy/symlink.
- Secrets/runtime patterns are pre-emptive: none exist in Sprint 1, but they will once runtime work
  starts (Sprint 4+), and the ignore rules should exist before then.

## 6. Validation to run AFTER a future, approved `git init`

(For reference — not run now.) After init + `.gitignore`, a human-approved worker should confirm:

```text
git status --untracked-files=all   # ChatGPTReview/ must NOT appear
git check-ignore -v ChatGPTReview   # (only meaningful if parent-level; sibling case = out of tree)
```

No Hermes source, no secrets, and no `ChatGPTReview/` paths should ever be staged.

## 7. Out of scope

No `.gitignore` file was created and no Git repository was initialized by this package.
