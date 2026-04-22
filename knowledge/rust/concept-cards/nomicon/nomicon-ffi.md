---
concept: "Foreign Function Interface (FFI)"
slug: nomicon-ffi
category: unsafe-rust
subcategory: interoperability
tier: intermediate
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "11-ffi"
chapter_number: 11
pdf_page: null
section: "Calling foreign functions, Creating a safe interface, Calling Rust from C, Callbacks, Linking, Foreign calling conventions, Variadic functions, Nullable pointer optimization, FFI and unwinding, Opaque structs"
extraction_confidence: high
aliases:
  - "Rust FFI"
  - "extern C"
  - "calling conventions"
  - "repr(C)"
  - "no_mangle"
  - "C interop"
  - "Rust from C"
  - "C-unwind"
  - "opaque types FFI"
  - "nullable pointer optimization"
prerequisites: []
extends: []
related:
  - ffi-accepting-strings
  - ffi-passing-strings
  - ffi-error-handling
  - ffi-object-based-api
  - ffi-type-consolidation
  - contain-unsafety
contrasts_with: []
answers_questions:
  - "How do I call C functions from Rust?"
  - "How do I call Rust functions from C?"
  - "What calling conventions does Rust support?"
  - "How do I create a safe wrapper around unsafe FFI functions?"
  - "How do I pass callbacks between Rust and C?"
  - "How do I represent opaque C structs in Rust?"
  - "What is the nullable pointer optimization and how does it help FFI?"
  - "What happens when a panic crosses an FFI boundary?"
  - "How do I link to native libraries in Rust?"
  - "How do I access foreign global variables?"
  - "How do I use variadic C functions from Rust?"
  - "What is extern C-unwind?"
---

# Quick Definition

Rust's FFI system uses `extern "C"` blocks with `#[link]` attributes to declare and link foreign functions, `#[unsafe(no_mangle)] pub extern "C" fn` to export Rust functions to C, and `#[repr(C)]` to ensure struct layout compatibility. Foreign functions are inherently unsafe. Safe wrappers convert between Rust types (slices, Vec, Option) and C types (raw pointers, size_t). The nullable pointer optimization allows `Option<extern "C" fn(...)>` to represent nullable C function pointers with zero overhead. Unwinding across non-`-unwind` ABI boundaries causes abort (for panic) or undefined behavior (for foreign exceptions).

# Core Definition

"The `extern` block is a list of function signatures in a foreign library, in this case with the platform's C ABI. The `#[link(...)]` attribute is used to instruct the linker to link against the snappy library so the symbols can be resolved." (Ch. 11, Calling foreign functions) "Foreign functions are assumed to be unsafe so calls to them need to be wrapped with `unsafe {}` as a promise to the compiler that everything contained within truly is safe." (Ch. 11, Calling foreign functions)

For calling Rust from C: "The `extern "C"` makes this function adhere to the C calling convention. The `no_mangle` attribute turns off Rust's name mangling, so that it has a well defined symbol to link to." (Ch. 11, Calling Rust code from C) Struct interoperability requires `#[repr(C)]`: "Rust guarantees that the layout of a `struct` is compatible with the platform's representation in C only if the `#[repr(C)]` attribute is applied to it." (Ch. 11, Interoperability)

# Prerequisites

None -- this chapter is self-contained, though understanding of raw pointers and `unsafe` is assumed.

# Key Properties

1. **extern blocks**: Declare foreign function signatures; all functions in an `extern "C"` block are implicitly unsafe; the `#[link(name = "...")]` attribute specifies which native library to link
2. **Safe wrappers**: Wrap raw C API calls in safe Rust functions -- e.g., take `&[u8]` instead of `*const u8 + size_t`, return `Option<Vec<u8>>` instead of error codes
3. **Calling Rust from C**: Use `#[unsafe(no_mangle)]` + `extern "C"` on the function; set `crate-type = ["cdylib"]` in Cargo.toml; compile with `cargo build`
4. **Callbacks**: Mark callback functions as `extern "C"`; pass as function pointers across the FFI boundary; for object-targeted callbacks, pass a `*mut RustObject` alongside the function pointer
5. **Async callbacks from C threads**: Require proper synchronization (mutexes, channels); must unregister callbacks before the Rust object is destroyed
6. **Link kinds**: Dynamic (`#[link(name = "readline")]`), Static (`#[link(name = "foo", kind = "static")]`), Framework (`#[link(name = "CoreFoundation", kind = "framework")]` -- macOS only)
7. **Calling conventions**: `extern "C"` (default), `extern "stdcall"`, `extern "system"` (stdcall on win32/x86, C elsewhere), and others (aapcs, cdecl, fastcall, thiscall, vectorcall, win64, sysv64, Rust)
8. **repr(C)**: Required for struct layout compatibility; `#[repr(C, packed)]` removes padding; applies to enums too
9. **Variadic functions**: Declared with `...` in extern blocks (e.g., `fn foo(x: i32, ...)`); normal Rust functions cannot be variadic
10. **Nullable pointer optimization**: `Option<T>` where T is a non-nullable type (references, Box, function pointers) has the same representation as a nullable pointer -- `None` is null, `Some(x)` is the pointer value; `Option<extern "C" fn(c_int) -> c_int>` correctly represents a nullable C function pointer
11. **Foreign globals**: Accessed via `static` (immutable) or `static mut` (mutable) in extern blocks; all interaction with `static mut` is unsafe
12. **FFI and unwinding**: `-unwind` ABI variants (e.g., `extern "C-unwind"`) permit unwinding across the boundary; without `-unwind`, panic aborts the process and foreign exceptions cause UB; `catch_unwind` can preemptively catch panics before they reach the boundary
13. **Opaque structs**: Represented as `#[repr(C)] struct Foo { _data: (), _marker: PhantomData<(*mut u8, PhantomPinned)> }` -- private field prevents external construction; marker prevents Send/Sync/Unpin; never use empty enums (they are uninhabited and trigger UB)

