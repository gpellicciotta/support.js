# Versioned Changes

A summarized overview of all changes, per version of this project.

> Entries will be added in reverse chronological order, so with the most recent at the top.
>
> The top-most version heading is always the active in-development version, identified by a `-pre`
> suffix on its version number (e.g. `## v1.8.1-pre`) instead of a status tag. Once a version is frozen
> or released, that suffix is replaced by one of these status codes:
> - `[{{date}}]` - frozen/finalized on {{date}}
> - `[released: {{date}}]` - released to package manager or production on {{date}}
> - `[broken]` - considered broken and not be used

---

## v4.0.1-pre
- DevEx: Added a root base element to the account, dashboard, help, and notifications view harnesses so their sprite icons load.
- DevEx: Made the devops deploy PATH test use a fake gcloud path without a drive colon, so it passes on Linux CI.

## v4.0.0 [released: 2026-11-17] [google-cloud-run: auth-00011-jvv]
- DevEx: Vendored support.webapp v0.2.1, with the slate neutral palette, a brighter blue accent, and focus glows.
- SPA: The top bar's brand and buttons now line up with the content's start and end edges.
- Admin: The top bar holds a navigation toggle and the Admin Console brand; the screen title moved into the content.
- Admin: The toggle collapses the sidebar to an icon rail or hides it, and opens it as a drawer below 1024 px.
- SPA: **[breaking]** Moved the SPA's chrome onto the vendored `neutral` look and shell; signed-in pages get a menu button and an account menu.
- SPA: The menu holds Dashboard, Notifications with an unread badge, Help, and Admin Console for administrators; Account and Sign Out moved to the account menu.
- SPA: The notification bar became shell banners for inbox alerts, errors, and warnings, and vendored toasts for other notifications.
- SPA: Home became a public start page with Sign In and Create Account, replacing the splash screen.
- SPA: A view's error page is now an empty state with Try again and Back to dashboard.
- SPA: The theme preference moved to the `auth.theme` key; a stored `auth_theme` value moves there once.
- SPA: The service worker offers updates through the vendored update prompt and precaches the vendored files the SPA uses.
- SPA: Dropped Roboto and the old layout, menu, action bar, notification bar, splash, and error stylesheets; other screens keep theirs until their own redesign.
- SPA: Sign-in offers its social, password, and email code methods as a segmented control, with vendored forms and fields.
- SPA: The relying-party branding became a banner; its redirect confirmation, `app-state` forwarding, and error handling are unchanged.
- SPA: Create account validates on the vendored form and shows the result, including the server's reason, in banners.
- SPA: The dashboard shows one link card per application, and an empty state when there is none.
- SPA: Dropped the sign-in, create account, and dashboard stylesheets and their precache entries.
- SPA: The account view moved onto vendored cards, forms, fields, rows, a settings table, and the theme switch.
- SPA: The theme switch replaces the theme select; each change also saves the account's `theme` setting.
- SPA: Signing in applies the account's saved theme, which the user resources never carried before.
- SPA: Deleting the account and undoing it now ask in place instead of in a dialog.
- SPA: Dropped the account and settings view stylesheets, the legacy dialog, and their precache entries.
- SPA: Notifications show as rows with badges and chips; a multi-select marks several read or discards them at once.
- SPA: Help moved onto cards, topic filter chips, and collapsible FAQ and release entries; search, FAQ, and changelog stay.
- SPA: Help answers now describe the current account view, menu, and Admin Console instead of removed screens.
- SPA: **[breaking]** Removed every stylesheet in `webapp/css/`, `auth.css` included; app rules moved to `webapp/styles/app.css`.
- SPA: Dropped the Font Awesome kit; icons come from the vendored and app-local sprites only.
- SPA: The service worker precaches exactly the stylesheets and modules the SPA loads, without unused or duplicate entries.
- DevEx: The design conformance check now also scans `webapp/styles`.
- SPA: **[breaking]** Removed the SPA's old admin, user, and application views; `/admin`, `/users/...`, and `/applications/...` now redirect to the matching Admin Console screen.
- SPA: The menu keeps one Admin Console entry, shown to administrators only and linking `/admin/`; Create New User and Register Application are gone.
- SPA: The service worker no longer precaches the deleted views or files removed in earlier versions.
- SPA: Navigation links, such as help topic cards, now open their target when an icon or inner text inside them is clicked.
- SPA: Added the standalone Admin Console at `/admin/` with its shell, sign-in, access pages, Overview, and Changelog.
- SPA: Added the Admin Console Users screen with account filters, a detail panel, account creation, grants, export, and deletion.
- SPA: Added the Admin Console Sessions screen with token filters, single and bulk revocation, and expired-token removal.
- SPA: Added the Admin Console Applications screen with registration, editing, user grants, one-time secret reveal, and deletion.
- SPA: Admin Console confirmation questions now hide the button that asked them, as the vendored inline confirmation intends.
- SPA: Added the Admin Console System events screen with server filters, offset paging, and expandable JSON metadata.
- SPA: Added the Admin Console Logs screen, which filters and pages the server's log buffer in the browser.
- SPA: Added the Admin Console Broadcasts screen with a live preview, audiences, history rebuilt from system events, and retraction.
- Docs: [web-api.md](docs/web-api.md) now shows the real `target-filter` fields of broadcasts and the `log-entries` wrapper of `GET /api/logs`.
- SPA: Sign-in now loads a `/admin/` return URL with a full page navigation.
- SPA: Favicons, the header logo, and the dashboard fallback logo use the shared support.webapp v0.2.1 blue hexagon.
- SPA: Install icons, the apple touch icon, and maskable manifest icons use the dimensional hexagon from `img/install/`.
- SPA: The Admin Console links the SVG favicon and apple touch icon; the unused 256 and 512 px renditions are gone.
- BackEnd: A bare `/admin` keeps serving the SPA, while `/admin/` serves the console's `index.html`.
- Docs: Added [admin-spec.md](docs/specs/admin-spec.md) and static [admin-wireframes/](docs/specs/admin-wireframes/) on the vendored `neutral` look.
- DevEx: Vendored `support.webapp` (`neutral` look) via [design.json](design.json) and added design conformance and Playwright checks to [devops.py](scripts/devops.py) and CI.
- DevEx: The sign-in view harness honors `?theme=`, so `capture-view.py --theme` themes the sign-in presets; its notice icons now load.
- DevEx: **[breaking]** `capture-view.py`'s admin presets now open Admin Console screens with mocked API data; the `app-internals` preset is gone.
- DevEx: `capture-view.py` serves `.js` as `text/javascript`, since Windows registries can map it to `text/plain` and block module scripts.
- Docs: Regenerated the [UI tour](docs/tour/ui-tour-report.md) for v3.4.1-pre with an Admin Console overview step and renumbered steps.
- DevEx: A browser test now loads the nested deep link `/my/account` and fails on any failed request.
- DevEx: The legacy admin route tests no longer excuse a stylesheet HTTP 404 on nested routes.

