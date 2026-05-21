---
# === CORE IDENTIFICATION ===
concept: filename Module
slug: filename-module

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
  - "filename"
  - "filename:join"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - file-module
  - filelib-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the filename module do?"
  - "How do I manipulate filenames in a platform-independent way?"
  - "How do I build a path from its component parts?"
---

# Quick Definition

`filename` is the Erlang module of routines that manipulate filenames in a platform-independent manner, so the same code runs unchanged on different operating systems.

# Core Definition

The `filename` module has routines that manipulate filenames in a platform-independent manner, so you can run the same code on a number of different operating systems (Chapter 16, "Modules for Manipulating Files"). It has useful routines for "ripping apart full filenames in directories and finding the file extensions, and so on, as well as for rebuilding filenames from the component parts" — all done in a platform-independent way (Chapter 16, "Bits and Pieces"). For example, `filename:join([Dir, File])` builds a full path from its component parts.

# Prerequisites

This is a foundational module concept with no prerequisites within this source.

# Key Properties

1. `filename` is one of the four file-manipulation modules.
2. Its routines manipulate filenames platform-independently.
3. It can split full filenames into directories, base names, and extensions.
4. It can rebuild filenames from component parts (e.g. `filename:join/1`).
5. Using it lets the same code run unchanged across operating systems.

# Construction / Recognition

## To Use the filename Module:
1. To build a path from parts, call `filename:join([Dir, File])`.
2. To extract components (directory, base name, extension), use the `filename` splitting routines.
3. Prefer `filename` routines over hand-built path strings for portability.

## To Recognize It:
1. Look for `filename:` prefixed calls, especially `filename:join`.
2. Look for path handling that avoids hard-coded separators.

# Context & Application

- **Typical contexts**: Portable filename and path manipulation.
- **Common applications**: The find utility builds full paths with `filename:join([Dir, File])`.
- **Historical/stylistic notes**: The chapter introduces `filename` at an overview level under "Bits and Pieces," pointing to the manual for the full API.

# Examples

**Example 1** (Chapter 16, "A Find Utility"): The find utility constructs each entry's full path with `FullName = filename:join([Dir, File])`.

**Example 2** (Chapter 16, "Bits and Pieces"): The book describes `filename` as having routines "for ripping apart full filenames in directories and finding the file extensions ... as well as for rebuilding filenames from the component parts."

# Relationships

## Builds Upon
- A foundational module; builds on no other concept in this source.

## Enables
- Portable path construction and decomposition.

## Related
- **file module** — `filename` complements `file` by handling the name strings `file` operates on.
- **filelib module** — also operates on filenames at a higher level.

## Contrasts With
- A foundational module; no commonly confused counterpart in this chapter.

# Common Errors

- **Error**: Concatenating directory and file names with hard-coded separators.
  **Correction**: Use `filename:join/1` so the code is portable across operating systems.

# Common Confusions

- **Confusion**: `filename` opens or reads files.
  **Clarification**: `filename` only manipulates name strings; opening and reading are done by `file`.
- **Confusion**: Path handling is the same on every OS, so a plain module would do.
  **Clarification**: Separators and conventions differ; `filename` exists precisely to abstract those differences.

# Source Reference

Chapter 16: Programming with Files, section "Modules for Manipulating Files" (the `filename` description) and "Bits and Pieces" (the `filename` overview); `filename:join` used in "A Find Utility."

# Verification Notes

- Definition source: Direct adaptation of the `filename` descriptions in "Modules for Manipulating Files" and "Bits and Pieces."
- Confidence rationale: HIGH — the module's purpose is explicitly described, with `filename:join` shown in code.
- Uncertainties: The full API is deferred to the manual; the card stays at the source's overview level.
- Cross-reference status: Slugs match planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
