---
concept: Constant Evaluation
slug: rust-constant-evaluation
category: type-system
subcategory: const
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Constant Evaluation"
chapter_number: 18
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "const evaluation"
  - "const expressions"
  - "const context"
  - "const fn"
  - "compile-time evaluation"
  - "constant expressions"
prerequisites: []
extends: []
related:
  - rust-unsafety-reference
contrasts_with: []
answers_questions:
  - "What expressions can be evaluated at compile time in Rust?"
  - "What are all the const contexts where expressions must be constant?"
  - "What is a const function and what restrictions does it have?"
  - "What are the rules for borrows in const contexts?"
  - "When are constant expressions guaranteed vs. optionally evaluated at compile time?"
  - "What happens with overflow and out-of-bounds in const vs. runtime contexts?"
---

# Quick Definition

Constant evaluation is the process of computing expression results during compilation. Only a subset of expressions qualifies as constant expressions. Expressions in const contexts are always evaluated at compile time; outside const contexts, constant expressions may or may not be evaluated at compile time. Const functions extend compile-time evaluation to function calls.

# Core Definition

**Constant expressions** are expressions that can be evaluated at compile time. They must not cause `Drop::drop` calls and include: literals, const parameters, paths to functions and constants (no recursive definitions), paths to statics (with restrictions), tuple/array/struct expressions, block expressions (including `unsafe` and `const` blocks with let/assignment/expression statements), field expressions, array/slice indexing (with `usize` index), range expressions, closures not capturing environment variables, built-in arithmetic/logical/comparison/lazy boolean operators on integer/float/bool/char, most forms of borrows (with restrictions), dereference expressions, grouped expressions, casts (except pointer-to-address and fn-pointer-to-address), calls to const functions, `loop`/`while`/`if`/`match` expressions.

**Const contexts** (where expressions *must* be constant):
- Array type length expressions (`[T; N]`)
- Array repeat length expressions (`[expr; N]`)
- Initializers of constants, statics, and enum discriminants
- Const generic arguments
- Const blocks (`const { ... }`)

**Static path restrictions** in constant expressions:
- Writes to `static` items are never allowed in const evaluation
- Reads from `extern` statics are never allowed
- Outside `static` initializers, reads from mutable statics (`static mut` or statics with interior mutability) are not allowed

**Borrow restrictions**: Shared borrows of interior-mutable data and mutable borrows are only allowed when the borrowed place expression is *transient* (local variable or non-extended temporary), *indirect* (through a dereference), or *static* (a `static` item). Borrows whose temporary scope would be extended to the end of the program are restricted: mutable borrows and shared borrows of interior-mutable values are rejected.

# Prerequisites

Understanding of Rust expressions, the type system, and the distinction between compile-time and runtime evaluation.

# Key Properties

1. Expressions in const contexts are always evaluated at compile time; outside const contexts, constant expressions may optionally be evaluated at compile time
2. Out-of-bounds array indexing and overflow in const contexts are compile-time errors; outside const contexts, they are warnings but will likely panic at runtime
3. Constant expressions must not cause `Drop::drop` calls
4. Static reads in const expressions: writes never allowed, `extern` reads never allowed, mutable/interior-mutable static reads only allowed within that static's own initializer
5. These restrictions on statics are checked only when evaluated, not syntactically -- code paths that are never executed may contain such accesses
6. Array length expressions and const generic arguments are restricted to either a single const generic parameter or an expression that does not reference any generic parameters
7. Const functions are interpreted by the compiler at compile time targeting the compilation target, not the host (e.g., `usize` is 32 bits when compiling for a 32-bit target)
8. When called outside a const context, const functions behave identically to non-const functions
9. The body of a const function may only use constant expressions
10. Const functions are not allowed to be async
11. Pointer-to-address casts and function-pointer-to-address casts are not allowed in constant expressions

# Construction / Recognition

## Identifying Const Contexts

1. Look for `const` items (`const X: T = ...`), `static` items, enum discriminants, and const blocks
2. Array types use const contexts for their length: `[T; CONST_EXPR]`
3. Const generic arguments are const contexts: `Foo::<{CONST_EXPR}>`
4. The initializer expression in any of these must be a constant expression

## Writing Const Functions

1. Mark the function with `const fn`
2. Ensure the body uses only constant expressions
3. Avoid async, non-const function calls, and disallowed casts
4. Note: tuple struct and tuple enum variant constructors are implicitly const functions
5. Type parameters and return types must be compatible with const contexts

## Understanding Borrow Rules in Const

A borrow in a const context is allowed if the place expression is:
- **Transient**: a local variable or a temporary whose scope is contained within the const context
- **Indirect**: accessed through a dereference expression
- **Static**: a `static` item

Rejected: mutable borrows or shared borrows of interior-mutable values whose temporary scope would be extended to the end of the program (lifetime extension).

