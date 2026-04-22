---
concept: API Naming Guidelines
slug: api-naming-guidelines
category: api-design
subcategory: null
tier: foundational
source: "Rust API Guidelines"
source_slug: api-guidelines
authors: "The Rust Library Team"
chapter: "01-naming"
chapter_number: 1
pdf_page: null
section: "Naming"
extraction_confidence: high
aliases:
  - "rust naming conventions"
  - "api naming conventions"
  - "C-CASE C-CONV C-GETTER C-ITER C-ITER-TY C-FEATURE C-WORD-ORDER"
prerequisites:
  - api-guidelines-overview
extends:
  - api-guidelines-overview
related:
  - api-predictability-guidelines
  - api-interoperability-guidelines
contrasts_with: []
answers_questions:
  - "How should I name types, functions, and methods in Rust?"
  - "What are the as_, to_, into_ conversion naming conventions?"
  - "How should getters be named in Rust?"
  - "What should iterator methods and types be named?"
  - "How should Cargo feature names be chosen?"
  - "What word order should Rust type names use?"
---

# Quick Definition

The Naming chapter of the Rust API Guidelines defines 7 guidelines (C-CASE, C-CONV, C-GETTER, C-ITER, C-ITER-TY, C-FEATURE, C-WORD-ORDER) governing how types, functions, methods, conversions, iterators, features, and error types should be named. Consistent naming enables Rust code to be readable and predictable across the ecosystem.

# Core Definition

**C-CASE** -- Casing conforms to RFC 430: `UpperCamelCase` for types and traits, `snake_case` for functions and methods, `SCREAMING_SNAKE_CASE` for statics and constants. Acronyms count as one word: `Uuid` not `UUID`, `Usize` not `USize`. In snake_case, a word should never be a single letter unless it is the last word: `btree_map` not `b_tree_map`. Crate names should not use `-rs` or `-rust` as a suffix or prefix.

**C-CONV** -- Ad-hoc conversions follow `as_`/`to_`/`into_` conventions based on cost and ownership:
- `as_`: Free cost, borrowed to borrowed (e.g., `str::as_bytes()`)
- `to_`: Expensive, borrowed to borrowed or borrowed to owned (e.g., `str::to_lowercase()`)
- `into_`: Variable cost, owned to owned for non-Copy types (e.g., `String::into_bytes()`)

Conversions prefixed `as_` and `into_` typically decrease abstraction. Conversions prefixed `to_` typically stay at the same abstraction level but change representation. When a type wraps a single value, access should be via `into_inner()`.

**C-GETTER** -- The `get_` prefix is not used for getters. A field `first` has getter `fn first(&self)` and mutable getter `fn first_mut(&mut self)`. The bare `get` name is used only when there is a single obvious thing to get (e.g., `Cell::get`). Getters with runtime validation may offer `_unchecked` variants.

**C-ITER** -- Collection iterator methods follow `iter`/`iter_mut`/`into_iter` (per RFC 199), returning `Iterator<Item = &U>`, `Iterator<Item = &mut U>`, and `Iterator<Item = U>` respectively. This applies to homogeneous collections; nuanced types like `str` use domain-specific names (`bytes`, `chars`).

**C-ITER-TY** -- Iterator type names match their producing methods: `into_iter()` returns `IntoIter`, `iter()` returns `Iter`, `keys()` returns `Keys`. These names are most clear when prefixed with their owning module (e.g., `vec::IntoIter`).

**C-FEATURE** -- Feature names are free of placeholder words like `use-` or `with-`. Name the feature directly (e.g., `std` not `use-std`, `serde` not `with-serde`). This aligns with Cargo's implicit feature names for optional dependencies. Features named negatively like `no-abc` are practically never correct because Cargo requires features to be additive.

**C-WORD-ORDER** -- Names use a consistent word order. The standard library uses verb-object-error order: `ParseBoolError`, `ParseIntError`, `JoinPathsError`. The specific word order choice matters less than consistency within a crate and with similar standard library functionality.

# Prerequisites

- **api-guidelines-overview** -- understanding the overall guidelines framework and checklist structure

# Key Properties

1. RFC 430 defines the canonical casing rules; acronyms and contractions count as single words in CamelCase
2. The `as_`/`to_`/`into_` prefix system encodes both cost and ownership semantics into the method name
3. Getters omit the `get_` prefix (unlike many other languages), using bare field names
4. The `mut` qualifier in conversion names appears as it would in the return type: `as_mut_slice` not `as_slice_mut`
5. Iterator method/type name correspondence enables discoverability across the ecosystem
6. Feature names align with Cargo's implicit naming for optional dependencies
7. Word order consistency within a crate is more important than any specific word order choice

# Construction / Recognition

