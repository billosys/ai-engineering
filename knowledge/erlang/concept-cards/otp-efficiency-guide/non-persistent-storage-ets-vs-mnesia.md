---
concept: Non-Persistent Storage ETS vs Mnesia
slug: non-persistent-storage-ets-vs-mnesia
category: performance
subcategory: ets
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Tables and Databases"
chapter_number: null
pdf_page: null
section: "Non-Persistent Database Storage"
extraction_confidence: high
aliases:
  - "ETS vs Mnesia for non-persistent storage"
  - "ETS vs Mnesia local_content"
prerequisites: []
extends: []
related:
  - ets-key-usage-and-indexing
  - mnesia-transactions-vs-dirty
contrasts_with: []
answers_questions:
  - "How do ETS tables compare to Mnesia for non-persistent storage?"
  - "What must I know before choosing between ETS and Mnesia?"
---

# Quick Definition

For non-persistent database storage, ETS tables are always faster than Mnesia `local_content` tables. Even Mnesia dirty operations carry fixed overhead compared to ETS because Mnesia must check for replication and indices on every write.

# Core Definition

The Efficiency Guide states (Tables and Databases chapter, "Non-Persistent Database Storage" section): "For non-persistent database storage, prefer Ets tables over Mnesia `local_content` tables. Even the Mnesia `dirty_write` operations carry a fixed overhead compared to Ets writes. Mnesia must check if the table is replicated or has indices, this involves at least one Ets lookup for each `dirty_write`. Thus, Ets writes are always faster than Mnesia writes."

The key insight is that Mnesia is built on top of ETS, so every Mnesia operation includes at least the cost of an ETS operation plus additional Mnesia overhead (replication checks, index checks).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. ETS writes are always faster than Mnesia writes
2. Mnesia `dirty_write` carries fixed overhead vs. ETS write
3. Mnesia must check for table replication on every write
4. Mnesia must check for indices on every write
5. Each Mnesia `dirty_write` involves at least one ETS lookup for these checks
6. This applies specifically to non-persistent (in-memory only) storage
7. For persistent or distributed storage, Mnesia provides features ETS cannot

# Construction / Recognition

## When to Choose ETS

1. Storage is non-persistent (in-memory only)
2. Data does not need to be replicated across nodes
3. Data does not need transactions
4. Maximum write performance is required

## When Mnesia May Still Be Appropriate

1. Data needs to be replicated across nodes
2. Data needs to be persistent (disc copies)
3. Transaction guarantees are required
4. Secondary indexes with automatic maintenance are needed

# Context & Application

This guidance applies specifically to the scenario where a developer needs a fast, in-memory key-value store on a single node. In this case, there is no reason to incur Mnesia's overhead. Mnesia's value proposition is in its distributed database features (replication, transactions, schema management, persistence) -- when those features are not needed, ETS is the right choice.

The observation that Mnesia is built on ETS is fundamental: Mnesia uses ETS tables internally, so its operations are always at least as expensive as direct ETS operations, plus the overhead of Mnesia's metadata management.

# Examples

**Performance hierarchy** (Tables and Databases chapter):

ETS write < Mnesia `dirty_write` < Mnesia transactional write

The source explains that even the fastest Mnesia operation (`dirty_write`) involves "at least one Ets lookup" for metadata checks, making it slower than a direct ETS write.

# Relationships

## Related

- **ets-key-usage-and-indexing** -- Understanding ETS tables as the underlying primitive
- **mnesia-transactions-vs-dirty** -- Dirty operations are faster than transactions, but both are slower than ETS

# Common Errors

- **Error**: Using Mnesia `local_content` tables for single-node, non-persistent storage
  **Correction**: Use ETS tables directly; they are always faster for this use case

- **Error**: Assuming Mnesia dirty operations have no overhead compared to ETS
  **Correction**: Even `dirty_write` involves at least one extra ETS lookup for replication/index checks

# Common Confusions

- **Confusion**: Thinking this advice means ETS is always better than Mnesia
  **Clarification**: The advice is specifically about non-persistent storage; Mnesia provides essential features for persistent, distributed, or transactional storage that ETS does not offer

- **Confusion**: Believing that Mnesia and ETS are independent subsystems
  **Clarification**: Mnesia is built on top of ETS; every Mnesia operation includes ETS operations plus additional overhead

# Source Reference

Tables and Databases chapter, "Non-Persistent Database Storage" section. Brief but explicit section stating the performance comparison.

# Verification Notes

- Definition: Directly quoted from source text
- Fixed overhead claim: Explicitly stated with the mechanism (ETS lookup for metadata)
- Confidence: HIGH -- direct, unambiguous performance comparison in official documentation
