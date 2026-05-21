---
concept: Library Application
slug: library-application
category: applications-releases
subcategory: applications
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building Applications the OTP Way"
chapter_number: 19
pdf_page: null
section: "Library Applications"
extraction_confidence: high
aliases:
  - library app
prerequisites:
  - otp-application
  - app-file
extends:
  - otp-application
related:
  - application-callback-module
contrasts_with:
  - otp-application
answers_questions:
  - "What is an OTP application?"
  - "How do I structure an OTP application?"
---

# Library Application

## Quick Definition

A library application is an OTP application that wraps flat modules with no process to start — so it has an `.app` file but no application callback module.

## Core Definition

"What happens when we want to wrap flat modules in an application but we have no process to start and thus no need for an application callback module? ... the only other thing left to do is to remove the tuple `{mod, {Module, Args}}` from the application file. That's it. This is called a *library application*. The Erlang `stdlib` (standard library) application is an example of one of these" (Ch. 19, "Library Applications").

## Prerequisites

- **OTP application** — A library application is a kind of OTP application.
- **App file** — It still has an `.app` file (just without `{mod, ...}`).

## Key Properties

1. It has no application callback module.
2. Its `.app` file omits the `{mod, {Module, Args}}` tuple.
3. It still has `description`, `vsn`, `modules`, `registered`, `applications`, `env`.
4. It cannot be "started" in the active sense — there is no supervision tree to launch.
5. Erlang's own `stdlib` is a library application.

## Construction / Recognition

## To Make a Library Application

1. Lay out the modules in the standard application structure.
2. Write the `.app` file with `description`, `vsn`, `modules`, etc.
3. Omit the `{mod, {Module, Args}}` tuple.
4. Other applications can list it as a dependency and call its functions.

## Context & Application

The book shows `stdlib.app.src` as a real-world example: it lists `array`, `gen_event`, `gen_fsm`, `gen_server`, `io`, `lists`, `zip`, etc. in `modules`, declares `{applications, [kernel]}`, but has no `{mod, ...}` tuple. In releases, a library application can be marked with `{LibraryApp, load}` so it is loaded but never started (Ch. 21 Reltool comment).

## Examples

**Example 1** (Ch. 19): Erlang's `stdlib` — `{application, stdlib, [{description, ...}, {vsn, "%VSN%"}, {modules, [...]}, {registered, [...]}, {applications, [kernel]}, {env, []}]}.` — no `{mod, ...}`.

## Relationships

## Builds Upon

- **OTP application** — A library application is an OTP application without a callback module.

## Related

- **application-callback-module** — Precisely what a library application lacks.

## Contrasts With

- **otp-application** — An *active* OTP application has a callback module and a supervision tree to start; a library application has neither.

## Common Errors

- **Error**: Adding a `{mod, ...}` tuple to a library application's `.app` file.
  **Correction**: Omit it; there is no process to start, so there is no callback module to name.

## Common Confusions

- **Confusion**: Thinking a library application is not a "real" OTP application.
  **Clarification**: It is a real OTP application — it has an `.app` file, version, dependencies, and is managed by the application system; it simply has nothing to start.

## Source Reference

Chapter 19: "Building Applications the OTP Way," section "Library Applications."

## Verification Notes

- Definition: Direct quote from "Library Applications."
- Key Properties: Adapted from the `stdlib.app.src` example.
- Confidence: HIGH — explicitly defined with a real example.
