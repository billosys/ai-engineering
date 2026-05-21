---
concept: gen_server terminate Callback
slug: gen-server-terminate-callback
category: otp-behaviours
subcategory: gen-server-callbacks
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "An Introduction to OTP"
chapter_number: 14
pdf_page: null
section: "The terminate Function"
extraction_confidence: high
aliases:
  - "terminate/2"
  - "terminate callback"
prerequisites:
  - gen-server
extends: []
related:
  - gen-server-init-callback
contrasts_with: []
answers_questions:
  - "What does the gen_server terminate/2 callback do?"
  - "When is terminate/2 called?"
---

# gen_server terminate Callback

## Quick Definition

`terminate/2` is the `gen_server` callback that runs cleanup when the server stops. It is the opposite of `init/1` — the function that "locks the door after making sure everyone is gone."

## Core Definition

`terminate/2` "is called whenever one of the three `handle_something` functions returns a tuple of the form `{stop, Reason, NewState}` or `{stop, Reason, Reply, NewState}`." It takes `Reason` and `State`. It is also called "when its parent (the process that spawned it) dies, if and only if the `gen_server` is trapping exits." The chapter notes that "if any reason other than `normal`, `shutdown`, or `{shutdown, Term}` is used when `terminate/2` is called, the OTP framework will see this as a failure and start logging the process's state, reason for failures, last messages received." `terminate/2` "is pretty much the direct opposite of `init/1`, so whatever was done in there should have its opposite in `terminate/2`." Its return value does not matter, since the code stops after it (Hébert, ch. 14, "The terminate Function").

## Prerequisites

- **gen_server** — `terminate/2` is a `gen_server` callback

## Key Properties

1. Runs cleanup when the server is stopping
2. Triggered when a `handle_*` callback returns a `{stop, Reason, ...}` tuple
3. Also triggered when the parent dies, if the `gen_server` is trapping exits
4. Takes `Reason` and `State`
5. Reasons `normal`, `shutdown`, `{shutdown, Term}` are clean; any other reason makes OTP log a failure
6. Should undo whatever `init/1` set up
7. Its return value is irrelevant — execution stops after it

## Construction / Recognition

## To Write terminate/2

1. Define `terminate(Reason, State)` in the callback module
2. Release resources and undo `init/1`'s setup
3. Match clean reasons (`normal`, `shutdown`) separately if cleanup differs
4. Do not rely on the return value — it is ignored

## Examples

> **Kitty server cleanup** (ch. 14): `terminate(normal, Cats) -> [io:format("~p was set free.~n",[C#cat.name]) || C <- Cats], ok.`

## Relationships

## Builds Upon

- **gen_server** — `terminate/2` is one of its callbacks

## Related

- **gen_server init callback** — `terminate/2` is the direct opposite of `init/1`

## Common Errors

- **Error**: Stopping a server with a non-clean reason for an intentional shutdown
  **Correction**: Use `normal` or `shutdown`; other reasons make OTP log it as a failure

## Common Confusions

- **Confusion**: Thinking `terminate/2`'s return value matters
  **Clarification**: It is ignored — the process stops once `terminate/2` returns

## Source Reference

Chapter 14, "An Introduction to OTP," section "Callback to the Future," subsection "The terminate Function."

## Verification Notes

- Trigger conditions and failure-logging rule: directly from ch. 14
- Confidence: HIGH — explicitly described
