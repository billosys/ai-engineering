---
concept: Type Coercions and Destructors
slug: type-coercions-and-destructors
category: type-system
subcategory: coercions-and-drop
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Type System"
chapter_number: 10
pdf_page: null
section: "Type Coercions, Destructors, Trait and Lifetime Bounds, Lifetime Elision, Divergence"
extraction_confidence: high
aliases:
  - "type coercion"
  - "coercion sites"
  - "unsized coercion"
  - "destructors"
  - "drop scopes"
  - "drop order"
  - "lifetime elision"
  - "trait bounds"
  - "higher-ranked trait bounds"
  - "HRTB"
  - "diverging expressions"
prerequisites:
  - rust-type-system
extends:
  - rust-type-system
related:
  - special-types-and-traits
  - rust-memory-model-and-panic
contrasts_with: []
answers_questions:
  - "What implicit type coercions does Rust perform?"
  - "Where can coercions occur (coercion sites)?"
  - "What are unsized coercions?"
  - "In what order are destructors run?"
  - "What are drop scopes?"
  - "How does temporary lifetime extension work?"
  - "What are the lifetime elision rules?"
  - "How do trait bounds and lifetime bounds work?"
  - "What are higher-ranked trait bounds (HRTBs)?"
  - "What is a diverging expression?"
  - "What is the never type fallback?"
---

# Quick Definition

Type coercions are implicit, automatic type conversions at specific program locations (coercion sites). Destructors run when initialized variables or temporaries go out of scope, following a deterministic order defined by drop scopes. Together with trait/lifetime bounds, lifetime elision, and divergence rules, these mechanisms form the operational backbone of Rust's type system.

# Core Definition

**Type Coercions**: "Type coercions are implicit operations that change the type of a value. They happen automatically at specific locations and are highly restricted in what types actually coerce." (Ch. 10, "Type coercions"). Coercions can only occur at coercion sites: `let` statements with explicit types, `static`/`const` declarations, function arguments, struct/union/enum field instantiations, function return values, and assignment operands.

The allowed coercion types include: subtype coercion (reflexive), transitive coercion, `&mut T` to `&T`, `*mut T` to `*const T`, references to raw pointers, deref coercions (via `Deref`/`DerefMut` traits), unsized coercions, function items to `fn` pointers, non-capturing closures to `fn` pointers, and `!` to any `T`.

**Unsized coercions** convert sized types to unsized: `[T; n]` to `[T]`, `T` to `dyn U` (when `T: U + Sized`), and `dyn T` to `dyn U` (trait upcasting, when `U` is a supertrait of `T`). These use the `Unsize` and `CoerceUnsized` traits internally.

**Least Upper Bound (LUB) coercions** find a common type for `if`/`match` branches, array elements, and closure/function returns. The target type starts as the first branch's type and is iteratively widened.

**Destructors**: "When an initialized variable or temporary goes out of scope, its destructor is run or it is dropped." (Ch. 10, "Destructors"). The destructor of type `T` consists of: (1) calling `<T as Drop>::drop` if `T: Drop`, then (2) recursively dropping all fields. Struct fields drop in declaration order. Enum variant fields drop in declaration order. Tuple fields drop in order. Array/slice elements drop first-to-last. Closure move-captures drop in unspecified order.

**Drop scopes** define when variables are dropped. Variables within a scope drop in reverse order of declaration. Scopes exist for the entire function, each statement, each expression, each block, and each match arm. Drop scopes nest: when multiple scopes are left at once, variables drop from inside outwards.

**Temporary lifetime extension**: In `let` statements, if a pattern binds by reference (e.g., `let ref x = ...` or `let x = &expr`), the temporary's scope is extended to the enclosing block rather than being dropped at the semicolon. This applies recursively to borrow operands, tuple/struct/array constructors, blocks, `if`/`else`, and `match` arms when they are "extending expressions."

**Lifetime elision** allows omitting lifetime annotations in common patterns: each elided parameter lifetime becomes distinct; if there is exactly one input lifetime, it applies to all output lifetimes; in methods, the receiver lifetime (`&self`/`&mut self`) applies to all output lifetimes. Default trait object lifetimes are `'static` when contained in `Box<dyn Trait>`, or match the container's constraint otherwise.

**Trait and lifetime bounds** restrict generic parameters: `T: Trait` requires the type to implement `Trait`; `'a: 'b` means `'a` outlives `'b`; `T: 'a` means all lifetime parameters of `T` outlive `'a`. Higher-ranked trait bounds (`for<'a> F: Fn(&'a i32)`) specify bounds true for all lifetimes. Implied lifetime bounds are inferred from function signatures (e.g., `&'a T` implies `T: 'a`).

**Divergence**: A diverging expression never completes normal execution. Any expression of type `!` diverges. If a type is only unified with diverging expressions, it is inferred as `!` (Edition 2024+; previously `()`).

# Prerequisites

- **rust-type-system** -- coercions and destructors operate on the type system's foundations

# Key Properties

1. Coercions only occur at explicit coercion sites -- they do not happen in arbitrary positions
2. `&mut T` coerces to `&T` but not vice versa; `*mut T` coerces to `*const T`
3. Deref coercions chain: `&T` to `&U` when `T: Deref<Target=U>`
4. Function items and non-capturing closures coerce to function pointers
5. `!` (never type) coerces to any type
6. Trait upcasting: `dyn T` coerces to `dyn U` when `U` is a supertrait of `T`
7. Destructors run `Drop::drop` first, then recursively drop all fields
8. Struct fields drop in declaration order; variables drop in reverse declaration order
9. Closure move-captures have unspecified drop order
10. Temporary lifetime extension activates when `let` bindings use reference patterns or the initializer is a borrow of an extending expression
11. Lifetime elision: single input lifetime applies to all outputs; method receiver lifetime applies to all outputs
12. `?Sized` relaxes the implicit `Sized` bound on type parameters
13. Higher-ranked trait bounds (`for<'a>`) specify bounds true for all lifetimes
14. Implied lifetime bounds are automatically inferred from type structure (e.g., `&'a T` implies `T: 'a`)

