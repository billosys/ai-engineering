---
concept: "Beneath std: #![no_std], Runtime, and Panic Handlers"
slug: beneath-std
category: unsafe-rust
subcategory: runtime
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "12-beneath-std"
chapter_number: 12
pdf_page: null
section: "Using libc, Writing an executable without std, #[panic_handler]"
extraction_confidence: high
aliases:
  - "no_std"
  - "bare metal Rust"
  - "panic handler"
  - "eh_personality"
  - "lang items"
  - "no_main"
  - "freestanding Rust"
prerequisites: []
extends: []
related:
  - nomicon-ffi
contrasts_with: []
answers_questions:
  - "How do I write a Rust program without std?"
  - "What do I need to provide when using #![no_std]?"
  - "What is #[panic_handler] and how do I implement it?"
  - "What is the eh_personality lang item?"
  - "How do I use libc in a no_std context?"
  - "How do I define an entry point in a no_std binary?"
  - "What are panic crates and how do they work?"
  - "What is compiler_builtins and when is it needed?"
---

# Quick Definition

`#![no_std]` programs must provide what `std` normally supplies: an entry point (via `#![no_main]` plus a platform-appropriate main/`_start`/`WinMain`), a panic handler (`#[panic_handler]` with signature `fn(&PanicInfo) -> !`), and the `eh_personality` lang item for unwinding. The `libc` crate is used with `default-features = false` to avoid pulling in `std`. Panic behavior can be swapped between development and release by conditionally linking different "panic crates."

# Core Definition

"This section documents features that are normally provided by the `std` crate and that `#![no_std]` developers have to deal with (i.e. provide) to build `#![no_std]` binary crates." (Ch. 12, introduction)

