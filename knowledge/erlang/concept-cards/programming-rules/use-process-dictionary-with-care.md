---
concept: Use The Process Dictionary With Extreme Care
slug: use-process-dictionary-with-care
category: anti-patterns
subcategory: erlang-specific-conventions
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Various Erlang Specific Conventions"
chapter_number: 6
pdf_page: null
section: "6.5 Use the process dictionary with extreme care"
extraction_confidence: high
aliases:
  - "process dictionary"
  - "get and put"
prerequisites: []
extends: []
related:
  - eliminate-side-effects
  - make-code-deterministic
  - isolate-dirty-code
contrasts_with: []
answers_questions:
  - "What is the process dictionary, and why should it be used with care?"
  - "How can I rewrite a function that uses get/put?"
---

# Quick Definition

Use `get` and `put` (the process dictionary) as little as possible, and only when you know exactly what you are doing — a function using it can usually be rewritten with an extra argument.

# Core Definition

"Do not use `get` and `put` etc. unless you know exactly what you are doing! Use `get` and `put` etc. as little as possible" (Programming Rules, 6.5). A function that uses the process dictionary can be rewritten by introducing a new argument. Using `get`/`put` makes a function behave differently for the same input at different times — it becomes non-deterministic and hard to read, and run-time errors (e.g. `bad_match`) report the arguments but never the process dictionary, complicating debugging.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The process dictionary (`get`/`put`/`erase`) is used as little as possible.
2. A process-dictionary-using function can be rewritten by adding an argument.
3. `get`/`put` make a function depend on hidden state, so it is non-deterministic.
4. Run-time errors report function arguments but never the process dictionary, hampering debugging.

# Construction / Recognition

## To Apply

1. Replace `put`/`get` of a value with an explicit function parameter threaded through calls.

## To Recognize a Violation

1. A function reads or writes the process dictionary instead of using its arguments.

# Context & Application

A core Erlang-specific convention (section 6).

- **Typical contexts**: code tempted to stash state in the process dictionary.
- **Common applications**: threading a `Device` argument instead of `get(device)`.

# Examples

**Example** (from source): the bad `tokenize/1` calls `get(device)`; the correct `tokenize/2` takes `Device` as an explicit argument and threads it through the recursion.

# Relationships

## Related

- **Try to eliminate side effects** — `get`/`put` are environment-changing side effects.
- **Make code as deterministic as possible** — the process dictionary makes behavior non-deterministic.
- **Isolate "tricky" or "dirty" code into separate modules** — process-dictionary use is named "dirty" code.

# Common Errors

- **Error**: Stashing state in the process dictionary instead of passing it.
  **Correction**: Add an explicit argument and thread the value through.

# Common Confusions

- **Confusion**: Thinking the process dictionary is just convenient local storage.
  **Clarification**: It makes functions non-deterministic and invisible to error reports — debugging becomes much harder.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 6.5 "Use the process dictionary with extreme care".

# Verification Notes

- Definition source: Direct adaptation of section 6.5.
- Confidence rationale: HIGH — the rule is stated explicitly with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
