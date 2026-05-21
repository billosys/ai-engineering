---
# === CORE IDENTIFICATION ===
concept: Erlang Comment
slug: erlang-comment

# === CLASSIFICATION ===
category: core-idioms
subcategory: source-style
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.3.4 Creating modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - comment
  - source code comment

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you write a comment in Erlang?"
  - "What is the comment-character convention in Erlang?"
---

# Quick Definition

A comment in Erlang is introduced with the `%` character and runs to the end of the line. There is only one kind of comment.

# Core Definition

"There is only one kind of source code comment in Erlang. These comments are introduced with the `%` character and go on until the end of the line" (Chapter 2, section 2.3.4). A `%` inside a quoted string or atom does not begin a comment. By style convention, comments that follow code on the same line use a single `%`, while comments on lines of their own typically start with two `%%` characters; some people use three `%%%` for whole-file-level comments. Syntax-aware editors such as Emacs and erlIDE use the number of `%` characters to indent comments automatically.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. There is only one kind of comment in Erlang.
2. A comment starts with `%` and runs to the end of the line.
3. A `%` inside a quoted string or atom does not start a comment.
4. By convention: `%` for end-of-line comments, `%%` for standalone lines, `%%%` for file-level comments.
5. Syntax-aware editors indent comments based on the number of leading `%` characters.

# Construction / Recognition

## To Construct/Create:
1. Write `%` and then the comment text, to the end of the line.
2. Use `%` after code, `%%` on its own line, `%%%` for file-level commentary.

# Context & Application

- **Typical contexts**: Documenting Erlang source code.
- **Common applications**: Module headers, function-level commentary, inline notes.
- **Historical/stylistic notes**: The three-level convention (`%`, `%%`, `%%%`) is widely followed and supported by editors.

# Examples

**Example 1** (section 2.3.4): `% This is a comment and it ends here.` — a standard comment; `"This % does not begin a comment"` shows a `%` inside a string is not a comment.

**Example 2** (section 2.3.4): `frotz() -> blah.    % this is a comment on a line of code` uses a single `%` for an end-of-line comment, while standalone comment lines use `%%`.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- Documented, readable Erlang source.

## Related
- **Erlang module** — the first item in a module may be comments before the module declaration.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Expecting block-comment syntax.
  **Correction**: Erlang has only one comment form — `%` to end of line; longer comments need multiple lines.

# Common Confusions

- **Confusion**: Thinking a `%` always starts a comment.
  **Clarification**: A `%` within a quoted string or atom is just a character, not a comment start.

# Source Reference

Chapter 2: Erlang language essentials, section 2.3.4 "Creating modules," "Comments" subsection.

# Verification Notes

- Definition source: Direct adaptation from section 2.3.4.
- Confidence rationale: HIGH — comments and the `%`/`%%`/`%%%` convention are explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
