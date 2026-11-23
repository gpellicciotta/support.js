# REST Client Upgrade Guide

Guide for migrating downstream JavaScript REST client libraries (`auth` and `counters`)
to the shared transport and error hierarchy modules in `@gpellicciotta/support.js`.

---

## Overview
The `auth` and `counters` client packages previously maintained independent,
near-identical copies of transport and error handling.
In v2.0.0, `@gpellicciotta/support.js` consolidates these into:
- `net.mjs`: URL construction, authorization header generation, `fetch`-based request execution, and the complete `ApiError` hierarchy.
- `dates.mjs`: wire date serialization (`toWireDate`, `fromWireDate`, `parseDate`) and relative/human formatting.

---

## Shared Modules Architecture

### `src/net.mjs`
Exports:
- `sendRequest(baseUrl, method, path, options)`: executes request via `fetch`, preserving auth's `options.headers` merging over default `Accept: application/json`, handling optional `redirect: 'manual'`, and returning `{ status, data, headers }`.
- `buildUrl(baseUrl, path, query)`: constructs query string handling scalar values and arrays.
- `basicAuthHeader(userName, password)`: generates standard `Basic <base64>` header value.
- `bearerAuthHeader(token)`: generates standard `Bearer <token>` header value.
- `redirectToAuth(loginUrl, returnUrl)`: redirects browser to centralized auth.
- `ApiError`: base class carrying `message`, `status`, and parsed `body`.
- `AuthenticationError`: status 401.
- `ValidationError`: status 400.
- `NotFoundError`: status 400 where message matches regex patterns indicating missing resource. Inherits from `ValidationError`.
- `ConflictError`: status 409.
- `NOT_FOUND_PATTERNS`: regex patterns matching missing resource identifiers.
- `mapError(status, message, body)`: factory function mapping status code and message to the appropriate class.

### `src/dates.mjs`
Exports wire date helpers:
- `toWireDate(value)`: serializes Date objects to UTC ISO strings without milliseconds (`yyyy-MM-ddTHH:mm:ssZ`).
- `fromWireDate(value)`: deserializes server date strings into `Date` instances.
- `parseDate(value)`: alias for `fromWireDate`.

---

## Upgrading `auth`

### Update Dependencies
In `clients/js/package.json`, add `@gpellicciotta/support.js` under `dependencies`:

```json
{
  "dependencies": {
    "@gpellicciotta/support.js": "^2.0.0"
  }
}
```

### Re-export Errors
Replace local implementation with re-exports from the shared library:

```javascript
export * from '@gpellicciotta/support.js/net.mjs';
```

### Re-export HTTP Transport
Replace local implementation with re-exports from the shared library:

```javascript
export * from '@gpellicciotta/support.js/net.mjs';
```

### Verify Auth Client
Run the test suite in `clients/js/`:

```bash
npm test
```

All authentication, model conversion, and client request tests must pass without modification.

---

## Upgrading `counters`

### Update Dependencies
In `clients/js/package.json`, add `@gpellicciotta/support.js` under `dependencies`:

```json
{
  "dependencies": {
    "@gpellicciotta/support.js": "^2.0.0"
  }
}
```

### Re-export Errors
Re-export from the shared library:

```javascript
export * from '@gpellicciotta/support.js/net.mjs';
```

### Re-export HTTP Transport
Re-export from the shared library:

```javascript
export * from '@gpellicciotta/support.js/net.mjs';
```

Note: `parseDate` is exported as an alias to `fromWireDate`, ensuring full compatibility with existing counters client code.

### Synchronize Client Files to Webapp
Run the synchronization script to update webapp client copies:

```bash
node clients/js/scripts/sync-client.mjs
```

### Verify Counters Client
Run the client test suite:

```bash
npm test
```

Verify unit tests (`unit.test.mjs`), mutations matrix tests (`mutations-matrix.test.mjs`), and offline sync tests (`offline-sync.test.mjs`) all pass.

---

## Migrating UI Components and Stylesheets in v4.0.0
Starting in v4.0.0, `@gpellicciotta/support.js` ships non-UI JavaScript only.
Visual tokens, stylesheets, UI components, and the application shell live in [`support.webapp`](https://github.com/gpellicciotta/support.webapp).

| Removed from `support.js`                    | Replacement in `support.webapp`                                                    |
| :------------------------------------------- | :--------------------------------------------------------------------------------- |
| `css/*.css` (all 19 stylesheets)             | `src/css/` base, reset, shell, components, and looks                               |
| `component.mjs`                              | Component CSS plus behavior modules in `src/js/`                                   |
| `app-view.mjs`                               | App shell (`shell.css`, `app-nav.js`)                                              |
| `app-menu.mjs`                               | `menu.js`, `account-menu.js`                                                       |
| `app-action-bar.mjs`                         | Toolbar component and shell action slots                                           |
| `app-notification-bar.mjs`                   | `toast.js`, banner component                                                       |
| `app-internals-view.mjs`, `home-view.mjs`    | Shell pages built by each app                                                      |
| `dialog.mjs`                                 | `dialog.js`, `inline-confirm.js`                                                   |
| `collection-editor.mjs`                      | List, row, and list-editor shell pattern                                           |
| [forms.mjs](../../src/forms.mjs) DOM helpers | `form.js`, `field.js` (pure validators remain in [forms.mjs](../../src/forms.mjs)) |
| `reorder.mjs`, `installer.mjs`, `img/*`      | Retired from `support.js` (stay on v3.1.0 if still needed)                         |
| `docs/specs/visual-style-guide.md`           | `support.webapp` visual style guide                                                |
