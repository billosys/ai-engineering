---
# === CORE IDENTIFICATION ===
concept: Directory Operations
slug: directory-operations

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
section: "Directory and File Operations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "file:list_dir"
  - "file:make_dir"
  - "file:del_dir"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - file-module
extends: []
related:
  - file-info
  - filelib-module
  - filename-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I list the files in a directory?"
  - "How do I create or delete a directory?"
  - "What directory operations does the file module provide?"
---

# Quick Definition

Directory operations are the `file` functions for working with directories: `list_dir(Dir)` lists a directory's contents, `make_dir(Dir)` creates a directory, and `del_dir(Dir)` deletes one.

# Core Definition

Three functions in the `file` module are used for directory operations (Chapter 16, "Directory and File Operations"): `list_dir(Dir)` produces a list of the files in `Dir`; `make_dir(Dir)` creates a new directory; and `del_dir(Dir)` deletes a directory. `file:list_dir` returns `{ok, FileNames}`, but the result has no particular order and gives no indication of whether each entry is a file or a directory, nor its size — to discover that, you call `file:read_file_info` on each entry. The `file` module also provides `copy`, `delete`, and `rename` for individual files.

# Prerequisites

- **file module** — Directory operations are `file` functions.

# Key Properties

1. `file:list_dir(Dir)` lists the entries of a directory, returning `{ok, FileNames}`.
2. The listing has no particular order.
3. The listing does not indicate file vs. directory, size, or other metadata.
4. `file:make_dir(Dir)` creates a new directory.
5. `file:del_dir(Dir)` deletes a directory.
6. To classify entries, call `file:read_file_info` on each.

# Construction / Recognition

## To Perform Directory Operations:
1. List a directory's contents with `file:list_dir(Dir)`.
2. Create a directory with `file:make_dir(Dir)`.
3. Delete a directory with `file:del_dir(Dir)`.
4. To learn about each listed entry, call `file:read_file_info` per entry.

## To Recognize Them:
1. Look for `file:list_dir`, `file:make_dir`, `file:del_dir` calls.
2. Look for follow-up `file:read_file_info` calls classifying listed entries.

# Context & Application

- **Typical contexts**: Scanning, creating, and removing directories.
- **Common applications**: A recursive find utility uses `file:list_dir` plus `file:read_file_info` to walk directory trees.
- **Historical/stylistic notes**: Because `list_dir` gives only names, building a find utility requires combining it with `read_file_info`.

# Examples

**Example 1** (Chapter 16, "Directory and File Operations"): `file:list_dir(".")` returns `{ok,["id3_v1.erl~","update_binary_file.beam","benchmark_assoc.beam", ...]}` — an unordered list of names with no type or size information.

**Example 2** (Chapter 16, "A Find Utility"): The find utility uses `file:list_dir` and `file:read_file_info` together to make a general-purpose recursive "find" tool.

# Relationships

## Builds Upon
- **file module** — directory operations are `file` functions.

## Enables
- Directory traversal and find utilities.

## Related
- **File info** — `read_file_info` classifies entries returned by `list_dir`.
- **filelib module** — adds higher-level file-listing utilities.
- **filename module** — used to build full paths from directory and entry names.

## Contrasts With
- A set of `file` functions; no commonly confused counterpart in this chapter.

# Common Errors

- **Error**: Assuming `file:list_dir` returns entries in a meaningful order.
  **Correction**: The listing has no particular order; sort it yourself if order matters.
- **Error**: Treating a `list_dir` entry as a file without checking.
  **Correction**: Call `file:read_file_info` to determine whether an entry is a file or a directory.

# Common Confusions

- **Confusion**: `file:list_dir` tells you which entries are subdirectories.
  **Clarification**: It returns only names; use `file:read_file_info` to classify them.
- **Confusion**: `file:del_dir` deletes a directory and its contents.
  **Clarification**: `del_dir` deletes a directory; the chapter does not present it as recursive.

# Source Reference

Chapter 16: Programming with Files, section "Directory and File Operations" (`list_dir`, `make_dir`, `del_dir`, `copy`, `delete`); applied in "A Find Utility."

# Verification Notes

- Definition source: Direct adaptation of "Directory and File Operations."
- Confidence rationale: HIGH — the three directory functions are explicitly described with an example.
- Uncertainties: None.
- Cross-reference status: Slugs match planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
