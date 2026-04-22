---
# === CORE IDENTIFICATION ===
concept: Macro Substitution
slug: macro-substitution

# === CLASSIFICATION ===
category: macro-system
subcategory: expansion-mechanics
tier: intermediate

# === PROVENANCE ===
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "02-practical-introduction"
chapter_number: 2
pdf_page: null
section: "Substitution"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "metavariable substitution"
  - "capture substitution"
  - "macro variable expansion"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - macro-rules
  - metavariable
  - macro-repetition
extends:
  - macro-expansion
related:
  - macro-invocation-design
  - macro-hygiene
  - incremental-macro-development
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use captured values from a macro's matcher in its expansion?"
  - "How do I substitute a repeated capture back into the expansion?"
  - "Can I compute derived values (like a count) from captured repetitions?"
  - "What happens when I substitute an expression capture into a context expecting a different grammar element?"
---

# Quick Definition

Macro substitution is the mechanism by which captured metavariables from a macro's matcher pattern are inserted into the expansion template. A capture `$name:frag` in the matcher is referenced as `$name` in the expansion. Repeated captures are substituted inside matching repetition syntax `$( ... ),*` in the expansion.

# Core Definition

> "Substituting something you've captured in a macro is quite simple; you can insert the contents of a capture `$sty:ty` by using `$sty`." -- Daniel Keep et al., "Macros, A Practical Introduction"

When a macro rule matches, each captured metavariable binds to a fragment of the input. In the expansion, writing `$name` inserts the captured tokens at that position. For repeated captures (those inside `$( ... ),+` in the matcher), the substitution must also appear inside a repetition block in the expansion.

# Prerequisites

- Understanding of metavariables and how they bind to input fragments
- Knowledge of macro repetition syntax (`$( ... ),*` and `$( ... ),+`)
- Familiarity with fragment specifiers (`expr`, `ty`, `ident`, etc.)

# Key Properties

1. **Simple substitution**: A capture `$sty:ty` is referenced as `$sty` in the expansion. The captured tokens are inserted verbatim at the substitution site.
2. **Repetition symmetry**: A capture inside a repetition in the matcher must be substituted inside a repetition in the expansion. The pattern `$($inits:expr),+` in the matcher becomes `$($inits),+` in the expansion.
3. **Context sensitivity**: The substituted tokens must be valid in their new position. A `$sty:ty` capture can be used anywhere a type is expected (struct fields, function return types, type parameters).
4. **No direct computation**: You cannot directly compute derived values from captures. For example, there is no built-in way to count the number of elements in a repeated capture. A helper macro (like `count_exprs!`) is needed.
5. **Capture preserves structure**: Repeated captures preserve the sequence of matched elements. `$($inits:expr),+` matching `0, 1` stores both values, and `$($inits),+` in the expansion reproduces `0, 1`.

# Construction / Recognition

**Simple type substitution -- replacing `u64` with `$sty` throughout:**

```rust,ignore
macro_rules! recurrence {
    ( a[n]: $sty:ty = $($inits:expr),+ ... $recur:expr ) => {
        {
            struct Recurrence {
                mem: [$sty; MEM_SIZE],   // $sty substituted for u64
                pos: usize,
            }
            impl Iterator for Recurrence {
                type Item = $sty;        // $sty substituted for u64
                fn next(&mut self) -> Option<$sty> { /* ... */ }
            }
            // ...
        }
    };
}
```

**Repetition substitution -- expanding captured initial values:**

```rust,ignore
// In the matcher: $($inits:expr),+
// In the expansion:
Recurrence { mem: [$($inits),+], pos: 0 }
// If input was "0, 1", this expands to: [0, 1]
```

**Expression substitution -- inserting the recurrence formula:**

```rust,ignore
// In the matcher: $recur:expr
// In the expansion:
let next_val = {
    let n = self.pos;
    let a = IndexOffset { slice: &self.mem, offset: n };
    $recur   // a[n-1] + a[n-2] inserted here
};
```

**Derived computation via helper macro:**

```rust,ignore
// Cannot directly count $inits, so use a helper:
const MEM_SIZE: usize = count_exprs!($($inits),+);
// Passes the repeated captures to another macro for counting
```

# Context & Application

Substitution is the core mechanism that makes macros useful for code generation. Every `macro_rules!` macro relies on substitution to parameterize its output. The practical challenge is that substitution is purely textual (token-level) -- the macro system does not perform type checking or semantic analysis at substitution time. Errors from invalid substitutions only appear when the compiler processes the expanded code.

# Examples

The `recurrence!` macro uses all forms of substitution:

- `$sty` (type): Substituted in 6 positions where the element type is needed (struct fields, trait implementations, function signatures).
- `$($inits),+` (repeated expressions): Substituted in the array literal for initial values and forwarded to `count_exprs!` for computing the array size.
- `$recur` (expression): Substituted into a block where local variables `a` and `n` are in scope, so the expression can reference them.
- `$seq` and `$ind` (identifiers): Substituted as variable names in `let` bindings, ensuring they share the caller's syntax context for hygiene correctness.

# Relationships

- **metavariable**: The captured names that substitution references.
- **macro-repetition**: Repeated captures require matched repetition in the expansion.
- **macro-expansion**: Substitution is the primary mechanism within expansion.
- **macro-hygiene**: Substituted identifiers carry their original syntax context, which affects name resolution.
- **incremental-macro-development**: Substitutions are introduced one at a time in the recommended development process.

# Common Errors

1. **Forgetting repetition wrapper**: Using `$inits` outside a `$( ... )*` block when `inits` was captured inside a repetition. The compiler will report that the variable is used at the wrong repetition depth.
2. **Mismatched separators**: Using a different separator in the expansion repetition than was used in the matcher (e.g., matching with `,` but expanding with `;`).
3. **Substituting into incompatible positions**: Placing an `$e:expr` capture where a type is expected, or vice versa. The error appears at the expansion site, not the macro definition.

# Common Confusions

- **Substitution is not string interpolation**: Captures are token trees, not strings. `$sty` does not produce the text "u64" -- it produces the type token `u64` which the compiler interprets in its grammatical context.
- **Repeated captures are sequences, not concatenations**: `$($inits:expr),+` captures each expression individually as an ordered sequence. It does not paste them together. In the expansion, you choose how to separate them.
- **Helper macros for derived values**: There is no `$inits.len()` or similar. Computing the count of a repeated capture requires a recursive helper macro like `count_exprs!`.

# Source Reference

The Little Book of Rust Macros, Chapter 2 "Macros, A Practical Introduction", "Substitution" section and surrounding code examples. The substitution process is demonstrated across lines 667-981 of the source text.

# Verification Notes

Confidence: high. All substitution mechanics are directly demonstrated in the source with before/after code examples and explicit commentary.
