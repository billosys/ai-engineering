---
# === CORE IDENTIFICATION ===
concept: API Dependability and Debuggability Guidelines
slug: api-dependability-guidelines

# === CLASSIFICATION ===
category: api-design
subcategory: dependability
tier: intermediate

# === PROVENANCE ===
source: "Rust API Guidelines"
source_slug: api-guidelines
authors: "The Rust Library Team"
chapter: "08-dependability, 09-debuggability"
chapter_number: 8
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "C-VALIDATE"
  - "C-DTOR-FAIL"
  - "C-DTOR-BLOCK"
  - "C-DEBUG"
  - "C-DEBUG-NONEMPTY"
  - "Rust API dependability"
  - "Rust API debuggability"
  - "argument validation guidelines"
  - "destructor guidelines"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - api-guidelines-overview
  - api-type-safety-guidelines
extends: []
related:
  - api-predictability-guidelines
  - api-interoperability-guidelines
  - api-future-proofing-guidelines
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should Rust APIs validate their arguments?"
  - "What is the difference between static and dynamic enforcement in Rust?"
  - "What does the _unchecked suffix convention mean?"
  - "Why should destructors never fail in Rust?"
  - "What should I do instead of panicking in a Drop implementation?"
  - "Why should destructors avoid blocking operations?"
  - "Should all public types implement Debug?"
  - "What should the Debug representation of an empty value look like?"
  - "Does Rust follow the robustness principle?"
---

# Quick Definition

Rust APIs should validate inputs strictly rather than following the robustness principle, preferring static enforcement via types over dynamic runtime checks. Destructors must never fail (C-DTOR-FAIL) and should avoid blocking (C-DTOR-BLOCK), offering explicit `close` methods instead. All public types should implement `Debug` (C-DEBUG) with non-empty representations (C-DEBUG-NONEMPTY). These five guidelines (C-VALIDATE, C-DTOR-FAIL, C-DTOR-BLOCK, C-DEBUG, C-DEBUG-NONEMPTY) ensure APIs are reliable and diagnosable.

# Core Definition

The Rust API Guidelines define five conventions for dependable and debuggable APIs spanning Chapters 8 and 9.

**C-VALIDATE**: "Rust APIs do not generally follow the robustness principle: 'be conservative in what you send; be liberal in what you accept.' Instead, Rust code should enforce the validity of input whenever practical." The source defines a hierarchy of enforcement mechanisms in order of preference: (1) static enforcement via types, (2) dynamic enforcement via runtime validation, (3) dynamic enforcement with `debug_assert!` for expensive checks, and (4) dynamic enforcement with opt-out via `_unchecked` suffixed functions or `raw` submodules.

**C-DTOR-FAIL**: "Destructors are executed while panicking, and in that context a failing destructor causes the program to abort." The guideline mandates providing a separate `close` method returning `Result` for clean teardown, with `Drop` silently handling or logging errors.

**C-DTOR-BLOCK**: "Destructors should not invoke blocking operations, which can make debugging much more difficult." Like C-DTOR-FAIL, the guidance is to provide a separate method for preparing an infallible, nonblocking teardown.

**C-DEBUG**: "All public types implement `Debug`. If there are exceptions, they are rare."

**C-DEBUG-NONEMPTY**: "Even for conceptually empty values, the `Debug` representation should never be empty." An empty string debugs as `""`, an empty vec as `[]`.

# Prerequisites

- **API Guidelines Overview** -- understanding the overall framework and checklist approach
- **API Type Safety Guidelines** -- C-VALIDATE builds on C-NEWTYPE for static enforcement via wrapper types

# Key Properties

1. **Reject the robustness principle**: Rust APIs enforce strict input validity rather than being liberal in what they accept
2. **Static enforcement preferred**: Choose argument types that rule out bad inputs at compile time (e.g., `Ascii` instead of `u8`)
3. **Static enforcement is cheapest**: "Pushes the costs to the boundaries" and "catches bugs early, during compilation"
4. **Dynamic enforcement tradeoffs**: Runtime overhead, delayed bug detection, introduces failure cases via `panic!` or `Result`/`Option`
5. **debug_assert! for expensive checks**: Allows turning off costly validation in production builds
6. **_unchecked convention**: Opt-out functions use the `_unchecked` suffix or live in a `raw` submodule
7. **Destructors must be infallible**: A failing destructor during panic causes program abort
8. **Destructors must be non-blocking**: Blocking destructors make debugging difficult
9. **Provide explicit close methods**: Return `Result` to signal teardown problems
10. **Universal Debug implementation**: All public types should implement `Debug` with non-empty output

# Construction / Recognition

## Static enforcement (C-VALIDATE, preferred):
```rust
// Prefer this: type rules out invalid input
fn foo(a: Ascii) { /* ... */ }

// Over this: any u8 value accepted, including invalid ones
fn foo(a: u8) { /* ... */ }
```

## Dynamic enforcement with opt-out (C-VALIDATE):
```rust
// Checked version (default)
fn from_utf8(v: Vec<u8>) -> Result<String, FromUtf8Error> { /* ... */ }

// Unchecked version (opt-out for performance)
unsafe fn from_utf8_unchecked(v: Vec<u8>) -> String { /* ... */ }
```

## Destructor with separate close method (C-DTOR-FAIL, C-DTOR-BLOCK):
```rust
impl MyResource {
    /// Explicitly close the resource, returning any errors.
    pub fn close(self) -> Result<(), Error> { /* ... */ }
}

impl Drop for MyResource {
    fn drop(&mut self) {
        // Do teardown, ignore or log errors -- never panic
        let _ = self.internal_close();
    }
}
```

