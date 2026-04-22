---
# === CORE IDENTIFICATION ===
concept: Temporary Mutability
slug: temporary-mutability

# === CLASSIFICATION ===
category: idiom
subcategory: ownership
tier: foundational

# === PROVENANCE ===
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "Temporary mutability"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "scoped mutability"
  - "variable rebinding to immutable"
  - "freeze after mutation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mutability
  - variable-shadowing
extends: []
related:
  - pass-variables-to-closure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make a variable mutable for setup and then immutable for the rest of its lifetime?"
  - "What are the two patterns for temporary mutability in Rust?"
  - "How does variable rebinding differ from nested blocks for restricting mutability?"
---

# Quick Definition

Restrict mutability to just the preparation phase by either (1) using a nested block that returns the final value as immutable, or (2) rebinding a `mut` variable with `let data = data;` to shadow it as immutable. Both approaches enlist the compiler to enforce that data is not accidentally mutated after setup.

# Core Definition

> "Often it is necessary to prepare and process some data, but after that data are only inspected and never modified. The intention can be made explicit by redefining the mutable variable as immutable." -- Rust Design Patterns, "Temporary mutability"

> "It can be done either by processing data within a nested block or by redefining the variable." -- Rust Design Patterns, "Temporary mutability"

The two approaches are equivalent in effect: after the transition point, the compiler treats the binding as immutable and rejects any mutation attempts.

# Prerequisites

- Understanding of `let mut` vs. `let` bindings
- Familiarity with variable shadowing in Rust
- Knowledge of block expressions

# Key Properties

1. **Compiler-enforced immutability**: After the transition, any mutation attempt is a compile error.
2. **Nested block approach**: `let data = { let mut data = get_vec(); data.sort(); data };` -- mutability is scoped to the block.
3. **Rebinding approach**: `let mut data = get_vec(); data.sort(); let data = data;` -- shadows the mutable binding with an immutable one.
4. **Intent communication**: Makes it explicit to readers that mutation is intentionally limited to the setup phase.
5. **No runtime cost**: Both patterns are purely compile-time; they generate identical code.

# Construction / Recognition

## To Apply (nested block):
1. Open a block expression: `let data = { ... };`
2. Declare the mutable variable inside: `let mut data = ...;`
3. Perform all mutations
4. Return the value as the last expression (no semicolon)
5. The outer `let` binding is immutable

## To Apply (rebinding):
1. Declare with `let mut data = ...;`
2. Perform all mutations
3. Shadow with `let data = data;`
4. From this point, `data` is immutable

## To Recognize:
- `let data = { let mut data = ...; ... data };`
- `let mut x = ...; /* mutations */ let x = x;`

# Context & Application

This idiom is useful whenever data requires a preparation phase (sorting, filtering, normalization) before being used in a read-only fashion. By making the transition from mutable to immutable explicit, you prevent accidental mutations later and communicate intent to other developers. The nested block approach is slightly more structured; the rebinding approach is simpler but requires one extra line.

# Examples

**Approach 1 -- nested block:**

```rust
let data = {
    let mut data = get_vec();
    data.sort();
    data
};

// Here `data` is immutable.
```

**Approach 2 -- variable rebinding:**

```rust
let mut data = get_vec();
data.sort();
let data = data;

// Here `data` is immutable.
```

# Relationships

## Related
- **pass-variables-to-closure** -- Similarly uses block scoping to control variable properties

# Common Errors

- **Error**: Forgetting to rebind, leaving the variable mutable for its entire lifetime
  **Correction**: Add `let data = data;` after the mutation phase, or use the nested block pattern

- **Error**: Trying to mutate after rebinding and being confused by the compiler error
  **Correction**: This is the intended behavior; the rebinding is there to prevent further mutation

# Common Confusions

- **Confusion**: Thinking the nested block approach has runtime overhead
  **Clarification**: Blocks are a compile-time scoping construct; the generated code is identical

- **Confusion**: Believing the two approaches differ in semantics
  **Clarification**: Both produce an immutable binding; the choice is purely stylistic

# Source Reference

Chapter 1: Idioms, Section "Temporary mutability".

# Verification Notes

- Definition source: Directly from "Temporary mutability" section
- Confidence rationale: HIGH -- concise idiom with two clear code examples
- Uncertainties: None
- Cross-reference status: Standalone idiom
