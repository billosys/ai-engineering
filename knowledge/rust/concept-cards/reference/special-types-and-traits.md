---
concept: Special Types and Traits
slug: special-types-and-traits
category: type-system
subcategory: compiler-known-types
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Special Types and Traits"
chapter_number: 11
pdf_page: null
section: "Box, Rc, Arc, Pin, UnsafeCell, PhantomData, Operator Traits, Deref, Drop, Copy, Clone, Send, Sync, Termination, Auto Traits, Sized"
extraction_confidence: high
aliases:
  - "compiler known types"
  - "lang types"
  - "auto traits"
  - "marker traits"
  - "Box special features"
  - "Send and Sync"
  - "Copy trait"
  - "Sized trait"
prerequisites:
  - rust-type-system
extends:
  - rust-type-system
related:
  - type-coercions-and-destructors
  - rust-memory-model-and-panic
contrasts_with: []
answers_questions:
  - "What special features does Box<T> have?"
  - "What is UnsafeCell and why is it special?"
  - "What is PhantomData and what is it used for?"
  - "What does the Copy trait do and what are its constraints?"
  - "What is the difference between Copy and Clone?"
  - "What are Send and Sync?"
  - "What are auto traits and how do they work?"
  - "What is the Sized trait?"
  - "How does ?Sized work?"
  - "What is the Deref trait used for beyond operator overloading?"
  - "What types can take self by Box, Rc, Arc, or Pin?"
---

# Quick Definition

Certain types and traits in the standard library have special compiler support that user-defined types cannot replicate. These include `Box<T>` (built-in deref and move semantics), `UnsafeCell<T>` (the only source of interior mutability), `PhantomData<T>` (zero-sized ownership marker), auto traits (`Send`, `Sync`, `Unpin`, `UnwindSafe`, `RefUnwindSafe`), and fundamental traits like `Copy`, `Clone`, `Drop`, `Sized`, `Deref`, and `Termination`.

# Core Definition

"Certain types and traits that exist in the standard library are known to the Rust compiler. This chapter documents the special features of these types and traits." (Ch. 11, intro)

**`Box<T>`** has three special features: (1) "The dereference operator for `Box<T>` produces a place which can be moved from" -- both `*` and the destructor are built-in. (2) Methods can take `Box<Self>` as a receiver. (3) "A trait may be implemented for `Box<T>` in the same crate as `T`," bypassing the orphan rules that prevent this for other generic types.

**`Rc<T>`**, **`Arc<T>`**, and **`Pin<P>`** each allow methods to take them as receivers (`Rc<Self>`, `Arc<Self>`, `Pin<P>` respectively).

**`UnsafeCell<T>`** is "used for interior mutability. It ensures that the compiler doesn't perform optimisations that are incorrect for such types." It also ensures that `static` items with interior mutability aren't placed in read-only memory. It is the only sanctioned way to achieve interior mutability.

**`PhantomData<T>`** is "a zero-sized, minimum alignment, type that is considered to own a `T` for the purposes of variance, drop check, and auto traits." It informs the compiler about logical ownership without consuming space.

**Operator traits** (`std::ops` and `std::cmp`) overload operators, indexing, and call expressions.

**`Deref` and `DerefMut`**: Beyond overloading `*`, they are used in method resolution (auto-deref) and deref coercions.

**`Drop`** provides a destructor run whenever a value of the implementing type is to be destroyed.

**`Copy`** changes move semantics to copy semantics: "Values whose type implements `Copy` are copied rather than moved upon assignment." Constraints: `Copy` can only be implemented for types that don't implement `Drop`, and whose fields are all `Copy`. The compiler automatically implements `Copy` for tuples of `Copy` types, function pointers, function items, and closures that capture no values or only `Copy` values.

**`Clone`** is a supertrait of `Copy`. The compiler implements it for types with built-in `Copy`, tuples of `Clone` types, and closures capturing only `Clone` types.

**`Send`** indicates "a value of this type is safe to send from one thread to another."

**`Sync`** indicates "a value of this type is safe to share between multiple threads." It must be implemented for all types used in immutable `static` items.

**`Termination`** indicates acceptable return types for the `main` function and test functions.

**Auto traits** (`Send`, `Sync`, `Unpin`, `UnwindSafe`, `RefUnwindSafe`) have special properties: the compiler automatically implements them based on field types. For composite types, the auto trait is implemented if all fields implement it. For closures, if all captures implement it. Negative implementations (`impl !AutoTrait for T`) override automatic implementations (e.g., `*mut T` is `!Send`). Auto traits can be added as additional bounds to trait objects (e.g., `Box<dyn Debug + Send + UnwindSafe>`).

**`Sized`** indicates that a type's size is known at compile time. Type parameters are `Sized` by default. `Sized` is always implemented automatically by the compiler. The `?Sized` bound relaxes this default.

# Prerequisites

- **rust-type-system** -- special types build on the fundamental type system

# Key Properties

1. `Box<T>` has built-in dereference/move semantics and bypasses orphan rules for trait impls
2. `UnsafeCell<T>` is the sole mechanism for interior mutability; all safe interior-mutable types build on it
3. `PhantomData<T>` is zero-sized and affects variance, drop check, and auto-trait inference
4. `Copy` requires no `Drop` impl and all fields must be `Copy`
5. `Copy` changes assignment from move to copy semantics
6. `Clone` is a supertrait of `Copy` -- all `Copy` types are `Clone`
7. `Send` means safe to transfer across threads; `Sync` means safe to share between threads
8. Auto traits are automatically implemented based on field types; negative impls can override this
9. `*mut T` has negative `Send` implementation, making it `!Send` even if `T` is `Send`
10. `Sized` is an implicit bound on all type parameters; `?Sized` relaxes it
11. `Sized` is always implemented by the compiler, never by user code
12. `Deref` and `DerefMut` power method auto-deref and deref coercions, not just the `*` operator
13. Auto traits can be added as extra bounds on trait objects (e.g., `dyn Trait + Send`)

