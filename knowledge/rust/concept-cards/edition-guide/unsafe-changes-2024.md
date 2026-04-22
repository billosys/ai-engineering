---
concept: Unsafe Explicitness Changes 2024
slug: unsafe-changes-2024
category: edition-2024
subcategory: null
tier: advanced
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "05-rust-2024"
chapter_number: 5
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "unsafe extern 2024"
  - "unsafe attributes 2024"
  - "unsafe_op_in_unsafe_fn 2024"
  - "static mut references 2024"
  - "unsafe changes Rust 2024"
prerequisites:
  - rust-editions
related:
  - rust-2024-edition
contrasts_with: []
extends: []
answers_questions:
  - "What unsafe-related changes were made in Rust 2024?"
  - "Why must extern blocks be marked unsafe in Rust 2024?"
  - "Which attributes must be marked unsafe in Rust 2024?"
  - "What is unsafe_op_in_unsafe_fn?"
  - "Why are references to static mut disallowed in Rust 2024?"
  - "How do I replace static mut in Rust?"
---

# Quick Definition

Rust 2024 introduces four related changes that make `unsafe` more explicit: `extern` blocks must be marked `unsafe`; attributes like `no_mangle` and `export_name` must use `unsafe(...)` syntax; the `unsafe_op_in_unsafe_fn` lint now warns by default (requiring explicit `unsafe` blocks inside unsafe functions); and references to `static mut` are denied by default.

# Core Definition

The 2024 Edition strengthens Rust's safety model by requiring more explicit acknowledgment of unsafe operations across four areas:

**1. Unsafe `extern` blocks (RFC 3484):** `extern` blocks must be prefixed with `unsafe` to emphasize that the author is responsible for ensuring signature correctness. Items within can be marked `safe` or `unsafe` individually. Items without annotation default to `unsafe`.

```rust
unsafe extern "C" {
    pub safe fn sqrt(x: f64) -> f64;      // callable without unsafe block
    pub unsafe fn strlen(p: *const c_char) -> usize;  // explicitly unsafe
    pub fn free(p: *mut c_void);           // defaults to unsafe
    pub safe static IMPORTANT_BYTES: [u8; 256];
}
```

**2. Unsafe attributes (RFC 3325):** The `export_name`, `link_section`, and `no_mangle` attributes must use `#[unsafe(...)]` syntax because they affect symbol names and linking behavior, which can cause undefined behavior if incorrect (e.g., `#[export_name = "malloc"]` on a safe function can crash programs).

```rust
#[unsafe(no_mangle)]
pub fn example() {}
```

**3. `unsafe_op_in_unsafe_fn` warning (RFC 2585):** The `unsafe_op_in_unsafe_fn` lint now warns by default. Previously, the `unsafe fn` keyword served two roles: declaring that calling the function requires `unsafe`, and allowing unsafe operations inside the function body. The 2024 Edition separates these: `unsafe fn` still marks the function as requiring unsafe to call, but unsafe operations inside must be wrapped in explicit `unsafe {}` blocks.

**4. Disallow `static mut` references:** The `static_mut_refs` lint is now `deny` by default. Taking a reference (`&` or `&mut`) to a `static mut` is instantaneous undefined behavior because it violates Rust's mutability XOR aliasing requirement. Alternatives include atomics, `Mutex`/`RwLock`, `OnceLock`/`LazyLock`, or raw pointers via `&raw const`/`&raw mut`.

# Prerequisites

- **Rust editions** -- understanding the edition migration mechanism

# Key Properties

1. All four changes share the theme of making unsafe operations more visible and explicit
2. Unsafe extern blocks can annotate individual items as `safe` or `unsafe`
3. The `unsafe(...)` attribute syntax was available since Rust 1.82 in all editions
4. `unsafe_op_in_unsafe_fn` requires explicit `unsafe {}` blocks inside `unsafe fn` bodies
5. `static mut` references are denied, not just warned -- this is the strictest of the four changes
6. Taking a reference to `static mut` is UB even if the reference is never read or written
7. Reasoning about `static mut` safety requires global reasoning about the entire program
8. All four changes have corresponding lints in the `rust-2024-compatibility` group for migration

# Construction / Recognition

## Migrating Extern Blocks:

```rust
// Before (2021):
extern "C" { fn free(p: *mut c_void); }

// After (2024):
unsafe extern "C" { pub fn free(p: *mut c_void); }
```

## Migrating Unsafe Attributes:

```rust
// Before (2021):
#[no_mangle]
pub fn example() {}

// After (2024):
#[unsafe(no_mangle)]
pub fn example() {}
```

## Migrating Unsafe Operations in Unsafe Functions:

