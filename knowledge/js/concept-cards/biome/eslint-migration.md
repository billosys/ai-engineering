---
# === CORE IDENTIFICATION ===
concept: ESLint Migration
slug: eslint-migration

# === CLASSIFICATION ===
category: migration
subcategory: ESLint and Prettier migration
tier: advanced

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "guides/migrate-eslint-prettier.mdx"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint/Prettier migration"
  - "biome migrate eslint"
  - "biome migrate prettier"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-configuration
  - biome-cli
extends: []
related:
  - vcs-integration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I migrate from ESLint/Prettier to Biome?"
---

# Quick Definition
Biome provides `biome migrate eslint` and `biome migrate prettier` commands that read existing ESLint/Prettier configurations and translate them into equivalent Biome settings.

# Core Definition
Biome offers dedicated migration commands for transitioning from ESLint and Prettier. `biome migrate eslint --write` reads the ESLint configuration (both legacy `.eslintrc` and flat config formats), resolves plugins and shared configs via Node.js, migrates `.eslintignore`, and overwrites `biome.json` with equivalent rules. It handles plugins like TypeScript ESLint, ESLint React, JSX A11y, and ESLint Unicorn. `biome migrate prettier --write` reads Prettier configuration and translates formatting options. Both commands support the `--write` flag to apply changes directly. By default, "inspired" rules (rules where Biome deviates from the ESLint original) are not migrated unless `--include-inspired` is specified.

# Prerequisites
- biome-configuration: Must understand biome.json to review migration output.
- biome-cli: Must know how to run Biome commands.

# Key Properties
1. `biome migrate eslint --write` translates ESLint rules to Biome equivalents.
2. `biome migrate prettier --write` translates Prettier formatting options.
3. Supports legacy (`.eslintrc.json`) and flat ESLint config formats.
4. Requires Node.js to resolve plugins and shared configurations.
5. Migrates `.eslintignore` patterns.
6. `--include-inspired` migrates rules where Biome's implementation differs from ESLint's.
7. The migration disables `recommended` rules and explicitly enables individual rules from the ESLint config.
8. Does not support YAML, TOML, or JSON5 configuration formats.
9. Biome uses `camelCaseRuleName` while ESLint uses `kebab-case-rule-name`.
10. The migration may not produce identical behavior due to intentional deviations in rule implementations.

# Construction / Recognition
To migrate from ESLint and Prettier:
1. Run `biome migrate eslint --write` to translate ESLint rules.
2. Run `biome migrate prettier --write` to translate formatting options.
3. Review the generated `biome.json` for accuracy.
4. Enable VCS integration (recommended since both ESLint and Prettier respect VCS ignore files).
5. Optionally use `--include-inspired` if you want rules that deviate from ESLint originals.

# Context & Application
Used as a one-time operation when transitioning a project from ESLint/Prettier to Biome. The migration commands lower the barrier to adoption by automatically translating existing configurations. Post-migration review is important since Biome may handle some rules differently.

# Examples
From the source, migrating an ESLint configuration:

Given `.eslintrc.json`:
```json
{
  "extends": ["plugin:unicorn/recommended"],
  "plugins": ["unicorn"],
  "globals": { "Global1": "readonly" },
  "rules": { "eqeqeq": "error" },
  "overrides": [{ "files": ["tests/**"], "rules": { "eqeqeq": "off" } }]
}
```

Running `biome migrate eslint --write` produces:
```json
{
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": false,
      "complexity": { "noForEach": "error", "noStaticOnlyClass": "error" },
      "suspicious": { "noDoubleEquals": "error" }
    }
  },
  "javascript": { "globals": ["Global1"] },
  "overrides": [
    { "include": ["tests/**"], "linter": { "rules": { "suspicious": { "noDoubleEquals": "off" } } } }
  ]
}
```

Prettier migration: `biome migrate prettier --write` reads `.prettierrc.json` and translates `useTabs`, `singleQuote`, `tabWidth`, and overrides into Biome's formatter configuration.

(From guides/migrate-eslint-prettier.mdx)

# Relationships
## Builds Upon
- biome-configuration
- biome-cli
## Enables
None directly.
## Related
- vcs-integration (recommended after migration since ESLint/Prettier respect VCS ignores)
## Contrasts With
None.

# Common Errors
1. Expecting exact behavioral parity after migration -- Biome intentionally deviates from some ESLint rules.
2. Using YAML or TOML ESLint/Prettier configs, which are not supported by the migration command.
3. Running migration without Node.js available, which prevents resolving plugins.
4. Not reviewing the generated config, especially the `recommended: false` setting.

# Common Confusions
1. Thinking migration is reversible or incremental -- it overwrites the existing `biome.json`.
2. Not understanding that `--include-inspired` adds rules whose behavior differs from their ESLint counterparts.
3. Confusing Biome's `camelCase` rule names with ESLint's `kebab-case` names when reviewing migration output.

# Source Reference
- guides/migrate-eslint-prettier.mdx, "Migrate from ESLint" and "Migrate from Prettier" sections

# Verification Notes
Documented with before/after configuration examples for both ESLint and Prettier. High confidence.