## Debug for empty values (C-DEBUG-NONEMPTY):
```rust
let empty_str = "";
assert_eq!(format!("{:?}", empty_str), "\"\"");

let empty_vec = Vec::<bool>::new();
assert_eq!(format!("{:?}", empty_vec), "[]");
```

# Context & Application

These guidelines reflect a core Rust philosophy: prefer compile-time guarantees over runtime checks, and when runtime checks are necessary, make them explicit. The C-VALIDATE guideline's explicit rejection of Postel's Law (the robustness principle) is a deliberate design choice -- Rust APIs are strict by default with opt-in leniency via `_unchecked` variants. The destructor guidelines (C-DTOR-FAIL, C-DTOR-BLOCK) address a practical concern unique to Rust's ownership model: `Drop` runs automatically and can run during unwinding, so it must be safe to execute in all contexts. The debuggability guidelines (C-DEBUG, C-DEBUG-NONEMPTY) are brief but important -- `Debug` is essential for error messages, logging, and `assert_eq!` output.

# Examples

**Example 1** (Ch. 8, C-VALIDATE): Static enforcement with the `Ascii` wrapper type:
> "`Ascii` is a wrapper around `u8` that guarantees the highest bit is zero; see newtype patterns (C-NEWTYPE) for more details on creating typesafe wrappers."
The cost is pushed to the boundary where a `u8` is first converted into an `Ascii`.

**Example 2** (Ch. 8, C-VALIDATE): The `_unchecked` convention:
> "The convention is to mark these opt-out functions with a suffix like `_unchecked` or by placing them in a `raw` submodule. The unchecked functions can be used judiciously in cases where (1) performance dictates avoiding checks and (2) the client is otherwise confident that the inputs are valid."

**Example 3** (Ch. 8, C-DTOR-FAIL): Why destructors must not fail:
> "Destructors are executed while panicking, and in that context a failing destructor causes the program to abort."
The solution is a separate `close` method returning `Result`.

**Example 4** (Ch. 9, C-DEBUG-NONEMPTY): Empty values still have non-empty Debug output:
> `""` for empty strings, `[]` for empty vectors -- the Debug representation always shows the type's structure.

# Relationships

## Builds Upon
- **API Guidelines Overview** -- these guidelines are part of the overall API Guidelines checklist
- **API Type Safety Guidelines** -- C-VALIDATE's static enforcement uses the newtype pattern from C-NEWTYPE

## Enables
- Reliable error handling in destructors
- Consistent debugging experience across crate APIs
- Clear contract between library authors and consumers about input validation

## Related
- **api-predictability-guidelines** -- predictable APIs complement dependable ones
- **api-interoperability-guidelines** -- Debug is a standard trait covered by interoperability guidelines
- **api-future-proofing-guidelines** -- strict validation supports future API evolution

## Contrasts With
- None within this source

# Common Errors

- **Error**: Following the robustness principle by accepting any input and trying to make sense of it.
  **Correction**: "Rust code should enforce the validity of input whenever practical." Use types to rule out bad inputs statically. (C-VALIDATE)

- **Error**: Panicking in a `Drop` implementation when cleanup fails.
  **Correction**: "Provide a separate method for checking for clean teardown, e.g. a `close` method, that returns a `Result` to signal problems. If that `close` method is not called, the `Drop` implementation should do the teardown and ignore or log/trace any errors." (C-DTOR-FAIL)

- **Error**: Performing blocking I/O (e.g., flushing a network socket) in a destructor.
  **Correction**: "Consider providing a separate method for preparing for an infallible, nonblocking teardown." (C-DTOR-BLOCK)

- **Error**: Omitting `Debug` implementation on a public type.
  **Correction**: "All public types implement `Debug`. If there are exceptions, they are rare." (C-DEBUG)

# Common Confusions

- **Confusion**: Thinking static enforcement always has high runtime cost.
  **Clarification**: "Static enforcement usually comes at little run-time cost: it pushes the costs to the boundaries (e.g. when a `u8` is first converted into an `Ascii`)." The validation happens once at conversion time.

- **Confusion**: Thinking `_unchecked` functions are always unsafe.
  **Clarification**: The `_unchecked` convention indicates the function skips validation, but it is not always marked `unsafe` -- it depends on whether invalid inputs cause undefined behavior or just incorrect results.

- **Confusion**: Thinking `debug_assert!` is equivalent to `assert!`.
  **Clarification**: `debug_assert!` is only checked in debug builds, making it suitable for "expensive checks for production builds" where the validation overhead would be unacceptable.

- **Confusion**: Thinking an empty `Debug` output (empty string) is acceptable for empty collections.
  **Clarification**: "Even for conceptually empty values, the `Debug` representation should never be empty." Use `"[]"`, `"()"`, etc. to indicate the type's structure.

# Source Reference

Chapter 8: Dependability -- guidelines C-VALIDATE (functions validate their arguments), C-DTOR-FAIL (destructors never fail), C-DTOR-BLOCK (destructors that may block have alternatives). Chapter 9: Debuggability -- guidelines C-DEBUG (all public types implement Debug), C-DEBUG-NONEMPTY (Debug representation is never empty). No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 8 and Ch. 9 of the Rust API Guidelines
- Confidence rationale: HIGH -- guidelines are clearly stated with specific examples and rationale
- Uncertainties: None -- these are well-established conventions in the Rust ecosystem
- Cross-reference status: api-guidelines-overview and api-type-safety-guidelines referenced; api-type-safety-guidelines is in this extraction set
