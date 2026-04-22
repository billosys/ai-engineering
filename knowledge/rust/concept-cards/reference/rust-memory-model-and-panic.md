---
concept: Rust Memory Model and Panic
slug: rust-memory-model-and-panic
category: language-semantics
subcategory: memory-and-error-handling
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Memory Model / Panic"
chapter_number: 13-14
pdf_page: null
section: "Memory Model, Bytes, Memory Allocation, Variables, Panic, panic_handler, Panic Strategy, Unwinding, FFI Unwinding"
extraction_confidence: high
aliases:
  - "memory model"
  - "memory allocation"
  - "heap allocation"
  - "stack allocation"
  - "variables"
  - "local variables"
  - "panic"
  - "panic handler"
  - "unwind"
  - "abort"
  - "panic strategy"
  - "catch_unwind"
  - "FFI unwinding"
prerequisites:
  - rust-type-system
  - type-coercions-and-destructors
extends: []
related:
  - special-types-and-traits
contrasts_with: []
answers_questions:
  - "What is Rust's memory model?"
  - "What are the two kinds of bytes in Rust?"
  - "How does memory allocation work in Rust?"
  - "What is the difference between stack and heap allocation?"
  - "What are local variables and how are they initialized?"
  - "What happens when a Rust program panics?"
  - "What is the difference between unwind and abort panic strategies?"
  - "How does panic unwinding work?"
  - "What is a panic handler?"
  - "Can panics cross FFI boundaries?"
  - "How do you recover from a panic?"
  - "What is catch_unwind?"
---

# Quick Definition

Rust's memory model defines bytes as the basic unit of memory (either initialized with a `u8` value and optional provenance, or uninitialized). Memory is divided between compile-time items (static allocation), heap allocations (via `Box` and friends), and stack-local variables. Panic is Rust's mechanism for unrecoverable errors, with two strategies: unwinding (which runs destructors and is potentially recoverable via `catch_unwind`) and aborting (which terminates immediately).

# Core Definition

**Memory Model**: "The most basic unit of memory in Rust is a byte." (Ch. 13, "Bytes"). Each byte has one of two values: (1) an initialized byte containing a `u8` value with optional provenance, or (2) an uninitialized byte. The model is "abstract" -- Rust's bytes can make distinctions absent in hardware, "such as being uninitialized, or storing part of a pointer. Those distinctions can affect whether your program has undefined behavior."

> **Warning**: "The memory model of Rust is incomplete and not fully decided." (Ch. 13, intro)

**Memory Allocation and Lifetime**: Items (functions, modules, types) have values "calculated at compile-time and stored uniquely in the memory image of the rust process. Items are neither dynamically allocated nor freed." The heap "is a general term that describes boxes. The lifetime of an allocation in the heap depends on the lifetime of the box values pointing to it." Heap allocations may outlive their creating stack frame and are "guaranteed to reside at a single location in the heap for the whole lifetime of the allocation -- it will never be relocated as a result of moving a box value."

**Variables**: "A variable is a component of a stack frame, either a named function parameter, an anonymous temporary, or a named local variable." Local variables hold values directly within the stack frame's memory. Local variables are immutable unless declared with `mut`. Function parameters are immutable unless declared with `mut` (applies only to the following parameter). "Local variables are not initialized when allocated. Instead, the entire frame worth of local variables are allocated, on frame-entry, in an uninitialized state." Variables can only be used after initialization through all reachable control flow paths.

**Panic**: "Rust provides a mechanism to prevent a function from returning normally, and instead 'panic,' which is a response to an error condition that is typically not expected to be recoverable within the context in which the error is encountered." (Ch. 14, intro). Some language constructs (like out-of-bounds array indexing) panic automatically.

**The `panic_handler` attribute**: Applied to a function with signature `fn(&PanicInfo) -> !` to define panic behavior. "There must be a single `panic_handler` function in the dependency graph." The standard library provides two handlers: `unwind` (potentially recoverable) and `abort` (non-recoverable). Linking a `no_std` binary requires specifying a custom panic handler.

**Panic Strategy**: "The panic strategy defines the kind of panic behavior that a crate is built to support." Set via the `-C panic` CLI flag. The `abort` strategy allows the optimizer to "assume that unwinding across Rust frames is impossible, which can result in both code-size and runtime speed improvements." Crates built with `unwind` can use the `abort` handler, but `abort`-strategy crates cannot use the `unwind` handler.

