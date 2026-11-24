# Bump Crew

A static web app (no build step) for tracking friends' and family's babies. See README.md for the layout.

## Branches: always follow the dev-main-workflow skill

- Work and push on **`dev`**. Never commit or push to **`main`**, which is live on GitHub Pages.
- When work is pushed, ask the owner whether to open a PR from `dev` into `main`. The owner reviews and merges it.
- Full steps: `.claude/skills/dev-main-workflow/SKILL.md`

## Checks

- Tests: `node --test test/*.test.js`
- Icons: `python3 scripts/make-icon.py` (needs Pillow)
