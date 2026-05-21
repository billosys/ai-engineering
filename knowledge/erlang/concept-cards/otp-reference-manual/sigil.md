---
# === CORE IDENTIFICATION ===
concept: Sigil
slug: sigil

# === CLASSIFICATION ===
category: data-types
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Data Types"
chapter_number: null
pdf_page: null
section: "Sigil"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string
  - binary
extends: []
related:
  - triple-quoted-string
  - escape-sequence
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
---

# Quick Definition
A sigil is a prefix to a string literal (starting with `~`) that indicates how to interpret the string content. Sigils provide compact notation for creating UTF-8 binaries and verbatim strings.

# Core Definition
The Erlang Reference Manual states: "A _sigil_ is a prefix to a string literal. It is not a data type in Erlang, but a shorthand notation that indicates how to interpret the string literal." Sigils start with the tilde character (`~`) followed by a name defining the sigil type. The sigil content follows, enclosed in content delimiters. Allowed delimiters include paired brackets (`() [] {} <>`), or symmetric characters (``/ | ' " ` #``), or triple-quote delimiters. Sigils were introduced in Erlang/OTP 27 (Data Types, "Sigil" section).

# Prerequisites
- **string** -- `~s` and `~S` sigils produce string (list) values
- **binary** -- `~b` and `~B` sigils produce binary values

# Key Properties
1. Not a data type -- a notation that controls string interpretation
2. Starts with `~` followed by a type name
3. Five sigil types:
   - `~` (vanilla/default): UTF-8 binary, escaping depends on delimiter type
   - `~b`: UTF-8 binary with escape sequences
   - `~B`: UTF-8 binary, verbatim (no escaping)
   - `~s`: string (list of code points) with escape sequences
   - `~S`: string (list of code points), verbatim
4. Content delimiters: `() [] {} <>` or `/ | ' " \` #` or triple-quote `"""`
5. Verbatim sigils (`~B`, `~S`) have no escape character
6. Adjacent sigil expressions cannot be concatenated with string concatenation syntax
7. `~s"a" ++ "b"` works because `++` is an operator, but `~s"a" "b"` is a syntax error

# Construction / Recognition
## To Construct/Create:
1. Binary from string: `~b"hello"` or `~"hello"` or `~b[hello]`
2. Verbatim binary: `~B<"\µA">` (backslash is literal, not escape)
3. String sigil: `~s"hello"` (same as `"hello"`)
4. Verbatim string: `~S("\µA")` (no escape processing)
5. With triple-quote delimiters for multi-line:
```text
~b"""
    content
    """
```

## To Identify/Recognize:
1. Starts with `~` followed by optional sigil type name
2. Immediately followed by content in delimiters
3. The result type depends on the sigil name (binary vs. string)

# Context & Application
Sigils are primarily useful for:
- Creating UTF-8 binary strings without the verbose `<<"...">>` syntax
- Writing regular expressions and other content where backslashes are common (using verbatim sigils)
- Choosing delimiters that avoid escaping issues with the content

# Examples
**Example 1** (Data Types, "Sigil" section): Equivalent expressions producing UTF-8 binary `<<"\"\\µA\""/utf8>>`:
```text
~b'"\\µA"' = ~B<"\µA"> = ~"\"\\µA\"" = ~/"\\µA"/
```

**Example 2** (Data Types, "Sigil" section): Equivalent expressions producing string `[$",$\\,$µ,$A,$"]`:
```text
~s"\"\\µA\"" = ~s["\\µA"] = ~S("\µA") = "\"\\µA\""
```

**Example 3** (Data Types, "Sigil" section): Concatenation with `++`:
`~s"a" ++ "b"` evaluates to `"ab"` since both operands are strings.

# Relationships
## Builds Upon
- **string** -- `~s`/`~S` produce strings
- **binary** -- `~b`/`~B`/`~` produce binaries

## Enables
No direct dependents within this extraction scope.

## Related
- **triple-quoted-string** -- Triple-quote delimiters can be used with sigils
- **escape-sequence** -- Uppercase sigils disable escape processing; lowercase sigils use normal escape rules

## Contrasts With
No direct contrasts within this source.

# Common Errors
- **Error**: Trying to concatenate sigils with adjacent string syntax: `~s"a" "b"`
  **Correction**: This is a syntax error. Use `~s"a" ++ "b"` with the `++` operator instead.

# Common Confusions
- **Confusion**: Confusing `~b` (escaped binary) with `~B` (verbatim binary)
  **Clarification**: Lowercase `~b` processes escape sequences (like `\n`); uppercase `~B` treats content verbatim (backslash is literal).

- **Confusion**: Thinking the default `~` sigil always behaves the same regardless of delimiter
  **Clarification**: With triple-quote delimiters, `~` behaves like `~B` (verbatim); with other delimiters, it behaves like `~b` (escaped).

# Source Reference
Data Types chapter, "Sigil" section.

# Verification Notes
- Definition source: Direct quote from source ("a prefix to a string literal")
- Confidence rationale: High -- explicit definition with detailed examples
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
