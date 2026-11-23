/**
 * Form field validation helpers.
 */

/**
 * Checks whether a string is a valid email address.
 *
 * @param {string} email
 * @returns {boolean} True if email is non-empty and matches standard email format.
 */
export function isValidEmailAddress(email) {
  if (!email) {
    return false;
  }
  if (email.indexOf('@') <= 0) {
    return false;
  }
  return /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email);
}

/**
 * Checks whether a string is a valid password (at least 6 characters).
 *
 * @param {string} password The password to validate.
 * @returns {boolean} True if password has at least 6 characters.
 */
export function isValidPassword(password) {
  if (!password || password.length < 6) {
    return false;
  }
  return true;
}

/**
 * Human-readable description of what constitutes a valid password.
 *
 * @returns {string} Description of valid password requirements.
 */
export function validPasswordDescription() {
  return 'minimally 6 letters';
}
