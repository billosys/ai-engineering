---
concept: Exotic Types
slug: exotic-types
category: unsafe-rust
subcategory: data-representation
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "Data Representation in Rust"
chapter_number: 2
pdf_page: null
section: "Exotically Sized Types"
extraction_confidence: high
aliases:
  - "zero-sized types"
  - "ZSTs"
  - "dynamically sized types"
  - "DSTs"
  - "empty types"
  - "unsized types"
  - "wide pointers"
  - "fat pointers"
prerequisites:
  - nomicon-overview
  - data-layout-repr
extends: []
related:
  - ownership-and-lifetimes
  - drop-check-and-phantom-data
contrasts_with: []
answers_questions:
  - "What are zero-sized types and why do they matter?"
  - "What is a dynamically sized type (DST)?"
  - "What is a wide pointer / fat pointer?"
  - "How can you create an empty type in Rust?"
  - "Why shouldn't you model C's void* with *const Void?"
  - "How are ZSTs handled in generic code and allocators?"
  - "How do trait objects and slices differ as DSTs?"
---

# Quick Definition

Rust supports three categories of "exotic" types: Dynamically Sized Types (DSTs) that lack a compile-time-known size and exist only behind wide pointers, Zero-Sized Types (ZSTs) that occupy no space but enable powerful generic patterns, and Empty Types that cannot be instantiated and enable type-level unreachability.

# Core Definition

**Dynamically Sized Types (DSTs)** are types without a statically known size or alignment. They can only exist behind a pointer, which becomes a **wide pointer** (also called a fat pointer) carrying both the pointer and "completing" information. The two major DSTs are trait objects (`dyn MyTrait`), where the completing information is a vtable pointer, and slices (`[T]`, `str`), where the completing information is the element count. Structs can store a single DST as their last field, making the struct itself a DST. Custom DSTs are created through unsizing coercions from sized generic types (Ch. 2, "Exotically Sized Types").

**Zero-Sized Types (ZSTs)** occupy no space. Examples include unit structs (`struct Nothing;`), the empty tuple `()`, and zero-length arrays (`[u8; 0]`). In generic contexts, operations on ZSTs are reduced to no-ops: storing is meaningless, and loading can produce the value "from the aether." The canonical example is `Set<Key> = Map<Key, ()>`, where monomorphization eliminates all value-related overhead. Unsafe code must handle ZSTs carefully: pointer offsets are no-ops, and allocators typically require non-zero sizes (Ch. 2, "Zero Sized Types").

**Empty Types** cannot be instantiated at all. Declared as `enum Void {}` (no variants), they enable type-level unreachability -- e.g., `Result<T, Void>` communicates infallibility statically and is represented as just `T`. Raw pointers to empty types are valid to construct but dereferencing them is UB (Ch. 2, "Empty Types").

# Prerequisites

- **nomicon-overview** -- understanding the safe/unsafe boundary, especially for ZST and empty type pitfalls in unsafe code
- **data-layout-repr** -- alignment, size, and padding rules that exotic types modify or circumvent

# Key Properties

1. DSTs can only exist behind a pointer; that pointer becomes a "wide" pointer with extra metadata
2. Trait object pointers carry a vtable pointer; slice pointers carry an element count
3. A struct can contain exactly one DST, and only as its last field, making the struct itself a DST
4. Custom DSTs are created via unsizing coercions from `T: Sized` to `T: ?Sized`
5. ZSTs have size 0 and alignment 1 or greater; all operations that produce or store them become no-ops
6. Only one value exists for any ZST, so loads produce it "from the aether"
7. `Set<Key>` implemented as `Map<Key, ()>` eliminates all value overhead through monomorphization
8. References to ZSTs must still be non-null and suitably aligned
9. Loading/storing through a null pointer to a ZST is not UB (unlike other types)
10. Empty types (`enum Void {}`) have no valid values and can never be instantiated
11. `Result<T, Void>` can represent infallible operations and is laid out as just `T`
12. Do not model C's `void*` as `*const Void`; use `*const ()` instead to avoid UB risks

# Construction / Recognition

## To Create a DST

1. Use built-in DSTs: `dyn Trait`, `[T]`, or `str`
2. For custom DSTs: make a struct generic over `T: ?Sized` with `T` as the last field
3. Create instances via unsizing coercion from a sized type (e.g., `&MySuperSliceable<[u8; 8]>` to `&MySuperSliceable<[u8]>`)

## To Use ZSTs Effectively

1. Define as `struct Nothing;` or use `()` or `[T; 0]`
2. Use as type parameters to eliminate overhead (e.g., `HashMap<K, ()>` as a set)
3. In unsafe code: check for zero size before calling allocators, handle no-op pointer offsets

## To Use Empty Types