## v3.4.0 [released: 2026-11-16] [google-cloud-run: auth-00010-mv6]
- API: Fixed the `expired` filter of the token and credential routes: `true` now matches only expired entries, `false` only unexpired ones.
- API: `DELETE /api/tokens?expired=true` no longer deletes active sessions; [web-api.md](docs/web-api.md) documents the filter.
- Clients: **[breaking]** The Java, JavaScript, and Python clients send `expired=false` unless `includeExpired` is set, so default deletes spare expired entries.
- SPA: The admin session list no longer sends `expired=true`, so it keeps listing active and expired sessions.
- DevEx: **[breaking]** Rebuilt [devops.py](scripts/devops.py) on support-python's `DevopsCli`: `check`, `test`, `build`, `versions`, `release`, and `deploy`, plus the `docker`, `db`, `server`, `mail`, and `client` groups.
- DevEx: **[breaking]** Replaced the `production` group and the `start`, `stop`, `status`, `verify`, `proxy`, `test-emails`, and `verify-deployment` shortcuts; `migrate`, `rollback`, and `verify-anonymized` remain.
- DevOps: **[breaking]** Split releasing from deploying: `devops.py release` freezes, tags, and publishes, then `devops.py deploy` deploys the checked-out tag and records its Cloud Run revision on `main`.
- DevOps: `devops.py deploy` always runs the schema migration; `--skip-migration` and the other deploy override flags are gone.
- DevEx: `gradle.properties` now carries the `-pre` suffix in development, and `CHANGELOG.md` uses `## v` headings, as the release tooling expects.
- SPA: The help page's release notes read both `## v` and the older `### v` changelog headings.
- DevOps: `:server:verifyProductionDeployment` now runs `devops.py client verify-deployment` for the deployed version.
- DevEx: `devops.py server stop` terminates the server through support-python's `safe_kill`.
- Build: Upgraded support-python from v2.0.0 to v3.2.0 in [requirements.txt](scripts/requirements.txt) and [pyproject.toml](clients/python/pyproject.toml).
- DevEx: Moved the snapshot anonymization rules into [anonymizer.py](scripts/lib/anonymizer.py), since support-python v3 dropped its `auth` profile; snapshots stay byte-identical.
- DevEx: **[breaking]** Removed `devops.py db snapshot --custom-password`; anonymized accounts always use the test password.
- DevEx: `devops.py` and `capture-view.py` set their own banner copyright, which support-python v3 no longer supplies.
- Build: Upgraded `com.pellicciotta:support.java` from 1.0.1 to 1.1.0 in `service`, `server`, and `clients/java`, picking up its HTTP response fixes.
- Build: Upgraded support-python to v2.0.0 in [pyproject.toml](clients/python/pyproject.toml) and the new [requirements.txt](scripts/requirements.txt), which also pins pytest for the scripts.
- DevEx: [bootstrap-dev-environment.py](scripts/bootstrap-dev-environment.py) now uses the standard library only and installs `scripts/requirements.txt` into a project-local `.venv`, never the global interpreter; `--skip-build` stops after that.
- DevEx: `devops.py` and `capture-view.py` rerun themselves with the `.venv` interpreter when it exists, so `python scripts/devops.py ...` keeps working.
- DevEx: **[breaking]** Moved `capture-view.py` onto support-python's `run_capture_cli` harness: no arguments shows help, invalid arguments exit 2, and `version` appends the commit hash.
- DevEx: Kept `capture-view.py --theme light|dark` through support-python v3.2.0's capture hooks; it combines with `--mode` and themes `--url` paths.
- DevEx: `capture-view.py` falls back to a sibling `support.python` checkout only when no support-python is installed, so a stale install fails loudly.
- DevEx: Replaced support-python v1's removed `print_version` in `devops.py` and the bootstrap with a local banner of the same format.

