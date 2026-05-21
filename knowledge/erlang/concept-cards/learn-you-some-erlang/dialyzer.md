---
concept: Dialyzer
slug: dialyzer
category: tooling
subcategory: static-analysis
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Type Specifications and Dialyzer"
chapter_number: 30
pdf_page: null
section: "PLTs Are the Best Sandwiches"
extraction_confidence: high
aliases:
  - "DIscrepancy AnaLYZer for ERlang"
prerequisites:
  - dynamic-typing
related:
  - success-typing
  - type-specification
  - dialyzer-warning
contrasts_with: []
answers_questions:
  - "What is Dialyzer?"
  - "How does Dialyzer relate to type specifications?"
---

# Dialyzer

## Quick Definition

Dialyzer is an Erlang static analysis tool that detects type errors and other discrepancies — such as unreachable code — without requiring type declarations.

## Core Definition

Dialyzer is a very effective tool for analyzing Erlang code, used to find discrepancies such as code that will never be executed, but whose main use is detecting type errors in an Erlang code base. It works without type declarations being present (though it accepts them as hints), respects the operational semantics of Erlang, imposes no code rewrites, and complains only about type errors that would guarantee a crash. Its first step is building a *persistent lookup table (PLT)* — a compilation of everything Dialyzer can identify about the applications and modules in the Erlang distribution and other code (Chapter 30, "PLTs Are the Best Sandwiches" and "Success Typing").

## Prerequisites

- **Dynamic typing** — Dialyzer exists because Erlang is dynamically typed; understanding dynamic typing motivates the tool

## Key Properties

1. Detects type errors and discrepancies (e.g., unreachable code) without requiring type declarations
2. Requires a persistent lookup table (PLT) built once with `dialyzer --build_plt --apps ...`
3. The PLT can be extended (`--add_to_plt`), and multiple/disjoint PLTs can be used (`--plt`, `--plts`)
4. Analyzes `.beam` files by default; `--src` makes it analyze `.erl` source instead
5. Based on success typing — it never "cries wolf," reporting only errors guaranteed to cause a crash
6. Optimistic: assumes functions succeed until evidence proves otherwise; unknown functions are harmless
7. May stay silent about errors that occur only *sometimes*, since it requires certainty
8. Respects user-provided `-spec` type signatures and uses them to find further errors

## Construction / Recognition

## To Use Dialyzer

1. Build the PLT once: `dialyzer --build_plt --apps erts kernel stdlib ...`
2. Run analysis on modules: `dialyzer module.erl` (or `dialyzer -r dir --src` for source trees)
3. Read the emitted warnings and fix the discrepancies (optionally adding `-spec` signatures to sharpen analysis)

## Context & Application

Dialyzer provides the early type-error safety that a static type system would, without forcing Erlang to change its semantics. The chapter frames it as a friend that prevents the four-in-the-morning crash that gets your car keyed by the operations guy. Adding `-spec` signatures lets Dialyzer find errors it would otherwise miss (e.g., `discrep3.erl` passes clean until type signatures are added in `discrep4.erl`). Dialyzer is "practically never wrong" — it speaks only when certain.

## Examples

**Example** (Chapter 30, "Type Inference and Discrepancies"): running `dialyzer discrep1.erl` on `run() -> some_op(5, you).` reports "Function run/0 has no local return" and that `some_op(5,'you')` differs from the success typing `(number(),number())`.

## Relationships

## Builds Upon

- **Dynamic typing** — Dialyzer adds optional static checking to a dynamically typed language

## Related

- **Success typing** — The type-inference principle Dialyzer is built on
- **Type specification** — `-spec` signatures Dialyzer consumes to sharpen its analysis
- **Dialyzer warning** — The discrepancy messages Dialyzer emits

## Common Errors

- **Error**: Running `dialyzer -r dir` and getting "No .beam files to analyze"
  **Correction**: Add the `--src` flag to analyze `.erl` source, or compile to `.beam` with `debug_info`

- **Error**: Expecting Dialyzer to report every possible runtime type error
  **Correction**: Dialyzer reports only errors guaranteed to crash; it stays silent when an error is merely possible

## Common Confusions

- **Confusion**: Thinking a clean Dialyzer run proves the program has no type errors
  **Clarification**: Dialyzer does not prove the absence of errors — it does a best effort and never contradicts reality

## Source Reference

Chapter 30: Type Specifications and Dialyzer, sections "PLTs Are the Best Sandwiches," "Success Typing," "Type Inference and Discrepancies," and "You're My Type."

## Verification Notes

- Definition: Direct adaptation from the chapter opening and "PLTs Are the Best Sandwiches"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — extensively defined and demonstrated
- Cross-references: `dynamic-typing` is a shared slug from Agent 1
