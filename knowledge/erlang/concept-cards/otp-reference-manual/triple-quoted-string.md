---
# === CORE IDENTIFICATION ===
concept: Triple-Quoted String
slug: triple-quoted-string

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
section: "String"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - multi-line string
  - verbatim string

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string
extends:
  - string
related:
  - sigil
  - escape-sequence
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
---

# Quick Definition
Triple-quoted strings are multi-line, verbatim strings delimited by `"""` that can be indented to follow the surrounding code. They do not recognize escape sequences and do not require double quotes to be escaped.

# Core Definition
Introduced in Erlang/OTP 27, triple-quoted strings are strings delimited by `"""` that can span multiple lines and be indented to match surrounding code. They are verbatim: escape sequences are not recognized, and double quote characters do not need escaping. The indentation is defined by the whitespace preceding `"""` on the closing line, which is stripped from all content lines. The newline on the opening line and the newline on the last content line are not included in the string content (Data Types, "String" section).

# Prerequisites
- **string** -- Triple-quoted strings produce the same list-of-integers values as regular strings

# Key Properties
1. Delimited by `"""` (three or more double-quote characters)
2. Verbatim -- no escape sequences recognized
3. Double quote characters do not need escaping
4. Multi-line with automatic indentation stripping
5. The indentation is defined by whitespace before `"""` on the closing line
6. The newline after the opening `"""` is not string content
7. The newline on the last content line is not string content
8. No characters other than whitespace allowed after the opening delimiter
9. All content lines must start with the defined indentation
10. More quote characters in the delimiter allow sequences of `"` characters in content

# Construction / Recognition
## To Construct/Create:
1. Basic triple-quoted string:
```text
"""
  Line "1"
  Line "2"
  """
```
This is equivalent to `"Line \"1\"\nLine \"2\""`.

2. For content with `"""` at the start of a line, use more quote characters as delimiter:
```text
"""""
""""
"""""
```

## To Identify/Recognize:
1. Starts and ends with three or more `"` characters on their own lines
2. Content between delimiters is verbatim
3. Indentation of closing delimiter defines the stripping level

# Context & Application
Triple-quoted strings are useful for:
- Embedding multi-line text in code without escape sequences
- Including double quotes without escaping
- Writing regular expressions and other text where backslashes are common
- Code examples and templates within Erlang source

The automatic indentation stripping allows triple-quoted strings to be indented with the surrounding code without affecting the string content.

# Examples
**Example 1** (Data Types, "String" section): Basic triple-quoted string with verbatim double quotes:
```text
"""
  Line "1"
  Line "2"
  """
```
is equivalent to:
```text
"Line \"1\"\nLine \"2\""
```

**Example 2** (Data Types, "String" section): Larger example with uninterpreted escape sequences:
```text
X = """
      First line starting with two spaces
    Not escaped: "\t \r \xFF" and """

    """
```
corresponds to:
```text
X = "  First line starting with two spaces\nNot escaped: \"\\t \\r \\xFF\" and \"\"\"\n"
```

**Example 3** (Data Types, "String" section): Empty strings:
```text
"""
"""
```
and
```text
"""

  """
```
are both equivalent to `""`.

# Relationships
## Builds Upon
- **string** -- Triple-quoted strings produce string (list-of-integers) values

## Enables
No direct dependents within this extraction scope.

## Related
- **sigil** -- Sigils can use triple-quote delimiters; `~b` and `~s` with triple-quotes follow different escaping rules
- **escape-sequence** -- Triple-quoted strings do NOT recognize escape sequences (in contrast to regular strings)

## Contrasts With
No direct contrasts within this source.

# Common Errors
- **Error**: Putting non-whitespace characters after the opening `"""`
  **Correction**: Only whitespace is allowed after the opening delimiter on the same line

- **Error**: Not matching the indentation on all content lines
  **Correction**: All content lines must start with the same whitespace sequence as defined by the closing delimiter's indentation

# Common Confusions
- **Confusion**: Expecting escape sequences like `\n` or `\t` to work in triple-quoted strings
  **Clarification**: Triple-quoted strings are verbatim. `\n` appears as the literal characters backslash and n, not as a newline.

- **Confusion**: Expecting triple-quoted strings to behave the same as before OTP 27
  **Clarification**: Before OTP 27, `"""` was interpreted as `"" "` (empty string concatenated with the following string). The meaning changed with the introduction of triple-quoted strings.

# Source Reference
Data Types chapter, "String" section, triple-quoted strings subsection. Includes a warning about pre-OTP 27 behavior.

# Verification Notes
- Definition source: Direct from source material
- Confidence rationale: High -- detailed explanation with multiple examples
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
