---
# === CORE IDENTIFICATION ===
concept: Severity
slug: severity

# === CLASSIFICATION ===
category: rules
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/core-concepts/glossary.md"
chapter_number: null
pdf_page: null
section: "Severity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rule severity"
  - "severity level"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rules
extends: []
related:
  - configuration-files
  - violations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What severity levels does ESLint support?"
  - "What is the difference between warn and error in ESLint?"
  - "How do I turn off an ESLint rule?"
  - "What do the numeric severity values 0, 1, 2 mean?"
---

# Quick Definition
Severity is the level of reporting a rule is configured to run at, determining whether violations are ignored, reported as warnings, or reported as errors that affect the exit code.

# Core Definition
ESLint supports three levels of severity for rule configuration:
- `"off"` (or `0`): Do not run the rule.
- `"warn"` (or `1`): Run the rule, but do not exit with a non-zero status code based on its violations (excluding the `--max-warnings` flag).
- `"error"` (or `2`): Run the rule, and exit with a non-zero status code if it produces any violations.

# Prerequisites
- rules: Severity is a configuration property of rules

# Key Properties
1. **Three levels** -- off, warn, and error
2. **String or numeric** -- Can be specified as strings ("off", "warn", "error") or numbers (0, 1, 2)
3. **Exit code impact** -- Only "error" severity causes a non-zero exit code (unless `--max-warnings` is set)
4. **Per-rule** -- Each rule can have its own severity level
5. **Overridable** -- Can be overridden per file pattern or via inline config comments

# Construction / Recognition
- In config files: `"prefer-const": "error"` or `"prefer-const": 2`
- In inline comments: `/* eslint no-undef: "warn" */`
- In config arrays with options: `"semi": ["error", "always"]`

# Context & Application
Severity controls how ESLint handles rule violations in CI/CD and development workflows. Setting rules to "error" causes builds to fail, making them suitable for critical code quality checks. Setting rules to "warn" allows gradual adoption of new rules without breaking builds. Setting rules to "off" disables them entirely.

# Examples
From use/core-concepts/glossary.md:
- `"off"` (0): "Do not run the rule."
- `"warn"` (1): "Run the rule, but don't exit with a non-zero status code based on its violations"
- `"error"` (2): "Run the rule, and exit with a non-zero status code if it produces any violations"

# Relationships
## Builds Upon
- rules

## Related
- configuration-files
- violations
- flat-config

# Common Errors
1. Using "warning" instead of "warn" -- the correct string is "warn"
2. Forgetting that `--max-warnings` can make warnings affect the exit code too

# Common Confusions
1. **warn vs. error** -- Both run the rule and report violations; only "error" affects the exit code by default

# Source Reference
- use/core-concepts/glossary.md: Severity definition with all three levels

# Verification Notes
- High confidence: Explicitly defined with exact semantics in the glossary
