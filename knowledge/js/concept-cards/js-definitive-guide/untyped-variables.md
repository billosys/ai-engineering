---
# === CORE IDENTIFICATION ===
concept: Untyped Variables
slug: untyped-variables

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: variables
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 73
section: "3.10.1 Declarations with let and const"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - dynamically typed variables
  - dynamic typing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variables-overview
  - type-system-overview
extends: []
related:
  - let-and-const-declarations
  - type-coercion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

JavaScript variables are untyped: declarations do not specify a type, and any variable can hold a value of any type, with the type allowed to change at any time during execution.

# Core Definition

"There is no type associated with JavaScript's variable declarations. A JavaScript variable can hold a value of any type." "It is perfectly legal (but generally poor programming style) in JavaScript to assign a number to a variable and then later assign a string to that variable." (p. 73)

# Prerequisites

- **variables-overview** — Must understand what variables are
- **type-system-overview** — Must understand that values have types even though variables don't

# Key Properties

1. Variable declarations do not specify types
2. Any variable can hold any type of value
3. A variable's type can change during execution
4. Values always have types; variables do not
5. TypeScript and Flow add optional type annotations (mentioned in footnote)
6. Changing a variable's type is legal but "generally poor programming style"

# Construction / Recognition

```javascript
let i = 10;
i = "ten";      // Legal: i changed from number to string
```

# Context & Application

Untyped variables give JavaScript flexibility but can lead to type-related bugs. This is why TypeScript (which adds static types) has become popular. Understanding that values are typed while variables are not is key to understanding JavaScript's type system.

# Examples

From the source text (p. 73):
```javascript
let i = 10;
i = "ten";
```

# Relationships

## Builds Upon
- **variables-overview** — Extends understanding of variables
- **type-system-overview** — Values have types; variables do not

## Enables
- Understanding why TypeScript exists
- Understanding dynamic dispatch and duck typing

## Related
- **type-coercion** — Untyped variables + type coercion = flexible but error-prone

## Contrasts With
- Statically typed languages like Java, C, TypeScript

# Common Errors

- **Error**: Accidentally storing the wrong type in a variable.
  **Correction**: Use meaningful variable names and consider TypeScript for large projects.

# Common Confusions

- **Confusion**: JavaScript has no type system.
  **Clarification**: JavaScript values always have types. It is the variables that are untyped — a crucial distinction.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.10.1, page 73.

# Verification Notes

- Definition source: Direct quote from p. 73
- Confidence rationale: High — clearly stated
- Uncertainties: None
- Cross-reference status: Verified