**Unwinding**: "Panicking may either be recoverable or non-recoverable." The `unwind` handler "unwinds Rust frames, just as C++'s `throw` unwinds C++ frames, until the panic reaches the point of recovery." During unwinding, live objects with `Drop` implementations have their destructors called, ensuring resource cleanup. Two standard recovery mechanisms exist: `std::panic::catch_unwind` (recovers within the panicking thread) and `std::thread::spawn` (automatically recovers for the spawned thread so other threads continue running).

**FFI Unwinding**: Unwinding across FFI boundaries requires an appropriate ABI declaration (e.g., `extern "C-unwind"`). Unwinding with the wrong ABI is undefined behavior. Catching a foreign unwinding operation (e.g., C++ exception) via `catch_unwind` has unspecified behavior: either the process aborts or the function returns `Result::Err` with an opaque type. "An unwind originated from a Rust runtime must either lead to termination of the process or be caught by the same runtime."

# Prerequisites

- **rust-type-system** -- memory layout of types determines allocation behavior
- **type-coercions-and-destructors** -- destructors run during panic unwinding

# Key Properties

1. Rust bytes are abstract: they can be initialized (with `u8` value + optional provenance) or uninitialized
2. The memory model is explicitly incomplete and not fully decided
3. Items are statically allocated; they are never dynamically allocated or freed
4. Heap allocations via `Box` are never relocated during their lifetime
5. Stack variables are allocated uninitialized at frame entry; they must be initialized before use through all control flow paths
6. Local variables are immutable by default; `mut` is required for mutability
7. `fn(&PanicInfo) -> !` is the required signature for a panic handler
8. Exactly one `panic_handler` must exist in the dependency graph
9. `unwind` strategy runs destructors during unwinding, enabling resource cleanup
10. `abort` strategy terminates immediately with no destructors; enables optimizer improvements
11. `catch_unwind` can recover from panics within the panicking thread
12. `thread::spawn` automatically sets up panic recovery per-thread
13. FFI unwinding requires unwinding-compatible ABIs (`extern "C-unwind"`); wrong ABI causes undefined behavior
14. Foreign exceptions caught by Rust may either abort the process or return an opaque `Err`; behavior is unspecified

# Construction / Recognition

## Panic Recovery Patterns

```rust
// Pattern 1: catch_unwind for in-thread recovery
use std::panic;
let result = panic::catch_unwind(|| {
    // Code that might panic
    panic!("oh no");
});
assert!(result.is_err());

// Pattern 2: Thread-based isolation
let handle = std::thread::spawn(|| {
    panic!("thread panic");
});
// Other threads continue running; join returns Err
let result = handle.join();
assert!(result.is_err());
```

## Panic Strategy Selection

| Strategy | Destructors | Recoverable | Code size | Runtime cost |
|----------|-------------|-------------|-----------|--------------|
| `unwind` | Run during unwinding | Via `catch_unwind` / threads | Larger | Higher |
| `abort` | Not run | Never | Smaller | Lower |

Set via: `rustc -C panic=unwind` or `rustc -C panic=abort`

## FFI Boundary Safety

| Scenario | ABI | Result |
|----------|-----|--------|
| Rust panic through `extern "C"` | UB | Undefined behavior |
| Rust panic through `extern "C-unwind"` | Safe | Unwinds across boundary |
| C++ exception into Rust via `catch_unwind` | Unspecified | Abort or opaque `Err` |

## `no_std` Panic Handler

```rust
#![no_std]
use core::panic::PanicInfo;

#[panic_handler]
fn panic(info: &PanicInfo) -> ! {
    // Log, halt, or loop forever
    loop {}
}
```

# Context & Application

- **Typical contexts**: Understanding stack vs heap allocation, designing robust error handling, writing `no_std` code, FFI interoperability.
- **Common applications**: Choosing between `unwind` and `abort` for production binaries (abort for smaller binaries, unwind for libraries that must clean up resources); using `catch_unwind` at FFI boundaries to prevent panics from crossing into C code; writing custom panic handlers for embedded/`no_std` targets.
- **Embedded/`no_std`**: In `no_std` environments, a custom `#[panic_handler]` is required. The `abort` strategy is common since unwinding infrastructure may not be available on the target platform.

