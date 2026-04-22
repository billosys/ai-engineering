---
concept: Name Resolution
slug: name-resolution
category: language-semantics
subcategory: names-and-scoping
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Names"
chapter_number: 12
pdf_page: null
section: "Names, Namespaces, Scopes, Preludes, Paths, Name Resolution, Visibility and Privacy"
extraction_confidence: high
aliases:
  - "names"
  - "namespaces"
  - "scopes"
  - "preludes"
  - "paths"
  - "visibility"
  - "privacy"
  - "pub(crate)"
  - "canonical paths"
  - "turbofish"
  - "name resolution"
  - "qualified paths"
prerequisites:
  - rust-type-system
extends: []
related:
  - special-types-and-traits
  - type-coercions-and-destructors
contrasts_with: []
answers_questions:
  - "What are the different namespaces in Rust?"
  - "How does name resolution work in Rust?"
  - "What are preludes and how do they work?"
  - "What are the different kinds of paths in Rust?"
  - "How does visibility and privacy work?"
  - "What is pub(crate) and pub(super)?"
  - "What is a canonical path?"
  - "What is the turbofish syntax?"
  - "How do generic parameter scopes work?"
  - "What is the no_std attribute?"
  - "How does pattern binding shadowing work?"
  - "What are the three stages of name resolution?"
---

# Quick Definition

Names in Rust are organized into five namespaces (Type, Value, Macro, Lifetime, Label) and resolved through a three-stage process: expansion-time resolution (macros and `use` declarations), primary resolution (remaining non-type-dependent names), and type-relative resolution (names requiring type information). Access to names is controlled by visibility modifiers (`pub`, `pub(crate)`, `pub(super)`, `pub(in path)`), and names are brought into scope through preludes, paths, and `use` declarations.

# Core Definition

An **entity** is "a language construct that can be referred to in some way within the source program, usually via a path." Entities include types, items, generic parameters, variable bindings, loop labels, lifetimes, fields, attributes, and lints. A **declaration** introduces a name that refers to an entity, and that name is valid within a **scope** -- a region of source text where it may be referenced.

**Namespaces** segregate names so the same name can refer to different entities without conflict. The five namespaces are:

- **Type Namespace**: Modules, external crate declarations, structs, unions, enums, enum variants, traits, type aliases, associated types, built-in types, generic type parameters, `Self` type
- **Value Namespace**: Functions, constants, statics, struct/enum variant constructors, `Self` constructors, generic const parameters, associated consts/functions, local bindings (`let`, `if let`, `while let`, `for`, `match`, function/closure parameters)
- **Macro Namespace**: `macro_rules!` declarations, built-in attributes, tool attributes, procedural macros (function-like, derive, attribute). Split into two sub-namespaces: bang-style macros and attributes, preventing one from shadowing the other.
- **Lifetime Namespace**: Generic lifetime parameters
- **Label Namespace**: Loop labels, block labels

**Scopes** determine where names are visible. Item names declared in a module extend from module start to end. Statement-scoped items extend to the end of their block. Pattern bindings (`let`) extend from after the `let` statement to the end of the block. Function parameters are scoped to the function body. Generic parameters are scoped to the item they are declared on and are available within the generic parameter list regardless of declaration order.

**Preludes** are collections of names automatically brought into scope of every module (but not as members of the module). Five prelude layers exist, ordered by shadowing priority (earlier shadows later): (1) Extern prelude, (2) Tool prelude, (3) `macro_use` prelude, (4) Standard library prelude, (5) Language prelude. Items in a module shadow items in any prelude.

The **standard library prelude** depends on edition and `no_std`: editions 2015/2018 use `std::prelude::v1` (or `core::prelude::v1` with `no_std`); editions 2021/2024 use their respective versioned preludes. The **extern prelude** contains external crates; `core` is always present, `std` is present unless `no_std` is specified. The **language prelude** includes primitive types and built-in attributes; it cannot be disabled by `no_implicit_prelude`.

**Paths** refer to entities via `::` separated segments. Path types include:
- **Simple paths**: Used in visibility, attributes, macros, `use` items
- **Paths in expressions**: Support generic arguments with turbofish syntax (`::<>`)
- **Qualified paths**: `<Type as Trait>::method()` for disambiguation
- **Paths in types**: Type references, no turbofish required

