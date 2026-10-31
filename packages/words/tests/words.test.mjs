import { describe, it } from 'vitest';
import assert from 'node:assert/strict';
import { SIMPLE_DUTCH_WORDS } from '../src/dutchwords.mjs';
import { SIMPLE_ENGLISH_WORDS } from '../src/englishwords.mjs';

describe('word lists', () => {
  for (const [name, words] of [['Dutch', SIMPLE_DUTCH_WORDS], ['English', SIMPLE_ENGLISH_WORDS]]) {
    it(`${name} list is a non-empty array of non-empty strings`, () => {
      assert.ok(Array.isArray(words));
      assert.ok(words.length > 100);
      assert.ok(words.every((word) => typeof word === 'string' && word.length > 0));
    });
  }
});
