---
concept: IOLists Over String Concatenation
slug: iolists-over-string-concatenation
category: data-types
subcategory: strings
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Strings"
chapter_number: null
pdf_page: null
section: "IOLists over string concatenation"
extraction_confidence: high
aliases:
  - "iolist"
  - "io lists"
  - "avoid string concatenation"
prerequisites: []
extends: []
related:
  - avoid-length-1-calls
contrasts_with: []
answers_questions:
  - "What is an iolist, and why is it preferred over string concatenation?"
  - "How do I build strings efficiently in Erlang?"
---

# Quick Definition

Build output from iolists rather than concatenating strings with `++` whenever possible.

# Core Definition

"Use iolists instead of string concatenation whenever possible" (Inaka, "IOLists over string concatenation"). An iolist is a (possibly deeply nested) list of integers and binaries representing IO data; assembling output as an iolist avoids the copying that `++` concatenation incurs.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. An iolist is a nested list of integers and binaries.
2. Building an iolist avoids copying the data being concatenated.
3. `++`-based string concatenation copies its left operand and risks conversion errors.
4. IO functions accept iolists directly, so no flattening is needed.

# Construction / Recognition

## To Apply

1. Instead of `A ++ B ++ C`, collect the parts in a list: `[A, B, C]`.
2. Pass the iolist straight to IO/socket functions.

## To Recognize a Violation

1. `++` is used to splice together fragments of output, sometimes with `binary_to_list/1` conversions.

# Context & Application

A PR-blocking convention under Strings.

- **Typical contexts**: building HTTP responses, log lines, rendered text.
- **Common applications**: returning `["Hello ", Param, "! Have a nice day!"]` rather than concatenating.

# Examples

**Example 1** — bad: `"Hello " ++ binary_to_list(Param) ++ "! Have a nice day!"`.

**Example 2** — good: `["Hello ", Param, "! Have a nice day!"]`.

# Relationships

## Related

- **Avoid unnecessary calls to length/1** — both concern efficient handling of list-shaped data.

# Common Errors

- **Error**: Converting a binary to a list with `binary_to_list/1` just to `++` it.
  **Correction**: Put the binary directly into an iolist; no conversion needed.

# Common Confusions

- **Confusion**: Thinking an iolist must be flattened before use.
  **Clarification**: IO functions accept the nested structure as-is; flattening would reintroduce copying.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Strings", guideline "IOLists over string concatenation".

# Verification Notes

- Definition source: Direct quote plus paraphrase of the reasoning.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: `avoid-length-1-calls` is a planned card in this extraction.
