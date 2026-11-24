# Bump Crew 🍼

A baby tracker for **everyone else's** babies. Most pregnancy apps follow one baby, your own. Bump Crew lets you add as many as you like (friends, siblings, coworkers, neighbors) and see where each one is at a glance.

## Features

- **Unlimited babies**, each with parent names, an optional nickname and who they are to you (friend, family, coworker…)
- **Two ways to set timing**: enter a due date, or just "she's 14 weeks" and the due date is worked out for you
- **Weekly size comparisons** in four themes, with a scrollable week-by-week "journey" view:
  - 🍎 Fruits & Veggies: poppy seed → watermelon
  - 🐾 Animals: flea → seal pup
  - 🧁 Sweet Treats: sprinkle → wedding cake
  - ⚽ Toys & Sports: speck of glitter → piñata
- Pick a default theme, or give individual babies their own (your animal-loving friend gets animals)
- Week + day, trimester, approximate length and weight (lb/in or kg/cm), days to go, overdue alerts
- **"Baby arrived!"**: switch to a newborn with birthday and birth weight, then see their age grow
- Filter (on the way / arrived), search, sort by due date, name or date added
- Export/import a JSON backup; data otherwise stays in your browser (localStorage)
- Light and dark mode, works on phones

## Live site

https://prestonthomas-cmd.github.io/bumpCrew/ (served by GitHub Pages from the root of `main`).

## Running it

No build step. Open `index.html` in a browser, or serve the folder:

```sh
python3 -m http.server 8000   # then visit http://localhost:8000
```

## Home-screen icon

In Safari, tap **Share → Add to Home Screen** to get the bottle icon. The icons in `icons/` are drawn by `python3 scripts/make-icon.py` (needs Pillow) from the numbers in that script, so the logo can be retuned without an image editor.

The home-screen icon opens the app in Safari on purpose (`"display": "browser"`). A full-screen home-screen web app gets its own separate storage on iOS, so the babies you'd already saved in Safari wouldn't show up in it.

If iOS draws the icon as a dark tile, the home screen's icon style is set to Dark or Automatic. Long-press the home screen → **Edit → Customize → Light** to fix it.

## Tests

```sh
node --test test/*.test.js
```

## Layout

| Path | Purpose |
| --- | --- |
| `index.html` | The page, including the home-screen icon tags |
| `js/data.js` | Size themes and average length/weight per week (4–40) |
| `js/calc.js` | Date math and unit formatting (no DOM, unit-tested) |
| `js/app.js` | UI: rendering, forms, storage |
| `css/styles.css` | Styles |
| `icons/`, `manifest.webmanifest` | Home-screen and browser icons |
| `scripts/make-icon.py` | Draws the icons in `icons/` |
| `test/` | Unit tests for `js/calc.js` and `js/data.js` |
| `.nojekyll` | Tells GitHub Pages to serve the files as-is |

## Branches

- **`main`** is what's live. Every push to it redeploys the site.
- **`dev`** is where changes go first. Once they're tested, merge `dev` into `main` to publish them.

Sizes are friendly averages for fun, not medical guidance.
