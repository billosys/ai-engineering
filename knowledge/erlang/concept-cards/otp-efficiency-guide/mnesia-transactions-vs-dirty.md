---
concept: Mnesia Transactions vs Dirty Operations
slug: mnesia-transactions-vs-dirty
category: data-structures
subcategory: mnesia
tier: advanced
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Tables and Databases"
chapter_number: null
pdf_page: null
section: "Transactions"
extraction_confidence: high
aliases:
  - "Mnesia dirty operations"
  - "mnesia:transaction vs dirty"
  - "dirty_read"
  - "dirty_write"
prerequisites:
  - non-persistent-storage-ets-vs-mnesia
extends: []
related:
  - mnesia-secondary-index
  - ets-key-usage-and-indexing
contrasts_with: []
answers_questions:
  - "What distinguishes Mnesia transactions from dirty operations?"
  - "What must I know before choosing between ETS and Mnesia?"
---

# Quick Definition

Mnesia transactions guarantee consistency for distributed tables but carry performance overhead. Dirty operations (`dirty_read`, `dirty_write`) bypass transaction overhead but lose the consistency guarantee. For real-time requirements, dirty operations are recommended with consistency ensured by limiting writes to a single process.

# Core Definition

The Efficiency Guide states (Tables and Databases chapter, "Transactions" section under Mnesia): "Using transactions is a way to guarantee that the distributed Mnesia database remains consistent, even when many different processes update it in parallel. However, if you have real-time requirements it is recommended to use dirty operations instead of transactions."

On the consistency trade-off: "When using dirty operations, you lose the consistency guarantee; this is usually solved by only letting one process update the table. Other processes must send update requests to that process."

The performance hierarchy is:
1. ETS operations (fastest)
2. Mnesia dirty operations (faster than transactions, slower than ETS)
3. Mnesia transactions (slowest, but consistent)

# Prerequisites

- **non-persistent-storage-ets-vs-mnesia** -- Understanding the performance relationship between ETS and Mnesia

# Key Properties

1. Transactions guarantee consistency for distributed Mnesia tables
2. Transactions handle parallel updates by multiple processes safely
3. Dirty operations bypass transaction overhead
4. Dirty operations do not guarantee consistency
5. For real-time requirements, dirty operations are recommended
6. Consistency without transactions is achieved by designating a single writer process
7. Non-writer processes send update requests to the writer process
8. Dirty operations include `dirty_read`, `dirty_write`, `dirty_index_read`, etc.

# Construction / Recognition

## Transactional Operations

```erlang
Fun = fun() ->
          [mnesia:read({Table, Key}),
           mnesia:read({Table2, Key2})]
      end,
{atomic, [Result1, Result2]} = mnesia:transaction(Fun).
```

## Dirty Operations (Equivalent)

```erlang
Result1 = mnesia:dirty_read({Table, Key}),
Result2 = mnesia:dirty_read({Table2, Key2}).
```

## Single-Writer Pattern for Dirty Operations

1. Designate one process as the writer for each table
2. All other processes read with `dirty_read` (safe for reads)
3. Other processes send update messages to the writer process
4. The writer process performs `dirty_write` operations

# Context & Application

The transaction vs. dirty trade-off is fundamental to Mnesia application design. Transactions use a protocol (based on the "no dirty read" isolation level) that involves inter-node communication and locking, making them significantly slower than dirty operations.

In practice, many Erlang/OTP applications use dirty operations for performance-critical paths and transactions only where strict consistency across distributed nodes is required. The single-writer pattern is a well-established Erlang idiom that leverages the sequential execution guarantee of Erlang processes to provide consistency without transaction overhead.

This trade-off also factors into the ETS vs. Mnesia decision: if neither transactions nor distribution are needed, ETS is always the fastest option.

# Examples

**Transactional read** (Tables and Databases chapter):
```erlang
Fun = fun() ->
          [mnesia:read({Table, Key}),
           mnesia:read({Table2, Key2})]
      end,
{atomic, [Result1, Result2]} = mnesia:transaction(Fun).
```

**Dirty read equivalent** (Tables and Databases chapter):
```erlang
Result1 = mnesia:dirty_read({Table, Key}),
Result2 = mnesia:dirty_read({Table2, Key2}).
```

# Relationships

## Related

- **mnesia-secondary-index** -- Index reads also have transactional (`index_read/3`) and dirty (`dirty_index_read/3`) variants
- **ets-key-usage-and-indexing** -- ETS operations are faster than both Mnesia transaction and dirty operations

## Performance Hierarchy

- ETS write < Mnesia dirty_write < Mnesia transactional write
- Non-persistent storage should use ETS (see `non-persistent-storage-ets-vs-mnesia`)

# Common Errors

- **Error**: Using transactions for all Mnesia operations in a real-time system
  **Correction**: Use dirty operations for performance-critical paths; reserve transactions for operations requiring strict consistency

- **Error**: Using dirty operations from multiple processes writing to the same table without coordination
  **Correction**: Designate a single writer process; other processes send update requests to it

- **Error**: Assuming dirty reads are unsafe
  **Correction**: Dirty reads are safe for most use cases; it is dirty writes from multiple processes that can cause inconsistency

# Common Confusions

- **Confusion**: Thinking dirty operations are "wrong" or "hacky"
  **Clarification**: Dirty operations are a deliberate, documented feature of Mnesia for performance-critical use cases; the official guide recommends them for real-time requirements

- **Confusion**: Believing the single-writer pattern is a workaround
  **Clarification**: It is the recommended Erlang idiom for maintaining consistency with dirty operations, leveraging the sequential execution of Erlang processes

- **Confusion**: Thinking transactions and dirty operations cannot coexist
  **Clarification**: An application can use transactions for some operations and dirty operations for others; the choice is per-operation

# Source Reference

Tables and Databases chapter, "Transactions" section (under "Mnesia" heading). Includes code examples comparing transactional and dirty read operations.

# Verification Notes

- Definition: Directly quoted from source text
- Code examples: Verbatim from source
- Single-writer pattern: Described in source text
- Confidence: HIGH -- explicit comparison with code examples in official documentation
