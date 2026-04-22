---
# === CORE IDENTIFICATION ===
concept: Incremental Macro Development
slug: incremental-macro-development

# === CLASSIFICATION ===
category: macro-design
subcategory: development-methodology
tier: intermediate

# === PROVENANCE ===
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "02-practical-introduction"
chapter_number: 2
pdf_page: null
section: "Construction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "iterative macro building"
  - "outside-in macro development"
  - "macro development process"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - macro-rules
  - macro-expansion
  - macro-invocation-design
extends: []
related:
  - macro-substitution
  - macro-hygiene
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the recommended process for building a complex macro from scratch?"
  - "How do I debug a macro that does not compile?"
  - "In what order should I tackle the parts of a macro definition?"
  - "How do I use --pretty expanded to debug macros?"
---

# Quick Definition

Incremental macro development is a methodology for building macros in stages: (1) design the invocation syntax, (2) write the desired expansion as plain Rust code and verify it compiles, (3) paste it into the macro body, (4) replace hardcoded values with captures one at a time, compiling after each change. This outside-in approach catches errors early and makes debugging tractable.

# Core Definition

The chapter demonstrates this process end-to-end through a `recurrence!` macro. The key insight is that the expansion code should be written and tested as ordinary Rust *before* it becomes a macro expansion. Each step is small and independently verifiable:

1. **Design invocation** -- Write the desired call syntax and derive the matcher.
2. **Write expansion as plain code** -- Implement the full expansion as regular Rust in `fn main()`, with hardcoded values. Verify it compiles and runs correctly.
3. **Paste into macro body** -- Copy the working code into the `=> { ... }` expansion, with no other changes. Verify the macro invocation still compiles.
4. **Substitute captures one at a time** -- Replace one hardcoded value (e.g., `u64` with `$sty`) per step. Compile after each substitution to isolate errors.
5. **Handle hygiene issues** -- When identifier resolution fails after substitution, capture the identifiers from the call site to put them in the correct syntax context.
6. **Inspect expansion** -- Use `rustc -Z unstable-options --pretty expanded` to see the actual expanded code when debugging.

# Prerequisites

- Familiarity with `macro_rules!` basics (syntax rules, captures, repetitions)
- Understanding of macro expansion (what the compiler does with a macro invocation)
- Knowledge of macro invocation design (the first step of this process)

# Key Properties

1. **Plain code first**: The expansion is verified as working Rust before it becomes a macro. This separates "does my algorithm work?" from "does my macro work?".
2. **One substitution at a time**: Each captured metavariable is introduced individually, with a compile check after each. This isolates the source of any error.
3. **Expansion inspection**: The `--pretty expanded` flag is used to see what the macro actually produces, which is essential for debugging hygiene issues where the expanded code *looks* correct but uses different syntax contexts.
4. **Hygiene awareness**: Identifiers defined inside a macro expansion are in a different syntax context than identifiers from the invocation. This manifests as "unresolved name" errors even when `--pretty expanded` output looks correct.
5. **Helper macros as needed**: When a substitution requires computation (e.g., counting the number of initial values to determine an array size), introduce a helper macro like `count_exprs!`.

# Construction / Recognition

**Phase 1 -- Working plain code:**

```rust,ignore
fn main() {
    let fib = {
        struct Recurrence { mem: [u64; 2], pos: usize }
        impl Iterator for Recurrence {
            type Item = u64;
            fn next(&mut self) -> Option<u64> { /* ... */ }
        }
        Recurrence { mem: [0, 1], pos: 0 }
    };
    for e in fib.take(10) { println!("{}", e) }
}
```

**Phase 2 -- Paste into macro, no substitutions yet:**

```rust,ignore
macro_rules! recurrence {
    ( a[n]: $sty:ty = $($inits:expr),+ ... $recur:expr ) => {
        {
            // Literally the code from before, cut and pasted.
            struct Recurrence { mem: [u64; 2], pos: usize }
            // ...
            Recurrence { mem: [0, 1], pos: 0 }
        }
    };
}
```

**Phase 3 -- Substitute captures one at a time:**

```rust,ignore
// Step 1: Replace u64 with $sty
struct Recurrence { mem: [$sty; 2], pos: usize }

// Step 2: Replace [0, 1] with [$($inits),+]
Recurrence { mem: [$($inits),+], pos: 0 }

// Step 3: Replace hardcoded 2 with count_exprs!($($inits),+)
const MEM_SIZE: usize = count_exprs!($($inits),+);

// Step 4: Replace recurrence expression with $recur
let next_val = { let n = self.pos; let a = ...; $recur };

// Step 5: Fix hygiene -- capture a and n as $seq:ident and $ind:ident
```

# Context & Application

This methodology is essential for any macro that generates more than a few lines of code. Complex macros can produce cryptic error messages; the incremental approach ensures that each error is attributable to the most recent change. The technique of writing expansion code as plain Rust first is especially valuable because it lets you use IDE features, type checking, and runtime testing before introducing the additional complexity of macro mechanics.

# Examples

The chapter builds a complete `recurrence!` macro through this process. The final macro is approximately 60 lines of expansion code, supports arbitrary sequence names, index names, element types, initial values, and recurrence expressions. The development proceeds through approximately 8 distinct compilable stages.

Debugging example using `--pretty expanded`:

```shell
$ rustc -Z unstable-options --pretty expanded recurrence.rs
```

This revealed that while the expanded code looked correct textually, the identifiers `a` and `n` from the invocation were in a different syntax context than the `a` and `n` defined inside the expansion, causing "unresolved name" errors.

# Relationships

- **macro-invocation-design**: Step 1 of this process.
- **macro-substitution**: The mechanism used in Phase 3 when replacing hardcoded values with captures.
- **macro-hygiene**: The source of errors in Phase 4 that require capturing identifiers from the call site.
- **macro-expansion**: Understanding what expansion produces is needed to debug problems.

# Common Errors

1. **Writing the macro all at once**: Trying to write the complete macro (captures, repetitions, substitutions) in one go, then facing inscrutable errors with no idea which part is wrong.
2. **Not testing the plain code**: Pasting untested expansion code into a macro, conflating algorithm bugs with macro bugs.
3. **Substituting multiple captures at once**: Replacing several hardcoded values simultaneously, making it impossible to isolate which substitution introduced a new error.

# Common Confusions

- **"Pretty expanded looks fine but it doesn't compile"**: This is the hallmark of a hygiene issue. The textual representation looks correct, but identifiers are in different syntax contexts. The solution is to capture identifiers from the call site using `$name:ident`.
- **Helper macros feel like overhead**: Introducing `count_exprs!` to compute an array size from a repetition may seem excessive, but there is no way to directly count elements in a repetition. Helper macros are a normal and expected part of macro development.

# Source Reference

The Little Book of Rust Macros, Chapter 2 "Macros, A Practical Introduction", "Construction" through "Being Hygienic" sections. The entire chapter is structured as a demonstration of this methodology.

# Verification Notes

Confidence: high. The incremental development process is the organizing principle of the entire chapter, demonstrated step by step with compilable code at each stage.
