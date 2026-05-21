---
# === CORE IDENTIFICATION ===
concept: Compiled Module vs. Shell Evaluation
slug: compiled-module-vs-shell

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
section: "2.3.7 Compiled modules versus evaluation in the shell"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - shell interpretation
  - interpreted vs compiled code

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-shell
  - compiling-modules
extends: []
related:
  - beam-file
  - erlang-module
contrasts_with:
  - erlang-shell
  - beam-file

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does shell evaluation differ from running compiled code?"
  - "Why can't you use declarations in the shell?"
  - "Why should you never benchmark code in the shell?"
---

# Quick Definition

Code in a compiled module is byte-code compiled together in one context; code in the shell is interpreted on the fly as one-off expressions. The compiled version is the gold standard.

# Core Definition

"There is a difference between what happens with expressions that you enter in the Erlang shell and code that you put in a module" (Chapter 2, section 2.3.7). A `.beam` file is an efficient, ready-to-deploy representation; all its code was compiled together at the same time, in the same context, which is what makes module-wide declarations (like `-export` and `-module`) meaningful. Shell code "consists basically of one-off expressions, to be forgotten fairly soon" — it is never part of any module, so declarations cannot be used in the shell. The shell parses and interprets expressions on the fly, which is several orders of magnitude slower than compiled code, though this rarely matters because the shell usually just calls into already-compiled functions. The book stresses: "never measure on code that is interpreted by the shell." In rare corner cases shell-interpreted code may behave slightly differently from the same code compiled in a module; in such cases the compiled version is the gold standard.

# Prerequisites

- **Erlang shell** — one side of the contrast is shell evaluation.
- **Compiling and loading modules** — the other side is compiled module code.

# Key Properties

1. Compiled module code is byte-code compiled together in one context.
2. Shell code is one-off expressions interpreted on the fly.
3. Declarations (`-module`, `-export`) work only in modules — there is no shell module context.
4. Shell interpretation is several orders of magnitude slower than compiled code.
5. The slowness rarely matters because the shell mostly calls into compiled functions.
6. In rare corner cases shell behavior differs slightly; the compiled version is authoritative.

# Construction / Recognition

## To Identify/Recognize:
1. Module code: declarations allowed, compiled to `.beam`, fast.
2. Shell code: expressions only, interpreted, slower, no declarations.
3. Code that runs entirely in the shell interpreter (list comprehensions, recursive funs) is notably slow.

# Context & Application

- **Typical contexts**: Deciding where to run code; benchmarking.
- **Common applications**: Quick experiments in the shell; production code in compiled modules.
- **Historical/stylistic notes**: For sane benchmark numbers, write code as modules, not as shell one-liners.

# Examples

**Example 1** (section 2.3.7): When you write `lists:reverse([1,2,3])` in the shell, the shell only prepares the list and passes it to the already-compiled `reverse` function, which runs at normal speed.

**Example 2** (section 2.3.7): Code written entirely with list comprehensions or recursive funs can be evaluated start-to-end by the shell's interpreter and is notably slower than the compiled equivalent.

# Relationships

## Builds Upon
- **Erlang shell** and **Compiling and loading modules** — the two sides being contrasted.

## Enables
- Sound benchmarking practice (measure compiled modules, not the shell).

## Related
- **BEAM file** — the compiled, efficient module form.
- **Erlang module** — declarations are only meaningful in a module context.

## Contrasts With
- **Erlang shell** — interpreted, one-off, no declarations.
- **BEAM file** — compiled, efficient, self-contained, supports declarations.

# Common Errors

- **Error**: Benchmarking code by running it in the shell.
  **Correction**: Never measure shell-interpreted code; write benchmarks as compiled modules.

- **Error**: Trying to use `-module` or `-export` in the shell.
  **Correction**: Declarations need a module context, which the shell does not have.

# Common Confusions

- **Confusion**: Assuming the shell runs code at the same speed as a compiled module.
  **Clarification**: Shell interpretation is orders of magnitude slower; it just usually delegates to compiled functions so the difference is unnoticeable.

# Source Reference

Chapter 2: Erlang language essentials, section 2.3.7 "Compiled modules versus evaluation in the shell."

# Verification Notes

- Definition source: Direct adaptation from section 2.3.7.
- Confidence rationale: HIGH — the distinction is explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
