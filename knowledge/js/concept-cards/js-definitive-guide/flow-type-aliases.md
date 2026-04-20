---
concept: Flow Type Aliases
slug: flow-type-aliases
category: tooling
subcategory: type checking
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript Tools and Extensions"
chapter_number: 17
pdf_page: 674
section: "17.8.5 Type Aliases"
extraction_confidence: high
aliases:
  - type keyword
  - named types
prerequisites:
  - flow-type-annotations
extends:
  - flow-type-annotations
related:
  - flow-union-types
contrasts_with: []
answers_questions:
  - "How do I write and run unit tests with Jest?"
---

# Quick Definition

Flow's `type` keyword creates named aliases for complex type expressions, making object types, union types, and other compound types reusable and readable.

# Core Definition

Flow uses the `type` keyword to define aliases for types. After `type Point = {x: number, y: number}`, the identifier `Point` can be used wherever a type is needed. Type aliases can be exported with `export type` and imported with `import type`. These imports and exports are Flow-only constructs that are stripped by Babel (Flanagan, Ch. 17, pp. 674-675).

# Prerequisites

- **flow-type-annotations** — Must understand Flow's basic type system.

# Key Properties

1. `type Name = TypeExpression` defines a type alias.
2. `export type` / `import type` for sharing types between modules.
3. Type imports are stripped by Babel (no runtime cost).
4. Useful for complex object types, unions, and tuples.

# Construction / Recognition

```javascript
// @flow
export type Point = { x: number, y: number };
export default function distance(point: Point): number {
  return Math.hypot(point.x, point.y);
}
```

# Context & Application

Essential for any non-trivial Flow project where the same type structure is used in multiple places.

# Examples

From the source (p. 674): A `Point` type alias used in a `distance()` function, exportable for use by other modules.

# Relationships

## Builds Upon
- **flow-type-annotations** — Extends the basic type annotation system

## Enables
- Reusable, readable type definitions

## Related
- **flow-union-types** — Union types often benefit from aliases

## Contrasts With
- (None)

# Common Errors

- **Error**: Using `import` instead of `import type` for Flow types.
  **Correction**: Use `import type` for types to ensure Babel strips them properly.

# Common Confusions

- **Confusion**: Type aliases create new types.
  **Clarification**: Type aliases are just names for existing type expressions. Structurally identical types are interchangeable regardless of alias names.

# Source Reference

Chapter 17: JavaScript Tools and Extensions, Section 17.8.5, pages 674-675.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear example with import/export pattern
- Uncertainties: Flow vs TypeScript ecosystem evolution
- Cross-reference status: Verified