# Construction / Recognition

## When to Use PhantomData

Use `PhantomData<T>` when a type logically owns or references `T` but has no actual field of that type:
- Raw pointer wrappers that logically own data: `PhantomData<T>` for ownership
- Types parameterized by a lifetime but holding only raw pointers: `PhantomData<&'a T>` for the lifetime
- When you need specific variance: choose the phantom type accordingly

## Auto Trait Implementation Rules

| Type form | Auto trait implemented if... |
|-----------|----------------------------|
| `&T`, `&mut T`, `*const T`, `*mut T`, `[T; n]`, `[T]` | `T` does |
| Function items and function pointers | Always |
| Structs, enums, unions, tuples | All fields do |
| Closures | All capture types do |

Generic implementations can override automatic ones (e.g., `Send` for `&T` where `T: Sync`).

## Copy vs Clone Decision

- Use `Copy` when the type is small, has no heap allocation, and has no `Drop` impl
- Use `Clone` only when the type requires non-trivial duplication (heap allocation, resource acquisition)
- `Copy` implies `Clone`, but `Clone` does not imply `Copy`

# Context & Application

- **Typical contexts**: Designing types that interact with the borrow checker, thread safety system, or FFI.
- **Common applications**: Using `PhantomData` for lifetime-parameterized raw pointer wrappers, implementing `Send`/`Sync` for concurrent data structures, choosing `Copy` vs `Clone` for value types.
- **Thread safety**: A type is safe to send across threads if `Send`, safe to share via `&T` if `Sync`. `Rc<T>` is `!Send` and `!Sync` by design; use `Arc<T>` for thread-safe reference counting.

# Examples

**Example 1** -- Copy semantics (Ch. 11, "Copy"):
```rust
#[derive(Copy, Clone)]
struct Point { x: i32, y: i32 }

let p1 = Point { x: 1, y: 2 };
let p2 = p1;  // Copy, not move
println!("{}", p1.x);  // p1 is still valid
```

`Copy` cannot be derived if any field is not `Copy` or if the type implements `Drop`.

**Example 2** -- PhantomData for lifetime tracking:
```rust
use std::marker::PhantomData;

struct Iter<'a, T: 'a> {
    ptr: *const T,
    end: *const T,
    _marker: PhantomData<&'a T>,  // Establishes covariance in 'a and T
}
```

Without `PhantomData<&'a T>`, the lifetime `'a` would be unbounded.

**Example 3** -- Auto trait propagation (Ch. 11, "Auto traits"):
```rust
// Struct is Send+Sync because both fields are
struct MyStruct {
    data: Vec<i32>,     // Vec<i32> is Send + Sync
    count: usize,       // usize is Send + Sync
}

// This struct is NOT Sync because Rc is !Sync
struct NotSync {
    data: std::rc::Rc<i32>,  // Rc is !Send and !Sync
}
```

**Example 4** -- Trait object with auto trait bounds (Ch. 11, "Auto traits"):
```rust
use std::fmt::Debug;
// Auto traits can be added as extra bounds on trait objects
fn process(item: Box<dyn Debug + Send + Sync>) {
    println!("{:?}", item);
}
```

# Relationships

## Builds Upon
- **rust-type-system** -- special types are part of the broader type system

## Enables
- **type-coercions-and-destructors** -- `Drop`, `Deref`, `DerefMut`, `Copy`, `Unsize`, and `CoerceUnsized` directly power coercion and destructor behavior

## Related
- **rust-memory-model-and-panic** -- `Send`/`Sync` relate to memory safety in concurrent contexts; `Drop` interacts with panic unwinding

## Contrasts With
No direct contrasts within scope.

# Common Errors

- **Error**: Implementing `Copy` on a type that also implements `Drop`.
  **Correction**: "`Copy` can only be implemented for types which do not implement `Drop`." Remove the `Drop` impl or do not implement `Copy`.

- **Error**: Assuming `*mut T` is `Send` when `T` is `Send`.
  **Correction**: `*mut T` has a negative `Send` implementation in the standard library. Raw pointers are neither `Send` nor `Sync` regardless of `T`.

- **Error**: Forgetting `PhantomData` in a raw-pointer wrapper, causing unbounded lifetimes or incorrect variance.
  **Correction**: Add `PhantomData<&'a T>` or `PhantomData<T>` to declare the logical relationship.

# Common Confusions

- **Confusion**: `Copy` and `Clone` are the same.
  **Clarification**: `Copy` is implicit (on assignment) and must be trivial (bitwise). `Clone` is explicit (`.clone()`) and can perform arbitrary work. `Copy` is a subtrait of `Clone`, meaning all `Copy` types are `Clone`, but not the reverse.

- **Confusion**: `Send` means the type uses locks or atomics.
  **Clarification**: `Send` simply means it is safe to transfer ownership to another thread. Most types are `Send` automatically. Types like `Rc<T>` are `!Send` because their reference counting is not atomic.

- **Confusion**: `?Sized` makes a type dynamically sized.
  **Clarification**: `?Sized` removes the `Sized` bound, allowing a type parameter to accept both sized and unsized types. It does not change a type's sizedness.

# Source Reference

The Rust Reference, Chapter 11: Special Types and Traits.

# Verification Notes

- Definition source: Direct from Ch. 11 of The Rust Reference
- Confidence rationale: High -- the chapter is concise and explicit about each special type's properties
- Uncertainties: The chapter notes the `Box<T>` special features list is "nowhere close to an exhaustive list"
- Cross-reference status: Related cards verified against planned card slugs
