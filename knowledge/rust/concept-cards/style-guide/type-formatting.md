---
# === CORE IDENTIFICATION ===
concept: Type Formatting
slug: type-formatting

# === CLASSIFICATION ===
category: style
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Rust Style Guide"
source_slug: style-guide
authors: "The Rust Style Team"
chapter: "Types and Bounds"
chapter_number: 4
pdf_page: null
section: "Single line formatting, Line breaks, Precise capturing bounds"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "type style rules"
  - "bound formatting"
  - "trait bound formatting"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - item-formatting
extends: []
related:
  - expression-formatting
  - statement-formatting
  - rust-style-guide
  - formatting-conventions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should types be formatted in Rust?"
  - "How should trait bounds be formatted?"
  - "Where should line breaks go in complex types?"
  - "How should types with + be formatted across lines?"
---

# Quick Definition

Type and bound formatting rules specify spacing and line-breaking for all Rust type syntax: slices, arrays, pointers, references, function types, paths, tuples, trait object bounds (`T + T + T`), and impl trait. The key principles are: no spaces around brackets/angle brackets/parentheses, single spaces around `as` and `+`, and when line-breaking, break at the outermost scope first and break before every `+` in trait bounds.

# Core Definition

Types follow specific single-line spacing rules: no spaces around `[]`, `<>`, `()`, or `::` in type positions; single spaces separating keywords and sigils in reference/pointer/function types (`&'a mut T`, `*const T`, `unsafe extern "C" fn(T) -> U`); spaces after commas in generic/tuple type lists with no trailing commas; and single spaces around `as` in qualified paths and `+` in trait bounds. When line-breaking is necessary, prefer breaking at the outermost scope (e.g., break the outer generic parameters, not inner ones). For types with `+` (trait bounds, impl trait), break before every `+` and block-indent subsequent lines. Array types `[T; expr]` break after the `;`. Function types follow function declaration rules. Generic types follow generics rules. The `use<'a, T>` precise capturing bound is formatted like a trait bound with a path segment named `use`.

# Prerequisites

- **item-formatting** -- type formatting rules are most frequently applied within item signatures (function parameters, return types, struct fields, generics, where clauses)

# Key Properties

1. **Slices**: `[T]` -- no spaces
2. **Arrays**: `[T; expr]` -- space after `;`, no spaces around `[]`; break after `;` if needed
3. **Pointers**: `*const T`, `*mut T` -- no space after `*`, space before type
4. **References**: `&'a T`, `&'a mut T`, `&mut T` -- no space after `&`, single spaces between words
5. **Function types**: `unsafe extern "C" fn(T, U) -> W` -- single spaces around keywords/sigils, commas with spaces, no trailing commas, no spaces around brackets
6. **Never type**: `!` treated like any other type name
7. **Tuples**: `(A, B, C)` -- spaces after commas, no spaces around parens, trailing comma only for one-tuples `(A,)`
8. **Qualified paths**: `<Baz<T> as SomeTrait>::Foo::Bar` -- no spaces around `::` or `<>`, single spaces around `as`
9. **Generic type application**: `Foo::Bar<T, U, V>` -- spaces after commas, no trailing comma, no spaces around `<>`
10. **Trait bounds**: `T + T + T` -- single spaces between types and `+`
11. **Impl trait**: `impl T + T + T` -- single spaces between keyword, types, and `+`
12. **No space around parens in types**: e.g., `(Foo)` has no spaces
13. **Line-break preference**: break at outermost scope first
14. **Trait bound line-breaking**: break before every `+`, block-indent subsequent lines

# Construction / Recognition

## Single-Line Type Formatting:
1. Write types with no spaces inside delimiters: `[T]`, `(A, B)`, `Foo<T, U>`
2. Space after commas in lists, no trailing comma
3. Space around `as` in paths, space around `+` in bounds
4. No space after `&` or `*`; space between `&`/keywords and type name

## Multi-Line Type Formatting:
1. Prefer breaking at the outermost generic scope:
   ```
   Foo<
       Bar,
       Baz<Type1, Type2>,
   >
   ```
   Not:
   ```
   Foo<Bar, Baz<
       Type1,
       Type2,
   >>
   ```
2. For `+` bounds, break before every `+` and block-indent:
   ```
   impl Clone
       + Copy
       + Debug
   ```
3. Inside a generic `Box<>` with bounds:
   ```
   Box<
       Clone
       + Copy
       + Debug
   >
   ```
