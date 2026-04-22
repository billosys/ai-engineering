---
concept: Data Layout and repr
slug: data-layout-repr
category: unsafe-rust
subcategory: data-representation
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "Data Representation in Rust"
chapter_number: 2
pdf_page: null
section: "repr(Rust) / Alternative representations"
extraction_confidence: high
aliases:
  - "repr(C)"
  - "repr(Rust)"
  - "repr(transparent)"
  - "data layout"
  - "struct alignment"
  - "field reordering"
  - "null pointer optimization"
prerequisites:
  - nomicon-overview
extends: []
related:
  - exotic-types
  - type-conversions
contrasts_with: []
answers_questions:
  - "How does Rust lay out structs in memory by default?"
  - "When should I use repr(C) vs repr(Rust)?"
  - "What is repr(transparent) and when is it needed?"
  - "How does the null pointer optimization work?"
  - "What is repr(packed) and when should it be used?"
  - "How does repr(align) work?"
  - "Can Rust reorder struct fields?"
---

# Quick Definition

Rust's default data layout (`repr(Rust)`) allows the compiler to reorder and pad struct fields for optimization, with no guaranteed field ordering across different types. Alternative representations (`repr(C)`, `repr(transparent)`, `repr(u*)`, `repr(packed)`, `repr(align)`) give explicit control over layout for FFI, transmutation, and performance.

# Core Definition

All types have an alignment (always a power of 2, at least 1) and a size (always a multiple of alignment). Under `repr(Rust)`, composite types are aligned to the maximum of their fields' alignments, with padding inserted as needed, but **field ordering is not specified**. Two instances of the same type `A` have identical layout, but Rust does not guarantee `A` and `B` have the same layout even with identical fields. The compiler may reorder fields to minimize padding -- for example, different monomorphizations of `Foo<T, U>` may use different field orders to optimize space.

**`repr(C)`** follows C's layout rules: fields are in declaration order with C-compatible alignment and padding. This is essential for FFI and for code that reinterprets memory. **`repr(transparent)`** guarantees a struct or single-variant enum has the same layout and ABI as its single non-zero-sized field, enabling safe transmutation between the wrapper and the inner type. **`repr(u*)`/`repr(i*)`** specify the discriminant size for fieldless enums. **`repr(packed)`** removes padding (minimum alignment of 1), and **`repr(align(n))`** forces minimum alignment of `n`.

Enums have a tag/discriminant plus a data field large enough for the largest variant. Rust performs the **null pointer optimization**: for an enum with one unit variant and one non-nullable pointer variant (e.g., `Option<&T>`), the tag is eliminated and null represents the unit variant, so `size_of::<Option<&T>>() == size_of::<&T>()`.

# Prerequisites

- **nomicon-overview** -- understanding the safe/unsafe boundary is needed to appreciate why layout control matters for unsafe code and FFI

# Key Properties

1. Alignment must be a power of 2 (at least 1); size must be a multiple of alignment
2. `repr(Rust)` allows field reordering and provides no cross-type layout guarantees
3. Two instances of the same type are guaranteed to have identical layout
4. `repr(C)` preserves declaration order, uses C-compatible alignment; essential for FFI
5. `repr(transparent)` can only apply to structs/enums with one non-ZST field; guarantees identical layout and ABI to that field
6. `repr(u*)`/`repr(i*)` set the discriminant size for fieldless enums; adding them to enums with fields suppresses null pointer optimization
7. Null pointer optimization eliminates the tag for `Option<&T>`, `Option<Box<T>>`, etc.
8. `repr(packed)` forces alignment to at most `n` (default 1); taking references to packed fields can cause UB
9. `repr(align(n))` forces alignment to at least `n`; incompatible with `repr(packed)`
10. `repr(packed)` and `repr(align)` are modifiers on `repr(C)` or `repr(Rust)`
11. ZSTs remain zero-sized under `repr(C)`, which differs from C++ (empty types consume 1 byte in C++)
12. DST pointers (wide pointers) and tuples are never FFI-safe

# Construction / Recognition

## To Choose a repr

1. Use `repr(Rust)` (default) when layout doesn't matter and you want the compiler to optimize
2. Use `repr(C)` when passing types across FFI boundaries or when you need deterministic layout for reinterpretation
3. Use `repr(transparent)` when creating newtypes that must be transmutable to/from their inner type
4. Use `repr(u8)`, `repr(u16)`, etc., when you need explicit discriminant sizes for fieldless enums (especially for FFI)
5. Use `repr(packed)` only with extreme care and typically only as `repr(C, packed)` for FFI matching
6. Use `repr(align(n))` for performance (e.g., cache-line alignment for concurrent code)

## To Verify Layout Properties