A `#![no_std]` executable requires: (1) a nightly compiler because "on many platforms, we have to provide the `eh_personality` lang item, which is unstable"; (2) `#![no_main]` with a manually defined entry point appropriate for the target; (3) a `#[panic_handler]` function with signature `fn(&PanicInfo) -> !` that "must appear once in the dependency graph of a binary / dylib / cdylib crate"; and (4) the `libc` crate with `default-features = false` because "the default features of `libc` include the `std` crate and so must be disabled." (Ch. 12, Using libc, Writing an executable without std, #[panic_handler])

# Prerequisites

None -- this chapter is self-contained, though familiarity with Rust's build system and the distinction between `core`, `alloc`, and `std` is helpful.

# Key Properties

1. **libc dependency**: Must use `default-features = false` in Cargo.toml because libc's default features include std; alternatively, use the unstable `rustc_private` feature with `extern crate libc`
2. **Windows exception**: Windows-msvc targets do not require libc and have no `libc` crate in their sysroot; `extern crate libc` on these targets is a compile error
3. **Nightly requirement**: Needed because `eh_personality` is an unstable lang item; required features include `lang_items`, `core_intrinsics`, `rustc_private`
4. **Entry point**: Use `#![no_main]` and define an `extern "C" fn main(_argc: c_int, _argv: *const *const c_char) -> c_int` (or `_start`, `WinMain`, etc. depending on target)
5. **eh_personality**: A lang item for the unwinding personality function; must be provided as `#[lang = "eh_personality"] fn rust_eh_personality() {}`; necessary for `panic = "unwind"` builds
6. **#[panic_handler]**: Required function with signature `fn(&PanicInfo) -> !`; defines what happens on panic; must appear exactly once in the dependency graph
7. **Panic crates**: Crates that contain only a `#[panic_handler]`; allow swapping panic behavior by linking different crates for dev vs release (e.g., `panic-semihosting` for development, `panic-halt` for release)
8. **Conditional panic crate selection**: Use `#[cfg(debug_assertions)] extern crate panic_semihosting` and `#[cfg(not(debug_assertions))] extern crate panic_halt` to switch behavior between dev and release builds
9. **compiler_builtins**: Required when building for targets without binary releases of the standard library; provides compiler-rt intrinsics to resolve linker errors like `undefined reference to '__aeabi_memcpy'`
10. **Panic unwind support**: On cfg(unix) platforms with `panic = "unwind"`, must include `extern crate unwind` with `#![feature(panic_unwind)]`

# Construction / Recognition

## To Create a #![no_std] Binary:
1. Add `#![no_std]` and `#![no_main]` to the crate root
2. Add `libc = { version = "0.2", default-features = false }` to Cargo.toml (non-Windows)
3. Define an entry point function with `#[unsafe(no_mangle)] extern "C" fn main(...)` or platform equivalent
4. Implement a `#[panic_handler]` function: `fn panic(_info: &PanicInfo) -> ! { loop {} }` or similar
5. Provide `#[lang = "eh_personality"] fn rust_eh_personality() {}` (requires nightly + `#![feature(lang_items)]`)
6. For `panic = "unwind"` on unix: add `#![feature(panic_unwind)]` and `extern crate unwind`

## To Create Swappable Panic Crates:
1. Create a crate containing only `#![no_std]` and a `#[panic_handler]` function
2. Choose panic behavior: halt (loop), semihosting (log to host), abort, custom
3. In the application, conditionally link: `#[cfg(debug_assertions)] extern crate panic_semihosting`

## To Handle Missing compiler_builtins:
1. If getting linker errors like `undefined reference to '__aeabi_memcpy'`
2. Add the `compiler_builtins` crate as a dependency
3. This provides compiler-rt intrinsics normally supplied by the standard library

# Context & Application

This short chapter addresses the requirements for freestanding Rust programs -- binaries that run without the standard library. This is the domain of embedded systems, operating system kernels, bootloaders, and other bare-metal applications.

The key insight is that `std` provides three categories of runtime support: (1) the entry point and process setup, (2) panic handling and unwinding infrastructure, and (3) compiler intrinsics. A `#![no_std]` program must provide all of these itself or through explicit dependencies.

The "panic crate" pattern is a practical architectural recommendation: by isolating panic behavior into separate crates, embedded applications can swap between verbose debugging output (semihosting) and minimal release behavior (halt or abort) through Cargo profile configuration alone, without changing application code.

The chapter is notably brief (165 lines) and focused on the practical requirements rather than the theory. It serves as a checklist for what must be provided when `std` is absent.

# Examples

**Example 1** (Ch. 12, Minimal no_std executable): Complete freestanding binary:
```rust
#![feature(lang_items, core_intrinsics, rustc_private)]
#![allow(internal_features)]
#![no_std]
#![no_main]

#![feature(panic_unwind)]
extern crate unwind;

#[cfg(not(windows))]
extern crate libc;

use core::ffi::{c_char, c_int};
use core::panic::PanicInfo;

#[unsafe(no_mangle)]
extern "C" fn main(_argc: c_int, _argv: *const *const c_char) -> c_int { 0 }

#[lang = "eh_personality"]
fn rust_eh_personality() {}

#[panic_handler]
fn panic_handler(_info: &PanicInfo) -> ! { core::intrinsics::abort() }
```

**Example 2** (Ch. 12, Panic crate -- semihosting): Development panic handler:
```rust
#![no_std]
use core::fmt::Write;
use core::panic::PanicInfo;

#[panic_handler]
fn panic(info: &PanicInfo) -> ! {
    let mut host_stderr = HStderr::new();
    writeln!(host_stderr, "{}", info).ok();
    loop {}
}
```

**Example 3** (Ch. 12, Conditional panic selection): Swapping panic behavior by profile:
```rust
#![no_std]
#[cfg(debug_assertions)]
extern crate panic_semihosting;   // dev: log to host
#[cfg(not(debug_assertions))]
extern crate panic_halt;           // release: halt
```

# Relationships

## Builds Upon
- The `core` crate (always available, provides fundamental types and traits)
- The `libc` crate (for C runtime integration on non-Windows targets)
- Rust's lang items system (unstable, for providing compiler-required functions)

## Enables
- Bare-metal and embedded Rust development
- Operating system kernel development in Rust
- Custom runtime environments

## Related
- **nomicon-ffi** -- no_std programs often use FFI extensively for hardware access and C runtime integration

## Contrasts With
- Normal `std`-based Rust programs that get all runtime support automatically
- Programs using `#![no_std]` with `alloc` (which provides heap allocation but not the full runtime)

# Common Errors

- **Error**: Using `libc` with default features in a no_std context.
  **Correction**: "The default features of `libc` include the `std` crate and so must be disabled." Use `libc = { version = "0.2", default-features = false }` in Cargo.toml.

- **Error**: Defining multiple `#[panic_handler]` functions in the dependency graph.
  **Correction**: The panic handler "must appear once in the dependency graph of a binary / dylib / cdylib crate." If multiple panic crates are linked, use `#[cfg]` to ensure only one is active.

- **Error**: Using `extern crate libc` on a Windows-msvc target.
  **Correction**: "Windows-msvc targets do not require a libc, and correspondingly there is no `libc` crate in their sysroot." Guard with `#[cfg(not(windows))]`.

# Common Confusions

- **Confusion**: Thinking `#![no_std]` means no heap allocation is possible.
  **Clarification**: `#![no_std]` removes `std` but the `alloc` crate can still be used for heap allocation if a global allocator is provided. The `core` crate is always available.

- **Confusion**: Thinking the panic handler must halt or abort.
  **Clarification**: The signature requires `-> !` (never returns), but the implementation can loop indefinitely, log to a host, trigger a debugger breakpoint, or perform any other diverging action. The "panic crate" pattern encourages different behaviors for different build profiles.

- **Confusion**: Thinking `eh_personality` is only needed for panic=abort builds.
  **Clarification**: The opposite -- `eh_personality` is the unwinding personality function needed for `panic = "unwind"` builds. With `panic = abort`, it may not be required on all platforms, but the chapter includes it for completeness.

# Source Reference

Chapter 12: Beneath std -- all sections: Using libc (default-features, Windows exception), Writing an executable without std (no_main, entry point, eh_personality, lang items, compiler_builtins), #[panic_handler] (signature, panic crates, conditional linking by build profile).

# Verification Notes

- Definition source: Direct quotations from Ch. 12 introduction and subsections
- Key Properties: Covers all topics in the 165-line chapter
- Confidence rationale: HIGH -- short, focused chapter with clear requirements and complete code examples
- Uncertainties: Some features are nightly-only and may stabilize or change (lang_items, rustc_private)
- Cross-reference status: `nomicon-ffi` is in this extraction set
