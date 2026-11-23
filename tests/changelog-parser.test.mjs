import { test, describe } from 'vitest';
import assert from 'node:assert/strict';
import * as fs from 'node:fs';
import { parseChangelog } from '../src/changelog-parser.mjs';

describe('Changelog Parser Suite', () => {
  const sampleMarkdown = `
# Changelog

All notable changes are documented here.

## Full Change History

### vNext
- BackEnd: Expose GET and DELETE /api/users/{userId}/credentials
- SPA: Manage social identities on Account and User screens
- Docs: Condense devops.md
- [breaking] SPA: Implement native Context Action Bar feedback with [UNDO] action
- DevOps: Automate schema migration and health checks

### v1.0.2 [in development]
- Build: Fix a missing brace in RepositoryUtils
- FrontEnd: Fix sign-in silently redirecting deep links
- DevEx: Fix ui-tour.mjs
- Clients: Add provider fields to models
- Fix: Format calorie values as whole numbers

### v1.0.1 [2026-08-22] [released: 2026-08-22]
- Test: Add live SPA test suite
- Feature: Add OLED theme support
- Docs: Update requirements document

### v1.0.0 (2026-08-21)
- [breaking] Client: Native ESM exports across all clients
- Test: Expand integration test matrix

### v0.23.0 [2023-08-14] - First Useable Version
- Multi-line entry with continued text
  that wraps across indented lines.
- ADR: Record MySQL architecture decision
`;

  test('1. Parses release versions and tags correctly', () => {
    const releases = parseChangelog(sampleMarkdown);
    assert.equal(releases.length, 5);

    assert.equal(releases[0].version, 'Next');
    assert.equal(releases[0].isLatest, true);
    assert.equal(releases[0].tag, 'in development');

    assert.equal(releases[1].version, '1.0.2');
    assert.equal(releases[1].isLatest, false);
    assert.equal(releases[1].tag, 'in development');

    assert.equal(releases[2].version, '1.0.1');
    assert.equal(releases[2].isLatest, false);
    assert.equal(releases[2].tag, '2026-08-22 • released: 2026-08-22');

    assert.equal(releases[3].version, '1.0.0');
    assert.equal(releases[3].isLatest, false);
    assert.equal(releases[3].tag, '2026-08-21');

    assert.equal(releases[4].version, '0.23.0');
    assert.equal(releases[4].isLatest, false);
    assert.equal(releases[4].tag, '2023-08-14');
  });

  test('2. Correctly categorizes user-facing vs internal developer entries', () => {
    const releases = parseChangelog(sampleMarkdown);
    const vNext = releases[0];

    const internalEntries = vNext.entries.filter((e) => !e.isUserFacing);
    const userFacingEntries = vNext.entries.filter((e) => e.isUserFacing);

    assert.equal(internalEntries.length, 2); // Docs and DevOps
    assert.equal(userFacingEntries.length, 3); // BackEnd, SPA, [breaking] SPA
  });

  test('3. Properly classifies Clients (plural) prefix as client category', () => {
    const releases = parseChangelog(sampleMarkdown);
    const v102 = releases[1];

    const clientEntry = v102.entries.find((e) => e.text === 'Add provider fields to models');
    assert.ok(clientEntry, 'Clients entry should exist');
    assert.equal(clientEntry.category, 'client');
    assert.equal(clientEntry.isUserFacing, true);
  });

  test('4. Detects [breaking] change annotations', () => {
    const releases = parseChangelog(sampleMarkdown);
    const breakingEntries = releases.flatMap((r) => r.entries).filter((e) => e.isBreaking);

    assert.equal(breakingEntries.length, 2);
    assert.ok(!breakingEntries[0].text.includes('[breaking]'), 'Clean text should strip [breaking]');
    assert.ok(breakingEntries[0].isBreaking);
    assert.ok(!breakingEntries[1].text.includes('[breaking]'), 'Clean text should strip [breaking]');
    assert.ok(breakingEntries[1].isBreaking);
  });

  test('5. Appends multi-line continuation text to the previous entry', () => {
    const releases = parseChangelog(sampleMarkdown);
    const v0230 = releases[4];

    assert.equal(v0230.entries.length, 2);
    assert.equal(v0230.entries[0].text, 'Multi-line entry with continued text that wraps across indented lines.');
    assert.equal(v0230.entries[0].category, 'feature');
    assert.equal(v0230.entries[0].isUserFacing, true);
  });

  test('6. Handles maxReleases option', () => {
    const releases = parseChangelog(sampleMarkdown, { maxReleases: 2 });
    assert.equal(releases.length, 2);
    assert.equal(releases[0].version, 'Next');
    assert.equal(releases[1].version, '1.0.2');
  });

  test('7. Handles null, undefined, or empty markdown gracefully', () => {
    assert.deepEqual(parseChangelog(null), []);
    assert.deepEqual(parseChangelog(undefined), []);
    assert.deepEqual(parseChangelog(''), []);
  });

  test('9. Strips a bold **[breaking]** marker without leaving asterisks behind', () => {
    const releases = parseChangelog(`
## v4.0.0 [released: 2026-11-17]
- SPA: **[breaking]** Moved the SPA's chrome onto the vendored look.
- **[breaking]** Client: Dropped the legacy export.
- Docs: Mentioned *[breaking]* changes in prose.
`);
    const [spa, client, docs] = releases[0].entries;
    assert.equal(spa.isBreaking, true);
    assert.equal(spa.category, 'ux');
    assert.equal(spa.text, 'Moved the SPA\'s chrome onto the vendored look.');
    assert.equal(client.isBreaking, true);
    assert.equal(client.category, 'client');
    assert.equal(client.text, 'Dropped the legacy export.');
    assert.equal(docs.isBreaking, true);
    assert.equal(docs.text, 'Mentioned changes in prose.');
  });

  test('10. Marks -pre versions with isPreRelease and keeps the suffix in version by default', () => {
    const releases = parseChangelog(`
# Versioned Changes

## Version History

## v1.1.2-pre
- DevEx: Moved devops.py onto DevopsCli

## v1.1.1 [released: 2026-09-07] [google-cloud-run: auth-00075-kxj]
- Security: Escaped app-logo-url in outgoing mails
`);
    assert.equal(releases.length, 2);
    assert.equal(releases[0].version, '1.1.2-pre');
    assert.equal(releases[0].isPreRelease, true);
    assert.equal(releases[0].tag, 'in development');
    assert.equal(releases[0].entries.length, 1);
    assert.equal(releases[1].version, '1.1.1');
    assert.equal(releases[1].isPreRelease, false);
    assert.equal(releases[1].tag, 'released: 2026-09-07 • google-cloud-run: auth-00075-kxj');
  });

  test('11. Strips the -pre suffix from version when stripPreSuffix is set', () => {
    const releases = parseChangelog('## v1.1.2-pre\n\n## v1.1.1 [2026-09-07]\n', { stripPreSuffix: true });
    assert.equal(releases[0].version, '1.1.2');
    assert.equal(releases[0].isPreRelease, true);
    assert.equal(releases[0].tag, 'in development');
    assert.equal(releases[1].version, '1.1.1');
    assert.equal(releases[1].isPreRelease, false);
  });

  test('12. Accepts second-level headings only with a v prefix and a digit or Next', () => {
    const releases = parseChangelog(`
## Next Steps
- Not a release entry

## 2.0.0
- Not a release entry either

## v2.0.0-pre
- Real entry

### v1.9.0
- Older entry
`);
    assert.deepEqual(releases.map((r) => r.version), ['2.0.0-pre', '1.9.0']);
    assert.equal(releases[0].entries.length, 1);
  });

  test('13. Parses the Auth CHANGELOG.md fixture without leaving asterisks in entry text', () => {
    const content = fs.readFileSync(new URL('./fixtures/auth-changelog.md', import.meta.url), 'utf8');
    const releases = parseChangelog(content, { maxReleases: Infinity });
    assert.ok(releases.length > 10);
    assert.equal(releases[0].isPreRelease, true);
    const entries = releases.flatMap((r) => r.entries);
    assert.ok(entries.some((e) => e.isBreaking));
    const withAsterisks = entries.filter((e) => e.text.includes('**'));
    assert.deepEqual(withAsterisks.map((e) => e.text), []);
  });

  test('8. Parses real repository CHANGELOG.md without throwing', () => {
    const changelogPath = new URL('../CHANGELOG.md', import.meta.url);
    if (fs.existsSync(changelogPath)) {
      const content = fs.readFileSync(changelogPath, 'utf8');
      const releases = parseChangelog(content);
      assert.ok(releases.length > 0);
      assert.ok(releases[0].version);
      assert.ok(releases[0].tag);
      assert.strictEqual(releases[0].isLatest, true);
      assert.ok(releases.some((r) => r.entries.length > 0));
    }
  });
});