# Context & Application

Constant evaluation powers Rust's compile-time computation capabilities, from simple array lengths and enum discriminants to complex const-generic type-level programming. The rules carefully balance expressiveness with safety: const evaluation must not have observable side effects (no I/O, no mutable global state access except within static initializers), and the interior-mutability restrictions on borrows prevent creating compile-time references to mutable state that would persist to runtime.

The distinction between "must evaluate" (const context) and "may evaluate" (constant expression outside const context) is important for error handling: const context errors are hard compile errors, while the same errors outside const contexts may only be warnings that become runtime panics.

# Examples

**Example 1** (Const function and const context):
```rust
const fn square(x: i32) -> i32 { x * x }

const VALUE: i32 = square(12); // Const context: evaluated at compile time
let runtime_val = square(5);    // Not const context: may be evaluated at either time
```

**Example 2** (Borrow rules in const -- transient place is allowed):
```rust
const C: () = { let mut x = 0; _ = &mut x; }; // OK: x is local (transient)
const D: () = { _ = &mut 0u8; };               // OK: temporary scope not extended
```

**Example 3** (Borrow rules in const -- lifetime-extended temporary is rejected):
```rust
// ERROR: mutable borrow of lifetime-extended temporary
// const C: &[u8] = &mut [];

// But this works because the temporary is promoted, not lifetime-extended:
const C: &[u8] = { let x: &mut [u8] = &mut []; x }; // OK
```

**Example 4** (Static access restrictions):
```rust
use core::sync::atomic::AtomicU8;
// Shared borrow of interior-mutable static is OK (not a temporary):
const C: &AtomicU8 = {
    static S: AtomicU8 = AtomicU8::new(0); &S // OK
};
```

# Relationships

## Builds Upon
(none -- this defines the const evaluation model)

## Enables
- Compile-time computation, const generics, and type-level programming
- Static initialization and array length computation

## Related
- **rust-unsafety-reference** -- const contexts have additional provenance-related validity requirements for pointer/integer values (defined in the UB chapter)

## Contrasts With
(none)

# Common Errors

- **Error**: Attempting to read from a `static mut` or interior-mutable static within a `const` item's initializer.
  **Correction**: Only a `static` item's own initializer may read from mutable statics. Use const items, const fn parameters, or const generics to pass values into const evaluation.

- **Error**: Using a pointer-to-address cast in a const expression.
  **Correction**: Pointer-to-address and function-pointer-to-address casts are explicitly excluded from constant expressions. Use other approaches (e.g., const fn returning the address) or restructure to avoid the cast.

- **Error**: Creating a const reference to an `AtomicU8::new(0)` temporary with extended lifetime.
  **Correction**: `const C: &AtomicU8 = &AtomicU8::new(0)` is rejected because the borrow of an interior-mutable temporary would be lifetime-extended. Instead, use a `static` item: `const C: &AtomicU8 = { static S: AtomicU8 = AtomicU8::new(0); &S };`.

# Common Confusions

- **Confusion**: Assuming constant expressions outside const contexts are always evaluated at compile time.
  **Clarification**: Only expressions in const contexts (const/static initializers, array lengths, const generic args, const blocks) are guaranteed to be evaluated at compile time. Outside these contexts, constant expressions *may* be evaluated at compile time but this is not guaranteed.

- **Confusion**: Thinking const functions cannot use `unsafe` blocks.
  **Clarification**: `unsafe` blocks are listed as valid in constant expressions. Const functions can use unsafe operations (e.g., `UnsafeCell::get()`, raw pointer dereferences) within unsafe blocks, though the same safety obligations apply.

- **Confusion**: Expecting `&mut []` in tail position of a const to work because empty arrays are promoted.
  **Clarification**: `const C: &[u8] = &mut [];` fails because the borrow is in tail position, triggering temporary lifetime extension (which rejects mutable borrows). Moving the borrow to a non-tail position avoids lifetime extension: `const C: &[u8] = { let x: &mut [u8] = &mut []; x };`.

# Source Reference

Chapter 18 (Constant Evaluation, 343 lines): Constant expressions (full list of allowed expression forms), const contexts (5 types), static path restrictions, borrow restrictions with transient/indirect/static place classification, const functions (definition, interpretation rules, body restriction, async prohibition, type restrictions).

# Verification Notes

- Definition source: Direct extraction from Chapter 18 (343 lines), covering all sections
- Key Properties: Items 1-11 are direct from source with minimal synthesis
- Confidence rationale: HIGH -- the source provides explicit, well-structured rules with numerous examples
- Uncertainties: Type restrictions on const fn parameters/returns are marked as TODO in the source; the set of constant expressions may expand in future Rust versions
- Cross-reference status: Related slug references card in the reference extraction set
