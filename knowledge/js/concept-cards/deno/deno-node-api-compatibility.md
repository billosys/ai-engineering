---
# === CORE IDENTIFICATION ===
concept: Deno Node.js API Compatibility
slug: deno-node-api-compatibility

# === CLASSIFICATION ===
category: api
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "api/node/index.md"
chapter_number: null
pdf_page: null
section: "Node.js Built-in APIs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Node.js compatibility"
  - "node: imports"
  - "Deno Node compat"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno
extends: []
related:
  - deno-api-overview
  - deno-web-platform-apis
  - kv-node-integration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Which Node.js APIs does Deno support?"
  - "How do I migrate from Node.js to Deno?"
---

# Quick Definition
Deno provides comprehensive support for Node.js built-in modules (accessed via the `node:` prefix) and global objects like `Buffer` and `process`, enabling seamless migration of Node.js applications.

# Core Definition
Deno implements Node.js built-in modules accessible through the `node:` import prefix. This compatibility layer enables running existing Node.js code and npm packages in Deno with minimal modifications. Supported module categories include:

- **File System** -- `node:fs`, `node:fs/promises`, `node:path`
- **Network** -- `node:http`, `node:https`, `node:http2`, `node:net`, `node:dns`
- **Process** -- `node:process`, `node:os`, `node:child_process`, `node:cluster`
- **Crypto** -- `node:crypto`, `node:tls`
- **Streams & Data** -- `node:stream`, `node:buffer`, `node:zlib`, `node:string_decoder`
- **Utilities** -- `node:util`, `node:events`, `node:url`, `node:querystring`, `node:assert`
- **Development** -- `node:vm`, `node:repl`, `node:inspector`

Node.js global objects (`Buffer`, `process`, `global`, `__dirname`, `__filename`) are available in npm package scope and can be imported from their respective `node:` modules.

Migration from Node.js involves: updating imports to use the `node:` prefix, verifying dependency compatibility, using `npm:` specifiers for npm packages, and configuring Deno's permission system.

# Prerequisites
- Understanding of the Deno runtime (deno)

# Key Properties
1. **node: prefix** -- All Node.js built-in modules use the `node:` import prefix (e.g., `import fs from "node:fs"`)
2. **Comprehensive coverage** -- Most core Node.js modules are supported with high fidelity
3. **Global objects** -- `Buffer`, `process`, `global`, `__dirname`, `__filename` available in npm package scope
4. **npm: specifiers** -- npm packages imported with `npm:` prefix, no `npm install` required
5. **Native implementations** -- Optimized for the Deno runtime, not polyfilled
6. **Ongoing project** -- Compatibility is continuously improving

# Construction / Recognition
- Import Node modules: `import fs from "node:fs";`
- Promise-based: `import { readFile } from "node:fs/promises";`
- HTTP server: `import http from "node:http"; http.createServer((req, res) => { ... });`
- Crypto: `import crypto from "node:crypto"; crypto.createHash("sha256").update("data").digest("hex");`

# Context & Application
Node.js API compatibility enables teams to migrate existing Node.js applications to Deno incrementally. Libraries built for Node.js often work in Deno without modification. This compatibility is critical for the Deno ecosystem's growth, as it provides access to the vast npm package ecosystem while offering Deno's security, TypeScript, and tooling benefits.

# Examples
From api/node/index.md:
- File read: `import fs from "node:fs"; const data = fs.readFileSync("file.txt", "utf8");`
- Async file read: `import { readFile } from "node:fs/promises"; const content = await readFile("file.txt", "utf8");`
- HTTP server: `http.createServer((req, res) => { res.writeHead(200); res.end("Hello"); }).listen(3000);`
- Path join: `import path from "node:path"; path.join("/users", "documents", "file.txt");`

# Relationships
## Builds Upon
- deno (runtime providing the compatibility layer)

## Enables
- Migration from Node.js to Deno
- Using npm packages in Deno

## Related
- deno-api-overview (complementary Deno-specific APIs)
- deno-web-platform-apis (complementary Web Platform APIs)
- kv-node-integration (@deno/kv npm package for Node.js)

## Contrasts With
- Native Node.js runtime (Deno adds permissions, TypeScript, and different module resolution)

# Common Errors
1. Omitting the `node:` prefix -- `import fs from "fs"` may not resolve correctly; use `import fs from "node:fs"`
2. Expecting all Node.js APIs to be fully compatible -- some edge cases and newer APIs may have gaps
3. Forgetting to configure Deno permissions -- Node.js code that accesses the file system or network needs appropriate `--allow-*` flags

# Common Confusions
1. **node: vs. npm: specifiers** -- `node:` is for built-in Node.js modules; `npm:` is for third-party npm packages
2. **Global scope differences** -- Node globals like `Buffer` and `process` are available in npm package scope but may need explicit import in Deno-native code

# Source Reference
- api/node/index.md: Overview of supported Node.js modules, global objects, usage examples, and migration guidance

# Verification Notes
- High confidence: Module list and migration steps explicitly documented
