---
concept: Flow Type Annotations
slug: flow-type-annotations
category: tooling
subcategory: type checking
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript Tools and Extensions"
chapter_number: 17
pdf_page: 667
section: "17.8 Type Checking with Flow"
extraction_confidence: high
aliases:
  - Flow
  - type checking
  - type annotations
prerequisites:
  - babel-transpilation
extends: []
related:
  - flow-union-types
  - flow-type-aliases
  - flow-generics
contrasts_with: []
answers_questions:
  - "How do I write and run unit tests with Jest?"
---

# Quick Definition

Flow is a JavaScript language extension and static type checker that uses annotations (e.g., `x: string`, `function f(n: number): boolean`) to catch type errors at development time, with all annotations stripped by Babel before runtime.

# Core Definition

Flow allows annotating JavaScript code with types and then checking for type errors statically. Variables, function parameters, and return types are annotated with a colon followed by a type name. Flow uses `// @flow` to opt in per file. Even without annotations, Flow can infer types and detect inconsistencies. Primitive types include `string`, `number`, `boolean`, `null`, and `void` (for undefined). `?type` allows null/undefined. Flow annotations are stripped by Babel before runtime, adding no overhead (Flanagan, Ch. 17, pp. 667-671).

# Prerequisites

- **babel-transpilation** — Babel strips Flow annotations for runtime.

# Key Properties

1. Add `// @flow` at the top of a file to opt in.
2. Syntax: `variable: type`, `(param: type): returnType`.
3. `?type` allows null and undefined in addition to the specified type.
4. Flow can detect errors even without annotations via type inference.
5. Annotations are stripped by Babel; no runtime cost.
6. Install with `npm install flow-bin`; run with `flow` or `npx flow`.

# Construction / Recognition

```javascript
// @flow
function size(s: string): number {
  return s.length;
}
let message: string = "Hello world";
```

# Context & Application

Adds type safety to medium and large JavaScript projects. Flow is an alternative to TypeScript, with similar goals but narrower scope (types only, no additional language features).

# Examples

From the source (p. 669-670): Flow detects that calling `size(1000)` is an error because numbers don't have a `length` property. It also detects that using a `?string` parameter without a null check is unsafe.

# Relationships

## Builds Upon
- **babel-transpilation** — Babel strips Flow annotations

## Enables
- **flow-union-types** — Union types for flexible typing
- **flow-type-aliases** — Named type definitions
- **flow-generics** — Parameterized types

## Related
- (TypeScript -- similar goals, different implementation)

## Contrasts With
- (None)

# Common Errors

- **Error**: Using `null` where a string is expected without the `?` prefix.
  **Correction**: Use `?string` to allow null, and add null checks before using the value.

# Common Confusions

- **Confusion**: Flow and TypeScript are equivalent.
  **Clarification**: Flow is types-only; TypeScript adds additional language features (enums, namespaces). TypeScript has better IDE integration (especially VSCode). Both achieve the same fundamental goal.

# Source Reference

Chapter 17: JavaScript Tools and Extensions, Section 17.8, pages 667-671.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Extensive tutorial section
- Uncertainties: Flow's popularity has declined relative to TypeScript since the book's publication (2020)
- Cross-reference status: Verified
