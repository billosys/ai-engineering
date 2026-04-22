---
# === CORE IDENTIFICATION ===
concept: Statement Formatting
slug: statement-formatting

# === CLASSIFICATION ===
category: style
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Rust Style Guide"
source_slug: style-guide
authors: "The Rust Style Team"
chapter: "Statements"
chapter_number: 2
pdf_page: null
section: "Let statements, else blocks, macros in statement position, expressions in statement position"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "statement style rules"
  - "let statement formatting"
  - "let-else formatting"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - item-formatting
extends: []
related:
  - expression-formatting
  - type-formatting
  - rust-style-guide
  - formatting-conventions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should let statements be formatted in Rust?"
  - "How should let-else statements be formatted?"
  - "How should macros be formatted in statement position?"
  - "When should semicolons be used in Rust statements?"
---

# Quick Definition

Statement formatting in Rust covers `let` bindings (including `let-else`), macros in statement position, and expressions in statement position. The core principles are: space after `:` and around `=`, no space before `;`, single-line when possible, and a specific cascading break strategy for multi-line let statements (break after `=` first, then after `:` if needed).

# Core Definition

Let statements follow the format `let pattern: Type = expr;` with a space after `:` and around `=`, no space before `;`. When a let statement does not fit on one line, first try breaking after `=` with the expression block-indented. If the first line still does not fit, break after `:` as well. For let-else statements (`let pattern = expr else { ... }`), format the entire statement on one line if it is short, the else block is a single expression, and there are no comments. Otherwise, never break between `else` and `{`, always break before `}`, and place the `else {` either on the same line as the initializer or on a new line depending on fit. Macros in statement position use parentheses or square brackets and terminate with a semicolon. Expressions in statement position are terminated with a semicolon unless they end with a block or serve as the block's return value.

# Prerequisites

- **item-formatting** -- statement formatting rules apply within item bodies, so understanding item structure provides necessary context

# Key Properties

1. **Let spacing**: space after `:`, spaces around `=`, no space before `;`
2. **Single-line preference**: format on one line when possible
3. **Multi-line break cascade**: first break after `=` (block-indent expr), then after `:` (block-indent type), then both
4. **Block expressions**: if the expression is a block and the type/pattern is multi-line, put opening brace on a new line (unindented) for visual separation
5. **Let-else single line**: only when entire statement is short, else block is one expression, no comments, and pre-else part fits on one line
6. **Let-else multi-line**: never break between `else` and `{`; always break before `}`; indent `}` to match `let`
7. **Macros in statement position**: use `()` or `[]` delimiters, terminate with `;`, no spaces around `!` or delimiters
8. **Semicolons**: terminate all statement-position expressions with `;` unless they end with a block or are the block's return value; use `;` for void-type expressions even if propagation is possible

# Construction / Recognition

## Let Statement Line-Breaking Strategy:
1. Try single line: `let pattern: Type = expr;`
2. Break after `=`, block-indent expression: `let pattern: Type =\n    expr;`
3. Break after `:` too: `let pattern:\n    Type =\n    expr;`
4. If expression is a block and type/pattern is multi-line, put `{` on its own unindented line

## Let-Else Formatting:
1. Single line if short: `let Some(1) = opt else { return };`
2. If pre-else fits on one line but else block needs multiple lines, put `else {` on same line: `let Some(1) = opt else {\n    return;\n};`
3. If `else {` does not fit on same line as pre-else, break before `else`
4. If initializer is multi-line and ends with closing brackets at the same indent as `let`, put `else {` on that same line
5. Otherwise, put `else {` on next line at `let`'s indentation level

# Context & Application

These rules are enforced by `rustfmt`. The cascading break strategy for let statements ensures readability: the most common case (breaking only the expression) is tried first, with progressively more breaks only when needed. The let-else rules are particularly detailed because let-else was stabilized in Rust 1.65 and its formatting needed careful specification to handle the interaction between the initializer expression, the `else` keyword, and the diverging block.

