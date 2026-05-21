---
concept: Do And Undo Things In The Same Function
slug: do-and-undo-in-same-function
category: core-idioms
subcategory: sw-engineering-principles
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.15 Do and undo things in the same function"
extraction_confidence: high
aliases:
  - "do and undo together"
  - "symmetric open and close"
  - "resource symmetry"
prerequisites: []
extends: []
related:
  - dont-write-long-functions
  - eliminate-side-effects
contrasts_with: []
answers_questions:
  - "Where should a resource be released relative to where it is acquired?"
---

# Quick Definition

Acquire and release a resource in the same function — e.g. open a file and close it in the same routine — so the symmetry is visible.

# Core Definition

"Suppose we have a program which opens a file, does something with it and closes it later. This should be coded as" a single function that calls `file:open`, does the work, and calls `file:close` (Programming Rules, 3.15). The symmetry of opening and closing in the same routine makes the code easy to follow. Closing the file in some deeply nested helper function is "much harder to follow and it is not obvious which file is closed".

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Resource acquisition and release appear in the same function.
2. The open/close (do/undo) symmetry is visible at one place.
3. Releasing a resource in a distant nested helper obscures what is being released.

# Construction / Recognition

## To Apply

1. Pair each acquisition with its matching release in the same function.

## To Recognize a Violation

1. A resource is acquired in one function and released in a separate, deeply nested one.

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: file handles, sockets, locks — any acquire/release pair.
- **Common applications**: `file:open` and `file:close` in one `do_something_with/1`.

# Examples

**Example** (from source): the good `do_something_with/1` opens the file and calls `file:close(Stream)` in the same `case` branch; the bad version passes `Stream` down through `doit/1` and `func234/...` where `file:close` is finally called — "Don't do this".

# Relationships

## Related

- **Don't write very long functions** — keeping do/undo together is easiest in short functions.
- **Try to eliminate side effects** — acquisition/release are side effects best kept localized.

# Common Errors

- **Error**: Closing a resource in a nested helper far from where it was opened.
  **Correction**: Close it in the same function that opened it.

# Common Confusions

- **Confusion**: Thinking passing the handle down for cleanup is fine.
  **Clarification**: It hides which resource is released and breaks the visible do/undo symmetry.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.15 "Do and undo things in the same function".

# Verification Notes

- Definition source: Direct adaptation of section 3.15.
- Confidence rationale: HIGH — the rule is stated explicitly with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