# Examples

**Example 1** -- Variable initialization (Ch. 13, "Variables"):
```rust
fn initialization_example() {
    let init_after_if: ();
    let uninit_after_if: ();

    if random_bool() {
        init_after_if = ();
        uninit_after_if = ();
    } else {
        init_after_if = ();
    }

    init_after_if;       // OK: initialized on all paths
    // uninit_after_if;  // ERROR: possibly uninitialized
}
```

**Example 2** -- Custom panic handler (Ch. 14, "panic_handler"):
```rust
#![no_std]
use core::fmt::{self, Write};
use core::panic::PanicInfo;

#[panic_handler]
fn panic(info: &PanicInfo) -> ! {
    let mut sink = Sink::new();
    let _ = writeln!(sink, "{}", info);
    loop {}
}
```

**Example 3** -- FFI unwinding boundary (Ch. 14, "Unwinding across FFI boundaries"):

Unwinding with the wrong ABI is undefined behavior:
- Causing an unwind into Rust from a foreign function called via non-unwinding ABI (e.g., `"C"`)
- Calling a Rust `extern "C-unwind"` function from code compiled with `-fno-exceptions`

Use `extern "C-unwind"` when panics or exceptions must cross the boundary.

**Example 4** -- Panic strategy tradeoff:

```toml
# Cargo.toml - abort for release builds (smaller, faster)
[profile.release]
panic = "abort"

# Cargo.toml - unwind for dev builds (better diagnostics)
[profile.dev]
panic = "unwind"
```

# Relationships

## Builds Upon
- **rust-type-system** -- types determine memory layout and allocation requirements
- **type-coercions-and-destructors** -- destructors are the primary mechanism invoked during panic unwinding

## Enables
No directly enabled cards within this batch.

## Related
- **special-types-and-traits** -- `Drop` trait's destructor is invoked during unwinding; `UnwindSafe` and `RefUnwindSafe` are auto traits related to panic safety

## Contrasts With
No direct contrasts within scope.

# Common Errors

- **Error**: Assuming panics in one thread crash the entire process.
  **Correction**: With the `unwind` strategy, panics are contained within the thread. Other threads continue running. The panic is captured by `thread::join()` returning `Err`.

- **Error**: Using `extern "C"` for Rust functions that might panic when called from C.
  **Correction**: Use `extern "C-unwind"` if the function might panic, or catch panics at the boundary with `catch_unwind`. Unwinding through `extern "C"` is undefined behavior.

- **Error**: Expecting destructors to run when using `abort` panic strategy.
  **Correction**: With `abort`, the process terminates immediately. No destructors are run. Use `unwind` if resource cleanup is needed.

# Common Confusions

- **Confusion**: `catch_unwind` is Rust's equivalent of try/catch and should be used for normal error handling.
  **Clarification**: `catch_unwind` is designed for FFI boundaries and thread isolation. For normal error handling, use `Result<T, E>`. Panic is for truly unexpected, unrecoverable conditions.

- **Confusion**: Moving a `Box` relocates the heap allocation.
  **Clarification**: "An allocation in the heap is guaranteed to reside at a single location in the heap for the whole lifetime of the allocation -- it will never be relocated as a result of moving a box value." Moving a `Box` copies the pointer, not the heap data.

- **Confusion**: The Rust memory model is fully specified.
  **Clarification**: The reference explicitly warns: "The memory model of Rust is incomplete and not fully decided." Abstract byte semantics (provenance, uninitialized memory) are still being formalized.

# Source Reference

The Rust Reference, Chapter 13: Memory Model (Bytes, Memory Allocation and Lifetime, Variables) and Chapter 14: Panic (panic_handler, Panic Strategy, Unwinding, FFI Unwinding).

# Verification Notes

- Definition source: Direct from Ch. 13 and Ch. 14 of The Rust Reference
- Confidence rationale: High for panic semantics (well-documented); medium-high for memory model (explicitly incomplete)
- Uncertainties: Memory model is officially incomplete; foreign exception handling behavior is unspecified between two options (abort or opaque Err)
- Cross-reference status: Related cards verified against planned card slugs
