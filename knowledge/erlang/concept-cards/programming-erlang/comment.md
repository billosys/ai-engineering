---
# === CORE IDENTIFICATION ===
concept: Comment
slug: comment

# === CLASSIFICATION ===
category: core-idioms
subcategory: source-formatting
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Basic Concepts"
chapter_number: 3
pdf_page: null
section: "Evaluating Commands in the Shell"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - percent comment
  - "%"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - module
  - erlang-shell
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a comment in Erlang?"
---

# Quick Definition

A comment in Erlang begins with a percent sign (`%`) and runs to the end of the line. Everything from the `%` onward is ignored by the shell and the compiler.

# Core Definition

"In line 2, the percent (%) character indicates the start of a comment. All the text from the percent sign to the end of line is treated as a comment and is ignored by the shell and the Erlang compiler" (Chapter 3, "Evaluating Commands in the Shell"). A comment may follow code on the same line — the example `X + 20. % and this is a comment` shows an end-of-line comment. Comments are line comments only; there is no block-comment form. The source also shows function-level commentary used to annotate code, e.g. `%% wait for a command` inside the file-server loop (Chapter 2).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A comment starts with the percent sign `%`.
2. It extends from the `%` to the end of the line.
3. Text in a comment is ignored by both the shell and the compiler.
4. A comment may appear at the start of a line or after code on the same line.
5. Erlang has only line comments — there is no block-comment syntax.

# Construction / Recognition

## To Write a Comment:
1. Type `%` followed by the comment text.
2. Everything up to the end of the line is the comment.
3. Place it on its own line or after code on a line.

## To Recognize It:
1. Text following a `%` up to the line's end.

# Context & Application

- **Typical contexts**: Documenting modules, functions, and individual lines of code.
- **Common applications**: A `%% wait for a command` note above a code block; an inline `% explanation` after an expression.
- **Historical/stylistic notes**: Erlang convention uses comment depth to signal scope — `%%%` for module-level, `%%` for function-level, `%` for inline commentary — though Chapter 3 introduces only the basic `%` rule.

# Examples

**Example 1** (Chapter 3, "Evaluating Commands in the Shell"): `2> X + 20. % and this is a comment` — the text after `%` is ignored; the shell still evaluates `X + 20` to `40`.

**Example 2** (Chapter 2, "The File Server Process"): `%% wait for a command` appears as a function-level comment annotating the `loop/1` skeleton.

# Relationships

## Builds Upon
- This is a foundational concept and does not build upon another card in this source.

## Enables
- Self-documenting modules and functions.

## Related
- **Module** — Comments document modules and their functions.
- **Erlang shell** — Comments are also ignored when typed at the shell prompt.

## Contrasts With
- No directly contrasting concept in these chapters.

# Common Errors

- **Error**: Expecting a block-comment syntax to comment out many lines at once.
  **Correction**: Erlang has only line comments; prefix each line with `%`.

- **Error**: Putting code after a `%` on the same line and expecting it to run.
  **Correction**: Everything after `%` is ignored to end of line; put live code before the `%`.

# Common Confusions

- **Confusion**: Thinking `%%` or `%%%` are a different comment mechanism.
  **Clarification**: Any run of `%` starts a comment; multiple `%` is a *convention* for indicating scope, not separate syntax.

# Source Reference

"Programming Erlang, Second Edition," Chapter 3: Basic Concepts, section "Evaluating Commands in the Shell"; Chapter 2: A Whirlwind Tour of Erlang, "The File Server Process." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotation from Chapter 3, "Evaluating Commands in the Shell."
- Confidence rationale: HIGH — the `%` comment rule is explicitly stated.
- Uncertainties: The `%%`/`%%%` scope convention is noted from the taxonomy's notation conventions; Chapter 3 itself states only the basic `%` rule.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