```rust
// Before (2021):
unsafe fn get_unchecked<T>(x: &[T], i: usize) -> &T {
    x.get_unchecked(i)  // allowed without unsafe block
}

// After (2024):
unsafe fn get_unchecked<T>(x: &[T], i: usize) -> &T {
    unsafe { x.get_unchecked(i) }  // explicit unsafe block required
}
```

## Replacing `static mut`:

```rust
// Before: static mut COUNTER: u64 = 0;
// After (using atomics):
use std::sync::atomic::{AtomicU64, Ordering};
static COUNTER: AtomicU64 = AtomicU64::new(0);

// After (using Mutex for complex types):
use std::sync::Mutex;
static QUEUE: Mutex<VecDeque<String>> = Mutex::new(VecDeque::new());

// After (using raw pointers when necessary):
let ptr = &raw const X;  // instead of &X for static mut X
```

# Context & Application

These changes reflect a longstanding Rust community consensus that unsafe should be visible at the point of use, not implicit. The `unsafe fn` keyword historically served as both a marker for callers and a blanket permission for the function body, which led to accidentally performing unsafe operations without documenting their safety invariants.

The `static mut` restriction is the most impactful for embedded and systems programming, where mutable global state is sometimes unavoidable. The recommended replacements (atomics, `Mutex`, `OnceLock`/`LazyLock`, `UnsafeCell` with raw pointers) provide locally-reasoned abstractions rather than requiring global reasoning about all accesses.

For FFI-heavy code, the unsafe extern and unsafe attribute changes require a one-time migration but improve documentation of safety contracts. The `safe` annotation on extern items is a new capability that can reduce unnecessary `unsafe` blocks at call sites.

# Examples

**Example 1** (unsafe extern with safe items): `unsafe extern "C" { pub safe fn sqrt(x: f64) -> f64; }` -- items marked `safe` can be called without an `unsafe` block.

**Example 2** (dangerous export_name): In 2021, `#[export_name = "malloc"] fn foo() -> usize { 1 }` is safe code that crashes on most platforms by replacing the allocator. In 2024, `unsafe(export_name = "malloc")` makes the danger visible.

**Example 3** (static mut UB): `static mut X: i32 = 23; unsafe { let y = &X; }` is instantaneous undefined behavior even if `y` is never used, because it creates a reference that violates aliasing requirements.

# Relationships

## Related
- **rust-2024-edition** -- these changes are part of the 2024 edition's safety theme

# Common Errors

- **Error**: Assuming `static_mut_refs` is just a style warning and can be silenced.
  **Correction**: Taking a reference to `static mut` is genuine undefined behavior. Use atomics, `Mutex`, or raw pointers instead.

- **Error**: Running `cargo fix --edition` for `static mut` and assuming the auto-generated `unsafe` blocks are correct.
  **Correction**: The automatic migration for `set_var`/`remove_var` wraps in `unsafe` blocks but cannot verify correctness. You must manually ensure these are called only in single-threaded contexts.

# Common Confusions

- **Confusion**: Thinking `unsafe extern` means all items in the block are unsafe to call.
  **Clarification**: Items can be individually marked `safe` (callable without `unsafe`) or `unsafe`. Items without annotation default to `unsafe`.

- **Confusion**: Thinking `unsafe_op_in_unsafe_fn` makes unsafe functions safe.
  **Clarification**: The function is still `unsafe` to call. The change only requires that unsafe operations within the body are wrapped in `unsafe {}` blocks, improving documentation of which specific operations are unsafe.

- **Confusion**: Thinking `static mut` references are only UB when there is actual concurrent access.
  **Clarification**: Merely taking a reference to `static mut` is instantaneous UB regardless of whether concurrent access actually occurs, because it creates a reference that the compiler assumes satisfies aliasing guarantees.

# Source Reference

Rust Edition Guide, Chapter 5: Rust 2024. Four sections: "Unsafe `extern` blocks" (RFC 3484), "Unsafe attributes" (RFC 3325), "`unsafe_op_in_unsafe_fn` warning" (RFC 2585), and "Disallow references to static mut." The `static mut` section includes extensive alternatives: atomics, Mutex/RwLock, OnceLock/LazyLock, UnsafeCell with raw pointers, and an embedded-specific single-core pattern.

# Verification Notes

- All four subsections drawn from their respective "Summary" and "Details" sections
- RFC numbers verified from the source text
- Code examples adapted from the source
- `static mut` UB characterization directly quoted: "merely taking such a reference... has always been instantaneous undefined behavior, even if the reference is never read from or written to"
- Confidence: HIGH -- each change is well-documented with clear before/after examples
- Cross-references: slugs verified against this extraction set
