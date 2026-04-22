---
concept: Statements and Expressions
slug: rust-statements-and-expressions
category: language-fundamentals
subcategory: null
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Statements and Expressions"
chapter_number: 8
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "expression-oriented language"
  - "place expressions"
  - "value expressions"
  - "expression statements"
  - "declaration statements"
  - "block expressions"
prerequisites: []
extends: []
related:
  - rust-operator-expressions
  - rust-patterns
contrasts_with: []
answers_questions:
  - "What makes Rust an expression-oriented language?"
  - "What are the two kinds of statements in Rust?"
  - "What is the difference between a place expression and a value expression?"
  - "What are the two main categories of expressions (with-block and without-block)?"
  - "How does a block expression determine its value?"
  - "What is the expression precedence order in Rust?"
  - "What is an assignee expression?"
  - "How do temporaries work in Rust expressions?"
  - "What is the evaluation order for operands?"
  - "When does a block expression diverge?"
---

# Quick Definition

Rust is primarily an expression language: most value-producing or effect-causing evaluation uses the uniform syntax category of expressions, which can nest arbitrarily. Statements serve mostly to contain and sequence expression evaluation. Expressions divide into two fundamental categories -- place expressions (representing memory locations) and value expressions (representing actual values) -- and structurally into ExpressionWithBlock and ExpressionWithoutBlock.

# Core Definition

**Statements** come in two kinds: **declaration statements** (item declarations and `let` statements) and **expression statements** (an expression followed by a semicolon). Item declarations within a block are scoped to that block. `let` statements introduce variables via a pattern, optionally with a type annotation and initializer. Since edition 2024, `let ... else` allows refutable patterns with a diverging else block.

**Expressions** always produce a value and may have side effects. They divide structurally into:

- **ExpressionWithoutBlock**: literals, paths, operators, grouped, array, tuple, struct, call, method call, field, closure, await, continue, break, range, return, underscore, and macro invocations.
- **ExpressionWithBlock**: block, const block, unsafe block, loop, if, and match expressions. These can omit a trailing semicolon when used as statements.

Expressions are also categorized by what they represent:

- **Place expressions** represent memory locations: local variables, statics, dereferences (`*expr`), array indexing (`expr[expr]`), field access (`expr.f`), and parenthesized place expressions. Historically called "lvalues."
- **Value expressions** represent actual values -- everything else. Historically called "rvalues."
- **Assignee expressions** appear on the left of assignment: place expressions, underscores, tuples/slices/structs of assignee expressions.

**Block expressions** are both control flow expressions and anonymous namespace scopes. A block's value is its final operand (the trailing expression without a semicolon); without one, the block has unit type `()`. A block with no final operand that diverges has the never type `!`.

# Prerequisites

- None -- this is a foundational concept

# Key Properties

1. Rust is primarily an expression language: most forms of evaluation are expressions, and blocks are just another kind of expression, enabling arbitrary nesting of blocks, statements, and expressions
2. Expression statements consisting of only a block or control flow expression can omit the trailing semicolon; the block's type must then be `()`
3. Place expressions can appear in place contexts (left of compound assignment, operand of borrow/deref, field access operand, array index operand, scrutinee of `if let`/`match`/`while let`, initializer of `let`, base of functional update)
4. When a place expression is evaluated in a value expression context, the value is either copied (if `Copy`) or moved (if `Sized` and the place is movable)
5. Operands of most expressions are evaluated left to right, but assignment evaluates the right operand first
6. Expression precedence goes from strong to weak: paths, method calls, field expressions, function calls/indexing, `?`, unary operators, `as`, multiplicative, additive, shifts, bitwise AND, XOR, OR, comparisons, `&&`, `||`, ranges, assignment/compound assignment, `return`/`break`/closures
7. Comparison operators require parentheses when combined and do not chain -- `a == b == c` is not valid
8. A `let` statement with an `else` block allows refutable patterns; the else block must diverge (evaluate to `!`)
9. Variables introduced by `let` are visible from the point of declaration to the end of the enclosing block, unless shadowed
10. Temporaries are created when value expressions appear in place expression contexts; they are typically dropped at the end of the enclosing statement

# Construction / Recognition

## To recognize an ExpressionWithBlock vs. ExpressionWithoutBlock:
1. **With block**: starts with or contains a `{ }` block as primary structure -- `if`, `match`, `loop`/`while`/`for`, plain blocks, `unsafe`/`const`/`async` blocks
2. **Without block**: everything else -- literals, paths, operators, calls, closures, `return`, `break`, `continue`, ranges, `await`

## To determine a block's value:
1. If the block ends with an expression without a semicolon (the final operand), that expression's value is the block's value
2. If the block ends with a semicolon or has no final expression, the block has value `()`
3. If the block diverges (all paths contain diverging expressions), it has type `!`

