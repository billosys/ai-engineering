---
# === CORE IDENTIFICATION ===
concept: Function() Constructor
slug: function-constructor

# === CLASSIFICATION ===
category: functions
subcategory: function creation
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 229
section: "8.7.7 The Function() Constructor"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declarations
  - functions-as-values
extends: []
related:
  - closures
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can functions be created dynamically at runtime?"
---

# Quick Definition

The `Function()` constructor creates functions dynamically from strings at runtime. Unlike normal functions, it does not use lexical scoping -- it is always compiled as a top-level function.

# Core Definition

"Because functions are objects, there is a Function() constructor that can be used to create new functions." The last argument is the function body; preceding arguments are parameter names. "A last, very important point about the Function() constructor is that the functions it creates do not use lexical scoping; instead, they are always compiled as if they were top-level functions." It "is best thought of as a globally scoped version of eval()." (Flanagan, p. 229-230)

# Prerequisites

- **function-declarations** — Must understand normal function creation
- **functions-as-values** — Functions are objects

# Key Properties

1. Arguments: parameter name strings, then body string
2. Creates anonymous functions
3. No lexical scoping (always top-level scope)
4. Parses and compiles on each call (inefficient in loops)
5. Rarely needed in practice

# Construction / Recognition

```javascript
const f = new Function("x", "y", "return x*y;");
```

# Context & Application

Almost never needed. Used only for dynamic code generation. Security risk if used with user input.

# Examples

```javascript
const f = new Function("x", "y", "return x*y;");
// equivalent to: const f = function(x, y) { return x*y; };

let scope = "global";
function constructFunction() {
    let scope = "local";
    return new Function("return scope");  // doesn't capture local scope!
}
constructFunction()()  // => "global"
```
(Flanagan, p. 229-230)

# Relationships

## Builds Upon
- **function-declarations** — Dynamic alternative to static declarations
- **functions-as-values** — Functions are objects that can be constructed

## Enables
- Dynamic code generation

## Related
- **closures** — Function() constructor does NOT create closures (no lexical scoping)

## Contrasts With
- None specific

# Common Errors

- **Error**: Expecting Function() to capture local scope variables.
  **Correction**: Function() always uses global scope. It does not form closures.

# Common Confusions

- **Confusion**: Function() is equivalent to function expressions.
  **Clarification**: Function() lacks lexical scoping and is recompiled each call. It's fundamentally different.

# Source Reference

Chapter 8: Functions, Section 8.7.7, pages 229-230.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented with warning
- Uncertainties: None
- Cross-reference status: Verified
