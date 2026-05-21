---
# === CORE IDENTIFICATION ===
concept: Dialyzer
slug: dialyzer

# === CLASSIFICATION ===
category: tooling
subcategory: static-analysis
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Types"
chapter_number: 9
pdf_page: null
section: "A Session with the Dialyzer"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "DIscrepancy AnaLYZer for ERlang programs"
  - "discrepancy analyzer"
  - "dialyzer"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-specification
extends: []
related:
  - success-typing
  - type-inference
  - type-system-limitations
contrasts_with:
  - type-inference

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Dialyzer?"
  - "How does the type system relate to Dialyzer?"
  - "How do I check an Erlang program for type errors?"
---

# Quick Definition

Dialyzer is a static-analysis tool, shipped with Erlang/OTP, that finds discrepancies (type and logic errors) in Erlang code. It is conservative: if it reports an error, there really is an inconsistency.

# Core Definition

Dialyzer — "DIscrepancy AnaLYZer for ERlang programs" — "finds discrepancies in Erlang code" (Armstrong, "Types," chapter introduction). It works with no type annotations at all, but adding `-spec` and `-type` annotations improves the quality of its analysis. Before first use, Dialyzer builds a **persistent lookup table (PLT)** — a cache of all the types in the standard libraries — via `dialyzer --build_plt --apps erts kernel stdlib ...`, a once-only operation taking a few minutes. Dialyzer is **conservative**: "If it complains, then there really is an inconsistency in the program." A goal of the project was to eliminate false warnings (Armstrong, "Types," "A Session with the Dialyzer").

# Prerequisites

- **Type specification** — Although Dialyzer runs without annotations, `-spec` declarations are what make its discrepancy reports precise; understanding specs is needed to use Dialyzer effectively.

# Key Properties

1. Ships with the standard Erlang distribution.
2. Requires a PLT — built once with `dialyzer --build_plt --apps ...`.
3. Conservative: every reported discrepancy is a real inconsistency, not a false positive.
4. Works with or without `-spec`/`-type` annotations; annotations sharpen the analysis.
5. A passing run means data types are used consistently — it does *not* prove the code is correct.
6. Detects abstraction violations of opaque types when type visibility is declared.

# Construction / Recognition

## To Construct/Create:
1. Build the PLT once: `dialyzer --build_plt --apps erts kernel stdlib`.
2. Run analysis on a module: `dialyzer module.erl`.
3. Read each reported discrepancy and stop to understand it before continuing.

## To Identify/Recognize:
1. Dialyzer reports begin with a PLT freshness check, then "Proceeding with analysis."
2. A clean run ends with "done (passed successfully)."

# Context & Application

- **Typical contexts**: Run continuously during development, after writing each new function.
- **Common applications**: Catching incorrect BIF return-value use, incorrect arguments to BIFs, and incorrect program logic at compile time.
- **Historical/stylistic notes**: Armstrong's recommended workflow — "think about the types first," write specs for exported functions before the code, and run Dialyzer after every new function rather than annotating a finished program all at once.

# Examples

**Example 1** ("A Session with the Dialyzer"): First launch with no PLT prints instructions to run `dialyzer --build_plt --apps erts kernel stdlib mnesia`.

**Example 2** ("Type Inference and Success Typing"): `dialyzer types1.erl` on a consistent module reports "done (passed successfully)" — but this means types are used consistently, not that the code is logically correct.

**Example 3** ("Working with the Dialyzer"): Things that confuse Dialyzer include `-compile(export_all)`, missing record field defaults (the atom `undefined` propagates), and anonymous variables in arguments.

# Relationships

## Builds Upon
- **Type specification** — Dialyzer consumes `-spec` contracts to constrain its analysis.

## Enables
- (No downstream concept in this chapter strictly requires Dialyzer.)

## Related
- **Success typing** — Dialyzer's analysis derives the success typing of each function.
- **Type inference** — Dialyzer infers types by solving constraint equations.
- **Type system limitations** — Some logic errors cannot be caught even by Dialyzer.

## Contrasts With
- **Type inference** — Type inference is the *process* of deriving types; Dialyzer is the *tool* that applies it to find discrepancies.

# Common Errors

- **Error**: Writing a whole program with no annotations, then adding specs everywhere and running Dialyzer once.
  **Correction**: Run Dialyzer at every stage; declare types first and check after each new function.

- **Error**: Using `-compile(export_all)`, which makes Dialyzer reason about arguments that "could be called from anywhere and have any type."
  **Correction**: Export only the functions that are part of the public API.

# Common Confusions

- **Confusion**: Thinking a clean Dialyzer run proves the program correct.
  **Clarification**: It only proves data types are used consistently; logic bugs (e.g. wrong unit conversions) can still pass.

- **Confusion**: Believing Dialyzer produces false positives.
  **Clarification**: Dialyzer is conservative — a reported discrepancy is always a real inconsistency.

# Source Reference

Chapter 9: "Types," sections "A Session with the Dialyzer," "Working with the Dialyzer," and "Things That Confuse the Dialyzer." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the chapter introduction and "A Session with the Dialyzer."
- Confidence rationale: HIGH — Dialyzer is defined explicitly with usage examples.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-9 cards.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
