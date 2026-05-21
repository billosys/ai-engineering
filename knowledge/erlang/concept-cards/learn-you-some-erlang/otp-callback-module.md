---
concept: OTP Callback Module
slug: otp-callback-module
category: otp-behaviours
subcategory: otp-fundamentals
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "An Introduction to OTP"
chapter_number: 14
pdf_page: null
section: "Callback to the Future"
extraction_confidence: high
aliases:
  - "callback module"
  - "callbacks"
prerequisites:
  - otp-behaviour
extends: []
related:
  - gen-server
  - the-otp-way
contrasts_with: []
answers_questions:
  - "What is an OTP callback module?"
  - "How does a behaviour relate to its callback module?"
---

# OTP Callback Module

## Quick Definition

An OTP callback module is the user-written module that supplies the specific functions an OTP behaviour requires. The behaviour's generic code calls these callbacks at the right moments.

## Core Definition

OTP behaviours split code into a generic part (the behaviour) and a specific part (the callback module). The callback module declares `-behavior(Name)` and implements the callback functions named in the behaviour's contract. The chapter develops this idea by hand: `my_server`'s `loop/2` calls `Module:handle_call/3` and `Module:handle_cast/2` on the supplied module, and `kitty_server2` is rewritten "as a callback module that will respect the interface we defined for `my_server`." For `gen_server`, the callbacks are `init/1`, `handle_call/3`, `handle_cast/2`, `handle_info/2`, `terminate/2`, and `code_change/3`. The callback module holds only the application-specific logic — initialization, request handling, and termination — while the behaviour provides spawning, the loop, message dispatch, timeouts, and error handling (Hébert, ch. 14, "Generalizing the Server Loop," "Callback to the Future").

## Prerequisites

- **OTP behaviour** — A callback module exists to fulfill a behaviour's contract

## Key Properties

1. A callback module declares `-behavior(BehaviourName).`
2. It exports and implements every callback the behaviour requires
3. It contains only application-specific logic — not generic process machinery
4. The behaviour's generic code invokes the callbacks (`Module:callback(...)`)
5. Callbacks receive and return state, which the behaviour threads through its loop
6. Because callbacks are plain functions of state, they are easy to unit-test without spawning a process

## Construction / Recognition

## To Write a Callback Module

1. Create a module and add `-behavior(gen_server).` (or another behaviour)
2. Export the behaviour's required callbacks
3. Implement `init/1` to build and return the initial state
4. Implement the request handlers (`handle_call/3`, `handle_cast/2`, `handle_info/2`)
5. Implement `terminate/2` to undo what `init/1` set up
6. Implement `code_change/3` for upgrades
7. Keep client API functions in the same module, delegating to the behaviour's `call`/`cast`

## Examples

> **kitty_server2 as a callback module** (ch. 14): it is re-implemented "as a callback module that will respect the interface we defined for `my_server`," exporting `init/1`, `handle_call/3`, `handle_cast/2`.
>
> **Easier testing** (ch. 14): the callback version "requires us to run the function calls over only the `handle_call/3` and `handle_cast/2` functions... There is no need to set up servers. Just pass the state in as a function parameter."

## Relationships

## Builds Upon

- **OTP behaviour** — The callback module implements a behaviour's contract

## Related

- **gen_server** — The behaviour whose callbacks a server callback module implements
- **The OTP way** — Callback modules are the "specific" half of OTP's generic/specific split

## Common Errors

- **Error**: Putting generic loop/spawn code into the callback module
  **Correction**: The behaviour supplies all generic machinery; the callback module holds only specifics
- **Error**: Forgetting to export a required callback
  **Correction**: Export every callback; the compiler warns about omissions

## Common Confusions

- **Confusion**: Thinking the callback module runs the loop itself
  **Clarification**: The behaviour runs the loop and *calls into* the callback module at defined points

## Source Reference

Chapter 14, "An Introduction to OTP," sections "Generalizing the Server Loop," "Generalizing Kitty Server," "Callback to the Future."

## Verification Notes

- Callback module concept and testability: directly from ch. 14
- Confidence: HIGH — explicitly demonstrated with `kitty_server2`
