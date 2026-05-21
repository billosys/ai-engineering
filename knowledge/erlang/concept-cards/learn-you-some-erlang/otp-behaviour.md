---
concept: OTP Behaviour
slug: otp-behaviour
category: otp-behaviours
subcategory: otp-fundamentals
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "An Introduction to OTP"
chapter_number: 14
pdf_page: null
section: "The Common Process, Abstracted"
extraction_confidence: high
aliases:
  - "behaviour"
  - "behavior"
  - "OTP behavior"
prerequisites:
  - process-state-loop
extends: []
related:
  - gen-server
  - otp-callback-module
  - the-otp-way
contrasts_with: []
answers_questions:
  - "What is an OTP behaviour?"
  - "How does a behaviour relate to its callback module?"
---

# OTP Behaviour

## Quick Definition

An OTP behaviour is a generic, battle-tested module that implements the common parts of a process pattern and specifies — as a contract — the callback functions a user-supplied module must provide to fill in the specific parts.

## Core Definition

The OTP framework spotted that "in most processes, we had a function in charge of spawning the new process, a function in charge of giving the process its initial values, a main loop, and so on... usually present in all concurrent programs." The generic abstractions built on these basic libraries are called *behaviours*. The chapter defines a behaviour precisely when discussing `-behavior(gen_server)`: "A *behavior* is basically a way for a module to specify functions it expects another module to have. The behavior is the contract sealing the deal between the well-behaved generic part of the code and the specific, error-prone part of the code (yours)." If a `-behavior` is declared but a callback is missing, the compiler emits a warning. You can define your own behaviour by exporting `behavior_info/1` returning a list of `{Function, Arity}` callbacks (Hébert, ch. 14, "The Common Process, Abstracted," ".BEAM Me Up, Scotty!").

## Prerequisites

- **Process state loop** — Behaviours abstract exactly the loop-plus-interface pattern

## Key Properties

1. A behaviour separates the generic (framework) code from the specific (callback) code
2. It is a contract: it specifies the callback functions a user module must implement
3. Declared in a user module with `-behavior(Name).` (`behaviour` also accepted)
4. The compiler warns if a required callback is missing
5. The generic part is reused, well-tested, and battle-hardened over years
6. Custom behaviours are defined by exporting `behavior_info(callbacks)` returning `{Fun, Arity}` pairs
7. Common OTP behaviours include `gen_server`, finite-state-machine, `gen_event`, and supervisor

## Construction / Recognition

## To Use a Behaviour

1. Pick the OTP behaviour matching your process pattern (e.g. `gen_server`)
2. Declare it in your module: `-behavior(gen_server).`
3. Implement and export every callback the behaviour requires
4. Compile — heed compiler warnings about missing callbacks
5. Start the process through the behaviour's `start`/`start_link` functions

## Examples

> **Behaviour declaration and warnings** (ch. 14): `-behavior(gen_server).` in an otherwise empty module compiles but warns "undefined callback function handle_call/3 (behavior 'gen_server')," etc.
>
> **Custom behaviour** (ch. 14): `behavior_info(callbacks) -> [{init,1}, {some_fun, 0}, {other, 3}]; behavior_info(_) -> undefined.`

## Relationships

## Related

- **gen_server** — The most-used OTP behaviour, abstracting the client/server pattern
- **OTP callback module** — The user module that implements a behaviour's callbacks
- **The OTP way** — The overall philosophy of which behaviours are the centerpiece

## Common Errors

- **Error**: Declaring `-behavior` but forgetting a required callback
  **Correction**: Implement every callback; the compiler warns but you should fix all of them
- **Error**: Reimplementing generic process machinery instead of using a behaviour
  **Correction**: Use the existing behaviour — its generic code is far more tested than hand-written code

## Common Confusions

- **Confusion**: Thinking a behaviour is a base class to inherit from
  **Clarification**: It is a contract — the generic module calls *your* callbacks; there is no inheritance
- **Confusion**: Believing `behavior` and `behaviour` are different things
  **Clarification**: Both spellings are accepted by the Erlang compiler

## Source Reference

Chapter 14, "An Introduction to OTP," sections "The Common Process, Abstracted" and ".BEAM Me Up, Scotty!" ("Defining Behaviors" sidebar).

## Verification Notes

- Definition of behaviour as a contract: quoted directly from ch. 14
- `behavior_info/1`: from the ch. 14 sidebar
- Confidence: HIGH — explicitly defined
