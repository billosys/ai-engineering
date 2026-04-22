---
concept: Linkage
slug: rust-linkage
category: compilation
subcategory: linking
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Linkage"
chapter_number: 15
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "crate types"
  - "static linking"
  - "dynamic linking"
  - "rlib"
  - "staticlib"
  - "cdylib"
  - "dylib"
prerequisites: []
extends: []
related:
  - rust-abi-and-runtime
  - nomicon-ffi
contrasts_with: []
answers_questions:
  - "What crate types does Rust support and when should each be used?"
  - "How does the compiler choose between rlib and dylib formats for dependencies?"
  - "How do you statically or dynamically link the C runtime?"
  - "How do you link Rust code into a non-Rust application?"
  - "What are the rules for panic unwinding across linked artifacts?"
---

# Quick Definition

Rust supports seven crate types (bin, lib, rlib, dylib, staticlib, cdylib, proc-macro) that control how compiled output is produced and linked. The compiler follows specific rules for resolving dependency formats, managing C runtime linkage, and ensuring unwinding consistency across linked artifacts.

# Core Definition

The compiler can generate multiple artifact types in a single compilation session via `--crate-type` flags or `#![crate_type = "..."]` attributes. Command-line flags override attributes when both are specified. The crate types are:

- **bin** (default): Runnable executable. Links in all Rust and native dependencies into a single distributable binary. Requires a `main` function.
- **lib**: Compiler-recommended library format (alias for one of the concrete types).
- **rlib**: Intermediate "Rust library" containing metadata for `rustc` to consume. Does not embed upstream dependencies. Used for statically linked executables and staticlib outputs.
- **dylib**: Dynamic Rust library (`.so`/`.dylib`/`.dll`). Can be used as a dependency by other Rust libraries and executables.
- **staticlib**: Static system library containing all local crate code plus all upstream dependencies. Intended for linking into non-Rust applications. Produces `.a` or `.lib` files. Dynamic dependencies must be specified manually when linking.
- **cdylib**: Dynamic system library for loading from other languages. Produces `.so`/`.dylib`/`.dll`.
- **proc-macro**: Procedural macro crate, always compiled for the compiler's host target regardless of the cross-compilation target.

For dependency resolution, the compiler looks only for `rlib` and `dylib` formats. Static libraries require all dependencies in `rlib` format. Executables prefer `rlib` unless `-C prefer-dynamic` is set. When dynamically linking, the compiler ensures no library appears more than once in the final artifact.

# Prerequisites

General familiarity with Rust compilation and the difference between static and dynamic linking. Understanding of FFI is helpful for staticlib/cdylib use cases.

# Key Properties

1. Multiple crate types can be produced from one compilation without recompilation, but only when specified by the same method (all via attributes or all via flags)
2. `staticlib` bundles all upstream dependencies and exports all public symbols; the resulting library may need linker scripts or symbol filtering when embedded in shared libraries
3. `rlib` files do not contain upstream dependencies -- they only contain metadata and the current crate's code
4. `cdylib` is specifically designed for C-ABI-compatible dynamic libraries loaded from foreign languages
5. `proc-macro` crates are always compiled for the host target, not the cross-compilation target
6. The C runtime can be statically or dynamically linked via `-C target-feature=+crt-static` or `-crt-static`; musl targets default to static, most others to dynamic
7. The `crt-static` target feature is detectable at compile time via `#[cfg(target_feature = "crt-static")]` and in Cargo build scripts via `CARGO_CFG_TARGET_FEATURE`
8. A Rust artifact is "potentially unwinding" if it uses the `unwind` panic handler, calls `-unwind` ABI functions, or calls into another potentially unwinding Rust artifact
9. If a Rust artifact is potentially unwinding, all its crates must be built with the `unwind` panic strategy; otherwise UB results

# Construction / Recognition

## Choosing a Crate Type

1. For standalone programs: use `bin` (the default)
2. For Rust-to-Rust library dependencies: use `lib` (lets the compiler choose) or `rlib` (for static-only linking)
3. For embedding Rust in C/C++ applications: use `staticlib` (static) or `cdylib` (dynamic)
4. For Rust dynamic libraries consumed by Rust: use `dylib`
5. For procedural macros: use `proc-macro`
6. Use `--crate-type=bin` or `--crate-type=lib` for most needs; other types provide fine-grained control

