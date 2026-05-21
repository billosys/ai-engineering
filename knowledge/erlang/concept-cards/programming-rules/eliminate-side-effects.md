---
concept: Try To Eliminate Side Effects
slug: eliminate-side-effects
category: core-idioms
subcategory: sw-engineering-principles
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.10 Try to eliminate side effects"
extraction_confidence: high
aliases:
  - "eliminate side effects"
  - "pure functions"
  - "side-effect-free code"
prerequisites: []
extends: []
related:
  - common-code-into-libraries
  - isolate-dirty-code
  - use-process-dictionary-with-care
  - make-code-deterministic
contrasts_with: []
answers_questions:
  - "Why should I write side-effect-free code?"
  - "What counts as a side effect in Erlang?"
---

# Quick Definition

Write as much code as possible free of side effects; maximize pure functions and collect the side-effecting ones together with clear documentation.

# Core Definition

"Erlang has several primitives which have side effects. Functions which use these cannot be easily re-used since they cause permanent changes to their environment" (Programming Rules, 3.10). The rule: write as much side-effect-free code as possible, maximize pure functions, collect side-effecting functions together, and document all the side effects. The source (section 2) defines side effects as sending or receiving a message, calling `exit`, or calling any BIF that changes a process's environment (`get/1`, `put/2`, `erase/1`, `process_flag/2`, etc.).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A pure function returns the same value for the same arguments, regardless of context.
2. Side effects include sending/receiving messages, calling `exit`, and environment-changing BIFs.
3. Side-effecting functions are hard to reuse — they require knowing the process state first.
4. Pure functions are maximized; side-effecting functions are collected and documented.

# Construction / Recognition

## To Apply

1. Prefer pure functions; pass state as arguments rather than mutating environment.
2. Group the unavoidable side-effecting functions and document their effects.

## To Recognize a Violation

1. Side-effecting calls are scattered through code that could be pure.

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: most computation, which can be pure with a little care.
- **Common applications**: keeping message-passing and `put/get` at the edges, computation pure.

# Examples

The source defines side effects (section 2) and states the rule (3.10) without a dedicated code listing.

# Relationships

## Related

- **Put commonly used code into libraries** — pure functions make the best library functions.
- **Isolate "tricky" or "dirty" code into separate modules** — side-effecting code is largely "dirty" code.
- **Use the process dictionary with extreme care** — `put`/`get` are a key source of side effects.
- **Make code as deterministic as possible** — side effects undermine determinism.

# Common Errors

- **Error**: Sprinkling message sends or `put`/`get` through otherwise-pure computation.
  **Correction**: Keep computation pure; isolate the side effects.

# Common Confusions

- **Confusion**: Thinking only mutation is a side effect.
  **Clarification**: In Erlang, sending/receiving messages and calling `exit` also count, per the source's section-2 definition.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.10 "Try to eliminate side effects" (with the side-effect definition from section 2).

# Verification Notes

- Definition source: Direct adaptation of section 3.10, plus the side-effect definition from section 2.
- Confidence rationale: HIGH — the rule and definition are both stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