## To identify place vs. value context:
1. Left of `=` or compound assignment -> place/assignee context
2. Operand of `&`, `&mut`, `&raw const`, `&raw mut`, `*` -> place context
3. Scrutinee of `match`, `if let`, `while let` -> place context
4. Everything else -> value context

# Context & Application

The expression-oriented design is fundamental to Rust's ergonomics. Since `if`, `match`, `loop`, and blocks are all expressions, they can appear anywhere a value is needed: `let x = if cond { a } else { b };` or `let y = loop { break 42; };`. This eliminates the need for a ternary operator and reduces the need for mutable variables. The place/value distinction underpins Rust's ownership system: when a place expression appears in value context, the compiler decides whether to copy or move based on `Copy`. Expression statements (adding `;`) discard a value, converting an expression to a statement -- and removing the trailing semicolon from a block's last expression changes its type from `()` to the expression's type, which is a common source of type errors for newcomers.

# Examples

**Example 1** (Ch. 8, "Block expressions"): Blocks as expressions with values:
```rust
let x: u8 = { 0u8 };          // final operand is 0u8
let y: () = { 0u8; };         // semicolon makes it a statement; block is ()
let z = if true { 1 } else { 2 }; // if expression used as value
```

**Example 2** (Ch. 8, "let statements"): The `let ... else` pattern:
```rust
let mut v = vec![1, 2, 3];
let Some(t) = v.pop() else {
    panic!();  // else block must diverge
};
```

**Example 3** (Ch. 8, "Place expressions and value expressions"): Place context determines copy vs. move:
```rust
let s = String::from("hello");  // s is a place expression
let t = s;                       // s evaluated in value context -> moved
// s is now deinitialized and cannot be read

let n = 42i32;                   // n is a place expression
let m = n;                       // n evaluated in value context -> copied (i32: Copy)
// n is still valid
```

# Relationships

## Builds Upon
- None

## Enables
- **rust-operator-expressions** -- operators are a major subcategory of expressions
- **rust-patterns** -- patterns are used in `let` statements, `match` arms, `if let`, and `while let`

## Related
- **rust-operator-expressions** -- detailed treatment of operator expression subcategories
- **rust-patterns** -- pattern matching is integral to `match`, `if let`, `while let`, and `let` bindings

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Forgetting the semicolon difference -- `{ expr }` vs. `{ expr; }` produce different types.
  **Correction**: A block ending with `expr` has the type of `expr`; ending with `expr;` discards the value and has type `()`. This commonly causes "expected `()`, found `i32`" errors.

- **Error**: Trying to use a moved-from place expression after a move.
  **Correction**: After a place expression is evaluated in value context and the type does not implement `Copy`, the location is deinitialized. Either use a reference, clone the value, or restructure to avoid the move.

- **Error**: Using an `if` expression as a value without an `else` branch.
  **Correction**: When `if` is used as a value expression, it must have an `else` branch so the type is defined in all cases. Without `else`, the missing branch has type `()`.

# Common Confusions

- **Confusion**: Thinking statements and expressions are mutually exclusive categories.
  **Clarification**: Expression statements are statements that evaluate an expression and discard the result. The same expression can appear as a statement (with `;`) or as a value-producing expression (without `;` at the end of a block).

- **Confusion**: Thinking `if` and `match` in Rust work like statements in C-like languages.
  **Clarification**: In Rust, `if`, `match`, `loop`, and blocks are all expressions that produce values. You can assign their results: `let x = match v { ... };`. All arms must produce compatible types.

- **Confusion**: Mixing up place expressions with references.
  **Clarification**: A place expression represents a memory location, not a reference. Taking a reference (`&expr`) requires the operand to be in place context, producing a pointer to that location. The place expression itself is the location; the reference is a value that points to it.

# Source Reference

Chapter 8 of The Rust Reference: "Statements and Expressions" -- covers all statement types (declaration statements, let statements, expression statements), the complete expression taxonomy (ExpressionWithoutBlock and ExpressionWithBlock), place vs. value expression categories, expression precedence, evaluation order, temporaries, and block expression semantics. Lines 1-530 cover statements and the expression framework; lines 530-4857 cover each expression kind in detail.

# Verification Notes

- Definition source: Directly from Chapter 8 of The Rust Reference, with taxonomy and key properties synthesized from the chapter's first 530 lines plus section headers across 4857 lines
- Key Properties: All derived from explicit rules stated in the reference (r[expr.place-value], r[expr.precedence], r[expr.operand-order], r[statement.let], r[expr.block])
- Confidence rationale: HIGH -- all content comes from the authoritative language reference with explicit rule identifiers
- Uncertainties: None significant; the reference is definitive for these topics
- Cross-reference status: rust-operator-expressions and rust-patterns are companion cards in the same extraction set
