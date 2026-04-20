---
concept: Flow Union Types
slug: flow-union-types
category: tooling
subcategory: type checking
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript Tools and Extensions"
chapter_number: 17
pdf_page: 679
section: "17.8.10 Union Types"
extraction_confidence: high
aliases:
  - union type
  - discriminated union
  - "type A | B"
prerequisites:
  - flow-type-annotations
extends:
  - flow-type-annotations
related:
  - flow-type-aliases
contrasts_with: []
answers_questions:
  - "How do I write and run unit tests with Jest?"
---

# Quick Definition

Flow union types express that a value can be one of several types, written with `|` (e.g., `Array<mixed> | Set<mixed> | Map<mixed,mixed>`), requiring type narrowing (runtime checks) before type-specific operations.

# Core Definition

Union types are expressed by listing desired types separated by `|`. `?type` is shorthand for `type | null | void`. When a value has a union type, Flow requires runtime type checks before using type-specific properties. Literal types can form enumerated types (e.g., `type Suit = "Clubs" | "Diamonds" | "Hearts" | "Spades"`). Discriminated unions use a literal-typed property (like `messageType`) as a discriminant to safely narrow the type (Flanagan, Ch. 17, pp. 679-682).

# Prerequisites

- **flow-type-annotations** — Must understand basic Flow types.

# Key Properties

1. `A | B | C` means the value can be type A, B, or C.
2. `?type` is shorthand for `type | null | void`.
3. Must narrow the type (e.g., with `Array.isArray()`) before using type-specific features.
4. Literal types: `"yes" | "no"`, `0|1|2|3`.
5. Discriminated unions use a common literal-typed property for safe narrowing.

# Construction / Recognition

```javascript
// @flow
function size(collection: Array<mixed>|Set<mixed>|Map<mixed,mixed>): number {
  if (Array.isArray(collection)) { return collection.length; }
  else { return collection.size; }
}
type Suit = "Clubs" | "Diamonds" | "Hearts" | "Spades";
```

# Context & Application

Union types model values that can take multiple forms, such as API responses that may return different data shapes or functions that accept multiple argument types.

# Examples

From the source (p. 681): A discriminated union of worker messages with `messageType` as the discriminant:
```javascript
type WorkerMessage = ResultMessage | ErrorMessage | StatisticsMessage;
```
Each type has a different `messageType` literal, enabling safe property access after checking the discriminant.

# Relationships

## Builds Upon
- **flow-type-annotations** — Extends the type system

## Enables
- Type-safe handling of heterogeneous data

## Related
- **flow-type-aliases** — Union types are often given names via aliases

## Contrasts With
- (None)

# Common Errors

- **Error**: Accessing a union-specific property without narrowing the type first.
  **Correction**: Use type guards (typeof, instanceof, property checks) to narrow the union before accessing specific properties.

# Common Confusions

- **Confusion**: Literal types like `"yes" | "no"` accept any string.
  **Clarification**: Only the exact literal values are accepted. Flow flags errors if you assign a computed string, even if the runtime value would match.

# Source Reference

Chapter 17: JavaScript Tools and Extensions, Sections 17.8.10-17.8.11, pages 679-682.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Comprehensive coverage with discriminated union example
- Uncertainties: Flow vs TypeScript syntax differences
- Cross-reference status: Verified
