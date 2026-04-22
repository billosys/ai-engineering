---
concept: Macro Expansion
slug: macro-expansion
category: macro-system
subcategory: null
tier: intermediate
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "01-methodical-introduction"
chapter_number: 1
pdf_page: null
section: "Expansion"
extraction_confidence: high
aliases:
  - "macro transcription"
  - "expansion"
  - "macro substitution"
prerequisites:
  - macro-rules
  - token-tree
  - metavariable
extends: []
related:
  - syntax-extension
  - macro-matcher
  - macro-hygiene
contrasts_with: []
answers_questions:
  - "How are Rust macros expanded?"
  - "When does macro expansion happen in the compilation pipeline?"
  - "Is macro expansion token-based or AST-based?"
  - "What happens when a macro expands to another macro invocation?"
  - "What is the macro recursion limit?"
---

# Quick Definition

Macro expansion is the process of replacing a macro invocation with its expansion output. It happens after AST construction but before semantic analysis. The expansion is a structural AST operation (not textual), and the result is always parsed as a complete AST node. Expansion proceeds in passes until no more macro invocations remain, up to a recursion limit (default 32).

# Core Definition

Expansion occurs at some point after the construction of the AST but before the compiler begins constructing its semantic understanding of the program. It involves traversing the AST, locating macro invocations, and replacing them with their expansion.

The compiler parses the expansion result into an AST node based on context:
- Expression position: parsed as an expression
- Module scope: parsed as an item
- Statement position: parsed as a statement

More precisely, a syntax extension result can become:
- an expression
- a pattern
- zero or more items
- zero or more `impl` items
- zero or more statements

This is a **structural operation, not a textual one**. The compiler always treats the expansion of a macro as a complete AST node. Even without explicit parentheses, the compiler cannot "misinterpret" the result or change the order of evaluation.

When an expansion contains another macro invocation, the compiler performs another expansion pass. This continues until all invocations are fully expanded, up to the macro recursion limit (default 32, configurable with `#![recursion_limit="..."]`).

# Prerequisites

- **macro-rules** -- Expansion is the output side of `macro_rules!` definitions
- **token-tree** -- Understanding why expansion produces AST nodes, not token sequences
- **metavariable** -- Captured values are substituted during expansion

# Key Properties

1. **AST-level operation**: Expansion replaces AST nodes structurally, not textually.
2. **Context-dependent parsing**: The expansion result is parsed based on the invocation position (expression, item, statement, etc.).
3. **Implicit grouping**: Expanded expressions behave as if parenthesized, even without explicit parens.
4. **Multi-pass**: Expansion proceeds in passes until no invocations remain.
5. **Recursion limit**: Default limit of 32 passes, configurable with `#![recursion_limit="..."]`.
6. **Must be valid**: Macros can only expand to syntactically valid constructs for the expected AST node type.
7. **Cannot produce fragments**: Macros cannot expand to incomplete or syntactically invalid constructs.

# Construction / Recognition

## AST-level expansion example

```rust
macro_rules! four {
    () => { 1 + 3 };
}

let eight = 2 * four!();
```

The expansion produces `2 * (1 + 3)`, NOT `2 * 1 + 3`, because the macro expansion `1 + 3` is treated as a complete expression AST node. The result is `8`, not `5`.

## Recursive expansion

```rust
macro_rules! four {
    () => { 1 + three!() };
}

macro_rules! three {
    () => { 3 };
}

let x = four!();
// First pass: let x = 1 + three!();
// Second pass: let x = 1 + 3;
```

## Raising the recursion limit

```rust
#![recursion_limit="128"]
```

# Context & Application

The AST-level nature of macro expansion is one of Rust's key safety features for macros. Unlike C/C++ preprocessor macros, which perform textual substitution and can produce unexpected results due to operator precedence, Rust macros always produce structurally correct code.

This means:
- `2 * four!()` where `four!` expands to `1 + 3` always evaluates as `2 * (1 + 3) = 8`
- In C, `#define four 1 + 3` would make `2 * four` evaluate as `2 * 1 + 3 = 5`

The multi-pass expansion allows macros to compose: one macro can expand to code containing other macro invocations. This enables powerful patterns like recursive macros that expand step-by-step, but requires awareness of the recursion limit.

The position-dependent parsing means that where you invoke a macro determines what it must expand to. A macro invoked in expression position must produce a valid expression; one invoked at module scope must produce valid items.

# Examples

**AST-level structural expansion** (from "Expansion" section):

Given `let eight = 2 * four!();` where `four!` expands to `1 + 3`, the AST transformation replaces the `Macro` node with a `BinOp(Add, 1, 3)` node:

Before expansion:
```text
Let(eight) -> BinOp(Mul) -> lhs: LitInt(2)
                          -> rhs: Macro(four, ())
```

After expansion:
```text
Let(eight) -> BinOp(Mul) -> lhs: LitInt(2)
                          -> rhs: BinOp(Add) -> lhs: LitInt(1)
                                              -> rhs: LitInt(3)
```

Equivalent to `let eight = 2 * (1 + 3);` -- parens added despite not being in the expansion, because the expansion is an AST node, not a token sequence.

**Multi-pass expansion** (from "Expansion" section):

```rust
let x = four!();
// four! expands to: 1 + three!()
// three! expands to: 3
// Final result: let x = 1 + 3;
```

The takeaway: "expansion happens in 'passes'; as many as is needed to completely expand all invocations."

# Relationships

## Builds Upon

- **macro-rules** -- Expansion is the right-hand side of macro rules
- **metavariable** -- Captured values are substituted during expansion
- **syntax-extension** -- All syntax extensions go through the expansion process

## Related

- **macro-hygiene** -- Applies during expansion to prevent naming collisions
- **macro-matcher** -- The pattern-matching side that triggers expansion
- **token-tree** -- Input to expansion is token trees; output is AST nodes

# Common Errors

1. **Expecting textual substitution**: Writing `2 * my_macro!()` and expecting C-like token pasting. Rust always treats the expansion as a complete AST node.
2. **Exceeding recursion limit**: Deeply recursive macros (more than 32 levels) fail without explicitly raising `#![recursion_limit="..."]`.
3. **Wrong position**: Invoking a macro in expression position when it expands to an item (or vice versa) causes a parse error.

# Common Confusions

- **Confusion**: Thinking macro expansion is like C preprocessor text substitution.
  **Clarification**: Rust macro expansion is a structural AST operation. `2 * four!()` where `four!` expands to `1 + 3` evaluates as `2 * (1 + 3) = 8`, not `2 * 1 + 3 = 5`. The parentheses are implicit because the expansion is an AST node.
- **Confusion**: Thinking expansion happens during tokenisation or parsing.
  **Clarification**: Expansion happens after the AST is constructed, but before semantic analysis. This is fundamentally different from C/C++ where macro expansion happens during tokenisation.
- **Confusion**: Believing the recursion limit of 32 cannot be changed.
  **Clarification**: The limit can be raised with `#![recursion_limit="..."]` at the crate level, though it's recommended to keep macros below the default limit when possible.

# Source Reference

"The Little Book of Rust Macros" by Daniel Keep et al., Chapter 1: "Methodical Introduction," section "Expansion."

# Verification Notes

- AST-level expansion with `four!` example: directly from the source with full AST diagrams
- Recursive expansion: directly from the source
- Recursion limit (default 32): explicitly stated in the source
- The list of valid expansion targets (expression, pattern, items, impl items, statements): directly enumerated
- "This is a structural operation, not a textural one!" -- direct quote (with source's spelling of "textural")
- Confidence: HIGH -- detailed treatment with AST diagrams and multiple examples