Key principle: the `else {` placement in let-else depends on whether the closing brackets of the initializer are at the same indentation level as `let` -- if so, `else {` can share that line; otherwise it goes on the next line.

# Examples

**Example 1** (Let statement cascading breaks):
```rust
// Single line
let pattern: Type = expr;

// Break after =
let pattern: Type =
    expr;

// Break after : and =
let pattern:
    Type =
    expr;
```

**Example 2** (Block expression with multi-line pattern):
```rust
// Opening brace on new line for visual separation from multi-line type
let foo:
    ALongType =
{
    an_expression();
    ...
};
```

**Example 3** (Let-else formatting variations):
```rust
// Single line (short)
let Some(1) = opt else { return };

// Multi-line else block
let Some(1) = opt else {
    return;
};

// Pre-else doesn't fit, break before else
    let Some(x) = some_really_really_really_really_really_long_name
    else {
        return;
    };

// Multi-line initializer ending with ) at let indent
let Some(x) = y.foo(
    "abc",
    fairly_long_identifier,
    "def",
) else {
    bar()
}
```

**Example 4** (Multi-line initializer with chained calls -- else on new line):
```rust
fn main() {
    let Some(x) = abcdef()
        .foo(
            "abc",
            some_really_really_really_long_ident,
            "ident",
        )
        .bar()
        .baz()
        .qux("fffffffffffffffff")
    else {
        return
    };
}
```

**Example 5** (Expressions and macros in statement position):
```rust
// Macro in statement position: parens or brackets, semicolon, no spaces
a_macro!(...);

// Expression with void type gets semicolon
foo();

// Block-ending expression: no semicolon for return value
{
    an_expression();
    expr_as_value()
}
```

# Relationships

## Builds Upon
- **item-formatting** -- statements exist within item bodies

## Enables
- **expression-formatting** -- expressions within statements follow expression formatting rules

## Related
- **type-formatting** -- types within let statements follow type formatting rules
- **rust-style-guide** -- this card covers Chapter 2 of the official style guide
- **formatting-conventions** -- general formatting conventions that underpin these rules

## Contrasts With
None explicitly stated.

# Common Errors

- **Error**: Putting a space before the semicolon in a let statement.
  **Correction**: No space before the semicolon: `let x = 5;` not `let x = 5 ;`.

- **Error**: Breaking between `else` and `{` in a let-else statement.
  **Correction**: Never break between `else` and `{`. They must always be on the same line as `else {`.

- **Error**: Omitting the semicolon after a void-returning function call because its value "doesn't matter."
  **Correction**: Use a semicolon for void-type expressions even if the value could be propagated. Write `foo();` in `fn bar() { foo(); }`.

# Common Confusions

- **Confusion**: Thinking the opening `{` of a block expression in a let statement always goes on the same line as `=`.
  **Clarification**: If the type or pattern covers multiple lines and the expression is a block, put the opening `{` on a new unindented line for visual separation from the block's interior.

- **Confusion**: Thinking let-else always puts `else {` on the same line as the initializer.
  **Clarification**: `else {` goes on the same line only when the initializer's closing brackets are at the same indentation as `let`. If the initializer ends with a chained method call at a different indentation, `else` goes on the next line at `let`'s indentation level.

# Source Reference

Chapter 2: Statements. Covers let statements (including multi-line cascading break rules), else blocks (let-else statements with detailed placement rules for the `else {` token), macros in statement position, and expressions in statement position. Rules sourced from the official Rust Style Guide.

# Verification Notes

- Definition source: Direct rules from Chapter 2 "Statements" of the Rust Style Guide
- Key Properties: All from explicit formatting prescriptions in the source
- Confidence rationale: HIGH -- the source is the authoritative Rust style guide with explicit, prescriptive rules and numerous examples
- Uncertainties: None for the stated rules
- Cross-reference status: All slugs reference cards in this extraction set or planned cross-references
