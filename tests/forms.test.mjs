import { test, describe } from 'vitest';
import assert from 'node:assert/strict';
import {
  isValidEmailAddress,
  isValidPassword,
  validPasswordDescription,
} from '../src/forms.mjs';

describe('validation helpers', () => {
  test('isValidEmailAddress validates email format', () => {
    assert.equal(isValidEmailAddress('test@example.com'), true);
    assert.equal(isValidEmailAddress('invalid-email'), false);
    assert.equal(isValidEmailAddress(''), false);
    assert.equal(isValidEmailAddress(null), false);
  });

  test('isValidEmailAddress accepts plus addressing and long top-level domains, like Auth', () => {
    assert.equal(isValidEmailAddress('user+tag@example.com'), true);
    assert.equal(isValidEmailAddress('first.last@sub.example.info'), true);
    assert.equal(isValidEmailAddress('x@example.technology'), true);
    assert.equal(isValidEmailAddress('u_1@ex-ample.org'), true);
    assert.equal(isValidEmailAddress('@example.com'), false);
    assert.equal(isValidEmailAddress('a@b'), false);
    assert.equal(isValidEmailAddress('a@b.c'), false);
    assert.equal(isValidEmailAddress('a b@c.com'), false);
  });

  test('isValidPassword rejects short passwords', () => {
    assert.equal(isValidPassword(''), false);
    assert.equal(isValidPassword(null), false);
    assert.equal(isValidPassword('12345'), false);
    assert.equal(isValidPassword('123456'), true);
  });

  test('validPasswordDescription returns rule description', () => {
    assert.equal(validPasswordDescription(), 'minimally 6 letters');
  });
});
