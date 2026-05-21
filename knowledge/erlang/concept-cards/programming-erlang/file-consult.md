---
# === CORE IDENTIFICATION ===
concept: file:consult
slug: file-consult

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
section: "Reading All the Terms in the File"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "file:consult/1"
  - "consult"
  - "unconsult"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - file-module
extends: []
related:
  - io-module
  - file-modes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I read Erlang terms from a file?"
  - "How do I read a config file of Erlang terms?"
  - "How do I write a file that file:consult can read back?"
---

# Quick Definition

`file:consult(File)` reads a file containing a sequence of Erlang terms and returns `{ok, [Term]}` if it can read all of them, or `{error, Reason}` otherwise.

# Core Definition

`file:consult(File)` assumes that `File` contains a sequence of Erlang terms; it returns `{ok, [Term]}` if it can read all the terms in the file, otherwise it returns `{error, Reason}` (Chapter 16, "Reading All the Terms in the File"). It is the convenient one-call way to load a file of Erlang terms, contrasting with reading terms one at a time via `file:open` + `io:read` + `file:close`. The book shows a simplified implementation of `consult` built from those lower-level functions, and notes the standard library uses an improved version with better error reporting. The chapter also defines `unconsult(File, L)` — not in the standard library — which writes a list of terms to a file (using `io:format(S, "~p.~n", [X])`) so the file can later be read back with `file:consult`.

# Prerequisites

- **file module** — `consult` is a function of the `file` module; understand the module first.

# Key Properties

1. `file:consult(File)` reads a file assumed to contain a sequence of Erlang terms.
2. It returns `{ok, [Term]}` on success — a list of all the terms.
3. It returns `{error, Reason}` if any term cannot be read.
4. It is a single-call alternative to `open` + repeated `io:read` + `close`.
5. The standard library version has better error reporting than the naive one shown in the book.

# Construction / Recognition

## To Read Terms with file:consult:
1. Ensure the file contains valid Erlang terms, each ended with a period.
2. Call `file:consult(File)`.
3. Match `{ok, Terms}` or `{error, Reason}`.

## To Write a Consultable File:
1. Open the file in `write` mode.
2. For each term, write it with `io:format(S, "~p.~n", [Term])` (the `unconsult` pattern).
3. Close the file.

# Context & Application

- **Typical contexts**: Loading configuration or data files expressed as Erlang terms.
- **Common applications**: Reading `data1.dat` (a `person` term and a `cat` term); round-tripping data written by `unconsult`.
- **Historical/stylistic notes**: The book uses `consult` to illustrate how a library function can be reconstructed from `file:open`, `io:read`, and `file:close`.

# Examples

**Example 1** (Chapter 16, "Reading All the Terms in the File"): `file:consult("data1.dat")` returns `{ok,[{person,"joe","armstrong",[{occupation,programmer},{favoriteLanguage,erlang}]},{cat,{name,"zorro"},{owner,"joe"}}]}`.

**Example 2** (Chapter 16, "Writing a List of Terms to a File"): `lib_misc:unconsult("test1.dat", [{cats,["zorrow","daisy"]},{weather,snowing}])` writes the terms; `file:consult("test1.dat")` then reads them back as `{ok,[{cats,["zorrow","daisy"]},{weather,snowing}]}`.

# Relationships

## Builds Upon
- **file module** — `consult` is one of its functions.

## Enables
- Loading Erlang-term data and configuration files in one call.

## Related
- **io module** — the naive `consult` implementation uses `io:read`; `unconsult` uses `io:format`.
- **file modes** — `consult` reads; `unconsult` opens in `write` mode.

## Contrasts With
- A convenience function; no commonly confused counterpart in this chapter.

# Common Errors

- **Error**: Calling `file:consult` on a file whose terms lack the trailing period.
  **Correction**: Each term must be terminated with a period, as Erlang terms in source are.
- **Error**: Expecting a bare list back from `file:consult`.
  **Correction**: It returns `{ok, [Term]}` (or `{error, Reason}`); match the tuple.

# Common Confusions

- **Confusion**: `unconsult` is a standard library function.
  **Clarification**: The standard libraries do not contain `unconsult`; the book writes its own.
- **Confusion**: `file:consult` reads lines or raw bytes.
  **Clarification**: It reads *Erlang terms*; for lines use `io:get_line`, for raw bytes use `file:read_file`.

# Source Reference

Chapter 16: Programming with Files, sections "Reading All the Terms in the File" (`file:consult`), "Reading the Terms in the File One at a Time" (the naive `consult` implementation), and "Writing a List of Terms to a File" (`unconsult`).

# Verification Notes

- Definition source: Direct adaptation of the `file:consult` description and the `consult`/`unconsult` code.
- Confidence rationale: HIGH — `file:consult` is explicitly described with examples and a sample implementation.
- Uncertainties: None.
- Cross-reference status: Slugs match planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
