---
concept: API Flexibility Guidelines
slug: api-flexibility-guidelines
category: api-design
subcategory: null
tier: intermediate
source: "Rust API Guidelines"
source_slug: api-guidelines
authors: "The Rust Library Team"
chapter: "06-flexibility"
chapter_number: 6
pdf_page: null
section: "Flexibility"
extraction_confidence: high
aliases:
  - "rust flexibility guidelines"
  - "rust api flexibility"
  - "C-INTERMEDIATE C-CALLER-CONTROL C-GENERIC C-OBJECT"
prerequisites:
  - api-guidelines-overview
extends:
  - api-guidelines-overview
related:
  - api-predictability-guidelines
  - api-interoperability-guidelines
  - api-naming-guidelines
contrasts_with: []
answers_questions:
  - "Should functions expose intermediate results?"
  - "How should ownership be handled in function parameters?"
  - "When should functions use generics vs concrete types?"
  - "What makes a trait object-safe?"
  - "What are the tradeoffs between generics and trait objects?"
  - "How should Rust APIs handle data copying and placement?"
---

# Quick Definition

The Flexibility chapter of the Rust API Guidelines defines 4 guidelines (C-INTERMEDIATE, C-CALLER-CONTROL, C-GENERIC, C-OBJECT) ensuring crates support diverse real-world use cases. The central principle is that APIs should avoid unnecessary constraints: expose useful intermediate data, let callers control ownership and copying, use generics to minimize parameter assumptions, and make traits object-safe when trait objects would be useful.

# Core Definition

**C-INTERMEDIATE** -- Functions expose intermediate results to avoid duplicate work. When a function computes interesting data as a side effect of answering a question, expose that data rather than discarding it. `Vec::binary_search` returns the index where the value was found *or* the index where it would need to be inserted -- not just a bool. `String::from_utf8` returns the byte offset of the first invalid byte on error, plus ownership of the input bytes. `HashMap::insert` returns the previous value for the key, if any.

**C-CALLER-CONTROL** -- Caller decides where to copy and place data. If a function requires ownership, take ownership directly rather than borrowing and cloning:
```rust
// Prefer:
fn foo(b: Bar) { /* use b as owned */ }
// Over:
fn foo(b: &Bar) { let b = b.clone(); /* ... */ }
```
If a function does not require ownership, borrow rather than taking ownership and dropping:
```rust
// Prefer:
fn foo(b: &Bar) { /* use b as borrowed */ }
// Over:
fn foo(b: Bar) { /* use b as borrowed, drops before return */ }
```
The Copy trait should only be used as a bound when absolutely needed, not to signal that copies are cheap.

**C-GENERIC** -- Functions minimize assumptions about parameters by using generics. Prefer `fn foo<I: IntoIterator<Item = i64>>(iter: I)` over `fn foo(c: &[i64])` or `fn foo(c: &Vec<i64>)` when the function only needs to iterate. Generics provide: reusability across an open-ended collection of types, static dispatch with optimization, inline layout in structs/enums, type inference reducing verbosity, and precise types guaranteeing consistency. Tradeoffs include code size from monomorphization, homogeneous type constraints, and signature verbosity.

**C-OBJECT** -- Traits are object-safe if they may be useful as a trait object. Decide early whether a trait will be used as an object or as a generic bound. If meant for use as an object, methods should take and return trait objects rather than using generics. Generic methods can be excluded from the trait object with `where Self: Sized`:
```rust
trait MyTrait {
    fn object_safe(&self, i: i32);
    fn not_object_safe<T>(&self, t: T) where Self: Sized;
}
```
Trait object advantages: heterogeneity and reduced code size. Disadvantages: no generic methods, dynamic dispatch overhead, no Self (except in receiver position).

# Prerequisites

- **api-guidelines-overview** -- understanding the overall guidelines framework

# Key Properties

1. Intermediate results avoid forcing callers to duplicate expensive computations
2. Ownership in function signatures should match actual ownership requirements -- no unnecessary cloning or dropping
3. Generics enable static dispatch, inline layout, type inference, and precise type matching
4. Generic tradeoffs include code bloat from monomorphization and signature complexity
5. Object safety requires no generic methods and no Self except in receiver position
6. `where Self: Sized` can selectively exclude methods from trait objects while keeping the trait object-safe
7. The Copy bound should reflect a genuine requirement, not a hint about performance

# Construction / Recognition

## Applying the Flexibility Guidelines:
1. **Intermediate results** (C-INTERMEDIATE): When a function computes useful data as a byproduct, include it in the return type. Prefer `Result<(Success, Metadata), (Error, Metadata)>` patterns over discarding the metadata
2. **Ownership alignment** (C-CALLER-CONTROL): Audit each parameter -- does the function actually consume it? If yes, take by value. If no, take by reference. Never clone inside a function when the caller could pass an owned value
3. **Generics** (C-GENERIC): For each concrete parameter type, ask: what trait bounds does this function actually need? Replace concrete types with generic bounds (e.g., `AsRef<Path>` instead of `&Path`, `IntoIterator` instead of `&[T]`)
4. **Object safety** (C-OBJECT): If the trait might be used as `dyn Trait`, ensure all methods are object-safe. Move non-object-safe methods behind `where Self: Sized`

