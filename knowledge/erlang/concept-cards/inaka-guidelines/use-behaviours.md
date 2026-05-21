---
concept: Use Behaviours
slug: use-behaviours
category: otp-behaviours
subcategory: suggestions
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Suggestions & Great Ideas"
chapter_number: null
pdf_page: null
section: "Use behaviours"
extraction_confidence: high
aliases:
  - "behaviours"
  - "behaviors"
  - "encapsulate reusable code in behaviours"
prerequisites: []
extends: []
related:
  - use-callback-attributes
  - encapsulate-otp-apis
  - explicit-state-record-naming
contrasts_with: []
answers_questions:
  - "What is a behaviour, and what is it used for?"
  - "How should I encapsulate reusable code in Erlang?"
---

# Quick Definition

Encapsulate reusable code in behaviours.

# Core Definition

"Encapsulate reusable code in behaviors" (Inaka, "Use behaviours"). A behaviour factors a common pattern into a generic part plus a set of `-callback`-declared functions that concrete modules implement — "the OTP way."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Reusable structure is captured as a behaviour.
2. A behaviour declares required callbacks (e.g., via `-callback` attributes).
3. Concrete modules implement the callbacks and declare `-behaviour(...)`.
4. This is a "Suggestion & Great Idea" — advisory, not a PR-blocking rule.

# Construction / Recognition

## To Apply

1. Identify code reused across modules with the same shape.
2. Define a behaviour module with `-callback` declarations and any shared types.
3. Have concrete modules declare the behaviour and implement its callbacks.

## To Recognize a Candidate

1. Several modules duplicate the same structural pattern that could be a behaviour.

# Context & Application

A "Suggestion & Great Idea" — advisory; does not by itself block a PR.

- **Typical contexts**: storage/repository abstractions, protocol handlers.
- **Common applications**: a behaviour declaring `store/1`, `retrieve/1`, `delete/1`, `count/0` callbacks with exported `element/0` and `id/0` types.

# Examples

**Example 1** (from source): a `behavior` module with `-export_type([element/0, id/0])` and `-callback store(element()) -> id().`, `-callback retrieve(id()) -> notfound | element().`, `-callback delete(id()) -> ok.`, `-callback count() -> non_neg_integer().`

# Relationships

## Related

- **Use -callback attributes over behaviour_info/1** — how a behaviour's callbacks are declared.
- **Encapsulate OTP server APIs** — both concern disciplined use of OTP behaviours.
- **Explicit state should be explicitly named** — the state-record rule applies to behaviour implementations.

# Common Errors

- **Error**: Copy-pasting the same structural code across modules.
  **Correction**: Factor the shared pattern into a behaviour with callbacks.

# Common Confusions

- **Confusion**: Thinking behaviours are only the built-in OTP ones (`gen_server`, etc.).
  **Clarification**: You can and should define your own behaviours to encapsulate reusable code.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Suggestions & Great Ideas", guideline "Use behaviours".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit suggestion with a code example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
