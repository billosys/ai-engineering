---
# === CORE IDENTIFICATION ===
concept: String
slug: string

# === CLASSIFICATION ===
category: data-types
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Data Types"
chapter_number: null
pdf_page: null
section: "String"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - double-quoted string

# === TYPED RELATIONSHIPS ===
prerequisites:
  - list
  - integer
extends:
  - list
related:
  - erlang-term
  - binary
  - triple-quoted-string
  - sigil
  - escape-sequences
  - numeric-notation
contrasts_with:
  - atom
  - binary

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes atoms from strings in Erlang?"
  - "What is an Erlang term?"
---

# Quick Definition
Strings in Erlang are enclosed in double quotes but are not a distinct data type. A string `"hello"` is shorthand for the list `[$h,$e,$l,$l,$o]`, which is `[104,101,108,108,111]`.

# Core Definition
The Erlang Reference Manual states: "Strings are enclosed in double quotes (\"), but are not a data type in Erlang. Instead, a string `\"hello\"` is shorthand for the list `[$h,$e,$l,$l,$o]`, that is, `[104,101,108,108,111]`." Two adjacent string literals are concatenated into one during compilation. Starting from Erlang/OTP 27, adjacent string literals must be separated by white space to avoid confusion with triple-quoted strings (Data Types, "String" section).

# Prerequisites
- **list** -- Strings are lists of integers
- **integer** -- Each character in a string is its integer code point

# Key Properties
1. Not a distinct data type -- syntactic sugar for a list of integers
2. Enclosed in double quotes: `"hello"`
3. Each character is its Unicode code point (integer)
4. `"hello"` = `[$h,$e,$l,$l,$o]` = `[104,101,108,108,111]`
5. Adjacent string literals are concatenated at compile time: `"string" "42"` = `"string42"`
6. As of OTP 27, adjacent strings must be separated by whitespace
7. Supports escape sequences within the string content

# Construction / Recognition
## To Construct/Create:
1. Use double-quote syntax: `"hello"`
2. Concatenate adjacent strings: `"hello" " " "world"` (must have whitespace between as of OTP 27)
3. Convert from atom: `atom_to_list(hello)` yields `"hello"`
4. Convert from binary: `binary_to_list(<<"hello">>)`

## To Identify/Recognize:
1. Strings are lists, so `is_list/1` returns `true`
2. Each element is an integer code point
3. There is no `is_string/1` BIF -- strings are indistinguishable from lists of integers at the type level

# Context & Application
Erlang's representation of strings as lists of integers is historically significant but can be confusing for newcomers. For performance-critical string operations, binary strings (`<<"hello">>`) are often preferred because they use less memory and support efficient operations. The sigil `~b"..."` provides a compact way to create UTF-8 binary strings. List-based strings remain important for compatibility and for use with `io_lib`, `io:format`, and similar functions.

# Examples
**Example 1** (Data Types, "String" section): Adjacent string concatenation:
```text
"string" "42"
```
is equivalent to
```text
"string42"
```

**Example 2** (Data Types, "Type Conversions" section):
```erlang
1> atom_to_list(hello).
"hello"
2> list_to_atom("hello").
hello
```

# Relationships
## Builds Upon
- **list** -- Strings are lists of integer code points
- **integer** -- Each character is an integer

## Enables
- **triple-quoted-string** -- Triple-quoted strings extend string syntax for multi-line and verbatim content
- **sigil** -- Sigils provide alternative string notations

## Related
- **erlang-term** -- Strings (as lists) are terms
- **escape-sequence** -- Strings support escape sequences
- **numeric-notation** -- `$char` notation reveals the integer nature of characters

## Contrasts With
- **atom** -- Atoms are symbolic constants; strings are lists of integers. Atom comparison is identity-based; string comparison is value-based.
- **binary** -- Binary strings (`<<"hello">>`) are byte sequences; list strings (`"hello"`) are lists of integers. Binaries are more memory-efficient for large text.

# Common Errors
- **Error**: Expecting `"hello" =:= <<"hello">>` to be true
  **Correction**: `"hello"` is a list `[104,101,108,108,111]`; `<<"hello">>` is a binary. They are different types.

# Common Confusions
- **Confusion**: Believing strings are a separate data type in Erlang
  **Clarification**: Strings are syntactic sugar for lists of integers. There is no string type.

- **Confusion**: Expecting adjacent strings without whitespace to concatenate
  **Clarification**: As of OTP 27, adjacent string literals require whitespace separation, to avoid ambiguity with triple-quoted strings.

# Source Reference
Data Types chapter, "String" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
