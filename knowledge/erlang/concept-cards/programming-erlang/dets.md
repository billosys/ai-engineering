---
# === CORE IDENTIFICATION ===
concept: DETS (Disk ETS)
slug: dets

# === CLASSIFICATION ===
category: performance
subcategory: term-storage
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Storing Data with ETS and DETS"
chapter_number: 19
pdf_page: null
section: "Storing Tuples on Disk"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "disk ETS"
  - dets
  - "DETS table"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ets
  - tuple
extends: []
related:
  - ets-vs-dets
  - mnesia
contrasts_with:
  - ets

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is DETS?"
  - "How do I store Erlang tuples on disk?"
  - "How does ETS relate to DETS?"
---

# Quick Definition

DETS (Disk ETS) is a system module that provides persistent, disk-resident storage of Erlang tuples with almost the same interface as ETS, at the cost of being far slower.

# Core Definition

"DETS is short for disk ETS" — `dets` is a system module for "the efficient storage of large numbers of Erlang terms" ("Storing Data with ETS and DETS"). "DETS provides almost the same interface as ETS but stores the tables on disk. Because DETS uses disk storage, it is far slower than ETS but will have a much smaller memory footprint when running." "ETS tables store tuples in memory. DETS (short for Disk ETS) provides Erlang tuple storage on disk. DETS files have a maximum size of 2GB" ("Storing Tuples on Disk"). Data in DETS tables "is persistent and should survive an entire system crash." "DETS files must be opened before they can be used, and they should be properly closed when finished with. If they are not properly closed, then they will be automatically repaired the next time they are opened" — and the repair "can take a long time."

# Prerequisites

- **ETS** — DETS shares almost the same interface and concepts as ETS.
- **Tuple** — A DETS table is a collection of tuples, keyed on one element.

# Key Properties

1. Disk resident — tables are stored on disk, not in RAM.
2. Persistent — data should survive an entire system crash.
3. Far slower than ETS, but with a much smaller memory footprint.
4. DETS files have a maximum size of 2 GB.
5. A DETS file must be opened (`dets:open_file`) before use and closed (`dets:close`) when finished.
6. If not closed properly, the table is automatically repaired on next open — which can be slow.
7. Opened by global name: processes opening a table with the same name and options share it; the table stays open until all sharers close it (or crash).

# Construction / Recognition

## To use a DETS table:
1. Open or create the file with `dets:open_file(Name, [{file, File}])`, matching `{ok, Name}`.
2. Insert tuples with `dets:insert(Name, X)` (a tuple or list of tuples).
3. Look up tuples with `dets:lookup(Name, Key)`, returning a list of matching tuples.
4. Close the table with `dets:close(Name)` when finished.

# Context & Application

- **Typical contexts**: Storing data that must persist across application runs and system crashes.
- **Common applications**: The chapter's `lib_filenames_dets` builds a persistent disk table mapping filenames to integer indexes and back.
- **Historical/stylistic notes**: Mnesia uses DETS (and ETS) internally; many `dets` routines are intended for internal use by Mnesia.

# Examples

**Example 1** ("Example: A Filename Index", `lib_filenames_dets.erl`): `open/1` calls `dets:open_file(?MODULE, [{file, File}])` and seeds a new table with `dets:insert(?MODULE, {free,1})`.

**Example 2** (same): `filename2index/1` does `dets:lookup(?MODULE, FileName)` and, on a miss, inserts three tuples — `[{Free,FileName},{FileName,Free},{free,Free+1}]`.

## Worked Example

```erlang
open(File) ->
    Bool = filelib:is_file(File),
    case dets:open_file(?MODULE, [{file, File}]) of
        {ok, ?MODULE} ->
            case Bool of
                true  -> void;
                false -> ok = dets:insert(?MODULE, {free,1})
            end,
            true;
        {error,Reason} ->
            exit({eDetsOpen, File, Reason})
    end.

close() -> dets:close(?MODULE).
```

# Relationships

## Related
- **ETS vs DETS** — The comparison of memory vs. disk storage.
- **Mnesia** — Mnesia is built on top of DETS and ETS.

## Contrasts With
- **ETS** — ETS is in-memory and transient; DETS is on-disk and persistent (and slower).

# Common Errors

- **Error**: Failing to close a DETS table before the application finishes.
  **Correction**: Always `dets:close` the table; an unclosed table triggers a slow automatic repair on next open.

- **Error**: Calling `dets:open_file` without checking whether the file already exists when initialization is needed.
  **Correction**: `dets:open_file` both creates and opens; check `filelib:is_file/1` first if you need to seed a fresh table.

# Common Confusions

- **Confusion**: Thinking DETS tables are unlimited in size.
  **Clarification**: DETS files have a maximum size of 2 GB.

- **Confusion**: Believing DETS and ETS are completely different APIs.
  **Clarification**: DETS provides almost the same interface as ETS; `insert` and `lookup` work the same way.

# Source Reference

Chapter 19: "Storing Data with ETS and DETS", chapter introduction and section "Storing Tuples on Disk" (subsection "Example: A Filename Index"). Code from `lib_filenames_dets.erl`.

# Verification Notes

- Definition source: Direct quotes from chapter intro and "Storing Tuples on Disk".
- Confidence rationale: HIGH — DETS is explicitly defined with worked code.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs `ets`, `tuple`, `mnesia` used.
- Re-extraction notes: Fresh extraction; overwrites prior card.
