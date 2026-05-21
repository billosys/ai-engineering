---
concept: gen_server init Callback
slug: gen-server-init-callback
category: otp-behaviours
subcategory: gen-server-callbacks
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "An Introduction to OTP"
chapter_number: 14
pdf_page: null
section: "The init Function"
extraction_confidence: high
aliases:
  - "init/1"
  - "init callback"
prerequisites:
  - gen-server
  - otp-callback-module
extends: []
related:
  - gen-server-terminate-callback
contrasts_with: []
answers_questions:
  - "What does the gen_server init/1 callback do?"
  - "What can init/1 return?"
---

# gen_server init Callback

## Quick Definition

`init/1` is the `gen_server` callback that builds the server's initial state and performs one-time setup. It runs while the spawning process is blocked, and returns an `{ok, State}` tuple (or `stop`/`ignore`).

## Core Definition

`init/1` "is used to initialize the server's state and do all of these one-time tasks that the server will depend on." It can return `{ok, State}`, `{ok, State, TimeOut}`, `{ok, State, hibernate}`, `{stop, Reason}`, or `ignore`. The plain `{ok, State}` passes `State` "directly to the main loop of the process as the state to keep later on." Adding a `TimeOut` makes the server receive the atom `timeout` (handled by `handle_info/2`) if no message arrives by the deadline — "seldom used in production." Adding `hibernate` shrinks the process's memory at the cost of some CPU. `{stop, Reason}` signals that initialization failed. Importantly, "while `init/1` is running, execution is blocked in the process that spawned the server," because the spawner waits for a "ready" message that `gen_server` sends automatically (Hébert, ch. 14, "The init Function").

## Prerequisites

- **gen_server** — `init/1` is a `gen_server` callback
- **OTP callback module** — `init/1` lives in the callback module

## Key Properties

1. Builds the initial server state and does one-time setup
2. Return values: `{ok, State}`, `{ok, State, TimeOut}`, `{ok, State, hibernate}`, `{stop, Reason}`, `ignore`
3. `State` from `{ok, State}` is passed to the server's main loop
4. A `TimeOut` triggers a `timeout` message to `handle_info/2` if no message arrives in time
5. `hibernate` compacts process memory until the next message
6. `{stop, Reason}` indicates initialization failed
7. The spawning process is blocked until `init/1` finishes (it waits for an automatic "ready" message)

## Construction / Recognition

## To Write init/1

1. Define `init(Args)` in the callback module
2. Perform any one-time setup the server needs
3. Return `{ok, InitialState}` in the normal case
4. Return `{stop, Reason}` if setup cannot succeed
5. Add `TimeOut` or `hibernate` only when genuinely needed

## Examples

> **Simple init** (ch. 14): `init([]) -> {ok, []}.` for the kitty `gen_server`.
>
> **Blocking note** (ch. 14): "while `init/1` is running, execution is blocked in the process that spawned the server."

## Relationships

## Builds Upon

- **gen_server** — `init/1` is one of its callbacks
- **OTP callback module** — `init/1` is supplied by the user module

## Related

- **gen_server terminate callback** — `terminate/2` is "pretty much the direct opposite of `init/1`"

## Common Errors

- **Error**: Doing slow work in `init/1`
  **Correction**: The spawner blocks until `init/1` returns; keep it quick or defer work
- **Error**: Returning a bare `State` instead of `{ok, State}`
  **Correction**: `init/1` must return one of the documented tuples

## Common Confusions

- **Confusion**: Thinking `init/1` runs concurrently with the spawner
  **Clarification**: The spawner is blocked until `init/1` completes and `gen_server` sends its ready message

## Source Reference

Chapter 14, "An Introduction to OTP," section "Callback to the Future," subsection "The init Function."

## Verification Notes

- Return values and blocking behavior: directly from ch. 14
- Confidence: HIGH — explicitly described
