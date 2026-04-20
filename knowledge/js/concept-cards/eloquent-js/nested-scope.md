---
# === CORE IDENTIFICATION ===
concept: Nested Scope
slug: nested-scope

# === CLASSIFICATION ===
category: functions
subcategory: binding-visibility
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Functions"
chapter_number: 3
pdf_page: null
section: "Nested scope"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - scope nesting
  - nested functions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scope
  - local-scope
  - function-definition
extends:
  - scope
related:
  - lexical-scoping
  - closure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is scope?"
  - "What must I know before understanding closures?"
---

# Quick Definition

Nested scope occurs when blocks and functions are created inside other blocks and functions, producing multiple degrees of locality where inner scopes can access bindings from outer scopes.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 173-176 of 03-functions.md): "JavaScript distinguishes not just global and local bindings. Blocks and functions can be created inside other blocks and functions, producing multiple degrees of locality."

# Prerequisites

- **scope**: Nested scope builds on the general concept of scope.
- **local-scope**: Understanding that functions create local scopes.
- **function-definition**: Functions can be defined inside other functions.

# Key Properties

1. Blocks and functions can be nested to arbitrary depth.
2. Inner scopes can see bindings from all containing (outer) scopes.
3. Outer scopes cannot see bindings from inner scopes.
4. When bindings have the same name, the innermost one is visible (shadowing).

# Construction / Recognition

## To Construct/Create:
Define a function or block inside another function or block.

## To Identify/Recognize:
Functions defined inside other functions, or blocks nested within blocks.

# Context & Application

Nested scope is the structural basis for closures and for organizing complex functions that use helper functions internally.

# Examples

**Example 1** (Ch 3, lines 183-198 of 03-functions.md):
```javascript
const hummus = function(factor) {
  const ingredient = function(amount, unit, name) {
    let ingredientAmount = amount * factor;
    if (ingredientAmount > 1) {
      unit += "s";
    }
    console.log(`${ingredientAmount} ${unit} ${name}`);
  };
  ingredient(1, "can", "chickpeas");
  ingredient(0.25, "cup", "tahini");
};
```
"The code inside the `ingredient` function can see the `factor` binding from the outer function, but its local bindings, such as `unit` or `ingredientAmount`, are not visible in the outer function."

# Relationships

## Builds Upon
- **scope** -- Nested scope extends scope to multiple levels.
- **local-scope** -- Each nested function/block has its own local scope.

## Enables
- **lexical-scoping** -- The rule governing how nested scopes resolve bindings.
- **closure** -- Closures depend on nested scope to capture bindings.

## Related
- **function-definition** -- Functions create the scopes that are nested.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Assuming an outer function can access bindings from an inner function.
  **Correction**: Scope visibility goes inward only -- inner scopes see outer bindings, not the reverse.

# Common Confusions

- **Confusion**: Nested scope means bindings "leak" outward.
  **Clarification**: Inner bindings are invisible to outer scopes. Only the inward direction of visibility works.

# Source Reference

Chapter 3: Functions, Section "Nested scope", lines 170-212 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 173-176)
- Confidence rationale: Explicit section with example
- Cross-reference status: verified against lexical-scoping and closure sections