# Construction / Recognition

## To Call C from Rust:
1. Declare functions in an `unsafe extern "C" { ... }` block
2. Add `#[link(name = "library_name")]` to specify the native library
3. Call the foreign functions inside `unsafe { ... }` blocks
4. Create safe wrapper functions that handle type conversions and error checking

## To Call Rust from C:
1. Mark the function with `#[unsafe(no_mangle)]` and `extern "C"`
2. Set `crate-type = ["cdylib"]` (or `"staticlib"`) in Cargo.toml
3. Compile with `cargo build`
4. Link from C with `-l` and `-L` flags; set `LD_LIBRARY_PATH` at runtime
5. For automated header generation, use the `cbindgen` tool

## To Handle Callbacks:
1. Mark callback functions as `extern "C"` (or `unsafe extern "C"` if they access raw pointers)
2. Pass function pointers across FFI -- the type is `extern "C" fn(args) -> ret`
3. For object-targeted callbacks, pass a `*mut RustObject` as a context pointer alongside the callback
4. For async callbacks from C threads, use channels or mutexes for synchronization

## To Represent Opaque C Structs:
1. Define `#[repr(C)] pub struct Foo { _data: (), _marker: PhantomData<(*mut u8, PhantomPinned)> }`
2. The private field prevents construction outside the module
3. The marker prevents Send, Sync, and Unpin auto-implementation
4. Never use empty enums -- they are uninhabited and cause UB when referenced

## To Handle Unwinding at FFI Boundaries:
1. If unwinding should cross the boundary, use `-unwind` variants: `extern "C-unwind"`
2. If not, use `catch_unwind` to convert panics to error codes before crossing
3. A panic crossing a non-unwind boundary safely aborts; a foreign exception crossing into Rust is UB

# Context & Application

This chapter provides the comprehensive FFI reference for unsafe Rust, covering both directions (Rust calling C and C calling Rust), multiple calling conventions, and the subtleties of memory layout compatibility. It complements the design-patterns FFI cards (which focus on API design patterns like string handling and error conventions) by covering the underlying unsafe mechanics.

The nullable pointer optimization is highlighted as a particularly elegant feature: `Option<extern "C" fn(c_int) -> c_int>` is guaranteed to have the same representation as a nullable C function pointer, requiring "no `transmute` required!" This applies to any type that is guaranteed non-null: references, Box, and function pointers.

The unwinding section documents a critical safety boundary. The `C-unwind` ABI was introduced to allow Rust panics to safely unwind through C++ stack frames (calling destructors), and C++ exceptions to unwind through Rust frames (dropping Rust values). Without the `-unwind` suffix, panics abort and foreign exceptions are UB.

The opaque struct pattern is notable for what it avoids: "it is a really bad idea to use an empty enum as FFI type. The compiler relies on empty enums being uninhabited, so handling values of type `&Empty` is a huge footgun and can lead to buggy program behavior (by triggering undefined behavior)."

# Examples

**Example 1** (Ch. 11, Calling foreign functions): Declaring and calling a C library function:
```rust
use libc::size_t;
#[link(name = "snappy")]
unsafe extern "C" {
    fn snappy_max_compressed_length(source_length: size_t) -> size_t;
}
fn main() {
    let x = unsafe { snappy_max_compressed_length(100) };
    println!("max compressed length of a 100 byte buffer: {}", x);
}
```

**Example 2** (Ch. 11, Safe wrapper): Wrapping unsafe FFI in a safe API:
```rust
pub fn validate_compressed_buffer(src: &[u8]) -> bool {
    unsafe {
        snappy_validate_compressed_buffer(src.as_ptr(), src.len() as size_t) == 0
    }
}
```

**Example 3** (Ch. 11, Calling Rust from C): Exporting a Rust function for C:
```rust
#[unsafe(no_mangle)]
pub extern "C" fn hello_from_rust() {
    println!("Hello from Rust!");
}
```

