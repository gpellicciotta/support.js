import { describe, it } from 'vitest';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import * as forms from '../src/forms.mjs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const RETIRED_MODULES = [
  'app-action-bar.mjs',
  'app-internals-view.mjs',
  'app-menu.mjs',
  'app-notification-bar.mjs',
  'app-view.mjs',
  'collection-editor.mjs',
  'component.mjs',
  'dialog.mjs',
  'home-view.mjs',
  'installer.mjs',
  'reorder.mjs',
];

const RETAINED_MODULES = [
  'canvas.mjs',
  'changelog-parser.mjs',
  'collisions.mjs',
  'colors.mjs',
  'dates.mjs',
  'dom.mjs',
  'events.mjs',
  'fireworks.mjs',
  'forms.mjs',
  'logs.mjs',
  'math.mjs',
  'matrix.mjs',
  'mock-dom.mjs',
  'net.mjs',
  'noise.mjs',
  'objects.mjs',
  'paging.mjs',
  'snowflakes.mjs',
  'storages.mjs',
  'strings.mjs',
  'vector.mjs',
];

describe('Non-UI Package Surface', () => {
  it('package.json exports no CSS, omits css from files, and ships docs', () => {
    const pkgPath = path.join(rootDir, 'package.json');
    const pkg = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
    assert.ok(pkg.exports, 'package.json should have exports field');
    assert.equal(pkg.exports['./*.mjs'], './src/*.mjs');
    assert.equal(pkg.exports['./*.css'], undefined, 'package.json must not export ./*.css');
    assert.equal(pkg.exports['./css/*.css'], undefined, 'package.json must not export ./css/*.css');
    assert.ok(!pkg.files.includes('css'), 'package.json files must not include css');
    assert.ok(!pkg.files.includes('img'), 'package.json files must not include img');
    assert.ok(pkg.files.includes('docs'), 'package.json files must include docs');
    assert.equal(
      fs.existsSync(path.join(rootDir, 'docs', 'specs', 'client-upgrade-guide.md')),
      true,
      'client-upgrade-guide.md should exist in docs/specs/',
    );
  });

  it('css/ and img/ directories and visual-style-guide.md are absent', () => {
    assert.equal(fs.existsSync(path.join(rootDir, 'css')), false, 'css/ directory should be removed');
    assert.equal(fs.existsSync(path.join(rootDir, 'img')), false, 'img/ directory should be removed');
    assert.equal(
      fs.existsSync(path.join(rootDir, 'docs', 'specs', 'visual-style-guide.md')),
      false,
      'docs/specs/visual-style-guide.md should be removed',
    );
  });

  it('retired UI modules are absent from src/', () => {
    for (const mod of RETIRED_MODULES) {
      const fullPath = path.join(rootDir, 'src', mod);
      assert.equal(fs.existsSync(fullPath), false, `Retired module src/${mod} should not exist`);
    }
  });

  it('retained modules remain present in src/', () => {
    for (const mod of RETAINED_MODULES) {
      const fullPath = path.join(rootDir, 'src', mod);
      assert.equal(fs.existsSync(fullPath), true, `Retained module src/${mod} should exist`);
    }
  });

  it('src/forms.mjs exports only pure validation functions', () => {
    assert.deepEqual(Object.keys(forms).sort(), [
      'isValidEmailAddress',
      'isValidPassword',
      'validPasswordDescription',
    ]);
  });
});