# Construction / Recognition

## Coercion Sites (Where Coercions Happen)
1. `let` statements with explicit type: `let _: &i8 = &mut 42;`
2. Function arguments: `fn bar(_: &i8) { } bar(&mut 42);`
3. Struct/union/enum field instantiation
4. Function return values (final expression or `return`)
5. Assignment operands
6. Propagating expressions: array literals, tuples, parenthesized expressions, blocks

## Drop Scope Nesting (Outside-In)
1. Entire function (outermost)
2. Function body block
3. Statement scope
4. Expression scope (innermost)

When leaving multiple scopes, drops proceed inside-out.

## Lifetime Elision Rules
1. Each elided input lifetime becomes a distinct parameter
2. If exactly one input lifetime, it is assigned to all elided outputs
3. In methods, `&self`/`&mut self` lifetime is assigned to all elided outputs

# Context & Application

- **Typical contexts**: Understanding why `&mut T` works where `&T` is expected; why temporaries live long enough in `let` bindings; designing APIs with proper lifetime elision.
- **Common applications**: FFI boundary design (function pointers), iterator chains (deref coercions), RAII resource cleanup (drop ordering), generic APIs (trait bounds).
- **Suppressing destructors**: `core::mem::forget` prevents destruction; `ManuallyDrop` wraps a value to prevent automatic dropping. Both are safe to use. Process termination via `abort` or `exit` skips all destructors.

# Examples

**Example 1** -- Coercion sites (Ch. 10, "Type coercions"):
```rust
let _: &i8 = &mut 42;         // let statement coercion
fn bar(_: &i8) { }
bar(&mut 42);                   // argument coercion
struct Foo<'a> { x: &'a i8 }
Foo { x: &mut 42 };            // field instantiation coercion
```

**Example 2** -- Drop order (Ch. 10, "Destructors"):
```rust
struct PrintOnDrop(&'static str);
impl Drop for PrintOnDrop {
    fn drop(&mut self) { println!("{}", self.0); }
}
let mut overwritten = PrintOnDrop("drops when overwritten");
overwritten = PrintOnDrop("drops when scope ends");
// Assignment drops the old value immediately
```

**Example 3** -- Temporary lifetime extension (Ch. 10, "Destructors"):
```rust
let x = &mut 0;
// The temporary for `0` lives to the end of the block,
// not just the semicolon, because of lifetime extension.
println!("{}", x);
```

**Example 4** -- Lifetime elision (Ch. 10, "Lifetime elision"):
```rust
fn substr(s: &str, until: usize) -> &str;        // elided
fn substr<'a>(s: &'a str, until: usize) -> &'a str; // expanded (equivalent)

fn get_mut(&mut self) -> &mut dyn T;              // elided
fn get_mut<'a>(&'a mut self) -> &'a mut dyn T;    // expanded (equivalent)
```

**Example 5** -- Higher-ranked trait bounds (Ch. 10, "Trait and lifetime bounds"):
```rust
fn call_on_ref_zero<F>(f: F) where for<'a> F: Fn(&'a i32) {
    let zero = 0;
    f(&zero);
}
```

# Relationships

## Builds Upon
- **rust-type-system** -- coercions transform between types defined by the type system

## Enables
- **rust-memory-model-and-panic** -- destructors interact with unwinding during panic

## Related
- **special-types-and-traits** -- `Drop`, `Deref`, `DerefMut`, `Copy`, `Sized`, `Unsize`, `CoerceUnsized` are central to coercions and destructors

## Contrasts With
No direct contrasts within scope.

# Common Errors

- **Error**: Expecting coercions to happen in non-coercion sites (e.g., in generic type inference or pattern matching).
  **Correction**: Coercions only happen at specific sites. Use explicit `as` casts or turbofish syntax when coercion sites are not available.

- **Error**: Relying on a specific drop order for closure captures.
  **Correction**: "The variables that a closure captures by move are dropped in an unspecified order." Use explicit `drop()` calls or restructure code if drop order matters.

- **Error**: Assuming temporaries in function arguments live until the end of the statement.
  **Correction**: Temporary lifetime extension only applies to `let` bindings with reference patterns or extending expressions, not to function argument positions.

# Common Confusions

- **Confusion**: Deref coercion and the `as` cast operator are the same thing.
  **Clarification**: Deref coercion is implicit and uses the `Deref`/`DerefMut` traits; `as` is an explicit cast operator that supports a broader but different set of conversions (e.g., numeric casts, pointer casts).

- **Confusion**: `for<'a> Fn(&'a i32)` and `Fn(&'static i32)` are equivalent.
  **Clarification**: The former accepts any lifetime; the latter requires `'static`. `for<'a>` is a higher-ranked bound true for all lifetimes.

- **Confusion**: Assignment drops the new value, not the old one.
  **Clarification**: Assignment runs the destructor of the left-hand operand (the old value) before placing the new value.

# Source Reference

The Rust Reference, Chapter 10: Type Coercions, Destructors, Trait and Lifetime Bounds, Lifetime Elision, Divergence.

# Verification Notes

- Definition source: Direct from Ch. 10 of The Rust Reference
- Confidence rationale: High -- coercion rules, drop scopes, and lifetime elision are precisely documented
- Uncertainties: LUB coercion description is acknowledged as informal; temporary lifetime extension rules are noted as subject to change
- Cross-reference status: Related cards verified against planned card slugs