## Mixing Rust and Foreign Code

1. Using `rustc` as linker: pass non-Rust libraries via `-L` and `-l` flags or `#[link]` directives; pass `.o` files via `-Clink-arg=file.o`
2. Using a foreign linker: generate a single Rust `staticlib` and pass it to the foreign linker; do not use multiple Rust `staticlib` files as they will conflict
3. Passing `rlib` files directly to a foreign linker is unsupported
4. Code compiled with a different Rust runtime instance counts as "foreign code"

# Context & Application

Linkage control is primarily a compiler concern rather than a language-level feature, but it directly affects how Rust code integrates with the broader software ecosystem. The staticlib and cdylib types are essential for FFI scenarios -- embedding Rust in C/C++ projects, creating Python extensions, building WebAssembly modules, or producing plugins for non-Rust host applications. The distinction between rlib and dylib affects binary size, compilation time, and deployment complexity. The C runtime linkage choice matters for portability (musl for static, glibc for dynamic on Linux) and for Windows MSVC builds where `/MT` vs `/MD` flags must match.

# Examples

**Example 1** (Crate type attribute):
```rust
#![crate_type = "staticlib"]
// All code in this crate plus all upstream dependencies
// will be bundled into a single .a or .lib file
pub fn add(a: i32, b: i32) -> i32 { a + b }
```

**Example 2** (Detecting C runtime linkage in a build script):
```rust
use std::env;
fn main() {
    let linkage = env::var("CARGO_CFG_TARGET_FEATURE").unwrap_or(String::new());
    if linkage.contains("crt-static") {
        println!("the C runtime will be statically linked");
    } else {
        println!("the C runtime will be dynamically linked");
    }
}
```

**Example 3** (Static C runtime on MSVC via Cargo):
```sh
RUSTFLAGS='-C target-feature=+crt-static' cargo build --target x86_64-pc-windows-msvc
```

# Relationships

## Builds Upon
(none -- linkage is a foundational compilation concept)

## Enables
- **rust-abi-and-runtime** -- ABI attributes like `no_mangle` and `export_name` control how linked symbols appear
- **nomicon-ffi** -- staticlib and cdylib are the primary mechanisms for FFI linking

## Related
- **rust-inline-assembly** -- inline assembly interacts with linking via `global_asm!` which emits code at global scope

## Contrasts With
(none)

# Common Errors

- **Error**: Creating multiple `staticlib` outputs from separate Rust crates and linking them into the same binary.
  **Correction**: Multiple Rust staticlibs are likely to conflict because each bundles all upstream dependencies including the standard library. Use a single staticlib with `extern crate` to pull in multiple rlibs.

- **Error**: Forgetting to specify dynamic dependencies when linking a `staticlib` into an external application.
  **Correction**: Use `--print=native-static-libs` to discover which system libraries the staticlib depends on and specify them manually to the linker.

# Common Confusions

- **Confusion**: Thinking `lib` and `rlib` are the same thing.
  **Clarification**: `lib` is an alias that lets the compiler choose the best format (currently `rlib`). `rlib` explicitly requests the Rust-specific static library format. The actual output of `lib` may change between compiler versions.

- **Confusion**: Believing unwinding behavior is always safe across linked artifacts.
  **Clarification**: If any part of a Rust artifact can unwind, all crates in that artifact must use the `unwind` panic strategy. Mixing panic strategies can cause undefined behavior. The `ffi_unwind_calls` lint helps identify problematic calls to `-unwind` foreign functions.

# Source Reference

Chapter 15 (Linkage): Crate types (bin, lib, rlib, dylib, staticlib, cdylib, proc-macro), dependency resolution rules (4 cases), static and dynamic C runtimes (`crt-static` target feature), mixed Rust/foreign codebases (two linking approaches), prohibited linkage and unwinding rules.

# Verification Notes

- Definition source: Direct extraction from Chapter 15 (304 lines), all crate type descriptions are near-verbatim from source
- Key Properties: Items 1-9 synthesized from explicit source discussion of crate types, C runtime, and unwinding rules
- Confidence rationale: HIGH -- the source provides comprehensive, explicit definitions of all crate types with clear rules
- Uncertainties: The `lib` alias may change its underlying format; proc-macro output format is explicitly "not specified"
- Cross-reference status: Related slugs reference cards in the reference and nomicon extraction sets
