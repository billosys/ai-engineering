---
concept: Comment Conventions
slug: comment-conventions
category: documentation
subcategory: documenting-code
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Documenting Code"
chapter_number: 8
pdf_page: null
section: "8.5 Comments"
extraction_confidence: high
aliases:
  - "comments"
  - "comment levels"
  - "percent comment conventions"
prerequisites: []
extends: []
related:
  - comment-each-function
  - file-header-description
contrasts_with: []
answers_questions:
  - "What do %, %%, and %%% mean in Erlang comments?"
  - "How should comments be written and placed?"
---

# Quick Definition

Comments should be clear, concise, current, and in English; the number of percent signs encodes the comment's scope — `%%%` module, `%%` function, `%` code.

# Core Definition

"Comments should be clear and concise and avoid unnecessary wordiness" (Programming Rules, 8.5), kept up to date with the code, and written in English. The scope conventions: comments about the module have no indentation and start with `%%%`; comments about a function have no indentation and start with `%%`; comments within Erlang code start with `%`. A code comment on its own line is indented as Erlang code and placed above the statement it refers to; if it fits on the statement's own line, that is preferred.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Comments are clear, concise, current, and in English.
2. `%%%` — module-level comments, no indentation.
3. `%%` — function-level comments, no indentation.
4. `%` — code-level comments, indented as code, placed above (or on) the statement.

# Construction / Recognition

## To Apply

1. Use `%%%`, `%%`, `%` according to module/function/code scope.
2. Place an own-line code comment above its statement, indented as code; prefer same-line if it fits.

## To Recognize a Violation

1. A comment uses a percent-count that does not match its scope, or is stale, wordy, or not in English.

# Context & Application

A core documentation rule (section 8).

- **Typical contexts**: every comment in every module.
- **Common applications**: `%%% File header`, `%% function comment`, `%` inline note.

# Examples

**Example** (from source): a `%% Comment about function` above the function, a `% Comment at end of line`, and a `% Comment about complicated_stmnt` placed above the statement at the code's indentation.

# Relationships

## Related

- **Comment each function** — `%%` function comments follow this convention.
- **File Header, description** — the module description uses `%%%` comments.

# Common Errors

- **Error**: Using the wrong percent-count for a comment's scope, or letting comments go stale.
  **Correction**: Match `%`/`%%`/`%%%` to scope; keep comments current with the code.

# Common Confusions

- **Confusion**: Thinking the percent-count is arbitrary.
  **Clarification**: It encodes scope — `%%%` module, `%%` function, `%` code — and aids searching.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 8.5 "Comments".

# Verification Notes

- Definition source: Direct adaptation of section 8.5.
- Confidence rationale: HIGH — the rule is stated explicitly with an example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
