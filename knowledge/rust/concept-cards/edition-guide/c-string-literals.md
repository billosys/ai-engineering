---
concept: C-String Literals
slug: c-string-literals
category: edition-2021
subcategory: null
tier: advanced
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "04-rust-2021"
chapter_number: 4
pdf_page: null
section: "C-string literals"
extraction_confidence: high
aliases:
  - "CStr literal"
  - "c string syntax"
  - "c prefix string"
  - "cr raw c-string"
prerequisites:
  - rust-2021-edition
extends: []
related:
  - edition-migration
contrasts_with: []
answers_questions:
  - "How do I write a C-string literal in Rust?"
  - "What is the c\"...\" syntax?"
  - "What type does a C-string literal produce?"
  - "Can C-string literals contain NUL bytes?"
  - "What is the difference between c\"...\" and cr\"...\"?"
---

# Quick Definition

Starting with Rust 1.77, C-string literals can be written using the `c"..."` prefix (or `cr"..."` for raw C-strings). They produce values of type `&core::ffi::CStr`, are automatically NUL-terminated, and do not allow interior NUL bytes. This syntax requires the 2021 edition because the `c` prefix was reserved as part of the 2021 syntax reservation.

# Core Definition

"Literals of the form `c\"foo\"` or `cr\"foo\"` represent a string of type `&core::ffi::CStr`. [...] Starting with Rust 1.77, C-strings can be written using C-string literal syntax with the `c` or `cr` prefix. [...] Now, C-strings can be written directly using literal syntax notation, which will generate a value of type `&core::ffi::CStr` which is automatically terminated with a NUL byte." (Edition Guide, Ch. 4: Rust 2021, "C-string literals")

# Prerequisites

- **Rust 2021 Edition** (`rust-2021-edition`) -- the `c` prefix was reserved as part of 2021 syntax reservation, enabling this feature

# Key Properties

1. `c"..."` produces a value of type `&core::ffi::CStr`
2. The string is automatically NUL-terminated
3. Interior NUL bytes (e.g., `\0` escapes) are not allowed
4. Byte escapes (`\xff`) are supported
5. Unicode escapes (`\u{00E6}`) are supported and encoded as UTF-8
6. Unicode characters (e.g., `αβγ`) are encoded as UTF-8
7. Strings can span multiple lines using `\` continuation
8. `cr"..."` is the raw variant (no backslash escape processing)
9. Raw C-strings support `#` delimiters for embedding double quotes: `cr#""foo""#`
10. This replaces the need for the `cstr` proc-macro crate

# Construction / Recognition

## To Use C-String Literals:
1. Prefix a string with `c`: `c"hello"` produces a `&CStr`
2. Use byte escapes for non-UTF-8 bytes: `c"byte \xff here"`
3. Use unicode escapes: `c"unicode \u{00E6}"`
4. For strings with backslashes, use raw syntax: `cr"C:\foo"`
5. For strings with double quotes, use `#` delimiters: `cr#""quoted""#`

## To Migrate from the `cstr` Crate:
1. Replace `cstr!("hello")` with `c"hello"`
2. Ensure your crate uses `edition = "2021"` or later
3. Remove the `cstr` dependency from `Cargo.toml`

# Context & Application

Before C-string literals, creating `CStr` values that could interoperate with C APIs was cumbersome. The standard approach was `CStr::from_bytes_with_nul(b"hello\0").unwrap()`, which was verbose and error-prone (forgetting the NUL byte, or including interior NULs). The `cstr` crate provided a proc-macro solution but required compiling an expensive proc-macro.

C-string literals solve this at the language level. The compiler ensures the string is valid (NUL-terminated, no interior NULs) at compile time. The `c` prefix was available because it was reserved as part of the Rust 2021 prefix syntax reservation (`ident"..."` patterns), demonstrating how the reservation system enables future language features without additional edition boundaries.

# Examples

**Example 1** (Basic usage and equivalence, "Details" section):

```rust
use core::ffi::CStr;

assert_eq!(c"hello", CStr::from_bytes_with_nul(b"hello\0").unwrap());
```

**Example 2** (Byte and unicode escapes, "Details" section):

```rust
use core::ffi::CStr;

assert_eq!(
    c"byte escapes \xff work",
    CStr::from_bytes_with_nul(b"byte escapes \xff work\0").unwrap()
);
assert_eq!(
    c"unicode escapes \u{00E6} work",
    CStr::from_bytes_with_nul(b"unicode escapes \xc3\xa6 work\0").unwrap()
);
assert_eq!(
    c"unicode characters αβγ encoded as UTF-8",
    CStr::from_bytes_with_nul(
        b"unicode characters \xce\xb1\xce\xb2\xce\xb3 encoded as UTF-8\0"
    ).unwrap()
);
```

**Example 3** (Raw C-strings, "Details" section):

```rust
assert_eq!(cr"foo", c"foo");
// Embed interior double quotes with # delimiters
assert_eq!(cr#""foo""#, c"\"foo\"");
// Multiple # for strings containing "#
assert_eq!(cr##""foo"#"##, c"\"foo\"#");
// Escapes are not processed in raw strings
assert_eq!(cr"C:\foo", c"C:\\foo");
```

**Example 4** (Multi-line C-strings, "Details" section):

```rust
use core::ffi::CStr;

assert_eq!(
    c"strings can continue \
        on multiple lines",
    CStr::from_bytes_with_nul(b"strings can continue on multiple lines\0").unwrap()
);
```

# Relationships

## Builds Upon
- **rust-2021-edition** -- uses the `c` prefix reserved by the 2021 edition's syntax reservation

## Enables
- No downstream concepts directly

## Related
- **edition-migration** -- macros that tokenize `c"..."` as two tokens need whitespace insertion

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Including a `\0` escape inside a C-string literal.
  **Correction**: C-strings do not allow interior NUL bytes. The NUL terminator is added automatically. If you need a string with interior NULs, use a regular byte string.

- **Error**: Expecting `cr"..."` to process backslash escapes.
  **Correction**: Raw C-strings (`cr"..."`) do not process escape sequences, just like raw strings (`r"..."`). Use `c"..."` if you need escapes.

# Common Confusions

- **Confusion**: Thinking C-string literals are available in Rust 2018.
  **Clarification**: The `c` prefix was reserved as part of the 2021 edition's syntax reservation. In editions prior to 2021, `c"hello"` is tokenized as two separate tokens (`c` and `"hello"`), not as a C-string literal. The feature requires edition 2021 or later.

- **Confusion**: Thinking C-string literals require the `cstr` crate.
  **Clarification**: C-string literals are a language feature (as of Rust 1.77) and require no external crate. The `cstr` crate is a historical workaround that is no longer needed.

- **Confusion**: Thinking C-string literals produce `CString` (owned) values.
  **Clarification**: C-string literals produce `&CStr` (borrowed) values, analogous to how `"hello"` produces `&str` rather than `String`. For an owned `CString`, you can call `.to_owned()` or use `CString::from()`.

# Source Reference

Chapter 4: Rust 2021, "C-string literals" section. Stabilized in Rust 1.77. The syntax relies on the prefix reservation from the "Reserved syntax" section. See The Rust Reference for the full specification of C-string and raw C-string literals. Migration relates to the `rust_2021_prefixes_incompatible_syntax` lint.

# Verification Notes

- Definition source: Direct quotation from "C-string literals" section, "Summary" and "Details" subsections
- Key Properties: All from explicit statements and code examples in the source
- Confidence rationale: HIGH -- the source provides clear specification with extensive code examples
- Uncertainties: None
- Cross-reference status: All slugs reference cards in this extraction set or Agent A's set
