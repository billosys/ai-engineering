---
concept: Mnesia Dirty Operation
slug: mnesia-dirty-operation
category: distribution
subcategory: mnesia
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Mnesia and the Art of Remembering"
chapter_number: 29
pdf_page: null
section: "Access and Context"
extraction_confidence: high
aliases:
  - "async_dirty"
  - "sync_dirty"
  - "dirty context"
prerequisites:
  - mnesia
  - mnesia-transaction
related:
  - mnesia-replication
contrasts_with:
  - mnesia-transaction
answers_questions:
  - "What are Mnesia dirty operations?"
  - "When should I use async_dirty or sync_dirty instead of a transaction?"
---

# Mnesia Dirty Operation

## Quick Definition

A Mnesia dirty operation runs database actions in an activity context (`async_dirty` or `sync_dirty`) that bypasses transaction protocols and locking for speed, at the cost of isolation guarantees.

## Core Definition

Beyond transactions, Mnesia offers *dirty* activity access contexts that bypass all transaction protocols and locking activities while still performing logging, replication, and so on. `async_dirty` performs all actions locally and returns, leaving replication on other nodes to happen asynchronously (it does wait for any active transactions to finish first). `sync_dirty` is to `async_dirty` what `sync_transaction` is to `transaction`: it waits for confirmation that operations succeeded on remote nodes, but still stays outside any locking or transaction context. Dirty contexts are generally faster than transactions but "absolutely riskier by design" — they should be handled with care. There is also an `ets` context that bypasses everything Mnesia does to operate directly on the underlying ETS tables (Chapter 29, "Access and Context").

## Prerequisites

- **Mnesia** — Dirty operations are Mnesia activity contexts
- **Mnesia transaction** — Dirty contexts are best understood as the lock-free counterpart to transactions

## Key Properties

1. `async_dirty` and `sync_dirty` bypass the transaction protocol and locking
2. They still perform logging and replication
3. `async_dirty` acts locally then returns, replicating to other nodes asynchronously
4. `async_dirty` waits for active transactions to finish before proceeding
5. `sync_dirty` waits for confirmation from remote nodes; `async_dirty` does not
6. Dirty contexts are faster than transactions but lose isolation/atomicity guarantees
7. The `ets` context bypasses Mnesia entirely, doing raw operations on underlying ETS tables with no replication
8. All contexts are invoked the same way: `mnesia:activity(Context, Fun)`

## Construction / Recognition

## To Run a Dirty Operation

1. Wrap the operations in a `fun`
2. Call `mnesia:activity(async_dirty, Fun)` for fastest, fire-and-forget replication, or `sync_dirty` to wait for remote confirmation
3. Reserve the `ets` context for cases where you knowingly need raw, unreplicated ETS access

## Context & Application

Dirty operations are for cases where the locking and coordination cost of a transaction is unacceptable and the loss of isolation is acceptable. The chapter advises that the `ets` context "isn't something you usually need to use" — "you'll know when you need it; if in doubt, don't use it." Dirty contexts should be used only when the risk is understood.

## Examples

The chapter describes the dirty contexts conceptually within the activity-context list rather than with a dedicated `mafiapp` code example; the `mafiapp` functions all use `transaction`.

## Relationships

## Builds Upon

- **Mnesia** — Dirty operations are Mnesia activity contexts

## Related

- **Mnesia replication** — Dirty contexts still replicate (asynchronously for `async_dirty`)

## Contrasts With

- **Mnesia transaction** — Transactions give isolation and atomicity with locking; dirty contexts skip locking for speed and give up those guarantees

## Common Errors

- **Error**: Using a dirty context for read-modify-write logic that needs isolation
  **Correction**: Use a transaction; dirty contexts can interleave with other operations and corrupt invariants

## Common Confusions

- **Confusion**: Thinking dirty contexts skip replication
  **Clarification**: Dirty contexts still log and replicate — they only skip the transaction protocol and locking; `async_dirty` just replicates asynchronously

## Source Reference

Chapter 29: Mnesia and the Art of Remembering, section "Access and Context" (the `async_dirty`, `sync_dirty`, and `ets` contexts).

## Verification Notes

- Definition: Direct adaptation from "Access and Context"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly defined alongside the transaction contexts
- Cross-references: verified against planned cards in this extraction
