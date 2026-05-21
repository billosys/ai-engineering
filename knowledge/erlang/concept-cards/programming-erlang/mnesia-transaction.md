---
# === CORE IDENTIFICATION ===
concept: Mnesia Transaction
slug: mnesia-transaction

# === CLASSIFICATION ===
category: distribution
subcategory: database
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Mnesia: The Erlang Database"
chapter_number: 20
pdf_page: null
section: "Mnesia Transactions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "mnesia:transaction/1"
  - transaction
  - "transaction fun"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - mnesia-table
  - fun
extends: []
related:
  - mnesia-query-qlc
  - mnesia-dirty-operations
contrasts_with:
  - mnesia-dirty-operations

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Mnesia transaction?"
  - "How do I safely read and write Mnesia data?"
  - "How does Mnesia handle concurrent access?"
---

# Quick Definition

An Mnesia transaction wraps a sequence of database reads and writes in a zero-argument fun passed to `mnesia:transaction/1`, so that either all operations succeed or none do. Transactions guard against faulty code and concurrent access.

# Core Definition

A transaction is built by writing a fun `F` with zero arguments that calls some combination of `mnesia:write/1`, `mnesia:delete/1`, `mnesia:read/1`, or `qlc:e(Q)`, then calling `mnesia:transaction(F)`, which evaluates the expression sequence in the fun ("Mnesia Transactions"). "Either all the reads and writes to the tables in the database within a particular transaction succeed, or none of them does. If none of them does, the transaction is said to fail" — and on failure no changes are made to the database. Mnesia uses pessimistic locking: when the transaction manager accesses a table it locks the record or whole table; if deadlock is detected it aborts the transaction and undoes its changes. A transaction that fails because another process holds the data is retried after a short wait — so the transaction fun may be evaluated many times. A successful transaction returns `{atomic, Val}`; an aborted one returns `{aborted, Reason}`.

# Prerequisites

- **Mnesia** — Transactions are the safe access path into an Mnesia database.
- **Mnesia table** — Transactions read and write table rows.
- **Fun** — A transaction is a zero-argument fun passed to `mnesia:transaction/1`.

# Key Properties

1. A transaction is a zero-arity fun passed to `mnesia:transaction/1`.
2. All operations in the transaction succeed together or none do (atomicity).
3. Uses pessimistic locking and aborts on detected deadlock.
4. A failed transaction is retried after a short wait, so the fun may run many times.
5. On success returns `{atomic, Val}` where `Val` is the value of the fun; on abort returns `{aborted, Reason}`.
6. `mnesia:abort(Reason)` explicitly aborts a transaction and undoes its changes.
7. The transaction fun must have no side effects (e.g. no `io:format`), because it may be retried.

# Construction / Recognition

## To Write a Transaction:
1. Build a zero-argument fun `F` that performs the reads/writes/queries.
2. Use only `mnesia:read/1`, `mnesia:write/1`, `mnesia:delete/1`, or `qlc:e(Q)` inside it.
3. Keep the fun side-effect-free.
4. Call `mnesia:transaction(F)`.
5. Match the result: `{atomic, Val}` on success, `{aborted, Reason}` on failure.

## To Recognize:
1. Look for a fun passed to `mnesia:transaction/1`.
2. Look for `{atomic, _}` / `{aborted, _}` result handling.

# Context & Application

Transactions are the default, safe way to use Mnesia.

- **Typical contexts**: Any read or write that must be consistent under concurrent access — e.g. two people withdrawing from one bank account, where exactly one should succeed.
- **Common applications**: Wrapping `mnesia:write/1`, `mnesia:read/1`, and QLC evaluation in a transaction fun.
- **Historical/stylistic notes**: For pure efficiency in single-threaded or special cases, dirty operations bypass transactions.

# Examples

**Example 1** ("Adding a Row"): A write wrapped in a transaction.

```erlang
add_shop_item(Name, Quantity, Cost) ->
    Row = #shop{item=Name, quantity=Quantity, cost=Cost},
    F = fun() -> mnesia:write(Row) end,
    mnesia:transaction(F).
```

**Example 2** ("The do() Function"): Evaluating a QLC query inside a transaction.

```erlang
do(Q) ->
    F = fun() -> qlc:e(Q) end,
    {atomic, Val} = mnesia:transaction(F),
    Val.
```

## Worked Example

From "Aborting a Transaction", the `farmer/1` function updates the apple count, then aborts if there are not enough oranges. When `mnesia:abort(oranges)` runs, the earlier `mnesia:write` of the apple count is undone — calling `test_mnesia:farmer(100)` returns `{aborted, oranges}` and the database is left unchanged.

# Relationships

## Builds Upon
- **Mnesia table** — Transactions operate on table rows.

## Enables
- **Mnesia query (QLC)** — `qlc:e(Q)` is evaluated inside a transaction fun.

## Related
- **Fun** — The transaction is delivered as a fun.

## Contrasts With
- **Mnesia dirty operations** — Dirty operations run outside any transaction context: fast but without atomicity or locking guarantees.

# Common Errors

- **Error**: Performing side effects (e.g. `io:format`) inside the transaction fun.
  **Correction**: The fun may be retried many times; keep it side-effect-free.

- **Error**: Catching exceptions thrown by `mnesia:write/1`/`mnesia:delete/1` inside the fun.
  **Correction**: Never catch these — the transaction mechanism relies on those exceptions to detect failure; catching them breaks the mechanism.

# Common Confusions

- **Confusion**: Thinking the transaction fun runs exactly once.
  **Clarification**: On contention the transaction is retried, so the fun can run many times.

- **Confusion**: Believing a failed transaction leaves partial changes.
  **Clarification**: On abort, all changes are undone and the database state is restored.

# Source Reference

Chapter 20: "Mnesia: The Erlang Database", section "Mnesia Transactions", including "Aborting a Transaction", "Loading the Test Data", and "The do() Function".

# Verification Notes

- Definition source: Direct quotes and synthesis from "Mnesia Transactions".
- Confidence rationale: HIGH — transactions, atomicity, pessimistic locking, and retry behavior are explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
