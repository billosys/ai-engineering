---
# === CORE IDENTIFICATION ===
concept: Mnesia Transaction
slug: mnesia-transaction

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
  - "mnesia:transaction"
  - "ACID transaction"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
extends: []
related:
  - mnesia-dirty-operation
  - mnesia-query
contrasts_with:
  - mnesia-dirty-operation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Mnesia transaction?"
  - "What ACID properties do Mnesia transactions provide?"
  - "How do I run a transaction in Mnesia?"
---

# Quick Definition

A Mnesia transaction runs a fun of database operations atomically with full ACID guarantees; you pass the fun to `mnesia:transaction/1`, and it either succeeds entirely or is unrolled with no effect.

# Core Definition

A Mnesia transaction is a unit of database work that executes with the usual ACID properties (Ch. 9, Section 9.2.4):

- **Atomicity** — The transaction either succeeds or fails entirely; if it fails at any point it is unrolled with no effect on the database.
- **Consistency** — The effects of multiple transactions are as if executed in some particular order, going from one consistent state to the next, even if they overlap in real time.
- **Isolation** — All transactions appear to have the database to themselves; nobody else sees a transaction's effects until it is completely finished.
- **Durability** — If the transaction succeeds, all its changes have taken effect; for disk-backed tables they survive a restart or crash.

Setting up a transaction is easy: write a fun taking no arguments to do the work and pass it to `mnesia:transaction/1`. When a transaction succeeds, the result has the form `{atomic, Data}`, where `Data` is the result of the code inside the transaction fun. Transactions are critical for ensuring database integrity across complex operations and for isolating operations from simultaneous accesses by other processes.

# Prerequisites

- **mnesia** — Transactions are a feature of the Mnesia database.

# Key Properties

1. Executes a fun of database operations as one unit.
2. Provides Atomicity, Consistency, Isolation, and Durability.
3. On failure, the transaction is unrolled with no database effect.
4. Run with `mnesia:transaction/1`, passing a zero-argument fun.
5. A successful transaction returns `{atomic, Data}`.
6. Normal operations like `mnesia:read/2` are used inside transactions.

# Construction / Recognition

## To Run a Transaction:
1. Write a `fun() -> ... end` performing the database operations.
2. Pass it to `mnesia:transaction(Fun)`.
3. Check for the `{atomic, Data}` result; on abort, the database is unchanged.

## To Recognize:
1. A `mnesia:transaction/1` call wrapping a fun of `mnesia:read`/`write`/`select` operations.

# Context & Application

- **Typical contexts**: Multi-step database operations that must be consistent and isolated.
- **Common applications**: Inserting a user plus contributor records while asserting referenced projects exist.
- **Historical/stylistic notes**: When in doubt between dirty operations and transactions, the book says use transactions.

# Examples

**Example 1** (Section 9.2.4, Listing 9.3): `insert_user/3` writes a user record and, for each project, asserts the project exists (via `mnesia:read/2`) before inserting a contributor record — all inside one `mnesia:transaction/1`; if any step fails the whole transaction is unrolled.

**Example 2** (Section 9.2.5): A `select` wrapped in `mnesia:transaction/1` returns `{atomic, [1]}` — the `{atomic, Data}` success form.

# Relationships

## Builds Upon
- **mnesia** — Transactions are part of Mnesia.

## Enables
- None.

## Related
- **mnesia-query** — Queries like `read` and `select` run inside transactions.

## Contrasts With
- **mnesia-dirty-operation** — Dirty operations skip transactions and locks for speed, sacrificing the ACID guarantees.

# Common Errors

- **Error**: Performing a multi-step interdependent operation with dirty writes.
  **Correction**: Use a transaction so the operation is atomic and isolated.

# Common Confusions

- **Confusion**: Thinking the transaction fun takes arguments.
  **Clarification**: The fun passed to `mnesia:transaction/1` takes no arguments.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.2.4 "Populating the tables," subsection "Transactions," Listing 9.3.

# Verification Notes

- Definition source: Directly adapted from Section 9.2.4.
- Confidence rationale: HIGH — the book explicitly defines transactions and the ACID properties.
- Uncertainties: None.
- Cross-reference status: Verified.
