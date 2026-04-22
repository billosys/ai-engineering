---
concept: Operator Expressions
slug: rust-operator-expressions
category: language-fundamentals
subcategory: null
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Statements and Expressions"
chapter_number: 8
pdf_page: null
section: "Operator expressions"
extraction_confidence: high
aliases:
  - "borrow operators"
  - "dereference operator"
  - "try operator"
  - "question mark operator"
  - "type cast expressions"
  - "assignment expressions"
  - "compound assignment"
  - "arithmetic operators"
  - "comparison operators"
  - "lazy boolean operators"
  - "negation operators"
  - "destructuring assignment"
prerequisites:
  - rust-statements-and-expressions
extends: []
related:
  - rust-patterns
contrasts_with: []
answers_questions:
  - "What are all the operator expression types in Rust?"
  - "How does the try operator (?) work with Result, Option, and ControlFlow?"
  - "What happens on integer overflow in debug vs. release mode?"
  - "How does type casting with 'as' work for numeric types?"
  - "What is the difference between & and &raw const/&raw mut?"
  - "How does destructuring assignment work?"
  - "Which operators can be overloaded and which cannot?"
  - "What are lazy boolean operators and how do they differ from bitwise operators?"
  - "How does the dereference operator interact with Deref/DerefMut traits?"
  - "What numeric cast semantics does Rust define (truncation, saturation, rounding)?"
---

# Quick Definition

Operator expressions encompass ten categories: borrow (`&`/`&mut`/`&raw`), dereference (`*`), try propagation (`?`), negation (`-`/`!`), arithmetic and logical binary operators (`+`, `-`, `*`, `/`, `%`, `&`, `|`, `^`, `<<`, `>>`), comparison (`==`, `!=`, `<`, `>`, `<=`, `>=`), lazy boolean (`&&`, `||`), type cast (`as`), assignment (`=`), and compound assignment (`+=`, `-=`, etc.). Most can be overloaded via `std::ops` traits; borrow, dereference, and assignment cannot.

# Core Definition

**Borrow operators** (`&` and `&mut`) produce references to place expressions. Applied to value expressions, they create temporaries. `&raw const` and `&raw mut` produce raw pointers without creating references, which is necessary for unaligned or potentially invalid memory locations (e.g., packed struct fields). The `&&` token in borrow context acts as two borrows, not the lazy AND operator.

**Dereference** (`*`) on pointers/`Box` denotes the pointed-to location. On non-pointer types, it desugars to `Deref::deref()` or `DerefMut::deref_mut()`. Dereferencing raw pointers requires `unsafe`.

**Try propagation** (`?`) uses the `Try` trait to short-circuit: on `Result`, `Ok(v)` produces `v` and `Err(e)` returns `Err(From::from(e))`; on `Option`, `Some(v)` produces `v` and `None` returns `None`; on `ControlFlow`, `Continue(c)` produces `c` and `Break(b)` returns `Break(b)`. Also works on `Poll<Result>` and `Poll<Option<Result>>`.

**Arithmetic and logical binary operators** follow standard semantics with overloading via `std::ops` traits. Integer overflow panics in debug mode (controlled by `-C overflow-checks`). Integer division rounds toward zero. The `%` operator uses truncating division (remainder has same sign as dividend). Right shift is arithmetic for signed integers, logical for unsigned.

**Comparison operators** (`==`, `!=`, `<`, `>`, `<=`, `>=`) require parentheses and do not chain. They are overloaded via `PartialEq` and `PartialOrd`.

**Lazy boolean operators** (`&&`, `||`) short-circuit: the right operand is evaluated only if the left does not determine the result. They are not overloadable and work only on `bool`.

**Type cast** (`as`) performs numeric casts (truncation, sign/zero extension, float-to-int saturation), enum-to-integer discriminant casts, pointer casts, and function item/pointer conversions. Float-to-int casting saturates: `NaN` becomes `0`, `INFINITY` becomes the maximum integer value.

