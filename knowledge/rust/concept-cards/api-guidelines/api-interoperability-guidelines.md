---
concept: API Interoperability Guidelines
slug: api-interoperability-guidelines
category: api-design
subcategory: null
tier: intermediate
source: "Rust API Guidelines"
source_slug: api-guidelines
authors: "The Rust Library Team"
chapter: "02-interoperability"
chapter_number: 2
pdf_page: null
section: "Interoperability"
extraction_confidence: high
aliases:
  - "rust interoperability guidelines"
  - "C-COMMON-TRAITS C-CONV-TRAITS C-COLLECT C-SERDE C-SEND-SYNC C-GOOD-ERR C-NUM-FMT C-RW-VALUE"
prerequisites:
  - api-guidelines-overview
extends:
  - api-guidelines-overview
related:
  - api-naming-guidelines
  - api-predictability-guidelines
  - api-flexibility-guidelines
contrasts_with: []
answers_questions:
  - "What traits should my Rust types implement?"
  - "How should I handle conversions between types?"
  - "Should my types implement Serde traits?"
  - "How should error types be designed in Rust?"
  - "Why should types be Send and Sync?"
  - "How should reader/writer functions accept parameters?"
---

# Quick Definition

The Interoperability chapter of the Rust API Guidelines defines 8 guidelines (C-COMMON-TRAITS, C-CONV-TRAITS, C-COLLECT, C-SERDE, C-SEND-SYNC, C-GOOD-ERR, C-NUM-FMT, C-RW-VALUE) ensuring crates interact nicely with other library functionality. The central theme is eagerly implementing standard traits so types work seamlessly across the ecosystem.

# Core Definition

**C-COMMON-TRAITS** -- Types eagerly implement common traits. Because Rust's orphan rule prevents downstream crates from adding trait impls, crates must eagerly implement all applicable common traits: Copy, Clone, Eq, PartialEq, Ord, PartialOrd, Hash, Debug, Display, Default. "It is common and expected for types to implement both Default and an empty new constructor."

**C-CONV-TRAITS** -- Conversions use the standard traits From, TryFrom, AsRef, AsMut. Never implement Into or TryInto directly -- these have blanket impls based on From and TryFrom. Implement those instead.

**C-COLLECT** -- Collections implement FromIterator and Extend, enabling use with `Iterator::collect`, `Iterator::partition`, and `Iterator::unzip`. FromIterator creates a new collection from an iterator; Extend adds items from an iterator onto an existing collection.

**C-SERDE** -- Data structures implement Serde's Serialize and Deserialize. Types that play the role of a data structure (like `LinkedHashMap` or `IpAddr`) should implement these. Marker types (like `LittleEndian`) should not. Gate Serde impls behind a Cargo feature named simply `"serde"` -- not `"serde_impls"` or `"serde_serialization"`.

**C-SEND-SYNC** -- Types are Send and Sync where possible. These are automatically implemented by the compiler when appropriate. For types manipulating raw pointers, be vigilant that Send/Sync status accurately reflects thread safety characteristics. Test with compile-time assertions.

**C-GOOD-ERR** -- Error types are meaningful and well-behaved. Error types should always implement `std::error::Error`, plus Send and Sync (required for use across threads and in `std::io::Error::new`). Never use `()` as an error type -- it does not implement Error, Display, or produce meaningful Debug output. Define meaningful error types even if they carry no data (use a unit struct). Error messages should be lowercase without trailing punctuation.

**C-NUM-FMT** -- Binary number types provide Hex, Octal, Binary formatting via `UpperHex`, `LowerHex`, `Octal`, and `Binary` traits. Implement these for types on which bitwise manipulations are meaningful, especially bitflag types.

**C-RW-VALUE** -- Generic reader/writer functions take `R: Read` and `W: Write` by value, not by reference. Because `&mut R` implements `Read` when `R: Read`, callers can pass `&mut f` when they need to retain ownership. Documentation should remind users of this possibility.

# Prerequisites

- **api-guidelines-overview** -- understanding the overall guidelines framework

# Key Properties

1. The orphan rule makes eager trait implementation essential -- downstream crates cannot add missing impls
2. Implement From (not Into) and TryFrom (not TryInto) because blanket impls provide the reverse direction
3. Serde support should be gated behind a feature named exactly `"serde"` for ecosystem consistency
4. Error types must implement Error + Send + Sync + Display; `()` as an error type is never acceptable
5. Send + Sync enable basic multithreaded error handling; `Error + Send + Sync + 'static` is the most useful bound for trait objects
6. Read/Write by value works because `&mut R` implements Read when R: Read (and similarly for Write)
7. Both Default and `new()` should exist when reasonable, and they should have the same behavior

# Construction / Recognition

