---
concept: Class Expression
slug: class-expression
category: classes
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.2.2 Class expressions"
extraction_confidence: high
aliases:
  - "anonymous class"
  - "named class expression"
prerequisites:
  - class-declaration
extends: []
related:
  - function-declaration-vs-expression
contrasts_with: []
answers_questions:
  - "Can classes be created as expressions?"
---

# Quick Definition

Class expressions create class values inline, either anonymously (`class { }`) or with a name accessible only inside the class body.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, there are two kinds of class definitions: class declarations and class expressions. Class expressions can be anonymous (`const Person = class { }`) or named (`const Person = class MyClass { }`). The name of a named class expression is only accessible inside the class body, similar to named function expressions.

# Prerequisites

- Class declaration

# Key Properties

1. Anonymous: `const C = class { ... }`.
2. Named: `const C = class MyName { ... }` (name only accessible inside body).
3. Behaves like function expressions vs function declarations.

# Construction / Recognition

```js
const Person = class { /* ... */ };
const Person = class MyClass { /* ... */ };
```

# Context & Application

Less common than class declarations. Used when a class needs to be assigned dynamically or passed as a value.

# Examples

From the source text (Ch. 31, section 31.2.2):

```js
const Person = class MyClass { /* ... */ };
```

# Relationships

## Related
- **Function Declaration vs Expression** -- same relationship pattern

# Source Reference

Chapter 31: Classes, Section 31.2.2, lines 390-414.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition
- Cross-reference status: verified
