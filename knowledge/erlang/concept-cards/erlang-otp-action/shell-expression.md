---
# === CORE IDENTIFICATION ===
concept: Shell Expression
slug: shell-expression

# === CLASSIFICATION ===
category: tooling
subcategory: interactive-environment
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.1.2 Entering expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - entering expressions
  - shell prompt input

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-shell
extends: []
related:
  - shell-functions
  - erlang-term
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What do you enter at the Erlang shell prompt?"
  - "Why must a shell expression end with a period?"
  - "How do you refer to previous shell results?"
---

# Quick Definition

A shell expression is what you type at the Erlang shell prompt: not a command, but an expression that always has a result, which the shell evaluates, prints, and remembers.

# Core Definition

"What you enter at the shell prompt aren't commands as such, but *expressions*, the difference being that an expression always has a *result*. When the expression has been evaluated, the shell prints the result" (Chapter 2, section 2.1.2). The shell also remembers each result so it can be referred to later using `v(1)`, `v(2)`, and so on. Every expression must be terminated with a period (full stop) before pressing Enter; the period tells the shell it has seen the end of the expression. If the period is omitted, the shell keeps prompting for more characters (without incrementing the prompt number).

# Prerequisites

- **Erlang shell** — shell expressions are entered into the shell.

# Key Properties

1. Shell input is expressions, not commands.
2. Every expression has a result, which the shell prints.
3. An expression must be terminated with a period before Enter.
4. Omitting the period makes the shell prompt for more input without incrementing the prompt.
5. Results are remembered and retrievable with `v(N)`.
6. The shell by default keeps the latest 20 results.

# Construction / Recognition

## To Construct/Create:
1. Type an Erlang expression at the numbered prompt.
2. End it with a period (`.`).
3. Press Enter; the shell evaluates and prints the result.
4. Refer back to result number N with `v(N)`.

# Context & Application

- **Typical contexts**: Interactive experimentation and incremental development.
- **Common applications**: Trying arithmetic, building terms, calling library functions.
- **Historical/stylistic notes**: The period requirement mirrors the period that terminates function definitions and declarations in modules.

# Examples

**Example 1** (section 2.1.2): Typing `42.` and pressing Enter evaluates the expression `42`, prints `42`, and shows the next prompt `2>`.

**Example 2** (section 2.1.2): An expression can be split over lines without a period — `12`, then `+ 5`, then `.` — yielding `17`; and `v(2) + v(3)` reuses earlier results.

# Relationships

## Builds Upon
- **Erlang shell** — expressions are the unit of shell interaction.

## Enables
- Interactive evaluation and result reuse via `v(N)`.

## Related
- **Shell functions** — special functions like `v(N)` operate on shell expressions and results.
- **Erlang term** — the result of a shell expression is a term.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Pressing Enter without a terminating period and thinking the shell has hung.
  **Correction**: The shell is waiting for the end of the expression; type a period and press Enter.

# Common Confusions

- **Confusion**: Treating shell input as commands.
  **Clarification**: Shell input is expressions; each always produces and prints a result.

# Source Reference

Chapter 2: Erlang language essentials, section 2.1.2 "Entering expressions," including the "Ending with a period" subsection.

# Verification Notes

- Definition source: Direct adaptation from section 2.1.2.
- Confidence rationale: HIGH — the expression/result behavior is explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
