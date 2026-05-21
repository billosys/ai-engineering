---
concept: Avoid Dynamic Calls
slug: avoid-dynamic-calls
category: core-idioms
subcategory: syntax
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Syntax"
chapter_number: null
pdf_page: null
section: "Avoid dynamic calls"
extraction_confidence: high
aliases:
  - "dynamic function calls"
  - "Mod:Fun calls"
  - "runtime-resolved calls"
prerequisites: []
extends: []
related:
  - encapsulate-otp-apis
  - lock-your-dependencies
contrasts_with: []
answers_questions:
  - "What is a dynamic function call?"
  - "Why should I avoid dynamic function calls in Erlang?"
---

# Quick Definition

Don't use dynamic function calls (where the module or function name is a variable) unless there is a specific need for it.

# Core Definition

"If there is no specific need for it, don't use dynamic function calling" (Inaka, "Avoid dynamic calls"). A dynamic call resolves the module and/or function name from a variable at runtime (`Mod:Fun(Arg)`), which means tools cannot statically see the call.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A dynamic call has a variable in the module or function position.
2. Dynamic calls are invisible to `xref`, the cross-reference analyzer.
3. They should be used only when there is a specific, justified need.
4. It is a PR-rejection rule under Syntax.

# Construction / Recognition

## To Apply

1. Where the set of target modules/functions is known, write each call explicitly.
2. Reserve dynamic dispatch for genuine plugin-style needs.

## To Recognize a Violation

1. A variable appears before the `:` or after it in a remote call (`Mod:Fun(...)`).

# Context & Application

A PR-blocking convention under Syntax.

- **Typical contexts**: iterating a list of modules to call the "same" function on each.
- **Common applications**: replacing a `foreach` over `[module_1, module_2, module_3]` with three explicit calls.

# Examples

**Example 1** — bad: `lists:foreach(fun(Mod) -> Mod:Fun(Arg) end, [module_1, module_2, module_3])`.

**Example 2** — good: explicit `module_1:my_function(Arg)`, `module_2:my_function(Arg)`, `module_3:my_function(Arg)`.

# Relationships

## Related

- **Encapsulate OTP server APIs** — both improve static analysability and traceability.
- **Lock your dependencies** — both favor predictable, statically known behavior.

# Common Errors

- **Error**: Looping over module names to make "the same" call dynamically.
  **Correction**: Write the calls out explicitly so `xref` can see them.

# Common Confusions

- **Confusion**: Thinking dynamic calls are forbidden outright.
  **Clarification**: They are allowed when there is a specific need (e.g., true runtime plugin dispatch); the rule targets unnecessary use.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Syntax", guideline "Avoid dynamic calls".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
