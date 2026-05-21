---
# === CORE IDENTIFICATION ===
concept: Limitations of the Type System
slug: type-system-limitations

# === CLASSIFICATION ===
category: tooling
subcategory: static-analysis
tier: advanced

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Types"
chapter_number: 9
pdf_page: null
section: "Limitations of the Type System"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "type checking limitations"
  - "what Dialyzer cannot find"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - success-typing
extends: []
related:
  - dialyzer
  - success-typing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What kinds of errors can the type system not catch?"
  - "Why does a clean Dialyzer run not prove correctness?"
  - "What are the limits of success typing?"
---

# Quick Definition

The Erlang type system, as checked by Dialyzer, finds discrepancies but cannot catch errors where data is used type-consistently yet logically wrongly. A clean run proves consistency, not correctness.

# Core Definition

Dialyzer's analysis is based on success typing, which under-approximates failure. As a result, the type system has limitations: a program can be entirely type-consistent and still be wrong. The source illustrates this with arithmetic — when converting hours, minutes, and seconds, every value is a number and the operations are well-typed, so "no errors will be returned" even if the computation is logically incorrect; `typer` "thinks that calling" the function is fine because `+` takes two numbers and returns a number (Armstrong, "Types," "Limitations of the Type System"). The type checker reasons about *types*, not *intent*.

# Prerequisites

- **Success typing** — The limitations follow directly from the under-approximating nature of success typing; you must understand it first.

# Key Properties

1. A clean Dialyzer run proves type consistency, not program correctness.
2. Errors where wrongly used data still has the right type are invisible to the checker.
3. Arithmetic over numbers is fully type-consistent regardless of unit or magnitude mistakes.
4. The checker reasons about types, not the programmer's intent.
5. Tighter types (bounded ranges, distinct named types) shrink — but do not eliminate — the blind spot.

# Construction / Recognition

## To Construct/Create:
This concept is descriptive, not constructive. To *expose* the limitation: write a function whose values are all the same type (e.g. all numbers) but whose logic is wrong, and observe that Dialyzer still passes it.

## To Identify/Recognize:
1. A "passed successfully" Dialyzer result on code that still produces wrong answers indicates a limitation has been hit.
2. Bugs in unit conversion, sign, or magnitude over uniformly typed data are typical blind spots.

# Context & Application

- **Typical contexts**: Reasoning about how much assurance Dialyzer provides; deciding where tests are still needed.
- **Common applications**: Justifying that type checking complements — not replaces — unit tests and property tests.
- **Historical/stylistic notes**: Armstrong follows the limitation discussion with a `typer types1.erl` run showing the tool reports no errors on a module with a logic bug.

# Examples

**Example 1** ("Limitations of the Type System"): An hours/minutes/seconds conversion where every variable is a number — `typer` and Dialyzer report no error even though the conversion formula could be wrong.

**Example 2** ("Limitations of the Type System"): Running `typer types1.erl` shows the tool "knows that `+` takes two numbers as arguments and returns a number," so a call it analyzes is accepted regardless of logical intent.

# Relationships

## Builds Upon
- **Success typing** — Limitations are a direct consequence of success typing under-approximating failure.

## Enables
- (No downstream concept; this is a cautionary endpoint of the chapter.)

## Related
- **Dialyzer** — The tool whose guarantees these limitations bound.
- **Success typing** — The analysis basis whose nature causes the limitations.

## Contrasts With
- None.

# Common Errors

- **Error**: Skipping tests because "Dialyzer passes."
  **Correction**: Dialyzer proves consistency only; keep unit and property tests for logical correctness.

- **Error**: Modeling distinct quantities (miles vs. kilometers) all as `integer()`.
  **Correction**: Use distinct named types so the checker can distinguish them, narrowing the blind spot.

# Common Confusions

- **Confusion**: Believing a passing type check means the program is correct.
  **Clarification**: It means data types are used consistently; logic errors over correctly typed data go undetected.

- **Confusion**: Thinking Erlang's checker is simply weaker than other type systems by accident.
  **Clarification**: It is a deliberate design — success typing avoids false positives at the cost of missing some real bugs.

# Source Reference

Chapter 9: "Types," section "Limitations of the Type System." EPUB source — no page numbers.

# Verification Notes

- Definition source: Synthesized from the "Limitations of the Type System" discussion and the accompanying `typer` example.
- Confidence rationale: MEDIUM — the limitation is described through examples rather than a single crisp definition; the card synthesizes the principle.
- Uncertainties: None material.
- Cross-reference status: Verified slugs against planned chapter-9 cards.
- Re-extraction notes: Fresh extraction; new card (no prior file).
