---
# === CORE IDENTIFICATION ===
concept: Success Typing
slug: success-typing

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
section: "Type Inference and Success Typing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "success typing"
  - "the types that the function will not fail with"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-inference
extends:
  - type-inference
related:
  - dialyzer
  - type-system-limitations
contrasts_with:
  - type-inference

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a success typing?"
  - "How does Dialyzer decide whether a call is wrong?"
  - "Why does Dialyzer not reject all incorrect programs?"
---

# Quick Definition

A success typing is the set of argument and return types derived for a function by solving its constraint equations. It describes the types the function will *not* fail with — the basis for Dialyzer's discrepancy reports.

# Core Definition

The success typing of a program is "the result" of type inference — the set of types obtained by gathering constraints, building constraint equations, and solving them (Armstrong, "Types," "Type Inference and Success Typing"). The term "literally means 'the types that the function' will succeed with" — it characterizes the calls that can plausibly succeed. Dialyzer reports a discrepancy when a call cannot match the callee's success typing. Because success typing under-approximates failure, a function may have a permissive success typing that lets logically wrong calls through — so a clean Dialyzer run does not prove correctness.

# Prerequisites

- **Type inference** — A success typing is the output of the inference process; you must understand inference to understand what a success typing is.

# Key Properties

1. It is the solution to a function's constraint equations.
2. It names the argument and return types under which the function can succeed.
3. Dialyzer error messages report "success typing arguments" — the inferred types it expects.
4. A discrepancy is reported when an actual call cannot match the success typing.
5. Success typings are computed even without `-spec` annotations.
6. They under-approximate failure: not every type-wrong-in-intent program is rejected.

# Construction / Recognition

## To Construct/Create:
1. (Performed by the tool.) Solve the constraint equations produced by type inference.
2. The resulting type set is the success typing.

## To Identify/Recognize:
1. `typer` output lists each function's success typing.
2. Dialyzer messages of the form "...it differs in the Nth argument from the success typing arguments: (...)" name a success typing.

# Context & Application

- **Typical contexts**: Reported by `typer`; cited in Dialyzer discrepancy messages.
- **Common applications**: Understanding *why* Dialyzer flags a call; comparing a written `-spec` against the inferred success typing.
- **Historical/stylistic notes**: The success-typing approach was a deliberate design choice so the analysis produces no false positives.

# Examples

**Example 1** ("A Session with the Dialyzer"): Dialyzer reports a call differs "in the 1st argument from the success typing" — the printed tuple is the function's success typing.

**Example 2** ("Type Inference and Success Typing"): `typer types1_bug.erl` prints `success typing arguments: (integer(),integer(),integer())` for a function whose inferred argument types are three integers.

**Example 3** ("Type Inference and Success Typing"): A clean `dialyzer types1.erl` run means the success typings are consistent — but "this does not mean that the code is correct."

# Relationships

## Builds Upon
- **Type inference** — A success typing *is* the result of the inference process.

## Enables
- **Dialyzer** — Discrepancy detection compares actual calls against success typings.

## Related
- **Type system limitations** — Because success typing under-approximates, some bugs escape detection.

## Contrasts With
- **Type inference** — Inference is the procedure; the success typing is the artifact it produces.

# Common Errors

- **Error**: Treating a function's success typing as a strict contract that rejects all wrong calls.
  **Correction**: Success typing only flags calls that *cannot* succeed; add tight `-spec`s and tests for stronger guarantees.

- **Error**: Ignoring "success typing arguments" lines in Dialyzer output.
  **Correction**: They name exactly the types Dialyzer expected — read them to locate the discrepancy.

# Common Confusions

- **Confusion**: Thinking a success typing is the same as a hand-written `-spec`.
  **Clarification**: A `-spec` is declared by the programmer; a success typing is inferred — Dialyzer can compare the two.

- **Confusion**: Believing a permissive success typing means the function is correct.
  **Clarification**: Success typings under-approximate failure; logically wrong but type-consistent calls still type-check.

# Source Reference

Chapter 9: "Types," section "Type Inference and Success Typing." EPUB source — no page numbers.

# Verification Notes

- Definition source: Adapted from the success-typing definition and the typer/dialyzer examples in the named section.
- Confidence rationale: HIGH — the source names and explains the concept directly.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-9 cards.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
