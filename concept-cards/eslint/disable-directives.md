---
# === CORE IDENTIFICATION ===
concept: Disable Directives
slug: disable-directives

# === CLASSIFICATION ===
category: suppression
subcategory: inline suppression
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/configure/rules.md"
chapter_number: null
pdf_page: null
section: "Disable Rules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - eslint-disable
  - eslint-disable-next-line
  - eslint-enable
  - disable comments
  - eslint-disable-line

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rule-configuration
extends: []
related:
  - inline-config-comments
  - bulk-suppressions
contrasts_with:
  - inline-config-comments
  - bulk-suppressions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I disable an ESLint rule for a specific line?"
  - "How do I disable all rules for a block of code?"
  - "What is the difference between eslint-disable and eslint-disable-next-line?"
  - "How do I report unused disable directives?"
---

# Quick Definition
Disable directives are special comments (`/* eslint-disable */`, `// eslint-disable-next-line`, `// eslint-disable-line`) that suppress ESLint rule reporting for specific lines, blocks, or entire files.

# Core Definition
Disable directives use JavaScript comments to tell ESLint not to report rule violations in targeted code regions. Block-level suppression uses `/* eslint-disable */` and `/* eslint-enable */` pairs. Line-level suppression uses `// eslint-disable-line` (same line) or `// eslint-disable-next-line` (next line). All forms can target specific rules or suppress all rules. Descriptions can be added after `--` separators. The `linterOptions.reportUnusedDisableDirectives` setting (defaulting to `"warn"`) reports directives that suppress no actual violations. The `noInlineConfig` option can disable all directives.

# Prerequisites
- rule-configuration (understanding which rules are active)

# Key Properties
1. Block disable: `/* eslint-disable */` ... `/* eslint-enable */`
2. Rule-specific block: `/* eslint-disable no-alert, no-console */` ... `/* eslint-enable no-alert, no-console */`
3. Line disable: `alert("foo"); // eslint-disable-line no-alert`
4. Next-line disable: `// eslint-disable-next-line no-alert`
5. Whole-file disable: `/* eslint-disable */` at top of file (no matching enable)
6. Permanent disable: `/* eslint no-alert: "off" */` (cannot be re-enabled)
7. Descriptions after `--`: `// eslint-disable-next-line no-console -- Needed for debugging`
8. `/* eslint-enable */` without specific rules re-enables all disabled rules
9. Disabled code still needs to be syntactically valid JavaScript
10. `reportUnusedDisableDirectives` defaults to `"warn"`

# Construction / Recognition
Single-line suppression:
```js
alert("foo"); // eslint-disable-line no-alert

// eslint-disable-next-line no-alert
alert("foo");
```

Block suppression:
```js
/* eslint-disable no-alert */
alert("foo");
alert("bar");
/* eslint-enable no-alert */
```

Multi-rule, multi-line format:
```js
/* eslint-disable-next-line
  no-alert,
  quotes,
  semi
*/
alert("foo");
```

# Context & Application
Disable directives should be used sparingly and with documented reasons. The ESLint documentation recommends preferring configuration files for consistent rule handling. When used, they should be temporary solutions with follow-up tasks, documented with description comments, and reviewed during code review.

# Examples
From `use/configure/rules.md`: Plugin rules work with disable directives using the `namespace/rule-name` format:
```js
foo(); // eslint-disable-line example/rule-name
```

Reporting unused directives:
```js
export default defineConfig([{
  linterOptions: { reportUnusedDisableDirectives: "error" },
}]);
```

# Relationships
## Builds Upon
- rule-configuration (disables are meaningful only when rules are active)

## Enables
- Targeted suppression of known false positives
- Temporary rule exceptions during migration

## Related
- bulk-suppressions (project-wide suppression for rule adoption)

## Contrasts With
- inline-config-comments: `/* eslint rule: "off" */` permanently sets severity; `/* eslint-disable rule */` suppresses reporting but can be re-enabled. The `"off"` form cannot be re-enabled with `eslint-enable`.
- bulk-suppressions: Disable directives are manual, per-location; bulk suppressions are automated, project-wide.

# Common Errors
1. Using `/* eslint-enable */` without specifying rules, accidentally re-enabling all disabled rules
2. Placing `// eslint-disable-next-line` on the wrong line (it affects only the immediately following line)
3. Using disable directives as the default solution instead of fixing the underlying issue

# Common Confusions
1. Confusing `/* eslint-disable */` (suppress reporting) with `/* eslint rule: "off" */` (set severity) -- the latter cannot be re-enabled
2. Thinking disabled code is not parsed -- ESLint still parses it, so it must be valid syntax

# Source Reference
- `sources-md/eslint/use/configure/rules.md`, section "Disable Rules"

# Verification Notes
Extracted from rules configuration documentation. All directive forms and their behavior verified against examples.
