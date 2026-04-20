---
# === CORE IDENTIFICATION ===
concept: Memoization
slug: memoization

# === CLASSIFICATION ===
category: functions
subcategory: functional patterns
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 235
section: "8.8.4 Memoization"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "function caching"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - closures
  - higher-order-functions
extends: []
related:
  - closure-based-private-state
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is memoization and how is it implemented in JavaScript?"
---

# Quick Definition

Memoization is a functional programming technique where a function caches its previously computed results so that calling it again with the same arguments returns the cached result instead of recomputing.

# Core Definition

"In functional programming, this kind of caching is called memoization." The text provides a `memoize()` higher-order function that "accepts a function as its argument and returns a memoized version of the function." The cache is stored in a Map within the closure, making it private. (Flanagan, p. 235-236)

# Prerequisites

- **closures** — The cache is stored in a closure
- **higher-order-functions** — memoize() is a higher-order function

# Key Properties

1. Caches results keyed by argument values
2. Only works when arguments have distinct string representations
3. Cache is stored privately in a closure (Map object)
4. Returns cached result for repeated calls with same arguments
5. Trade-off: memory for speed

# Construction / Recognition

```javascript
function memoize(f) {
    const cache = new Map();
    return function(...args) {
        let key = args.length + args.join("+");
        if (cache.has(key)) {
            return cache.get(key);
        } else {
            let result = f.apply(this, args);
            cache.set(key, result);
            return result;
        }
    };
}
```

# Context & Application

Used to optimize expensive computations that are called repeatedly with the same arguments, like recursive functions.

# Examples

```javascript
function memoize(f) {
    const cache = new Map();
    return function(...args) {
        let key = args.length + args.join("+");
        if (cache.has(key)) return cache.get(key);
        let result = f.apply(this, args);
        cache.set(key, result);
        return result;
    };
}

// Usage:
function gcd(a,b) {
    if (a < b) [a, b] = [b, a];
    while (b !== 0) [a, b] = [b, a%b];
    return a;
}
const gcdmemo = memoize(gcd);
gcdmemo(85, 187)  // => 17 (computed)
gcdmemo(85, 187)  // => 17 (cached)
```
(Flanagan, p. 235-236)

# Relationships

## Builds Upon
- **closures** — Cache is stored in a closure
- **higher-order-functions** — memoize() wraps a function

## Enables
- Performance optimization for repeated computations

## Related
- **closure-based-private-state** — The cache is private state

## Contrasts With
- None specific

# Common Errors

- **Error**: Memoizing functions with complex object arguments.
  **Correction**: The cache key is based on string conversion of arguments. Objects may all produce "[object Object]" as a key. Use a more sophisticated key strategy.

# Common Confusions

- **Confusion**: Memoization is always beneficial.
  **Clarification**: It trades memory for speed. Functions called with many unique arguments may consume excessive memory.

# Source Reference

Chapter 8: Functions, Section 8.8.4, pages 235-236.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented with implementation
- Uncertainties: None
- Cross-reference status: Verified
