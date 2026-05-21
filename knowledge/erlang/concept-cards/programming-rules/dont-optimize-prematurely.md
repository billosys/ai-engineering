---
concept: Don't Optimize Code Prematurely
slug: dont-optimize-prematurely
category: core-idioms
subcategory: sw-engineering-principles
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.8 Don't optimize code"
extraction_confidence: high
aliases:
  - "don't optimize"
  - "premature optimization"
  - "make it right then fast"
prerequisites: []
extends: []
related:
  - top-down-design
  - principle-of-least-astonishment
contrasts_with: []
answers_questions:
  - "When should I optimize Erlang code?"
---

# Quick Definition

Don't optimize at the first stage — make the code right first, then make it fast only if necessary, while keeping it right.

# Core Definition

"Don't optimize your code at the first stage. First make it right, then (if necessary) make it fast (while keeping it right)" (Programming Rules, 3.8). Correctness comes before speed; optimization is a later, conditional step.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Correctness is achieved before any optimization.
2. Optimization happens only "if necessary".
3. Optimization must not break correctness.

# Construction / Recognition

## To Apply

1. Write the simplest correct implementation first.
2. Optimize later, only where measurement shows a need, preserving correctness.

## To Recognize a Violation

1. Code is contorted for speed before it is known to be correct or even necessary.

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: initial implementation of any function or module.
- **Common applications**: shipping a clear, correct version before profiling.

# Examples

The source states the principle directly; no code example is given.

# Relationships

## Related

- **Top-down** — both favor getting structure and correctness right before details and speed.
- **Use the principle of least astonishment** — clear, unoptimized code is more predictable.

# Common Errors

- **Error**: Hand-optimizing code during the first implementation pass.
  **Correction**: Make it right first; optimize later only if measurement demands it.

# Common Confusions

- **Confusion**: Thinking early optimization saves time.
  **Clarification**: It risks shipping fast-but-wrong code; correctness is the prerequisite for useful speed.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.8 "Don't optimize code".

# Verification Notes

- Definition source: Direct adaptation of section 3.8.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
