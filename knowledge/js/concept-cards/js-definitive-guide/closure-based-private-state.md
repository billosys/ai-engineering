---
# === CORE IDENTIFICATION ===
concept: Closure-Based Private State
slug: closure-based-private-state

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
pdf_page: 222
section: "8.6 Closures"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "private variables via closures"
  - "encapsulation via closures"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - closures
  - iifes
extends:
  - closures
related:
  - private-fields
contrasts_with:
  - private-fields

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can I create truly private state in JavaScript without classes?"
---

# Quick Definition

Closures can create private state by enclosing variables in a function scope that is only accessible through returned inner functions, providing data encapsulation without class syntax.

# Core Definition

"Closures capture the local variables of a single function invocation and can use those variables as private state." Multiple closures from the same invocation "share access to the private variable." "Once that outer function returns, no other code can see the counter variable: the inner function has exclusive access to it." (Flanagan, p. 222-225)

# Prerequisites

- **closures** — Must understand how closures capture scope
- **iifes** — Often used to create the enclosing scope

# Key Properties

1. Variables in enclosing scope are inaccessible from outside
2. Only the returned functions can access/modify the private variables
3. Multiple closures from the same invocation share the private state
4. Each invocation of the factory creates independent private state
5. Can be combined with getters/setters for property-like access

# Construction / Recognition

```javascript
let uniqueInteger = (function() {
    let counter = 0;  // private variable
    return function() { return counter++; };
}());
```

# Context & Application

Used for data encapsulation, protecting internal state from external modification. Predates the ES6+ class private fields feature (#field syntax).

# Examples

```javascript
// Private counter with shared access:
function counter() {
    let n = 0;
    return {
        count: function() { return n++; },
        reset: function() { n = 0; }
    };
}
let c = counter(), d = counter();
c.count()  // => 0
d.count()  // => 0  (independent)
c.reset();
c.count()  // => 0  (reset)
d.count()  // => 1  (unaffected)

// Private state with getter/setter:
function counter(n) {
    return {
        get count() { return n++; },
        set count(m) {
            if (m > n) n = m;
            else throw Error("count can only be set to a larger value");
        }
    };
}
```
(Flanagan, p. 223-225)

# Relationships

## Builds Upon
- **closures** — This is a specific application of closures
- **iifes** — Often used to create the private scope

## Enables
- Data encapsulation without class syntax

## Related
- **private-fields** — ES6+ class feature that serves a similar purpose

## Contrasts With
- **private-fields** — Private fields use `#` syntax in classes; closure-based privacy uses function scope

# Common Errors

- **Error**: Storing private state on the function object itself (which is publicly accessible).
  **Correction**: Use closures to make state truly private and inaccessible from outside.

# Common Confusions

- **Confusion**: Closure-based private state and class private fields (#) are the same.
  **Clarification**: They achieve similar goals but use different mechanisms: closures use function scope; private fields use class syntax with `#` prefix.

# Source Reference

Chapter 8: Functions, Section 8.6, pages 222-225.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented pattern with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
