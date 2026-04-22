---
# === CORE IDENTIFICATION ===
concept: On-Stack Dynamic Dispatch
slug: on-stack-dynamic-dispatch

# === CLASSIFICATION ===
category: idiom
subcategory: polymorphism
tier: intermediate

# === PROVENANCE ===
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "On-Stack Dynamic Dispatch"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "stack-based trait objects"
  - "heap-free dynamic dispatch"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - trait-objects
  - references-and-borrowing
extends: []
related:
  - dtor-finally
  - raii-guards
contrasts_with:
  - box-dyn-dispatch

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can I use dynamic dispatch without heap allocation in Rust?"
  - "How do I choose between Box<dyn Trait> and &dyn Trait for polymorphism?"
  - "How does Rust handle lifetime extension for temporary trait object references?"
---

# Quick Definition

Use a `&mut dyn Trait` reference to achieve dynamic dispatch without heap allocation. Since Rust 1.79.0, the compiler automatically extends the lifetimes of temporaries within `&` or `&mut` expressions, so you can simply assign conditionally to a `&mut dyn Trait` binding without deferred initialization or `Box`.

# Core Definition

> "We can dynamically dispatch over multiple values, however, to do so, we need to declare multiple variables to bind differently-typed objects. To extend the lifetime as necessary, we can use deferred conditional initialization." -- Rust Design Patterns, "On-Stack Dynamic Dispatch"

> "Since Rust 1.79.0, the compiler will automatically extend the lifetimes of temporary values within `&` or `&mut` as long as possible within the scope of the function." -- Rust Design Patterns, "On-Stack Dynamic Dispatch"

The idiom avoids monomorphization bloat and heap allocation by using trait object references on the stack instead of `Box<dyn Trait>`.

# Prerequisites

- Understanding of trait objects (`dyn Trait`)
- Knowledge of Rust references and borrowing
- Familiarity with lifetime extension rules

# Key Properties

1. **No heap allocation**: The trait object reference points to stack-allocated or existing values, avoiding `Box::new()`.
2. **Avoids monomorphization bloat**: Dynamic dispatch generates a single code path instead of per-type copies.
3. **Lifetime extension since 1.79.0**: The compiler automatically extends temporary lifetimes within `&` or `&mut` expressions.
4. **Conditional initialization**: Different concrete types can be assigned to the same `&mut dyn Trait` variable based on runtime conditions.
5. **Type ascription required**: The variable must be explicitly typed as `&mut dyn Trait` to get dynamic dispatch.

# Construction / Recognition

## To Apply:
1. Identify a scenario where you need to select between concrete types at runtime
2. Declare a variable with an explicit `&mut dyn Trait` type annotation
3. Use a conditional expression (`if`/`match`) to assign the appropriate concrete value
4. The compiler handles lifetime extension automatically (Rust >= 1.79.0)

## To Recognize:
- A `let` binding typed as `&dyn Trait` or `&mut dyn Trait`
- Conditional initialization from different concrete types
- No `Box` allocation

# Context & Application

Rust monomorphises code by default, generating a copy of generic code for each concrete type. While this produces fast code, it bloats binaries and increases compile times. When performance on the hot path is not critical, dynamic dispatch via trait object references avoids both the code bloat of monomorphization and the heap allocation of `Box<dyn Trait>`.

# Examples

**Good -- on-stack dynamic dispatch:**

```rust
use std::io;
use std::fs;

let readable: &mut dyn io::Read = if arg == "-" {
    &mut io::stdin()
} else {
    &mut fs::File::open(arg)?
};

// Read from `readable` here.
```

**Alternative -- Box-based dispatch (allocates on heap):**

```rust
let readable: Box<dyn io::Read> = if arg == "-" {
    Box::new(io::stdin())
} else {
    Box::new(fs::File::open(arg)?)
};
// Read from `readable` here.
```

# Relationships

## Related
- **dtor-finally** -- Finalisation in destructors benefits from tight lifetime control
- **raii-guards** -- RAII guards similarly benefit from precise lifetime management

## Contrasts With
- **box-dyn-dispatch** -- Box-based dynamic dispatch allocates on the heap but has simpler lifetime semantics

# Common Errors

- **Error**: Forgetting the explicit type annotation on the binding
  **Correction**: Always annotate with `&mut dyn Trait` to opt into dynamic dispatch

- **Error**: Using `Box<dyn Trait>` when heap allocation is unnecessary
  **Correction**: Use `&mut dyn Trait` for stack-based dispatch when values have sufficient lifetimes

# Common Confusions

- **Confusion**: Thinking this pattern requires `Box` or heap allocation
  **Clarification**: The whole point is to avoid heap allocation by using references to stack values

- **Confusion**: Believing deferred initialization with two `let` bindings is still needed
  **Clarification**: Since Rust 1.79.0, lifetime extension handles this automatically

# Source Reference

Chapter 1: Idioms, Section "On-Stack Dynamic Dispatch".

# Verification Notes

- Definition source: Directly from "On-Stack Dynamic Dispatch" section
- Confidence rationale: HIGH -- complete description with code examples and motivation
- Uncertainties: None
- Cross-reference status: References dtor-finally.md and RAII guards pattern
