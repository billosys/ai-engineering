---
# === CORE IDENTIFICATION ===
concept: Return Consumed Argument on Error
slug: return-consumed-arg-on-error

# === CLASSIFICATION ===
category: idiom
subcategory: error-handling
tier: intermediate

# === PROVENANCE ===
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "Return consumed argument on error"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "return moved value on error"
  - "error with consumed argument"
  - "give back on failure"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ownership-and-move
  - result-type
extends: []
related:
  - string-from-utf8
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I let callers retry an operation after failure without cloning the argument?"
  - "Why does String::from_utf8 return the original Vec in its error type?"
  - "What pattern allows recovering a moved argument when a function fails?"
---

# Quick Definition

When a fallible function consumes (moves) an argument, include the original argument in the error type so callers can recover it on failure. This avoids forcing callers to clone the argument preemptively and enables retry patterns without extra allocations.

# Core Definition

> "If a fallible function consumes (moves) an argument, return that argument back inside an error." -- Rust Design Patterns, "Return consumed argument on error"

> "In case of error you may want to try some alternative way or to retry action in case of non-deterministic function. But if the argument is always consumed, you are forced to clone it on every call, which is not very efficient." -- Rust Design Patterns, "Return consumed argument on error"

The standard library uses this pattern in `String::from_utf8`, where `FromUtf8Error` contains the original `Vec<u8>` accessible via `.into_bytes()`.

# Prerequisites

- Understanding of Rust ownership and move semantics
- Familiarity with `Result<T, E>` and custom error types

# Key Properties

1. **Error type contains the argument**: The error struct wraps the original moved value.
2. **Enables retry without cloning**: Callers can extract the value from the error and try again.
3. **Performance benefit**: Moves are cheap; avoiding preemptive clones saves allocation.
4. **Standard library precedent**: `String::from_utf8` returns `FromUtf8Error` which contains the original `Vec<u8>`.
5. **Slightly more complex error types**: The error struct must include a field for the returned argument.

# Construction / Recognition

## To Apply:
1. Identify a function that moves (consumes) an argument and can fail
2. Define a custom error type that wraps the consumed argument
3. On failure, return `Err(MyError(original_value))`
4. Callers can destructure the error to recover the value

## To Recognize:
- Error types that contain the same type as a consumed function parameter
- `Err(SendError(value))` patterns where `value` was moved into the function
- Retry loops that extract the value from the error: `Err(E(val)) => val`

# Context & Application

This pattern is particularly valuable for non-deterministic operations (network sends, lock acquisitions) where retry is a natural response to failure. Without it, callers must clone the argument before every call attempt, wasting allocation even on the successful path. The pattern shifts the cost to the error path only, where the value is moved back to the caller inside the error.

# Examples

**Function returning consumed argument on error:**

```rust
pub fn send(value: String) -> Result<(), SendError> {
    println!("using {value} in a meaningful way");
    // Simulate non-deterministic failure
    use std::time::SystemTime;
    let period = SystemTime::now()
        .duration_since(SystemTime::UNIX_EPOCH)
        .unwrap();
    if period.subsec_nanos() % 2 == 1 {
        Ok(())
    } else {
        Err(SendError(value))
    }
}

pub struct SendError(String);
```

**Caller retry loop recovering the value:**

```rust
let mut value = "imagine this is very long string".to_string();

let success = 's: {
    for _ in 0..2 {
        value = match send(value) {
            Ok(()) => break 's true,
            Err(SendError(value)) => value,  // recover the value
        }
    }
    false
};
```

# Relationships

## Related
- **string-from-utf8** -- Standard library example: `String::from_utf8` returns the original `Vec<u8>` inside `FromUtf8Error`

# Common Errors

- **Error**: Consuming an argument without returning it in the error, forcing callers to clone
  **Correction**: Include the consumed argument in the error type

- **Error**: Forgetting to destructure the error to recover the value in retry loops
  **Correction**: Pattern match on the error variant to extract the original argument

# Common Confusions

- **Confusion**: Thinking the value must be cloned before calling a consuming function
  **Clarification**: If the function follows this pattern, the value is returned on error -- no clone needed

- **Confusion**: Believing this pattern adds runtime overhead
  **Clarification**: Moving a value into an error type is as cheap as any other move; the real cost savings come from avoiding clones

# Source Reference

Chapter 1: Idioms, Section "Return consumed argument on error".

# Verification Notes

- Definition source: Directly from "Return consumed argument on error" section
- Confidence rationale: HIGH -- complete example with motivation and standard library reference
- Uncertainties: None
- Cross-reference status: References String::from_utf8 and FromUtf8Error
