---
# === CORE IDENTIFICATION ===
concept: Closures
slug: closures

# === CLASSIFICATION ===
category: functions
subcategory: closures
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 221
section: "8.6 Closures"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "lexical closure"
  - "function closure"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nested-functions
  - functions-as-values
  - function-expressions
extends: []
related:
  - closure-based-private-state
  - iifes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a closure?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

A closure is the combination of a function object and the scope (variable bindings) in which the function was defined. Closures allow inner functions to access variables of their enclosing function even after that function has returned.

# Core Definition

"JavaScript uses lexical scoping. This means that functions are executed using the variable scope that was in effect when they were defined, not the variable scope that is in effect when they are invoked. In order to implement lexical scoping, the internal state of a JavaScript function object must include not only the code of the function but also a reference to the scope in which the function definition appears. This combination of a function object and a scope (a set of variable bindings) in which the function's variables are resolved is called a closure in the computer science literature." (Flanagan, p. 221)

"Technically, all JavaScript functions are closures, but because most functions are invoked from the same scope that they were defined in, it normally doesn't really matter that there is a closure involved. Closures become interesting when they are invoked from a different scope than the one they were defined in." (Flanagan, p. 222)

# Prerequisites

- **nested-functions** — Closures require functions defined inside other functions
- **functions-as-values** — The inner function must be returned/passed out of the enclosing function
- **function-expressions** — Closures are typically created with function expressions

# Key Properties

1. Functions retain access to the scope where they were defined
2. The scope is "live" -- closures see updates to captured variables, not snapshots
3. Multiple closures from the same invocation share the same variable bindings
4. Each invocation of the enclosing function creates a new scope with independent variables
5. `var` in loops creates shared closure problems (fixed by `let`/`const`)
6. `this` is not captured like variables (use arrow functions or save to a variable)

# Construction / Recognition

```javascript
function outer() {
    let variable = "captured";
    return function inner() {
        return variable;  // accesses outer's scope
    };
}
let fn = outer();
fn();  // => "captured" (even though outer() has returned)
```

# Context & Application

Closures enable private state, data encapsulation, factory functions, memoization, and many functional programming patterns. They are one of the most powerful features of JavaScript.

# Examples

```javascript
// Fundamental closure example:
let scope = "global scope";
function checkscope() {
    let scope = "local scope";
    function f() { return scope; }
    return f;
}
let s = checkscope()();  // => "local scope" (not "global scope")

// Private state with closure:
let uniqueInteger = (function() {
    let counter = 0;
    return function() { return counter++; };
}());
uniqueInteger()  // => 0
uniqueInteger()  // => 1

// Multiple closures sharing state:
function counter() {
    let n = 0;
    return {
        count: function() { return n++; },
        reset: function() { n = 0; }
    };
}
let c = counter(), d = counter();
c.count()  // => 0
d.count()  // => 0 (independent)
c.reset();
c.count()  // => 0 (reset)
d.count()  // => 1 (not affected)
```
(Flanagan, p. 221-224)

# Relationships

## Builds Upon
- **nested-functions** — Closures require nested function definitions
- **functions-as-values** — Inner functions are passed out of their defining scope
- **function-expressions** — Closures are commonly created with expressions

## Enables
- **closure-based-private-state** — Using closures for data encapsulation
- **iifes** — IIFEs create scope for closures
- **higher-order-functions** — Many higher-order functions return closures
- **memoization** — Cache stored in closure scope

## Related
- None specific

## Contrasts With
- None specific

# Common Errors

- **Error**: Creating closures in a `var`-based loop expecting each iteration to capture its own value.
  **Correction**: Variables declared with `var` are function-scoped, so all closures share the same variable. Use `let` or `const` instead to get block-scoped variables per iteration.

```javascript
// Bug with var:
function constfuncs() {
    let funcs = [];
    for (var i = 0; i < 10; i++) {
        funcs[i] = () => i;
    }
    return funcs;
}
constfuncs()[5]()  // => 10 (not 5!)

// Fix with let:
for (let i = 0; i < 10; i++) { ... }  // each iteration gets its own i
```
(Flanagan, p. 225-226)

# Common Confusions

- **Confusion**: Closures capture a snapshot of variable values.
  **Clarification**: Closures capture references to variables, not copies. The scope is "live" -- nested functions see current values, not values at definition time.

- **Confusion**: `this` is captured in closures like other variables.
  **Clarification**: `this` is a keyword, not a variable. Non-arrow functions define their own `this`. Use arrow functions or save `this` to a variable for closures that need the outer `this`.

# Source Reference

Chapter 8: Functions, Section 8.6, pages 221-226.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Central concept with thorough treatment including definition, examples, and common pitfalls
- Uncertainties: None
- Cross-reference status: Verified
