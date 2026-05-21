---
# === CORE IDENTIFICATION ===
concept: Random-Access File I/O
slug: random-access-file-io

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
section: "Reading a File with Random Access"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "file:pread"
  - "file:pwrite"
  - "positional file access"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - file-module
  - file-modes
extends: []
related:
  - binary
  - bit-syntax
contrasts_with:
  - whole-file-io

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I read a specific portion of a file?"
  - "How do I read or write a file at a given byte offset?"
  - "When should I use random-access file I/O?"
---

# Quick Definition

Random-access file I/O reads or writes an arbitrary portion of a file at a specified byte offset, using `file:pread` and `file:pwrite` on a file opened in `raw` mode.

# Core Definition

If a file is very large or contains binary data in an externally defined format, you can open it in `raw` mode and read any portion of it using `file:pread` (Chapter 16, "Reading a File with Random Access"). `file:pread(IoDevice, Start, Len)` reads exactly `Len` bytes from `IoDevice` starting at byte `Start` — bytes are numbered from 0 — and returns `{ok, Bin}` or `{error, Why}`. Writing in random-access mode is similar: open the file in `write` mode (with `raw`/`binary`), then use `file:pwrite(IoDev, Position, Bin)` to write `Bin` at `Position`, overwriting the original content there.

# Prerequisites

- **file module** — `pread`/`pwrite` are `file` functions.
- **File modes** — Random access requires opening the file in `raw` mode.

# Key Properties

1. `file:pread(IoDevice, Start, Len)` reads exactly `Len` bytes starting at byte `Start`.
2. Bytes are numbered from 0 (the first byte is at position 0).
3. `file:pread` returns `{ok, Bin}` or `{error, Why}`.
4. `file:pwrite(IoDev, Position, Bin)` writes `Bin` at `Position`, overwriting existing content.
5. Random access requires the file to be opened in `raw` mode.

# Construction / Recognition

## To Read Randomly:
1. Open the file with `file:open(File, [read,binary,raw])`.
2. Call `file:pread(S, Start, Len)` for each region you need.
3. Close the file with `file:close(S)`.

## To Write Randomly:
1. Open the file with `file:open(File, [raw,write,binary])`.
2. Call `file:pwrite(S, Position, Bin)` to write at the offset.
3. Close the file.

# Context & Application

- **Typical contexts**: Very large files; binary formats with fixed-offset fields.
- **Common applications**: Reading the last 128 bytes of an MP3 file for its ID3v1 tag (`file:pread(S, Size-128, 128)`).
- **Historical/stylistic notes**: Random access pairs naturally with the bit syntax for parsing fixed-layout binary data.

# Examples

**Example 1** (Chapter 16, "Reading a File with Random Access"): After opening `data1.dat` in `[read,binary,raw]` mode, `file:pread(S, 22, 46)` reads 46 bytes starting at offset 22, returning `{ok,<<"rong\",\n\t[{occupation, programmer},\n\t {favorite">>}`.

**Example 2** (Chapter 16, "Writing to a Random-Access File"): `file:pwrite(S, 10, <<"new">>)` writes the characters `new` starting at offset 10, overwriting the original content there.

# Relationships

## Builds Upon
- **file module** and **file modes** — `pread`/`pwrite` on a `raw`-mode device.

## Enables
- Efficient access to large files and fixed-layout binary formats.

## Related
- **Binary** — `pread` returns binaries; `pwrite` takes a binary.
- **Bit syntax** — used to parse fixed-offset binary regions read by `pread`.

## Contrasts With
- **Whole-file I/O** — `read_file`/`write_file` move the entire file at once; random-access I/O touches only chosen regions.

# Common Errors

- **Error**: Numbering file bytes from 1.
  **Correction**: Bytes are numbered from 0; the first byte is at position 0.
- **Error**: Calling `pread`/`pwrite` on a file not opened in `raw` mode.
  **Correction**: Open the file in `raw` mode for random access.

# Common Confusions

- **Confusion**: `pwrite` inserts data, shifting the rest of the file.
  **Clarification**: `pwrite` overwrites the content at the given position; it does not insert.
- **Confusion**: Random access is the most efficient way to read a whole file.
  **Clarification**: For an entire file, `file:read_file` in one operation is the most efficient; random access is for portions.

# Source Reference

Chapter 16: Programming with Files, sections "Reading a File with Random Access" (`file:pread`) and "Writing to a Random-Access File" (`file:pwrite`); applied in "Reading MP3 Metadata."

# Verification Notes

- Definition source: Direct adaptation of the `file:pread` and `file:pwrite` descriptions and examples.
- Confidence rationale: HIGH — both functions are explicitly specified and demonstrated.
- Uncertainties: None.
- Cross-reference status: Slugs match canonical `binary`/`bit-syntax` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
