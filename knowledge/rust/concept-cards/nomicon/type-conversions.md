---
concept: Type Conversions
slug: type-conversions
category: unsafe-rust
subcategory: type-system
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "Type Conversions"
chapter_number: 4
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "coercions"
  - "casts"
  - "transmute"
  - "as keyword"
  - "type coercion"
  - "mem::transmute"
  - "dot operator method lookup"
prerequisites:
  - nomicon-overview
  - data-layout-repr
extends: []
related:
  - subtyping-and-variance
  - ownership-and-lifetimes
contrasts_with: []
answers_questions:
  - "What type coercions does Rust perform implicitly?"
  - "How does the dot operator resolve method calls?"
  - "What can you do with the as keyword for casts?"
  - "When is transmute appropriate and what are the dangers?"
  - "What is the difference between coercions, casts, and transmute?"
  - "Why is transmuting &T to &mut T always UB?"
---

# Quick Definition

Rust provides four levels of type conversion with increasing power and danger: implicit coercions (weakening types, mostly harmless), the dot operator (auto-ref, auto-deref, and coercion for method calls), explicit casts with `as` (infallible at runtime but potentially lossy), and `mem::transmute` (raw bit reinterpretation with almost no guardrails).

# Core Definition

**Coercions** are implicit type changes that weaken types, largely focused on pointers and lifetimes. They "mostly exist to make Rust 'just work' in more cases, and are largely harmless." Important: coercions are NOT performed when matching traits -- if `T` coerces to `U` and there's an `impl Trait for U`, that doesn't count as `impl Trait for T`. (Ch. 4, "Coercions")

**The dot operator** performs extensive type manipulation for method calls: it tries by-value calls, then auto-referencing (`&T`, `&mut T`), then auto-dereferencing (via `Deref`), then unsizing (e.g., `[i32; 2]` to `[i32]`). This creates subtle behavior: `value.clone()` may return `T` or `&T` depending on whether `T: Clone` is satisfied. The lookup chain for `Rc<Box<[T; 3]>>[0]` goes: `Rc` -> deref -> `Box` -> deref -> `[T; 3]` -> unsize -> `[T]` which implements `Index`. (Ch. 4, "The Dot Operator")

**Casts** (`as`) are a superset of coercions: every coercion can be written as a cast, but casts also permit conversions between numeric types and raw pointers. Casts are infallible at runtime -- they never panic, but may silently produce surprising values (e.g., truncation). Casts are not `unsafe` because they can't violate memory safety on their own; converting an integer to a raw pointer is safe, but dereferencing it is already `unsafe`. Casting is **not transitive**: `e as U1 as U2` being valid does not imply `e as U2` is valid. Raw slice casts don't adjust length: `*const [u16] as *const [u8]` creates a slice covering only half the memory. (Ch. 4, "Casts")