1. Declare as `enum Void {}` (no variants)
2. Use in `Result<T, Void>` to express infallibility
3. Match with `let Ok(val) = result;` -- the `Err` arm is irrefutable
4. Never try to create a value of the empty type, even in unsafe code

# Context & Application

DSTs are fundamental to Rust's abstraction mechanisms: trait objects enable runtime polymorphism and slices provide safe views into contiguous memory. The wide pointer mechanism is how Rust avoids garbage collection while supporting dynamic dispatch -- the metadata travels with the pointer rather than being stored in the object.

ZSTs demonstrate Rust's commitment to zero-cost abstractions. The `Map<Key, ()>` pattern means a `HashSet` built atop `HashMap` has literally zero overhead from the unused value type -- monomorphization eliminates all value-related code and allocation. This is impossible in most other languages, where the compiler cannot prove the zero-size optimization is valid.

Empty types are "even more marginal than ZSTs" but serve important roles in type-level programming. The source warns against using `*const Void` for C's `void*` because Rust lacks safety guards against instantiating empty types in unsafe code, and `&Void` is UB to construct. Instead, `*const ()` works as a safe alternative.

# Examples

**Example 1** (Ch. 2, "Dynamically Sized Types"): A struct with a DST as its last field:
```rust
struct MySuperSliceable<T: ?Sized> {
    info: u32,
    data: T,
}
// Create sized, then coerce to unsized:
let sized: MySuperSliceable<[u8; 8]> = MySuperSliceable { info: 17, data: [0; 8] };
let dynamic: &MySuperSliceable<[u8]> = &sized;
```

**Example 2** (Ch. 2, "Zero Sized Types"): ZSTs are used to implement sets from maps:
> "In Rust, we can just say that `Set<Key> = Map<Key, ()>`. Now Rust statically knows that every load and store is useless, and no allocation has any size."

**Example 3** (Ch. 2, "Empty Types"): An empty type for infallible results:
```rust
enum Void {}
let res: Result<u32, Void> = Ok(0);
let Ok(num) = res; // Err doesn't exist, so Ok is irrefutable
```

# Relationships

## Builds Upon
- **data-layout-repr** -- exotic types are special cases of Rust's layout system

## Enables
- **drop-check-and-phantom-data** -- PhantomData is a ZST used to simulate type/lifetime associations

## Related
- **ownership-and-lifetimes** -- DSTs interact with lifetime constraints through wide pointer metadata
- **type-conversions** -- unsizing coercions are a type conversion mechanism

## Contrasts With
(none)

# Common Errors

- **Error**: Calling allocators with zero-sized allocations when working with ZSTs in unsafe code.
  **Correction**: Check `size_of::<T>()` before allocating; allocators typically require non-zero sizes. Use special-case logic for ZSTs.

- **Error**: Using `*const Void` to model C's `void*` pointer.
  **Correction**: Use `*const ()` instead. Developers frequently convert raw pointers to references, and `&Void` is UB to construct since it requires a valid value of an uninhabitable type.

- **Error**: Attempting to dereference a raw pointer to an empty type.
  **Correction**: While raw pointers to empty types are valid to construct, dereferencing them is UB because no valid value of the type exists.

# Common Confusions

- **Confusion**: Thinking DSTs are laid out like normal types and can be stored on the stack.
  **Clarification**: DSTs have no compile-time-known size. They can only exist behind a pointer (reference, Box, etc.), which becomes a wide pointer carrying the necessary metadata.

- **Confusion**: Believing ZSTs are useless or purely theoretical.
  **Clarification**: ZSTs are central to real Rust patterns. `HashSet` is literally `HashMap<K, ()>`, and the monomorphized code eliminates all value-related overhead. PhantomData is a ZST that controls variance and drop checking.

- **Confusion**: Assuming `Result<T, Void>` is just `T` at the representation level.
  **Clarification**: While `Result<T, Void>` is represented as just `T` in practice, this is an optimization not formally guaranteed. Transmuting between them is still technically UB.

# Source Reference

Chapter 2: Data Representation in Rust, section "Exotically Sized Types" -- Dynamically Sized Types (DSTs), Zero Sized Types (ZSTs), Empty Types, Extern Types.

# Verification Notes

- Definition source: Direct synthesis from Ch. 2 "Exotically Sized Types" section (lines 189-367 of source)
- Key Properties: All items explicitly stated in the source text with code examples
- Confidence rationale: HIGH -- each exotic type category has a dedicated subsection with clear definitions and examples
- Uncertainties: The source notes extern types (RFC 1861) are "stuck in limbo" regarding `size_of_val` behavior; custom DSTs are described as "largely half-baked"
- Cross-reference status: All slugs reference cards in the nomicon extraction set
