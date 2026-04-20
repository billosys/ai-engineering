---
# === CORE IDENTIFICATION ===
concept: KV Operations
slug: kv-operations

# === CLASSIFICATION ===
category: kv
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/kv/operations.md"
chapter_number: null
pdf_page: null
section: "Operations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "KV CRUD operations"
  - "Deno KV API methods"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-kv
  - kv-key-space
extends: []
related:
  - kv-atomic-transactions
  - kv-key-expiration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use Deno KV?"
  - "What read and write operations does Deno KV support?"
  - "What is the difference between strong and eventual consistency in Deno KV?"
---

# Quick Definition
Deno KV provides two read operations (`get`, `list`) and five write operations (`set`, `delete`, `sum`, `min`, `max`), plus a `watch` operation for real-time change notifications.

# Core Definition
The Deno KV API exposes operations for reading and writing data in the key space. Read operations (`get` and `list`) support both strong and eventual consistency modes. Strong consistency returns the most recently written value; eventual consistency may return a stale value but is faster. Write operations (`set`, `delete`, `sum`, `min`, `max`) are always strongly consistent.

**Read operations:**
- `get(key)` / `getMany(keys)` -- Retrieve one or more entries as snapshot reads (multi-key reads are consistent with each other)
- `list(selector)` -- Iterate over entries matching a prefix or range selector, returning a `Deno.KvListIterator`

**Write operations:**
- `set(key, value)` -- Create or overwrite a key-value pair
- `delete(key)` -- Remove a key (no-op if key does not exist)
- `sum` -- Atomically add a `Deno.KvU64` value to a key
- `min` -- Atomically set a key to the minimum of its current and given `Deno.KvU64` value
- `max` -- Atomically set a key to the maximum of its current and given `Deno.KvU64` value

**Reactive operation:**
- `watch(keys)` -- Returns a `ReadableStream` that emits the latest state of watched keys when they change

The `sum`, `min`, and `max` operations can only be performed within atomic operations and only on `Deno.KvU64` values.

# Prerequisites
- Understanding of Deno KV (deno-kv)
- Understanding of key structure (kv-key-space)

# Key Properties
1. **Snapshot reads** -- `get` and `getMany` return consistent results even when reading multiple keys
2. **Prefix and range selectors** -- `list` supports prefix-based filtering (`{ prefix: [...] }`) and range queries (`{ start: [...], end: [...] }`)
3. **Batched iteration** -- `list` reads in batches (default 500 keys); consistency holds within a batch but not across batches
4. **Reverse listing** -- `list` supports `reverse: true` for descending lexicographic order
5. **Consistency modes** -- Reads accept `{ consistency: "strong" | "eventual" }`; writes are always strong
6. **Atomic mutations** -- `sum`, `min`, `max` operate only on `Deno.KvU64` values within `kv.atomic()` chains
7. **Watch stream** -- `watch` may skip intermediate states, always providing the latest value

# Construction / Recognition
- Get: `const res = await kv.get<string>(["config"]);`
- Get with eventual consistency: `await kv.get(["config"], { consistency: "eventual" })`
- Get many: `const [r1, r2] = await kv.getMany([["users", "sam"], ["users", "taylor"]]);`
- List by prefix: `const iter = kv.list({ prefix: ["users"] });`
- List with limit: `kv.list({ prefix: ["users"] }, { limit: 2 })`
- List in reverse: `kv.list({ prefix: ["users"] }, { reverse: true })`
- Set: `await kv.set(["users", "alex"], "alex");`
- Delete: `await kv.delete(["users", "alex"]);`
- Sum mutation: `kv.atomic().mutate({ type: "sum", key: [...], value: new Deno.KvU64(100n) }).commit()`
- Watch: `for await (const entries of kv.watch([["foo"], ["bar"]])) { ... }`

# Context & Application
These operations form the complete data access layer for Deno KV. Simple CRUD workflows use `get`, `set`, and `delete`. Prefix listing enables querying collections of related entries. The `sum`, `min`, and `max` mutations are useful for counters, rate limiters, and statistical aggregations. The `watch` operation enables real-time features like chat applications and live dashboards.

# Examples
From deploy/kv/operations.md:
- Range query: `kv.list({ start: ["users", "a"], end: ["users", "n"] })` returns users with keys between "a" and "n"
- Reverse with start bound: `kv.list({ prefix: ["users"], start: ["users", "sam"] }, { reverse: true })` returns from "taylor" down to "sam"
- Sum mutation: `kv.atomic().mutate({ type: "sum", key: ["accounts", "alex"], value: new Deno.KvU64(100n) }).commit()`

# Relationships
## Builds Upon
- deno-kv
- kv-key-space

## Enables
- kv-atomic-transactions (operations are composed into atomic chains)
- kv-secondary-indexes (double-read pattern uses get and list)

## Related
- kv-key-expiration (set with `expireIn` option)

## Contrasts With
- SQL queries (declarative queries vs. explicit key/prefix lookups)

# Common Errors
1. Expecting `list` to be consistent across batches -- consistency only holds within each batch of results
2. Confusing `start`/`end` semantics with `reverse` -- start and end are always evaluated in ascending order, even when `reverse: true` is set
3. Trying to use `sum`/`min`/`max` outside of `kv.atomic()` -- these are only available as atomic mutations
4. Using `sum`/`min`/`max` on non-KvU64 values -- these operations only work with `Deno.KvU64`

# Common Confusions
1. **Prefix vs. range selectors** -- Prefix matches all keys sharing array-prefix parts; range matches keys between start and end bounds
2. **`list` batch boundaries** -- The 500-key batch size is an implementation detail; the iterator API hides batch boundaries but consistency does not span them
3. **`watch` intermediate states** -- `watch` does not guarantee delivery of every intermediate value change, only the latest state

# Source Reference
- deploy/kv/operations.md: Complete documentation of get, getMany, list, set, delete, sum, min, max, and watch operations with consistency semantics

# Verification Notes
- High confidence: Each operation is explicitly documented with API signatures and examples
- Consistency semantics described verbatim from source
