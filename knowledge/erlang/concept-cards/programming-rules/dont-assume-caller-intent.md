---
concept: Don't Assume What The Caller Will Do With A Result
slug: dont-assume-caller-intent
category: api-design
subcategory: sw-engineering-principles
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.5 Don't make assumptions about what the caller will do with the results of a function"
extraction_confidence: high
aliases:
  - "don't assume caller intent"
  - "return errors, don't print them"
prerequisites: []
extends: []
related:
  - use-tagged-return-values
  - separate-error-handling-from-normal-code
  - eliminate-side-effects
contrasts_with: []
answers_questions:
  - "Should a function decide what to do with its own error, or return it to the caller?"
  - "Why shouldn't a function print or log an error itself?"
---

# Quick Definition

A function should not assume why it was called or what the caller wants done with its results — return an error descriptor and let the caller decide.

# Core Definition

"Don't make assumptions about why a function has been called or about what the caller of a function wishes to do with the results" (Programming Rules, 3.5). When arguments may be invalid, the implementer must not assume what should happen; rather than printing an error to standard output, return an error descriptor (`{error, What}`) so the application can decide what to do with it.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A function does not assume the caller's intent or purpose.
2. Errors are returned as descriptors, not printed or logged inside the function.
3. The decision about how to handle a result belongs to the caller.
4. A separate function (e.g. `error_report/1`) can convert a descriptor to a printable string when the caller chooses.

# Construction / Recognition

## To Apply

1. Return `{error, What}` instead of calling `io:format` inside the function.
2. Provide a separate reporting function the caller may invoke if it wants.

## To Recognize a Violation

1. A function writes an error to standard output (or logs it) instead of returning it.

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: functions validating arguments or producing fallible results.
- **Common applications**: returning `{error, What}` from `do_something/1` and offering `error_report/1` to format it.

# Examples

**Example** (from source): the bad `do_something/1` calls `io:format("* error:~s\n", [String])` inside the error branch; the good version returns `{error, What}` and supplies a separate `error_report/1` that formats the descriptor.

# Relationships

## Related

- **Use tagged return values** — error descriptors are tagged return values.
- **Separate error handling and normal case code** — both keep error policy out of the worker function.
- **Try to eliminate side effects** — printing inside a function is a side effect.

# Common Errors

- **Error**: Printing or logging an error from within the function that detected it.
  **Correction**: Return the error descriptor; let the caller decide whether to print it.

# Common Confusions

- **Confusion**: Thinking printing the error is "handling" it.
  **Clarification**: Printing forces one behavior on every caller; returning the descriptor leaves the choice where it belongs.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.5 "Don't make assumptions about what the caller will do with the results of a function".

# Verification Notes

- Definition source: Direct adaptation of section 3.5.
- Confidence rationale: HIGH — the rule is stated explicitly with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