## v3.3.0 [2026-11-08] [released: 2026-11-08] [google-cloud-run: auth-00009-xd9]
- Build: Renamed the GitHub repository to `gpellicciotta/auth.server` and updated repository and publishing URLs.
- Security: Made the sign-in page forward `app-state` to social sign-in and return `state` before `authorization-code` on password, OTP, and cookie redirects.
- Security: Escaped `app-logo-url` in outgoing mails and replaced non-http(s) logo URLs with the default brand logo.
- Security: Added the optional `app-state` parameter to social sign-in and account linking, returned unchanged as `state` on the redirect to the relying party so it can prevent login CSRF.
- Security: Escaped `app-name` and `app-logo-url` in the sign-in page's relying-party banner and limited logos to absolute http(s) URLs, closing a script injection through crafted `/sign-in` links.
- Security: Made the sign-in page and the silent cookie-based sign-in hand the session to an `app-redirect-url` only after `GET /api/relying-party/redirect-check` confirmed it; a rejected URL drops the relying-party banner and redirect.
- Security: **[breaking]** Rejected an `app-redirect-url` whose origin is not registered (`redirect-url` or `base-url`) for the named application on the social sign-in, account-linking, and OTP mail routes; test mode also accepts loopback URLs. Relying-party apps must register the origin of their callback.
- BackEnd: Added the public `GET /api/relying-party/redirect-check` route that tells whether a redirect URL is registered; the sign-in page will use it (T0212).
- Config: Moved the Google OAuth 2.0 client to `pellicciotta-apps` across Cloud Run, Secret Manager, [build.gradle](server/build.gradle), and [devops.py](scripts/devops.py).
- DevOps: Switched `devops.py`, the Cloud DB Gradle tasks, and `dockerRun` from the service-account key file to user Application Default Credentials; `--credentials-file` stays as an override and `dockerRun` mounts the ADC file read-only.
- Infra: Deleted the legacy `auth-api-service@hinolugi-apps` service account, which held `roles/owner` and `roles/editor`, together with its 2023 key.
- DevOps: Moved the Cloud SQL target from `hinolugi-apps:europe-west1:hinolugi-data` to the MySQL 8.4 LTS instance `pellicciotta-apps:europe-west1:db-1` in `devops.py`, `migrate-gcp-service.py`, `server/build.gradle`, `server/Dockerfile`, and the documentation.
- BackEnd: Upgraded `mysql-socket-factory-connector-j-8` from 1.14.0 to 1.30.2, so a cold `caching_sha2_password` full authentication no longer sends the password in plain text and fails with `1045 Access denied`.
- DevOps: Added `gcp.cloud-sql-instance` to `gradle.properties` as the one Gradle source of the instance, derived the `devops.py` instance ID from its connection name, and raised the local and Testcontainers MySQL images from `mysql:8.0` to `mysql:8.4`.
- DevOps: Made `migrate-gcp-service.py` grant `roles/cloudsql.client` on the project that hosts the Cloud SQL instance instead of the source project.
- DevEx: Fixed `verify-anonymized` signing in as `anon-user-1@hinolugi.local`, an address anonymized snapshots never contain.

## v3.2.2 [2026-11-04] [released: 2026-11-04] [google-cloud-run: auth-00005-4cb]
- Docs: Replaced remaining `@hinolugi.com` addresses in docs, Maven metadata, scripts, and IDE run configurations.
- DevEx: Replaced the `hinolugi.com` sample mail brand in server tests with a reserved `acme.example` brand.
- BackEnd: Made `auth-tester@pellicciotta.com` the `add-test-user` account and seeded fake test users at `pellicciotta.local`.
- BackEnd: Added schema version `0.20` moving the reserved admin account (ID `0`) to `admin@pellicciotta.com`.
- Security: Limited the Auth service account's Secret Manager access to its five own secrets instead of the whole project.

