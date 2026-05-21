---
concept: Properly Use Logging Levels
slug: logging-levels
category: production-ops
subcategory: tools
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Tools"
chapter_number: null
pdf_page: null
section: "Properly use logging levels"
extraction_confidence: high
aliases:
  - "log levels"
  - "lager logging levels"
  - "severity levels"
prerequisites: []
extends: []
related:
  - loud-errors
  - no-debug-calls-in-production
contrasts_with: []
answers_questions:
  - "How should I choose a lager logging level?"
  - "What do the different log severity levels mean?"
---

# Quick Definition

When using `lager`, choose the logging level by the specific meaning the guideline assigns to each level.

# Core Definition

Per Inaka's "Properly use logging levels" guideline, `lager` levels carry these meanings: `debug` — very low-level info that may flood the screen; `info` — the system's life in some detail, events that happen usually but not constantly; `notice` — meaningful events worth noticing (supervisor/important `gen_server` startup or termination); `warning` — handled errors where the system keeps working but something unusual happened; `error` — something bad and unexpected, usually an exception (log the stack trace here); `critical` — the system or a part of it crashed and someone must act; `alert` and `emergency` — no rule given for when to use them.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Each level has an assigned operational meaning.
2. `error` is the level at which stack traces are logged.
3. `info` should leave the console usable; `debug` may flood it.
4. `alert` and `emergency` have no defined usage rule in the source.

# Construction / Recognition

## To Apply

1. Match the event's operational severity to the level definitions above.
2. Log stack traces at `error`; reserve `critical` for actual crashes needing action.

## To Recognize a Violation

1. A routine event is logged at `error`, or a crash needing action is logged at `info`.

# Context & Application

A PR-blocking convention under Tools; applies to projects using `lager`.

- **Typical contexts**: operational logging across an application.
- **Common applications**: supervisor startup at `notice`, a handled-but-unusual condition at `warning`.

# Examples

The source provides the level definitions themselves as its content; it gives no separate code example for this guideline.

# Relationships

## Related

- **Loud errors** — specifies that caught errors are logged (this card specifies at which level).
- **No debug calls** — debug-only logging does not belong in production `src/` code.

# Common Errors

- **Error**: Logging ordinary lifecycle events at `error`.
  **Correction**: Use `info`/`notice` for normal life; reserve `error` for unexpected failures.

# Common Confusions

- **Confusion**: Expecting a rule for `alert` and `emergency`.
  **Clarification**: The source explicitly states there is no rule for when to use those two levels.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Tools", guideline "Properly use logging levels".

# Verification Notes

- Definition source: Direct adaptation of the guideline's level-by-level "Meanings" list.
- Confidence rationale: HIGH — the source enumerates each level explicitly; no code example exists (noted above).
- Uncertainties: `alert`/`emergency` deliberately undefined by the source.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
