---
# === CORE IDENTIFICATION ===
concept: Flat Config
slug: flat-config

# === CLASSIFICATION ===
category: core
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/core-concepts/glossary.md"
chapter_number: null
pdf_page: null
section: "Flat Config"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "flat configuration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - configuration-files
extends:
  - configuration-files
related:
  - eslint
contrasts_with:
  - legacy-config

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is flat config in ESLint?"
  - "Why is it called flat config?"
  - "What replaced .eslintrc?"
  - "What is the difference between flat config and legacy config?"
---

# Quick Definition
Flat config is the current ESLint configuration file format, using a single `eslint.config.(c|m)?js` file where all configuration nesting is done within one file rather than across multiple files in subdirectories.

# Core Definition
Flat config is the current configuration format for ESLint, named because all nesting must be done within a single configuration file. This contrasts with the legacy config format, which allowed `.eslintrc.*` configuration files to be nested in subdirectories throughout a project. Flat config files are named in the format `eslint.config.(c|m)?js` and export a config array.

# Prerequisites
- configuration-files: Flat config is a specific format for ESLint configuration files

# Key Properties
1. **Single file** -- All configuration is consolidated in one file at the project root
2. **No directory nesting** -- Unlike legacy config, configuration files cannot be placed in subdirectories
3. **Named format** -- `eslint.config.js`, `eslint.config.cjs`, or `eslint.config.mjs`
4. **Array export** -- Exports a config array of config objects
5. **Current standard** -- The active, recommended config format (legacy is superseded)

# Construction / Recognition
- File named `eslint.config.js` (or `.cjs`/`.mjs` variants) at project root
- Exports an array of configuration objects
- Uses file pattern matching within config objects for targeting

# Context & Application
Flat config was introduced to simplify ESLint configuration by eliminating the confusion of cascading config files across directories. All configuration intent is visible in one place. The migration from legacy to flat config is a one-time project setup change.

# Examples
From use/core-concepts/glossary.md:
- "'Flat' config files are named as such because all nesting must be done in one configuration file."
- "In contrast, the 'Legacy' config format allowed nesting configuration files in sub-directories within a project."

# Relationships
## Builds Upon
- configuration-files

## Related
- eslint
- rules
- plugins

## Contrasts With
- legacy-config: Legacy format used `.eslintrc.*` files nested across subdirectories

# Common Errors
1. Creating multiple config files in subdirectories as in legacy config -- flat config requires a single file
2. Using `.eslintrc.*` naming -- this triggers legacy config mode

# Common Confusions
1. **Flat vs. legacy** -- Flat config uses one file; legacy allowed cascading files in subdirectories. Flat config is the current recommended approach

# Source Reference
- use/core-concepts/glossary.md: Flat Config and Legacy Config definitions

# Verification Notes
- High confidence: Explicitly defined in the glossary with clear contrast to legacy config