4. Array types: break after `;`
5. Function types: follow function declaration break rules
6. Generic types: follow generics break rules

# Context & Application

Type formatting interacts with nearly every other formatting rule since types appear in function signatures, let bindings, struct fields, trait bounds, where clauses, and expressions (turbofish, as casts). The "break at outermost scope" rule is essential for readability of deeply nested generic types common in Rust (e.g., `HashMap<String, Vec<Box<dyn Trait>>>`).

The precise capturing bounds syntax (`use<'a, T>`) was introduced for RPITIT (Return Position Impl Trait in Trait) and follows the same formatting as a generic path segment, treating `use` as if it were a trait name.

Despite being the shortest chapter, these rules are frequently referenced by other chapters: generics formatting (Ch 1), type annotations in let statements (Ch 2), and cast expressions (Ch 3) all defer to these type formatting rules.

# Examples

**Example 1** (Single-line type formatting):
```rust
// Slice, array, pointers, references
let a: [u8];
let b: [u32; 42];
let c: *const str;
let d: &'a mut Vec<T>;

// Function type
let f: unsafe extern "C" fn(i32, i32) -> i32;

// Qualified path
let x: <Baz<T> as SomeTrait>::Foo::Bar;

// Trait bounds
let y: Box<dyn Clone + Send + Sync>;
fn foo() -> impl Clone + Copy + Debug { ... }
```

**Example 2** (Break at outermost scope -- preferred):
```rust
// Good: break outermost generic
Foo<
    Bar,
    Baz<Type1, Type2>,
>

// Bad: break inner generic
Foo<Bar, Baz<
    Type1,
    Type2,
>>
```

**Example 3** (Trait bound line-breaking):
```rust
impl Clone
    + Copy
    + Debug

Box<
    Clone
    + Copy
    + Debug
>
```

**Example 4** (Precise capturing bounds):
```rust
fn foo() -> impl Sized + use<'a> {}

// Formatted analogously to:
fn foo() -> impl Sized + Use<'a> {}
```

# Relationships

## Builds Upon
- **item-formatting** -- types most frequently appear in item signatures (where generics and where clause rules apply)

## Enables
None -- type formatting is a reference used by other formatting rules.

## Related
- **expression-formatting** -- `as` casts and turbofish in expressions follow type formatting rules
- **statement-formatting** -- type annotations in let statements follow these rules
- **rust-style-guide** -- this card covers Chapter 4 of the official style guide
- **formatting-conventions** -- general formatting conventions that underpin these rules

## Contrasts With
None explicitly stated.

# Common Errors

- **Error**: Putting spaces inside angle brackets in generic types (`Foo< T, U >`).
  **Correction**: No spaces around angle brackets: `Foo<T, U>`.

- **Error**: Breaking a complex type at an inner scope instead of the outermost scope.
  **Correction**: Always prefer breaking at the outermost scope. `Foo<\n    Bar,\n    Baz<Type1, Type2>,\n>` not `Foo<Bar, Baz<\n    Type1, Type2,\n>>`.

- **Error**: Breaking only some `+` in a trait bound list across lines.
  **Correction**: When breaking trait bounds across lines, break before every `+`, not just some.

# Common Confusions

- **Confusion**: Thinking tuple types always need a trailing comma.
  **Clarification**: Only one-tuples need a trailing comma: `(A,)`. Multi-element tuples do not: `(A, B, C)`.

- **Confusion**: Thinking `use<'a, T>` in precise capturing bounds requires special formatting.
  **Clarification**: It is formatted exactly like a trait bound whose identifier is `use` -- treated as a path segment with angle-bracketed arguments.

# Source Reference

Chapter 4: Types and Bounds. Covers single-line formatting rules for all type syntax (slices, arrays, pointers, references, function types, paths, tuples, generics, trait bounds, impl trait), line-breaking rules (outermost scope preference, `+` breaking), and precise capturing bounds. Rules sourced from the official Rust Style Guide.

# Verification Notes

- Definition source: Direct rules from Chapter 4 "Types and Bounds" of the Rust Style Guide
- Key Properties: All from explicit formatting prescriptions in the source
- Confidence rationale: HIGH -- the source is the authoritative Rust style guide with explicit, prescriptive rules
- Uncertainties: None for the stated rules
- Cross-reference status: All slugs reference cards in this extraction set or planned cross-references
