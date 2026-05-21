---
concept: Comment Levels
slug: comment-levels
category: documentation
subcategory: suggestions
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Suggestions & Great Ideas"
chapter_number: null
pdf_page: null
section: "Comment levels"
extraction_confidence: high
aliases:
  - "comment levels"
  - "percent comment convention"
  - "%%% %% % comments"
prerequisites: []
extends: []
related:
  - group-functions-logically
contrasts_with: []
answers_questions:
  - "What do %, %%, and %%% mean in Erlang comments?"
  - "What distinguishes the three comment levels?"
---

# Quick Definition

Module-level comments use `%%%`, function-level comments use `%%`, and inline code comments use `%`.

# Core Definition

"Module comments go with `%%%`, function comments with `%%`, and code comments with `%`" (Inaka, "Comment levels"). The number of percent signs encodes the scope of the comment.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `%%%` — module-level commentary (file header, big-picture).
2. `%%` — function-level commentary (immediately above a function).
3. `%` — inline / end-of-line code comments.
4. This is a "Suggestion & Great Idea" — advisory, not a PR-blocking rule.

# Construction / Recognition

## To Apply

1. Write the module's header/big-picture comment with `%%%`.
2. Write a function's doc comment with `%%`, directly above it.
3. Write in-body and end-of-line comments with `%`.

## To Recognize a Candidate

1. A comment uses a percent-count that does not match its scope (e.g., `%%%` on an in-body comment).

# Context & Application

A "Suggestion & Great Idea" — advisory; does not by itself block a PR.

- **Typical contexts**: every comment in every module.
- **Common applications**: a `%%% @doc` module header, a `%% @doc` function comment, a `%` inline note.

# Examples

**Example 1** — bad: `% @doc` used for a function comment, or `%%%` used for an in-body comment.

**Example 2** — good: `%%% @doc` for the module, `%% @doc` for a function, `%` for inline notes.

# Relationships

## Related

- **Group functions logically** — both shape how a module reads top-to-bottom.

# Common Errors

- **Error**: Using `%` for a function's doc comment.
  **Correction**: Use `%%` directly above the function; reserve `%` for code-level comments.

# Common Confusions

- **Confusion**: Thinking the percent count is arbitrary.
  **Clarification**: It encodes scope — more signs, broader scope — and makes comments greppable (e.g., search `%% @`).

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Suggestions & Great Ideas", guideline "Comment levels".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit suggestion with a bad/good example.
- Uncertainties: None.
- Cross-reference status: `group-functions-logically` is a planned card in this extraction.
