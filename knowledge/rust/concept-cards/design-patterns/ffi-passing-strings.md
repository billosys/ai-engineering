---
# === CORE IDENTIFICATION ===
concept: FFI Passing Strings
slug: ffi-passing-strings

# === CLASSIFICATION ===
category: ffi-idiom
subcategory: string-handling
tier: advanced

# === PROVENANCE ===
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "Passing Strings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "FFI string output"
  - "Rust string to C"
  - "CString to FFI"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ffi-basics
  - cstr-cstring
  - unsafe-rust
extends: []
related:
  - ffi-accepting-strings
  - ffi-error-handling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I safely pass a Rust string to a C function?"
  - "Why does creating a CString and calling as_ptr() in one expression cause a dangling pointer?"
  - "When should I use Vec instead of CString for FFI string buffers?"
---

# Quick Definition

When passing strings to FFI functions, create a `CString` in a `let` binding to ensure it lives long enough, then pass `.as_ptr()` inside a minimal `unsafe` block. Never create a temporary `CString` and call `.as_ptr()` in the same expression -- this creates a dangling pointer. For strings the C code may modify, use a `Vec<u8>` buffer instead.

# Core Definition

> "Make the lifetime of owned strings as long as possible." -- Rust Design Patterns, "Passing Strings"

> "Minimize `unsafe` code during the conversion." -- Rust Design Patterns, "Passing Strings"

Four principles guide this idiom: (1) maximize the lifetime of owned strings, (2) minimize `unsafe` code, (3) use `Vec` instead of `CString` if the C code can modify the string data, and (4) do not transfer ownership to the callee unless the foreign API requires it.

# Prerequisites

- Understanding of `CString` and `CStr` types in `std::ffi`
- Knowledge of Rust's temporary lifetime and drop rules
- Familiarity with `unsafe` Rust and `extern "C"` functions

# Key Properties

1. **Maximize lifetime**: Bind `CString` to a `let` variable so it lives through the entire `unsafe` block.
2. **Dangling pointer trap**: `CString::new(...).as_ptr()` in one expression drops the `CString` immediately, creating a dangling pointer.
3. **Minimal unsafe**: Only the FFI call needs `unsafe`; the `CString` creation is safe.
4. **Vec for mutable buffers**: When C code writes into a buffer, use `Vec<u8>` with `as_mut_ptr()` instead of `CString`.
5. **Retain ownership**: Do not transfer string ownership to C unless the API explicitly requires it.
6. **Error propagation**: `CString::new()` returns a `Result` that handles embedded null bytes; propagate this error.

# Construction / Recognition

## To Apply (sending a string to C):
1. Create a `CString` from the Rust string with `CString::new()`
2. Bind it to a named `let` variable (not a temporary)
3. Pass `.as_ptr()` to the FFI function inside an `unsafe` block
4. The `CString` remains alive until the end of the enclosing scope

## To Apply (receiving a string from C):
1. Create a zeroed `Vec<u8>` buffer of sufficient size
2. Pass `buffer.as_mut_ptr()` to the FFI function
3. Truncate the buffer based on the returned length
4. Convert back via `CString::new(buffer).unwrap().into_string()`

## To Recognize:
- `CString::new(...)` bound to a `let` before `.as_ptr()` is used
- `unsafe` block containing only the FFI call
- `Vec<u8>` buffers for receiving strings from C

# Context & Application

The most common mistake when passing strings to C is creating a temporary `CString` and calling `.as_ptr()` in the same expression. The `CString` is dropped at the end of the statement, but the pointer lives on -- a classic dangling pointer. This is documented in the standard library as a known footgun. The fix is simple: always bind `CString` to a named variable first.

# Examples

**Good -- CString bound to a variable:**

```rust
fn report_error_to_ffi<S: Into<String>>(
    err: S,
) -> Result<(), std::ffi::NulError> {
    let c_err = std::ffi::CString::new(err.into())?;

    unsafe {
        // SAFETY: c_err lives until after this call returns
        seterr(c_err.as_ptr());
    }

    Ok(())
    // c_err is dropped here, after the unsafe block
}
```

**Bad -- dangling pointer from temporary:**

```rust
unsafe {
    // DANGLING POINTER: CString is dropped at end of this statement
    seterr(std::ffi::CString::new(err.into())?.as_ptr());
}
```

**Good -- Vec buffer for receiving strings from C:**

```rust
fn get_error_from_ffi() -> Result<String, std::ffi::IntoStringError> {
    let mut buffer = vec![0u8; 1024];
    unsafe {
        let written: usize = geterr(buffer.as_mut_ptr(), 1023).into();
        buffer.truncate(written + 1);
    }
    std::ffi::CString::new(buffer).unwrap().into_string()
}
```

# Relationships

## Related
- **ffi-accepting-strings** -- The reverse direction: accepting C strings in Rust
- **ffi-error-handling** -- Companion FFI idiom for error representation

# Common Errors

- **Error**: Creating a temporary `CString` and calling `.as_ptr()` in the same expression
  **Correction**: Always bind `CString` to a named `let` variable first

- **Error**: Using `CString` for buffers that C code will modify
  **Correction**: Use `Vec<u8>` with `as_mut_ptr()` for mutable buffers; round-tripping a modified `CString` is UB

- **Error**: Not propagating the `NulError` from `CString::new()`
  **Correction**: Use `?` to propagate; Rust strings may contain interior null bytes that C strings cannot

# Common Confusions

- **Confusion**: Thinking `vec![0u8; 1024]` is slow to initialize
  **Clarification**: Modern Rust optimizes this to `zmalloc`, which is as fast as the OS can return zeroed memory

- **Confusion**: Believing the `CString` lifetime extends because a pointer was derived from it
  **Clarification**: Pointer creation does not extend lifetimes the way reference creation does

# Source Reference

Chapter 1: Idioms, Section "Passing Strings" (within FFI Idioms).

# Verification Notes

- Definition source: Directly from "Passing Strings" section with good/bad examples and dangling pointer explanation
- Confidence rationale: HIGH -- includes the canonical dangling pointer anti-pattern
- Uncertainties: None
- Cross-reference status: Part of the FFI Idioms group