**Example 4** (Ch. 11, Nullable pointer optimization): Zero-cost nullable function pointers:
```rust
extern "C" fn apply(process: Option<extern "C" fn(c_int) -> c_int>, int: c_int) -> c_int {
    match process {
        Some(f) => f(int),
        None    => int * int
    }
}
```

**Example 5** (Ch. 11, Catching panic): Preventing unwinding across FFI:
```rust
use std::panic::catch_unwind;
#[unsafe(no_mangle)]
pub extern "C" fn oh_no() -> i32 {
    let result = catch_unwind(|| { panic!("Oops!"); });
    match result { Ok(_) => 0, Err(_) => 1 }
}
```

# Relationships

## Builds Upon
- Raw pointers and `unsafe` blocks
- The `libc` crate for C type definitions
- Rust's type system (for safe wrappers over unsafe internals)

## Enables
- **ffi-accepting-strings** -- string conversion patterns build on the basic FFI mechanics
- **ffi-passing-strings** -- passing Rust strings to C builds on extern blocks and raw pointers
- **ffi-error-handling** -- error handling patterns build on safe wrapper design
- **ffi-object-based-api** -- object-oriented C API wrappers build on opaque struct patterns

## Related
- **ffi-type-consolidation** -- type wrapper patterns for FFI types
- **contain-unsafety** -- FFI is the primary domain where the "contain unsafety" principle applies

## Contrasts With
- Pure Rust APIs that do not cross language boundaries
- Higher-level FFI tools (cxx, diplomat, uniffi) that generate bindings automatically

# Common Errors

- **Error**: Using an empty enum to represent an opaque C struct.
  **Correction**: "The compiler relies on empty enums being uninhabited, so handling values of type `&Empty` is a huge footgun and can lead to buggy program behavior (by triggering undefined behavior)." Use a struct with a private field and PhantomData marker instead.

- **Error**: Allowing a Rust panic to unwind across an `extern "C"` (non-unwind) boundary.
  **Correction**: This causes the process to abort. If the foreign code needs to handle the error, use `catch_unwind` to convert panics to return codes, or use `extern "C-unwind"` if unwinding is intentional.

- **Error**: Omitting `#[repr(C)]` on structs passed across the FFI boundary.
  **Correction**: Without `#[repr(C)]`, Rust makes no guarantees about struct layout. The compiler may reorder fields or add unexpected padding.

- **Error**: Forgetting to unregister callbacks before destroying the Rust object they target.
  **Correction**: For asynchronous callbacks from C threads, "it is absolutely necessary that no more callbacks are performed by the C library after the respective Rust object gets destroyed." Unregister in the destructor.

# Common Confusions

- **Confusion**: Thinking `extern "system"` is always the same as `extern "C"`.
  **Clarification**: On win32 x86, `extern "system"` maps to `stdcall`, not C. On x86_64 windows and all other platforms, it maps to `extern "C"`. It is a convenience for cross-platform Windows API calls.

- **Confusion**: Thinking `Option<extern "C" fn(...)>` adds overhead compared to a raw function pointer.
  **Clarification**: The nullable pointer optimization guarantees that `Option` around any non-nullable type (references, Box, function pointers) has exactly the same size and representation as a raw pointer. None is null, Some is the pointer value.

- **Confusion**: Thinking `catch_unwind` catches foreign (C++) exceptions.
  **Clarification**: "The interaction of `catch_unwind` with foreign exceptions is undefined." `catch_unwind` only catches Rust panics. For C++ exceptions, the `-unwind` ABI variant is needed.

# Source Reference

Chapter 11: Foreign Function Interface -- all sections: Introduction (snappy example), Calling foreign functions (extern blocks, #[link]), Creating a safe interface (wrapper functions), Calling Rust from C (no_mangle, cdylib), Callbacks (function pointers, object-targeted, async), Linking (dynamic, static, framework), Unsafe blocks, Accessing foreign globals, Foreign calling conventions (stdcall, system, etc.), Interoperability with foreign code (repr(C), CString), Variadic functions, Nullable pointer optimization, FFI and unwinding (C-unwind, catch_unwind), Representing opaque structs.

# Verification Notes

- Definition source: Direct quotations from Ch. 11 introduction, calling conventions, and interoperability sections
- Key Properties: Comprehensive coverage of all chapter sections
- Confidence rationale: HIGH -- the chapter is thorough with code examples for each topic; some topics (extern types) are noted as unstable/future
- Uncertainties: Extern types are "currently unstable and have some unresolved questions" (noted in source, June 2021)
- Cross-reference status: Design-patterns FFI cards (ffi-accepting-strings, ffi-passing-strings, ffi-error-handling, ffi-object-based-api, ffi-type-consolidation) are in a separate extraction set and cover API design patterns rather than unsafe mechanics
