---
concept: Rust Common Collections
slug: rust-collections
category: language-fundamentals
subcategory: data-structures
tier: foundational
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "08 - Common Collections"
chapter_number: 8
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Vec"
  - "vectors"
  - "String"
  - "strings"
  - "HashMap"
  - "hash map"
  - "collections"
  - "vec! macro"
  - "entry API"
  - "UTF-8 strings"
prerequisites:
  - rust-enums-and-matching
  - rust-structs
extends: []
related:
  - rust-enums-and-matching
  - rust-error-handling
  - rust-module-system
contrasts_with: []
answers_questions:
  - "How do I create and use vectors in Rust?"
  - "What is the difference between indexing and .get() for vector access?"
  - "Why can't I hold a reference to a vector element while pushing?"
  - "How do I store multiple types in a vector?"
  - "What is the difference between String and &str?"
  - "Why doesn't Rust allow indexing into a String?"
  - "What are bytes, scalar values, and grapheme clusters?"
  - "How do I create and use a HashMap?"
  - "How does ownership work with HashMap insertion?"
  - "What is the entry API for hash maps?"
  - "How do I concatenate strings in Rust?"
---

# Quick Definition

Rust's three most commonly used collections are `Vec<T>` (a growable array of same-typed values stored on the heap), `String` (a growable UTF-8 encoded string built on `Vec<u8>`), and `HashMap<K, V>` (a key-value store using SipHash). Unlike arrays and tuples, collections store data on the heap and can grow or shrink at runtime. Each interacts with Rust's ownership and borrowing rules in important ways.

# Core Definition

**`Vec<T>`** (vector) stores a variable number of values of the same type contiguously in heap memory. Create with `Vec::new()` (requires type annotation) or the `vec!` macro (infers type from values). Add elements with `.push()`, which requires the vector to be `mut`. Access elements by indexing with `&v[index]` (panics on out-of-bounds) or `.get(index)` (returns `Option<&T>`, returning `None` for out-of-bounds). The borrow checker prevents holding an immutable reference to a vector element while pushing, because `push` may reallocate the entire vector, invalidating existing references. Iterate with `for item in &v` (immutable) or `for item in &mut v` (mutable, using `*item` to dereference). To store multiple types, use an enum as the element type. When a vector goes out of scope, it and all its elements are dropped.

**`String`** is a growable, mutable, owned, UTF-8 encoded string type wrapping `Vec<u8>`. The core language has only `&str` (string slices). Create with `String::new()`, `String::from("text")`, or `"text".to_string()`. Append with `.push_str(&str)` (appends a slice, does not take ownership) or `.push(char)` (single character). Concatenate with the `+` operator (which calls `fn add(self, s: &str) -> String` -- moves the first operand and borrows the second via deref coercion) or the `format!` macro (uses references, no ownership transfer, cleaner for multiple strings).

Rust **does not allow indexing into `String`** with `s[0]` because: (1) UTF-8 characters vary in byte width (1-4 bytes), so a byte index may not correspond to a character boundary; (2) there are three valid interpretations of string data -- bytes, Unicode scalar values (`char`), and grapheme clusters; (3) indexing is expected to be O(1) but finding the nth character requires scanning. Strings can be sliced with ranges (`&s[0..4]`), but this panics at runtime if the range does not fall on a character boundary. Iterate over characters with `.chars()` or over raw bytes with `.bytes()`. Grapheme cluster iteration requires an external crate.

**`HashMap<K, V>`** stores key-value pairs using a hashing function (SipHash by default, chosen for DoS resistance). Unlike `Vec` and `String`, `HashMap` is not in the prelude and must be imported: `use std::collections::HashMap;`. There is no built-in macro for construction. Create with `HashMap::new()` and add entries with `.insert(key, value)`. Access values with `.get(&key)`, which returns `Option<&V>`. For owned types like `String`, `.insert()` moves the values and the hash map takes ownership; for `Copy` types like `i32`, values are copied. Iterate with `for (key, value) in &map` (arbitrary order).

