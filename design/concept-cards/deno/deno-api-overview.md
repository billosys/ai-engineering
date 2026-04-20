---
# === CORE IDENTIFICATION ===
concept: Deno API Surface
slug: deno-api-overview

# === CLASSIFICATION ===
category: api
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "api/deno/index.md"
chapter_number: null
pdf_page: null
section: "Deno Namespace APIs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Deno namespace"
  - "Deno APIs"
  - "Deno built-in APIs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno
extends: []
related:
  - deno-web-platform-apis
  - deno-node-api-compatibility
  - deno-kv
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What APIs are available in the Deno namespace?"
  - "How does Deno's API surface differ from web and Node APIs?"
---

# Quick Definition
The global `Deno` namespace provides non-web-standard APIs for file system operations, networking, subprocess management, HTTP serving, FFI, and permissions -- capabilities specific to the Deno runtime.

# Core Definition
The global `Deno` namespace contains APIs that are not web standard but are essential for server-side operations. These include:

- **File System** -- `Deno.readTextFile`, `Deno.writeTextFile`, and other file/directory operations (requires `--allow-read`/`--allow-write`)
- **Network** -- `Deno.connect` (TCP connections), `Deno.listen` (listening on ports)
- **HTTP Server** -- `Deno.serve` (high-level, preferred) and `Deno.serveHttp` (low-level), both supporting HTTP/1.1 and HTTP/2
- **Subprocesses** -- `Deno.Command` for spawning and managing child processes (requires `--allow-run`)
- **Permissions** -- `Deno.permissions.query()`, `.request()`, `.revoke()` for runtime permission management
- **FFI** -- `Deno.dlopen` for calling native C-ABI libraries from JavaScript/TypeScript (requires `--allow-ffi`)
- **Errors** -- 20 error classes under `Deno.errors` (e.g., `Deno.errors.NotFound`)
- **import.meta** -- `import.meta.url`, `import.meta.main`, `import.meta.filename`, `import.meta.dirname`, `import.meta.resolve()`
- **Program lifecycle** -- `load`, `beforeunload`, `unload` events

Deno provides three distinct API layers: the Deno namespace (this concept), Web Platform APIs (deno-web-platform-apis), and Node.js compatibility APIs (deno-node-api-compatibility). Together they form the complete runtime API surface.

# Prerequisites
- Understanding of the Deno runtime (deno)

# Key Properties
1. **Non-web-standard** -- APIs in the `Deno` namespace are specific to Deno and not available in browsers
2. **Permission-gated** -- Most APIs require explicit permission flags (`--allow-read`, `--allow-net`, `--allow-run`, `--allow-ffi`)
3. **HTTP server** -- `Deno.serve` is the preferred high-level API for HTTP servers
4. **FFI support** -- `Deno.dlopen` enables calling Rust, C, C++, and other native libraries
5. **Runtime permission management** -- Permissions can be queried, requested, and revoked at runtime
6. **20 error classes** -- Structured error handling via `Deno.errors`

# Construction / Recognition
- HTTP server: `Deno.serve((_req) => new Response("Hello"));`
- File read: `const text = await Deno.readTextFile("file.txt");`
- Permission query: `await Deno.permissions.query({ name: "read", path: "/foo" })`
- Subprocess: `new Deno.Command("echo", { args: ["hello"] })`
- FFI: `Deno.dlopen("./lib.so", { add: { parameters: ["i32", "i32"], result: "i32" } })`

# Context & Application
The Deno namespace APIs are the primary interface for server-side functionality that goes beyond what web standards provide. File I/O, networking, subprocess management, and native interop all live here. The permission system ensures these powerful capabilities are opt-in, maintaining Deno's secure-by-default principle.

# Examples
From api/deno/index.md:
- HTTP server on default port 8000: `Deno.serve((_req) => new Response("Hello, World!"));`
- Error handling: `catch (error) { if (error instanceof Deno.errors.NotFound) { ... } }`
- Permission request with user prompt: `await Deno.permissions.request({ name: "read", path: "/foo" })`
- FFI call to Rust library: `dylib.symbols.add(35, 34)` after opening with `Deno.dlopen`

# Relationships
## Builds Upon
- deno (the runtime that provides this namespace)

## Enables
- Server-side applications
- CLI tools
- Native library integration

## Related
- deno-web-platform-apis (complementary web-standard APIs)
- deno-node-api-compatibility (complementary Node.js-compatible APIs)
- deno-kv (Deno.Kv is part of this namespace)

## Contrasts With
- Browser APIs (Deno namespace is server-side only)
- Node.js core modules (similar capabilities but different API design)

# Common Errors
1. Forgetting permission flags -- `Deno.readTextFile` fails without `--allow-read`
2. Using `Deno.serveHttp` instead of `Deno.serve` -- `Deno.serve` is the preferred higher-level API

# Common Confusions
1. **Three API layers** -- Deno has the `Deno` namespace, Web Platform APIs, and Node.js APIs; they are complementary, not alternatives
2. **`import.meta.filename` on remote modules** -- Returns `undefined` for non-local (remote) modules

# Source Reference
- api/deno/index.md: Overview of file system, network, subprocess, HTTP server, permissions, FFI, errors, import.meta, and program lifecycle APIs

# Verification Notes
- High confidence: All API categories explicitly documented with examples
