---
concept: Foreign Function Interface
slug: deno-ffi
category: interop
subcategory: native code
tier: advanced
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/ffi.md"
chapter_number: null
pdf_page: null
section: "Foreign Function Interface (FFI)"
extraction_confidence: high
aliases:
  - "Deno FFI"
  - "Deno.dlopen"
  - "Deno foreign function interface"
  - "--allow-ffi"
prerequisites:
  - deno-configuration
extends: []
related:
  - deno-http-server
contrasts_with: []
answers_questions:
  - "How do I use FFI in Deno?"
  - "How do I call native libraries from Deno?"
  - "What is Deno.dlopen?"
---

# Quick Definition

Deno's Foreign Function Interface (FFI) allows JavaScript and TypeScript code to call functions in native dynamic libraries (C, C++, Rust) via `Deno.dlopen()`, requiring the `--allow-ffi` permission flag since native code runs outside Deno's security sandbox.

# Core Definition

FFI provides a bridge between Deno's JavaScript runtime and native code compiled as dynamic libraries (`.so`, `.dylib`, `.dll`). The API is based on `Deno.dlopen()`, which loads a dynamic library and creates JavaScript bindings to the functions it exports.

The basic pattern involves three steps:
1. Define the interface for native functions (parameter types and return type)
2. Load the dynamic library with `Deno.dlopen()`
3. Call loaded functions via `dylib.symbols.<function_name>()`

FFI requires the `--allow-ffi` permission because native code runs outside Deno's security sandbox and has the same access level as the Deno process itself.

# Prerequisites

- `deno-configuration` — FFI permissions can be configured in `deno.json`

# Key Properties

1. **Supported types**: `i8`, `u8`, `i16`, `u16`, `i32`, `u32`, `i64`, `u64`, `usize`, `isize`, `f32`, `f64`, `void`, `pointer`, `buffer`, `function`, and `{ struct: [...] }`.
2. **Callbacks**: JavaScript functions can be passed to native code via `Deno.UnsafeCallback`, which wraps a JS function as a C-compatible function pointer.
3. **Struct support**: C structs can be passed and returned by value using `TypedArray`s with automatic padding.
4. **Security warning**: Native libraries have full process-level access (filesystem, network, environment, system commands) — they bypass Deno's sandbox entirely.
5. **Resource cleanup**: Libraries must be closed with `dylib.close()` and callbacks with `callback.close()`.
6. **Node-API compatibility**: Deno also supports Node-API (N-API) for existing Node.js native addons as an alternative to FFI.

# Construction / Recognition

Basic FFI usage:

```ts
const dylib = Deno.dlopen("libexample.so", {
  add: { parameters: ["i32", "i32"], result: "i32" },
});

console.log(dylib.symbols.add(5, 3)); // 8
dylib.close();
```

Cross-platform library loading:

```ts
const libName = {
  windows: "./lib.dll",
  linux: "./liblib.so",
  darwin: "./liblib.dylib",
}[Deno.build.os];

const dylib = Deno.dlopen(libName, {
  fibonacci: { parameters: ["u32"], result: "u32" },
} as const);
```

Callback example:

```ts
const callback = new Deno.UnsafeCallback(
  { parameters: ["i32"], result: "void" } as const,
  (value) => { console.log("Callback received:", value); },
);
dylib.symbols.setCallback(callback.pointer);
dylib.symbols.runCallback();
callback.close();
```

# Context & Application

FFI is used when JavaScript performance is insufficient for a critical code path, when existing native libraries need to be reused, or when operating system APIs not available in JavaScript must be accessed. Before using FFI, consider alternatives: WebAssembly (portable, sandboxed), `Deno.command` (subprocesses with controlled permissions), or Deno's native APIs.

# Examples

**Rust library** (from `runtime/fundamentals/ffi.md`):

```rust
#[unsafe(no_mangle)]
pub extern "C" fn fibonacci(n: u32) -> u32 {
    if n <= 1 { return n; }
    fibonacci(n - 1) + fibonacci(n - 2)
}
```

Compile with `rustc --crate-type cdylib lib.rs`, then call from Deno:

```ts
const dylib = Deno.dlopen(libName, {
  fibonacci: { parameters: ["u32"], result: "u32" },
} as const);
console.log(`Fibonacci(10) = ${dylib.symbols.fibonacci(10)}`); // 55
dylib.close();
```

**FFI vs Node-API comparison** (from `runtime/fundamentals/ffi.md`):

| Aspect      | FFI                    | Node-API                              |
|-------------|------------------------|---------------------------------------|
| Setup       | No build step required | Requires precompiled binaries or build step |
| Portability | Tied to library ABI    | ABI-stable across versions            |
| Use Case    | Direct library calls   | Reuse Node.js addons                  |

# Relationships

- **Related**: `deno-http-server` — server applications may use FFI for performance-critical operations

# Common Errors

1. **Forgetting to close resources**: Not calling `dylib.close()` or `callback.close()` causes resource leaks.
2. **Missing `--allow-ffi`**: FFI calls fail without the explicit permission flag.
3. **Type mismatches**: Incorrect parameter or return type definitions cause undefined behavior or crashes.

# Common Confusions

- **FFI vs WebAssembly**: FFI calls native shared libraries directly (no sandbox), while WebAssembly runs portable bytecode inside Deno's sandbox.
- **`pointer` vs `buffer`**: Since Deno 1.25, `pointer` returns an opaque pointer object, while `buffer` accepts `TypedArray`s as parameters for optimized performance.

# Source Reference

Source: "Deno Documentation", file `runtime/fundamentals/ffi.md`, all sections.

# Verification Notes

All API details, type tables, and security considerations are explicitly documented in the source file. Extraction confidence is high.
