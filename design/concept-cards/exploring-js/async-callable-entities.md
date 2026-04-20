---
concept: Asynchronous Callable Entities
slug: async-callable-entities
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.1.3 Asynchronous callable entities"
extraction_confidence: high
aliases:
  - async function forms
prerequisites:
  - async-function
extends: []
related:
  - await-operator
contrasts_with: []
answers_questions:
  - "What is an async function?"
---

# Quick Definition

JavaScript provides five forms of async callable entities: async function declarations, async function expressions, async arrow functions, async method definitions in object literals, and async method definitions in class definitions.

# Core Definition

"Exploring JavaScript" Ch. 44 lists all async versions of synchronous callable entities:
```js
async function func1() {}           // declaration
const func2 = async function () {}; // expression
const func3 = async () => {};       // arrow function
const obj = { async m() {} };       // object method
class MyClass { async m() {} }      // class method
```

# Prerequisites

- **Async function** -- these are all forms of async functions

# Key Properties

1. All five forms use the `async` keyword
2. All can use `await` internally
3. All return Promises
4. Roles are always either real function or method

# Construction / Recognition

See the five forms listed in the Core Definition.

(Ch. 44, Section 44.1.3, lines 200-216)

# Context & Application

Choose the appropriate form based on context: declarations for named functions, arrows for callbacks, methods for object/class members.

# Examples

From the source, all five syntactic forms are demonstrated.

(Ch. 44, Section 44.1.3, lines 202-216)

# Relationships

## Builds Upon
- **Async function** -- these are syntactic variants

# Common Errors

- **Error**: Forgetting `async` keyword when using `await` in a method
  **Correction**: The `async` keyword is required for any function that uses `await`

# Common Confusions

- **Confusion**: Async arrow functions need different syntax than regular arrows
  **Clarification**: Simply prefix with `async`: `const f = async () => {}`

# Source Reference

Chapter 44: Async functions, Section 44.1.3, lines 193-239.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit enumeration of all forms
- Cross-reference status: verified
