---
# === CORE IDENTIFICATION ===
concept: Erlang Character Set
slug: erlang-character-set

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
section: "Character Set"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Latin-1 character set"
  - "ISO-8859-1 in Erlang"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - source-file-encoding
  - unicode-in-erlang-tokens
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What character set does Erlang use?"
  - "Can I use Latin-1 characters in Erlang identifiers?"
  - "Which character classes are defined for the upper Latin-1 range?"
---

# Quick Definition

Erlang token syntax allows the full ISO-8859-1 (Latin-1) character set, meaning unquoted atoms and variables can use Latin-1 letters, and all printable Latin-1 characters can appear in source code.

# Core Definition

As stated in the Erlang Reference Manual: "The syntax of Erlang tokens allows the use of the full ISO-8859-1 (Latin-1) character set." This manifests in two ways: "All the Latin-1 printable characters can be used and are shown without the escape backslash convention" and "Unquoted atoms and variables can use all Latin-1 letters." The upper half of the Latin-1 range (128-255) is classified into control characters, punctuation characters, uppercase letters (e.g., A with grave through thorn), and lowercase letters (e.g., sharp s through y with diaeresis) (Erlang Reference Manual, "Character Set and Source File Encoding", "Character Set").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Erlang tokens allow the full ISO-8859-1 (Latin-1) character set (codes 0-255)
2. Unquoted atoms and variables can use all Latin-1 letters
3. Upper Latin-1 uppercase letters: codes 192-214 (A grave to O diaeresis) and 216-222 (O stroke to Thorn)
4. Upper Latin-1 lowercase letters: codes 223-246 (sharp s to o diaeresis) and 248-255 (o stroke to y diaeresis)
5. Codes 215 (multiplication sign) and 247 (division sign) are classified as punctuation, not letters
6. Module names, application names, and node names are restricted to the Latin-1 range even when Unicode is available

# Construction / Recognition

## To Identify/Recognize:
1. Latin-1 letters in the range 192-255 (excluding 215 and 247) are valid in unquoted atoms and variables
2. Characters classified as "Uppercase letters" can start variables
3. Characters classified as "Lowercase letters" can start atoms

# Context & Application

Understanding the character set is essential for writing portable Erlang code. While the token syntax allows Latin-1 characters, practical usage typically stays within the ASCII range for identifiers. The restriction of module, application, and node names to Latin-1 is particularly important for distributed systems.

# Examples

**Example 1** (Character Set section): The character classification table shows that codes 300-326 (192-214 decimal, A grave to O diaeresis) are uppercase letters, while 337-366 (223-246 decimal, sharp s to o diaeresis) are lowercase letters.

**Example 2** (Character Set section): Code 327 (215 decimal, multiplication sign) is classified as a punctuation character, not a letter, despite being adjacent to letter ranges.

# Relationships

## Enables
- **source-file-encoding** -- The character set determines what can appear in source files
- **unicode-in-erlang-tokens** -- Unicode support extends beyond the base Latin-1 character set

## Related
- **reserved-words** -- Reserved words use only ASCII characters from within the character set

# Common Errors

- **Error**: Using a multiplication sign (x, code 215) or division sign (division, code 247) in an atom expecting them to be treated as letters
  **Correction**: These code points are classified as punctuation, not letters; they cannot appear in unquoted atoms

# Common Confusions

- **Confusion**: Assuming Unicode characters can be used in module names
  **Clarification**: Atoms used as module names, application names, and node names are restricted to the Latin-1 range

# Source Reference

"Character Set and Source File Encoding" chapter, section "Character Set", including the Character Classes table.

# Verification Notes

- Definition source: Direct from source text and character classification table
- Confidence rationale: HIGH -- explicit character class table and definitions in source
- Uncertainties: None
- Cross-reference status: Related slugs planned for extraction
