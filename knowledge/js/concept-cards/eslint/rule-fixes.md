---
# === CORE IDENTIFICATION ===
concept: Rule Fixes
slug: rule-fixes

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
section: "Fix"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "fix"
  - "auto-fix"
  - "automatic fix"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rules
  - violations
extends: []
related:
  - rule-suggestions
contrasts_with:
  - rule-suggestions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an ESLint fix?"
  - "How do automatic fixes work in ESLint?"
  - "What does the --fix flag do?"
  - "Are ESLint fixes safe to apply?"
---

# Quick Definition
A fix is an optional augmentation to a rule violation that describes how to automatically correct the violation without changing application logic.

# Core Definition
Fixes are safe automatic corrections attached to rule violations. They correct the violation without changing application logic. When ESLint is run with the `--fix` flag, it attempts to apply as many fixes as possible, though there is no guarantee that all fixes will be applied. Fixes may also be applied by editor extensions. Rules that provide fixes are marked with the wrench icon in the rules documentation.

# Prerequisites
- rules: Fixes are produced by rules
- violations: Fixes are attached to specific violations

# Key Properties
1. **Safe** -- Fixes do not change application logic or code behavior
2. **Automatic** -- Can be applied via the `--fix` CLI flag or editor extensions
3. **Best-effort** -- ESLint attempts to apply as many fixes as possible but does not guarantee all will be applied
4. **Optional** -- Not all rules provide fixes

# Construction / Recognition
- Apply fixes via CLI: `eslint --fix .`
- Apply fixes via editor extensions (e.g., ESLint VS Code extension)
- Rules with fixes are marked with the wrench icon in documentation

# Context & Application
Fixes are used in development workflows to automatically correct common code issues. They are typically applied during editing (via editor integrations) or as a pre-commit step. Because they are safe by design, they can be applied in bulk without manual review.

# Examples
From use/core-concepts/index.md:
- "Fixes safely correct the violation without changing application logic."
- "Fixes may be applied automatically with the `--fix` command line option and via editor extensions."

From use/core-concepts/glossary.md:
- "ESLint attempts to apply as many fixes as possible in a report when run with the `--fix` flag, though there is no guarantee that all fixes will be applied."

# Relationships
## Builds Upon
- rules
- violations

## Related
- configuration-files

## Contrasts With
- rule-suggestions: Suggestions are unsafe and cannot be applied automatically via CLI

# Common Errors
1. Assuming all rule violations have fixes -- only some rules provide fixes
2. Expecting `--fix` to apply every available fix -- some fixes may conflict and ESLint applies them on a best-effort basis

# Common Confusions
1. **Fixes vs. suggestions** -- Fixes are safe and automatically applied; suggestions may change behavior and require manual application through an editor

# Source Reference
- use/core-concepts/index.md: Rule Fixes section
- use/core-concepts/glossary.md: Fix definition

# Verification Notes
- High confidence: Explicitly defined in both source files
- Safety and automatic application properties directly from source text
