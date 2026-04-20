---
concept: Web Platform APIs
slug: web-platform-apis
category: apis
subcategory: web standards
tier: intermediate
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/reference/web_platform_apis.md"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Web APIs in Deno"
  - "Web Standard APIs"
prerequisites:
  - deno
extends: []
related:
  - deno-namespace-apis
  - deno-run
  - jsx-support
  - webassembly-support
contrasts_with:
  - deno-namespace-apis
answers_questions:
  - "What Web APIs are available in Deno?"
  - "How does Deno's fetch differ from a browser's?"
  - "Can I use Web Workers in Deno?"
---

# Quick Definition

Deno implements standard Web Platform APIs -- including `fetch`, EventTarget, Web Storage, Web Workers, the Cache API, and more -- so that code written for the browser can run server-side with minimal modification.

# Core Definition

"One way Deno simplifies web and cloud development is by using standard Web Platform APIs (like `fetch`, WebSockets and more) over proprietary APIs. This means if you've ever built for the browser, you're likely already familiar with Deno, and if you're learning Deno, you're also investing in your knowledge of the web."

Deno implements these Web APIs following WHATWG and W3C specifications, with documented deviations where server-side semantics differ from browser semantics (e.g., no cookie jar, no same-origin policy, no DOM tree for event bubbling).

# Prerequisites

- **Deno** -- Web Platform APIs are part of the Deno runtime global scope.

# Key Properties

1. **fetch API** -- Implements the WHATWG fetch spec, including fetching `file:` URLs and duplex streaming. Deviations: no cookie jar, no CORS/CORB, no same-origin policy.
2. **CustomEvent and EventTarget** -- DOM Event API without bubbling (no DOM hierarchy). `timeStamp` is always 0.
3. **Web Storage** -- `localStorage` (persisted across executions) and `sessionStorage` (per-execution), with 10MB limit. Storage location determined by `--location`, `--config`, or main module path.
4. **Web Workers** -- Only `module` type workers supported (`type: "module"` required). Workers inherit permissions by default but can be restricted via `deno.permissions`.
5. **Cache API** -- Partial implementation: `CacheStorage.open()`, `.has()`, `.delete()`; `Cache.match()`, `.put()`, `.delete()`. No relative paths; no query options on `match()`/`delete()`.
6. **Location API** -- Available via `--location <href>` flag; throws without it. Cannot be mutated.

# Construction / Recognition

## To Use:
- `fetch` is globally available:
```ts
const response = await fetch("https://api.example.com/data");
```
- Web Workers:
```ts
new Worker(import.meta.resolve("./worker.js"), { type: "module" });
```
- Web Storage:
```ts
localStorage.setItem("key", "value");
```

## To Identify:
- APIs matching browser globals (`fetch`, `addEventListener`, `localStorage`, `Worker`, `caches`).
- TypeScript definitions in `lib.deno.shared_globals.d.ts` and `lib.deno.window.d.ts`.

# Context & Application

- **Isomorphic code**: Code using Web Platform APIs can run in both Deno and browsers.
- **Server-side fetch**: Deno supports `file:` URL fetching and duplex streaming not available in browsers.
- **Worker permissions**: Deno extends the Worker API with `deno.permissions` to restrict worker capabilities.

# Examples

**Example 1** (from source): Fetching relative to current module.
```js
const response = await fetch(new URL("./config.json", import.meta.url));
const config = await response.json();
```
(Section: "Fetching local files")

**Example 2** (from source): Using localStorage.
```ts
localStorage.setItem("myDemo", "Deno App");
const cat = localStorage.getItem("myDemo");
```
(Section: "Web Storage")

**Example 3** (from source): Creating a Worker with restricted permissions.
```ts
const worker = new Worker(import.meta.resolve("./worker.js"), {
  type: "module",
  deno: {
    permissions: {
      net: ["deno.land"],
      read: [new URL("./file_1.txt", import.meta.url)],
      write: false,
    },
  },
});
```
(Section: "Specifying worker permissions")

# Relationships

## Builds Upon
- WHATWG Fetch specification.
- WHATWG DOM specification (EventTarget).
- W3C Web Storage specification.
- HTML specification (Web Workers).

## Enables
- Isomorphic JavaScript code that runs in both browsers and Deno.
- Server-side use of familiar Web APIs.

## Related
- **deno-namespace-apis** -- Deno-specific APIs complement Web Platform APIs.
- **jsx-support** -- JSX SSR often uses `fetch` and `Deno.serve` together.

## Contrasts With
- **deno-namespace-apis** -- Web Platform APIs follow browser standards; Deno namespace APIs are Deno-specific (file system, subprocess, etc.).

# Common Errors

- **Error**: Using relative URLs with `fetch()` without `--location`.
  **Correction**: Either pass `--location <href>` or use `new URL("./path", import.meta.url)` to construct absolute URLs.

- **Error**: Creating a Worker without `type: "module"`.
  **Correction**: Deno only supports module-type workers. Always specify `{ type: "module" }`.

- **Error**: Registering a Worker message handler after a top-level `await`.
  **Correction**: Register `self.onmessage` before any `await` to avoid losing messages.

# Common Confusions

- **Confusion**: Deno's `fetch` behaves identically to a browser's `fetch`.
  **Clarification**: Deno's fetch has no cookie jar, no CORS enforcement, no same-origin policy. It also supports `file:` URLs and duplex streaming.

- **Confusion**: `localStorage` persists globally like in a browser.
  **Clarification**: Deno determines storage location based on `--location`, `--config`, or main module path -- different entry points may have different storage.

# Source Reference

- runtime/reference/web_platform_apis.md: Full documentation of fetch, EventTarget, Location, Web Storage, Web Workers, Cache API, and spec deviations.

# Verification Notes

- High confidence: Detailed documentation with spec deviation lists, code examples, and permission models directly from source.
- Spec deviations enumerated verbatim from source.
