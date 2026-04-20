---
# === CORE IDENTIFICATION ===
concept: KV Secondary Indexes
slug: kv-secondary-indexes

# === CLASSIFICATION ===
category: kv
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/kv/secondary_indexes.md"
chapter_number: null
pdf_page: null
section: "Secondary Indexes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "secondary index"
  - "index by alternate key"
  - "pointer index"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-kv
  - kv-operations
  - kv-atomic-transactions
extends: []
related:
  - kv-key-space
  - kv-data-modeling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I query Deno KV by non-primary keys?"
  - "What is the secondary index pattern in Deno KV?"
  - "How do I enforce uniqueness constraints in Deno KV?"
---

# Quick Definition
Secondary indexes in Deno KV are manually maintained additional keys that enable querying data by alternate attributes, typically storing a pointer (the primary key) as the value rather than duplicating the full data.

# Core Definition
Key-value stores like Deno KV allow retrieval only by key. To query by non-key attributes (e.g., looking up a user by email when the primary key is user ID), you create secondary indexes: additional key-value pairs where the key is based on the alternate attribute and the value is a pointer to the primary key.

The recommended approach is to store the primary key (or a compact reference) as the value in the secondary index rather than duplicating the full data. This reduces storage, avoids keeping multiple copies in sync, and simplifies updates -- at the cost of requiring a second read to resolve the actual data (double lookup: index -> primary).

Consistency between primary and secondary keys is maintained using atomic transactions. Every insert, update, or delete must atomically modify both the primary key and all associated secondary index keys.

There are two patterns:
- **Unique indexes (one-to-one):** Each secondary key maps to exactly one primary key. Can enforce uniqueness constraints (e.g., unique email).
- **Non-unique indexes (one-to-many):** Multiple primary keys share a secondary index prefix. The secondary key includes the primary key as a suffix to avoid collisions (e.g., `["users_by_color", color, userId]`).

# Prerequisites
- Understanding of Deno KV operations (kv-operations)
- Understanding of atomic transactions (kv-atomic-transactions)

# Key Properties
1. **Pointer indexes** -- Store the primary key as the secondary index value, not the full data
2. **Double lookup** -- Querying via secondary index requires two reads: index entry -> primary entry
3. **Atomic consistency** -- All index operations (insert/update/delete) must be wrapped in `kv.atomic()` to prevent inconsistencies
4. **Unique indexes** -- One secondary key per primary key; atomic checks with `versionstamp: null` enforce uniqueness
5. **Non-unique indexes** -- Composite secondary keys include the primary key as a part to avoid collisions; `list` by prefix retrieves all matching entries
6. **Delete requires read** -- Deleting an entry with a secondary index requires first reading the primary to find the secondary key

# Construction / Recognition
- Unique index insert:
  ```
  kv.atomic()
    .check({ key: primaryKey, versionstamp: null })
    .check({ key: byEmailKey, versionstamp: null })
    .set(primaryKey, user)
    .set(byEmailKey, user.id)
    .commit()
  ```
- Unique index lookup (double read):
  ```
  const idRes = await kv.get(["users_by_email", email]);
  const userRes = await kv.get(["users", idRes.value]);
  ```
- Non-unique index insert:
  ```
  kv.atomic()
    .check({ key: primaryKey, versionstamp: null })
    .set(primaryKey, user)
    .set(["users_by_color", user.favoriteColor, user.id], user.id)
    .commit()
  ```
- Non-unique index query:
  ```
  const iter = kv.list({ prefix: ["users_by_color", color] });
  ```

# Context & Application
Secondary indexes are essential whenever the application needs to query data by attributes other than the primary key. Common examples include looking up users by email, filtering products by category, or finding orders by customer. The pointer index pattern keeps storage lean and avoids data synchronization issues. For very small, read-heavy values where the second lookup is costly, duplicating the full value in the index may be acceptable if updates are always atomic.

# Examples
From deploy/kv/secondary_indexes.md:
- Unique index: `["users_by_email", email]` stores `user.id`; lookup does `kv.get(["users_by_email", email])` then `kv.get(["users", id])`
- Non-unique index: `["users_by_favorite_color", color, user.id]` stores `user.id`; query with `kv.list({ prefix: ["users_by_favorite_color", color] })`
- Atomic delete with index cleanup: read user to get email, then atomically delete both `["users", id]` and `["users_by_email", email]` with a versionstamp check

# Relationships
## Builds Upon
- kv-operations (get, set, list, delete)
- kv-atomic-transactions (consistency enforcement)
- kv-key-space (composite key structures)

## Enables
- kv-data-modeling (complex data patterns rely on secondary indexes)

## Related
- deno-kv

## Contrasts With
- Database-managed indexes (SQL databases create and maintain indexes automatically)
- Full-text search indexes (KV secondary indexes are exact-match or prefix-based)

# Common Errors
1. Updating the primary key without updating the secondary index -- causes stale index entries pointing to wrong or deleted data
2. Not using atomic transactions for index maintenance -- creates race conditions where primary and index can become inconsistent
3. Forgetting to include the primary key in non-unique index keys -- causes collisions when multiple entities share the same indexed attribute

# Common Confusions
1. **Pointer vs. duplicated value indexes** -- Pointer indexes store just the primary key reference; duplicated value indexes copy the full data. Pointer indexes are recommended for most cases.
2. **Unique vs. non-unique index key structure** -- Unique indexes use `[indexPrefix, attribute]`; non-unique indexes use `[indexPrefix, attribute, primaryId]` to allow multiple entries
3. **Migration from duplicated to pointer indexes** -- Requires a backfill step (scan primaries, write pointer values), cutover (update write paths), and cleanup (remove duplicated entries)

# Source Reference
- deploy/kv/secondary_indexes.md: Complete documentation of unique and non-unique secondary index patterns, pointer index recommendation, atomic consistency requirements, and migration guidance

# Verification Notes
- High confidence: Both unique and non-unique patterns are explicitly documented with full code examples
- Pointer index recommendation is explicitly stated as best practice
