---
concept: Macro Hygiene
slug: macro-hygiene
category: macro-system
subcategory: null
tier: advanced
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "01-methodical-introduction"
chapter_number: 1
pdf_page: null
section: "Hygiene"
extraction_confidence: high
aliases:
  - "hygienic macros"
  - "syntax context"
  - "macro hygiene"
prerequisites:
  - macro-rules
  - macro-expansion
  - metavariable
extends: []
related:
  - macro-scoping
contrasts_with: []
answers_questions:
  - "What is macro hygiene in Rust?"
  - "How does Rust prevent naming collisions in macro expansions?"
  - "What is a syntax context?"
  - "Are Rust macros fully hygienic?"
  - "How can you work around hygiene when you need to share identifiers between macro and call site?"
---

# Quick Definition

Rust macros are partially hygienic: they prevent naming collisions for most identifiers by attaching an invisible "syntax context" to each identifier. Two identifiers with the same textual name but different syntax contexts are considered distinct. However, hygiene does not apply to generic type parameters or lifetimes.

# Core Definition

Hygiene works by attaching an invisible "syntax context" value to all identifiers. When two identifiers are compared, both the identifiers' textual names and syntax contexts must be identical for the two to be considered equal.

Each macro expansion is given a new, unique syntax context for its contents. Tokens that were substituted into the expanded output (i.e., provided to the macro as arguments) retain their original syntax context. Tokens that are part of the macro definition itself get the new syntax context.

This means that an identifier `a` defined inside a macro expansion and an identifier `a` provided as input to the macro are treated as different identifiers, even though they have the same textual name. This prevents accidental name collisions between the macro's internal variables and the caller's variables.

Rust macros are only partially hygienic: hygiene applies to most identifiers but not to generic type parameters or lifetimes.

# Prerequisites

- **macro-rules** -- Hygiene is a property of the `macro_rules!` expansion system
- **macro-expansion** -- Hygiene applies during the expansion process
- **metavariable** -- Substituted captures retain their original syntax context

# Key Properties

1. **Syntax context**: Each identifier carries an invisible syntax context value.
2. **Identity requires both**: Two identifiers are equal only if both textual name AND syntax context match.
3. **Unique context per expansion**: Each macro expansion gets a new, unique syntax context.
4. **Substituted tokens keep original context**: Captures substituted into the expansion retain their original syntax context from the call site.
5. **Partial hygiene**: Applies to identifiers but NOT to generic type parameters or lifetimes.

# Construction / Recognition

## Hygiene prevents accidental capture

```rust
macro_rules! using_a {
    ($e:expr) => {
        {
            let a = 42;
            $e
        }
    }
}

let four = using_a!(a / 10);  // ERROR: unresolved name `a`
```

The `a` in `let a = 42` (inside the macro) has a different syntax context than the `a` in `a / 10` (from the call site). They are different identifiers.

## Working around hygiene by passing the identifier

```rust
macro_rules! using_a {
    ($a:ident, $e:expr) => {
        {
            let $a = 42;
            $e
        }
    }
}

let four = using_a!(a, a / 10);  // Works: both `a`s share the same syntax context
```

By accepting the identifier as a macro argument, both uses of `a` come from the call site and share the same syntax context.

# Context & Application

Macro hygiene is a critical safety feature that prevents a class of bugs common in unhygienic macro systems (like C's preprocessor). Without hygiene, a macro that internally defines a variable `temp` could accidentally shadow or be shadowed by a caller's variable named `temp`.

The partial nature of Rust's hygiene (not covering generic type parameters or lifetimes) means you still need to be careful in those areas. However, for the most common case of local variable names, hygiene provides strong protection.

The workaround pattern -- accepting identifiers as macro arguments so that both the definition site and the use site share the same syntax context -- is a fundamental technique in Rust macro design. It shifts the responsibility for naming from the macro to the caller, which is safer and more explicit.

# Examples

**Hygiene in action** (from "Hygiene" section):

```rust
macro_rules! using_a {
    ($e:expr) => {
        {
            let a = 42;   // syntax context 1 (macro expansion)
            $e            // syntax context 0 (call site)
        }
    }
}

let four = using_a!(a / 10);
```

After expansion, there are two different `a`s:
- `a` in `let a = 42` has the macro expansion's syntax context
- `a` in `a / 10` has the call site's syntax context

The compiler sees these as different identifiers and reports `unresolved name 'a'`.

**The fix -- passing the identifier** (from "Hygiene" section):

```rust
macro_rules! using_a {
    ($a:ident, $e:expr) => {
        {
            let $a = 42;
            $e
        }
    }
}

let four = using_a!(a, a / 10);  // Works!
```

Now both `$a` (in `let $a = 42`) and `a` (in `a / 10`) originate from the call site and share the same syntax context.

# Relationships

## Builds Upon

- **macro-expansion** -- Hygiene is applied during expansion
- **metavariable** -- Substituted captures retain their original syntax context

## Related

- **macro-scoping** -- Scoping interacts with hygiene for identifier resolution
- **macro-rules** -- Hygiene is a fundamental property of the `macro_rules!` system

# Common Errors

1. **Expecting the macro's internal `let` bindings to be visible at the call site**: Variables defined inside the macro expansion have a different syntax context and are not accessible to the caller's code.
2. **Forgetting that hygiene is partial**: Generic type parameters and lifetimes are not hygienic, so naming collisions can still occur in those domains.

# Common Confusions

- **Confusion**: Thinking Rust macros are fully hygienic.
  **Clarification**: Rust macros are only partially hygienic. Hygiene applies to most identifiers but not to generic type parameters or lifetimes.
- **Confusion**: Expecting a variable defined inside a macro to be accessible by name at the call site.
  **Clarification**: Due to syntax contexts, the macro's internal variables are invisible at the call site. To share a name between macro and caller, pass the identifier as a macro argument.
- **Confusion**: Thinking hygiene is the same as scoping.
  **Clarification**: Hygiene is about syntax contexts on identifiers; scoping is about where macros are visible and can be invoked. They are related but distinct mechanisms.

# Source Reference

"The Little Book of Rust Macros" by Daniel Keep et al., Chapter 1: "Methodical Introduction," section "Hygiene."

# Verification Notes

- Syntax context mechanism: directly explained in the source with colored-background visualizations
- The `using_a` examples (both broken and fixed): directly from the source
- Partial hygiene (not covering generics/lifetimes): explicitly stated in the opening of the section
- Error message "unresolved name `a`": directly from the source
- Confidence: HIGH -- explicit, detailed treatment with clear examples