**Transmute** (`mem::transmute<T, U>`) reinterprets a value of type `T` as type `U`, requiring only that they have the same size. It is "the most horribly unsafe thing you can do in Rust." Key dangers: creating invalid values (e.g., transmuting `3` to `bool`), transmuting `&T` to `&mut T` is **always UB** ("No you can't do it. No you're not special."), transmuting to a reference without an explicit lifetime produces an unbounded lifetime, and transmuting between types requires knowing their exact layouts (which `repr(Rust)` doesn't guarantee). `mem::transmute_copy<T, U>` is even more dangerous -- it copies `size_of::<U>` bytes from a `&T` without even checking size equality. (Ch. 4, "Transmutes")

# Prerequisites

- **nomicon-overview** -- understanding the safe/unsafe boundary and what constitutes UB is essential for reasoning about transmute
- **data-layout-repr** -- repr annotations determine when transmute is sound; `repr(C)` and `repr(transparent)` provide layout guarantees

# Key Properties

1. Coercions are implicit, weakening, and largely harmless; they don't apply when matching trait implementations
2. The dot operator performs: by-value call -> auto-ref (`&T`, `&mut T`) -> auto-deref (`Deref`) -> unsizing
3. Auto-ref in the dot operator can cause subtle behavior: `value.clone()` may clone the value or clone the reference, depending on trait bounds
4. Casts with `as` are a superset of coercions; they are infallible at runtime but may truncate or produce unexpected values
5. Casts are not `unsafe` -- they can't violate memory safety on their own
6. Casting is not transitive: `e as U1 as U2` valid does not imply `e as U2` valid
7. Raw slice casts don't adjust length metadata
8. `transmute` requires `T` and `U` to have the same size; it has an overloaded return type
9. Transmuting `&T` to `&mut T` is always, unconditionally UB
10. Transmuting to a reference without an explicit lifetime produces an unbounded lifetime
11. Transmuting between `repr(Rust)` types is unsound because layout is not guaranteed (even `Vec<i32>` and `Vec<u32>` may differ)
12. `transmute_copy` is even more dangerous -- no size equality check, UB if `U` is larger than `T`

# Construction / Recognition

## To Choose the Right Conversion

1. If the type weakening is automatic (e.g., `&mut T` to `&T`, longer lifetime to shorter): rely on coercions
2. If calling a method on a wrapped/referenced type: rely on the dot operator's auto-deref chain
3. If converting between numeric types or to/from raw pointers: use `as` casts
4. If reinterpreting bits with same-sized types and known layout: consider `transmute` (last resort)
5. Always prefer `From`/`Into` for safe conversions before reaching for `as` or `transmute`

## To Use Transmute Safely

1. Ensure both types have the same size
2. Ensure the target type's layout is defined (`repr(C)` or `repr(transparent)`)
3. Ensure the bit pattern represents a valid value of the target type
4. Never transmute `&T` to `&mut T`
5. When transmuting to a reference, provide an explicit lifetime bound
6. Consider alternatives: raw pointer casts, `union`s, or `from_raw_parts`

# Context & Application

The Nomicon presents type conversions as a spectrum from safe and implicit (coercions) to powerful and perilous (transmute). This ordering matters for unsafe code design: prefer the weakest conversion that works. Coercions handle most day-to-day cases invisibly. The dot operator's complex lookup chain is why Rust feels ergonomic with smart pointers -- you can call methods through `Rc<Box<Vec<T>>>` without manual dereferencing.

Transmute is described in apocalyptic terms because it bypasses nearly all type-system guarantees. The source's emphasis that transmuting `&T` to `&mut T` is "always Undefined Behavior" reflects a common temptation in unsafe code: developers see a shared reference they "know" is unique and try to cast it to mutable. The Rust optimizer assumes shared references don't change, and transmutation violates this assumption at a fundamental level.

The dot operator's auto-ref behavior has practical implications for generic code: the `Container<T>` example shows that `#[derive(Clone)]` generates `impl<T: Clone> Clone for Container<T>`, so calling `.clone()` on `&Container<T>` where `T: !Clone` auto-refs to clone the reference (producing `&Container<T>`) rather than the value.

# Examples

**Example 1** (Ch. 4, "Coercions"): Coercions don't apply for trait matching:
```rust
trait Trait {}
fn foo<X: Trait>(t: X) {}
impl<'a> Trait for &'a i32 {}
let t: &mut i32 = &mut 0;
foo(t); // ERROR: Trait not implemented for &mut i32 (even though &mut i32 coerces to &i32)
```

**Example 2** (Ch. 4, "The Dot Operator"): Auto-ref changes clone semantics:
```rust
#[derive(Clone)]
struct Container<T>(Arc<T>);
fn clone_containers<T>(foo: &Container<i32>, bar: &Container<T>) {
    let foo_cloned = foo.clone();   // Container<i32> (by-value, since i32: Clone)
    let bar_cloned = bar.clone();   // &Container<T> (auto-ref, since T: !Clone)
}
```

**Example 3** (Ch. 4, "The Dot Operator"): Method lookup chain for `Rc<Box<[T; 3]>>[0]`:
`Rc<Box<[T; 3]>>` -> deref -> `Box<[T; 3]>` -> deref -> `[T; 3]` -> unsize -> `[T]` which implements `Index`.

**Example 4** (Ch. 4, "Transmutes"): The three absolute rules of transmute:
- Never transmute `3` to `bool` (invalid state)
- Never transmute `&T` to `&mut T` (always UB -- the optimizer assumes `&T` is immutable)
- Transmuting to a reference without a lifetime produces an unbounded lifetime

# Relationships

## Builds Upon
- **nomicon-overview** -- understanding UB and the safe/unsafe boundary
- **data-layout-repr** -- repr guarantees determine when transmute is sound

## Enables
(none directly -- type conversions are a foundational unsafe operation)

## Related
- **subtyping-and-variance** -- lifetime coercions are a form of subtyping
- **ownership-and-lifetimes** -- unbounded lifetimes from transmute connect to lifetime safety

## Contrasts With
(none)

# Common Errors

- **Error**: Transmuting between two `repr(Rust)` types, assuming they have the same layout because they have the same fields.
  **Correction**: `repr(Rust)` provides no layout guarantees across different types. Even `Vec<i32>` and `Vec<u32>` might have different field orderings. Use `repr(C)` or `repr(transparent)` types for transmutation.

- **Error**: Assuming cast transitivity -- that if `e as U1` and `U1 as U2` both work, then `e as U2` also works.
  **Correction**: Casting is not transitive. Each cast is checked independently; an intermediate type may be necessary.

- **Error**: Casting a raw slice pointer to a different element type and assuming the length adjusts.
  **Correction**: `*const [u16] as *const [u8]` keeps the same length metadata, meaning the resulting slice covers only half the original memory. Adjust length manually.

# Common Confusions

- **Confusion**: Thinking transmuting `&T` to `&mut T` is safe if you "know" no other references exist.
  **Clarification**: This is always, unconditionally UB regardless of aliasing state. The Rust optimizer makes assumptions about shared reference immutability at compile time, and transmutation violates these assumptions even if no actual aliasing occurs at runtime.

- **Confusion**: Believing casts are unsafe operations.
  **Clarification**: Casts (`as`) are not `unsafe` because they cannot violate memory safety on their own. Creating a raw pointer from an integer is safe; only dereferencing it is unsafe.

- **Confusion**: Thinking the dot operator simply dereferences pointers.
  **Clarification**: The dot operator performs a complex multi-step lookup: by-value, then auto-ref (`&` and `&mut`), then auto-deref (via `Deref` trait), then unsizing. At each step, it checks for matching method signatures.

# Source Reference

Chapter 4: Type Conversions -- Coercions (implicit weakening, trait matching limitation), The Dot Operator (auto-ref, auto-deref, unsizing, method lookup algorithm, Clone example), Casts (superset of coercions, safety, non-transitivity, raw slice length), Transmutes (mem::transmute, mem::transmute_copy, UB catalog, &-to-&mut prohibition, unbounded lifetimes, layout requirements).

# Verification Notes

- Definition source: Direct synthesis from Ch. 4 (317 lines), covering all four sections
- Key Properties: All items directly stated in the source with code examples; the transmute rules are emphatic and explicit
- Confidence rationale: HIGH -- each section provides clear rules with concrete examples and explicit warnings
- Uncertainties: None -- the source is definitive on the rules, especially the absolute prohibition on &-to-&mut transmutation
- Cross-reference status: All slugs reference cards in the nomicon extraction set
