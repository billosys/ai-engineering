---
# === CORE IDENTIFICATION ===
concept: KV Node.js Integration
slug: kv-node-integration

# === CLASSIFICATION ===
category: kv
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/kv/node.md"
chapter_number: null
pdf_page: null
section: "Using KV in Node.js"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "@deno/kv"
  - "KV Connect"
  - "KV Node client"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-kv
extends: []
related:
  - kv-operations
  - deno-node-api-compatibility
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use Deno KV from Node.js?"
  - "What is KV Connect?"
---

# Quick Definition
The `@deno/kv` npm package provides an official client library for connecting to Deno KV databases from Node.js applications via the KV Connect protocol, offering the same API as the native Deno runtime.

# Core Definition
Deno KV can be accessed from Node.js using the official `@deno/kv` npm package. This client library connects to a Deno KV database hosted on Deno Deploy using a KV Connect URL in the format `https://api.deno.com/databases/<database-id>/connect`. The `database-id` is found in the Deno Deploy dashboard under the project's KV tab.

Authentication uses an access token, which defaults to the `DENO_KV_ACCESS_TOKEN` environment variable or can be passed explicitly via the `accessToken` option.

Once initialized, the client exposes the same API available in the Deno runtime (`get`, `set`, `delete`, `list`, `atomic`, etc.), enabling Node.js applications to interact with Deno Deploy-hosted KV databases.

# Prerequisites
- A Deno KV database hosted on Deno Deploy (deno-kv)
- Node.js runtime with npm

# Key Properties
1. **Official npm package** -- `@deno/kv` is the official client, supporting both ESM `import` and CJS `require`
2. **KV Connect protocol** -- Uses a specific URL format to connect to Deploy-hosted databases
3. **Same API** -- Once initialized, provides the same KV API as the Deno runtime
4. **Token-based auth** -- Authenticates via `DENO_KV_ACCESS_TOKEN` environment variable or explicit `accessToken` option
5. **Cross-runtime** -- Enables Node.js services to share KV data with Deno Deploy applications

# Construction / Recognition
- Install: `npm install @deno/kv`
- Connect and use:
  ```js
  import { openKv } from "@deno/kv";
  const kv = await openKv("https://api.deno.com/databases/<database-id>/connect");
  await kv.set(["users", "alice"], { name: "Alice" });
  const result = await kv.get(["users", "alice"]);
  ```
- With explicit token: `const kv = await openKv(url, { accessToken: myToken });`

# Context & Application
This integration enables hybrid architectures where some services run on Deno Deploy and others run on Node.js, all sharing the same KV database. It also allows existing Node.js applications to adopt Deno KV as a data store without migrating the entire application to the Deno runtime. The KV Connect URL and access token can be found in the Deno Deploy dashboard.

# Examples
From deploy/kv/node.md:
- Basic usage: `import { openKv } from "@deno/kv";` then `openKv("<KV Connect URL>")`
- Explicit auth: `openKv(url, { accessToken: myToken })`
- KV Connect URL format: `https://api.deno.com/databases/<database-id>/connect`

# Relationships
## Builds Upon
- deno-kv (connects to Deno KV databases)
- kv-operations (exposes the same operation set)

## Enables
- Hybrid Deno/Node.js architectures sharing KV data

## Related
- deno-node-api-compatibility

## Contrasts With
- Native `Deno.openKv()` (runs in-process; Node client connects over the network)

# Common Errors
1. Missing access token -- ensure `DENO_KV_ACCESS_TOKEN` is set or pass `accessToken` explicitly
2. Using a local file path instead of a KV Connect URL -- the Node client only supports remote connections via KV Connect

# Common Confusions
1. **Local vs. remote** -- The Node.js client only connects to remote Deno Deploy databases; it does not support local SQLite-backed KV
2. **openKv vs. Deno.openKv** -- In Node, import `openKv` from `@deno/kv`; in Deno, use `Deno.openKv()`

# Source Reference
- deploy/kv/node.md: Installation instructions, usage examples, KV Connect URL format, and authentication

# Verification Notes
- High confidence: Official npm package and KV Connect protocol explicitly documented
