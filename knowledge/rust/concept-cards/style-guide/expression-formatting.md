---
# === CORE IDENTIFICATION ===
concept: Expression Formatting
slug: expression-formatting

# === CLASSIFICATION ===
category: style
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Rust Style Guide"
source_slug: style-guide
authors: "The Rust Style Team"
chapter: "Expressions"
chapter_number: 3
pdf_page: null
section: "Blocks, Closures, Struct/Tuple/Array literals, Operators, Function/Method calls, Chains, Control flow, Match, Combinable expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "expression style rules"
  - "match formatting"
  - "chain formatting"
  - "closure formatting"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - item-formatting
extends: []
related:
  - statement-formatting
  - type-formatting
  - rust-style-guide
  - formatting-conventions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should method chains be formatted in Rust?"
  - "How should match expressions be formatted?"
  - "How should closures be formatted in Rust?"
  - "How should function and method calls be formatted?"
  - "How should struct, tuple, and array literals be formatted?"
  - "How should blocks and control flow be formatted?"
  - "What are combinable expressions in the Rust style guide?"
---

# Quick Definition

Expression formatting covers the largest section of the Rust Style Guide -- blocks, closures, literals (struct, tuple, array), operators (unary, binary, ranges), function/method calls, method chains, control flow (if/else, loops, match), and combinable expressions. The overarching principle is single-line when small, block-indented multi-line otherwise, with specific rules for chains (break before `.`), match arms (trailing comma when no block), and combinable expressions (nesting single-argument multi-line calls).

# Core Definition

Expressions follow a "small means single-line" principle: if an expression is small enough, keep it on one line; otherwise, use block-indentation with consistent break points. Blocks require a newline after `{` and before `}` unless they qualify for single-line treatment (expression position, single expression, no statements or comments). Closures omit `{}` when possible, adding them for return types, statements, comments, or multi-line control flow. Function calls break after `(` and before `)` with each argument block-indented and a trailing comma. Method chains break before each `.` with block indentation, preferring multi-line-all over mixed formatting. Match expressions block-indent arms once, use trailing commas only when not using a block body, and never break after `=>` without a block. Combinable expressions allow nesting a single multi-line argument directly within the outer call's parentheses.

# Prerequisites

- **item-formatting** -- expressions exist within item bodies; function call formatting mirrors function definition formatting

# Key Properties

1. **Blocks**: newline after `{` and before `}` unless single-line eligible (expression position, single expression, no statements/comments); spaces after `{` and before `}` in single-line form; write empty blocks as `{}`
2. **Closures**: no extra space before first `|`; space between second `|` and body; omit `{}` when possible; add `{}` for return types, statements, comments, or multi-line control flow
3. **Unary ops**: no space between operator and operand (`!x`), except `&mut` (space after `&mut`)
4. **Binary ops**: spaces around all binary operators including `=` and `+=`; break before operator (except assignment operators, which break after); use parentheses liberally for precedence
5. **Function calls**: no space between name and `(`; single-line has no trailing comma; multi-line puts each arg on its own block-indented line with trailing comma
6. **Method chains**: break before `.` and after `?`; block-indent each subsequent line; if any element is multi-line, put it and all later elements on their own lines; prefer all-multi-line over mixed formatting
7. **Control flow (if/else/loops)**: no extraneous parentheses; `} else {` on one line; if control line breaks, opening `{` goes on its own unindented line; single-line `if else` only in expression position when small
8. **Match**: block-indent arms once; trailing comma only when not using block body; never start a pattern with `|`; never break after `=>` without a block; prefer block body if it avoids breaking the left-hand side
9. **Combinable expressions**: a single multi-line argument may be nested inside the outer call without breaking; applies recursively; also applies to last-argument closures with explicit blocks when no other closure arguments exist
10. **Ranges**: no spaces (`0..10`, `x..=y`); use parentheses for compound bounds (`..(x + 1)`)
11. **Struct literals**: space before `{`; spaces inside braces for single-line; `field: value` (space after colon only); functional update `..expr` has no space after `..`
12. **Array literals**: no spaces inside `[]`; repeating initializer spaces after `;` only (`[42; 10]`); multi-line follows function call rules

# Construction / Recognition

## Method Chain Formatting:
1. Single line if small: `x.foo().bar().baz(x, y, z);`
2. Multi-line: break before each `.`, block-indent, break after `?`:
   ```
   let foo = bar
       .baz?
       .qux();
   ```
3. Combining rule: if the last line of the first element plus its indent is <= the indent of the second line, combine first and second lines if they fit
4. Multi-line elements: once any element is multi-line, that element and all subsequent go on their own lines

## Match Arm Formatting:
1. Right-hand side on same line if it is a single non-control-flow expression: `foo => bar,`
2. Use a block if: multiple statements, line comments, expression doesn't fit, or right-hand side is a macro call (to preserve potential trailing semicolons)
3. Block arms: no trailing comma, block-indent body
4. Pattern breaking: put each `|` clause on its own line (break before `|`, no leading `|`); if there's an `if` guard, break before `if` and block-indent it
5. Prefer block body if it avoids breaking the left-hand side pattern

## Combinable Expressions:
1. Single-argument call with multi-line argument: nest directly:
   ```
   foo(bar(
       an_expr,
       another_expr,
   ))
   ```
2. Also applies to struct literals, closures, arrays as single arguments
3. For multi-argument calls, only the last argument may be a multi-line closure with explicit block (and no other closures)
4. Apply recursively

# Context & Application

