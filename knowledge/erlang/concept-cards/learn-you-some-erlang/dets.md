---
concept: DETS
slug: dets
category: performance
subcategory: in-memory-storage
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Bears, ETS, Beets: In-Memory NoSQL for Free!"
chapter_number: 25
pdf_page: null
section: "DETS"
extraction_confidence: high
aliases:
  - "DETS"
  - "Disk ETS"
  - "dets module"
prerequisites:
  - ets-table
extends:
  - ets-table
related:
  - mnesia
contrasts_with:
  - ets-table
answers_questions:
  - "What is DETS?"
  - "What distinguishes DETS from ETS?"
  - "When should I use DETS instead of ETS?"
---

# DETS

## Quick Definition

DETS is a disk-based version of ETS. It shares nearly the same API but persists data to a file, with no `ordered_set` type and a 2GB file size limit.

## Core Definition

"DETS is a disk-based version of ETS, with a few key differences" (Ch. 25, "DETS"). It removes `ordered_set` tables, imposes a 2GB disk-size limit per file, and makes operations like `prev/1` and `next/1` slower and less safe. Table lifecycle also differs: a DETS table is created with `dets:open_file/2`, closed with `dets:close/1`, and reopened later with `dets:open_file/1`. Otherwise the API is nearly identical to ETS, giving a simple way to read and write data inside files.

## Prerequisites

- **Ets-table** — DETS is the disk-based counterpart and shares ETS's API and concepts

## Key Properties

1. DETS stores data on disk rather than in memory
2. There is no `ordered_set` table type in DETS
3. DETS files have a 2GB size limit
4. `prev/1` and `next/1` traversal operations are slower and less safe than in ETS
5. Tables open with `dets:open_file/2`, close with `dets:close/1`, reopen with `dets:open_file/1`
6. The rest of the API is nearly the same as ETS
7. DETS risks being slow because it is a disk-only database

## Construction / Recognition

### To use a DETS table

1. Open: `dets:open_file(Name, Options)`
2. Use ETS-like `insert`/`lookup` operations
3. Close: `dets:close(Name)`
4. Reopen later: `dets:open_file(Name)`

## Context & Application

DETS provides simple file-backed storage. The book suggests that coupling ETS and DETS for a RAM+disk database is possible but recommends Mnesia instead, which does the same while adding sharding, transactions, and distribution.

## Examples

The book describes the DETS differences in a bullet list rather than a code listing. (The source provides no explicit DETS code example.)

## Relationships

### Builds Upon / Extends

- **Ets-table** — DETS is ETS adapted for disk storage with a near-identical API

### Related

- **Mnesia** — Recommended over a hand-rolled ETS+DETS combination for RAM+disk storage

### Contrasts With

- **Ets-table** — ETS is in-memory, supports `ordered_set`, has no 2GB limit, and is faster

## Common Errors

- **Error**: Expecting `ordered_set` semantics from a DETS table.
  **Correction**: DETS has no `ordered_set` type.
- **Error**: Relying on `prev/1`/`next/1` traversal in DETS as if it were as fast/safe as ETS.
  **Correction**: These operations are slower and less safe on disk.

## Common Confusions

- **Confusion**: Thinking DETS is a drop-in for ETS in all cases.
  **Clarification**: The lifecycle differs (`open_file`/`close`), there is no `ordered_set`, and there is a 2GB limit.
- **Confusion**: Believing DETS is the best choice for combined RAM+disk storage.
  **Clarification**: The book recommends Mnesia for that, since it adds sharding, transactions, and distribution.

## Source Reference

Chapter 25, "Bears, ETS, Beets: In-Memory NoSQL for Free!", section "DETS."

## Verification Notes

- Definition: Direct adaptation from "DETS"
- Key Properties: All explicit in source
- Confidence: HIGH — the short section enumerates all the differences
- Cross-references: `ets-table` shared/planned this chapter; `mnesia` referenced as a later concept
