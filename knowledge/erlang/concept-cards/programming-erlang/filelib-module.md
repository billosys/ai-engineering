---
# === CORE IDENTIFICATION ===
concept: filelib Module
slug: filelib-module

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
  - "filelib"
  - "filelib:file_size"
  - "filelib:ensure_dir"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - file-module
extends:
  - file-module
related:
  - filename-module
  - file-info
  - directory-operations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the filelib module do?"
  - "How do I get a file's size conveniently?"
  - "How do I ensure all parent directories of a path exist?"
---

# Quick Definition

`filelib` is an extension to the `file` module containing higher-level utilities for listing files, checking file types, getting file sizes, and ensuring directories exist.

# Core Definition

The `filelib` module is an extension to `file`, containing a number of utilities for listing files, checking file types, and so on; most of these are written using the functions in `file` (Chapter 16, "Modules for Manipulating Files"). It "has a small number of routines that can save us some work" (Chapter 16, "Bits and Pieces"). Two routines the chapter highlights: `filelib:file_size(File)`, a convenient way to get a file's size without calling `file:read_file_info` and unpacking the `#file_info` record; and `filelib:ensure_dir(Name)`, which ensures that all parent directories for the given file or directory name `Name` exist, trying to create them if necessary.

# Prerequisites

- **file module** — `filelib` is an extension to `file`; most of its routines are built on `file` functions.

# Key Properties

1. `filelib` is an extension to the `file` module.
2. Most of its routines are implemented using `file` functions.
3. It provides higher-level utilities for listing files and checking file types.
4. `filelib:file_size(File)` returns a file's size conveniently.
5. `filelib:ensure_dir(Name)` ensures all parent directories of `Name` exist, creating them if needed.

# Construction / Recognition

## To Use the filelib Module:
1. For a file's size, call `filelib:file_size(File)` instead of unpacking `#file_info`.
2. To guarantee parent directories exist before writing, call `filelib:ensure_dir(Name)`.
3. Use `filelib` listing/type-checking utilities for higher-level file queries.

## To Recognize It:
1. Look for `filelib:` prefixed calls, especially `file_size` and `ensure_dir`.
2. Look for it used as a convenience layer above raw `file` calls.

# Context & Application

- **Typical contexts**: Convenient file queries and directory preparation.
- **Common applications**: `id3_v1` uses `filelib:file_size` to find the trailing ID3 tag; `filelib:ensure_dir` guarantees a write path's directories exist.
- **Historical/stylistic notes**: The chapter presents `filelib` as a small set of labor-saving routines layered on `file`.

# Examples

**Example 1** (Chapter 16, "Reading MP3 Metadata"): `Size = filelib:file_size(File)` gets the MP3 file's size so the ID3v1 tag can be read from `Size-128`.

**Example 2** (Chapter 16, "Bits and Pieces"): `filelib:ensure_dir(Name)` "ensures that all parent directories for the given file or directory name `Name` exist, trying to create them if necessary."

# Relationships

## Builds Upon
- **file module** — `filelib` is an extension layered on `file`.

## Enables
- Convenient file-size queries and directory preparation.

## Related
- **filename module** — both operate on filenames; `filename` manipulates name strings, `filelib` queries the filesystem.
- **File info** — `filelib:file_size` is a shortcut over `file:read_file_info`.
- **Directory operations** — `filelib:ensure_dir` complements `file:make_dir`.

## Contrasts With
- A convenience extension; no commonly confused counterpart in this chapter.

# Common Errors

- **Error**: Calling `file:read_file_info` and unpacking `#file_info` just to get a size.
  **Correction**: Use `filelib:file_size(File)`.
- **Error**: Writing a file into a path whose parent directories may not exist.
  **Correction**: Call `filelib:ensure_dir(Name)` first to create them.

# Common Confusions

- **Confusion**: `filelib` replaces `file`.
  **Clarification**: `filelib` is an *extension* — most of its routines are implemented using `file` functions.
- **Confusion**: `filelib:ensure_dir` creates the named directory itself.
  **Clarification**: It ensures the *parent* directories of `Name` exist.

# Source Reference

Chapter 16: Programming with Files, section "Modules for Manipulating Files" (the `filelib` description) and "Bits and Pieces" (the `filelib` overview, `ensure_dir`); `filelib:file_size` used in "Reading MP3 Metadata."

# Verification Notes

- Definition source: Direct adaptation of the `filelib` descriptions and the `file_size`/`ensure_dir` routines.
- Confidence rationale: HIGH — the module and its highlighted routines are explicitly described, with `file_size` shown in code.
- Uncertainties: The full `filelib` API is deferred to the manual; the card covers the routines the chapter names.
- Cross-reference status: Slugs match planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