## Applying the Interoperability Guidelines:
1. **Common traits** (C-COMMON-TRAITS): For each public type, derive or implement all applicable traits from the list: Copy, Clone, Eq, PartialEq, Ord, PartialOrd, Hash, Debug, Display, Default
2. **Conversions** (C-CONV-TRAITS): Implement From<T> for infallible conversions, TryFrom<T> for fallible ones, and AsRef/AsMut for cheap reference conversions. Never impl Into or TryInto directly
3. **Collections** (C-COLLECT): Implement FromIterator and Extend for any collection type
4. **Serde** (C-SERDE): Add optional Serde support with `serde = { version = "1.0", optional = true }` and `#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]`
5. **Thread safety** (C-SEND-SYNC): Add compile-time tests asserting Send and Sync for types that should be thread-safe
6. **Errors** (C-GOOD-ERR): Define a meaningful error type (even a unit struct) with Error, Display, Debug, Send, Sync implementations
7. **Formatting** (C-NUM-FMT): Implement Hex/Octal/Binary formatting for bitwise-manipulable types
8. **Read/Write** (C-RW-VALUE): Accept R: Read and W: Write by value and document that `&mut reader` can be passed

# Context & Application

Interoperability is what makes the Rust ecosystem feel cohesive. When all crates implement standard traits eagerly, types compose naturally: they can be used as hash map keys (Hash + Eq), printed for debugging (Debug), serialized (Serde), and sent across threads (Send + Sync) without friction.

The orphan rule makes this particularly important in Rust compared to languages with open class extensions. If a crate author forgets to implement Display, no downstream user can add it -- they must use the inconvenient newtype workaround.

# Examples

**Example 1** (C-CONV-TRAITS): `From<u16>` is implemented for `u32` because a smaller integer always fits. `From<u32>` is not implemented for `u16` because it may fail. Instead, `TryFrom<u32>` is implemented for `u16`, returning an error if the value is too large.

**Example 2** (C-GOOD-ERR): Instead of `fn do_the_thing() -> Result<Wow, ()>`, define a meaningful error: `struct DoError;` with `impl Display for DoError` and `impl Error for DoError`. Error messages should be lowercase without trailing punctuation: "unexpected end of file", "invalid IP address syntax".

**Example 3** (C-SERDE): The canonical Serde integration with derive:
```toml
[dependencies]
serde = { version = "1.0", optional = true, features = ["derive"] }
```
```rust
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub struct T { /* ... */ }
```

**Example 4** (C-SEND-SYNC): Compile-time assertions for thread safety:
```rust
#[test]
fn test_send() {
    fn assert_send<T: Send>() {}
    assert_send::<MyStrangeType>();
}
```

**Example 5** (C-RW-VALUE): Functions like `serde_json::from_reader` and `flate2::read::GzDecoder::new` take `R: Read` by value. Users who need to read multiple times from the same file pass `&mut f` instead of `f`.

# Relationships

## Builds Upon
- **api-guidelines-overview** -- this is one of the 10 guideline categories

## Enables
- Types that implement common traits compose seamlessly across the ecosystem
- Serde integration enables serialization to any format without per-type work
- Send + Sync enable concurrent and parallel usage patterns

## Related
- **api-naming-guidelines** -- C-CONV-TRAITS complements C-CONV (naming conventions for conversions)
- **api-predictability-guidelines** -- C-CONV-SPECIFIC relates to where conversion methods live
- **api-flexibility-guidelines** -- C-GENERIC relates to accepting generic Read/Write parameters

## Contrasts With
- Languages without orphan rules where trait/interface impls can be added anywhere
- Error handling approaches using string messages or generic error types

# Common Errors

- **Error**: Implementing Into<T> directly instead of From<T>.
  **Correction**: Always implement From<T>. The Into<T> blanket impl is provided automatically. Implementing Into directly is never necessary and skips the reverse From impl.

- **Error**: Using `()` as an error type for functions that can fail.
  **Correction**: Define a meaningful error type, even if it is a unit struct like `struct DoError;`. This enables use with `?`, error-chain, and provides a useful Debug representation.

- **Error**: Naming the Serde feature `serde_impls` or `serde_serialization`.
  **Correction**: Name it simply `"serde"` for consistency with the ecosystem and Cargo's implicit feature naming.

# Common Confusions

- **Confusion**: Thinking that implementing many traits is wasteful if not all users need them.
  **Clarification**: Due to the orphan rule, missing trait impls cannot be added by downstream crates. It is far better to implement eagerly and let users benefit when needed than to force the newtype workaround.

- **Confusion**: Thinking `Error::description()` should be implemented for error types.
  **Clarification**: `Error::description()` is deprecated. Users should always use Display instead. Do not implement description.

- **Confusion**: Thinking reader/writer functions should take `&mut R` to avoid consuming the reader.
  **Clarification**: Taking `R: Read` by value is correct because `&mut R` itself implements Read. Callers pass `&mut f` when they need to retain ownership. The function signature is simpler and more flexible by taking by value.

# Source Reference

Chapter 2: Interoperability. All 8 guidelines (C-COMMON-TRAITS, C-CONV-TRAITS, C-COLLECT, C-SERDE, C-SEND-SYNC, C-GOOD-ERR, C-NUM-FMT, C-RW-VALUE) are covered with detailed explanations, rationale, and examples from the standard library and ecosystem crates.

# Verification Notes

- Definition: All guideline descriptions drawn directly from the chapter text
- Key Properties: Extracted from explicit statements and rationale in each guideline section
- Confidence: HIGH -- the interoperability guidelines are well-established with extensive examples
- Uncertainties: The boundary between "data structure" and "not data structure" for C-SERDE is acknowledged as sometimes gray
- Cross-reference status: All slugs reference cards in this extraction set
