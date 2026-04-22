---
concept: Rust Type System
slug: rust-type-system
category: type-system
subcategory: types
tier: foundational
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Type System"
chapter_number: 10
pdf_page: null
section: "Types, Type Expressions, Recursive Types, Primitive Types, Sequence Types, User-Defined Types, Function Types, Pointer Types, Trait Types, Type Parameters, DSTs, Type Layout"
extraction_confidence: high
aliases:
  - "types"
  - "Rust types"
  - "type expressions"
  - "type layout"
  - "repr attribute"
  - "dynamically sized types"
  - "DST"
prerequisites: []
extends: []
related:
  - type-coercions-and-destructors
  - special-types-and-traits
  - name-resolution
contrasts_with: []
answers_questions:
  - "What types exist in Rust?"
  - "What is a type expression?"
  - "What are the primitive types in Rust?"
  - "What are dynamically sized types (DSTs)?"
  - "How does Rust lay out types in memory?"
  - "What are the repr attributes and when should I use them?"
  - "What are function item types vs function pointer types?"
  - "How do closures capture variables?"
  - "What is the never type?"
  - "What are trait objects and impl Trait?"
  - "What is the difference between argument-position and return-position impl Trait?"
  - "What is subtyping and variance in Rust?"
---

# Quick Definition

Rust's type system encompasses primitive types (bool, numeric, char, str, never), sequence types (tuple, array, slice), user-defined types (struct, enum, union), function types (function items, closures), pointer types (references, raw pointers, function pointers), and trait types (trait objects, impl Trait). Every value has a known type, and the system enforces memory safety through ownership, borrowing, and lifetime tracking at compile time.

# Core Definition

Every variable, item, and value in a Rust program has a type. "The type of a value defines the interpretation of the memory holding it and the operations that may be performed on the value." (Ch. 10, "Types"). Built-in types are "tightly integrated into the language, in nontrivial ways that are not possible to emulate in user-defined types," while user-defined types "have limited capabilities."

**Primitive types** include: `bool` (1 byte, bit pattern `0x00` or `0x01`), numeric types (integers `i8` through `i128`, `u8` through `u128`, `usize`/`isize`, floats `f32`/`f64`), `char` (a Unicode scalar value, 32-bit, same layout as `u32`), `str` (a dynamically sized UTF-8 byte sequence), and the never type `!` (a type with no values that can be coerced into any other type, used for diverging functions).

**Sequence types**: Tuples are heterogeneous structural types; the unit tuple `()` is zero-sized. Arrays `[T; N]` are fixed-size sequences. Slices `[T]` are dynamically sized views into sequences.

**User-defined types**: Structs have undefined default memory layout (the compiler may reorder fields). Enums are nominal, heterogeneous disjoint union types where each value consumes as much memory as the largest variant plus a discriminant. Unions are C-like unions where accessing a field transmutes the content.

**Function item types** are zero-sized types that uniquely identify a function -- "its name, its type arguments, and its early-bound lifetime arguments." Different functions or the same function with different generics yield distinct types. They coerce to function pointers with matching signatures.

**Closure types** are unique anonymous types approximately equivalent to structs containing captured values. Closures implement `FnOnce`, and optionally `FnMut` (if they don't move out of captures) and `Fn` (if they don't mutate or move). Since Edition 2021, closures capture individual fields rather than entire variables. Non-capturing closures coerce to function pointers.

**Pointer types**: Shared references (`&T`) prevent direct mutation and are `Copy`. Mutable references (`&mut T`) provide exclusive access and are not `Copy`. Raw pointers (`*const T`, `*mut T`) lack safety guarantees; dereferencing them is unsafe. Function pointers (`fn(...)`) are created via coercion from function items or non-capturing closures.

**Trait objects** (`dyn Trait`) are opaque values implementing a set of traits, stored behind a pointer with a vtable for dynamic dispatch. **Impl Trait** in argument position is syntactic sugar for an anonymous generic type parameter; in return position, it allows returning an abstract type the function chooses.

