---
# === CORE IDENTIFICATION ===
concept: Rustdoc Search
slug: rustdoc-search

# === CLASSIFICATION ===
category: documentation
subcategory: navigation
tier: intermediate

# === PROVENANCE ===
source: "Rustdoc Book"
source_slug: rustdoc
authors: "The Rust Project"
chapter: "How to read rustdoc output"
chapter_number: 3
pdf_page: null
section: "Rustdoc search"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rustdoc type search"
  - "rustdoc search by name"
  - "rustdoc search by type signature"
  - "doc search syntax"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - reading-rustdoc-output
extends: []
related:
  - rustdoc
  - rustdoc-advanced-features
  - doc-attribute
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I search for items in rustdoc documentation?"
  - "How does rustdoc's type-based search work?"
  - "What is the syntax for searching by function signature?"
  - "How do I filter search results to a specific item type?"
  - "How does fuzzy matching work in rustdoc search?"
  - "Can I search for functions that take a specific type and return another?"
  - "What wrapper types can be omitted in type-based search?"
  - "How do I search for functions that take closures as parameters?"
  - "What are the special syntax shortcuts for primitives in search?"
  - "What are the limitations of type-based search?"
---

# Quick Definition

Rustdoc's search feature supports two modes: name-based search (with fuzzy matching and path support) and type-signature-based search (matching parameters and return types). Searches execute instantly as you type. Name-based search includes tabs for "In Names," "In Parameters," and "In Return Types." Type-based search supports generics, trait bounds, associated types, nested signatures, and special primitive syntax.

# Core Definition

As stated in the source: "Typing in the search bar instantly searches the available documentation, matching either the name and path of an item, or a function's approximate type signature." (Ch. 3: Rustdoc search).

**Name-based search** matches item names and paths. Path separators (`::`) can be replaced with spaces -- `vec new` and `vec::new` both find `std::vec::Vec::new`. Rustdoc uses fuzzy matching based on the length of the typed name (e.g., `HahsMap` finds `HashMap`). Wrapping a term in quotes disables fuzzy matching for exact searches. Results appear in three tabs: "In Names," "In Parameters," and "In Return Types."

**Type-signature-based search** allows querying by parameter and return types. Parameters are separated by commas, and return types follow `->`. The search is order-agnostic for parameters but sensitive to nesting. Items can be left out of the query but items present in the query must exist in the function. The `self` parameter is treated like any other, and `Self` resolves to the underlying type. If a named type is not found in the docs, it is treated as a generic type parameter.

Type-based search supports generics with angle brackets, associated types (with optional `=Name` syntax), closures wrapped in parentheses, and special shorthand syntax for primitives like references (`&`, `&mut`), slices/arrays (`[]`, `[T]`), tuples (`(T, U)`), the never type (`!`), and function types (`(T, U -> V, W)`).

# Prerequisites

- **reading-rustdoc-output** -- Understanding the rustdoc page structure and search interface location

# Key Properties

1. **Instant search**: Results appear as you type with no page reload
2. **Dual mode**: Name-based search with fuzzy matching, and type-signature-based search with structural matching
3. **Path as spaces**: `::` separators can be replaced with whitespace -- `Vec new` equals `Vec::new`
4. **Three result tabs**: "In Names" (default), "In Parameters," and "In Return Types"
5. **Fuzzy matching**: Tolerates typos based on name length; disable with quotes (`"HahsMap"` returns nothing)
6. **Order-agnostic parameters**: Function parameter types match regardless of order in the query
7. **Nesting-sensitive**: `Result<Vec<u8>, Error>` and `Result<Error, Vec<u8>>` are different queries
8. **Wrapper omission**: References, Box, Rc, Arc, Option, Result, From, Into, and Future can be omitted from queries
9. **Item type filtering**: Prefix with a type filter and colon (e.g., `mod:`, `struct:`, `fn:`, `macro:`) or append `!` for macros
10. **Non-function search**: Struct fields are treated as getter methods; `const`/`static` items as nullary functions
11. **Generic inference**: Unknown type names in queries are treated as generic type parameters

# Construction / Recognition

## Name-Based Search:
```
vec new              -> finds Vec::new
vec::new             -> finds Vec::new
std::vec::Vec        -> finds the Vec struct
"HashMap"            -> exact match only (no fuzzy)
println!             -> searches for macro println
macro:println        -> same as above with type filter
```

## Type-Signature-Based Search:
```
usize -> vec                              -> slice::repeat, Vec::with_capacity
vec, vec -> bool                          -> Vec::eq
option<T>, fnonce -> option<U>            -> Option::map, Option::and_then
option<T>, (T -> bool) -> option<T>       -> Option::filter
option -> default                         -> Option::unwrap_or_default
stdout, [u8]                              -> Stdout::write
any -> !                                  -> panic::panic_any
vec::intoiter<T> -> [T]                   -> IntoIter::as_slice
iterator<T>, fnmut -> T                   -> Iterator::reduce, Iterator::find
Iterator<T>, (T -> bool) -> bool          -> Iterator::all
```

## Primitive Shorthand:
| Shorthand | Meaning |
|-----------|---------|
| `&` | `primitive:reference` |
| `&mut T` | `primitive:reference<keyword:mut, T>` |
| `[T]` | `primitive:slice<T>` and/or `primitive:array<T>` |
| `()` | `primitive:unit` and/or `primitive:tuple` |
| `!` | `primitive:never` |
| `(T, U -> V, W)` | `fn(T, U) -> (V, W)`, plus Fn/FnMut/FnOnce |

## Item Type Filters:
`mod:`, `struct:`, `enum:`, `fn:`, `type:`, `trait:`, `macro:`, `static:`, `method:`, `primitive:`, `keyword:`, `generic:`, and many more.

