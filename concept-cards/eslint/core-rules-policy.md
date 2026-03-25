---
# === CORE IDENTIFICATION ===
concept: Core Rules Policy
slug: core-rules-policy

# === CLASSIFICATION ===
category: maintenance
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "contribute/core-rules.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint core rules"
  - "frozen rules"
  - "core rule contribution policy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - rules
extends: []
related:
  - rule-deprecation-policy
  - eslint-architecture
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are ESLint core rules maintained?"
  - "What does it mean for a rule to be frozen?"
  - "What is the file structure for a core rule?"
  - "What naming conventions do core rules follow?"
  - "What happens after a core rule is feature complete?"
---

# Quick Definition
ESLint's core rules policy defines how built-in rules are structured, named, tested, and maintained, including the concept of "frozen" rules that receive only bug fixes and ECMAScript/TypeScript compatibility updates.

# Core Definition
Core rules are the lint rules included in the ESLint package itself. Each core rule consists of three files: a source file in `lib/rules/`, a test file in `tests/lib/rules/`, and a Markdown documentation file in `docs/src/rules/`. Core rules follow the same API as custom rules but must adhere to additional conventions. Rules use a standard module structure with `meta` (containing `type`, `docs`, `fixable`, `schema`) and `create` (returning visitor callbacks) properties.

The frozen rules concept is central to ESLint's maintenance strategy. When a rule is considered feature complete (catches 80%+ of expected violations and covers the majority of common exceptions), it is marked as frozen. Frozen rules still receive bug fixes, ECMAScript compatibility updates, and TypeScript compatibility updates, but will not receive new options unless an option is the only way to fix a bug or support a new ECMAScript feature. Users who need modifications to frozen rules are advised to copy the rule source and customize it.

Rule naming follows specific conventions: dashes between words, `no-` prefix for rules that disallow something (e.g., `no-eval`), and short names without prefix for rules enforcing inclusion.

# Prerequisites
- eslint: Basic ESLint knowledge
- rules: Understanding of ESLint rules

# Key Properties
1. **Three-file structure** -- Each core rule has a source file, test file, and documentation file
2. **Standard module format** -- Rules export `meta` and `create` properties
3. **Frozen rules** -- Feature-complete rules are frozen and receive only bug fixes and compatibility updates
4. **80% threshold** -- Rules are considered feature complete when they catch 80%+ of expected violations
5. **No new formatting rules** -- ESLint has deprecated formatting rules in favor of dedicated formatters
6. **Performance testing** -- Core rule changes can be benchmarked with `npm run perf`
7. **RuleTester required** -- All core rules must have unit tests using the `RuleTester` utility
8. **Naming conventions** -- `no-` prefix for disallowing, short names for enforcing

# Construction / Recognition
Core rule source file structure:
```javascript
module.exports = {
  meta: {
    type: "suggestion",
    docs: {
      description: "disallow unnecessary semicolons",
      recommended: true,
      url: "https://eslint.org/docs/rules/no-extra-semi"
    },
    fixable: "code",
    schema: []
  },
  create: function(context) {
    return {
      // visitor callbacks
    };
  }
};
```

# Context & Application
The core rules policy governs ESLint's approach to long-term rule maintenance. The frozen rules concept is particularly important because it sets expectations for the community: once a rule is frozen, feature requests for new options will be declined. This encourages the plugin ecosystem to fill gaps rather than expanding core rules indefinitely. Contributors must understand these policies before submitting core rule PRs.

# Examples
From contribute/core-rules.md:
- "When rules are feature complete, they are marked as frozen (indicated with [snowflake emoji] in the documentation)."
- "If you find that a frozen rule would work better for you with a change, we recommend copying the rule source code and modifying it to fit your needs."

Performance testing example:
```bash
$ git checkout main && npm run perf
Performance budget ok: 1394.689313ms (limit: 3409.090909090909ms)
$ git checkout my-rule-branch && npm run perf
Performance budget ok: 1443.736547ms (limit: 3409.090909090909ms)
```

# Relationships
## Part Of
- eslint

## Related
- rule-deprecation-policy
- eslint-architecture

## Contrasts With
- Plugin rules (not subject to core contribution conventions or frozen status)

# Common Errors
1. Submitting a PR to add options to a frozen rule -- frozen rules accept only bug fixes and compatibility updates
2. Not including all three files (source, test, docs) when contributing a core rule
3. Using incorrect naming conventions for rule identifiers

# Common Confusions
1. **Frozen vs. deprecated** -- Frozen rules are still actively maintained for bugs and compatibility; deprecated rules are being phased out
2. **Core rules vs. custom rules** -- They share the same API, but core rules have additional contribution requirements

# Source Reference
- contribute/core-rules.md: Full core rule contribution guide including file structure, naming, testing, and frozen policy

# Verification Notes
- High confidence: Directly documented policies with clear definitions
- Frozen rule definition and 80% threshold taken verbatim from documentation
