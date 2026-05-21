---
concept: Use Catch And Throw With Extreme Care
slug: use-catch-and-throw-with-care
category: error-handling
subcategory: erlang-specific-conventions
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Various Erlang Specific Conventions"
chapter_number: 6
pdf_page: null
section: "6.4 Use catch and throw with extreme care"
extraction_confidence: high
aliases:
  - "catch and throw"
  - "catch/throw with care"
prerequisites: []
extends: []
related:
  - separate-error-handling-from-normal-code
  - dont-program-defensively
contrasts_with: []
answers_questions:
  - "When is it appropriate to use catch and throw?"
---

# Quick Definition

Use `catch` and `throw` as little as possible, and only when you know exactly what you are doing.

# Core Definition

"Do not use catch and throw unless you know exactly what you are doing! Use catch and throw as little as possible" (Programming Rules, 6.4). They can be useful when a program handles complicated, unreliable input from the outside world that may cause errors deep within the code — one example being a compiler.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `catch` and `throw` are used as little as possible.
2. They are used only when the programmer knows exactly what they are doing.
3. A legitimate use is handling complicated, unreliable external input that can fail deep in the code.
4. A compiler is the source's example of such a legitimate case.

# Construction / Recognition

## To Apply

1. Reserve `catch`/`throw` for deeply nested failures from unreliable external input.
2. For ordinary control flow and error reporting, prefer tagged return values and crashing.

## To Recognize a Candidate For Caution

1. `catch`/`throw` is used for routine control flow rather than rare deep-error escape.

# Context & Application

A core Erlang-specific convention (section 6).

- **Typical contexts**: parsers and compilers handling untrusted input.
- **Common applications**: escaping from deep recursion on a detected input error.

# Examples

The source gives a compiler as the example of complicated, unreliable input handling where `catch`/`throw` can be justified; no code listing is given.

# Relationships

## Related

- **Separate error handling and normal case code** — both keep error mechanisms out of the normal path.
- **Do not program "defensively"** — for trusted input, crashing is preferred over catch/throw.

# Common Errors

- **Error**: Using `catch`/`throw` as a general control-flow mechanism.
  **Correction**: Reserve it for rare deep-error escape from unreliable external input.

# Common Confusions

- **Confusion**: Thinking `catch`/`throw` is the normal Erlang error mechanism.
  **Clarification**: The normal mechanisms are tagged returns and crashing; `catch`/`throw` is an exception, used sparingly.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 6.4 "Use catch and throw with extreme care".

# Verification Notes

- Definition source: Direct adaptation of section 6.4.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
