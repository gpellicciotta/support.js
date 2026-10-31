import { test, describe, vi } from 'vitest';
import assert from 'node:assert/strict';
import { addLogHandler, removeLogHandler, error, ERROR_LEVEL } from '../src/logs.mjs';

describe('fireLogEvent', () => {
  test('routes a failing handler to defaultHandler as an ERROR-level event, not the raw exception', () => {
    const failingHandler = () => {
      throw new Error('boom');
    };
    const errorMock = vi.spyOn(console, 'error').mockImplementation(() => {});
    const logMock = vi.spyOn(console, 'log').mockImplementation(() => {});
    addLogHandler(failingHandler);
    try {
      error('something happened');
    }
    finally {
      removeLogHandler(failingHandler);
    }

    assert.equal(logMock.mock.calls.length, 0);
    assert.equal(errorMock.mock.calls.length, 1);
    const [message, loggedEvent, loggedErr] = errorMock.mock.calls[0];
    errorMock.mockRestore();
    logMock.mockRestore();
    assert.match(message, /^\[error\] Log event handler failed for event/);
    assert.equal(loggedEvent.level, ERROR_LEVEL);
    assert.equal(loggedErr.message, 'boom');
  });
});