# Context & Application

Rustdoc search is one of the most powerful features of Rust's documentation ecosystem. Type-based search is particularly valuable when you know what types you have and what type you need but do not know the function name -- a common scenario when exploring unfamiliar libraries. The search works on docs.rs, the standard library documentation, and any locally generated rustdoc output. Custom search engine templates can be configured in browsers using `https://doc.rust-lang.org/stable/std/?search=%s` (covered in the advanced features chapter). The crate filter dropdown below the search bar restricts results to a specific crate.

# Examples

**Example 1** (Ch. 3): Fuzzy matching with auto-correction:
> Searching for `HahsMap` finds `HashMap` because "Rustdoc uses a fuzzy matching function that can tolerate typos for this, though it's based on the length of the name that's typed in." The "In Parameters" and "In Return Types" tabs auto-correct to `hashmap` and show functions that use `HashMap`.

**Example 2** (Ch. 3): Type-based search with generics and associated types:
```rust
pub trait MyTrait {
    type First;
    type Second;
}
pub fn my_fn(x: impl MyTrait<First=u8, Second=u32>) -> bool { true }
```
This function matches `MyTrait<First=u8, Second=u32> -> bool` and `MyTrait<Second=u32> -> bool` but does *not* match `MyTrait<First=u32> -> bool` or `MyTrait<u32, u32> -> bool`.

**Example 3** (Ch. 3): Progressively looser generic queries:
A function `fn my_function<I: Iterator<Item=u32>>(input: I) -> usize` matches all of:
- `Iterator<Item=u32> -> usize`
- `Iterator<u32> -> usize` (leave out `Item=`)
- `Iterator -> usize` (leave out generic entirely)
- `T -> usize` (match with generic parameter)

**Example 4** (Ch. 3): Non-function items in type search:
> "Struct fields are treated as though they were getter methods. This means that a search for `CpuidResult -> u32` will show the `CpuidResult::eax` field in the results."
> "Additionally, `const` and `static` items are treated as nullary functions, so `-> u32` will match `u32::MAX`."

**Example 5** (Ch. 3): Closure parameter search:
> "To search for a function that accepts a function as a parameter, like `Iterator::all`, wrap the nested signature in parenthesis, as in `Iterator<T>, (T -> bool) -> bool`."

# Relationships

## Builds Upon
- **reading-rustdoc-output** -- search is one of the three main sections of the output

## Enables
- None directly -- search is a terminal user-facing feature

## Related
- **rustdoc** -- the tool that generates the searchable output
- **rustdoc-advanced-features** -- `#[doc(alias)]` adds extra search terms for items; custom search engine URLs
- **doc-attribute** -- `#[doc(alias = "...")]` affects search results

## Contrasts With
- None within this source

# Common Errors

- **Error**: Writing `Result<Vec, u8>` expecting to match `Result<Vec<u8>, Error>`.
  **Correction**: Nesting matters. `Vec<u8>` must be nested correctly inside `Result`. `Result<Vec<u8>>` works because items can be left out (omitting `Error`), but `Result<Vec, u8>` has incorrect nesting.

- **Error**: Searching for `Read -> u8` expecting to match `fn read_all(&mut self: impl Read) -> Result<Vec<u8>, Error>`.
  **Correction**: Only certain wrapper types (Reference, Box, Rc, Arc, Option, Result, From, Into, Future) can be omitted. `Vec` is not one of them, so `Vec<u8>` cannot be simplified to just `u8`.

- **Error**: Expecting `option<T> -> T where T: Default` to work as a query.
  **Correction**: "There's no way to write trait constraints on generic parameters." Use `option<Default> -> Default` instead.

# Common Confusions

- **Confusion**: Thinking type parameters and concrete types are interchangeable in queries.
  **Clarification**: "Type parameters match type parameters... but never match concrete types in function signatures." A query with `T` matches generic parameters but not concrete `i32`. A trait name like `Read` matches type parameters constrained by that trait, as well as `dyn Trait` and `impl Trait`.

- **Confusion**: Thinking `Result<Error, Vec<u8>>` and `Result<Vec<u8>, Error>` match the same functions.
  **Clarification**: While function *parameters* are order-agnostic, *nesting within a generic type* is order-sensitive. The position of type arguments within Result (or any generic) matters.

- **Confusion**: Thinking `(T)` only matches the type `T` itself.
  **Clarification**: Since parentheses act as grouping, `(u32)` also matches tuples like `(u32,)` for the same reason it matches `Result<u32, Error>` -- items can be left out of queries.

- **Confusion**: Thinking type-based search is fully mature and reliable.
  **Clarification**: The source explicitly states "Type-based search is still a buggy, experimental, work-in-progress feature." Supertraits, type aliases, and Deref are all ignored; searching for lifetimes and array lengths is not supported.

# Source Reference

Chapter 3: How to read rustdoc output -- "Rustdoc search" section including "Search By Name," "Searching By Type Signature," "Non-functions in type-based search," "How type-based search works," "Wrappers that can be omitted," "Primitives with Special Syntax," "Limitations and quirks," "Item filtering," and "Search query syntax." No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 3 -- "Typing in the search bar instantly searches the available documentation, matching either the name and path of an item, or a function's approximate type signature."
- Confidence rationale: HIGH -- the source provides extensive examples, formal grammar, and explicit documentation of limitations
- Uncertainties: Type-based search is described as experimental with known bugs; specific behavior may change
- Cross-reference status: reading-rustdoc-output, rustdoc, rustdoc-advanced-features are in this extraction set; doc-attribute from Agent B
