---
concept: Complex Termination (prep_stop)
slug: complex-termination
category: applications-releases
subcategory: applications
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Count of Applications"
chapter_number: 20
pdf_page: null
section: "Complex Terminations"
extraction_confidence: high
aliases:
  - "prep_stop"
  - "prep_stop/1"
  - complex termination
prerequisites:
  - application-callback-module
  - application-behaviour
extends: []
related:
  - application-callback-module
  - application-start-and-stop
contrasts_with: []
answers_questions:
  - "How do I structure an OTP application?"
---

# Complex Termination (prep_stop)

## Quick Definition

`prep_stop/1` is an optional application callback that runs *before* `stop/1`, while the application is still alive — letting you clean up things that must be done before the app is gone.

## Core Definition

"The `stop/1` function from the application callback module might not be enough, especially since it is called *after* the application has already terminated. ... Just add a function `prep_stop(State)` to your application callback module. `State` will be the state returned by your `start/2` function, and whatever `prep_stop/1` returns will be passed to `stop/1`" (Ch. 20, "Complex Terminations").

## Prerequisites

- **Application callback module** — `prep_stop/1` is an optional callback there.
- **Application behaviour** — It is part of the application behaviour's contract.

## Key Properties

1. `prep_stop/1` is optional; add it only when extra teardown is needed.
2. It receives the `State` returned by `start/2`.
3. Its return value is passed on to `stop/1`.
4. It "inserts itself between `start/2` and `stop/1`."
5. Crucially, it runs *while the application is still alive*, just before shutdown.
6. `stop/1`, by contrast, runs *after* the application has already terminated.

## Construction / Recognition

## To Use prep_stop

1. Identify cleanup work that must happen while the app is still running (e.g. notifying a service, draining work).
2. Add `prep_stop(State)` to the callback module.
3. Do the live-cleanup work; return whatever `stop/1` will need.
4. Implement `stop/1` to do the remaining post-shutdown cleanup.

## Context & Application

The book introduces `prep_stop/1` as the answer to "What do we do if we need to clean up things before the application is actually gone?" The `erlcount` example does not need it, but the book notes "for your own code, you will know when you need to use this kind of callback." Typical uses: gracefully closing external connections or flushing buffers while dependent processes are still up.

## Examples

**Example 1** (Ch. 20): The book describes `prep_stop/1` abstractly — it technically inserts itself between `start/2` and `stop/1` — and notes `erlcount` does not require it.

## Relationships

## Builds Upon

- **Application callback module** — `prep_stop/1` is an additional callback in that module.

## Related

- **application-behaviour** — Defines the optional `prep_stop/1` callback.
- **application-start-and-stop** — `prep_stop/1` participates in the stop sequence.

## Common Errors

- **Error**: Putting live-teardown logic in `stop/1`.
  **Correction**: `stop/1` runs after the app is already gone; put pre-shutdown work in `prep_stop/1`.

## Common Confusions

- **Confusion**: Thinking `stop/1` runs while the application is still alive.
  **Clarification**: `stop/1` runs *after* termination and does only final cleanup; `prep_stop/1` is the callback that runs before shutdown.

## Source Reference

Chapter 20: "The Count of Applications," section "Complex Terminations."

## Verification Notes

- Definition: Direct quotes from "Complex Terminations."
- Key Properties: Adapted from the section.
- Confidence: HIGH — explicitly defined.
