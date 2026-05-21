---
concept: gen_server code_change Callback
slug: gen-server-code-change-callback
category: otp-behaviours
subcategory: gen-server-callbacks
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "An Introduction to OTP"
chapter_number: 14
pdf_page: null
section: "The code_change Function"
extraction_confidence: high
aliases:
  - "code_change/3"
  - "code_change callback"
prerequisites:
  - gen-server
  - hot-code-loading
extends: []
related:
  - hot-code-loading
contrasts_with: []
answers_questions:
  - "What does the gen_server code_change/3 callback do?"
  - "How does a gen_server transform its state during a code upgrade?"
---

# gen_server code_change Callback

## Quick Definition

`code_change/3` is the `gen_server` callback that lets a server transform its state when its code is upgraded or downgraded, returning the converted state as `{ok, NewState}`.

## Core Definition

`code_change/3` "lets you upgrade code. It takes the form `code_change(PreviousVersion, State, Extra)`." `PreviousVersion` "is either the version term itself in the case of an upgrade or `{down, Version}` in the case of a downgrade (just reloading older code). The `State` variable holds all of the current server state so you can convert it." The chapter gives a concrete motivation: if a server stored data in an orddict that has become too slow and is being replaced by a dict, "the conversion from one data structure to the other can be done in there, safely. All we need to do is return the new state with `{ok, NewState}`." This avoids the process crashing on the next call into the new code (Hébert, ch. 14, "The code_change Function").

## Prerequisites

- **gen_server** — `code_change/3` is a `gen_server` callback
- **Hot code loading** — `code_change/3` is the formalized state-transformation step of a code upgrade

## Key Properties

1. Form: `code_change(PreviousVersion, State, Extra)`
2. `PreviousVersion` is the version term for an upgrade, or `{down, Version}` for a downgrade
3. `State` is the current server state, available for conversion
4. Returns `{ok, NewState}` — the state adapted to the new code
5. Used to convert data structures safely between code versions (e.g. orddict → dict)
6. Prevents the process crashing when the next call hits the new code

## Construction / Recognition

## To Write code_change/3

1. Define `code_change(OldVsn, State, Extra)` in the callback module
2. Transform `State` to match the new code's expectations
3. Return `{ok, NewState}`
4. If no change is needed, return `{ok, State}` unchanged (the callback is still required by the behaviour)

## Examples

> **No-op upgrade** (ch. 14): `code_change(_OldVsn, State, _Extra) -> {ok, State}.` — "No change planned. The function is there for the behavior."
>
> **Data-structure conversion** (ch. 14): converting a server's orddict state into a dict inside `code_change/3` so the process does not crash on the next call.

## Relationships

## Builds Upon

- **gen_server** — `code_change/3` is one of its callbacks
- **Hot code loading** — `code_change/3` is the OTP-formalized state-conversion step

## Common Errors

- **Error**: Omitting `code_change/3` because no upgrade is planned
  **Correction**: The behaviour requires it; provide a no-op `{ok, State}` version

## Common Confusions

- **Confusion**: Thinking `code_change/3` loads the new code itself
  **Clarification**: The code server loads new code; `code_change/3` only transforms the *state* for it

## Source Reference

Chapter 14, "An Introduction to OTP," section "Callback to the Future," subsection "The code_change Function."

## Verification Notes

- Signature, upgrade/downgrade, orddict→dict example: directly from ch. 14
- Confidence: HIGH — explicitly described
