---
concept: WebAssembly Support
slug: webassembly-support
category: platform
subcategory: language interop
tier: intermediate
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/reference/wasm.md"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Wasm in Deno"
  - "WebAssembly in Deno"
  - "WASM support"
prerequisites:
  - deno
extends: []
related:
  - web-platform-apis
  - deno-namespace-apis
contrasts_with: []
answers_questions:
  - "How do I run WebAssembly modules in Deno?"
  - "Does Deno type-check WebAssembly imports?"
---

# Quick Definition

Deno can execute WebAssembly modules via direct `import` statements (with type checking, since Deno 2.1) or through the standard `WebAssembly` API, supporting both streaming and non-streaming compilation.

# Core Definition

WebAssembly (Wasm) is "designed to be used alongside JavaScript to speed up key application components" and "can have much higher, and more consistent execution speed than JavaScript." Deno executes WebAssembly modules "with the same interfaces that browsers provide" and additionally supports importing them directly as ES modules.

Two approaches are available:

1. **Module imports** (Deno 2.1+): `import { add } from "./add.wasm"` -- Deno understands Wasm exports and type-checks their usage. Wasm modules can also import JavaScript modules.
2. **WebAssembly API**: The standard `WebAssembly.Module`, `WebAssembly.Instance`, `WebAssembly.instantiateStreaming`, and `WebAssembly.compileStreaming` APIs.

# Prerequisites

- **Deno** -- WebAssembly execution is part of the Deno runtime.

# Key Properties

1. **Direct import with type checking** -- Since Deno 2.1, `.wasm` files can be imported as modules; Deno infers and checks export types.
2. **Wasm-to-JS imports** -- Wasm modules can import JavaScript/TypeScript modules using standard import specifiers.
3. **Import map support** -- Non-relative Wasm import specifiers (e.g., `"env"`) can be mapped via import maps in `deno.json`.
4. **Streaming APIs** -- `WebAssembly.instantiateStreaming(fetch(...))` is the most efficient way to load remote Wasm.
5. **Multi-language support** -- Wasm modules can be compiled from Rust, Go, AssemblyScript, C/C++, and other languages.
6. **wasmbuild tool** -- Official Deno tool for compiling Rust to Wasm with TypeScript binding generation.
7. **Optimization** -- Production Wasm binaries can be optimized for size or speed using tools from the Rust-Wasm ecosystem.

# Construction / Recognition

## Module Import (Deno 2.1+):
```ts
import { add } from "./add.wasm";
console.log(add(1, 2)); // 3
```

## WebAssembly API:
```ts
const { instance } = await WebAssembly.instantiateStreaming(
  fetch("https://wpt.live/wasm/incrementer.wasm"),
);
const increment = instance.exports.increment as (input: number) => number;
console.log(increment(41)); // 42
```

## Overriding Wasm import specifiers:
```json
{
  "imports": {
    "env": "./env.ts"
  }
}
```

# Context & Application

- **Performance-critical code**: Offload compute-intensive work to Wasm (near-native speed).
- **Multi-language projects**: Call Rust, C/C++, or Go code from Deno via Wasm.
- **Type safety**: Wasm module imports are type-checked, catching errors like passing a string where a number is expected.

# Examples

**Example 1** (from source): Importing a Wasm module with type checking.
```ts
import { add } from "./add.wasm";
console.log(add(1, ""));
// error: TS2345: Argument of type 'string' is not assignable to parameter of type 'number'.
```
(Section: "Type Checking")

**Example 2** (from source): Streaming instantiation.
```ts
const { instance, module } = await WebAssembly.instantiateStreaming(
  fetch("https://wpt.live/wasm/incrementer.wasm"),
);
const increment = instance.exports.increment as (input: number) => number;
console.log(increment(41));
```
(Section: "Using the Streaming WebAssembly APIs")

**Example 3** (from source): Wasm module importing a TypeScript module.
```ts
// time.ts
export function getTimeInSeconds() {
  return Date.now() / 1000;
}
// main.ts
import { getValue } from "./toolkit.wasm";
console.log(getValue()); // calls getTimeInSeconds via Wasm
```
(Section: "Imports")

# Relationships

## Builds Upon
- W3C WebAssembly specification.
- Browser WebAssembly APIs.

## Enables
- Running native-speed code from Rust, C/C++, Go within Deno.
- Type-safe interop between TypeScript and Wasm.

## Related
- **web-platform-apis** -- WebAssembly APIs are Web Platform APIs.
- **deno-namespace-apis** -- Deno-specific features like import maps complement Wasm loading.

# Common Errors

- **Error**: Wasm module imports a bare specifier (e.g., `"env"`) that Deno cannot resolve.
  **Correction**: Map the specifier in `deno.json` import map: `{ "imports": { "env": "./env.ts" } }`.

- **Error**: Forgetting `application/wasm` MIME type when serving Wasm files for streaming APIs.
  **Correction**: Ensure the server sets `Content-Type: application/wasm` for `.wasm` files.

# Common Confusions

- **Confusion**: Wasm modules can only export/import numeric types.
  **Clarification**: Direct Wasm only supports numeric types. For complex types (strings, objects), use binding generators like `wasm-bindgen` (Rust) or `web_sys`/`js_sys` crates.

# Source Reference

- runtime/reference/wasm.md: Full documentation of Wasm module imports, type checking, WebAssembly API, streaming APIs, import overrides, wasmbuild, and optimization.

# Verification Notes

- High confidence: Detailed documentation with multiple code examples and patterns directly from source.
- Deno 2.1 requirement for module imports explicitly stated in source.
