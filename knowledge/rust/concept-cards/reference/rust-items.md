---
concept: Rust Items
slug: rust-items
category: language-semantics
subcategory: declarations
tier: foundational
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Items"
chapter_number: 6
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "item declarations"
  - "item types"
  - "Rust item taxonomy"
  - "modules and items"
  - "associated items"
  - "generic parameters"
prerequisites: []
extends: []
related:
  - rust-attributes
  - conditional-compilation
contrasts_with: []
answers_questions:
  - "What are the kinds of items in Rust?"
  - "What is the difference between an item and a statement?"
  - "Where can items be declared?"
  - "What are associated items and where can they appear?"
  - "How do inherent and trait implementations differ?"
  - "What is the orphan rule for trait implementations?"
  - "What are the three kinds of struct in Rust?"
  - "What is dyn compatibility (object safety) for traits?"
  - "What types can be used as const generic parameters?"
---

# Quick Definition

An _item_ is a compile-time component of a Rust crate -- "entirely determined at compile-time, generally remain fixed during execution, and may reside in read-only memory" (Ch. 6). Rust defines 13 kinds of items (modules, extern crate, use declarations, functions, type aliases, structs, enumerations, unions, constants, statics, traits, implementations, and extern blocks), plus associated items (functions/methods, types, constants) that appear within traits and implementations, and generic parameters that parameterize many item kinds.

# Core Definition

Items form the structural backbone of a Rust program. "An item is a component of a crate. Items are organized within a crate by a nested set of modules" (Ch. 6). Every crate has a single outermost anonymous module, and all items have paths within the module tree.

Items break into two grammar categories: `VisItem` (items that accept a visibility qualifier) and `MacroItem` (macro invocations and macro_rules definitions). Items "may be declared in the root of the crate, a module, or a block expression." A subset called _associated items_ may appear in traits and implementations, and another subset of _external items_ may appear in extern blocks. Items "may be defined in any order, with the exception of macro_rules."

**Modules** are containers for items, forming the hierarchical namespace tree. A module without a body loads from an external file, with the filesystem path mirroring the module path. The `path` attribute can override file locations.

**Functions** consist of a block (body), name, parameters, and output type. Functions yield zero-sized function item types. Qualifiers include `const`, `async`, `unsafe`, and `extern`. Functions whose first parameter is `self` are _methods_ and can be called with dot syntax. Bodyless functions (terminated with `;`) appear only in traits or extern blocks.

**Data types** come in several forms:
- **Structs** have three variants: named-field structs, tuple structs (which also define a constructor function), and unit-like structs (which define a constant). Layout is not specified unless a `repr` attribute is used.
- **Enumerations** define a type plus constructors. Variants can be unit, tuple, or struct-like. Discriminants can be explicitly assigned or auto-incremented. Zero-variant enums are uninhabited types.
- **Unions** share storage across all fields. Reads require `unsafe` blocks; writes are safe. Field types are restricted to `Copy` types, references, `ManuallyDrop<T>`, and tuples/arrays of allowed types.

**Constants and Statics**: Constants are "essentially inlined wherever they are used" and are not associated with a specific memory address. Statics represent a program allocation with `'static` lifetime; all references to a static refer to the same allocation. Mutable statics require `unsafe` for both reads and writes.

**Traits** describe abstract interfaces with associated functions, types, and constants. The implicit `Self` type parameter refers to the implementing type. Dyn compatibility (formerly "object safety") requires: all supertraits are dyn compatible, `Sized` is not a supertrait, no associated constants, no generic associated types, and all methods must be dispatchable or explicitly non-dispatchable.

**Implementations** come in two kinds: _inherent_ (directly on a type, containing functions/methods and constants but not type aliases) and _trait_ (implementing a trait for a type). The _orphan rule_ restricts trait implementations: "a trait implementation is only allowed if either the trait or at least one of the types in the implementation is defined in the current crate."

