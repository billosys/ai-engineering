---
# === CORE IDENTIFICATION ===
concept: File Info
slug: file-info

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
section: "Finding Information About a File"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "file:read_file_info"
  - "#file_info"
  - "file_info record"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - file-module
  - record
extends: []
related:
  - directory-operations
  - filelib-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I find information about a file?"
  - "How do I tell whether a directory entry is a file or a directory?"
  - "How do I get the size of a file?"
---

# Quick Definition

File info is the metadata about a file or directory returned by `file:read_file_info(F)` as a `#file_info` record — including its type, size, and timestamps.

# Core Definition

To find out about a file `F`, you call `file:read_file_info(F)`; this returns `{ok, Info}` if `F` is a valid file or directory name, where `Info` is a record of type `#file_info` (Chapter 16, "Finding Information About a File"). The `#file_info` record holds metadata such as the entry's type (regular file, directory, etc.), size, and modification/access times. Because `file:list_dir` returns only names with no type or size information, `read_file_info` is how you classify and measure directory entries. The book also notes that if you only want a file's size, it is more convenient to call `filelib:file_size` than to call `file:read_file_info` and unpack the `#file_info` record yourself.

# Prerequisites

- **file module** — `read_file_info` is a `file` function.
- **Record** — The result is a `#file_info` record; you must understand records to use it.

# Key Properties

1. `file:read_file_info(F)` returns `{ok, Info}` for a valid file or directory.
2. `Info` is a `#file_info` record.
3. The record carries the entry's type, size, and timestamps, among other fields.
4. It is the way to classify entries returned by `file:list_dir`.
5. For size alone, `filelib:file_size` is more convenient than unpacking `#file_info`.

# Construction / Recognition

## To Get File Info:
1. Call `file:read_file_info(F)`.
2. Match `{ok, Info}` where `Info` is a `#file_info` record.
3. Pattern-match or access record fields for type, size, times.
4. For size only, prefer `filelib:file_size(F)`.

## To Recognize It:
1. Look for `file:read_file_info` calls and `#file_info{}` record patterns.
2. Look for it paired with `file:list_dir` to classify entries.

# Context & Application

- **Typical contexts**: Inspecting file metadata; distinguishing files from directories during traversal.
- **Common applications**: The find utility uses `read_file_info` to walk directory trees; `id3_v1` uses `filelib:file_size` to locate the trailing ID3 tag.
- **Historical/stylistic notes**: `filelib:file_size` is the convenience shortcut for the most common metadata query.

# Examples

**Example 1** (Chapter 16, "Finding Information About a File"): `file:read_file_info(F)` returns `{ok, Info}` where `Info` is a `#file_info` record describing the file or directory.

**Example 2** (Chapter 16, "Reading MP3 Metadata"): `id3_v1` calls `filelib:file_size(File)` to get the file size, then `file:pread(S, Size-128, 128)` to read the trailing ID3v1 tag.

# Relationships

## Builds Upon
- **file module** — `read_file_info` is a `file` function.
- **Record** — the result is a `#file_info` record.

## Enables
- Classifying and measuring directory entries; directory traversal.

## Related
- **Directory operations** — `read_file_info` complements `list_dir` by adding metadata.
- **filelib module** — provides `file_size` as a convenience over `read_file_info`.

## Contrasts With
- A metadata-query function; no commonly confused counterpart in this chapter.

# Common Errors

- **Error**: Unpacking the whole `#file_info` record just to get a file's size.
  **Correction**: Use `filelib:file_size(F)` for the size alone.
- **Error**: Calling `file:read_file_info` on a nonexistent path and not handling the error.
  **Correction**: Match for `{error, Reason}` as well as `{ok, Info}`.

# Common Confusions

- **Confusion**: `file:list_dir` already tells you each entry's type and size.
  **Clarification**: `list_dir` returns only names; `read_file_info` supplies the metadata.
- **Confusion**: `read_file_info` returns a tuple of fields.
  **Clarification**: It returns a `#file_info` *record*; access it as a record.

# Source Reference

Chapter 16: Programming with Files, section "Finding Information About a File" (`file:read_file_info` and the `#file_info` record); `filelib:file_size` note in the same area and used in "Reading MP3 Metadata."

# Verification Notes

- Definition source: Direct adaptation of "Finding Information About a File."
- Confidence rationale: HIGH — `read_file_info` and the `#file_info` record are explicitly described.
- Uncertainties: The full `#file_info` field list is shown only partially in the source excerpt; the card describes the fields the chapter names.
- Cross-reference status: Slugs match canonical `record` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
