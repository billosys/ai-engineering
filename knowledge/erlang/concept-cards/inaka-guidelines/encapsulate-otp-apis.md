---
concept: Encapsulate OTP Server APIs
slug: encapsulate-otp-apis
category: otp-behaviours
subcategory: misc
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Misc"
chapter_number: null
pdf_page: null
section: "Encapsulate OTP server APIs"
extraction_confidence: high
aliases:
  - "OTP API encapsulation"
  - "no raw gen_server calls"
  - "API functions for gen_server"
prerequisites:
  - use-behaviours
extends: []
related:
  - avoid-dynamic-calls
  - dont-use-export-all
  - write-function-specs
  - tagged-tuple-messages
contrasts_with: []
answers_questions:
  - "What does \"encapsulate OTP server APIs\" mean?"
  - "Why shouldn't I make raw gen_server calls across module boundaries?"
---

# Quick Definition

Never make raw `gen_server` calls (or other OTP construct calls) across module boundaries; wrap each in an API function in the module that implements the corresponding callback.

# Core Definition

"Never do raw `gen_server` calls across module boundaries; the call should be encapsulated in an API function in the same module that implements the corresponding `handle_call` function. The same goes for other such OTP constructs (`gen_server` casts, `gen_fsm` events, etc)" (Inaka, "Encapsulate OTP server APIs"). Each `gen_server:call`/`cast` lives next to the `handle_call`/`handle_cast` it targets, behind a named API function.

# Prerequisites

- **Use behaviours** — this rule governs how callers interact with behaviour modules.

# Key Properties

1. `gen_server:call`/`cast` and similar OTP calls are not made from other modules.
2. Each such call is wrapped in an API function in the module that implements the matching callback.
3. The API function's name (and its `-spec`) make the message's origin and contract searchable.
4. Encapsulation lets the underlying message format — even the behaviour itself — change without touching callers.

# Construction / Recognition

## To Apply

1. For each `handle_call`/`handle_cast` clause, write a public API function in the same module that issues the call.
2. Have other modules invoke that API function, never the raw OTP call.

## To Recognize a Violation

1. A module issues `gen_server:call(SomeOtherModule, ...)` or `gen_fsm:send_all_state_event(some_fsm, ...)` for a behaviour implemented elsewhere.

# Context & Application

A PR-blocking convention under Misc.

- **Typical contexts**: `gen_server`/`gen_statem` modules and their callers.
- **Common applications**: a `good/0` API function calling `gen_server:call(?MODULE, do_good)` inside the implementing module.

# Examples

**Example 1** — good: `good() -> gen_server:call(?MODULE, do_good)` — an API call that encapsulates the local `gen_server`.

**Example 2** — bad: `bad() -> gen_fsm:send_all_state_event(some_fsm, make_everyone_sad)` — an event sent to a process implemented in another module.

# Relationships

## Builds Upon

- **Use behaviours** — encapsulation governs how behaviour modules are consumed.

## Related

- **Avoid dynamic calls** — both improve traceability and Dialyzer coverage.
- **Don't export_all** — both keep a deliberate, minimal public surface.
- **Write function specs** — the API functions carry the type specs that Dialyzer checks.
- **Use atoms or tagged tuples for messages** — the encapsulated messages still follow message-tagging rules.

# Common Errors

- **Error**: Calling `gen_server:call/2` directly on another module's server.
  **Correction**: Add and call an API function in that server's own module.

# Common Confusions

- **Confusion**: Thinking encapsulation is just tidiness.
  **Clarification**: It localizes message knowledge so the format — or even a `gen_server`→`gen_fsm` switch — can change with one-module edits.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Misc", guideline "Encapsulate OTP server APIs".

# Verification Notes

- Definition source: Direct quote plus paraphrase of the reasoning.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
