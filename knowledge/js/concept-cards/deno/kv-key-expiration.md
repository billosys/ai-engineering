---
# === CORE IDENTIFICATION ===
concept: KV Key Expiration
slug: kv-key-expiration

# === CLASSIFICATION ===
category: kv
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/kv/key_expiration.md"
chapter_number: null
pdf_page: null
section: "Key Expiration (TTL for keys)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "TTL"
  - "time to live"
  - "expireIn"
  - "key TTL"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-kv
  - kv-operations
extends: []
related:
  - kv-atomic-transactions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I set expiration on Deno KV keys?"
  - "Can multiple keys expire atomically?"
---

# Quick Definition
Deno KV supports key expiration via the `expireIn` option on `set` operations, specifying the number of milliseconds after which the key is automatically deleted.

# Core Definition
Since Deno 1.36.2, Deno KV supports key expiration (TTL). When setting a key, you can pass an `expireIn` option specifying the number of milliseconds after which the key will be automatically deleted from the database. This is supported on both the Deno CLI and Deno Deploy.

When multiple keys are set in the same atomic operation with the same `expireIn` value, their expiration is atomic -- they all expire together.

The expire timestamp specifies the earliest time after which the key can be deleted. The implementation may delay actual deletion beyond the specified timestamp, but will never delete before it. For security-critical expiration (e.g., authentication tokens), the documentation recommends also storing the expiration time as a field in the value and checking it after retrieval.

# Prerequisites
- Understanding of Deno KV (deno-kv)
- Understanding of set operations (kv-operations)

# Key Properties
1. **Millisecond TTL** -- `expireIn` is specified in milliseconds
2. **Automatic deletion** -- Expired keys are removed without manual intervention
3. **Atomic group expiration** -- Keys set in the same atomic operation with the same `expireIn` expire together
4. **Best-effort timing** -- Deletion occurs at or after the specified time, never before
5. **Cross-platform** -- Works on both Deno CLI and Deno Deploy

# Construction / Recognition
- Set with expiration: `await kv.set(["sessions", session.id], session, { expireIn: 3600000 });`
- Atomic expiration of related keys:
  ```
  await kv.atomic()
    .set(["users", user.id], user, { expireIn })
    .set(["verificationTokens", token], user.id, { expireIn })
    .commit();
  ```

# Context & Application
Key expiration is commonly used for session management, temporary verification tokens, rate limiting windows, cache entries, and any data with a natural time-to-live. The atomic group expiration pattern is particularly useful for ensuring related temporary data (e.g., a user record and its verification token) disappears at the same time.

# Examples
From deploy/kv/key_expiration.md:
- Session expiration: `await kv.set(["sessions", session.id], session, { expireIn });`
- Atomic expiration of user and verification token: both keys set with the same `expireIn` in a single `kv.atomic()` call

# Relationships
## Builds Upon
- kv-operations (extends the `set` operation with `expireIn`)
- kv-atomic-transactions (atomic group expiration)

## Enables
- Session management patterns
- Temporary token patterns

## Related
- deno-kv

## Contrasts With
- Redis TTL (similar concept, but Redis uses `EXPIRE` command or `EX`/`PX` options)

# Common Errors
1. Relying solely on `expireIn` for security-critical expiration -- the actual deletion may be delayed; also store expiration time in the value and check it on read
2. Expecting exact-millisecond precision -- the timestamp is a lower bound, not a guarantee of immediate deletion

# Common Confusions
1. **expireIn vs. expireAt** -- Deno KV uses `expireIn` (relative milliseconds from now), not an absolute timestamp
2. **Atomic expiration scope** -- Only keys set in the same atomic operation with the same `expireIn` value expire atomically; different `expireIn` values create independent expirations

# Source Reference
- deploy/kv/key_expiration.md: Complete documentation of key expiration, atomic expiration, and caveats

# Verification Notes
- High confidence: Feature is explicitly documented with clear API and caveats
- Caveat about best-effort timing quoted directly from source