The **entry API** (`.entry(key)`) returns an `Entry` enum representing a value that may or may not exist. `.entry(key).or_insert(default)` inserts the default only if the key is absent and returns a mutable reference to the value. This is the idiomatic way to insert-if-absent or update-based-on-old-value (e.g., word counting).

# Prerequisites

- **Enums** (Ch. 6): `Option<T>` is returned by `.get()` methods; enums are used to store multiple types in a vector
- **Structs** (Ch. 5): Collections are struct types with methods; ownership of struct fields applies to collection elements

# Key Properties

1. All three collections store data on the heap; their size is not known at compile time
2. `Vec::new()` requires type annotation; `vec![1, 2, 3]` infers the type
3. Vector `[]` indexing panics on out-of-bounds; `.get()` returns `Option<&T>`
4. You cannot hold an immutable reference to a vector element while pushing (borrow checker prevents dangling references from reallocation)
5. Vectors drop all their elements when they go out of scope
6. `String` is a wrapper around `Vec<u8>` with UTF-8 guarantees
7. `String::from()` and `.to_string()` do the same thing; which to use is a matter of style
8. The `+` operator moves the first `String` operand (via `add(self, &str)`); `format!` takes only references
9. String indexing with `s[n]` is not allowed; use `.chars()`, `.bytes()`, or range slicing
10. Range slicing (`&s[0..4]`) panics if it does not fall on a UTF-8 character boundary
11. `HashMap` is not in the prelude; it must be `use`d from `std::collections`
12. `HashMap` keys and values must each be homogeneous (all keys same type, all values same type)
13. The entry API (`.entry().or_insert()`) is the idiomatic way to conditionally insert or update
14. `HashMap` uses SipHash by default for DoS resistance; alternate hashers implement `BuildHasher`

# Construction / Recognition

## Working with Vectors

1. Create: `let v: Vec<i32> = Vec::new();` or `let v = vec![1, 2, 3];`
2. Mutate: `v.push(value)` (requires `mut`), `v.pop()` removes and returns the last element
3. Safe access: `v.get(index)` returns `Option<&T>` -- handle `None` gracefully
4. Direct access: `&v[index]` returns a reference but panics on out-of-bounds
5. Iterate: `for i in &v { }` (read), `for i in &mut v { *i += 50; }` (modify)
6. Multiple types: define an enum, use `Vec<MyEnum>` as the vector type

## Working with Strings

1. Create: `String::new()`, `String::from("text")`, or `"literal".to_string()`
2. Append: `.push_str("slice")` or `.push('c')` for a single character
3. Concatenate: `s1 + &s2` (moves s1) or `format!("{s1}-{s2}-{s3}")` (no moves)
4. Iterate: `.chars()` for Unicode scalar values, `.bytes()` for raw bytes
5. Slice: `&s[0..4]` with caution -- must align to character boundaries

## Working with Hash Maps

1. Import: `use std::collections::HashMap;`
2. Create and insert: `let mut map = HashMap::new(); map.insert(key, value);`
3. Access: `map.get(&key)` returns `Option<&V>`; chain `.copied().unwrap_or(default)`
4. Conditional insert: `map.entry(key).or_insert(default_value);`
5. Update: `*map.entry(key).or_insert(0) += 1;` (word-counting pattern)

# Context & Application

Collections are the workhorse data structures for most Rust programs. They demonstrate Rust's ownership model in practice: vector reallocation invalidates references (enforced by the borrow checker), the `+` operator on strings moves the left operand, and `HashMap::insert` takes ownership of non-Copy keys and values.

The design of `String` reflects Rust's commitment to correctness: rather than allowing potentially invalid byte-level indexing, Rust forces programmers to choose their interpretation (bytes, chars, or grapheme clusters) explicitly. This prevents subtle bugs with non-ASCII text but requires more upfront thought.

The three-collection model (Vec, String, HashMap) covers the majority of use cases. The standard library offers additional collections (BTreeMap, HashSet, VecDeque, LinkedList, etc.) in `std::collections` for specialized needs.

# Examples

**Example 1** (Sec. 8.1): Vectors with enum for multiple types:
```rust
enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Text(String),
}
let row = vec![
    SpreadsheetCell::Int(3),
    SpreadsheetCell::Text(String::from("blue")),
    SpreadsheetCell::Float(10.12),
];
```

