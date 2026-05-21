---
concept: Stateful Process
slug: stateful-process
category: processes-concurrency
subcategory: process-design
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "More on Multiprocessing"
chapter_number: 11
pdf_page: null
section: "State Your State"
extraction_confidence: high
aliases:
  - "process with state"
  - "stateful actor"
prerequisites:
  - process
  - receive-expression
  - tail-recursion
extends: []
related:
  - process-state-loop
contrasts_with: []
answers_questions:
  - "How do I implement a stateful process?"
  - "How is state held in an Erlang process?"
---

# Stateful Process

## Quick Definition

A stateful process holds data between messages by carrying that data in the arguments of its recursive loop function. Each message handler computes a new state and recurses with it.

## Core Definition

The chapter opens by noting that processes that are "just functions with messages" offer no real advantage — "to reap the benefits, we need to be able to hold state in a process." Erlang processes have no mutable variables, so "with the help of recursion, the state of a process can be held entirely in the parameters of the function." The chapter's `fridge2/1` example carries a `FoodList` argument: storing food recurses with `[Food|FoodList]`, taking food recurses with the item removed. Because each message is handled and then the function recurses with updated arguments, the loop's parameters *are* the process state (Hébert, ch. 11, "State Your State").

## Prerequisites

- **Process** — State lives inside a running process
- **Receive expression** — Each state transition is triggered by a received message
- **Tail recursion** — The loop recurses once per message; it must be tail recursive

## Key Properties

1. State is carried in the arguments of the loop function, not in mutable variables
2. Each `receive` clause computes a new state and recurses with it
3. The first version of the loop function takes the initial state as its argument
4. Because messages are serialized through the mailbox, state updates are race-free within the process
5. State can be any term — a list, a record, a dict, etc.

## Construction / Recognition

## To Implement a Stateful Process

1. Define a loop function that takes the state as a parameter, e.g. `fridge2(FoodList)`
2. In each `receive` clause, compute the updated state
3. Recurse, passing the new state: `fridge2([Food|FoodList])`
4. Provide a terminate clause that returns (or exits) without recursing
5. Spawn it with an initial state: `spawn(kitchen, fridge2, [[baking_soda]])`

## Examples

> **Fridge with no state** (ch. 11): `fridge1/0` always replies `not_found` because it recurses "without state."
>
> **Fridge with state** (ch. 11): `fridge2(FoodList)` stores food by recursing `fridge2([Food|FoodList])` and takes it by recursing with `lists:delete(Food, FoodList)`.
>
> **Race-free guarantee** (ch. 11): "even if a thousand people suddenly reached for the last piece of turkey... only one of them could get it."

## Relationships

## Builds Upon

- **Process** — The container of the state
- **Receive expression** — Drives each state transition
- **Tail recursion** — Keeps the loop from growing the stack

## Related

- **Process state loop** — The recursive loop pattern that carries the state

## Common Errors

- **Error**: Recursing without threading the updated state, losing changes
  **Correction**: Always pass the new state into the recursive call
- **Error**: Forgetting a termination clause, so the process can never stop
  **Correction**: Provide a clause (e.g. on `terminate`) that returns without recursing

## Common Confusions

- **Confusion**: Looking for mutable variables to hold process state
  **Clarification**: Erlang has single-assignment variables; state persists only by being passed through recursive loop arguments

## Source Reference

Chapter 11, "More on Multiprocessing," section "State Your State."

## Verification Notes

- Definition and fridge example: directly from ch. 11
- Confidence: HIGH — explicitly demonstrated