## v3.2.1 [2026-11-04] [released: 2026-11-04] [google-cloud-run: auth-00004-q6z]
- FrontEnd: Showed every dashboard app icon in the same 6rem square, whatever the size of its image.
- BackEnd: Fixed 503 answers to matching `If-Modified-Since` requests for web app files by upgrading `support.java` to 1.0.1.
- DevEx: Made `migrate-gcp-service.py` grant per-secret access, copy renamed secrets byte-exactly, and move domains only to ready services.
- DevEx: Moved `capture-view.py` mock applications to `counters.pellicciotta.com` and `todos.pellicciotta.com`.
- Config: Deployed the GitHub OAuth secret from Secret Manager `AUTH_GITHUB_CLIENT_SECRET`, retiring `AUTH_GITHUB_PELLICCIOTTA_CLIENT_SECRET`.
- Infra: Deleted the legacy Auth Cloud Run service, job, secrets, and images from `hinolugi-apps`; Cloud SQL stays.
- Infra: Retired `auth.hinolugi.com` by deleting its Cloud Run domain mapping and DNS records.

## v3.2.0 [2026-11-04] [released: 2026-11-04] [google-cloud-run: auth-00002-g9b]
- Config: Derived the bundled mail brand from `BASE_URL`, with optional `AUTH_MAIL_BRAND_NAME`, `AUTH_MAIL_LOGO_URL`, and link overrides.
- FrontEnd: Moved demo harnesses and offline demo data from `hinolugi.com` domains to `pellicciotta.com` apps and `pellicciotta.local` users.
- FrontEnd: Fixed Admin Console and Help versions falling back to a stale `2.0.0-pre`; PWA install status now renders immediately.
- DevEx: Limited `devops.py production` smoke tests to `https://auth.pellicciotta.com`.
- Config: Removed `AUTH_HINOLUGI_*` and `AUTH_GITHUB_PELLICCIOTTA_CLIENT_ID`; `AUTH_GITHUB_CLIENT_ID` now names the single Pellicciotta GitHub OAuth App.
- BackEnd: Served production only on `auth.pellicciotta.com`, dropping the `auth.hinolugi.com` origin, mail brand, and `hinolugi.com` CORS domain.
- Infra: Moved the Artifact Registry image and Cloud Run services to `pellicciotta-apps`.

## v3.1.0 [2026-11-01] [released: 2026-11-01] [google-cloud-run: auth-00085-rmw]
- CLI: Moved the `auth-cli` session from `~/.hinolugi` to `~/.auth`, so existing CLI users sign in once more.
- Docs: Replaced the remaining old product and library names in documentation, comments, and the Insomnia collection.
- BackEnd: Fixed `upgrade-repository` rejecting any schema not named `auth`.
- BackEnd: Pointed the seeded `auth` application at `auth.pellicciotta.com` with repository version 0.19.0.
- Docs: Presented `auth.pellicciotta.com` as the default domain, including its mail brand settings and tour reports.
- DevEx: Changed the default target of `devops.py` and `capture-view.py` to `https://auth.pellicciotta.com`, smoke-testing it first.
- FrontEnd: Changed the SPA fallback API URL, fallback feedback address, form placeholders, demo data, and mail preview to `pellicciotta.com`.
- BackEnd: Made `auth.pellicciotta.com` the default origin, mail brand, CORS domain, and OAuth redirect; `auth.hinolugi.com` stays served.
- Config: Replaced the `AUTH_PELLICCIOTTA_*` mail brand settings with `AUTH_HINOLUGI_*`; `BASE_URL` now selects the Pellicciotta brand.
- Build: Changed the default API URL of the JavaScript, Python, and Java clients to `https://auth.pellicciotta.com/api`.

## v3.0.0 [2026-11-01] [released: 2026-11-01] [google-cloud-run: auth-00084-n6m]
- Build: **[breaking]** Moved Java packages to `com.pellicciotta.auth`; update Java client imports from `com.hinolugi.auth`.
- Build: **[breaking]** Changed Maven coordinates to `com.pellicciotta:auth-service`, `auth-client-java`, and `auth-server`; update dependency declarations.
- Build: **[breaking]** Renamed the JavaScript client to `@gpellicciotta/auth-client`; update dependencies and imports from `@hinolugi/auth-client`.
- Build: **[breaking]** Renamed the Python client to `auth-client`, module `auth_client`; reinstall it and update `hinolugi_auth_client` imports.
- Build: **[breaking]** Renamed the jars to `auth-*.jar`, the distribution to `auth`, and the image to `europe-west1-docker.pkg.dev/hinolugi-apps/apps/auth`.
- Build: **[breaking]** Renamed the GitHub repository to `gpellicciotta/auth`; publishing now targets its registry, and old clones should update `origin`.
- BackEnd: **[breaking]** Renamed the session cookie from `hinolugi-auth` to `auth`, which signs every user out once.
- BackEnd: Derived unconfigured mail brand names, senders, and links from the resolved origin's domain instead of HiNoLuGi values.
- Config: Set Cloud Run `command` and `args` on every deploy, so stored values can't reference a renamed jar.
- DevEx: **[breaking]** Renamed the local MySQL container to `auth-local-mysql`; remove the old `hinolugi-auth-local-mysql` container.
- Build: **[breaking]** Moved Java modules to `com.pellicciotta:support.java` 1.0.0, resolved from its renamed GitHub Packages registry.
- Config: **[breaking]** Renamed support class names to `com.pellicciotta.support`; update `AUTH_LOG_FORMATTER_TYPE` in `.env` files.
- Config: **[breaking]** Renamed the `hinolugi.auth*` loggers to `auth*`; update `<logger>` overrides and log filters that name them.
- FrontEnd: Renamed the web UI, manifest, and service worker cache to Auth, with neutral sign-in and help copy.
- FrontEnd: Removed the unused HiNoLuGi logo images from `webapp/img` and the offline cache.
- CLI: Renamed the server, `auth-cli`, `devops.py`, capture, and bootstrap banners and help text to Auth.
- BackEnd: Changed the status endpoint's `name` value from `HiNoLuGi/Auth server` to `Auth Server`.
- Docs: Renamed the product to Auth, positioned as a standalone service, and removed deployment hostnames from the README.
- Docs: Replaced stale `gcr` image references in the [CLAUDE.md](CLAUDE.md) Docker commands with `gcp.image`.
- Build: **[breaking]** Moved clients to `support-python` 1.0.0 and `@gpellicciotta/support.js` 3.0.0; rename `hinolugi_support` imports to `support_python`.
- Build: **[breaking]** Raised the JavaScript client's Node.js requirement to 22, matching `@gpellicciotta/support.js`.

