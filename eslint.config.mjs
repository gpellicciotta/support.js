import js from '@eslint/js';
import stylistic from '@stylistic/eslint-plugin';
import globals from 'globals';

export default [
  { ignores: ['node_modules/', 'packages/words/src/'] },
  js.configs.recommended,
  {
    files: ['**/*.mjs'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals: { ...globals.browser, ...globals.node },
    },
  },
  stylistic.configs.customize({ indent: 2, quotes: 'single', semi: true, braceStyle: 'stroustrup', commaDangle: 'always-multiline', arrowParens: true }),
  {
    files: ['**/*.mjs'],
    rules: {
      curly: ['error', 'all'],
      '@stylistic/max-len': ['error', { code: 120, ignoreUrls: true, ignoreStrings: true, ignoreTemplateLiterals: true, ignoreRegExpLiterals: true, ignoreComments: true }],
      '@stylistic/linebreak-style': 'off',
      '@stylistic/max-statements-per-line': 'off',
      'no-unused-vars': ['error', { args: 'none', caughtErrors: 'none' }],
      'no-useless-assignment': 'warn',
      '@stylistic/operator-linebreak': 'off',
      '@stylistic/lines-between-class-members': 'off',
      '@stylistic/quote-props': 'off',
      '@stylistic/multiline-ternary': 'off',
      '@stylistic/indent-binary-ops': 'off',
      '@stylistic/no-multiple-empty-lines': ['error', { max: 2 }],
    },
  },
];
