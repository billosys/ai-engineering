---
concept: Do Not Program Defensively
slug: dont-program-defensively
category: fault-tolerance
subcategory: sw-engineering-principles
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.13 Do not program \"defensively\""
extraction_confidence: high
aliases:
  - "non-defensive programming"
  - "let it crash"
  - "trust the input"
prerequisites: []
extends: []
related:
  - identify-the-error-kernel
  - separate-error-handling-from-normal-code
  - dont-assume-caller-intent
contrasts_with: []
answers_questions:
  - "What is defensive programming, and why is it discouraged in Erlang?"
  - "Where should input data be checked for correctness?"
---

# Quick Definition

Don't program defensively — write code assuming its input is correct, and check data only once, where it first enters the system.

# Core Definition

"A defensive program is one where the programmer does not 'trust' the input data to the part of the system they are programming. In general one should not test input data to functions for correctness" (Programming Rules, 3.13). Most code assumes its input is correct; only a small part checks data, and that is done once, when data first enters the system. After that, the data is assumed correct. A function given bad input should simply crash — the caller is responsible for supplying correct input.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Most code is written assuming its input is correct.
2. Data is validated once, where it first enters the system.
3. After entry validation, data is assumed correct everywhere else.
4. A function given invalid input should crash, not defensively handle it.

# Construction / Recognition

## To Apply

1. Validate external data at the system boundary.
2. Write internal functions to assume correct input; let bad input crash them.

## To Recognize a Violation

1. Internal functions re-check arguments that were already validated at entry.

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: internal functions deep inside a system.
- **Common applications**: a function `case`-matching only the valid options, crashing on anything else.

# Examples

**Example** (from source): `get_server_usage_info/2` matches `Option` against `all` and `normal` only — "The function will crash if Option neither normal nor all, and it should do that. The caller is responsible for supplying correct input."

# Relationships

## Related

- **Identify the error kernel** — defines which boundary code *must* be correct (and validate).
- **Separate error handling and normal case code** — crashing keeps the normal path uncluttered.
- **Don't make assumptions about what the caller will do** — the caller, not the callee, owns input correctness.

# Common Errors

- **Error**: Re-validating already-checked data in every internal function.
  **Correction**: Validate once at the boundary; let internal functions crash on bad input.

# Common Confusions

- **Confusion**: Thinking crashing on bad input is sloppy.
  **Clarification**: In Erlang it is deliberate — the crash is caught by supervision; defensive checks just obscure the normal case.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.13 "Do not program 'defensively'".

# Verification Notes

- Definition source: Direct adaptation of section 3.13.
- Confidence rationale: HIGH — the rule is stated explicitly with a code example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
