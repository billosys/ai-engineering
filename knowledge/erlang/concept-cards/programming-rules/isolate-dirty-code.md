---
concept: Isolate "Tricky" Or "Dirty" Code Into Separate Modules
slug: isolate-dirty-code
category: core-idioms
subcategory: sw-engineering-principles
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.4 Isolate \"tricky\" or \"dirty\" code into separate modules"
extraction_confidence: high
aliases:
  - "isolate dirty code"
  - "clean vs dirty code"
prerequisites: []
extends: []
related:
  - eliminate-side-effects
  - use-process-dictionary-with-care
  - isolate-hardware-with-device-driver
contrasts_with: []
answers_questions:
  - "What is \"dirty\" code, and how should it be handled?"
  - "What distinguishes clean code from dirty code?"
---

# Quick Definition

Separate clean code from "tricky" or "dirty" code, putting the dirty code into its own modules, and document its side effects clearly.

# Core Definition

"Often a problem can be solved by using a mixture of clean and dirty code. Separate the clean and dirty code into separate modules" (Programming Rules, 3.4). Dirty code does "dirty things" — uses the process dictionary, uses `erlang:process_info/1` for strange purposes, or does anything you are not supposed to do but have to. Maximize clean code, minimize dirty code, isolate the dirty code, and document all its side effects and problems.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Clean and dirty code live in separate modules.
2. Dirty code includes process-dictionary use, odd `process_info/1` use, and other "things you are not supposed to do".
3. The amount of dirty code is minimized; clean code is maximized.
4. Dirty code's side effects and problems are clearly documented.

# Construction / Recognition

## To Apply

1. Identify the unavoidable dirty operations.
2. Move them into dedicated modules and document their side effects.

## To Recognize a Violation

1. Process-dictionary use or other "dirty" operations are scattered through otherwise-clean modules.

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: code that must touch the process dictionary, hardware, or runtime internals.
- **Common applications**: a dedicated module wrapping all process-dictionary access.

# Examples

The source lists examples of dirty code rather than giving a code listing: using the process dictionary; using `erlang:process_info/1` for strange purposes; doing anything you are not supposed to do but have to.

# Relationships

## Related

- **Try to eliminate side effects** — dirty code is largely side-effecting code.
- **Use the process dictionary with extreme care** — a specific class of dirty code.
- **Isolate hardware interfaces with a device driver** — a specific application of isolation.

# Common Errors

- **Error**: Mixing a few dirty operations into a clean module "just this once".
  **Correction**: Move them into a dedicated, documented dirty-code module.

# Common Confusions

- **Confusion**: Thinking dirty code can be avoided entirely.
  **Clarification**: Some dirty code is unavoidable; the rule is to isolate and document it, not pretend it away.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.4 "Isolate 'tricky' or 'dirty' code into separate modules".

# Verification Notes

- Definition source: Direct adaptation of section 3.4.
- Confidence rationale: HIGH — the rule is stated explicitly with examples.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