Path qualifiers: `::` (global/extern prelude), `self` (current module), `Self` (implementing type), `super` (parent module, may be repeated), `crate` (crate root), `$crate` (macro-defining crate root).

**Canonical paths** correspond to where an item is defined. Use declarations and implementations don't have canonical paths; all other paths to items are aliases.

**Name resolution** has three stages:
1. **Expansion-time resolution** (early resolution): Resolves `use` declarations and macro invocations. After this stage, no unexpanded macro invocations remain. Resolution must be stable regardless of macro expansion order.
2. **Primary resolution** (late resolution): Resolves names not dependent on type information.
3. **Type-relative resolution**: Resolves names requiring type information (e.g., associated items through type aliases).

**Visibility and privacy**: By default, everything is private, with two exceptions: associated items in a `pub` trait, and enum variants in a `pub` enum are public by default. Public items can be accessed externally if all ancestor modules are also accessible. Private items can be accessed by the current module and its descendants. Scoped visibility: `pub(crate)` (crate-wide), `pub(super)` (parent module), `pub(in path)` (specific ancestor module), `pub(self)` (equivalent to private). Re-exporting via `pub use` short-circuits the privacy chain.

# Prerequisites

- **rust-type-system** -- name resolution references types, traits, and items defined by the type system

# Key Properties

1. Five namespaces (Type, Value, Macro, Lifetime, Label) allow the same name to refer to different entities
2. The Macro namespace has two sub-namespaces (bang-style and attributes) that don't shadow each other
3. Fields, despite being named, are not in any namespace -- they are accessed via field expressions only
4. Generic parameters are in scope within the generic parameter list regardless of declaration order
5. It is an error to shadow generic parameters (except items within functions may shadow outer function generics)
6. Pattern bindings may shadow any name in scope except const generics, static items, const items, and struct/enum constructors
7. Preludes are layered with defined shadowing priority; module items shadow all preludes
8. The language prelude (primitive types, built-in attributes) cannot be disabled
9. Name resolution is split into three stages: expansion-time, primary, and type-relative
10. Resolution must be stable regardless of macro expansion order
11. Type-relative paths (`use m::A::V`) cannot be resolved in `use` declarations (expansion-time)
12. Everything is private by default; `pub` trait associated items and `pub` enum variants are the exceptions
13. Private items are accessible by the current module and all descendants
14. Turbofish (`::< >`) is required before generic arguments in expression paths to avoid ambiguity with `<`

# Construction / Recognition

## Namespace Overlap Example
```rust
struct Foo(u32);            // Type namespace (type) + Value namespace (constructor)
macro_rules! Foo { () => {} } // Macro namespace

fn example<'Foo>(f: Foo) {  // 'Foo in Lifetime namespace
    let ctor = Foo;          // Value namespace (constructor)
    Foo!{}                   // Macro namespace
    'Foo: loop {             // 'Foo as Label namespace
        let x: &'Foo Foo;   // 'Foo is lifetime, Foo is type
        break 'Foo;          // 'Foo is label
    }
}
```

## Visibility Modifiers
| Modifier | Accessible from |
|----------|----------------|
| (none) / `pub(self)` | Current module only |
| `pub(super)` | Parent module and its descendants |
| `pub(in path)` | Specified ancestor module and its descendants |
| `pub(crate)` | Anywhere in the current crate |
| `pub` | External crates (if all ancestors are also `pub`) |

## Prelude Shadowing Order (Higher Priority First)
1. Extern prelude (external crates)
2. Tool prelude (tool names)
3. `macro_use` prelude (macros from `extern crate`)
4. Standard library prelude (edition-dependent)
5. Language prelude (primitive types, built-in attributes)

# Context & Application

- **Typical contexts**: Understanding why a name resolves to one entity over another, especially when macros or globs introduce ambiguity. Designing module hierarchies with appropriate visibility.
- **Common applications**: Organizing public APIs while hiding implementation details; using `pub(crate)` for crate-internal helpers; resolving trait method ambiguity with qualified paths; understanding why `use` imports fail for type-relative paths.
- **`no_std` development**: The `no_std` attribute replaces the `std` prelude with `core` prelude and removes `std` from the extern prelude, but `core` is always available. Additional crates like `alloc` must be brought in with `extern crate alloc`.

