---
# === CORE IDENTIFICATION ===
concept: KV Atomic Transactions
slug: kv-atomic-transactions

# === CLASSIFICATION ===
category: kv
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/kv/transactions.md"
chapter_number: null
pdf_page: null
section: "Transactions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "atomic operations"
  - "OCC transactions"
  - "optimistic concurrency control"
  - "kv.atomic()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-kv
  - kv-key-space
  - kv-operations
extends: []
related:
  - kv-key-expiration
  - kv-secondary-indexes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before using Deno KV transactions?"
  - "How does optimistic concurrency control work in Deno KV?"
  - "How do I perform atomic operations in Deno KV?"
---

# Quick Definition
Deno KV uses optimistic concurrency control (OCC) transactions that combine versionstamp-based checks with multiple mutation actions, committing atomically only if all version constraints are satisfied.

# Core Definition
Deno KV uses optimistic concurrency control transactions rather than interactive (lock-based) transactions found in SQL databases. A transaction is built using `kv.atomic()`, which returns an `AtomicOperation` that chains `.check()` constraints and mutation actions (`.set()`, `.delete()`, `.mutate()`). The transaction commits only if every check's versionstamp matches the current versionstamp of the corresponding key in the database.

When a read returns an entry, it includes a versionstamp. This versionstamp is passed into `.check()` to assert that the data has not changed between read and commit. If any check fails (another agent modified a checked key between read and commit), the entire transaction aborts and returns `{ ok: false }`. The caller must then retry the transaction.

A `null` versionstamp in a check asserts that the key does not exist, enabling "insert if not exists" patterns.

# Prerequisites
- Understanding of Deno KV (deno-kv)
- Understanding of key-value operations (kv-operations)
- Understanding of versionstamps (kv-key-space)

# Key Properties
1. **Optimistic concurrency control** -- No locks are held; conflicts are detected at commit time via versionstamp comparison
2. **Check-then-mutate pattern** -- Checks assert expected versionstamps; mutations execute only if all checks pass
3. **All-or-nothing** -- Either all mutations in the atomic operation commit, or none do
4. **Retry on conflict** -- When `res.ok` is `false`, the application must retry the read-check-mutate cycle
5. **Null versionstamp check** -- `{ key, versionstamp: null }` asserts the key does not exist
6. **Shared versionstamp** -- All data modified in a single transaction receives the same versionstamp

# Construction / Recognition
- Insert if not exists:
  ```
  kv.atomic()
    .check({ key, versionstamp: null })
    .set(key, value)
    .commit()
  ```
- Transfer funds with retry loop:
  ```
  let res = { ok: false };
  while (!res.ok) {
    const [sender, receiver] = await kv.getMany([senderKey, receiverKey]);
    res = await kv.atomic()
      .check(sender)
      .check(receiver)
      .set(senderKey, newSenderBalance)
      .set(receiverKey, newReceiverBalance)
      .commit();
  }
  ```

# Context & Application
Atomic transactions are essential whenever multiple keys must be updated consistently. Common patterns include: transferring values between accounts, inserting data with uniqueness constraints, maintaining primary and secondary indexes in sync, and implementing compare-and-swap logic. The OCC model is well-suited to workloads with low contention; under high contention, retries may become frequent.

# Examples
From deploy/kv/transactions.md:
- Fund transfer with versionstamp checks: reads both account balances, checks both versionstamps, sets new balances atomically, retries on conflict
- Insert-if-not-exists: checks `versionstamp: null` to ensure key does not already exist before setting

# Relationships
## Builds Upon
- kv-operations (set, delete, mutate actions)
- kv-key-space (versionstamps for concurrency control)

## Enables
- kv-secondary-indexes (atomic updates to primary + secondary keys)
- kv-key-expiration (atomic expiration of multiple keys with same TTL)

## Related
- kv-data-modeling

## Contrasts With
- SQL interactive transactions (lock-based, multi-statement transactions with BEGIN/COMMIT)
- Pessimistic concurrency control (acquires locks before modification)

# Common Errors
1. Forgetting to retry on `{ ok: false }` -- transactions can fail due to concurrent modifications and must be retried
2. Not re-reading data before retry -- stale versionstamps will cause repeated failures
3. Exceeding transaction limits -- max 100 checks, 1000 mutations, 800 KiB total size, 90 KiB total key size per atomic operation

# Common Confusions
1. **OCC vs. interactive transactions** -- Deno KV does not support multi-step interactive transactions with held locks; all checks and mutations must be declared upfront
2. **Check semantics** -- A check does not read the current value; it compares the provided versionstamp against the database's current versionstamp for that key
3. **Commit result** -- `{ ok: false }` is not an error; it is the expected signal to retry when contention occurs

# Source Reference
- deploy/kv/transactions.md: Full explanation of OCC transactions, the check-mutate pattern, a fund transfer example, and transaction limits

# Verification Notes
- High confidence: OCC transaction model is explicitly defined with detailed examples
- Transaction limits taken verbatim from source documentation
