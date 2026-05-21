---
concept: The Most Common Erlang Programming Mistakes
slug: common-erlang-programming-mistakes
category: anti-patterns
subcategory: common-mistakes
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "The Most Common Mistakes"
chapter_number: 9
pdf_page: null
section: "9 The Most Common Mistakes"
extraction_confidence: high
aliases:
  - "common mistakes"
  - "most common programming errors"
prerequisites: []
extends: []
related:
  - dont-write-long-functions
  - dont-write-deeply-nested-code
  - use-tagged-return-values
  - function-names
  - variable-names
  - use-process-dictionary-with-care
  - flush-unknown-messages
contrasts_with: []
answers_questions:
  - "What are the most common Erlang programming mistakes?"
---

# Quick Definition

The document's own catalogue of the most common Erlang programming mistakes, each pointing back to the rule that prevents it.

# Core Definition

Section 9 of the Programming Rules collects the most common mistakes the rules exist to prevent. They are: functions that span many pages; functions with deeply nested `if`/`receive`/`case`; badly typed functions (untagged returns); function names that do not reflect what the function does; meaningless variable names; using processes when not needed; badly chosen data structures; bad or absent comments; unindented code; using `put`/`get`; and no control of the message queues.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. It is a recap list, not a new rule — each item cross-references a specific rule.
2. The mistakes span function size, nesting, typing, naming, process use, data structures, comments, indentation, the process dictionary, and message-queue control.
3. It serves as a checklist of the highest-frequency errors.

# Construction / Recognition

## To Apply

1. Use the list as a review checklist for the most frequent errors.

## To Recognize a Candidate

1. Code exhibits any listed mistake — e.g. a multi-page function or meaningless variable names.

# Context & Application

The document's common-mistakes recap (section 9).

- **Typical contexts**: code review and self-review.
- **Common applications**: a quick checklist pass before considering code done.

# Examples

**Example** (from source): the listed mistakes include "Writing functions which span many pages", "Writing badly typed functions", "Function names which do not reflect what the functions do", and "Using put/get".

# Relationships

## Related

- **Don't write very long functions** — addresses multi-page functions.
- **Don't write deeply nested code** — addresses deep `if`/`receive`/`case` nesting.
- **Use tagged return values** — addresses badly typed functions.
- **Function names** — addresses names that misrepresent behavior.
- **Variable names** — addresses meaningless variable names.
- **Use the process dictionary with extreme care** — addresses `put`/`get` misuse.
- **Flush unknown messages** — addresses lack of message-queue control.

# Common Errors

- **Error**: Treating this list as exhaustive guidance on its own.
  **Correction**: Use it as an index — follow through to the specific rule each item references.

# Common Confusions

- **Confusion**: Reading section 9 as a new set of rules.
  **Clarification**: It is a recap — every entry restates the danger a numbered rule already covers.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 9 "The Most Common Mistakes".

# Verification Notes

- Definition source: Direct adaptation of section 9's bullet list.
- Confidence rationale: HIGH — the list is given explicitly in the source.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are cards in this extraction.
