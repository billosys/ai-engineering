---
# === CORE IDENTIFICATION ===
concept: Rule Suggestions
slug: rule-suggestions

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
section: "Suggestion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "suggestion"
  - "rule suggestion"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rules
  - violations
extends: []
related:
  - rule-fixes
contrasts_with:
  - rule-fixes

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an ESLint suggestion?"
  - "How do suggestions differ from fixes?"
  - "Can suggestions be applied automatically?"
---

# Quick Definition
A suggestion is an optional augmentation to a rule violation that describes how one may manually adjust the code to address the violation, but which may change application logic.

# Core Definition
Suggestions differ from fixes in two key ways: they may change application logic (making them unsafe to apply automatically), and they cannot be applied through the ESLint CLI. Suggestions are only available through editor integrations, which may choose to present them to the developer for manual application. Rules that provide suggestions are marked with the lightbulb icon in the rules documentation.

# Prerequisites
- rules: Suggestions are produced by rules
- violations: Suggestions are attached to specific violations

# Key Properties
1. **Unsafe** -- May change application logic and code behavior
2. **Manual only** -- Cannot be applied via the CLI; only available through editor integrations
3. **Optional** -- Not all rules provide suggestions; a rule may provide suggestions instead of or in addition to fixes
4. **Editor-integrated** -- Editor extensions present suggestions for the developer to accept or reject

# Construction / Recognition
- Appear in editor integrations as suggested changes
- Rules with suggestions are marked with the lightbulb icon in documentation
- Cannot be triggered from the command line

# Context & Application
Suggestions are used when a rule detects a problem but the correction might alter program behavior. The developer must review and consciously choose to apply the suggestion. This is common for rules that detect patterns that are usually-but-not-always problematic.

# Examples
From use/core-concepts/index.md:
- "Suggestions may change application logic and so cannot be automatically applied."
- "Suggestions cannot be applied through the ESLint CLI and are only available through editor integrations."

# Relationships
## Builds Upon
- rules
- violations

## Contrasts With
- rule-fixes: Fixes are safe and can be automatically applied; suggestions are unsafe and require manual application

# Common Errors
1. Trying to apply suggestions via `--fix` -- the CLI only applies fixes, not suggestions
2. Assuming suggestions are always correct -- they may change code behavior and require careful review

# Common Confusions
1. **Suggestions vs. fixes** -- Fixes are safe (no behavior change) and auto-applicable; suggestions may alter behavior and require manual intervention

# Source Reference
- use/core-concepts/index.md: Rule Suggestions section
- use/core-concepts/glossary.md: Suggestion definition

# Verification Notes
- High confidence: Explicitly defined in both source files
- The two key differences (unsafe, editor-only) are stated directly