## v2.2.0 [2026-10-25] [released: 2026-10-25] [google-cloud-run: auth-00083-h6n]
- Config: Configured Cloud Run to serve `auth.pellicciotta.com` alongside `auth.hinolugi.com` with dual-domain smoke checks.
- FrontEnd: Raised dark-mode link contrast on cards to meet WCAG AA via `--color-link` (`#60a5fa`).
- DevEx: Seeded the in-memory dev server with `admin@hinolugi.com` and let `--memory-db` start without `.env` files on JDK 25.
- FrontEnd: Applied cleared optional application URLs in demo mode and seeded the admin harness from the demo store.
- FrontEnd: Showed an error toast via `toastActionError` whenever an admin console action API request fails.
- FrontEnd: Made admin console section headings readable in dark mode by using `--primary-text-color` instead of hard-coded `#1e293b`.
- DevEx: Migrated the production schema through the Cloud Run job during deploy, removing local secret requirements.
- FrontEnd: Showed and linked the feedback address of the request origin's mail brand in the help view.
- BackEnd: Added the request origin's mail brand `feedback-address` to `/api/status` and `/api/server` responses.
- BackEnd: Remembered each user's creation or sign-in origin so deletion reminders and purge notices use that origin's mail brand.
- BackEnd: Fixed the account-created mail's doubled period and stray "created. to access" by naming the app in its sign-in sentence.
- BackEnd: Branded outgoing mails per public origin with a configurable sender, name, logo, and links via `<mail-brand>` settings.
- CLI: Added an optional brand origin argument to `test-mail-formats` for previewing each mail brand.
- BackEnd: Selected sign-in provider client credentials per public origin, letting `auth.pellicciotta.com` use its own GitHub app.
- BackEnd: Served CORS, remember-me cookies, and OAuth redirects per public origin via `AUTH_PUBLIC_ORIGINS` and `AUTH_CORS_ALLOWED_DOMAINS`.
- Security: Fixed CORS accepting look-alike origins such as `evilhinolugi.com` by matching whole domain labels.
- Config: Mapped `auth.pellicciotta.com` to the Cloud Run service and registered its callback with all sign-in providers.
- Docs: Documented the `pellicciotta.com` mail records and corrected the stale `hinolugi.com` SPF record in the DevOps guide.

## v2.1.1 [2026-10-23] [released: 2026-10-23] [google-cloud-run: auth-00082-sn9]
- FrontEnd: Fixed the app update and data download notifications showing raw HTML instead of working buttons.

## v2.1.0 [2026-10-23] [released: 2026-10-23] [google-cloud-run: auth-00081-7h6]
- DevEx: Added a guarded `--skip-migration` option to `devops.py production deploy` for releases without schema changes.
- FrontEnd: Fixed admin console secondary, danger, and success buttons all rendering in the default blue.
- Build: Built and pushed the server image with Cloud Build by default, selectable via the `docker.builder` property.
- FrontEnd: Added a user picker and Grant Access button to the admin console application detail card.
- FrontEnd: Added an inline Edit Details form for application name, description, and URLs to the admin console.
- FrontEnd: Showed the rotated application secret once in the admin console, with a copy button and warning.
- CLI: Replaced the `applications:create` logo URL positional argument with an optional `--logo-url` flag.
  - Migration: `applications:create NAME DESC BASE_URL --logo-url URL`.
- BackEnd: Fixed the crash on form-encoded application create or update requests that omit a description.
- FrontEnd: Showed the default auth icon on dashboard app panels for applications without a logo URL.
- DevEx: Fixed CI webapp and JS client tests by installing `hinolugi-support.js` from GitHub Packages.