# Examples

**Example 1** -- Path qualifiers (Ch. 12, "Paths"):
```rust
mod a { pub fn foo() {} }
mod b {
    pub fn foo() {
        super::a::foo();          // super resolves to parent
        crate::a::foo();          // crate resolves to crate root
        self::foo();              // self resolves to current module (recursive!)
    }
}
```

**Example 2** -- Qualified path for disambiguation (Ch. 12, "Qualified paths"):
```rust
struct S;
impl S { fn f() { println!("S"); } }
trait T1 { fn f() { println!("T1"); } }
impl T1 for S {}
trait T2 { fn f() { println!("T2"); } }
impl T2 for S {}

S::f();            // Calls inherent impl
<S as T1>::f();    // Calls T1's implementation
<S as T2>::f();    // Calls T2's implementation
```

**Example 3** -- Scoped visibility (Ch. 12, "Visibility and privacy"):
```rust
pub mod outer_mod {
    pub mod inner_mod {
        pub(in crate::outer_mod) fn outer_mod_visible_fn() {}
        pub(crate) fn crate_visible_fn() {}
        pub(super) fn super_mod_visible_fn() {}
        pub(self) fn inner_mod_visible_fn() {}
    }
}
```

**Example 4** -- Canonical paths (Ch. 12, "Canonical paths"):
```rust
mod a {                        // crate::a
    pub struct Struct;         // crate::a::Struct
    pub trait Trait {           // crate::a::Trait
        fn f(&self);           // crate::a::Trait::f
    }
    impl Trait for Struct {
        fn f(&self) {}         // <crate::a::Struct as crate::a::Trait>::f
    }
    impl Struct {
        fn g(&self) {}         // <crate::a::Struct>::g
    }
}
```

# Relationships

## Builds Upon
- **rust-type-system** -- names refer to types, items, and other entities defined by the type system

## Enables
No directly enabled cards within this batch.

## Related
- **special-types-and-traits** -- special types like `Sized` interact with the language prelude
- **type-coercions-and-destructors** -- method resolution via deref coercions interacts with name resolution

## Contrasts With
No direct contrasts within scope.

# Common Errors

- **Error**: Using a type-relative path in a `use` declaration (e.g., `use MyEnum::AssociatedConst`).
  **Correction**: Type-relative paths cannot be resolved during expansion-time resolution. Access them via expression paths instead (`let x = MyEnum::AssociatedConst;`).

- **Error**: Expecting glob imports with conflicting names to produce an error at import time.
  **Correction**: "Glob imports are allowed to import conflicting names in the same namespace as long as the name is not used." The error occurs at use, not at import.

- **Error**: Assuming `pub` makes an item globally accessible regardless of parent module visibility.
  **Correction**: "To access an item, all of its parent items up to the current scope must still be visible as well."

# Common Confusions

- **Confusion**: Namespaces and modules are the same thing.
  **Clarification**: Namespaces are logical groupings (Type, Value, Macro, Lifetime, Label) that allow the same name to refer to different entities. Modules are organizational units within the Type namespace that create scope boundaries.

- **Confusion**: `self` and `Self` are the same.
  **Clarification**: Lowercase `self` refers to the current module (in paths) or the method receiver (in method bodies). Uppercase `Self` refers to the current type being implemented or defined.

- **Confusion**: `#![no_implicit_prelude]` removes all preludes.
  **Clarification**: It removes the standard library prelude, extern prelude, `macro_use` prelude, and tool prelude, but "does not affect the language prelude" -- primitive types and built-in attributes remain available.

# Source Reference

The Rust Reference, Chapter 12: Names (Names, Namespaces, Scopes, Preludes, Paths, Name Resolution, Visibility and Privacy).

# Verification Notes

- Definition source: Direct from Ch. 12 of The Rust Reference
- Confidence rationale: High -- namespaces, scopes, and visibility rules are precisely specified
- Uncertainties: Primary and type-relative resolution sections are noted as placeholders for future expansion; macro resolution visitation order "may change in the future"
- Cross-reference status: Related cards verified against planned card slugs
