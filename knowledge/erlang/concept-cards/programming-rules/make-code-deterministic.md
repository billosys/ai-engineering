---
concept: Make Code As Deterministic As Possible
slug: make-code-deterministic
category: core-idioms
subcategory: sw-engineering-principles
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.12 Make code as deterministic as possible"
extraction_confidence: high
aliases:
  - "deterministic code"
  - "reproducible behavior"
prerequisites: []
extends: []
related:
  - eliminate-side-effects
  - use-process-dictionary-with-care
contrasts_with: []
answers_questions:
  - "What distinguishes a deterministic program from a non-deterministic one?"
  - "Why make code deterministic for debugging?"
---

# Quick Definition

Make code as deterministic as possible — a deterministic program runs the same way every time, which makes errors reproducible.

# Core Definition

"A deterministic program is one which will always run in the same manner no matter how many times the program is run. A non-deterministic program may deliver different results each time" (Programming Rules, 3.12). For debugging it is good to make things as deterministic as possible, because this makes errors reproducible.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A deterministic program behaves identically across runs.
2. A non-deterministic program may produce different results each run.
3. Determinism makes errors reproducible, which aids debugging.
4. Unnecessary parallelism is a common source of non-determinism.

# Construction / Recognition

## To Apply

1. Where ordering does not matter for correctness, still impose a fixed order for reproducibility.
2. Prefer sequential steps over parallel ones when parallelism is not required.

## To Recognize a Candidate

1. A task is done in parallel where a deterministic sequential order would serve.

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: startup sequences, batch processing, anything where order is free.
- **Common applications**: starting and checking processes one at a time.

# Examples

**Example** (from source): starting five parallel processes — rather than starting all five at once and then checking, it is better to start them one at a time and check each before starting the next.

# Relationships

## Related

- **Try to eliminate side effects** — side effects are a source of run-to-run variation.
- **Use the process dictionary with extreme care** — process-dictionary state makes behavior non-deterministic.

# Common Errors

- **Error**: Doing order-independent work in parallel just because it can be.
  **Correction**: Impose a deterministic order so failures reproduce.

# Common Confusions

- **Confusion**: Thinking determinism conflicts with Erlang's concurrency.
  **Clarification**: The rule targets *unnecessary* non-determinism; genuine concurrency is still used where the problem requires it.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.12 "Make code as deterministic as possible".

# Verification Notes

- Definition source: Direct adaptation of section 3.12.
- Confidence rationale: HIGH — the rule is stated explicitly with an example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