**Generic parameters** include lifetime, type, and const parameters. Const generics are restricted to integer types, `char`, and `bool`. Parameters must constrain the implementation (appear in the trait or implementing type).

**Associated items** come in three kinds: functions/methods, types, and constants. They are declared in traits and defined in implementations. "Every associated item kind comes in two varieties: definitions that contain the actual implementation and declarations that declare signatures for definitions."

# Prerequisites

General understanding of Rust syntax, ownership, and the type system is assumed. This is a foundational taxonomy of the language's declaration forms.

# Key Properties

1. Items are entirely determined at compile-time and may reside in read-only memory
2. 13 item kinds exist, organized in a module tree; items can be declared at crate root, in modules, or in block expressions
3. Items may be defined in any order (except `macro_rules`); name resolution allows forward references
4. Modules map to the filesystem: `mod foo;` loads `foo.rs` or `foo/mod.rs` (but not both)
5. Structs come in three forms: named-field, tuple, and unit-like; enums have unit, tuple, and struct-like variants
6. Union field reads require `unsafe`; writes are safe; field types are restricted to `Copy`, references, and `ManuallyDrop<T>`
7. Constants are inlined at each use site; statics have a fixed allocation with `'static` lifetime
8. Static items in generic scopes produce exactly one static (not one per monomorphization)
9. Trait implementations must satisfy the orphan rule and coherence (no overlapping impls)
10. Dyn-compatible traits cannot have associated constants, generic associated types, or require `Self: Sized`
11. Const generic parameters are limited to `u8`-`u128`, `i8`-`i128`, `usize`, `isize`, `char`, and `bool`
12. `use` declarations create local name bindings; when `pub`, they become re-exports

# Construction / Recognition

## To Declare Items:

1. Use `mod name { ... }` or `mod name;` for modules
2. Use `fn name(params) -> Type { body }` for functions; add `self` parameter for methods
3. Use `struct Name { fields }`, `struct Name(fields)`, or `struct Name;` for the three struct forms
4. Use `enum Name { Variant1, Variant2(T), Variant3 { field: T } }` for enumerations
5. Use `impl Type { ... }` for inherent implementations; `impl Trait for Type { ... }` for trait implementations
6. Use `trait Name { ... }` to declare a trait with associated items

## To Identify Item Properties:

1. Check namespace: types (structs, enums, unions, modules, traits, type aliases) are in the type namespace; values (functions, constants, statics) are in the value namespace
2. Check visibility: `pub`, `pub(crate)`, `pub(super)`, `pub(in path)`, or private (default)
3. Check whether generic parameters constrain the implementation

# Context & Application

- **Module organization**: Modules provide namespace hierarchy and privacy boundaries; privacy is the primary mechanism for controlling access to implementation details
- **Type definitions**: Structs, enums, and unions define the data types that Rust programs manipulate
- **Trait system**: Traits define shared behavior; the orphan rule ensures coherence across the ecosystem
- **FFI**: Extern blocks declare foreign functions and statics, forming Rust's foreign function interface; functions in extern blocks are implicitly unsafe unless marked `safe`
- **Generics**: Generic parameters enable code reuse; const generics allow parameterization over values

# Examples

**Example 1** (Ch. 6, "Items"): The item grammar showing the two top-level categories:
```rust,ignore
Item -> OuterAttribute* ( VisItem | MacroItem )
VisItem -> Visibility? ( Module | ExternCrate | UseDeclaration | Function |
           TypeAlias | Struct | Enumeration | Union | ConstantItem |
           StaticItem | Trait | Implementation | ExternBlock )
```

**Example 2** (Ch. 6, "Structs"): The three forms of struct:
```rust
// Named-field struct
struct Point { x: i32, y: i32 }

// Tuple struct (also defines a constructor function)
struct Inches(i32);

// Unit-like struct (defines a constant of its own type)
struct Marker;
```

