---
concept: Use The Principle Of Least Astonishment
slug: principle-of-least-astonishment
category: core-idioms
subcategory: sw-engineering-principles
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.9 Use the principle of \"least astonishment\""
extraction_confidence: high
aliases:
  - "least astonishment"
  - "least surprise"
  - "consistency"
prerequisites: []
extends: []
related:
  - function-names
  - consistent-formatting
contrasts_with: []
answers_questions:
  - "What is the principle of least astonishment?"
  - "How does consistency reduce astonishment in a system?"
---

# Quick Definition

A system should always respond in the way that causes the user the least astonishment — users should be able to predict what their actions will do.

# Core Definition

"The system should always respond in a manner which causes the 'least astonishment' to the user — i.e. a user should be able to predict what will happen when they do something" (Programming Rules, 3.9). This is about consistency: a system where different modules do similar things in similar ways is far easier to understand. "If you get astonished by what a function does, either your function solves the wrong problem or it has a wrong name."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The system behaves predictably; users can anticipate the result of an action.
2. Consistency across modules is the mechanism that delivers predictability.
3. An astonishing function either solves the wrong problem or is misnamed.

# Construction / Recognition

## To Apply

1. Make modules do similar things in similar ways.
2. If a function surprises you, fix its behavior or its name.

## To Recognize a Violation

1. A function's behavior surprises a reader who knew its name and arguments.

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: API design, naming, cross-module consistency.
- **Common applications**: aligning how analogous operations behave across modules.

# Examples

The source states the principle directly; no code example is given.

# Relationships

## Related

- **Function names** — an astonishing function is often simply misnamed.
- **Format programs in a consistent manner** — consistency is the route to predictability.

# Common Errors

- **Error**: Letting each module solve similar problems in its own idiosyncratic way.
  **Correction**: Make analogous operations consistent across modules.

# Common Confusions

- **Confusion**: Treating astonishment as the user's fault.
  **Clarification**: The source places the fault in the code — wrong problem solved, or wrong name.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.9 "Use the principle of 'least astonishment'".

# Verification Notes

- Definition source: Direct adaptation of section 3.9.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
