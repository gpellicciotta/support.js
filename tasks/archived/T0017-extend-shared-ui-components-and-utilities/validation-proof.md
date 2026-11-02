### Changes Implemented

- `js/formutils.mjs`: Added `setButtonLoading(buttonEl, isLoading, loadingText)` managing button state and spinner.
- `js/utils.mjs`: Added `MONTH_NAMES`, `formatHumanDateTime`, and `formatDetailedRelativeTime`.
- `js/component.mjs`: Added `data-ui-state` tracking (`ready`, `updating`, `error`), flexible operation overloads, and top progress hooks.
- `js/local-usage-tracking.mjs`: Ported usage tracking and pinning store backed by `localStorage`.
- `js/app-notification-bar.mjs` & `css/notification-bar.css`: Ported collapsible notification banner component and stylesheet.
- `js/app-action-bar.mjs` & `css/action-bar.css`: Ported responsive action bar component and stylesheet.
- `css/progress.css`: Ported 3px indeterminate top progress bar stylesheet.
- `js/hinolugi-auth-redirect.mjs`: Added generic SSO redirect utility for HiNoLuGi services.

### Validation

- Executed `npm test`: all 154 tests passed across 32 suites.
- Executed prettier on newly created and modified modules.