## Applying the Naming Guidelines:
1. **Casing** (C-CASE): Check all items against the RFC 430 table -- types/traits use UpperCamelCase, functions/methods use snake_case, constants/statics use SCREAMING_SNAKE_CASE, type parameters use concise UpperCamelCase (usually `T`), lifetimes use short lowercase (`'a`)
2. **Conversions** (C-CONV): For each conversion method, classify by cost and ownership to determine the correct prefix. Free borrows get `as_`, expensive operations get `to_`, consuming operations get `into_`
3. **Getters** (C-GETTER): Remove any `get_` prefixes from field accessors. Add `_mut` suffix for mutable variants. Consider `_unchecked` unsafe variants for validated getters
4. **Iterators** (C-ITER, C-ITER-TY): Ensure collection types provide the standard `iter`/`iter_mut`/`into_iter` trio with matching return type names
5. **Features** (C-FEATURE): Audit Cargo.toml features for placeholder words; rename `use-foo` or `with-foo` to just `foo`
6. **Word order** (C-WORD-ORDER): Survey existing names for a pattern and apply it consistently

# Context & Application

Naming is one of the most visible aspects of API design. Users encounter names constantly, and inconsistent naming creates cognitive overhead. The Rust ecosystem benefits from strong naming conventions because:
- Conversion prefixes communicate ownership and cost without reading documentation
- Iterator naming enables pattern-matching across different collection types
- Consistent casing makes it possible to determine the kind of item from its name alone
- Feature naming conventions prevent ecosystem fragmentation

The `as_`/`to_`/`into_` convention is particularly important because it communicates ownership transfer semantics at a glance -- critical information in Rust's ownership system.

# Examples

**Example 1** (C-CONV): `str::as_bytes()` gives a view of a `str` as `&[u8]`, which is free -- input is borrowed `&str`, output is borrowed `&[u8]`. `Path::to_str` performs an expensive UTF-8 check, so it would be incorrect to call it `as_str`. `String::into_bytes()` extracts the underlying `Vec<u8>`, taking ownership -- it consumes the `String`.

**Example 2** (C-CONV): `f64::to_radians()` converts degrees to radians. Even though `f64` is Copy, calling it `into_radians` would be misleading because the input is not consumed. The `to_` prefix is correct because it performs a non-trivial computation at the same abstraction level.

**Example 3** (C-GETTER): A struct `S` with field `first` provides `fn first(&self) -> &First` (not `get_first`) and `fn first_mut(&mut self) -> &mut First` (not `get_first_mut` or `get_mut_first`).

**Example 4** (C-FEATURE): The canonical way to provide an optional std dependency: feature named `std` (not `use-std`), matching Cargo's implicit feature naming for optional dependencies like `serde`.

**Example 5** (C-WORD-ORDER): Standard library error types follow verb-object-error order: `ParseBoolError`, `ParseFloatError`, `JoinPathsError`, `StripPrefixError`. A new address parsing error should be `ParseAddrError`, not `AddrParseError`.

# Relationships

## Builds Upon
- **api-guidelines-overview** -- this is one of the 10 guideline categories

## Enables
- **api-predictability-guidelines** -- consistent naming makes code behavior predictable
- **api-interoperability-guidelines** -- standard conversion names enable ecosystem interop

## Related
- RFC 430 (finalizing naming conventions)
- RFC 199 (ownership variants for iterator methods)

## Contrasts With
- Languages that use `get_`/`set_` prefixes for all accessors (Java, C#)
- Languages without ownership-aware naming (the `as_`/`to_`/`into_` system is unique to Rust)

# Common Errors

- **Error**: Using `get_` prefix on field accessors (e.g., `get_name()` instead of `name()`).
  **Correction**: Rust convention omits `get_`. Use bare field names for getters and append `_mut` for mutable access.

- **Error**: Using `as_` for an expensive conversion (e.g., `as_str` for something that requires UTF-8 validation).
  **Correction**: The `as_` prefix implies zero-cost borrowing. Use `to_` for operations with non-trivial cost.

- **Error**: Naming a Cargo feature `use-serde` or `with-serde` instead of just `serde`.
  **Correction**: Feature names should match the bare dependency name, aligning with Cargo's implicit feature naming.

# Common Confusions

- **Confusion**: Thinking `to_` always means "borrowed to owned."
  **Clarification**: `to_` covers multiple ownership patterns including borrowed-to-borrowed (e.g., `Path::to_str`) and owned-to-owned for Copy types (e.g., `f64::to_radians`). The key distinction is that `to_` implies non-trivial cost, unlike `as_`.

- **Confusion**: Thinking `into_` always implies the operation is free.
  **Clarification**: `into_` has variable cost. `String::into_bytes()` is free, but `BufWriter::into_inner()` requires a potentially expensive flush. The key property of `into_` is consuming ownership, not being cheap.

- **Confusion**: Treating `as_mut_slice` vs `as_slice_mut` as arbitrary.
  **Clarification**: The `mut` qualifier appears as it would in the return type. Since the return type is `&mut [T]` (a "mut slice"), the name is `as_mut_slice`.

# Source Reference

Chapter 1: Naming. All 7 guidelines (C-CASE, C-CONV, C-GETTER, C-ITER, C-ITER-TY, C-FEATURE, C-WORD-ORDER) are covered with detailed explanations, rationale, and standard library examples.

# Verification Notes

- Definition: All guideline descriptions drawn directly from the chapter text
- Key Properties: Extracted from explicit statements in each guideline section
- Confidence: HIGH -- the naming guidelines are well-established and extensively documented with examples
- Uncertainties: C-CASE notes crate naming conventions are still "unclear" per linked issue
- Cross-reference status: All slugs reference cards in this extraction set
