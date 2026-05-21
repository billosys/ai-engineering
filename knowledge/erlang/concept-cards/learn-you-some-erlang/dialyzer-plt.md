---
concept: Persistent Lookup Table
slug: dialyzer-plt
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
  - "PLT"
  - "Dialyzer PLT"
prerequisites:
  - dialyzer
related:
  - success-typing
contrasts_with: []
answers_questions:
  - "What is a Dialyzer PLT?"
  - "How do I build and extend Dialyzer's persistent lookup table?"
---

# Persistent Lookup Table

## Quick Definition

A persistent lookup table (PLT) is Dialyzer's cached compilation of type information about applications and modules, built once and reused to speed up subsequent analyses.

## Core Definition

The first step in using Dialyzer is creating its *persistent lookup table (PLT)* — a compilation of all the details Dialyzer can identify about the applications and modules that are part of the standard Erlang distribution, as well as code outside OTP. Building the PLT takes a while (often under 10 minutes), because it compiles modules and analyzes them; newer Erlang releases parallelize this. The PLT is built with `dialyzer --build_plt --apps ...`, can be extended with `--add_to_plt`, and you can maintain multiple PLTs selected with `--plt` or merge disjoint ones with `--plts` (Chapter 30, "PLTs Are the Best Sandwiches").

## Prerequisites

- **Dialyzer** — The PLT is Dialyzer's prerequisite data structure

## Key Properties

1. A cached compilation of type information about analyzed applications and modules
2. Built once with `dialyzer --build_plt --apps <apps...>`
3. Building is slow (minutes); newer releases (R15B02+) build it in parallel
4. Extendable with `dialyzer --add_to_plt --apps <apps...>`
5. Your own code is added with `-r Directories` (finds `.erl`/`.beam` files compiled with `debug_info`)
6. Multiple PLTs can coexist, selected per command with `--plt Name`
7. Disjoint PLTs (no shared modules) can be merged with `--plts Name1 ... NameN`
8. Warnings about unknown functions during PLT building are harmless — Dialyzer's optimism handles them

## Construction / Recognition

## To Build and Use a PLT

1. Build it: `dialyzer --build_plt --apps erts kernel stdlib crypto mnesia sasl common_test eunit`
2. Add more applications later with `dialyzer --add_to_plt --apps ssl reltool`
3. Add your own code with `-r Directories`
4. Run analyses normally; Dialyzer checks the PLT is up-to-date before proceeding

## Context & Application

The PLT lets Dialyzer avoid recompiling and reanalyzing the standard library on every run. On Windows, building may fail with a message that the `HOME` environment variable must be set, since Dialyzer needs a place to dump the PLT files. Maintaining separate or per-version PLTs is useful for different projects or Erlang versions.

## Examples

**Example** (Chapter 30, "PLTs Are the Best Sandwiches"): `dialyzer --build_plt --apps erts kernel stdlib crypto mnesia sasl common_test eunit` compiles key modules to native code and creates `~/.dialyzer_plt`, emitting harmless "Unknown functions" warnings.

## Relationships

## Builds Upon

- **Dialyzer** — The PLT is the data Dialyzer relies on for analysis

## Related

- **Success typing** — Unknown-function warnings during PLT building are harmless because Dialyzer optimistically assumes any use is valid

## Common Errors

- **Error**: On Windows, building a PLT without `HOME` set
  **Correction**: Set the `HOME` environment variable so Dialyzer knows where to store the PLT

## Common Confusions

- **Confusion**: Treating "Unknown functions" warnings during PLT building as errors
  **Clarification**: They are harmless — Dialyzer handles unknown functions via its optimistic success-typing approach

## Source Reference

Chapter 30: Type Specifications and Dialyzer, section "PLTs Are the Best Sandwiches."

## Verification Notes

- Definition: Direct adaptation from "PLTs Are the Best Sandwiches"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly defined with build commands
- Cross-references: verified against planned cards in this extraction
