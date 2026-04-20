---
concept: Flow Generics (Parameterized Types)
slug: flow-generics
category: tooling
subcategory: type checking
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript Tools and Extensions"
chapter_number: 17
pdf_page: 676
section: "17.8.7 Other Parameterized Types"
extraction_confidence: high
aliases:
  - parameterized types
  - generic types
  - type parameters
prerequisites:
  - flow-type-annotations
extends:
  - flow-type-annotations
related:
  - flow-union-types
  - flow-type-aliases
contrasts_with: []
answers_questions:
  - "How do I write and run unit tests with Jest?"
---

# Quick Definition

Flow generics use angle-bracket syntax to parameterize types (e.g., `Array<number>`, `Set<string>`, `Map<string, Color>`), and allow defining generic classes and functions with type parameters like `<A, B>`.

# Core Definition

Flow supports parameterized types using angle brackets. `Array<number>` specifies an array of numbers; `Set<string>` a set of strings; `Map<string, Color>` a map with string keys and Color values. Classes can define type parameters: `class Result<E, V>`. Functions can also be generic: `function zip<A,B>(a:Array<A>, b:Array<B>): Array<[?A,?B]>`. The special types `mixed` (requires type checking before use) and `any` (opts out of type checking) are used for heterogeneous collections (Flanagan, Ch. 17, pp. 676-678).

# Prerequisites

- **flow-type-annotations** — Must understand Flow's basic type system.

# Key Properties

1. `Array<T>` or `T[]` for typed arrays.
2. `Set<T>` and `Map<K, V>` for typed collections.
3. `class MyClass<T>` defines a generic class.
4. `function myFunc<T>(arg: T): T` defines a generic function.
5. `mixed` requires type narrowing; `any` skips type checking.
6. Tuples: `[number, string]` for fixed-length typed arrays.

# Construction / Recognition

```javascript
// @flow
function zip<A,B>(a:Array<A>, b:Array<B>): Array<[?A,?B]> {
  let result:Array<[?A,?B]> = [];
  let len = Math.max(a.length, b.length);
  for(let i = 0; i < len; i++) { result.push([a[i], b[i]]); }
  return result;
}
```

# Context & Application

Essential for writing reusable, type-safe library code. Generics allow functions and classes to work with any type while maintaining type safety.

# Examples

From the source (p. 677-678): A generic `Result<E, V>` class that represents either an error of type E or a value of type V, with methods that return the appropriate typed value.

# Relationships

## Builds Upon
- **flow-type-annotations** — Advanced type annotation feature

## Enables
- Type-safe generic programming

## Related
- **flow-union-types** — Can be combined with generics
- **flow-type-aliases** — Aliases for generic types

## Contrasts With
- (None)

# Common Errors

- **Error**: Using `any` instead of `mixed` for heterogeneous data.
  **Correction**: Use `mixed` to maintain type safety (Flow will require type narrowing). Use `any` only when you intentionally opt out of type checking.

# Common Confusions

- **Confusion**: Generics add runtime overhead.
  **Clarification**: All type annotations, including generics, are stripped by Babel. There is zero runtime cost.

# Source Reference

Chapter 17: JavaScript Tools and Extensions, Section 17.8.7, pages 676-678.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear examples of generic classes and functions
- Uncertainties: Flow vs TypeScript syntax differences
- Cross-reference status: Verified