**Dynamically sized types (DSTs)** have sizes known only at runtime. Slices, trait objects, and `str` are DSTs. Pointers to DSTs are "fat pointers" -- twice the size of regular pointers, storing either a length or a vtable pointer.

**Subtyping and variance**: Subtyping in Rust is restricted to lifetimes and higher-ranked lifetimes. `&'static str` is a subtype of `&'a str` because `'static` outlives any `'a`. Variance describes how a generic type's subtyping relates to its type parameter's subtyping: covariant (passes through), contravariant (reverses), or invariant (no relation). `&'a T` is covariant in both `'a` and `T`; `&'a mut T` is covariant in `'a` but invariant in `T`.

# Prerequisites

No prior concept cards required; this is a foundational card covering the entire type taxonomy.

# Key Properties

1. Every value has a type that defines both memory interpretation and allowed operations
2. `bool` has size and alignment of 1; only `0x00` and `0x01` are valid bit patterns
3. `char` is a 32-bit Unicode scalar value with the same size and alignment as `u32`
4. `usize` and `isize` match the platform's pointer size; they are at least 16 bits wide
5. The never type `!` has no values; expressions of type `!` can be coerced into any other type
6. Tuple field names are numeric (`0`, `1`, ...); the unit type `()` is zero-sized with alignment 1
7. Array size must be a constant expression evaluating to `usize`
8. Struct memory layout is undefined by default (compiler may reorder fields); use `#[repr(C)]` for deterministic layout
9. Function item types are zero-sized and unique per function/generic instantiation
10. Closures since Edition 2021 capture individual fields, not entire variables
11. `move` closures may still implement `Fn`/`FnMut` -- the trait is determined by usage, not capture mode
12. DST pointers are fat pointers: slices/str store length; trait objects store vtable pointer
13. `impl Trait` in argument position is caller-chooses (like generics); in return position is callee-chooses
14. Variance is automatically determined from how type parameters are used in field types

# Construction / Recognition

## Type Layout and Representations

The layout of a type is its size, alignment, and field offsets. Four representations are available via `#[repr(...)]`:

- **`Rust`** (default): No guarantees beyond soundness. Fields may be reordered.
- **`C`**: Matches C layout rules -- fields in declaration order, padding for alignment. Required for FFI interoperability.
- **Primitive representations** (`u8`, `u16`, etc.): Apply to enums only; set discriminant size.
- **`transparent`**: The type has the same layout and ABI as its single non-zero-sized field. Cannot combine with other representations.

The `align` and `packed` modifiers raise or lower alignment: `#[repr(packed)]` removes inter-field padding; `#[repr(align(N))]` raises minimum alignment. They cannot be combined on the same type.

## Closure Capture Rules (Edition 2021+)

1. Closures capture the minimal path needed (e.g., `s.f1.1` not all of `s`)
2. Capture mode is the minimum needed: `ImmBorrow < UniqueImmBorrow < MutBorrow < ByValue`
3. Shared reference dereferences truncate the capture path at the rightmost dereference
4. Wildcard patterns (`_`) do not capture values
5. Array/slice captures are always whole -- partial capture is not supported
6. Union field access and raw pointer dereference capture the entire parent

# Context & Application

- **Typical contexts**: Understanding what types are available, how they are laid out, and how the compiler handles them is foundational to all Rust programming.
- **Common applications**: Choosing between `&T`, `Box<T>`, `Rc<T>`, and raw pointers; designing struct layouts for FFI; selecting closure types for callbacks; understanding why certain code does or doesn't compile due to variance constraints.
- **Interior mutability**: `UnsafeCell<T>` is the only way to disable the requirement that shared references point to immutable data. `Cell<T>`, `RefCell<T>`, and atomics build on it.

# Examples

**Example 1** -- Recursive type (Ch. 10, "Recursive Types"):
```rust
enum List<T> {
    Nil,
    Cons(T, Box<List<T>>)
}
let a: List<i32> = List::Cons(7, Box::new(List::Cons(13, Box::new(List::Nil))));
```
Recursive types must include a pointer indirection (like `Box`) since the size must be finite.