## v2.0.2 [2026-10-22] [released: 2026-10-22] [google-cloud-run: auth-00080-k2m]
- BackEnd: Made the application logo URL optional via schema 0.17.0, fixing the 400 when registering apps without one.
- Docs: Updated REST API specifications, data model, and architecture documents with notification and broadcast endpoints.
- FrontEnd: Added notification inbox and administrative broadcast FAQ guides with quick navigation in HelpView.
- DevEx: Expanded capture-view presets and visual UI tour report to cover notification inbox, broadcast studio, and audit events.
- FrontEnd: Added Admin Console Notifications tab with broadcast compose, audience targeting, live preview, and system events audit viewer.
- FrontEnd: Added reactive notification bell icon, unread counter badge, user inbox view, and urgent banner in webapp.
- CLI: Added notification inbox, broadcast publishing, and system event methods to JavaScript, Python, and Java SDKs and CLI.
- BackEnd: Added server models, repository operations, REST API routes, and nightly purge for notifications and system events.
- BackEnd: Added schema migrations and data model documentation for `system-events` and `notifications` tables under version 0.16.0.
- DevEx: Adopted lockstep versioning across client SDKs and added `devops.py versions` command with pre-flight deploy validation.
- DevEx: Standardized production deployment pipeline into `devops.py` under `production` subcommands and retired `deploy-to-production.py`.
- FrontEnd: Fixed session revocation, token expiry parsing, and active device tracking in Account and Admin views.
- BackEnd: Fixed account restoration and automatic reactivation upon authentication for soft-deleted user accounts.
- FrontEnd: Added notification toast and PWA state helper methods to App with fallback handling in AdminView.
- FrontEnd: Replaced unsupported Font Awesome Pro browser icon with free window-maximize icon in Admin Console component status.
- FrontEnd: Added `promptAppInstall` method to `App` and fallback handling in `AdminView`.

## v2.0.1 [2026-09-20] [released: 2026-09-20] [google-cloud-run: auth-00079-qjs]
- FrontEnd: Reorganized Account view with unified left-aligned provider panels, activity rows, switched sessions order, and indented preferences.
- FrontEnd: Fixed Admin console UI issues across component status, user deletion, session tokens, registration, recycle bin, and logs.
- FrontEnd: Aligned Help view layout, filter contrast, section titles, and monospace changelog code styling with Counters.

## v2.0.0 [2026-09-20] [released: 2026-09-20] [google-cloud-run: auth-00078-gb2]
- FrontEnd: Standardized views, dialogs, and panels with design tokens and full dark mode contrast fixes.
- DevEx: **[breaking]** Removed client and script forwarding modules in favor of direct hinolugi-support imports; see [docs/migrating-v1-to-v2.md](docs/migrating-v1-to-v2.md).
- FrontEnd: **[breaking]** Introduced unified Admin Console consolidating user accounts, active sessions, applications, recycle bin, logs, and devtools.
- FrontEnd: **[breaking]** Replaced `AboutView` with public `HelpView` featuring search, category filters, FAQ, and Auth guides.
- FrontEnd: Redesigned Account and Preferences view into modular card deck with responsive layouts and zero mobile overflow.
- FrontEnd: Combined Account and Settings into unified Account & Preferences view with header sign-out button.
- BackEnd: Added user session token query and revocation REST endpoints.
- BackEnd: Allowed local domain names and modern top-level domains in email validation.
- FrontEnd: Added active session list and multi-device revocation controls to Account view.
- FrontEnd: Implemented System Default, Light, and Dark visual themes with instant live preview and dynamic CSS tokens.
- DevEx: Added `capture-view` CLI backed by shared `ViewCaptureEngine` with view presets and visual UI tours.
- FrontEnd: Aligned SPA stylesheets and view containers with HiNoLuGi Visual Style Guide.
- FrontEnd: Preserve deep links and return URLs across initial bootstrap and user sign-in.
- Docs: Change project license to MIT across repository and documentation.

## v1.2.0 [2026-09-12] [released: 2026-09-12] [google-cloud-run: auth-00076-m8m]
- DevEx: Provide unified devops.py CLI and shared standard-library module scripts/lib/common.py.
- DevEx: Add database snapshot and anonymization tooling with automated end-to-end test verification.
- DevEx: Reorganize repository structure by moving test suites to scripts/tests and cleaning unused files.
- BackEnd: Modernize HTML notification email templates with card layouts and relying-party context.
- BackEnd: Support optional file logging via AUTH_LOG_FILE alongside standard output.
- BackEnd: Initialize in-memory repositories at current schema version so local server startup succeeds.
- FrontEnd: Retain social provider sign-in method across OAuth redirects and session reloads.
- FrontEnd: Fix logout failure to ensure signed-in user state clears properly upon sign-out.
- CLI: Add remove-all-user-data command to delete tokens, credentials, settings, and grants.
- Docs: Update README and devops documentation for local development operations and OAuth usage.

