---
concept: ESLint
slug: eslint
category: tooling
subcategory: linting
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript Tools and Extensions"
chapter_number: 17
pdf_page: 653
section: "17.1 Linting with ESLint"
extraction_confidence: high
aliases:
  - linter
  - linting
prerequisites: []
extends: []
related:
  - prettier
contrasts_with: []
answers_questions:
  - "How do I write and run unit tests with Jest?"
---

# Quick Definition

ESLint is a configurable JavaScript linter that analyzes code for potential bugs, style problems, and suboptimal patterns, reporting issues like unused variables, missing semicolons, and use of `==` instead of `===`.

# Core Definition

A linter detects code that, while technically correct, is unsightly, potentially buggy, or suboptimal. ESLint is the most commonly used JavaScript linter. It defines many linting rules, has an ecosystem of plug-ins, and is fully configurable via configuration files. ESLint can detect problems like `var` instead of `let`/`const`, unused variables, `==` instead of `===`, inconsistent quoting, and missing semicolons (Flanagan, Ch. 17, pp. 653-654).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Fully configurable: enable/disable/configure individual rules.
2. Ecosystem of plug-ins for additional rules.
3. The `--fix` option can automatically fix some issues.
4. Installed via npm; run with `npx eslint`.
5. Configuration via `.eslintrc` or similar config files.

# Construction / Recognition

```bash
$ eslint code/ch17/linty.js
  1:1  error  Unexpected var, use let or const instead    no-var
  4:11 error  Expected '===' and instead saw '=='         eqeqeq
```

# Context & Application

Used in development workflows, CI/CD pipelines, and as a pre-commit hook to enforce code quality and consistency across teams.

# Examples

From the source (p. 653): Running ESLint on a factorial function reveals 6 problems including `var` usage, unused variables, wrong quote style, `==` instead of `===`, indentation errors, and missing semicolons.

# Relationships

## Builds Upon
- (None - foundational tooling concept)

## Enables
- Consistent code quality across projects

## Related
- **prettier** — Complementary tool for formatting (ESLint catches bugs; Prettier handles formatting)

## Contrasts With
- (None)

# Common Errors

- **Error**: Ignoring ESLint warnings because the code "works."
  **Correction**: ESLint warnings often catch real bugs (like `==` vs `===` or unused variables).

# Common Confusions

- **Confusion**: ESLint and Prettier do the same thing.
  **Clarification**: ESLint focuses on code quality and potential bugs. Prettier focuses on formatting. They are complementary tools.

# Source Reference

Chapter 17: JavaScript Tools and Extensions, Section 17.1, pages 653-654.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear example with output
- Uncertainties: None
- Cross-reference status: Verified
