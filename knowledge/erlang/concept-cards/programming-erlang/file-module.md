---
# === CORE IDENTIFICATION ===
concept: file Module
slug: file-module

# === CLASSIFICATION ===
category: tooling
subcategory: file-io
tier: foundational

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
  - "file"
  - "file operations"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - filename-module
  - filelib-module
  - io-module
  - file-consult
  - file-modes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Which modules manipulate files in Erlang?"
  - "What does the file module do?"
  - "How do I open, read, write, and close a file?"
---

# Quick Definition

`file` is the core Erlang module for file manipulation — opening, closing, reading, and writing files, listing directories, and related operations.

# Core Definition

The functions for file manipulation are organized into four modules: `file`, `filename`, `filelib`, and `io` (Chapter 16, "Modules for Manipulating Files"). The `file` module "has routines for opening, closing, reading, and writing files; listing directories; and so on." The chapter summarizes the more frequently used `file` functions in Table 7, "Summary of file operations" — including `open`, `close`, `read`, `write`, `read_file`, `write_file`, `consult`, `pread`, `pwrite`, `position`, `list_dir`, `make_dir`, `del_dir`, `copy`, `delete`, `rename`, `read_file_info`, `write_file_info`, and `format_error`. For full details the book directs readers to the manual page for `file`.

# Prerequisites

This is a foundational module concept with no prerequisites within this source.

# Key Properties

1. `file` is one of four file-manipulation modules (`file`, `filename`, `filelib`, `io`).
2. It provides opening, closing, reading, and writing of files.
3. It provides directory operations (`list_dir`, `make_dir`, `del_dir`).
4. It provides whole-file operations (`read_file`, `write_file`) and random-access ones (`pread`, `pwrite`).
5. Most `file` functions return `{ok, ...}` on success or `{error, Reason}` on failure.

# Construction / Recognition

## To Use the file Module:
1. For an open-read-close workflow: `file:open/2`, then reads, then `file:close/1`.
2. For whole-file work: `file:read_file/1` and `file:write_file/2`.
3. For random access: open in `raw` mode, then `file:pread/3` / `file:pwrite/3`.
4. For directories: `file:list_dir/1`, `file:make_dir/1`, `file:del_dir/1`.

## To Recognize It:
1. Look for `file:` prefixed calls throughout file-handling code.
2. Look for `{ok, ...}` / `{error, Reason}` result matching.

# Context & Application

- **Typical contexts**: All Erlang programs that touch the filesystem.
- **Common applications**: Reading config files with `file:consult`; bulk I/O with `read_file`/`write_file`; the `id3_v1` and `scavenge_urls` examples.
- **Historical/stylistic notes**: The book focuses on the small fraction of `file` functions used day-to-day and points to the manual for the rest.

# Examples

**Example 1** (Chapter 16, "Reading the Terms in the File One at a Time"): `{ok, S} = file:open("data1.dat", read)` opens a file for reading, and `file:close(S)` closes it.

**Example 2** (Chapter 16, Table 7): The chapter's Table 7 summarizes `file` operations such as `consult` ("Read Erlang terms from a file"), `read_file` ("Read an entire file"), and `write_file` ("Write an entire file").

# Relationships

## Builds Upon
- A foundational module; builds on no other concept in this source.

## Enables
- All concrete file reading and writing techniques in this chapter.

## Related
- **filename module** — platform-independent filename manipulation.
- **filelib module** — file-listing and type-checking utilities.
- **io module** — routines that operate on opened files.
- **file:consult** — a `file` function for reading Erlang terms.
- **file modes** — the modes passed to `file:open`.

## Contrasts With
- A foundational module; no commonly confused counterpart in this chapter.

# Common Errors

- **Error**: Ignoring the `{error, Reason}` return from `file` functions.
  **Correction**: Match on `{ok, ...}` vs `{error, Reason}` for every call.
- **Error**: Forgetting to `file:close/1` a file opened with `file:open/2`.
  **Correction**: Always close an explicitly opened file device when done.

# Common Confusions

- **Confusion**: All file operations live in `file`.
  **Clarification**: File work is split across four modules — `file`, `filename`, `filelib`, and `io`.
- **Confusion**: `file` operations always raise exceptions on failure.
  **Clarification**: They generally return `{error, Reason}` tuples rather than raising.

# Source Reference

Chapter 16: Programming with Files, section "Modules for Manipulating Files" (the description of `file` and Table 7, "Summary of file operations").

# Verification Notes

- Definition source: Direct adaptation of "Modules for Manipulating Files" and Table 7.
- Confidence rationale: HIGH — the `file` module is explicitly described and its functions tabulated.
- Uncertainties: None.
- Cross-reference status: Slugs match planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
