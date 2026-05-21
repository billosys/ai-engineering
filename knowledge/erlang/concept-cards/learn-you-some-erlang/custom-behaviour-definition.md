---
concept: Custom Behaviour Definition
slug: custom-behaviour-definition
category: otp-behaviours
subcategory: otp-fundamentals
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "An Introduction to OTP"
chapter_number: 14
pdf_page: null
section: ".BEAM Me Up, Scotty!"
extraction_confidence: high
aliases:
  - "behavior_info/1"
  - "defining behaviors"
  - "custom behavior"
prerequisites:
  - otp-behaviour
extends:
  - otp-behaviour
related:
  - gen-server
contrasts_with: []
answers_questions:
  - "How do I define my own behaviour?"
  - "How does a behaviour declare its required callbacks?"
---

# Custom Behaviour Definition

## Quick Definition

A custom behaviour is defined by writing a module that exports `behavior_info/1`, which returns the list of `{Function, Arity}` callbacks that modules using the behaviour must implement.

## Core Definition

"Defining your own behaviors is really simple. You just need to export a function called `behavior_info/1`." Implemented as `behavior_info(callbacks) -> [{init,1}, {some_fun, 0}, {other, 3}]; behavior_info(_) -> undefined.`, this declares which callbacks (by name and arity) are expected. "And that's about it for behaviors. You can just use `-behavior(my_behavior).` in a module, implementing behaviors to get compiler warnings if you forgot a function." This is the same mechanism `gen_server` uses to produce its "undefined callback function" warnings (Hébert, ch. 14, ".BEAM Me Up, Scotty!", "Defining Behaviors" sidebar).

## Prerequisites

- **OTP behaviour** — A custom behaviour is an instance of the general behaviour concept

## Key Properties

1. A behaviour module exports `behavior_info/1`
2. `behavior_info(callbacks)` returns a list of `{FunctionName, Arity}` tuples
3. `behavior_info(_)` returns `undefined` for all other arguments
4. A module using it declares `-behavior(my_behavior).`
5. The compiler then warns if any declared callback is missing
6. This is the same mechanism the built-in `gen_server` behaviour uses

## Construction / Recognition

## To Define a Custom Behaviour

1. Create a module for the behaviour
2. Export `behavior_info/1`
3. Implement `behavior_info(callbacks) -> [{Fun, Arity}, ...];`
4. Implement `behavior_info(_) -> undefined.`
5. In user modules, add `-behavior(my_behavior).` and implement the listed callbacks

## Examples

> **behavior_info** (ch. 14): `behavior_info(callbacks) -> [{init,1}, {some_fun, 0}, {other, 3}]; behavior_info(_) -> undefined.`
>
> **Using it** (ch. 14): `-behavior(my_behavior).` in a module yields compiler warnings for any missing callback.

## Relationships

## Builds Upon

- **OTP behaviour** — A custom behaviour applies the general behaviour mechanism

## Related

- **gen_server** — A built-in behaviour defined via the same `behavior_info` mechanism

## Common Errors

- **Error**: Forgetting the `behavior_info(_) -> undefined.` clause
  **Correction**: Provide it so non-`callbacks` arguments are handled

## Common Confusions

- **Confusion**: Thinking defining a behaviour enforces callbacks at runtime
  **Clarification**: It only produces compile-time warnings for missing callbacks, not runtime errors

## Source Reference

Chapter 14, "An Introduction to OTP," section ".BEAM Me Up, Scotty!", "Defining Behaviors" sidebar.

## Verification Notes

- `behavior_info/1` definition: directly from the ch. 14 sidebar
- Confidence: HIGH — explicitly described with an example
