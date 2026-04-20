---
concept: Deno Namespace APIs
slug: deno-namespace-apis
category: apis
subcategory: runtime APIs
tier: intermediate
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/reference/deno_namespace_apis.md"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - "Deno.* APIs"
  - "Deno global namespace"
  - "Deno built-in APIs"
prerequisites:
  - deno
  - web-platform-apis
extends: []
related:
  - web-platform-apis
  - deno-run
  - deno-stability-and-releases
contrasts_with:
  - web-platform-apis
answers_questions:
  - "What APIs does the Deno namespace provide?"
  - "How do Deno namespace APIs differ from Web Platform APIs?"
---

# Quick Definition

The `Deno` global namespace exposes Deno-specific runtime APIs for file system operations, networking, subprocesses, environment access, permissions management, and other capabilities not covered by Web Platform standards.

# Core Definition

The Deno namespace APIs are accessible via the global `Deno` object and provide functionality that goes beyond what Web Platform APIs offer. These include:

- **File system**: `Deno.readTextFile()`, `Deno.writeTextFile()`, `Deno.open()`, `Deno.mkdir()`, `Deno.stat()`, etc.
- **Networking**: `Deno.serve()`, `Deno.listen()`, `Deno.connect()`
- **Subprocesses**: `Deno.Command` (replaces older `Deno.run`)
- **Environment**: `Deno.env`, `Deno.args`, `Deno.cwd()`, `Deno.exit()`
- **Permissions**: `Deno.permissions.query()`, `Deno.permissions.request()`, `Deno.permissions.revoke()`
- **FFI**: `Deno.dlopen()` for calling native libraries
- **Program lifecycle**: `Deno.addSignalListener()`, import.meta properties

As of Deno 1.0.0, stable Deno namespace APIs are guaranteed not to have breaking changes. Unstable APIs require explicit `--unstable-*` flags.

# Prerequisites

- **Deno** -- These APIs are part of the Deno runtime.
- **web-platform-apis** -- Understanding Web Platform APIs helps distinguish what Deno namespace APIs add beyond web standards.

# Key Properties

1. **Global access** -- All APIs available on the `Deno` global object (e.g., `Deno.readTextFile()`).
2. **Permission-gated** -- Most Deno namespace APIs require corresponding permission flags (e.g., `--allow-read` for file system, `--allow-net` for networking).
3. **Stability guarantee** -- Stable APIs (since Deno 1.0) will not break; unstable APIs are behind `--unstable-*` flags.
4. **Complement Web APIs** -- Provide server-side capabilities (file I/O, processes, FFI) not available in Web Platform APIs.
5. **TypeScript-typed** -- Full TypeScript definitions available via `Deno.` namespace.

# Construction / Recognition

## To Use:
```ts
// Read a file
const text = await Deno.readTextFile("./data.json");

// Start an HTTP server
Deno.serve((req) => new Response("Hello"));

// Access environment variables
const home = Deno.env.get("HOME");

// Run a subprocess
const command = new Deno.Command("echo", { args: ["hello"] });
const output = await command.output();
```

## To Identify:
- APIs accessed via `Deno.*` prefix.
- Require `--allow-*` permission flags.

# Context & Application

- **Server applications**: File I/O, networking, process management.
- **CLI tools**: Environment access, subprocess execution, `Deno.args`.
- **Security-sensitive contexts**: Permission APIs for querying and requesting capabilities at runtime.

# Examples

**Example 1** (synthesized from description): Reading a file.
```ts
const content = await Deno.readTextFile("./config.json");
```
Requires `--allow-read` permission.

**Example 2** (from web_platform_apis.md Worker example): Using Deno APIs in a Worker.
```js
self.onmessage = async (e) => {
  const { filename } = e.data;
  const text = await Deno.readTextFile(filename);
  console.log(text);
  self.close();
};
```
(Section: "Using Deno in a worker")

# Relationships

## Builds Upon
- **Deno runtime** -- These APIs are provided by the runtime itself.

## Enables
- Server-side file I/O, networking, and subprocess management.
- Runtime permission management.

## Related
- **web-platform-apis** -- Web Platform APIs handle standard web functionality; Deno namespace APIs handle server-specific needs.
- **deno-stability-and-releases** -- Stability guarantees and unstable API flags.

## Contrasts With
- **web-platform-apis** -- Web Platform APIs follow browser specifications; Deno namespace APIs are Deno-specific and cover capabilities browsers cannot provide.

# Common Errors

- **Error**: Using `Deno.readTextFile()` without `--allow-read`.
  **Correction**: File system operations require the `--allow-read` permission flag.

# Common Confusions

- **Confusion**: All `Deno.*` APIs are stable.
  **Clarification**: Some APIs are unstable and require `--unstable-*` flags (e.g., `--unstable-kv` for Deno KV).

- **Confusion**: Web Platform APIs and Deno namespace APIs are separate runtimes.
  **Clarification**: Both are available simultaneously in the same Deno execution context. Web APIs handle standard web functionality; Deno APIs handle server-side capabilities.

# Source Reference

- runtime/reference/deno_namespace_apis.md: Redirects to /api/deno/ for full API reference.
- runtime/reference/web_platform_apis.md: Worker examples using Deno namespace APIs.
- runtime/fundamentals/stability_and_releases.md: Stability guarantees for Deno namespace APIs.

# Verification Notes

- Medium confidence: The source file for Deno namespace APIs is a redirect page; content synthesized from references across other source files and the stability documentation. API categories are well-established in the Deno ecosystem.