This is the largest chapter of the Rust Style Guide because expressions are the most varied syntactic category. The rules are enforced by `rustfmt`. The chain formatting rules are particularly important in idiomatic Rust where method chaining and the `?` operator are pervasive. The combinable expression rules prevent excessive indentation nesting that would otherwise occur with common patterns like `foo(bar(...))` or `foo(|x| { ... })`.

Key design decisions: preferring all-multi-line chain formatting over mixed (some elements on one line, some on multiple) improves readability; requiring block bodies for match arms with multiple statements or comments maintains clear visual structure; allowing single-line `if else` only in expression position prevents ambiguity with standalone if statements.

The `as` cast is formatted like a binary operator but with a special rule: when chaining multiple `as` casts, if breaking before the first `as` makes the remainder fit, keep all subsequent casts on the same line rather than breaking before each one.

# Examples

**Example 1** (Method chain formatting):
```rust
// Prefer all-multi-line with each element on one line:
self.pre_comment
    .as_ref()
    .map_or(false, |comment| comment.starts_with("//"))

// Worse: mixed single/multi-line
self.pre_comment.as_ref().map_or(
    false,
    |comment| comment.starts_with("//"),
)
```

**Example 2** (Match arms):
```rust
match foo {
    foo => bar,
    a_very_long_pattern | another_pattern if an_expression() => {
        no_room_for_this_expression()
    }
    foo => {
        // A comment.
        an_expression()
    }
    foo => {
        let a = statement();
        an_expression()
    }
    bar => {}
}
```

**Example 3** (Match arm line-breaking with guard):
```rust
    a_very_long_pattern
    | another_pattern
    | yet_another_pattern
        if expr =>
    {
        ...
    }
```

**Example 4** (Closures):
```rust
// Simple: no braces
|arg1, arg2| expr

// With return type or statements: use braces
move |arg1: i32, arg2: i32| -> i32 {
    expr1;
    expr2
}

// Struct literal body: no braces needed
|| Foo {
    field1,
    field2: 0,
}

// Multi-line control flow: use braces
|| {
    if true {
        blah
    } else {
        boo
    }
}
```

**Example 5** (Combinable expressions):
```rust
// Single-argument nesting
foo(bar(
    an_expr,
    another_expr,
))

// Struct literal as single argument
let x = foo(Bar {
    field: whatever,
});

// Last-argument closure
foo(first_arg, x, |param| {
    action();
    foo(param)
})
```

**Example 6** (Control flow with broken control line):
```rust
while let Some(foo)
    = a_long_expression
{
    ...
}

if a_long_expression
    && another_long_expression
    || a_third_long_expression
{
    ...
}
```

# Relationships

## Builds Upon
- **item-formatting** -- function call formatting mirrors function definition formatting

## Enables
None -- expressions are leaf-level formatting rules.

## Related
- **statement-formatting** -- expressions appear within statements; let-else uses expression formatting
- **type-formatting** -- types within expressions (casts, turbofish) follow type formatting rules
- **rust-style-guide** -- this card covers Chapter 3 of the official style guide
- **formatting-conventions** -- general formatting conventions that underpin these rules

## Contrasts With
None explicitly stated.

# Common Errors

- **Error**: Starting a match arm pattern with `|` (e.g., `| foo => bar`).
  **Correction**: Never start a match arm pattern with `|`. Write `foo => bar` or `a_long_pattern\n| another_pattern => { ... }`.

- **Error**: Using a trailing comma on a match arm that uses a block body.
  **Correction**: Use a trailing comma only when NOT using a block body. Block arms do not get trailing commas.

- **Error**: Breaking after `=>` in a match arm without using a block.
  **Correction**: Never break after `=>` without the block form. If the right-hand side doesn't fit on the same line, wrap it in a block `{ ... }`.

- **Error**: Mixing single-line and multi-line elements in a method chain.
  **Correction**: Prefer formatting the whole chain in multi-line style with each element on one line, rather than putting some elements on multiple lines and some on one line.

# Common Confusions

- **Confusion**: Thinking all blocks can be written on a single line.
  **Clarification**: A block can be single-line only if it is in expression position (not statement position), contains a single expression (no statements), and contains no comments. Blocks in statement position must always be multi-line (except unsafe blocks).

- **Confusion**: Thinking closures always need `{}` braces.
  **Clarification**: Omit `{}` when possible. Only add them for: return types, statements in the body, comments in the body, or multi-line control flow expressions.

- **Confusion**: Thinking combinable expressions only apply to function calls.
  **Clarification**: Combinable expression rules apply to any expression with multi-line block-indented sub-expressions delimited by parentheses, including macros, tuple struct literals, and last-argument closures with explicit blocks.

# Source Reference

Chapter 3: Expressions. Covers blocks, closures, struct/tuple/array/enum literals, array accesses, unary and binary operations (including `as` casts), control flow (if/else/for/loop/while including let-chains), function and method calls, macro uses, method chains, match expressions (arms, line-breaking, combinable arms), combinable expressions, ranges, hexadecimal literals, and patterns. Rules sourced from the official Rust Style Guide.

# Verification Notes

- Definition source: Direct rules from Chapter 3 "Expressions" of the Rust Style Guide
- Key Properties: All from explicit formatting prescriptions in the source
- Confidence rationale: HIGH -- the source is the authoritative Rust style guide with explicit, prescriptive rules and extensive examples
- Uncertainties: None for the stated rules
- Cross-reference status: All slugs reference cards in this extraction set or planned cross-references
