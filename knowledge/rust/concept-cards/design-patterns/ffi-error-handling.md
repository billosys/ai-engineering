---
# === CORE IDENTIFICATION ===
concept: FFI Error Handling
slug: ffi-error-handling

# === CLASSIFICATION ===
category: ffi-idiom
subcategory: error-handling
tier: advanced

# === PROVENANCE ===
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "Error Handling in FFI"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "FFI error codes"
  - "C error conversion"
  - "foreign error handling"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ffi-basics
  - rust-error-handling
  - repr-c
extends: []
related:
  - ffi-accepting-strings
  - ffi-passing-strings
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert Rust errors to C-compatible error codes?"
  - "How do I expose Rust error information through an FFI boundary?"
  - "What are the strategies for representing structured Rust errors in C?"
---

# Quick Definition

Convert Rust errors to C-compatible representations using three strategies: flat enums convert directly to integer codes via `From<Enum> for c_int`; structured enums map to integer codes plus a separate function that returns a C string description; custom error types get a parallel `#[repr(C)]` struct for direct C representation.

# Core Definition

> "In foreign languages like C, errors are represented by return codes. However, Rust's type system allows much more rich error information to be captured and propagated through a full type." -- Rust Design Patterns, "Error Handling in FFI"

The idiom presents three escalating strategies:
1. **Flat Enums**: Assign integer discriminants and implement `From<Error> for libc::c_int`.
2. **Structured Enums**: Map variants to integer codes and provide a separate `extern "C"` function to retrieve a dynamically allocated C string description.
3. **Custom Error Types**: Create a parallel `#[repr(C)]` struct and implement `From<RustError> for CError`.

# Prerequisites

- Understanding of Rust's `Result` and error types
- FFI fundamentals (`extern "C"`, `#[no_mangle]`, `libc` types)
- Knowledge of `#[repr(C)]` for C-compatible struct layout

# Key Properties

1. **Flat enums to integers**: Assign explicit discriminants (e.g., `IsReadOnly = 1`) and convert via `(e as i8).into()`.
2. **Structured enums need accessors**: Map to integer codes with `match`, then provide a separate `extern "C"` function for error descriptions.
3. **Custom types use repr(C)**: Create a second struct with `#[repr(C)]` and implement `From` between the Rust and C versions.
4. **Preserve Rust API**: The C-facing error types do not compromise the internal Rust API design.
5. **Memory management**: Dynamically allocated error strings (via `libc::malloc`) must be freed by the caller.

# Construction / Recognition

## To Apply:
1. Identify the Rust error type to expose across FFI
2. Choose the appropriate strategy based on error complexity
3. For flat enums: assign integer discriminants and implement `From` for `c_int`
4. For structured enums: implement integer conversion plus an accessor function for descriptions
5. For custom types: create a `#[repr(C)]` mirror struct and implement `From`

## To Recognize:
- `impl From<ErrorType> for libc::c_int`
- `#[repr(C)]` structs mirroring Rust error types
- `extern "C"` functions returning error descriptions as `*const libc::c_char`

# Context & Application

C APIs communicate errors through integer return codes and sentinel values like `NULL` pointers. When exposing a Rust library to C consumers, Rust's rich error types must be flattened into this model. The three strategies provide increasing fidelity: flat enums give only an error code, structured enums add descriptive strings, and `#[repr(C)]` types preserve full structural information.

# Examples

**Example 1 -- Flat enum to integer code:**

```rust
enum DatabaseError {
    IsReadOnly = 1,
    IOError = 2,
    FileCorrupted = 3,
}

impl From<DatabaseError> for libc::c_int {
    fn from(e: DatabaseError) -> libc::c_int {
        (e as i8).into()
    }
}
```

**Example 2 -- Custom error type with repr(C):**

```rust
struct ParseError {
    expected: char,
    line: u32,
    ch: u16,
}

#[repr(C)]
pub struct parse_error {
    pub expected: libc::c_char,
    pub line: u32,
    pub ch: u16,
}

impl From<ParseError> for parse_error {
    fn from(e: ParseError) -> parse_error {
        let ParseError { expected, line, ch } = e;
        parse_error { expected, line, ch }
    }
}
```

# Relationships

## Related
- **ffi-accepting-strings** -- Companion FFI idiom for receiving C strings in Rust
- **ffi-passing-strings** -- Companion FFI idiom for sending Rust strings to C

# Common Errors

- **Error**: Forgetting to allocate a null-terminated C string for error descriptions
  **Correction**: Use `libc::malloc` with length + 1 and write a `'\0'` byte at the end

- **Error**: Not handling memory ownership for dynamically allocated error strings
  **Correction**: Document that the caller must free the returned pointer, or provide a dedicated free function

- **Error**: Assuming all Rust types can be trivially converted to C representations
  **Correction**: Some types (e.g., `String`, `Vec`) require careful conversion; not all map cleanly to C

# Common Confusions

- **Confusion**: Thinking the C error type must match the Rust type exactly
  **Clarification**: The C representation is a simplified parallel; use `From` to bridge them

- **Confusion**: Using Rust's `String` directly in FFI error descriptions
  **Clarification**: Must convert to a null-terminated C string allocated with `libc::malloc`

# Source Reference

Chapter 1: Idioms, Section "Error Handling in FFI".

# Verification Notes

- Definition source: Directly from "Error Handling in FFI" section with three code examples
- Confidence rationale: HIGH -- detailed examples for all three strategies
- Uncertainties: None
- Cross-reference status: Part of the FFI Idioms group
