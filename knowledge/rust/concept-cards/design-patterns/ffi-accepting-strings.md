---
# === CORE IDENTIFICATION ===
concept: FFI Accepting Strings
slug: ffi-accepting-strings

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
section: "Accepting Strings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "FFI string input"
  - "C string to Rust"
  - "CStr from pointer"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ffi-basics
  - cstr-cstring
  - unsafe-rust
extends: []
related:
  - ffi-passing-strings
  - ffi-error-handling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I safely accept a C string in a Rust FFI function?"
  - "Should I copy or borrow C strings when accepting them in Rust?"
  - "How do I minimize unsafe code when converting C strings to Rust strings?"
---

# Quick Definition

When accepting C strings via FFI, use `CStr::from_ptr()` to borrow the foreign string as a `&CStr`, then convert to `&str` with `.to_str()`. This minimizes `unsafe` code, avoids unnecessary copying, and turns an untracked raw pointer into a lifetime-tracked reference.

# Core Definition

> "Keep foreign strings 'borrowed', rather than copying them directly." -- Rust Design Patterns, "Accepting Strings"

> "Minimize the amount of complexity and `unsafe` code involved in converting from a C-style string to native Rust strings." -- Rust Design Patterns, "Accepting Strings"

Two principles guide this idiom: (1) borrow rather than copy, and (2) minimize unsafe surface area. The `&CStr` type provides a zero-cost borrowed view of a C string, and `.to_str()` validates UTF-8 without allocation. The `unsafe` block should contain only the `CStr::from_ptr()` call.

# Prerequisites

- Understanding of C string conventions (null-terminated, arbitrary non-zero bytes)
- Knowledge of `CStr` and `CString` types in `std::ffi`
- Familiarity with `unsafe` Rust and raw pointers

# Key Properties

1. **Borrow, don't copy**: Use `&CStr` to borrow the C string rather than copying into a `CString` or `String`.
2. **Minimal unsafe**: Only `CStr::from_ptr()` needs to be in an `unsafe` block.
3. **Zero-cost conversion**: Borrowing via `&CStr` involves no allocation or copying.
4. **UTF-8 validation**: `.to_str()` validates that the C string is valid UTF-8, returning a `Result`.
5. **Lifetime tracking**: Converts an untracked pointer lifetime into a tracked reference lifetime.
6. **Safety contract**: The caller must guarantee the pointer is non-null, points to valid data ending in a null byte, and won't be mutated during the call.

# Construction / Recognition

## To Apply:
1. Accept a `*const libc::c_char` parameter in an `extern "C"` function
2. Document safety requirements in a `# Safety` doc comment
3. Call `CStr::from_ptr(ptr)` inside a minimal `unsafe` block
4. Convert to `&str` with `.to_str()` and handle the UTF-8 validation result
5. Use the resulting `&str` in safe Rust code

## To Recognize:
- `extern "C"` function taking `*const libc::c_char`
- `CStr::from_ptr()` followed by `.to_str()`
- Small `unsafe` block containing only the pointer conversion

# Context & Application

C strings differ from Rust strings in three ways: they are null-terminated (Rust stores length), they can contain arbitrary non-zero bytes (Rust requires UTF-8), and they use unsafe pointer operations (Rust uses safe methods). The `CStr` and `&CStr` types bridge these differences. Copying the string (as shown in the anti-pattern) introduces more unsafe code, more invariants to uphold, and subtle bugs like missing the null terminator during manual pointer arithmetic.

# Examples

**Good -- borrow with CStr::from_ptr:**

```rust
pub unsafe extern "C" fn mylib_log(
    msg: *const libc::c_char,
    level: libc::c_int,
) {
    let level: crate::LogLevel = match level { /* ... */ };

    let msg_str: &str = match std::ffi::CStr::from_ptr(msg).to_str() {
        Ok(s) => s,
        Err(e) => {
            crate::log_error("FFI string conversion failed");
            return;
        }
    };

    crate::log(msg_str, level);
}
```

**Bad -- manual copy with pointer arithmetic (subtle bug):**

```rust
// DO NOT USE: verbose, more unsafe code, and contains a bug
// where the NUL terminator is not copied, leading to
// undefined behaviour when CString reads uninitialized memory.
let msg_len = unsafe { libc::strlen(msg) };
let mut msg_data = Vec::with_capacity(msg_len + 1);
let msg_cstr: std::ffi::CString = unsafe {
    std::ptr::copy_nonoverlapping(msg, msg_data.as_mut(), msg_len);
    msg_data.set_len(msg_len + 1);
    std::ffi::CString::from_vec_with_nul(msg_data).unwrap()
};
```

# Relationships

## Related
- **ffi-passing-strings** -- The reverse direction: passing Rust strings to C
- **ffi-error-handling** -- Companion FFI idiom for error representation

# Common Errors

- **Error**: Manually copying string bytes with pointer arithmetic instead of using `CStr`
  **Correction**: Use `CStr::from_ptr()` for zero-cost borrowing

- **Error**: Forgetting to copy the null terminator when manually copying C strings
  **Correction**: Avoid manual copying entirely; use the `CStr` API

- **Error**: Not handling the UTF-8 validation failure from `.to_str()`
  **Correction**: Always match on the `Result` and handle invalid UTF-8 gracefully

# Common Confusions

- **Confusion**: Thinking you need to allocate a `CString` to accept a C string
  **Clarification**: `&CStr` borrows the data in place; `CString` is for owned C strings created in Rust

- **Confusion**: Believing the `unsafe` block must encompass the entire function
  **Clarification**: Only `CStr::from_ptr()` requires `unsafe`; keep the block minimal

# Source Reference

Chapter 1: Idioms, Section "Accepting Strings" (within FFI Idioms).

# Verification Notes

- Definition source: Directly from "Accepting Strings" section with good and bad examples
- Confidence rationale: HIGH -- detailed anti-pattern with explained bug
- Uncertainties: None
- Cross-reference status: Part of the FFI Idioms group
