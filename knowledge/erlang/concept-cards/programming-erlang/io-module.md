---
# === CORE IDENTIFICATION ===
concept: io Module
slug: io-module

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
section: "Modules for Manipulating Files"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "io"
  - "io:read"
  - "io:get_line"
  - "io:format"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - file-module
extends: []
related:
  - file-consult
  - file-modes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the io module do?"
  - "How do I read a term or a line from an open file?"
  - "How do I write formatted output to a file?"
---

# Quick Definition

`io` is the Erlang module of routines that work on already-opened files (I/O devices): reading terms and lines, and writing formatted output.

# Core Definition

The `io` module has routines that work on opened files; it contains routines for parsing data in a file and writing formatted data to a file (Chapter 16, "Modules for Manipulating Files"). Key functions: `io:read(IoDevice, Prompt)` reads an Erlang term from `IoDevice`, returning `{ok, Term}`, `{error, Why}`, or `eof` (the prompt is ignored for an opened file and used only for standard input); `io:get_line(IoDevice, Prompt)` reads characters until a line feed or end-of-file; and `io:format(IoDevice, Format, Args)` writes formatted output, where `IoDevice` must have been opened in `write` mode, `Format` is a string of formatting codes beginning with `~`, and `Args` is a list of items to output. Common format codes are `~n` (line feed, platform-aware), `~p` (pretty-print), `~s` (string/IO-list/atom without quotes), and `~w` (standard term syntax).

# Prerequisites

- **file module** — `io` routines operate on devices produced by `file:open`.

# Key Properties

1. `io` routines operate on already-opened I/O devices.
2. `io:read/2` reads one Erlang term, returning `{ok, Term}`, `{error, Why}`, or `eof`.
3. `io:get_line/2` reads characters up to a line feed or end-of-file.
4. `io:format/3` writes formatted output to a `write`-mode device.
5. Format codes begin with `~`; common ones are `~n`, `~p`, `~s`, `~w`.

# Construction / Recognition

## To Use the io Module:
1. Open the file with `file:open` (`read` or `write` mode as needed).
2. Read terms with `io:read(S, '')` or lines with `io:get_line(S, '')` until `eof`.
3. Write formatted output with `io:format(S, Format, Args)`.
4. Close the device with `file:close`.

## To Recognize It:
1. Look for `io:read`, `io:get_line`, and `io:format` calls on an open device.
2. Look for `~`-prefixed format strings.

# Context & Application

- **Typical contexts**: Term-by-term and line-by-line file processing; formatted file output.
- **Common applications**: The naive `consult` reads terms with `io:read`; `unconsult` writes terms with `io:format(S, "~p.~n", [X])`.
- **Historical/stylistic notes**: The author says he remembers only `~p`, `~s`, and `~n` and points to the `io` manual page for the full set of format codes.

# Examples

**Example 1** (Chapter 16, "Reading the Terms in the File One at a Time"): `io:read(S, '')` reads one term at a time from an open file, returning `{ok, Term}` and finally `eof`.

**Example 2** (Chapter 16, "Writing Lines to a File"): `io:format(S, "~s~n", ["Hello readers"])` writes the line `Hello readers` to the open device `S`.

# Relationships

## Builds Upon
- **file module** — `io` works on devices opened by `file`.

## Enables
- Term-by-term, line-by-line, and formatted file I/O.

## Related
- **file:consult** — its naive implementation uses `io:read`; `unconsult` uses `io:format`.
- **file modes** — `io:format` requires a `write`-mode device.

## Contrasts With
- A module of device routines; no commonly confused counterpart in this chapter.

# Common Errors

- **Error**: Calling `io:format/3` on a device opened in `read` mode.
  **Correction**: The I/O device must be opened in `write` mode for `io:format`.
- **Error**: Providing a format string whose `~` codes do not match the number of `Args`.
  **Correction**: Each item in `Args` needs a corresponding formatting command.

# Common Confusions

- **Confusion**: `io:read` reads a line of text.
  **Clarification**: `io:read` reads an Erlang *term*; `io:get_line` reads a line.
- **Confusion**: The `Prompt` argument matters for files.
  **Clarification**: For an opened file the prompt is ignored; it only matters for standard input.

# Source Reference

Chapter 16: Programming with Files, section "Modules for Manipulating Files" (the `io` description) and sections "Reading the Terms in the File One at a Time" (`io:read`), "Reading the Lines in a File One at a Time" (`io:get_line`), and "Writing a List of Terms to a File" / "Writing Lines to a File" (`io:format`).

# Verification Notes

- Definition source: Direct adaptation of the `io` module description and the `io:read`/`io:get_line`/`io:format` specs.
- Confidence rationale: HIGH — the `io` module and its key functions are explicitly described with examples.
- Uncertainties: None.
- Cross-reference status: Slugs match planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
