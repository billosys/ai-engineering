---
concept: No Debug Calls
slug: no-debug-calls-in-production
category: production-ops
subcategory: misc
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Misc"
chapter_number: null
pdf_page: null
section: "No debug calls"
extraction_confidence: high
aliases:
  - "no debug calls"
  - "no io:format in production"
  - "no ct:pal in src"
prerequisites: []
extends: []
related:
  - loud-errors
  - logging-levels
contrasts_with: []
answers_questions:
  - "Can I leave io:format or ct:pal calls in production Erlang code?"
---

# Quick Definition

Production code (modules in `src`) should contain no `io:format` or `ct:pal` calls, nor `lager`/`error_logger` calls used purely for debugging.

# Core Definition

"Unless your project is meant to be run as an escript, there should be no `io:format` nor `ct:pal` calls in your production code (i.e. in the modules inside the `src` folder). Same rule applies for `lager` or `error_logger` calls if they're used just for debugging purposes during test stages" (Inaka, "No debug calls").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. No `io:format` or `ct:pal` in `src/` modules.
2. No `lager`/`error_logger` calls that exist only for debugging.
3. The exception is projects meant to run as an escript.
4. It is a PR-rejection rule under Misc.

# Construction / Recognition

## To Apply

1. Remove debug print/log statements before merging.
2. Keep only logging that is part of the system's real operational behavior.

## To Recognize a Violation

1. An `io:format`/`ct:pal` call (or a debug-only `lager` call) appears in a `src/` module.

# Context & Application

A PR-blocking convention under Misc.

- **Typical contexts**: leftover debugging output from development.
- **Common applications**: stripping `io:format(...)` and `ct:pal(...)` from a function before merge.

# Examples

**Example 1** — bad: a function interleaving `io:format("About to ...")` and `ct:pal("The result was ...")` with its real work.

**Example 2** — good: the same function with the debug calls removed.

# Relationships

## Related

- **Loud errors** — distinguishes legitimate error logging from debug noise.
- **Properly use logging levels** — defines which logging *is* legitimate in production.

# Common Errors

- **Error**: Committing code with `io:format` debugging left in.
  **Correction**: Remove debug output; it harms performance and log clarity.

# Common Confusions

- **Confusion**: Thinking all logging is banned in production.
  **Clarification**: Operational logging is fine; the rule targets *debug-only* prints and logs (and `io:format`/`ct:pal` specifically).

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Misc", guideline "No debug calls".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
