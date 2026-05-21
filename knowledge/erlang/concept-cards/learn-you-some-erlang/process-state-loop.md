---
concept: Process State Loop
slug: process-state-loop
category: processes-concurrency
subcategory: process-design
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "More on Multiprocessing"
chapter_number: 11
pdf_page: null
section: "We Love Messages, But We Keep Them Secret"
extraction_confidence: high
aliases:
  - "receive loop"
  - "main loop"
  - "server loop"
prerequisites:
  - stateful-process
  - receive-expression
extends:
  - stateful-process
related:
  - otp-callback-module
contrasts_with: []
answers_questions:
  - "How do I structure the main loop of a stateful process?"
  - "How should I hide a process's message protocol from its users?"
---

# Process State Loop

## Quick Definition

A process state loop is the recurring structure of a long-lived process: a function that receives a message, computes a new state, and tail-recurses with it. The chapter also recommends hiding its message protocol behind interface functions.

## Core Definition

Every stateful process in the chapter follows the same shape: a loop function pattern-matches messages in a `receive`, acts, and recurses with updated state. The chapter stresses two refinements to this pattern. First, *hide the protocol*: "the programmer who's going to use the fridge must know about the protocol that has been invented for that process. That's a useless burden" — so wrap sends and receives in interface functions like `store/2` and `take/2`. Second, *hide the spawning*: provide a `start/1` function (using the `?MODULE` macro) so the whole process is handled by one module. This same loop-plus-interface pattern is the seed of the OTP `gen_server` abstraction (Hébert, ch. 11, "We Love Messages, But We Keep Them Secret").

## Prerequisites

- **Stateful process** — The loop carries the process's state
- **Receive expression** — Each loop iteration is a `receive`

## Key Properties

1. The loop is a function taking the state, doing a `receive`, and tail-recursing with new state
2. Message protocols should be hidden behind interface functions, not exposed to callers
3. Interface functions package `self()` (and often a reference) so callers need not know the wire format
4. A `start/1` function should hide process creation (commonly using `?MODULE` for the module name)
5. Concentrating spawn, send, and receive in one module gives consistency and easier change
6. This pattern recurs in every concurrent program — it is what OTP behaviours abstract

## Construction / Recognition

## To Build a Process State Loop

1. Write a loop function `loop(State)` with a `receive` matching each supported message
2. In each clause, compute the new state and tail-recurse: `loop(NewState)`
3. Write interface functions that hide the `!`/`receive` protocol, e.g. `store(Pid, Food)`
4. Write a `start/1` function that calls `spawn(?MODULE, loop, [InitialState])`
5. Expose only the interface functions to users of the module

## Examples

> **Hidden message functions** (ch. 11): `store(Pid, Food)` sends `{self(), {store, Food}}` and receives `{Pid, Msg}`, so callers never see the protocol.
>
> **Hidden spawning** (ch. 11): `start(FoodList) -> spawn(?MODULE, fridge2, [FoodList]).` — "everything about the fridge process is now handled by the `kitchen` module."

## Relationships

## Builds Upon

- **Stateful process** — The loop is the mechanism that carries state

## Related

- **OTP callback module** — The OTP `gen_server` generalizes exactly this loop-plus-interface pattern

## Common Errors

- **Error**: Forcing callers to construct protocol messages themselves
  **Correction**: Wrap every interaction in an interface function
- **Error**: Leaving `spawn/3` calls scattered across callers
  **Correction**: Provide a `start/1` function so changes (logging, extra processes) happen in one place

## Common Confusions

- **Confusion**: Thinking the loop and the public API are the same thing
  **Clarification**: The loop is the private receive-recurse machinery; interface functions are the public façade that hides it

## Source Reference

Chapter 11, "More on Multiprocessing," section "We Love Messages, But We Keep Them Secret."

## Verification Notes

- Loop pattern and protocol-hiding advice: directly from ch. 11
- OTP connection: cross-referenced from ch. 14
- Confidence: HIGH — explicitly demonstrated
