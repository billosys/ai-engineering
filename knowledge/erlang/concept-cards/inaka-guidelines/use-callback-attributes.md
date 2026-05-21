---
concept: Use -callback Attributes Over behaviour_info/1
slug: use-callback-attributes
category: otp-behaviours
subcategory: misc
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Misc"
chapter_number: null
pdf_page: null
section: "Use -callback attributes over behaviour_info/1"
extraction_confidence: high
aliases:
  - "-callback attribute"
  - "behaviour_info/1"
  - "behavior callback definitions"
prerequisites:
  - use-behaviours
extends: []
related:
  - write-function-specs
contrasts_with: []
answers_questions:
  - "What is a -callback attribute, and what does it replace?"
  - "How should I declare a behaviour's required callbacks?"
---

# Quick Definition

Define a behaviour's required callbacks with `-callback` attributes rather than the older `behaviour_info/1` function.

# Core Definition

"Unless you know your project will be compiled with R14 or lower, use `-callback` instead of `behavior_info/1` for your behavior definitions" (Inaka, "Use -callback attributes over behaviour_info/1"). `-callback` attributes declare each required callback with a type spec; `behaviour_info/1` is the deprecated predecessor.

# Prerequisites

- **Use behaviours** — this rule applies when you are defining a behaviour at all.

# Key Properties

1. Required callbacks are declared with `-callback` attributes.
2. `behaviour_info(callbacks)` is the deprecated mechanism it replaces.
3. `-callback` carries a full type spec; `behaviour_info/1` only lists name/arity.
4. The only exception is targeting Erlang R14 or older.

# Construction / Recognition

## To Apply

1. For each required callback, write `-callback name(ArgType) -> ReturnType.`

## To Recognize a Violation

1. A behaviour module defines `behavior_info(callbacks) -> [{Fun, Arity}]`.

# Context & Application

A PR-blocking convention under Misc.

- **Typical contexts**: modules defining a custom behaviour.
- **Common applications**: `-callback function1(binary(), State) -> {ok, State}.`

# Examples

**Example 1** — bad: `-export([behavior_info/1])` plus `behavior_info(callbacks) -> [{function1, 2}]`.

**Example 2** — good: `-callback function1(binary(), State) -> {ok, State}.`

# Relationships

## Builds Upon

- **Use behaviours** — `-callback` is how a behaviour's contract is declared.

## Related

- **Write function specs** — `-callback` attributes are spec-like callback declarations.

# Common Errors

- **Error**: Declaring callbacks via `behaviour_info/1`.
  **Correction**: Use `-callback` attributes, which also carry type information.

# Common Confusions

- **Confusion**: Thinking both mechanisms are equivalent.
  **Clarification**: `-callback` adds type specs and is current; `behaviour_info/1` is deprecated functionality.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Misc", guideline "Use -callback attributes over behaviour_info/1".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with bad/good example files.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