1. Use `std::mem::size_of::<T>()` and `std::mem::align_of::<T>()` to check concrete sizes
2. For `repr(C)` types, manually calculate padding following C rules
3. For `repr(transparent)`, confirm exactly one non-ZST field exists

# Context & Application

Data layout matters critically in three contexts: FFI (where Rust must match C/C++ struct layouts exactly), performance optimization (where alignment and padding affect cache behavior), and unsafe code (where pointer arithmetic and transmutation require known layouts). The `repr(C)` attribute is described as "the most important repr" because C is "the lingua-franca of the programming world" for cross-language interop. The source recommends `rust-bindgen` and `cbindgen` for managing FFI boundaries.

The null pointer optimization is a significant space saving that applies to many standard library types (`Box<T>`, `Vec<T>`, `String`, `&T`, `&mut T`). Adding an explicit `repr(u*)`, `repr(i*)`, or `repr(C)` to an enum with fields suppresses this optimization -- a design choice worth understanding when wrapping pointer types.

# Examples

**Example 1** (Ch. 2, "repr(Rust)"): A struct `A { a: u8, b: u32, c: u16 }` with 32-bit alignment might be laid out with padding as `{ a: u8, _pad1: [u8; 3], b: u32, c: u16, _pad2: [u8; 2] }` -- or the compiler might reorder to `{ b: u32, c: u16, a: u8, _pad: u8 }` to save space.

**Example 2** (Ch. 2, "repr(Rust)"): Null pointer optimization means `size_of::<Option<&T>>() == size_of::<&T>()` -- null represents `None` with no additional discriminant.

**Example 3** (Ch. 2, "Alternative representations"): Adding `#[repr(u8)]` to an enum with fields suppresses the null pointer optimization:
```rust
enum MyOption<T> { Some(T), None }         // size 8 for &u16
#[repr(u8)]
enum MyReprOption<T> { Some(T), None }     // size 16 for &u16
```

# Relationships

## Builds Upon
- **nomicon-overview** -- layout control is one reason developers enter unsafe Rust

## Enables
- **type-conversions** -- transmute requires understanding layouts; `repr(C)` and `repr(transparent)` make transmutation sound
- **exotic-types** -- ZSTs, DSTs, and empty types have special layout considerations

## Related
- **exotic-types** -- zero-sized types, dynamically sized types, and empty types are special layout cases

## Contrasts With
(none)

# Common Errors

- **Error**: Assuming two structs with identical fields have the same layout under `repr(Rust)`.
  **Correction**: Only `repr(C)` guarantees layout based on field declaration order. Under `repr(Rust)`, even two structs with the same fields may have different padding and ordering.

- **Error**: Taking a reference to a field in a `repr(packed)` struct.
  **Correction**: References to packed fields may be unaligned, which is UB. This is a lint that will become a hard error. Use reads/copies instead of references.

- **Error**: Passing `repr(Rust)` types across FFI boundaries.
  **Correction**: Always use `repr(C)` for types that cross FFI boundaries. Rust's default layout provides no stability guarantees that other languages can rely on.

# Common Confusions

- **Confusion**: Thinking `repr(C)` means "use a C compiler's exact layout."
  **Clarification**: `repr(C)` means "follow C's layout rules," but C's enum representation is implementation-defined. For fieldless enums, `repr(C)` uses the target platform's C ABI default, which may not match code compiled with specific C compiler flags.

- **Confusion**: Believing `repr(transparent)` can be used on any struct.
  **Clarification**: `repr(transparent)` requires exactly one non-zero-sized field (additional ZST fields are allowed). The layout guarantee is that the struct has the same ABI as that one field.

- **Confusion**: Thinking that setting an enum to an integer value without a corresponding variant is valid with `repr(C)`.
  **Clarification**: Even with `repr(C)` or `repr(u*)`, constructing an enum value that doesn't match a defined variant is undefined behavior in Rust, despite being permitted in C/C++.

# Source Reference

Chapter 2: Data Representation in Rust -- repr(Rust) (alignment, padding, field reordering, enum layout, null pointer optimization), Exotically Sized Types (DSTs, ZSTs, Empty Types, Extern Types), Alternative Representations (repr(C), repr(transparent), repr(u*/i*), repr(packed), repr(align)).

# Verification Notes

- Definition source: Direct synthesis from Ch. 2 (542 lines), covering three major sections
- Key Properties: All items directly stated or demonstrated with code examples in the source
- Confidence rationale: HIGH -- the source provides explicit rules, code examples, and size assertions for all repr annotations
- Uncertainties: The source notes that enum layout optimization algorithms may become more elaborate; extern types are stuck in limbo
- Cross-reference status: All slugs reference cards in the nomicon extraction set
