---
concept: VM Shutdown (init:stop)
slug: vm-shutdown
category: applications-releases
subcategory: releases
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Release Is the Word"
chapter_number: 21
pdf_page: null
section: "Terminating the VM"
extraction_confidence: high
aliases:
  - "init:stop"
  - "init:stop/0"
  - terminating the VM
prerequisites:
  - supervision-tree
  - otp-application
extends: []
related:
  - supervision-tree
  - erlang-release
contrasts_with: []
answers_questions:
  - "How do I build an Erlang release?"
  - "What is an Erlang release?"
---

# VM Shutdown (init:stop)

## Quick Definition

`init:stop/0` shuts the Erlang VM down in an orderly way — terminating all applications in dependency order and releasing resources like file descriptors and sockets.

## Core Definition

"The perfect function to tear everything down is `init:stop/0`. This function is quite complex, but will take care of terminating our applications in order. It will get rid of file descriptors, sockets, and so on for us" (Ch. 21, "Terminating the VM").

## Prerequisites

- **Supervision tree** — Orderly shutdown relies on every process being supervised.
- **OTP application** — `init:stop` terminates applications.

## Key Properties

1. `init:stop/0` shuts down the whole VM in an orderly manner.
2. It terminates all applications respecting their dependency order.
3. It releases resources — file descriptors, sockets — automatically.
4. Orderly shutdown is "very hard to achieve without having all of your processes being part of the [supervision] tree."
5. It is the right way to make a non-server application exit when its work is done.

## Construction / Recognition

## To Shut Down the VM Cleanly

1. Identify the point where the application's work is complete.
2. Call `init:stop()` there (e.g. in a worker's `terminate` after results are obtained).
3. Rely on the supervision tree so every process terminates in good order.

## Context & Application

In Chapter 21, the `erlcount` release should exit once it has counted regex matches, rather than leaving the VM idle. The fix is to call `init:stop()` from `erlcount_dispatch`'s `terminate` function — "given it's called after we obtain the results." This connects to Chapter 17's point that supervision trees make well-ordered VM shutdown possible (functions like `init:stop/1` walk the top supervisor down).

## Examples

**Example 1** (Ch. 21): `terminate(_Reason, _State, _Data) -> init:stop().` in `erlcount_dispatch` — the release shuts the VM down after producing its results.

## Relationships

## Builds Upon

- **Supervision tree** — Every process being supervised is what makes orderly shutdown work.

## Related

- **erlang-release** — A release often needs to terminate the VM when its job is done.

## Common Errors

- **Error**: Leaving the VM running idle after a batch application finishes.
  **Correction**: Call `init:stop()` once the work is complete to shut down cleanly.

## Common Confusions

- **Confusion**: Thinking `init:stop/0` kills processes abruptly.
  **Clarification**: It terminates applications *in order* through the supervision tree, releasing resources — an orderly shutdown, not a brutal kill.

## Source Reference

Chapter 21: "Release Is the Word," section "Terminating the VM"; orderly-shutdown rationale in Chapter 17, "Supervisor Concepts."

## Verification Notes

- Definition: Direct quote from "Terminating the VM."
- Key Properties: Synthesised from the section and the Chapter 17 shutdown discussion.
- Confidence: HIGH — explicitly defined.