## v1.1.1 [released: 2026-09-07] [google-cloud-run: auth-00075-kxj]
- Build: Upgrade hinolugi-support dependency to 5.1.0, replacing local web, database, and HTTP utility classes.
- Security: Provision isolated auth_test Cloud SQL database and adopt explicit safety-signaling env filenames.
- DevEx: Migrate clients/python and Cloud SQL proxy scripts onto shared hinolugi-support CliLogger.
- FrontEnd: Redirect unauthenticated visits to Account to sign-in instead of showing an error page.
- CLI: Add seed-test-data admin action generating configurable synthetic test-user accounts.
- Docs: Remove numbered heading prefixes, fix stale cross-references, and align documentation with dev-guidelines.

## v1.1.0 [2026-09-02] [released: 2026-09-02] [google-cloud-run: auth-00074-ngq]
- Security: Register Microsoft Entra ID OAuth tenant credentials and verify authentication and account linking.
- Security: Document social identity provider selection criteria and evaluation in security-adr.md.
- Architecture: Complete MySQL vs PostgreSQL evaluation and formally retain MySQL 8.0 on Google Cloud SQL.
- DevEx: Add automated deploy-to-production.py release pipeline and remove unauthoritative YAML service configs.
- FrontEnd: Fix sign-in method display after reload and display redirect error query parameters.
- CLI: Add structured logging options across Python tools and ensure mail admin commands fail when unconfigured.
- Docs: Consolidate operational and architecture guides into devops.md, mails.md, single-page-app.md, and back-end.md.

## v1.0.3 [2026-09-01] [released: 2026-09-01] [google-cloud-run: auth-00069-phv]
- FrontEnd: Prevent service worker from intercepting OAuth callback navigation during social sign-in linking.

## v1.0.2 [2026-09-01] [released: 2026-09-01] [google-cloud-run: auth-00068-qsl]
- FrontEnd: Fix provider ID field mapping, form button submission, and styling on Sign-In Methods panel.
- FrontEnd: Prevent service worker from intercepting social sign-in OAuth redirect navigation.

## v1.0.0 [2026-09-01] [released: 2026-09-01] [google-cloud-run: auth-00067-qt4]
- FrontEnd: Add release notes viewer to About view with category filters and offline service-worker support.
- FrontEnd: Manage social identities and credentials on Account and User screens with explicit OAuth linking.
- BackEnd: Expose credentials management endpoints with owner and admin access, and include provider details.
- Clients: Add provider fields to JavaScript and Python client credential models.
- BackEnd: Improve error messaging when signing in with non-existing accounts or invalid credentials.
- DevEx: Run database migration and post-deploy health verification automatically during deployment.
- DevEx: Add Testcontainers coverage exercising database schema upgrade paths.
- DevEx: Upgrade Guava to suppress terminally deprecated Unsafe startup warnings.
- Docs: Add architecture-spec.md and update devops.md with environment, pipeline, and account operational guides.

## v0.23.2 [2026-08-30]
- BackEnd: Fix upgrade-repository and reset-repository handling for dropped keys and dependent tables.
- DevEx: Fix Testcontainers MySQL test connection leak causing test deadlocks.

## v0.23.1 [2026-08-30] [released: 2026-08-30] [google-cloud-run: auth-00066-4zv]
- BackEnd: Fix social sign-in rejection for unauthenticated users.

## v0.23.0 [2026-08-30] [released: 2026-08-30] [google-cloud-run: auth-00065-tl7]
- BackEnd: Support optional per-application redirect URLs for authenticated session handoff across API and client libraries.
- BackEnd: Fix setup script SQL version comment parsing and unset token user ID representation.
- FrontEnd: Hand off authenticated sessions from dashboard application tiles using configured redirect URLs.
- FrontEnd: Move Create New User and Register Application actions from main menu to list views.
- FrontEnd: Fix Realms checkboxes layout alignment in user view.
- DevEx: Run repository test suite against throwaway Testcontainers MySQL instance in CI.

## v0.22.2 [2026-08-29] [released: 2026-08-29]
- FrontEnd: Fix race condition where default home navigation cleared relying-party deep-link redirect URLs.

## v0.22.1 [2026-08-29] [released: 2026-08-29]
- BackEnd: Ensure social sign-in sets remember-me cookie for automatic recognition upon return.
- FrontEnd: Preserve deep links and relying-party redirects on initial unauthenticated visits.

## v0.22.0 [2026-08-29] [released: 2026-08-29]
- BackEnd: Fix relying-party callback redirect parameters during social sign-in flows.
- BackEnd: Automatically grant new accounts access to originating application and drop user name uniqueness constraint.
- FrontEnd: Ensure authenticated users return to referring relying-party application from dashboard.
- FrontEnd: Fix layout overlap on Application Access grant panel revoke buttons.

## v0.21.0 [2026-08-28] [released: 2026-08-28]
- Clients: Add relying-party auth-token validation and achieve endpoint parity across Java, JS, and Python client libraries.
- BackEnd: Fix GET /api routing without trailing slash, OTP log severity, and application modification persistence.
- BackEnd: Integrate federated credentials into social sign-in with account takeover conflict rejection.
- FrontEnd: Add contextual relying-party branding to sign-in page and define shared design tokens.
- DevEx: Introduce cross-platform Python operational scripts and run JS and Python client test suites in CI.
- Docs: Update devops, requirements, and back-end guides, adding operational accounts inventory.

