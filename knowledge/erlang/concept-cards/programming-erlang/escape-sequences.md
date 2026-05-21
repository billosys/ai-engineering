---
# === CORE IDENTIFICATION ===
concept: Escape Sequences
slug: escape-sequences

# === CLASSIFICATION ===
category: core-idioms
subcategory: syntax
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Escape Sequences"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - escape character
  - "\\n"
  - "\\t"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - numbers
  - character-set
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What escape sequences does Erlang support?"
  - "How do I enter a nonprintable character in a string?"
---

# Quick Definition

Escape sequences are backslash-prefixed codes used within strings and quoted atoms to enter nonprintable characters; each evaluates to an integer character code.

# Core Definition

"Within strings and quoted atoms, you can use escape sequences to enter any nonprintable characters" ("The Rest of Sequential Erlang", *Escape Sequences*). The book tabulates them: `\b` backspace (8), `\d` delete (127), `\e` escape (27), `\f` form feed (12), `\n` new line (10), `\r` carriage return (13), `\s` space (32), `\t` tab (9), `\v` vertical tab (11), `\x{...}` hexadecimal characters, `\^a..\^z`/`\^A..\^Z` Ctrl+A to Ctrl+Z (1 to 26), `\'` single quote (39), `\"` double quote (34), `\\` backslash (92), and `\C` the ASCII code for character `C`. Octal characters are also accepted (e.g. `\123` is 83). Because Erlang strings are lists of integers, an escape sequence in a string contributes its integer code to the list.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Escape sequences begin with `\` and are used in strings and quoted atoms.
2. Each evaluates to an integer character code.
3. Named sequences include `\b \d \e \f \n \r \s \t \v`.
4. `\x{...}` enters hexadecimal characters; `\C` gives the ASCII code of character `C`.
5. `\^a..\^Z` produce Ctrl+A through Ctrl+Z (codes 1 to 26).
6. Octal sequences such as `\123` are accepted.
7. `\'`, `\"`, and `\\` escape the quote and backslash characters.

# Construction / Recognition

## To Construct/Create:
1. Embed escapes in a string literal: `"\b\d\e\f\n\r\s\t\v"`.
2. Use `\x{...}` for hexadecimal or `\NNN` for octal characters.

## To Identify/Recognize:
1. A backslash inside a string or quoted atom begins an escape sequence.

# Context & Application

- **Typical contexts**: string literals containing control or special characters.
- **Common applications**: `\n` for newlines, `\t` for tabs in formatted output.
- **Historical/stylistic notes**: since strings are lists of integers, `io:format("~w~n", ["\b\d..."])` prints the underlying integer codes, e.g. `[8,127,...]`.

# Examples

**Example 1** (*Escape Sequences*): control characters resolve to their codes:

```erlang
1> io:format("~w~n", ["\b\d\e\f\n\r\s\t\v"]).
[8,127,27,12,10,13,32,9,11]
```

**Example 2** (*Escape Sequences*): octal characters — `"\123\12\1"` is `[83,10,1]`.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Numbers** — The `$C` integer syntax may itself contain an escape sequence (e.g. `$\n` is 10).
- **Character set** — Escape sequences enter characters that may otherwise need the source character set.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Forgetting to escape a quote or backslash inside a string.
  **Correction**: Use `\"`, `\'`, and `\\` to include those characters literally.

# Common Confusions

- **Confusion**: Thinking an escape sequence produces a special character object.
  **Clarification**: It produces an integer character code; since strings are lists of integers, the escape simply contributes its code.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Escape Sequences" (Table 4).

# Verification Notes

- Definition source: Direct adaptation of the *Escape Sequences* section and Table 4.
- Confidence rationale: HIGH — the source tabulates every escape sequence with its integer code.
- Uncertainties: None.
- Cross-reference status: Slugs `numbers`, `character-set` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