**Assignment** (`=`) evaluates the right operand first, then the left. The assigned-to place's old value is dropped before the new value is stored. Assignment always produces `()`. **Destructuring assignment** allows patterns on the left: `(a, b) = (3, 4)` desugars to a `let` binding followed by sequential assignments. **Compound assignment** (`+=`, etc.) evaluates the right operand first, then the left, and are overloaded via `AddAssign`, `SubAssign`, etc.

# Prerequisites

- **Statements and expressions** -- operator expressions are a subcategory of expressions; understanding place vs. value context is essential

# Key Properties

1. Integer overflow panics in debug mode; in release mode, it wraps (two's complement for signed types). The `-C overflow-checks` flag controls this independently
2. Division by zero always panics for integers, regardless of overflow-checks settings; `MIN / -1` for signed integers also always panics
3. The `?` operator works on `Result`, `Option`, `ControlFlow`, `Poll<Result>`, and `Poll<Option<Result>>`; the `Try` trait is currently unstable and cannot be implemented for user types
4. Borrow, raw borrow, dereference, and assignment operators cannot be overloaded
5. Lazy boolean operators (`&&`, `||`) are distinct from bitwise operators (`&`, `|`) -- lazy booleans short-circuit and work only on `bool`; bitwise operators are overloadable and apply to integers too
6. `&raw const` and `&raw mut` create raw pointers without forming references, avoiding UB for unaligned or uninhabited locations
7. Numeric casts with `as` have specific saturation semantics: float-to-int rounds toward zero, `NaN` becomes `0`, values beyond range saturate to min/max
8. Larger-to-smaller integer casts truncate; smaller-to-larger zero-extend (unsigned) or sign-extend (signed)
9. Assignment evaluates right-to-left (right operand first), unlike most other expressions which evaluate left-to-right
10. Compound assignment evaluates the right operand, then the left operand, then calls the trait method; it takes a mutable reference to the left operand (not by value like binary operators)

# Construction / Recognition

## To use the try operator effectively:
1. The enclosing function must return a type compatible with the operand's error type (e.g., `Result<T, E>` for `?` on `Result`)
2. Error conversion via `From::from()` is applied automatically, so the function's error type need not exactly match the operand's
3. For `Option`, the function must return `Option`; for `ControlFlow`, it must return `ControlFlow`

## To perform safe numeric conversions:
1. Use `as` for primitive numeric casts (with awareness of truncation/saturation semantics)
2. Use `From`/`Into` for infallible widening conversions
3. Use `TryFrom`/`TryInto` for fallible narrowing conversions that should not silently truncate
4. Float-to-int: values round toward zero, `NaN` becomes `0`, out-of-range saturates

## To use destructuring assignment:
1. Write assignee expressions (tuples, arrays, structs) on the left of `=`
2. The desugared patterns must be irrefutable
3. Identifiers may appear multiple times; `_` discards values

# Context & Application

Operator expressions are the workhorses of Rust computation. The overflow-panic-in-debug behavior catches bugs during development while avoiding runtime overhead in release builds. The `?` operator is central to Rust's error handling story, replacing verbose `match` expressions on `Result`/`Option` with concise propagation. The distinction between lazy boolean (`&&`/`||`) and bitwise operators (`&`/`|`) matters because `&` and `|` on `bool` evaluate both sides (useful for side effects) while `&&` and `||` short-circuit. Raw borrow operators (`&raw const`/`&raw mut`) were added specifically to support `unsafe` code that needs to create pointers to potentially unaligned or invalid locations without triggering UB through intermediate reference creation.

# Examples

**Example 1** (Ch. 8, "Borrow operators"): Raw borrows for packed structs:
```rust
#[repr(packed)]
struct Packed { f1: u8, f2: u16 }
let packed = Packed { f1: 1, f2: 2 };
// &packed.f2 would create an unaligned reference -- UB!
let raw_f2 = &raw const packed.f2;
assert_eq!(unsafe { raw_f2.read_unaligned() }, 2);
```

**Example 2** (Ch. 8, "Try propagation"): The `?` operator on multiple types:
```rust
fn try_to_parse() -> Result<i32, std::num::ParseIntError> {
    let x: i32 = "123".parse()?; // Ok(123) -> 123
    let y: i32 = "24a".parse()?; // Err(_) -> returns immediately
    Ok(x + y)
}
```

**Example 3** (Ch. 8, "Destructuring assignments"): Swapping values:
```rust
let (mut a, mut b) = (0, 1);
(b, a) = (a, b);  // swap via destructuring assignment
// Desugars to: { let (_a, _b) = (a, b); b = _a; a = _b; }
```

**Example 4** (Ch. 8, "Numeric cast"): Saturation semantics for float-to-int:
```rust
assert_eq!(42.9f32 as i32, 42);           // rounds toward zero
assert_eq!(f32::NAN as i32, 0);            // NaN -> 0
assert_eq!(f32::INFINITY as i32, i32::MAX); // saturates to max
assert_eq!(-42.9f32 as i32, -42);          // rounds toward zero
```

# Relationships

## Builds Upon
- **rust-statements-and-expressions** -- operators are a subcategory of expressions; place/value context determines borrow vs. dereference behavior

## Enables
- None explicitly

## Related
- **rust-patterns** -- patterns appear in destructuring assignment and in `match`/`if let` which often interact with operators

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Using `&` to take a reference to a packed struct field, causing undefined behavior from an unaligned reference.
  **Correction**: Use `&raw const field` or `&raw mut field` to create a raw pointer instead, then use `read_unaligned()` to access the value safely.

- **Error**: Assuming integer overflow wraps in debug mode.
  **Correction**: Integer overflow panics in debug mode. Use `wrapping_add()`, `checked_add()`, `saturating_add()`, or the `Wrapping<T>` type for explicit overflow handling.

- **Error**: Chaining comparison operators like `a < b < c` (as in Python).
  **Correction**: Rust comparison operators do not chain and require parentheses when combined. Write `a < b && b < c` instead.

# Common Confusions

- **Confusion**: Thinking `&&` and `||` are the same as `&` and `|` on `bool`.
  **Clarification**: `&&` and `||` are lazy (short-circuit): the right operand is only evaluated if needed. `&` and `|` on `bool` evaluate both operands and are overloadable traits. Use `&&`/`||` for control flow; `&`/`|` when you need both sides evaluated.

- **Confusion**: Thinking `as` casts are always safe and lossless.
  **Clarification**: `as` casts can truncate integers (e.g., `1234u16 as u8` gives `210`), and float-to-int casts round and saturate. For safe conversions, prefer `From`/`Into` (infallible widening) or `TryFrom`/`TryInto` (fallible narrowing).

- **Confusion**: Expecting `?` to work in `main()` or non-returning functions.
  **Clarification**: The `?` operator requires the enclosing function to return a compatible type (`Result`, `Option`, or `ControlFlow`). `main()` can return `Result<(), E>` to use `?`, but ordinary functions returning `()` cannot.

# Source Reference

Chapter 8 of The Rust Reference: "Operator expressions" section (lines 1559-2828). Covers borrow and raw borrow operators, dereference, try propagation (`?`), negation, arithmetic and logical binary operators, comparison operators, lazy boolean operators, type cast expressions (`as`) with full numeric cast semantics, assignment and destructuring assignment, and compound assignment expressions.

# Verification Notes

- Definition source: Directly from the "Operator expressions" section of Chapter 8 of The Rust Reference
- Key Properties: All derived from explicit rule identifiers (r[expr.operator.int-overflow], r[expr.try], r[expr.operator.borrow], r[expr.as.numeric], r[expr.assign], r[expr.compound-assign])
- Confidence rationale: HIGH -- authoritative language reference with precise semantics and explicit edge cases
- Uncertainties: The `Try` trait (r[expr.try.intro]) is noted as currently unstable; its precise API may change
- Cross-reference status: rust-statements-and-expressions and rust-patterns are companion cards in this extraction set
