---
concept: Mnesia Transaction
slug: mnesia-transaction
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
  - "transaction"
  - "activity access context"
prerequisites:
  - mnesia
related:
  - mnesia-dirty-operation
  - mnesia-replication
contrasts_with:
  - mnesia-dirty-operation
answers_questions:
  - "What is an Mnesia transaction?"
  - "What activity access contexts does Mnesia provide?"
---

# Mnesia Transaction

## Quick Definition

An Mnesia transaction is an activity access context that runs a series of database operations as a single isolated, all-or-nothing functional block across all nodes.

## Core Definition

All reads and modifications to an Mnesia table must run inside an *activity access context*. The `transaction` context lets you run a series of database operations as a single functional block: the whole block runs on all nodes or on none of them — it succeeds entirely or fails entirely — and when it returns, the tables are guaranteed consistent and isolated from other transactions even if they touched the same data. Operations are wrapped in a `fun` and executed with `mnesia:activity(Context, Fun)`. A transaction is partially asynchronous: synchronous on the local node, but for remote nodes it waits only for their commitment to commit, not for the commit itself; `sync_transaction` is the fully synchronous variant (Chapter 29, "Access and Context").

## Prerequisites

- **Mnesia** — Transactions are Mnesia's activity contexts

## Key Properties

1. Runs a block of operations as a single atomic, isolated unit
2. All-or-nothing across all nodes — succeeds entirely or fails entirely
3. Provides consistency and isolation between concurrent transactions
4. Partially asynchronous: synchronous locally, waits only for remote nodes' agreement to commit
5. May report success but be rolled back later if a network/hardware failure prevents a remote commit
6. `sync_transaction` is fully synchronous — waits for final confirmation from all nodes
7. A transaction's `fun` may be executed many times on retry, so it must contain no side effects
8. Transactions can be nested, though nesting is often unnecessary

## Construction / Recognition

## To Run a Transaction

1. Wrap the database operations (e.g., `mnesia:read/1`, `mnesia:write/1`) in a zero-argument `fun`
2. Execute it with `mnesia:activity(transaction, Fun)` (or `sync_transaction` for full synchrony)
3. Keep all side effects (messages, spawns, external calls) out of the `fun`

## Context & Application

Transactions are vital when concurrent reads and writes must act as one unit — for example, checking whether a username is taken and then creating the user. Without a transaction, those are two separate operations and a race can let multiple processes create the same unique user. Use `sync_transaction` when transaction success must be certain before triggering side effects, or to throttle an overloaded cluster. The chapter recommends doing as much validation as possible *outside* the transaction, since transaction code may run repeatedly and competes for database resources.

## Examples

**Example** (Chapter 29, "Implementing the First Requests"): `add_friend/4` wraps `mnesia:write(#mafiapp_friends{...})` in a `fun` and calls `mnesia:activity(transaction, F)`; `add_service/4` reads both friends and conditionally writes, all within one transaction.

## Relationships

## Builds Upon

- **Mnesia** — Transactions are one of Mnesia's activity access contexts

## Related

- **Mnesia dirty operation** — The faster, riskier alternative contexts
- **Mnesia replication** — A transaction commits coordinated across all replica nodes

## Contrasts With

- **Mnesia dirty operation** — Dirty contexts bypass locking and the transaction protocol; transactions provide isolation and atomicity but are slower

## Common Errors

- **Error**: Sending a message or spawning a process inside a transaction `fun`
  **Correction**: A transaction may run many times; side effects could fire repeatedly — keep them out of the `fun`

- **Error**: Doing heavy input validation inside the transaction
  **Correction**: Validate outside the transaction where possible; transaction code competes for database resources

## Common Confusions

- **Confusion**: Believing a successful `transaction` return guarantees the commit everywhere
  **Clarification**: `transaction` waits only for remote nodes to agree; it may roll back later — use `sync_transaction` for full certainty

## Source Reference

Chapter 29: Mnesia and the Art of Remembering, section "Access and Context."

## Verification Notes

- Definition: Direct adaptation from "Access and Context"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly defined and contrasted with the synchronous and dirty variants
- Cross-references: verified against planned cards in this extraction
