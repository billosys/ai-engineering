---
# === CORE IDENTIFICATION ===
concept: Unicode in Erlang Tokens
slug: unicode-in-erlang-tokens

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
  - "Unicode support in Erlang"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-character-set
extends:
  - erlang-character-set
related:
  - source-file-encoding
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Where can I use Unicode characters in Erlang source code?"
  - "Can I use Unicode in Erlang atom names?"
  - "What are the limitations on Unicode in Erlang identifiers?"
---

# Quick Definition

Certain Erlang tokens allow Unicode characters beyond the Latin-1 range, including string literals, character literals, comments, quoted atoms, and function names. Module names remain restricted to Latin-1.

# Core Definition

The Erlang Reference Manual specifies that "the following tokens are allowed to also use Unicode characters outside of the Latin-1 range: String literals (e.g., `"square-root-pi"`), Character literals (e.g., `$summation`), Comments in code, Quoted atoms (e.g., `'mu-s'`), Function names (e.g., `'s_to_mu-s'(S) -> S * 1_000_000.`)." However, "Atoms used as module names, application names, and node names are restricted to the Latin-1 range." Unicode in string/character literals and comments was introduced in Erlang/OTP R16B; Unicode in atom and function names was introduced in Erlang/OTP 20 (Erlang Reference Manual, "Character Set and Source File Encoding", "Character Set").

# Prerequisites

- **erlang-character-set** -- Understanding the base Latin-1 character set is needed to understand what Unicode extends

# Key Properties

1. String literals can contain Unicode: `"square-root-pi"`
2. Character literals can contain Unicode: `$summation`
3. Comments can contain Unicode characters
4. Quoted atoms can contain Unicode: `'mu-s'`
5. Function names (as quoted atoms) can contain Unicode: `'s_to_mu-s'(S) -> S * 1_000_000.`
6. Module names, application names, and node names remain Latin-1 only
7. Unquoted atoms and variables cannot use Unicode outside Latin-1

# Construction / Recognition

## To Construct/Create:
1. Use Unicode characters freely in string literals enclosed in double quotes
2. Use Unicode characters in character literals with the `$` prefix
3. Quote atoms containing Unicode characters with single quotes
4. Quote function names containing Unicode characters with single quotes

## To Identify/Recognize:
1. Unicode characters appear in quoted contexts (strings, quoted atoms)
2. Module-name atoms never contain characters outside Latin-1

# Context & Application

Unicode support allows Erlang programs to handle international text in string data and to use descriptive names with special characters in quoted atoms. The restriction on module names to Latin-1 ensures compatibility with the file system and distributed node communication. The phased introduction (R16B for strings, OTP 20 for atoms) reflects the gradual expansion of Unicode support.

# Examples

**Example 1** (Character Set section): String literal with Unicode: `"square-root-pi"`

**Example 2** (Character Set section): Character literal with Unicode: `$summation`

**Example 3** (Character Set section): Quoted atom with Unicode: `'mu-s'`

**Example 4** (Character Set section): Function name with Unicode: `'s_to_mu-s'(S) -> S * 1_000_000.`

# Relationships

## Builds Upon
- **erlang-character-set** -- Unicode extends the base Latin-1 character support

## Related
- **source-file-encoding** -- The source file encoding (Latin-1 or UTF-8) affects how Unicode characters are stored

# Common Errors

- **Error**: Using Unicode characters in an unquoted atom
  **Correction**: Atoms with Unicode characters outside Latin-1 must be quoted with single quotes

- **Error**: Using Unicode characters in a module name atom
  **Correction**: Module names are restricted to Latin-1; use only Latin-1 characters for module names

# Common Confusions

- **Confusion**: Assuming all atoms support Unicode
  **Clarification**: Only _quoted_ atoms support Unicode outside Latin-1; unquoted atoms are limited to Latin-1 letters, and module-name atoms are further restricted to Latin-1 only

# Source Reference

"Character Set and Source File Encoding" chapter, section "Character Set", paragraphs on Unicode token support and the Change note about version history.

# Verification Notes

- Definition source: Direct from source text with specific examples
- Confidence rationale: HIGH -- explicit enumeration of allowed token types with examples
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
