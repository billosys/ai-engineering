---
concept: Collections Are Smart Pointers
slug: collections-as-smart-pointers
category: idiom
subcategory: null
tier: intermediate
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "Collections are smart pointers"
extraction_confidence: high
aliases:
  - "collections as smart pointers"
  - "Deref for collections"
  - "owning and borrowed views"
  - "collection Deref pattern"
prerequisites:
  - borrowed-types-for-arguments
extends:
  - borrowed-types-for-arguments
related:
  - default-trait
  - constructor-idiom
contrasts_with: []
answers_questions:
  - "How do collections relate to smart pointers in Rust?"
  - "Why does Vec<T> implement Deref<Target=[T]>?"
  - "What is the relationship between String and &str?"
  - "How does Deref enable borrowed views of collection data?"
  - "Why are most Vec methods actually defined on slices?"
---

# Quick Definition

Collections in Rust can be treated as smart pointers by implementing the `Deref` trait, which provides an owning view (the collection itself) and a borrowed view (a slice or reference). This is why `Vec<T>` derefs to `&[T]` and `String` derefs to `&str` -- most methods are defined on the borrowed view and become available on the owning type through auto-deref.

# Core Definition

"Use the `Deref` trait to treat collections like smart pointers, offering owning and borrowed views of data." (Ch. 1, "Collections are smart pointers")

"A `Vec<T>` is an owning collection of `T`s, while a slice (`&[T]`) is a borrowed collection of `T`s. Implementing `Deref` for `Vec` allows implicit dereferencing from `&Vec<T>` to `&[T]` and includes the relationship in auto-dereferencing searches. Most methods you might expect to be implemented for `Vec`s are instead implemented for slices."

"Smart pointers and collections are analogous: a smart pointer points to a single object, whereas a collection points to many objects. From the point of view of the type system, there is little difference between the two." (Discussion)

# Prerequisites

- **borrowed-types-for-arguments** -- understanding borrowed types (`&str`, `&[T]`) is essential to understanding what the Deref target represents

# Key Properties

1. A collection owns its data; a slice/reference is a borrowed view of that data
2. Implementing `Deref` for a collection enables implicit dereferencing from the owned type to the borrowed view
3. `Vec<T>` implements `Deref<Target=[T]>`, so `&Vec<T>` auto-derefs to `&[T]`
4. `String` implements `Deref<Target=str>`, so `&String` auto-derefs to `&str`
5. Most methods are implemented on the borrowed view (slice), not on the collection itself
6. Auto-deref means those slice methods are automatically available on the owning collection
7. Ordered collections typically implement `Index` for `Range` types to provide slicing syntax
8. The Deref target can be a custom dynamically sized type (not limited to built-in types like `[T]` and `str`)

# Construction / Recognition

## To Implement This Pattern:
1. Define your owning collection type `Foo<T>`
2. Define or identify the borrowed view type `Bar<T>` (a DST or reference type)
3. Implement `Deref<Target=Bar<T>>` for `Foo<T>`
4. Implement methods on `Bar<T>` -- they become available on `Foo<T>` via auto-deref
5. Optionally implement `Index` with `Range` targets for slicing syntax

## Standard Library Examples:
- `Vec<T>` -> `Deref<Target=[T]>`
- `String` -> `Deref<Target=str>`
- `Box<T>` -> `Deref<Target=T>`
- `Arc<T>` -> `Deref<Target=T>`

```rust,ignore
use std::ops::Deref;

struct Vec<T> {
    data: RawVec<T>,
    //..
}

impl<T> Deref for Vec<T> {
    type Target = [T];

    fn deref(&self) -> &[T] {
        //..
    }
}
```

# Context & Application

This pattern is fundamental to Rust's approach to ownership and borrowing in data structures. By separating the owning view (collection) from the borrowed view (slice), Rust achieves two goals: the collection manages memory (allocation, deallocation), while the slice provides a lightweight, non-owning reference for reading data.

**Typical contexts:**
- Designing custom collection types that need to expose a borrowed view
- Understanding why `Vec` methods are found in the `[T]` (slice) documentation
- Building APIs that accept `&[T]` or `&str` and work with both owned and borrowed data

**Design motivation:** "Ownership and borrowing are key aspects of the Rust language. Data structures must account for these semantics properly to give a good user experience. When implementing a data structure that owns its data, offering a borrowed view of that data allows for more flexible APIs."

# Examples

**Example 1** (Ch. 1, "Collections are smart pointers"): The `Vec<T>` / `[T]` relationship:

```rust,ignore
use std::ops::Deref;

struct Vec<T> {
    data: RawVec<T>,
    //..
}

impl<T> Deref for Vec<T> {
    type Target = [T];

    fn deref(&self) -> &[T] {
        //..
    }
}
```

"Most methods you might expect to be implemented for `Vec`s are instead implemented for slices." This means methods like `.iter()`, `.len()`, `.contains()`, and indexing operations are defined on `[T]` and available on `Vec<T>` through auto-deref.

**Example 2** (Ch. 1): The source notes that "Also `String` and `&str` have a similar relation" -- `String` owns the data and derefs to `str`, so string methods like `.chars()`, `.len()`, `.starts_with()` are defined on `str` and available on `String`.

# Relationships

## Builds Upon
- **borrowed-types-for-arguments** -- this pattern is the mechanism that makes the borrowed-types idiom work

## Enables
- Flexible APIs that accept borrowed views
- The "most methods on slice" design pattern in the standard library

## Related
- **default-trait** -- collections typically implement `Default` (empty collection)
- **constructor-idiom** -- collections follow the `new()` convention

## Contrasts With
- **Deref polymorphism anti-pattern** -- the source links to the anti-pattern of misusing Deref for inheritance-like behavior (see anti_patterns/deref.md)

# Common Errors

- **Error**: Implementing methods on the owning collection when they could be on the borrowed view.
  **Correction**: "Most methods can be implemented only for the borrowed view, they are then implicitly available for the owning view." Put methods on the Deref target type.

- **Error**: Using `Deref` to simulate inheritance between unrelated types.
  **Correction**: `Deref` is for smart-pointer/collection relationships where there is a genuine owning-to-borrowed relationship. Misuse is documented as the "Deref polymorphism" anti-pattern.

# Common Confusions

- **Confusion**: Thinking `Deref` methods are taken into account during generic bounds checking.
  **Clarification**: "Methods and traits only available via dereferencing are not taken into account when bounds checking, so generic programming with data structures using this pattern can get complex (see the `Borrow` and `AsRef` traits, etc.)." This is a real limitation.

- **Confusion**: Thinking any custom type should implement `Deref`.
  **Clarification**: `Deref` should only be implemented when there is a natural owning-to-borrowed relationship. The `Foo<T>` -> `Bar<T>` pattern should mean "Foo owns the data, Bar borrows it." Arbitrary Deref implementations violate user expectations.

# Source Reference

Chapter 1: Idioms, "Collections are smart pointers" section. Covers Description, Example, Motivation, Advantages, Disadvantages, Discussion, and See Also. The Discussion section provides the smart-pointer/collection analogy and notes on custom Deref targets and Index for slicing. See also: Deref trait documentation, Deref polymorphism anti-pattern.

# Verification Notes

- Definition: Direct quotation from the Description and Discussion subsections
- Key Properties: All from explicit statements in the source
- Examples: Code example directly from the source; String/str relationship mentioned explicitly
- Confidence: HIGH -- the source provides thorough description with code, motivation, advantages, disadvantages, and discussion
- Uncertainties: None
- Cross-reference status: All slugs reference cards in this extraction set
