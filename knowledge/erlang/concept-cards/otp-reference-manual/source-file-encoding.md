---
# === CORE IDENTIFICATION ===
concept: Source File Encoding
slug: source-file-encoding

# === CLASSIFICATION ===
category: core-idioms
subcategory: character-encoding
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Character Set and Source File Encoding"
chapter_number: null
pdf_page: null
section: "Source File Encoding"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "encoding directive"
  - "coding comment"
  - "file encoding declaration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-character-set
extends: []
related:
  - unicode-in-erlang-tokens
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I set the encoding of an Erlang source file?"
  - "What is the default encoding for Erlang source files?"
  - "How does Erlang detect source file encoding?"
---

# Quick Definition

Erlang source file encoding is specified by a comment in the first two lines matching the pattern `coding\s*[:=]\s*([-a-zA-Z0-9])+`. The valid encodings are Latin-1 and UTF-8, with UTF-8 as the default since OTP 17.

# Core Definition

The Erlang Reference Manual states: "The Erlang source file `encoding` is selected by a comment in one of the first two lines of the source file. The first string that matches the regular expression `coding\s*[:=]\s*([-a-zA-Z0-9])+` selects the encoding. If the matching string is an invalid encoding, it is ignored. The valid encodings are `Latin-1` and `UTF-8`, where the case of the characters can be chosen freely." The default encoding changed from Latin-1 to UTF-8 in Erlang/OTP 17.0 (Erlang Reference Manual, "Character Set and Source File Encoding", "Source File Encoding").

# Prerequisites

- **erlang-character-set** -- Understanding which characters are valid in Erlang tokens requires knowing the character set and encoding

# Key Properties

1. Encoding is declared via a comment in the first two lines of the source file
2. The comment must match the regex `coding\s*[:=]\s*([-a-zA-Z0-9])+`
3. Valid encodings are `Latin-1` and `UTF-8` only
4. Encoding names are case-insensitive
5. Invalid encoding strings are silently ignored
6. Default encoding is UTF-8 (since Erlang/OTP 17.0)
7. Default was Latin-1 before Erlang/OTP 17.0

# Construction / Recognition

## To Construct/Create:
1. Add a comment in the first or second line of the source file
2. Include the word `coding` followed by `:` or `=` and the encoding name
3. Example for Latin-1: `%% -*- coding: latin-1 -*-`
4. Example for UTF-8: `%% coding: utf-8`

## To Identify/Recognize:
1. Look for a comment containing `coding` in the first two lines
2. If no valid encoding comment exists, the file uses UTF-8 (OTP 17+)

# Context & Application

Source file encoding is important when files contain non-ASCII characters in strings, atoms, or comments. Most modern Erlang projects use UTF-8 (the default). The Latin-1 option is primarily for legacy codebases written before OTP 17. The Emacs-style `-*- coding: ... -*-` comment format is recognized by both Erlang and many text editors.

# Examples

**Example 1** (Source File Encoding section): Selecting Latin-1 encoding with a descriptive comment:
```text
%% For this file we have chosen encoding = Latin-1
```

**Example 2** (Source File Encoding section): Selecting Latin-1 encoding with Emacs-style comment:
```erlang
%% -*- coding: latin-1 -*-
```

# Relationships

## Builds Upon
- **erlang-character-set** -- The encoding determines how the character set is represented in the source file

## Related
- **unicode-in-erlang-tokens** -- UTF-8 encoding enables full Unicode support in tokens that allow it

# Common Errors

- **Error**: Placing the encoding comment on line 3 or later
  **Correction**: The encoding comment must be in one of the first two lines of the source file

- **Error**: Using an unsupported encoding like `ASCII` or `ISO-8859-15`
  **Correction**: Only `Latin-1` and `UTF-8` are valid; invalid encodings are silently ignored and UTF-8 is used as default

# Common Confusions

- **Confusion**: Assuming the default encoding is Latin-1
  **Clarification**: The default changed from Latin-1 to UTF-8 in Erlang/OTP 17.0; modern Erlang defaults to UTF-8

- **Confusion**: Thinking encoding affects runtime string handling
  **Clarification**: The encoding directive only affects how the compiler reads the source file, not runtime string encoding

# Source Reference

"Character Set and Source File Encoding" chapter, section "Source File Encoding", including the Change note about the OTP 17 default change.

# Verification Notes

- Definition source: Direct from source text with regex and examples
- Confidence rationale: HIGH -- explicit definition with regex pattern and examples in source
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
