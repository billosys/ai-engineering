---
# === CORE IDENTIFICATION ===
concept: File Modes
slug: file-modes

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
section: "Bits and Pieces"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "open modes"
  - "read mode"
  - "write mode"
  - "raw mode"
  - "binary mode"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - file-module
extends: []
related:
  - random-access-file-io
  - binary
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What file modes can I open a file in?"
  - "How do I open a file for random access?"
  - "What does raw mode do?"
---

# Quick Definition

File modes are the option flags passed to `file:open` that determine how a file is accessed — for example `read`, `write`, `binary`, `raw`, and `compressed` — and they can be combined.

# Core Definition

When you open a file with `file:open`, you open it in a particular mode or a combination of modes (Chapter 16, "Bits and Pieces"). There are many more modes than one might think — for example, it is possible to read and write gzip-compressed files with the `compressed` mode flag. `file:open(File, read)` opens a file for reading and returns `{ok, IoDevice}` or `{error, Why}`. The chapter also uses combined-mode lists: `file:open("data1.dat", [read,binary,raw])` opens a file for efficient random-access binary reading, and `file:open("some_filename_here", [raw,write,binary])` opens it for random-access binary writing. In `raw` mode the returned device is a low-level file descriptor used with `file:pread`/`file:pwrite`. The full list of modes is in the manual page for `file`.

# Prerequisites

- **file module** — Modes are arguments to `file:open`; understand the `file` module first.

# Key Properties

1. Modes are passed to `file:open` as a single atom or a list of atoms.
2. `read` opens for reading; `write` opens for writing.
3. `binary` causes data to be returned as binaries rather than lists.
4. `raw` gives a low-level file descriptor for efficient random access (`pread`/`pwrite`).
5. `compressed` allows reading/writing gzip-compressed files.
6. Modes can be combined, e.g. `[read,binary,raw]`.

# Construction / Recognition

## To Choose File Modes:
1. For ordinary term/line reading: `file:open(File, read)`.
2. For random-access binary reading: `file:open(File, [read,binary,raw])`.
3. For random-access binary writing: `file:open(File, [raw,write,binary])`.
4. For compressed files: include the `compressed` flag.

## To Recognize Them:
1. Look at the second argument of `file:open` — a mode atom or list.
2. `raw` mode returns a `file_descriptor` device rather than an ordinary I/O device.

# Context & Application

- **Typical contexts**: Choosing access semantics when opening any file.
- **Common applications**: `raw,binary` mode for the `id3_v1` MP3 tag reader and random-access examples.
- **Historical/stylistic notes**: The book lists modes briefly under "Bits and Pieces" and defers the full set to the manual pages.

# Examples

**Example 1** (Chapter 16, "Reading a File with Random Access"): `{ok, S} = file:open("data1.dat", [read,binary,raw])` opens the file in raw binary mode, yielding `{ok,{file_descriptor,prim_file,{#Port<0.106>,5}}}`.

**Example 2** (Chapter 16, "Writing to a Random-Access File"): `{ok, S} = file:open("some_filename_here", [raw,write,binary])` opens a file for random-access binary writing with `file:pwrite`.

# Relationships

## Builds Upon
- **file module** — modes parameterize `file:open`.

## Enables
- **Random-access file I/O** — `raw` mode underlies `pread`/`pwrite`.

## Related
- **Binary** — `binary` mode returns file data as binaries.

## Contrasts With
- A set of option flags; no commonly confused counterpart in this chapter.

# Common Errors

- **Error**: Using ordinary `read` mode then expecting `file:pread` to work efficiently.
  **Correction**: Open with `raw` mode for low-level random access.
- **Error**: Expecting list data after opening with `binary` mode.
  **Correction**: `binary` mode returns binaries; choose modes to match how you will process the data.

# Common Confusions

- **Confusion**: There are only a couple of file modes.
  **Clarification**: There are many — including `compressed` — and the book points to the manual for the full list.
- **Confusion**: `raw` mode returns the same kind of device as `read` mode.
  **Clarification**: `raw` mode returns a low-level `file_descriptor`, not an ordinary I/O device.

# Source Reference

Chapter 16: Programming with Files, section "Bits and Pieces" (the "File modes" description), with mode usage shown in "Reading a File with Random Access" and "Writing to a Random-Access File."

# Verification Notes

- Definition source: Direct adaptation of the "File modes" description and the random-access `file:open` examples.
- Confidence rationale: HIGH — modes are explicitly described and used in worked examples.
- Uncertainties: The exhaustive mode list is deferred to the manual; the card covers the modes the chapter uses.
- Cross-reference status: Slugs match canonical `binary` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
