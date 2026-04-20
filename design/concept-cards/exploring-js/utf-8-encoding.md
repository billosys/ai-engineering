---
# === CORE IDENTIFICATION ===
concept: UTF-8 Encoding
slug: utf-8-encoding

# === CLASSIFICATION ===
category: primitive-types
subcategory: unicode
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Unicode -- a brief introduction (advanced)"
chapter_number: 21
pdf_page: null
section: "UTF-8"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "UTF-8"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - unicode-code-points
  - unicode-code-units
extends: []
related:
  - utf-16-encoding
contrasts_with:
  - utf-16-encoding

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

UTF-8 is a variable-length encoding using 8-bit code units (1-4 per code point), backward-compatible with ASCII, and the standard encoding for HTML and JavaScript source files.

# Core Definition

UTF-8 uses 8-bit code units with 1-4 code units per code point. The bit prefix of each code unit indicates its role (first in sequence, continuation, etc.). Code points 0x0000-0x007F map to single bytes identical to ASCII, providing backward compatibility. HTML and JavaScript files are almost always encoded as UTF-8 now (Ch. 21, Sections 21.1.2.3 and 21.2.3).

# Prerequisites

- **unicode-code-points** -- what UTF-8 encodes
- **unicode-code-units** -- the building blocks

# Key Properties

1. 8-bit code units (ES1+)
2. 1 code unit for ASCII (0x0000-0x007F)
3. 2 code units for 0x0080-0x07FF
4. 3 code units for 0x0800-0xFFFF
5. 4 code units for 0x10000-0x1FFFFF
6. Backward compatible with ASCII
7. Standard encoding for files, HTML

# Construction / Recognition

| Character | Code Point | UTF-8 Code Units |
|-----------|-----------|------------------|
| A | 0x0041 | 01000001 (1 byte) |
| π | 0x03C0 | 11001111, 10000000 (2 bytes) |
| 🙂 | 0x1F642 | 11110000, 10011111, 10011001, 10000010 (4 bytes) |

# Context & Application

UTF-8 is used for JavaScript source code files and HTML documents. JavaScript strings internally use UTF-16, but file I/O typically involves UTF-8.

# Examples

From the source text:

HTML files declare UTF-8:
```html
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
```

# Relationships

## Builds Upon
- **unicode-code-points** — encodes code points
- **unicode-code-units** — uses 8-bit code units

## Enables
- File storage and network transmission of Unicode text

## Related
- **utf-16-encoding** — alternative encoding used by JS strings

## Contrasts With
- **utf-16-encoding** — UTF-16 uses 16-bit units; UTF-8 uses 8-bit units

# Common Errors

- **Error**: Assuming JavaScript strings are UTF-8
  **Correction**: JavaScript strings are UTF-16 internally. UTF-8 is used for source files and I/O.

# Common Confusions

- **Confusion**: Thinking UTF-8 and ASCII are the same
  **Clarification**: UTF-8 is backward-compatible with ASCII for the first 128 code points, but extends to support all of Unicode.

# Source Reference

Chapter 21: Unicode, Section 21.1.2.3 and 21.2.3, lines 193-394.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete encoding table provided
- Cross-reference status: verified
