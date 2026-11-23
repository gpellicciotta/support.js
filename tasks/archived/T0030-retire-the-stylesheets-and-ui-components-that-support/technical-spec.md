## Technical Specifications
support.js keeps general-purpose, non-UI JavaScript only.
support.webapp owns the visual design system: tokens, looks, stylesheets, components, and the app shell.
The support.webapp roadmap, phase 5, sets the exit criterion: "support.js ships no stylesheets."

### Prerequisites
Each consumer below must load none of the retired files before this task starts.
The list comes from a search on 2026-11-23 that hit its time limit, so step 2 repeats it in full.

| Consumer        | Retired files it loads today                                                             |
| :-------------- | :--------------------------------------------------------------------------------------- |
| counters.server | app-view, app-menu, home-view, component, dialog, collection-editor, reorder, forms, dom |
| auth            | stale vendored stylesheet copies; `mock-dom.mjs` in tests (kept)                         |
| hinolugi-utils  | `css/reset.css`, `css/colors.css`                                                        |

counters.server T0272 and the auth redesign plan in support.webapp move the first two onto support.webapp.
hinolugi-utils needs its own move; record it as a backlog task there if the inventory still finds it.

### Removal List

| Item                                                | Action | support.webapp replacement or note                                                               |
| :-------------------------------------------------- | :----- | :----------------------------------------------------------------------------------------------- |
| `css/` (all 19 stylesheets)                         | Remove | `src/css/` base, reset, shell, components, and looks                                             |
| `src/component.mjs`                                 | Remove | Component CSS plus behavior modules in `src/js/`                                                 |
| `src/app-view.mjs`                                  | Remove | App shell (`shell.css`, `app-nav.js`)                                                            |
| `src/app-menu.mjs`                                  | Remove | `menu.js`, `account-menu.js`                                                                     |
| `src/app-action-bar.mjs`                            | Remove | Toolbar component and shell action slots                                                         |
| `src/app-notification-bar.mjs`                      | Remove | `toast.js`, banner component                                                                     |
| `src/app-internals-view.mjs`                        | Remove | Shell pages built by each app                                                                    |
| `src/home-view.mjs`                                 | Remove | Shell pages built by each app                                                                    |
| `src/dialog.mjs`                                    | Remove | `dialog.js`, `inline-confirm.js`                                                                 |
| `src/collection-editor.mjs`                         | Remove | List, row, and list-editor shell pattern                                                         |
| `src/forms.mjs` DOM helpers                         | Remove | `form.js`, `field.js`; keep `isValidEmailAddress`, `isValidPassword`, `validPasswordDescription` |
| `src/reorder.mjs`                                   | Remove | Drag reordering of lists; retired with UI components                                             |
| `src/installer.mjs`                                 | Remove | PWA install prompt helper; retired with app-shell components                                     |
| `src/dom.mjs`                                       | Keep   | DOM-ready, gesture, and animation-frame helpers; not visual styling                              |
| `src/canvas.mjs`, `fireworks.mjs`, `snowflakes.mjs` | Keep   | Canvas graphics and animation effects                                                            |
| `img/` provider logos and sign-in button            | Remove | Auth branding assets; retired from support.js                                                    |
| `src/mock-dom.mjs`                                  | Keep   | Test infrastructure; auth tests import it                                                        |
| `docs/specs/visual-style-guide.md`                  | Remove | support.webapp visual style guide                                                                |

Remove the matching tests of each removed module, such as `tests/component.test.mjs` and `tests/stylesheets.test.mjs`.
Remove the `./*.css` and `./css/*.css` entries from `exports` and `css` from `files` in `package.json`.
Check `scripts/lib/static-server.mjs` for CSS-specific serving and keep only what non-UI code needs.

### Declared Files
- package.json
- packages/words/package.json
- README.md
- docs/index.md
- docs/requirements.md
- docs/devops.md
- docs/specs/code-reuse-opportunities.md
- docs/specs/client-upgrade-guide.md
- src/forms.mjs
- tests/forms.test.mjs
- tests/package-exports.test.mjs

Combined task: Retiring UI components, stylesheets, and their documentation must ship together as the single breaking v4.0.0 boundary.
Size note: Nine modified files (721 lines) exceed the typical line because dropping DOM helpers from forms.mjs and forms.test.mjs deletes 607 lines.

### Tests
- Unit: a package test asserts `package.json` exports no CSS, lists no `css` in `files`, and every retired module is absent.
- Unit: `tests/forms.test.mjs` keeps passing for the three retained validators.
- Integration: `npm pack --dry-run` lists no `css/` file and no retired module.

Completion check: python scripts/devops.py check