## v0.20.0 [2026-08-28] [released: 2026-08-28]
- Clients: Add application secret, server status, log access, and realm editing across client libraries.
- Clients: Improve Python non-JSON response error reporting and default client libraries to production URL.
- BackEnd: Add self-lockout-protected realm editing to user update endpoints.
- FrontEnd: Add Realms editor for Owner, Test, and Admin roles to user admin view.
- DevEx: Fix auth-cli version command to output installed package version.

## v0.19.2 [2026-08-28] [released: 2026-08-28]
- FrontEnd: Fix admin account recognition by resolving conflict with anonymous user placeholder ID.

## v0.19.1 [2026-08-28] [released: 2026-08-28]
- BackEnd: Add add-admin-user command granting default admin account administrative privileges.
- FrontEnd: Prevent service worker fetch crashes on browser-initiated preload requests.

## v0.19.0 [2026-08-27] [released: 2026-08-28]
- Clients: **[breaking]** Retire Java CLI module in favor of Python auth-cli.
- BackEnd: Clean up AuthService interface implementation and clarify architecture in documentation.
- FrontEnd: Add application administration, user access grant management, and granted-app dashboard filtering.
- DevEx: Add node test suite for web application in CI and fix demo mode authorization stubs.
- Docs: Rewrite single-page application documentation and document offline non-goals.

## v0.18.0 [2026-08-27] [released: 2026-08-27]
- Clients: Provide Java, Python, and JavaScript client libraries with bundled auth-cli tool.
- BackEnd: Add family-SSO token validation, application secrets, user grant management, and account data import.
- BackEnd: Implement IP request throttling, explicit social account linking, and fix database schema upgrade checks.
- FrontEnd: Add account data import button and handle mid-session authentication expiration.
- Build: Modernize Docker configuration, explicit Cloud Run environment bindings, and Gradle dependencies.
- Docs: Standardize project documentation, architecture specifications, deployment guides, and changelog.

## v0.17.* [released: 2024-02]
- BackEnd: Refactor AuthService interface with in-memory and REST implementations.
- Build: Improve Gradle build configuration and GitHub Packages publishing.

## v0.16.* [released: 2024-02-01]
- FrontEnd: Improve error reporting, sign-out redirection, and admin role verification.
- Build: Update Gradle build scripts and GitHub Packages publishing.

## v0.15.* [released: 2024-01-31]
- BackEnd: Introduce registered applications schema and REST API with simplified app-name redirection.
- BackEnd: Automatically purge unverified accounts after 24 hours and fix account creation password mail handling.
- FrontEnd: Add registered applications dashboard and improve form validation across user views.
- CLI: Add account data export and registered application management commands.

## v0.14.* [released: 2024-01-19]
- BackEnd: Purge expired credentials, separate tokens from credentials, and add user email filtering.
- CLI: Release initial full command-line client.

## v0.13.* [released: 2024-01-05]
- BackEnd: Extract core data model into dedicated service library.
- CLI: Initialize command-line client project.

## v0.12.* [released: 2024-01-03]
- BackEnd: Refactor internal service structures and code organization.

## v0.11.* [released: 2023-12-31]
- BackEnd: Decouple REST controller from direct repository access and adopt authorization code terminology.

## v0.10.* [released: 2023-12-29]
- BackEnd: Restructure architecture to decouple entity models, DTO commands, and AuthService use cases.
- BackEnd: Update database schema with credential expiry timestamps and standardized update tracking.

## v0.9.* [released: 2023-12-20]
- BackEnd: Add scheduled Cloud Run background job purging expired accounts and sending deletion warnings.
- FrontEnd: Fix mobile navigation menu toggle and persistent hover state bugs.

## v0.8.* [released: 2023-12-18]
- BackEnd: Clean up service implementation code.
- FrontEnd: Remove deprecated timezone read and write handling from account view.

## v0.7.* [released: 2023-12-15]
- BackEnd: Extract user settings into dedicated database table with CRUD endpoints and secure cookies.
- FrontEnd: Add dashboard view for HiNoLuGi apps and improve user and account view layouts.

## v0.6.* [released: 2023-12-13]
- FrontEnd: Add administrator views to manage, create, delete, and inspect user accounts and active sessions.

## v0.5.* [released: 2023-12-13]
- BackEnd: Add social sign-in redirection, customize OTP notifications, and fix CORS handling.
- FrontEnd: Standardize terminology on OTP and support customizable branding in notification flows.

## v0.4.* [released: 2023-12-10]
- BackEnd: Fix email change verification URLs, broaden token type definition, and scope auth cookies to domain.
- FrontEnd: Enable user settings configuration in web application.

## v0.2.* [released: 2023-12-03]
- BackEnd: Add initial settings schema and verify social authentication and notification emails.

## v0.1.0 [released: 2023-12-03]
- BackEnd: Initialize core authentication service, database models, and cloud infrastructure on Google Cloud.
- FrontEnd: Initialize single-page web application with custom branding and icons.
