---
# === CORE IDENTIFICATION ===
concept: KV Key Space
slug: kv-key-space

# === CLASSIFICATION ===
category: kv
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/kv/key_space.md"
chapter_number: null
pdf_page: null
section: "Key Space"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "key space"
  - "key parts"
  - "Deno KV keys"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-kv
extends: []
related:
  - kv-operations
  - kv-atomic-transactions
  - kv-secondary-indexes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are keys structured in Deno KV?"
  - "What types can be used as key parts?"
  - "How are keys ordered in Deno KV?"
  - "What is a versionstamp?"
---

# Quick Definition
The Deno KV key space is a flat namespace of key+value+versionstamp triples, where keys are ordered sequences of typed parts (strings, numbers, bigints, booleans, or Uint8Arrays) that model hierarchical data without delimiter injection risks.

# Core Definition
Keys in Deno KV are sequences of key parts. Each part can be a `string`, `number`, `boolean`, `bigint`, or `Uint8Array`. Using an array of typed parts rather than a single delimited string eliminates delimiter injection attacks -- there is no visible delimiter that an attacker could exploit. Invisible delimiters separate parts internally, ensuring that different part sequences are always distinct (e.g., `["abc", "def"]` differs from `["ab", "cdef"]`).

Keys are case-sensitive and ordered lexicographically by their parts. The type ordering is: `Uint8Array` < `string` < `number` < `bigint` < `boolean`. Within a type, values follow their natural ordering (byte order for arrays/strings, mathematical order for numbers/bigints, `false` < `true` for booleans).

Values can be any JavaScript object compatible with the structured clone algorithm, plus the special `Deno.KvU64` type for 64-bit unsigned integers used with `sum`, `min`, and `max` mutations.

Versionstamps are monotonically increasing, non-sequential, 12-byte values assigned when data is inserted or modified. All mutations in a single atomic transaction share the same versionstamp. Versionstamps enable optimistic concurrency control.

# Prerequisites
- Understanding of Deno KV (deno-kv concept)

# Key Properties
1. **Array-based keys** -- Keys are arrays of typed parts, not single strings
2. **Type-aware ordering** -- Parts are ordered first by type (Uint8Array < string < number < bigint < boolean), then by value within type
3. **No delimiter injection** -- Invisible separators between parts prevent injection attacks
4. **Structured clone values** -- Values support `undefined`, `null`, `boolean`, `number`, `string`, `bigint`, `Uint8Array`, `Array`, `Object`, `Map`, `Set`, `Date`, `RegExp`, and circular references
5. **Deno.KvU64** -- Special 64-bit unsigned integer type for atomic `sum`, `min`, `max` operations; must be stored as a top-level value
6. **Monotonic versionstamps** -- 12-byte values that increase with each modification, enabling comparison of recency
7. **ULID support** -- Keys can use ULIDs (`@std/ulid`) for chronologically sortable, cryptographically random identifiers

# Construction / Recognition
- Simple key: `["users", 42, "profile"]`
- Hierarchical key: `["products", "electronics", "smartphones", "apple"]`
- Key with ULID: `["users", ulid()]` from `jsr:@std/ulid`
- Monotonic ULID: `["users", monotonicUlid()]` for strict ordering within same timestamp
- KvU64 value: `new Deno.KvU64(42n)`

# Context & Application
The key space design allows modeling hierarchical data in a flat key-value store. By convention, the first parts of a key represent the entity type or collection, and subsequent parts narrow down to a specific entity. This design supports efficient prefix-based listing (e.g., all keys starting with `["users"]`) and range queries. The type-aware ordering enables chronological listing when timestamps or ULIDs are used as key parts.

# Examples
From deploy/kv/key_space.md:
- User profile key: `["users", 42, "profile"]`
- Date-scoped key: `["posts", "2023-04-23", "comments"]`
- Key with Uint8Array: `["files", new Uint8Array([1, 2, 3]), "metadata"]`
- Comparing versionstamps: `"000002fa526aaccb0000" > "000002fa526aacc90000"` returns `true`
- ULID-based key: `["users", "01H76YTWK3YBV020S6MP69TBEQ"]`

# Relationships
## Builds Upon
- deno-kv

## Enables
- kv-operations (prefix listing depends on key structure)
- kv-secondary-indexes (alternate key hierarchies for querying)
- kv-atomic-transactions (versionstamp-based concurrency checks)

## Related
- kv-data-modeling

## Contrasts With
- String-delimited keys (e.g., Redis `"users:42:profile"`) which are vulnerable to delimiter injection

# Common Errors
1. Using partial key parts as prefix selectors -- `["f"]` will NOT match `["foo", "bar"]`; prefix selectors must use full key parts
2. Assuming type ordering matches intuition -- `1.0` (number) is ordered AFTER `0n` (bigint) because type ordering takes precedence over value ordering across types
3. Storing class instances or functions as values -- only structured-clone-compatible types are supported

# Common Confusions
1. **Key ordering across types** -- The ordering `Uint8Array < string < number < bigint < boolean` means a string key part always sorts before a number key part, regardless of their values
2. **Versionstamp vs. timestamp** -- Versionstamps represent ordering of modifications, not wall-clock time; they are 12-byte opaque values, not dates
3. **Deno.KvU64 constraints** -- Must be stored as a top-level value, not nested inside objects or arrays

# Source Reference
- deploy/kv/key_space.md: Comprehensive documentation of keys, key part ordering, values, structured clone compatibility, Deno.KvU64, versionstamps, and ULID usage

# Verification Notes
- High confidence: All properties explicitly defined in source documentation
- Type ordering and value compatibility lists taken verbatim from source