**Example 3** (Ch. 6, "Implementations"): Inherent vs. trait implementation:
```rust
struct Circle { radius: f64 }

// Inherent implementation
impl Circle {
    fn new(r: f64) -> Circle { Circle { radius: r } }
    fn area(&self) -> f64 { std::f64::consts::PI * self.radius * self.radius }
}

// Trait implementation
impl std::fmt::Display for Circle {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "Circle(r={})", self.radius)
    }
}
```

**Example 4** (Ch. 6, "Const generics"): Const generic parameters:
```rust
struct InnerArray<T, const N: usize>([T; N]);

fn foo<const N: usize>(arr: [i32; N]) {
    println!("{}", N * 2);
}
```

# Relationships

## Builds Upon
(none -- items are the foundational organizational unit of Rust programs)

## Enables
- **rust-attributes** -- attributes are applied to items and modify their behavior
- **conditional-compilation** -- `cfg` attributes conditionally include or exclude items

## Related
- **conditional-compilation** -- items are the primary targets of `#[cfg]`
- **rust-attributes** -- items accept outer attributes; some item types also accept inner attributes

## Contrasts With
(none within scope)

# Common Errors

- **Error**: Having both `foo.rs` and `foo/mod.rs` for the same module.
  **Correction**: "It is not allowed to have both util.rs and util/mod.rs" (Ch. 6). Choose one convention.

- **Error**: Adding associated type aliases in inherent implementations.
  **Correction**: Inherent implementations "cannot contain associated type aliases" (Ch. 6). Associated types only appear in trait definitions and trait implementations.

- **Error**: Implementing a foreign trait for a foreign type (violating the orphan rule).
  **Correction**: "A trait implementation is only allowed if either the trait or at least one of the types in the implementation is defined in the current crate" (Ch. 6).

- **Error**: Using non-primitive types as const generic parameters.
  **Correction**: "The only allowed types of const parameters are u8, u16, u32, u64, u128, usize, i8, i16, i32, i64, i128, isize, char and bool" (Ch. 6).

# Common Confusions

- **Confusion**: Constants and statics are interchangeable.
  **Clarification**: Constants are "inlined wherever they are used" -- references to the same constant may point to different addresses. Statics represent a single allocation; "all references and raw pointers to the static refer to the same allocation." Prefer constants unless you need the single-address property, large storage, or interior mutability.

- **Confusion**: Dyn compatibility ("object safety") means the trait has no methods.
  **Clarification**: Dyn-compatible traits can have methods, but those methods must be dispatchable (no type parameters, receiver must be `&Self`/`&mut Self`/`Box<Self>`/etc., no `Self` in return type). Non-dispatchable methods can coexist if they have a `where Self: Sized` bound.

- **Confusion**: Union field writes are unsafe like reads.
  **Clarification**: "Writes to union fields are safe, since they just overwrite arbitrary data, but cannot cause undefined behavior." Only reads require `unsafe`, because the bit pattern may not be valid for the read type.

# Source Reference

Chapter 6: Items (4219 lines). Covers all 13 item kinds: modules (with filesystem mapping and `path` attribute), extern crate declarations (with `no_link`), use declarations (visibility, paths, globs, underscore imports), functions (qualifiers, generics, async, const, extern), type aliases, structs, enumerations (discriminants, zero-variant enums), unions (field restrictions, read/write safety), constants (destructors, unnamed, evaluation), statics (generics, mutable statics), traits (bounds, dyn compatibility, supertraits, unsafe traits, visibility), implementations (inherent vs. trait, coherence, orphan rule, generic implementations), extern blocks (ABI, functions, statics, variadic functions, linking), generic parameters (const generics, where clauses), and associated items (functions/methods, types, constants).

# Verification Notes

- Definition source: Direct synthesis from Ch. 6 with key definitions quoted verbatim
- Key Properties: All 12 items derived from explicit source statements
- Confidence rationale: HIGH -- this is the authoritative language reference; all item kinds are explicitly defined and enumerated
- Uncertainties: The precise memory layout details and const generic expansion are evolving areas
- Cross-reference status: Related slugs reference cards in the reference extraction set
