---
# === CORE IDENTIFICATION ===
concept: Whole-File I/O
slug: whole-file-io

# === CLASSIFICATION ===
category: tooling
subcategory: file-io
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming with Files"
chapter_number: 16
pdf_page: null
section: "Reading the Entire File into a Binary"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "file:read_file"
  - "file:write_file"
  - "read entire file"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - file-module
extends: []
related:
  - binary
  - io-list
contrasts_with:
  - random-access-file-io

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I read an entire file in one operation?"
  - "How do I write an entire file at once?"
  - "What is the most efficient way to read or write a file?"
---

# Quick Definition

Whole-file I/O reads or writes an entire file in a single atomic operation — `file:read_file` returns the whole file as a binary, and `file:write_file` writes an entire I/O list to a file.

# Core Definition

You can use `file:read_file(File)` to read an entire file into a binary using a single atomic operation; it returns `{ok, Bin}` on success and `{error, Why}` otherwise (Chapter 16, "Reading the Entire File into a Binary"). This is by far the most efficient way of reading files. The book's author recommends, for most operations, reading the entire file into memory in one operation, manipulating the contents, and storing the file in a single operation with `file:write_file`. `file:write_file(File, IO)` writes the data in `IO` — an *I/O list* — to `File`; an I/O list is a list whose elements are I/O lists, binaries, or integers from 0 to 255, and when output it is automatically "flattened" so the list brackets are removed (Chapter 16, "Writing an Entire File in One Operation").

# Prerequisites

- **file module** — `read_file`/`write_file` are `file` functions.

# Key Properties

1. `file:read_file(File)` reads the whole file as a binary in one atomic operation.
2. It returns `{ok, Bin}` on success, `{error, Why}` on failure.
3. `file:write_file(File, IO)` writes an entire I/O list to a file in one operation.
4. An I/O list may nest I/O lists, binaries, and integers 0–255; output flattens it automatically.
5. Whole-file I/O is the most efficient approach for entire-file reads and writes.

# Construction / Recognition

## To Read a Whole File:
1. Call `file:read_file(File)`.
2. Match `{ok, Bin}` or `{error, Why}`.

## To Write a Whole File:
1. Build the content as an I/O list (deep lists of binaries/integers are fine).
2. Call `file:write_file(File, IO)` — the I/O system flattens the list automatically.

# Context & Application

- **Typical contexts**: Reading or writing an entire file at once.
- **Common applications**: `scavenge_urls:urls2htmlFile` builds an I/O list of HTML and writes it with `file:write_file`; the read-modify-write idiom for most file processing.
- **Historical/stylistic notes**: The author notes he uses `read_file`/`write_file` "a lot"; not flattening the I/O list before writing is deliberate and efficient.

# Examples

**Example 1** (Chapter 16, "Reading the Entire File into a Binary"): `file:read_file("data1.dat")` returns `{ok,<<"{person, \"joe\", \"armstrong\""...>>}` — the whole file as a binary.

**Example 2** (Chapter 16, "Listing URLs from a File"): `urls2htmlFile(Urls, File) -> file:write_file(File, urls2html(Urls)).` writes a deep I/O list of HTML to a file; the I/O system flattens it on output.

# Relationships

## Builds Upon
- **file module** — `read_file`/`write_file` are `file` functions.

## Enables
- The efficient read-modify-write file-processing idiom.

## Related
- **Binary** — `read_file` returns a binary.
- **I/O list** — `write_file` accepts an I/O list and flattens it on output.

## Contrasts With
- **Random-access file I/O** — random access touches chosen byte ranges of a file; whole-file I/O moves the entire file at once.

# Common Errors

- **Error**: Manually flattening an I/O list before calling `file:write_file`.
  **Correction**: Pass the deep I/O list directly — the I/O system flattens it efficiently.
- **Error**: Using whole-file reads on a file too large to fit in memory.
  **Correction**: For very large files, use `raw` mode and `file:pread` random access instead.

# Common Confusions

- **Confusion**: `file:read_file` returns a list of characters.
  **Clarification**: It returns a binary; use `binary_to_list` if you need a list.
- **Confusion**: `file:write_file` requires a flat list of bytes.
  **Clarification**: It accepts any I/O list — nested lists of binaries and integers — and flattens it automatically.

# Source Reference

Chapter 16: Programming with Files, sections "Reading the Entire File into a Binary" (`file:read_file`) and "Writing an Entire File in One Operation" (`file:write_file` and the I/O list definition); applied in "Listing URLs from a File."

# Verification Notes

- Definition source: Direct adaptation of the `read_file`/`write_file` descriptions and the I/O list definition.
- Confidence rationale: HIGH — both functions and the I/O list concept are explicitly described with examples.
- Uncertainties: None.
- Cross-reference status: Slugs match canonical `binary` and planned chapter cards (`io-list`, `random-access-file-io`).
- Re-extraction notes: Fresh extraction; no pre-existing card.
