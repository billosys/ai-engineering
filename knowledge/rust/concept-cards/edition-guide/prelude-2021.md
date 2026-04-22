---
concept: Rust 2021 Prelude Additions
slug: prelude-2021
category: edition-2021
subcategory: null
tier: intermediate
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "04-rust-2021"
chapter_number: 4
pdf_page: null
section: "Additions to the prelude"
extraction_confidence: high
aliases:
  - "2021 prelude"
  - "prelude additions 2021"
  - "TryInto prelude"
prerequisites:
  - rust-2021-edition
extends: []
related:
  - prelude-2024
  - edition-migration
contrasts_with: []
answers_questions:
  - "What traits were added to the Rust 2021 prelude?"
  - "Why does adding a trait to the prelude require an edition?"
  - "How do I fix ambiguous method call errors after upgrading to Rust 2021?"
  - "What is the rust_2021_prelude_collisions lint?"
---

# Quick Definition

The Rust 2021 edition adds three traits to the standard library prelude: `std::convert::TryInto`, `std::convert::TryFrom`, and `std::iter::FromIterator`. This can cause ambiguity with existing trait methods of the same name, requiring fully qualified syntax or other disambiguation.

# Core Definition

"As a solution, Rust 2021 will use a new prelude. It's identical to the current one, except for three new additions: `std::convert::TryInto`, `std::convert::TryFrom`, `std::iter::FromIterator`." (Edition Guide, Ch. 4: Rust 2021, "Additions to the prelude")

The prelude is the module containing everything automatically imported in every module. Adding items to the prelude is normally non-breaking because the compiler prioritizes manually imported items. However, adding a trait can break code because method calls become ambiguous when two in-scope traits define the same method name.

# Prerequisites

- **Rust 2021 Edition** (`rust-2021-edition`) -- these prelude additions are part of the 2021 edition changes

# Key Properties

1. Three traits added: `TryInto`, `TryFrom`, and `FromIterator`
2. The compiler prioritizes manually imported items over prelude items
3. Adding a struct/enum to the prelude is not breaking (manual imports shadow prelude)
4. Adding a trait to the prelude can break code via ambiguous method resolution
5. The `rust_2021_prelude_collisions` migration lint detects affected code
6. Inherent methods always take precedence over trait methods (no migration needed for those)
7. Dynamic dispatch on `dyn Trait` requires special handling when prelude traits conflict

# Construction / Recognition

## To Disambiguate Conflicting Trait Methods:
1. Use fully qualified syntax: `<Type as MyTrait>::method()` instead of `Type::method()`
2. For `dyn Trait` method calls, add a dereference to clarify the receiver: `(&*f).try_into()` instead of `f.try_into()`
3. Run `cargo fix --edition` to have the compiler insert disambiguations automatically

## To Check if Migration Is Needed:
1. Look for traits that define methods named `try_into`, `try_from`, or `from_iter`
2. Check if those methods are called using method syntax or unqualified paths
3. Inherent methods with the same name do not need migration (they take precedence)
4. Core/std origin methods cannot collide with themselves

# Context & Application

The addition of `TryInto` and `TryFrom` to the prelude was a long-desired ergonomic improvement. Before Rust 2021, every file that used `x.try_into()` needed an explicit `use std::convert::TryInto;` import. However, adding these traits to the prelude could not be done without an edition boundary because existing code might define traits with conflicting method names (e.g., a custom `MyTryInto` trait with a `try_into` method).

The migration lint considers several factors: whether the call uses fully qualified or dot-call syntax, whether it is an inherent or trait method, whether the method originates from `core`/`std`, whether the type implements the potentially conflicting trait, and whether dynamic dispatch is involved.

# Examples

**Example 1** (Conflicting trait methods, "Migration needed" section):

```rust
trait MyTrait<A> {
    fn from_iter(x: Option<A>);
}

impl<T> MyTrait<()> for Vec<T> {
    fn from_iter(_: Option<()>) {}
}

fn main() {
    // Ambiguous in Rust 2021: both MyTrait and FromIterator define from_iter
    // Fix: use fully qualified syntax
    <Vec<i32> as MyTrait<()>>::from_iter(None);
}
```

**Example 2** (dyn Trait method calls, "Migration needed" section):

```rust
mod submodule {
    pub trait MyTrait {
        fn try_into(&self) -> Result<u32, ()>;
    }
}

fn bar(f: Box<dyn submodule::MyTrait>) {
    // In Rust 2021, f.try_into() is ambiguous.
    // Fix: dereference to clarify the receiver type
    (&*f).try_into();
}
```

**Example 3** (No migration needed, "No migration needed" section): Inherent methods always take precedence over trait methods, so a struct with an inherent `from_iter` method will not be affected by the prelude addition:

```rust
struct MyStruct { data: Vec<u32> }

impl MyStruct {
    fn from_iter(iter: impl IntoIterator<Item = u32>) -> Self {
        Self { data: iter.into_iter().collect() }
    }
}
// MyStruct::from_iter still calls the inherent method, not FromIterator::from_iter
```

# Relationships

## Builds Upon
- **rust-2021-edition** -- these additions are part of the 2021 edition

## Enables
- No downstream concepts directly

## Related
- **prelude-2024** -- the 2024 edition further expands the prelude
- **edition-migration** -- `cargo fix --edition` handles the automated migration

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Assuming that all calls to `try_into()`, `try_from()`, or `from_iter()` will break.
  **Correction**: Only calls that are ambiguous between a custom trait and the new prelude trait will break. Inherent methods always take precedence, and calls via fully qualified syntax are unaffected.

- **Error**: Not understanding why `(&*f).try_into()` resolves the ambiguity for `dyn Trait`.
  **Correction**: The dereference changes the receiver type from `Box<dyn MyTrait>` to `dyn MyTrait`, which ensures the `dyn MyTrait` method is selected. Without the dereference, method resolution considers both `TryInto::try_into` (from prelude) and `MyTrait::try_into`.

# Common Confusions

- **Confusion**: Thinking that adding any item to the prelude requires an edition.
  **Clarification**: Adding types, functions, or constants to the prelude is generally safe because manual imports shadow prelude items. Only adding traits can cause breakage through ambiguous method resolution, which is why the prelude trait additions were tied to an edition.

- **Confusion**: Thinking inherent methods with the same name as prelude traits need migration.
  **Clarification**: Inherent methods always take priority over trait methods during method resolution. If your type has an inherent `try_into` method, it will continue to be called, even with `TryInto` in the prelude.

# Source Reference

Chapter 4: Rust 2021, "Additions to the prelude" section. The tracking issue is rust-lang/rust#85684. The section covers the three new traits, the reason an edition is required, and detailed migration guidance including conflicting trait methods, dyn Trait objects, inherent methods, and implementation reference for the lint.

# Verification Notes

- Definition source: Direct quotation from "Additions to the prelude" section, "Details" subsection
- Key Properties: All from explicit statements in the source
- Confidence rationale: HIGH -- the source provides comprehensive documentation of the change, its motivation, and migration paths
- Uncertainties: None
- Cross-reference status: prelude-2024 references Agent C's extraction; other slugs are in this set or Agent A's set
