---
# === CORE IDENTIFICATION ===
concept: Declarations Scope and Activation
slug: declarations-scope-activation

# === CLASSIFICATION ===
category: variables-scope
subcategory: activation
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Variables and assignment"
chapter_number: 13
pdf_page: null
section: "13.8 Declarations: scope and activation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - declaration behavior table

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable-scope
  - block-scoping
extends: []
related:
  - let-declaration
  - const-declaration
  - var-declaration
  - function-declarations
  - temporal-dead-zone
  - hoisting
  - early-activation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes `let` from `const` from `var`?"
  - "How do I declare and use variables with proper scoping?"
---

# Quick Definition

JavaScript declarations differ in four dimensions: scope (block vs. function vs. module), activation timing (declaration point with TDZ vs. scope start), duplicate allowance, and global object property creation.

# Core Definition

The text provides a comprehensive comparison table (Ch. 13, &sect;13.8) for all declaration types:
- `const`: Block scope, activated at declaration (TDZ), no duplicates, no global property
- `let`: Block scope, activated at declaration (TDZ), no duplicates, no global property
- `function`: Block scope (strict mode), activated at scope start, allows duplicates, creates global property
- `class`: Block scope, activated at declaration (TDZ), no duplicates, no global property
- `import`: Module scope, activated at start, no duplicates, no global property
- `var`: Function scope, activated at start (partially), allows duplicates, creates global property

# Prerequisites

- **variable-scope** -- scope is one of the key dimensions
- **block-scoping** -- most modern declarations are block-scoped

# Key Properties

1. Scope: block (const/let/class), function (var), module (import)
2. Activation: at declaration with TDZ (const/let/class), at scope start (function/import/var)
3. Duplicates: allowed for var and function only
4. Global property: only var and function
5. Function declarations are block-scoped in strict mode, function-scoped in sloppy mode

# Construction / Recognition

This is a reference concept -- recognized when comparing declaration behaviors.

# Context & Application

This comparison table is essential for understanding the behavioral differences between JavaScript's declaration types, especially when migrating from `var` to `let`/`const`.

# Examples

From the source text (Ch. 13, &sect;13.8), summarized:

| Declaration | Scope | Activation | Duplicates | Global prop |
|---|---|---|---|---|
| `const` | Block | TDZ | No | No |
| `let` | Block | TDZ | No | No |
| `function` | Block* | start | Yes | Yes |
| `class` | Block | TDZ | No | No |
| `var` | Function | start (partial) | Yes | Yes |

# Relationships

## Builds Upon
- **variable-scope** -- scope dimension
- **block-scoping** -- default scope for modern declarations

## Enables
- Informed choice between declaration types

## Related
- All declaration types and activation mechanisms

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Assuming all declarations behave the same regarding scope and activation.
  **Correction**: Each declaration type has unique scope, activation, and duplication rules.

# Common Confusions

- **Confusion**: Thinking `class` declarations are early-activated like `function` declarations.
  **Clarification**: Class declarations are subject to TDZ, not early-activated, because `extends` operands must be evaluated at the declaration point.

# Source Reference

Chapter 13: Variables and assignment, Section 13.8, lines 578-803.

# Verification Notes

- Definition source: direct from source (table format)
- Confidence rationale: Comprehensive comparison table with footnotes
- Cross-reference status: verified