**Example 2** -- Function item type coercion (Ch. 10, "Function item types"):
```rust
fn foo<T>() { }
// foo::<i32> and foo::<u32> have different function item types.
// But they coerce to the same function pointer type:
let foo_ptr: fn() = if true { foo::<i32> } else { foo::<u32> };
```

**Example 3** -- Closure capture precision (Ch. 10, "Closure types"):
```rust
struct SomeStruct { f1: (i32, i32) }
let s = SomeStruct { f1: (1, 2) };
let c = || {
    let x = s.f1.1; // Only s.f1.1 is captured by ImmBorrow
};
c();
```

**Example 4** -- Variance table (Ch. 10, "Subtyping and Variance"):

| Type                    | Variance in `'a` | Variance in `T` |
|-------------------------|-------------------|-----------------|
| `&'a T`                 | covariant          | covariant       |
| `&'a mut T`             | covariant          | invariant       |
| `*const T`              | --                 | covariant       |
| `*mut T`                | --                 | invariant       |
| `fn(T) -> ()`           | --                 | contravariant   |
| `UnsafeCell<T>`         | --                 | invariant       |
| `dyn Trait<T> + 'a`     | covariant          | invariant       |

**Example 5** -- `repr(C)` struct layout (Ch. 10, "Type Layout"):
```rust
#[repr(C)]
struct ThreeInts {
    first: i16,   // offset 0, size 2
    second: i8,   // offset 2, size 1 (+ 1 byte padding)
    third: i32    // offset 4, size 4
}
// Total size: 8, alignment: 4
```

# Relationships

## Builds Upon
No prior concept cards.

## Enables
- **type-coercions-and-destructors** -- coercion rules and destructor behavior depend on the type system
- **special-types-and-traits** -- compiler-known types like `Box`, `Copy`, `Sized` build on type system foundations

## Related
- **name-resolution** -- paths to types are resolved through the name resolution system

## Contrasts With
No direct contrasts within scope.

# Common Errors

- **Error**: Attempting to create a recursive type without indirection (e.g., `struct Node { next: Option<Node> }`).
  **Correction**: Recursive fields must use pointer types like `Box<Node>` to ensure finite size.

- **Error**: Assuming `&mut T` is covariant in `T` (e.g., trying to assign `&mut String` where `&mut dyn Display` is expected without explicit coercion).
  **Correction**: `&mut T` is invariant in `T`. Use explicit coercion or trait objects.

- **Error**: Expecting closures with different function items to unify without coercion.
  **Correction**: Each function item has a unique type. Use function pointers (`fn(...)`) when you need a single type for different functions.

# Common Confusions

- **Confusion**: `move` closures always implement `FnOnce` only.
  **Clarification**: "`move` closures may still implement `Fn` or `FnMut`, even though they capture variables by move. This is because the traits implemented by a closure type are determined by what the closure does with captured values, not how it captures them." (Ch. 10, "Closure types")

- **Confusion**: Function item types and function pointer types are the same thing.
  **Clarification**: Function items are zero-sized and uniquely identify a function; function pointers are sized values that store an address. Function items coerce to function pointers, but not vice versa.

- **Confusion**: `impl Trait` in argument and return position work the same way.
  **Clarification**: In argument position, the caller chooses the concrete type (like generics). In return position, the function chooses the type, and "the caller may only use the methods declared by the specified Trait."

# Source Reference

The Rust Reference, Chapter 10: Type System (Types, Boolean, Numeric, Char, Str, Never, Tuple, Array, Slice, Struct, Enum, Union, Function Item, Closure, Pointer, Function Pointer, Trait Object, Impl Trait, Type Parameters, Inferred Type, Dynamically Sized Types, Type Layout, Interior Mutability, Subtyping and Variance).

# Verification Notes

- Definition source: Direct from Ch. 10 of The Rust Reference
- Confidence rationale: High -- type system documentation is comprehensive and detailed
- Uncertainties: The Rust representation's layout guarantees are deliberately minimal and may evolve
- Cross-reference status: Related cards (type-coercions-and-destructors, special-types-and-traits, name-resolution) verified against planned card slugs
