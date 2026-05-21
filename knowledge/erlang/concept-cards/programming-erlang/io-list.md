---
# === CORE IDENTIFICATION ===
concept: I/O List
slug: io-list

# === CLASSIFICATION ===
category: data-types
subcategory: binaries-iolists
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming with Files"
chapter_number: 16
pdf_page: null
section: "Writing an Entire File in One Operation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "IO list"
  - "iolist"
  - "deep list"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binary
extends: []
related:
  - whole-file-io
  - port
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an I/O list?"
  - "How do I efficiently build output without flattening lists?"
  - "What can the elements of an I/O list be?"
---

# Quick Definition

An I/O list is a list whose elements are I/O lists, binaries, or integers from 0 to 255; when output, it is automatically flattened so that only the embedded bytes — not the list brackets — are written.

# Core Definition

An *I/O list* is a list whose elements are I/O lists, binaries, or integers from 0 to 255 (Chapter 16, "Writing an Entire File in One Operation"). When an I/O list is output, it is automatically "flattened," which means that all the list brackets are removed and only the embedded characters/bytes are written. This lets a program build a *deep* (nested) list of characters and "just throw it at the output routines" without the inefficiency of flattening it first. `file:write_file(File, IO)` accepts an I/O list as its `IO` argument, and the I/O system performs the flattening on output. The book stresses that not flattening the list yourself is deliberate and efficient.

# Prerequisites

- **Binary** — Binaries are valid elements of an I/O list, so understanding binaries comes first.

# Key Properties

1. An I/O list is a list of I/O lists, binaries, or integers in the range 0–255.
2. It may be arbitrarily nested (a *deep list*).
3. On output it is automatically flattened — list brackets are removed.
4. Building a deep list avoids the cost of pre-flattening.
5. `file:write_file` and port commands accept I/O lists directly.

# Construction / Recognition

## To Build an I/O List:
1. Freely nest lists of strings, binaries, and byte integers — no need to flatten.
2. Pass the resulting deep list to an output routine such as `file:write_file/2`.

## To Recognize It:
1. Look for output-building code that returns nested lists without flattening.
2. Look for functions like `urls2html` that compose results from sublists.

# Context & Application

- **Typical contexts**: Efficiently assembling output for files, ports, and sockets.
- **Common applications**: `scavenge_urls` builds a deep list of HTML fragments and writes it with `file:write_file`.
- **Historical/stylistic notes**: The book explicitly notes the code "make[s] no attempt to flatten the list (which would be rather inefficient)."

# Examples

**Example 1** (Chapter 16, "Writing an Entire File in One Operation"): The definition — "An I/O list is a list whose elements are I/O lists, binaries, or integers from 0 to 255. When an I/O list is output, it is automatically 'flattened.'"

**Example 2** (Chapter 16, "Listing URLs from a File"): `make_list(L) -> ["<ul>\n", map(fun(I) -> ["<li>", I, "</li>\n"] end, L), "</ul>\n"].` returns a deep I/O list of HTML; `file:write_file` flattens it on output.

# Relationships

## Builds Upon
- **Binary** — binaries are permitted I/O list elements.

## Enables
- **Whole-file I/O** — `file:write_file` accepts an I/O list.

## Related
- **Port** — port `{command, Data}` messages also take I/O lists.

## Contrasts With
- A data-shape concept; no commonly confused counterpart in this chapter.

# Common Errors

- **Error**: Calling `lists:flatten` on an I/O list before writing it.
  **Correction**: Pass the deep list directly; the I/O system flattens it efficiently.
- **Error**: Including integers outside 0–255 in an I/O list.
  **Correction**: I/O list integers must be bytes (0–255); use binaries for other data.

# Common Confusions

- **Confusion**: An I/O list must be a flat list of bytes.
  **Clarification**: It can be deeply nested and contain binaries; flattening happens automatically on output.
- **Confusion**: I/O lists are only for files.
  **Clarification**: They are accepted by file, port, and socket output routines alike.

# Source Reference

Chapter 16: Programming with Files, section "Writing an Entire File in One Operation" (the I/O list definition) and "Listing URLs from a File" (the deep-list `urls2html`/`make_list` example).

# Verification Notes

- Definition source: Direct adaptation of the I/O list definition and the `scavenge_urls` example.
- Confidence rationale: HIGH — the I/O list is explicitly defined with its flattening behavior and a worked example.
- Uncertainties: None.
- Cross-reference status: Slugs match canonical `binary` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
