---
# === CORE IDENTIFICATION ===
concept: Deno KV
slug: deno-kv

# === CLASSIFICATION ===
category: kv
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/kv/index.md"
chapter_number: null
pdf_page: null
section: "Deno KV Quick Start"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Deno.Kv"
  - "Deno KV database"
  - "KV"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno
extends: []
related:
  - kv-key-space
  - kv-operations
  - kv-atomic-transactions
  - kv-key-expiration
  - kv-secondary-indexes
  - kv-data-modeling
  - kv-backup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Deno KV?"
  - "How do I use Deno KV?"
  - "What distinguishes Deno KV from traditional databases?"
  - "How does Deno KV relate to Deno Deploy?"
---

# Quick Definition
Deno KV is a key-value database built directly into the Deno runtime, available via the `Deno.Kv` namespace, for fast reads and writes of simple data structures both locally and on Deno Deploy.

# Core Definition
Deno KV is a key-value database integrated into the Deno runtime. Data is stored as key-value pairs where keys are arrays of JavaScript types (`string`, `number`, `bigint`, `boolean`, `Uint8Array`) and values can be arbitrary JavaScript objects compatible with the structured clone algorithm. Each stored entry also carries a `versionstamp` -- a monotonically increasing value that tracks when the entry was last modified.

Locally (via the Deno CLI), KV is backed by SQLite. In production on Deno Deploy, it is backed by FoundationDB, Apple's open-source key-value store. The database is opened with `Deno.openKv()`, which returns a `Deno.Kv` instance. An optional file system path can be passed; passing `":memory:"` creates an ephemeral in-memory store suitable for testing.

Deno KV requires the `--unstable-kv` flag.

# Prerequisites
- Basic understanding of key-value data stores
- Familiarity with the Deno runtime (`deno` concept)

# Key Properties
1. **Built into the runtime** -- No external database server or driver installation needed; available through the `Deno.Kv` namespace
2. **Array-based keys** -- Keys are arrays of typed parts, eliminating delimiter injection attacks
3. **Structured clone values** -- Values can be any JavaScript object compatible with the structured clone algorithm (including `Map`, `Set`, `Date`, `RegExp`, nested objects, and circular references)
4. **Versionstamped entries** -- Every entry has a `versionstamp` that changes on each modification, enabling optimistic concurrency control
5. **Dual backends** -- SQLite locally, FoundationDB on Deno Deploy
6. **Strong and eventual consistency** -- Reads can use strong or eventual consistency; writes are always strongly consistent
7. **Watch support** -- `kv.watch()` emits a `ReadableStream` of updated values when watched keys change

# Construction / Recognition
- Open a database: `const kv = await Deno.openKv();`
- Open an in-memory database for tests: `const kv = await Deno.openKv(":memory:");`
- Set a value: `await kv.set(["preferences", "ada"], { theme: "dark" });`
- Get a value: `const entry = await kv.get(["preferences", "ada"]);`
- Close the connection: `await kv.close();`
- Run with: `deno run --unstable-kv script.ts`

# Context & Application
Deno KV excels at storing simple data structures that benefit from very fast reads and writes. Typical use cases include user preferences, session storage, feature flags, counters, and lightweight application state. Because it is built into the runtime, there is no need to provision or manage a separate database for these workloads. On Deno Deploy, KV provides a globally replicated store backed by FoundationDB.

# Examples
From deploy/kv/index.md:
- Creating a key-value pair: `await kv.set(["preferences", "ada"], prefs);`
- Reading a value: `const entry = await kv.get(["preferences", "ada"]);` returns `{ key, value, versionstamp }`
- Listing by prefix: `const entries = kv.list({ prefix: ["preferences"] });` with `for await`
- Deleting: `await kv.delete(["preferences", "alan"]);`
- Watching for updates: `for await (const [messageId] of kv.watch([["last_message_id", roomId]])) { ... }`

# Relationships
## Builds Upon
- Deno runtime
- SQLite (local backend)
- FoundationDB (Deno Deploy backend)

## Enables
- kv-key-space
- kv-operations
- kv-atomic-transactions
- kv-key-expiration
- kv-secondary-indexes
- kv-data-modeling
- kv-backup
- kv-node-integration

## Related
- deno-api-overview

## Contrasts With
- Traditional SQL databases (relational model vs. flat key-value namespace)
- Redis (external service vs. built-in runtime database)

# Common Errors
1. Forgetting to pass `--unstable-kv` flag -- the `Deno.Kv` namespace is not available without it
2. Expecting `kv.get()` to throw when a key does not exist -- it returns `{ value: null, versionstamp: null }` instead
3. Not closing the database connection -- use `kv.close()` when done to release resources

# Common Confusions
1. **Local vs. Deploy behavior** -- Locally KV uses SQLite; on Deploy it uses FoundationDB. The API is identical but performance characteristics and replication differ.
2. **Versionstamp vs. timestamp** -- Versionstamps represent modification order, not real wall-clock time

# Source Reference
- deploy/kv/index.md: Complete quick-start guide covering opening a database, CRUD operations, atomic transactions, secondary indexes, watching for updates, production usage, and testing

# Verification Notes
- High confidence: Deno KV is explicitly defined and comprehensively described in the quick-start guide
- All code examples taken directly from source
