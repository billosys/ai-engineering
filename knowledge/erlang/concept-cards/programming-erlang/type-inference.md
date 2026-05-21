---
# === CORE IDENTIFICATION ===
concept: Type Inference
slug: type-inference

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
  - "type derivation"
  - "constraint solving"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-type-notation
extends: []
related:
  - dialyzer
  - success-typing
contrasts_with:
  - success-typing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type inference in Erlang?"
  - "How does Dialyzer derive the types of functions?"
  - "How are constraint equations used to find types?"
---

# Quick Definition

Type inference is the process of deriving the types of a function by analyzing its code. Dialyzer and typer analyze the program for constraints, build constraint equations, and solve them.

# Core Definition

"Type inference is the process of deriving the types of a function by analyzing the code. To do this, we analyze the program looking for constraints; from the constraints, we build a set of constraint equations, and then we solve the equations. The result is a set of types that we call the success typing of the program" (Armstrong, "Types," "Type Inference and Success Typing"). The `typer` tool reports the inferred types of all functions in a module. Understanding inference helps interpret Dialyzer's sometimes cryptic error messages, because those messages are phrased in terms of the success typings the inference produces.

# Prerequisites

- **Erlang type notation** — Inferred types are expressed in the type grammar; reading the notation is needed to interpret inference results.

# Key Properties

1. It is a fully automatic analysis — no annotations are required.
2. The process: gather constraints → build constraint equations → solve them.
3. The solution is the *success typing* of each function.
4. The `typer` tool surfaces inferred types for every function in a module.
5. Inference underlies Dialyzer's discrepancy reports.

# Construction / Recognition

## To Construct/Create:
1. (Performed by the tool.) Walk the function body collecting type constraints from operators, guards, and BIF calls.
2. Assemble the constraints into a set of equations.
3. Solve the equations to yield the success typing.

## To Identify/Recognize:
1. Run `typer module.erl` to see the inferred (success) typings.
2. Dialyzer error messages that mention "success typing arguments" are reporting inference output.

# Context & Application

- **Typical contexts**: Behind every Dialyzer or typer run; invisible to the programmer but observable through `typer` output.
- **Common applications**: Deriving function signatures without annotations; explaining Dialyzer's reasoning.
- **Historical/stylistic notes**: Inference works even when no `-spec` is present; guards (e.g. `is_integer(H)`) add constraints that tighten the inferred type.

# Examples

**Example 1** ("Type Inference and Success Typing"): For `f1({H,M,S}) -> (H+M*60)*60+S.` the analysis infers, from the arithmetic, that `H`, `M`, and `S` must be numbers — so `f1` takes a 3-tuple of numbers.

**Example 2** ("Type Inference and Success Typing"): For `f2({H,M,S}) when is_integer(H) -> ...` the `is_integer(H)` guard adds a constraint, so the inferred type of the first tuple element narrows from number to integer.

**Example 3** ("Type Inference and Success Typing"): Running `typer types1.erl` prints the derived types of `f1`, `f2`, and `f3`.

# Relationships

## Builds Upon
- **Erlang type notation** — Inference results are expressed in the type grammar.

## Enables
- **Success typing** — The result of inference is the success typing of the program.

## Related
- **Dialyzer** — Uses inference to find discrepancies; `typer` reports the inferred types.

## Contrasts With
- **Success typing** — Type inference is the *process*; the success typing is its *result*.

# Common Errors

- **Error**: Expecting inference alone to catch logic bugs.
  **Correction**: Inference only derives consistent types; it does not know intent — pair it with tests and tight specs.

- **Error**: Using anonymous variables in arguments, which weakens the constraints inference can gather.
  **Correction**: Constrain variables (named, with guards) so inference produces specific types.

# Common Confusions

- **Confusion**: Believing Erlang has Hindley-Milner-style typing that rejects programs.
  **Clarification**: Erlang inference computes *success typings* — it under-approximates failure, it does not reject well-typed programs.

- **Confusion**: Thinking inference and success typing are different stages.
  **Clarification**: Success typing is precisely the output of the inference process.

# Source Reference

Chapter 9: "Types," section "Type Inference and Success Typing." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct quote of the inference definition from "Type Inference and Success Typing."
- Confidence rationale: HIGH — the source defines the inference process explicitly.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-9 cards.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
