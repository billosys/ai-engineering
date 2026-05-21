---
concept: ETS Concurrency Option
slug: ets-concurrency-option
category: performance
subcategory: in-memory-storage
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Bears, ETS, Beets: In-Memory NoSQL for Free!"
chapter_number: 25
pdf_page: null
section: "Creating and Deleting Tables"
extraction_confidence: high
aliases:
  - "read_concurrency"
  - "write_concurrency"
  - "ETS concurrency options"
prerequisites:
  - ets-table
extends: []
related:
  - ets-table-type
contrasts_with: []
answers_questions:
  - "What are the ETS read_concurrency and write_concurrency options?"
  - "When should I enable ETS concurrency options?"
  - "How does ETS table locking work?"
---

# ETS Concurrency Option

## Quick Definition

`read_concurrency` and `write_concurrency` are `ets:new/2` options that tune a table for concurrent access. They trade off the cost of reads versus writes and can hurt performance if misapplied.

## Core Definition

By default, writing to an ETS table "will lock the whole thing and no one else can access it, either for reading or writing, until the writing is done" (Ch. 25, "Creating and Deleting Tables"). Two options change this. `{read_concurrency, true}` makes reads much cheaper but makes switching to writes more expensive — enable it when you do a lot of reading and little writing. `{write_concurrency, true}` lets reads and writes happen concurrently without affecting ETS's ACID properties, but reduces single-process sequential write performance and concurrent read capacity. The two can be combined when both reads and writes come in large bursts.

## Prerequisites

- **Ets-table** — Concurrency options are set when creating a table

## Key Properties

1. By default a write locks the whole table against all reads and writes until done
2. `{read_concurrency, true}` makes reads cheaper but makes switching to writes more expensive
3. `read_concurrency` suits read-heavy, write-light workloads needing an extra performance kick
4. With interleaved reads and writes, `read_concurrency` can hurt performance
5. `{write_concurrency, true}` allows concurrent reads and writes without breaking ACID properties
6. `write_concurrency` reduces single-process sequential write speed and concurrent read capacity
7. Combining both options helps when reads and writes both arrive in large bursts

## Construction / Recognition

### To choose concurrency options

1. Read-heavy, write-light, need speed → `{read_concurrency, true}`
2. Reads and writes interleaved → leave `read_concurrency` off
3. Both reads and writes in large bursts → combine `read_concurrency` and `write_concurrency`

## Context & Application

These options are a tuning tool. The book stresses they can hurt rather than help if the access pattern does not match the option's intent.

## Examples

The book does not provide a code listing for these options; they are described as `ets:new/2` options. (The source provides no explicit code example for the concurrency options specifically.)

## Relationships

### Builds Upon

- **Ets-table** — Concurrency options are part of `ets:new/2`

### Related

- **Ets-table-type** — Both are creation-time table options

## Common Errors

- **Error**: Enabling `read_concurrency` on a table with interleaved reads and writes.
  **Correction**: It helps only when reading dominates; with interleaving it may hurt performance.
- **Error**: Assuming `write_concurrency` is free.
  **Correction**: It reduces single-process sequential write speed and concurrent read capacity.

## Common Confusions

- **Confusion**: Thinking ETS allows fully free concurrent access by default.
  **Clarification**: By default a write locks the whole table; concurrency options must be opted into.
- **Confusion**: Believing `write_concurrency` weakens ACID guarantees.
  **Clarification**: It allows concurrent reads/writes without affecting ETS's ACID properties.

## Source Reference

Chapter 25, "Bears, ETS, Beets: In-Memory NoSQL for Free!", section "Creating and Deleting Tables" (the `read_concurrency` and `write_concurrency` option entries).

## Verification Notes

- Definition: Direct adaptation from the option descriptions
- Key Properties: All explicit in source
- Confidence: HIGH — the section describes both options precisely
- Cross-references: `ets-table`, `ets-table-type` planned this chapter
