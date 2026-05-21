---
concept: Application Callback Module
slug: application-callback-module
category: applications-releases
subcategory: applications
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building Applications the OTP Way"
chapter_number: 19
pdf_page: null
section: "The Application Behavior"
extraction_confidence: high
aliases:
  - callback module
  - application module
prerequisites:
  - application-behaviour
  - app-file
extends: []
related:
  - application-behaviour
  - application-start-and-stop
  - complex-termination
contrasts_with: []
answers_questions:
  - "How does a behaviour relate to its callback module?"
  - "How do I structure an OTP application?"
---

# Application Callback Module

## Quick Definition

The application callback module is the module that implements the application behaviour's `start/2` and `stop/1` callbacks. It is named in the `.app` file's `{mod, {Module, Args}}` tuple.

## Core Definition

The callback module is the *specific* part of the application behaviour. "The application callback module requires very few functions to be functional: `start/2` and `stop/1`" (Ch. 19, "The Application Behavior"). The `.app` file's `{mod, {CallbackMod, Args}}` tuple "tells OTP that when starting your application, it should call `CallbackMod:start(normal, Args)`."

## Prerequisites

- **Application behaviour** — The callback module implements this behaviour.
- **App file** — The callback module is registered via the `.app` file's `{mod, ...}` tuple.

## Key Properties

1. Declared with `-behavior(application).`
2. Must export and implement `start/2` and `stop/1`.
3. `start(normal, Args)` initialises the app and returns `{ok, Pid}` or `{ok, Pid, State}`.
4. `stop(State)` does post-shutdown cleanup.
5. May optionally implement `prep_stop/1` for cleanup while the app is still alive.
6. Its job in `start/2` is typically just to start the top-level supervisor.
7. Named in the `.app` file as `{mod, {CallbackMod, Args}}`; `Args` is passed to `start/2`.

## Construction / Recognition

## To Write a Callback Module

1. Create the module, add `-behavior(application).`
2. Export `start/2, stop/1`.
3. `start(normal, _Args) -> top_supervisor:start_link().`
4. `stop(_State) -> ok.`
5. Register it in the `.app` file via `{mod, {ThisModule, []}}`.

## Context & Application

The book converts `ppool.erl` into the `ppool` callback module by replacing `start_link/0`/`stop/0` with `start/2`/`stop/1`. It notes you should remove ad-hoc `stop/0` functions from the top supervisor "because the OTP application tools will take care of that for us." A library application has *no* callback module — the `{mod, ...}` tuple is simply omitted.

## Examples

**Example 1** (Ch. 19): The `ppool` module: `-behavior(application).`, `start(normal, _Args) -> ppool_supersup:start_link().`, `stop(_State) -> ok.`

**Example 2** (Ch. 20): The `erlcount` module: `start(normal, _Args) -> erlcount_sup:start_link().`, `stop(_State) -> ok.`

## Relationships

## Builds Upon

- **Application behaviour** — The callback module is its specific half.

## Related

- **app-file** — Registers the callback module via `{mod, ...}`.
- **application-start-and-stop** — Driven through this module's callbacks.
- **complex-termination** — Adds the optional `prep_stop/1` callback here.

## Common Errors

- **Error**: Leaving a `start_link/0` / `stop/0` API on the module after converting it to a callback module.
  **Correction**: Replace them with `start/2`/`stop/1`; let `application:start/1` and `application:stop/1` drive the lifecycle.

## Common Confusions

- **Confusion**: Thinking every application needs a callback module.
  **Clarification**: Only *active* applications (those with processes to start) need one; library applications omit the `{mod, ...}` tuple entirely.

## Source Reference

Chapter 19: "Building Applications the OTP Way," sections "The Application Behavior" and "From Chaos to Application."

## Verification Notes

- Definition: Adapted from "The Application Behavior" and the `{mod, ...}` description.
- Key Properties: Synthesised from the conversion of `ppool.erl`.
- Confidence: HIGH — explicitly defined with code.
