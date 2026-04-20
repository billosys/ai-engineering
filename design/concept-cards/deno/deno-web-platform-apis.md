---
# === CORE IDENTIFICATION ===
concept: Deno Web Platform APIs
slug: deno-web-platform-apis

# === CLASSIFICATION ===
category: api
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "api/web/index.md"
chapter_number: null
pdf_page: null
section: "Web Platform APIs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Web APIs in Deno"
  - "web standard APIs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno
extends: []
related:
  - deno-api-overview
  - deno-node-api-compatibility
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What web standard APIs does Deno support?"
  - "How closely does Deno follow browser APIs?"
---

# Quick Definition
Deno implements many standard Web Platform APIs (fetch, WebSocket, Web Workers, Streams, Web Crypto, Cache, localStorage, and more) following WHATWG and W3C specifications, enabling cross-platform code that works in both Deno and browsers.

# Core Definition
Deno implements a broad set of Web Platform APIs that follow WHATWG and W3C specifications. This means code written for the web often works in Deno without modification. Key API categories include:

- **Network** -- `fetch` (WHATWG spec), WebSocket, Server-Sent Events (EventSource), BroadcastChannel
- **Storage** -- Web Storage (localStorage/sessionStorage with 10MB limit), Cache API, IndexedDB
- **Workers** -- Web Workers (module type only; `type: "module"` required)
- **Streams** -- ReadableStream, WritableStream, TransformStream, CompressionStream
- **Events** -- Event, CustomEvent, EventTarget (without DOM bubbling)
- **Encoding & Crypto** -- TextEncoder/TextDecoder, Web Crypto (SubtleCrypto), URL API
- **Timers** -- setTimeout, setInterval, Performance API

Notable deviations from browser specs: Deno's `fetch` has no cookie jar, does not implement CORS/same-origin policy, and supports `file:` URL fetching. Events do not bubble (no DOM hierarchy). Workers must use `type: "module"`. localStorage persistence rules differ from browsers (based on location flag, config file, or main module path).

# Prerequisites
- Understanding of the Deno runtime (deno)
- Familiarity with standard Web APIs

# Key Properties
1. **Standards compliance** -- APIs follow WHATWG and W3C specifications
2. **Cross-platform** -- Same code works in Deno and browsers
3. **No polyfills needed** -- Native implementations with optimal performance
4. **Module-only workers** -- Web Workers require `type: "module"`
5. **Fetch deviations** -- No cookie jar, no CORS, supports `file:` URLs, no same-origin policy
6. **localStorage rules** -- Persistence scoped by `--location` flag, config file path, or main module path
7. **Permission integration** -- Workers inherit parent permissions by default; can be restricted via `deno.permissions` option

# Construction / Recognition
- HTTP request: `const res = await fetch("https://api.github.com/users/denoland");`
- Web Worker: `new Worker(import.meta.resolve("./worker.js"), { type: "module" });`
- localStorage: `localStorage.setItem("key", "value");`
- Worker with restricted permissions:
  ```js
  new Worker(url, { type: "module", deno: { permissions: { net: false } } })
  ```

# Context & Application
The Web Platform APIs form the portable layer of Deno's API surface. Code using only these APIs can potentially run in Deno, browsers, and other web-standard runtimes. This makes Deno an attractive target for isomorphic applications and libraries. The fetch API is particularly important as the primary HTTP client interface.

# Examples
From api/web/index.md:
- Fetch: `const response = await fetch("https://api.github.com/users/denoland");`
- Worker: `new Worker(import.meta.resolve("./worker.js"), { type: "module" });`
- localStorage: `localStorage.setItem("myDemo", "Deno App");`
- Worker permissions: `deno: { permissions: { net: ["deno.land"], read: [new URL("./file.txt", import.meta.url)] } }`

# Relationships
## Builds Upon
- deno (runtime that implements these APIs)

## Enables
- Cross-platform JavaScript/TypeScript code
- Isomorphic applications

## Related
- deno-api-overview (complementary Deno-specific APIs)
- deno-node-api-compatibility (complementary Node.js-compatible APIs)

## Contrasts With
- Browser implementations (Deno omits CORS, cookie jar, DOM hierarchy)
- Node.js (Node does not natively support most Web Platform APIs)

# Common Errors
1. Using `type: "classic"` for Web Workers -- Deno only supports `type: "module"`
2. Expecting CORS or cookie handling in fetch -- Deno does not implement these browser-specific security features
3. Registering Worker message handler after top-level await -- messages arriving during the await are lost

# Common Confusions
1. **fetch spec deviations** -- Deno's fetch does not implement CORS, same-origin policy, or cookie jar; these are intentional differences for server environments
2. **localStorage scoping** -- Unlike browsers which scope by origin, Deno scopes by `--location` flag, config path, or main module path
3. **Cache API limitations** -- Only a subset is implemented (open, has, delete, match, put, delete on Cache)

# Source Reference
- api/web/index.md: Comprehensive documentation of supported Web Platform APIs, usage examples, fetch spec deviations, Web Worker details, localStorage, and Cache API limitations

# Verification Notes
- High confidence: All API categories and deviations explicitly documented
- Fetch deviations listed verbatim from source
