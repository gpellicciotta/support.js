# Requirements

Functional and technical requirements for the `support.js` project.

---

## High-Level Goals
- Provide general-purpose JavaScript support code, for both client-side (browser) and server-side (Node.js)
  use, with as few third-party dependencies as possible.
- Serve as a shared library for other web projects (`auth`, `counters`), reducing
  hand-duplicated utility code between their web apps and JS REST clients.
- Publish releases as an npm package (`@gpellicciotta/support.js`) on GitHub Packages.

---

## Functional Requirements

### CLI and Browser Logging
- Provide a unified logging module (`src/logs.mjs`) featuring `LogLevel`, `formatSeverityIndicator`/`formatLogMessage`, `CliLogger`, and browser event logging (`Logger`).

### DOM and Forms
- Provide DOM-related utility functions that rely on the global `document`/`window` objects (`src/dom.mjs`).
- Provide form-related validation/marking helper functions (`src/forms.mjs`).
- Provide a drag-to-reorder utility for container items (`src/reorder.mjs`).
- Provide a dialog component (`src/dialog.mjs`).

### General Utilities and Core Domains
- Provide specialized core modules: `src/objects.mjs` (equality, deepClone), `src/strings.mjs` (escaping, capitalization), `src/math.mjs` (numerics, clamping, random, formatting), `src/colors.mjs` (color conversions, contrast), and `src/dates.mjs` (diffs, formatting, wire serialization).
- Provide changelog parsing from markdown into structured release objects (`src/changelog-parser.mjs`).
- Provide `Vector` and `Matrix` classes for 2D/3D math (`src/vector.mjs`, `src/matrix.mjs`).
- Provide Perlin noise generation (`src/noise.mjs`).

### Storage and Paging
- Provide zero-dependency offline storage adapters and usage tracking (`src/storages.mjs`).
- Provide uniform pagination envelopes and navigation helpers (`src/paging.mjs`).

### Canvas and Games
- Provide canvas-drawing utility functions relying only on the Canvas API (`src/canvas.mjs`).
- Provide collision-detection utility functions between shapes, for simple games (`src/collisions.mjs`).
- Provide decorative canvas effects: fireworks (`src/fireworks.mjs`) and snowflakes (`src/snowflakes.mjs`).

### Word Lists
- Provide Dutch and English word lists for word-based games or utilities (`@gpellicciotta/support-words.js`,
  in `packages/words/`).

### REST Client Transport and Errors
- Provide a typed error hierarchy (`ApiError`, `AuthenticationError`, `ValidationError`, `NotFoundError`, `ConflictError`, `mapError`) and HTTP transport (`buildUrl`, `basicAuthHeader`, `bearerAuthHeader`, `sendRequest`, `redirectToAuth`) for fetch-based API clients (`src/net.mjs`).
- See [REST Client Upgrade Guide](specs/client-upgrade-guide.md) for downstream migration details.

### Styling
- Provide a CSS reset (`css/reset.css`) and a shared color palette (`css/colors.css`).

---

## Technical Requirements
- **Module Format**: ECMAScript modules (`.mjs`), consumed via subpath imports (e.g.
  `@gpellicciotta/support.js/logs.mjs`).
- **Runtime**: Browser-safe modules avoid Node-only APIs; Node-only modules (e.g. `cli-log.mjs`) are the
  exception, documented as such.
- **Testing**: Node's built-in `node:test` and `node:assert` (no third-party test framework dependency).
- **Dependencies**: As few third-party dependencies as possible, per
  [general-guidelines.md](https://github.com/gpellicciotta/dev-guidelines/blob/main/guidelines/general-guidelines.md).
- **Packaging**: npm package published to GitHub Packages via an automated GitHub Actions workflow, triggered
  by a published GitHub Release.
- **Code Standards**: 2-space indentation, UTF-8 encoding, US English, linted with ESLint Stylistic (Stroustrup braces)
  (`npm run lint`/`format`); exported functions and classes are documented with JSDoc comments.
- **Versioning**: [Semantic Versioning](https://semver.org/); backward-incompatible changes bump the major
  version and get an explicit breaking-change note in `CHANGELOG.md`.
