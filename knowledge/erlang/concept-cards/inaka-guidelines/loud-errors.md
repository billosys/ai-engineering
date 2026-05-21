---
concept: Loud Errors
slug: loud-errors
category: error-handling
subcategory: tools
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Tools"
chapter_number: null
pdf_page: null
section: "Loud errors"
extraction_confidence: high
aliases:
  - "loud errors"
  - "log the stack trace"
  - "don't swallow errors"
prerequisites: []
extends: []
related:
  - logging-levels
  - no-debug-calls-in-production
  - avoid-case-catch
contrasts_with: []
answers_questions:
  - "Should I log errors even when I handle them?"
---

# Quick Definition

Don't let errors and exceptions go unlogged — even when you handle them, write a log line with the stack trace.

# Core Definition

"Don't let errors and exceptions go unlogged. Even when you handle them, write a log line with the stack trace" (Inaka, "Loud errors"). A caught error is logged with enough context — including the stack trace — that someone reading the logs can understand what happened.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Caught errors are logged, not silently swallowed.
2. The log line includes the stack trace and relevant arguments.
3. Re-raising via `exit` is acceptable; quietly returning `{error, Error}` or re-`throw`ing without logging is not.
4. It is a PR-rejection rule under Tools.

# Construction / Recognition

## To Apply

1. In a `catch` clause, log the error, the arguments, and the stack trace before returning.
2. Or let the error propagate via `exit` so it is logged by the runtime.

## To Recognize a Violation

1. A `catch` clause returns or re-throws `{error, Error}` with no log line.

# Context & Application

A PR-blocking convention under Tools.

- **Typical contexts**: `try...catch` blocks around risky operations.
- **Common applications**: a `lager:error("Error here: ~p~n Arguments: ~p~n Stack: ~p", [...])` call inside the `catch` clause.

# Examples

**Example 1** — bad: a `catch` clause that simply returns `{error, Error}` (or re-throws it) with no logging.

**Example 2** — good1: the `catch` clause calls `lager:error/2` with the error, arguments, and stack trace, then returns `{error, Error}`.

**Example 3** — good2: the `catch` clause `exit({error, Error})`, letting the runtime surface it.

# Relationships

## Related

- **Properly use logging levels** — defines which level (`error`) such logs use.
- **No debug calls** — distinguishes legitimate error logging from debug noise.
- **Don't use case catch** — both concern handling errors deliberately.

# Common Errors

- **Error**: Catching an exception and returning `{error, Error}` silently.
  **Correction**: Log the error with its stack trace before returning.

# Common Confusions

- **Confusion**: Thinking handling an error means it need not be logged.
  **Clarification**: Handling and logging are separate duties — a handled error still needs a trace for whoever watches the logs.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Tools", guideline "Loud errors".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with four labelled examples.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