**Example 2** (Sec. 8.2): String concatenation and iteration:
```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");
let s = format!("{s1}-{s2}-{s3}");  // "tic-tac-toe", no moves

for c in "Зд".chars() {
    println!("{c}");  // prints З then д
}
for b in "Зд".bytes() {
    println!("{b}");  // prints 208, 151, 208, 180
}
```

**Example 3** (Sec. 8.3): HashMap entry API for word counting:
```rust
use std::collections::HashMap;

let text = "hello world wonderful world";
let mut map = HashMap::new();
for word in text.split_whitespace() {
    let count = map.entry(word).or_insert(0);
    *count += 1;
}
// {"world": 2, "hello": 1, "wonderful": 1}
```

# Relationships

## Builds Upon
- **rust-enums-and-matching** -- `Option<T>` returned by `.get()`; enums enable storing multiple types in vectors
- **rust-structs** -- collections are structs with methods; ownership rules apply to elements

## Enables
- **rust-error-handling** -- collections operations can fail (e.g., out-of-bounds); patterns of handling `Option` from collection access feed into `Result` handling

## Related
- **rust-enums-and-matching** -- `Option` is central to safe collection access
- **rust-error-handling** -- error-returning patterns build on the same Option/Result handling
- **rust-module-system** -- `use std::collections::HashMap;` demonstrates the `use` keyword

## Contrasts With
(none)

# Common Errors

- **Error**: Holding an immutable reference to a vector element while pushing new elements.
  **Correction**: The borrow checker prevents this because `push` may reallocate the vector's memory, invalidating all existing references. Finish using references before mutating the vector.

- **Error**: Trying to index into a `String` with `s[0]` to get a character.
  **Correction**: Rust strings are UTF-8 and do not support integer indexing. Use `.chars().nth(n)` for the nth Unicode scalar value, or range slicing `&s[start..end]` on known character boundaries.

- **Error**: Using the `+` operator and expecting the first `String` to remain valid.
  **Correction**: `+` calls `add(self, &str)` which moves the first operand. After `let s3 = s1 + &s2;`, `s1` is no longer valid. Use `format!` if you need all strings to remain valid.

# Common Confusions

- **Confusion**: Thinking `String` and `&str` are the same type.
  **Clarification**: `&str` is a string slice -- an immutable reference to UTF-8 data stored elsewhere (often in the binary or on the heap). `String` is an owned, growable, heap-allocated UTF-8 string. `String` derefs to `&str`, so you can pass `&String` where `&str` is expected (deref coercion).

- **Confusion**: Expecting `s.len()` to return the number of characters.
  **Clarification**: `.len()` returns the number of bytes, not characters. "Hola" is 4 bytes and 4 characters, but Cyrillic text can be 2 bytes per character and Devanagari can be 3+ bytes per grapheme cluster. Use `.chars().count()` for the number of Unicode scalar values.

- **Confusion**: Assuming `HashMap` iteration order is deterministic.
  **Clarification**: `HashMap` iteration order is arbitrary and not guaranteed to be consistent between runs. If you need ordered iteration, use `BTreeMap` from `std::collections`.

# Source Reference

Chapter 8: Common Collections. Section 8.1: Storing Lists of Values with Vectors (creating, updating, reading, iterating, enum multi-type, dropping). Section 8.2: Storing UTF-8 Encoded Text with Strings (String vs &str, creating, updating, concatenation, internal representation, bytes/chars/grapheme clusters, slicing, iterating). Section 8.3: Storing Keys with Associated Values in Hash Maps (creating, accessing, ownership, updating, overwriting, entry API, hashing functions).

# Verification Notes

- Definition source: Direct synthesis from Chapter 8 source (996 lines)
- Key Properties: All items directly stated in the source text
- Confidence rationale: HIGH -- the chapter provides explicit, comprehensive coverage of all three collection types
- Uncertainties: None; this is foundational, well-defined material
- Cross-reference status: Related slugs reference cards in this rust-book extraction set
