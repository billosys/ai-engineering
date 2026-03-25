---
# === CORE IDENTIFICATION ===
concept: Violations
slug: violations

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
section: "Violation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "violation"
  - "rule violation"
  - "lint error"
  - "lint warning"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rules
extends: []
related:
  - severity
  - rule-fixes
  - rule-suggestions
  - formatters-linting
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an ESLint violation?"
  - "What information does a violation contain?"
  - "Can violations include automatic fixes?"
---

# Quick Definition
A violation is an indication from a rule that an area of code does not meet the rule's expectation, including a source range and an error message.

# Core Definition
When a rule detects that code does not match its expected pattern, it produces a violation. Each violation indicates a range in source code and an error message explaining the problem. Violations may also optionally include a fix (safe automatic correction) and/or suggestions (potentially unsafe corrections requiring manual application). The collection of all violations from a linting run forms the report.

# Prerequisites
- rules: Violations are produced by rules checking code against expectations

# Key Properties
1. **Source range** -- Identifies the exact location in source code
2. **Error message** -- Explains what expectation was not met
3. **Optional fix** -- May include a safe automatic correction
4. **Optional suggestions** -- May include potentially unsafe corrections
5. **Aggregated into reports** -- All violations from a run are collected into a report for formatting

# Construction / Recognition
- Violations appear in CLI output with file path, line number, column, message, and rule name
- Violations are formatted by the configured formatter (default: stylish)

# Context & Application
Violations are the primary output of ESLint. They inform developers about code issues and, depending on severity, may cause the linting process to exit with a non-zero status code. Violations with fixes can be automatically resolved; those with suggestions require developer intervention.

# Examples
From use/core-concepts/glossary.md:
- "An indication from a rule that an area of code doesn't meet the expectation of the rule."
- "Rule violations indicate a range in source code and error message explaining the violation."
- "Violations may also optionally include a fix and/or suggestions that indicate how to improve the violating code."

# Relationships
## Builds Upon
- rules
- abstract-syntax-tree

## Enables
- rule-fixes
- rule-suggestions

## Related
- severity
- formatters-linting

# Common Errors
1. Confusing violations with runtime errors -- violations are static analysis findings, not execution failures
2. Ignoring violations by suppressing all warnings rather than addressing underlying issues

# Common Confusions
1. **Violations vs. errors** -- "Error" is a severity level; a violation can be at any severity (warn or error)

# Source Reference
- use/core-concepts/glossary.md: Violation definition

# Verification Notes
- High confidence: Explicitly defined in the glossary with clear properties