## Generics vs Trait Objects Decision Framework:
- **Use generics when**: you need static dispatch and optimization, types are homogeneous, and code size is not critical
- **Use trait objects when**: you need heterogeneous collections, want to reduce code size, and can accept the overhead of dynamic dispatch
- **Combine both**: Keep the trait object-safe and use `where Self: Sized` to add generic convenience methods that are excluded from the trait object

# Context & Application

Flexibility is about respecting the diversity of real-world use cases. No API author can predict all the ways their library will be used. By exposing intermediate results, callers avoid redundant work. By letting callers control ownership, the API avoids forcing clones where moves suffice. By using generics, the API accepts a wider range of input types. By maintaining object safety, traits can be used both statically and dynamically.

The `std::fs::File::open` function demonstrates C-GENERIC in practice: it accepts `AsRef<Path>`, so callers can pass `"f.txt"` (a string literal), a `Path`, an `OsString`, or any other type that converts to a path reference.

# Examples

**Example 1** (C-INTERMEDIATE): `Vec::binary_search` returns `Result<usize, usize>` -- the `Ok` variant gives the found index, and the `Err` variant gives the insertion point. This avoids callers needing a separate search to find where to insert.

**Example 2** (C-INTERMEDIATE): `String::from_utf8` returns an error that exposes both the byte offset of invalid UTF-8 and ownership of the input bytes, so the caller can recover the allocation rather than losing it.

**Example 3** (C-INTERMEDIATE): `HashMap::insert` returns `Option<V>` containing the previous value for the key. Without this, the caller would need a separate lookup to check for and retrieve the old value.

**Example 4** (C-GENERIC): Prefer generic iteration:
```rust
fn foo<I: IntoIterator<Item = i64>>(iter: I) { /* ... */ }
```
Over concrete types:
```rust
fn foo(c: &[i64]) { /* ... */ }
fn foo(c: &Vec<i64>) { /* ... */ }
```
The generic version accepts vectors, slices, ranges, hash set drains, and any other iterator of i64.

**Example 5** (C-OBJECT): The `io::Read` and `io::Write` traits are designed for use as trait objects. The `Iterator` trait marks generic methods with `where Self: Sized` to retain the ability to use `Iterator` as a trait object while still providing convenience methods for static dispatch.

**Example 6** (C-GENERIC): `std::fs::File::open` takes `AsRef<Path>`, allowing files to be opened from a string literal `"f.txt"`, a `Path`, or an `OsString`.

# Relationships

## Builds Upon
- **api-guidelines-overview** -- this is one of the 10 guideline categories

## Enables
- APIs that serve diverse use cases without forcing callers into specific patterns
- Callers that avoid redundant computation through exposed intermediate results
- Libraries usable in both generic and dynamic dispatch contexts

## Related
- **api-predictability-guidelines** -- C-METHOD and C-NO-OUT complement C-CALLER-CONTROL (ownership and return values)
- **api-interoperability-guidelines** -- C-CONV-TRAITS relates to C-GENERIC (accepting generic conversion parameters)
- **api-naming-guidelines** -- C-CONV naming conventions apply to the generic parameters discussed here

## Contrasts With
- APIs that return only boolean success/failure, discarding intermediate data
- APIs that clone internally rather than letting callers control data placement
- APIs that accept only concrete types (e.g., `&Vec<T>`) instead of generic bounds

# Common Errors

- **Error**: Returning a `bool` from a search function instead of the found index or insertion point.
  **Correction**: Return `Result<usize, usize>` or similar rich type that exposes useful intermediate data.

- **Error**: Accepting `&Bar` and cloning internally when the function actually needs ownership.
  **Correction**: Take `Bar` by value. Let the caller decide whether to clone or move.

- **Error**: Accepting `&Vec<T>` or `&String` as function parameters.
  **Correction**: Use `&[T]` or `&str` for borrowed access, or `impl IntoIterator<Item = T>` / `impl AsRef<str>` for maximum flexibility.

# Common Confusions

- **Confusion**: Thinking generics are always better than trait objects.
  **Clarification**: Generics and trait objects serve different needs. Generics provide static dispatch and precise types but increase code size and require homogeneous types. Trait objects enable heterogeneity and reduce code size but incur dynamic dispatch overhead and cannot use generic methods.

- **Confusion**: Thinking `where Self: Sized` removes a method from the trait entirely.
  **Clarification**: `where Self: Sized` only excludes the method from the trait object. The method is still available when the trait is used as a generic bound with a concrete type.

- **Confusion**: Using the Copy bound to hint that copies are cheap.
  **Clarification**: Copy should only be used as a bound when the function genuinely requires it. The ability to copy is a semantic requirement, not a performance annotation.

# Source Reference

Chapter 6: Flexibility. All 4 guidelines (C-INTERMEDIATE, C-CALLER-CONTROL, C-GENERIC, C-OBJECT) are covered with examples from the standard library (Vec::binary_search, String::from_utf8, HashMap::insert, File::open, io::Read, io::Write, Iterator) and detailed discussion of generics vs trait objects tradeoffs.

# Verification Notes

- Definition: All guideline descriptions drawn directly from the chapter text
- Key Properties: Extracted from explicit rationale and the advantages/disadvantages lists in C-GENERIC and C-OBJECT
- Confidence: HIGH -- the flexibility guidelines include extensive examples and tradeoff analysis
- Uncertainties: None -- the guidelines are well-defined with concrete examples
- Cross-reference status: All slugs reference cards in this extraction set
