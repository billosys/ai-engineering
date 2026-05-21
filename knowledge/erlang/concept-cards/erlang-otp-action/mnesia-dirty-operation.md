---
# === CORE IDENTIFICATION ===
concept: Mnesia Dirty Operation
slug: mnesia-dirty-operation

# === CLASSIFICATION ===
category: distribution
subcategory: mnesia
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding distribution to the cache with Mnesia"
chapter_number: 9
pdf_page: null
section: "9.2.4 Populating the tables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "dirty operation"
  - "dirty_write"
  - "dirty_read"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
extends: []
related:
  - mnesia-transaction
  - mnesia-query
contrasts_with:
  - mnesia-transaction

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Mnesia dirty operation?"
  - "When is it safe to use dirty operations?"
  - "Why are dirty operations faster than transactions?"
---

# Quick Definition

A Mnesia dirty operation is any `mnesia` function prefixed with `dirty_` that bypasses transactions and database locks; it is significantly faster but must be used with care, as it can leave data inconsistent.

# Core Definition

A Mnesia dirty operation is any Mnesia function with the prefix `dirty_` — such as `mnesia:dirty_write/1`, `mnesia:dirty_read/2`, or `mnesia:dirty_index_read/3`. A dirty operation does not respect transactions or database locks, so it must be used with great care. Using a dirty operation is significantly faster than setting up a transaction and performing normal database operations, and judicious use can speed up an application a lot. The danger is that, without thinking through the consequences, you may end up with inconsistent data. Dirty reads are usually less problematic than dirty writes; the book's rule of thumb is: whenever in doubt, use transactions (Ch. 9, Sections 9.2.4 and 9.3.1).

# Prerequisites

- **mnesia** — Dirty operations are a feature of the Mnesia database.

# Key Properties

1. Any `mnesia` function prefixed with `dirty_`.
2. Bypasses transactions and database locks.
3. Significantly faster than transaction-wrapped operations.
4. Can leave data inconsistent if used carelessly.
5. Dirty reads are less risky than dirty writes.
6. Recommended only when the consistency consequences are understood.

# Construction / Recognition

## To Use a Dirty Operation:
1. Confirm the operation does not need transactional isolation.
2. Call the `dirty_`-prefixed function (e.g., `mnesia:dirty_write/1`).
3. When in doubt, fall back to a transaction.

## To Recognize:
1. A `mnesia:dirty_*` function call is a dirty operation.

# Context & Application

- **Typical contexts**: Simple key-value access where transactional guarantees are unnecessary.
- **Common applications**: The distributed cache's `insert`, `lookup`, and `delete` on the `key_to_pid` table.
- **Historical/stylistic notes**: The cache uses Mnesia mainly for replication, not transactions, so dirty operations suffice.

# Examples

**Example 1** (Section 9.2.4): `insert_project/2` uses `mnesia:dirty_write/1` as a shortcut, accepting that a sudden insertion overwriting a previous project record will not seriously affect the application.

**Example 2** (Section 9.3.1): The cache's `insert/2` calls `mnesia:dirty_write(#key_to_pid{...})` and `lookup/1` calls `mnesia:dirty_read(key_to_pid, Key)` — a basic key-value store too simple to need transactions.

# Relationships

## Builds Upon
- **mnesia** — Dirty operations are part of Mnesia.

## Enables
- None.

## Related
- **mnesia-query** — `dirty_read` and `dirty_index_read` are dirty query forms.

## Contrasts With
- **mnesia-transaction** — Transactions provide ACID guarantees and locking; dirty operations skip both for speed.

# Common Errors

- **Error**: Using dirty writes for interdependent multi-step operations.
  **Correction**: Use a transaction when consistency across steps matters.

# Common Confusions

- **Confusion**: Thinking "dirty" means the operation corrupts data.
  **Clarification**: It means the operation skips transactions/locks; misuse *can* cause inconsistency, but correct use is fine and fast.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.2.4 "Populating the tables," subsection "Dirty operations," and Section 9.3.1.

# Verification Notes

- Definition source: Directly adapted from Section 9.2.4.
- Confidence rationale: HIGH — the book explicitly defines dirty operations and their trade-offs.
- Uncertainties: None.
- Cross-reference status: Verified.
