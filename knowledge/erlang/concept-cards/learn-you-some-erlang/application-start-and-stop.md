---
concept: Application Start and Stop
slug: application-start-and-stop
category: applications-releases
subcategory: applications
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building Applications the OTP Way"
chapter_number: 19
pdf_page: null
section: "From Chaos to Application"
extraction_confidence: high
aliases:
  - "application:start/1"
  - "application:stop/1"
  - starting an application
prerequisites:
  - application-callback-module
  - application-controller
extends: []
related:
  - application-start-type
  - application-dependency
contrasts_with: []
answers_questions:
  - "What is an OTP application?"
  - "How do I structure an OTP application?"
---

# Application Start and Stop

## Quick Definition

`application:start(AppName)` asks the application controller to launch an application — checking dependencies and calling its callback module's `start/2`. `application:stop(AppName)` shuts it down cleanly.

## Core Definition

"The magic command here is `application:start(ppool)`. This tells the application controller to launch our `ppool` application. It starts the `ppool_supersup` supervisor, and from that point on, everything can be used as normal" (Ch. 19, "From Chaos to Application"). `application:stop(AppName)` stops it, producing "a clean shutdown with a little informative report."

## Prerequisites

- **Application callback module** — `start/2`/`stop/1` are invoked by start/stop.
- **Application controller** — The process that actually performs start and stop.

## Key Properties

1. `application:start(AppName)` launches an application via the application controller.
2. It checks that dependency applications were loaded/started first.
3. It calls `CallbackMod:start(normal, Args)`, which starts the top supervisor.
4. `application:stop(AppName)` stops one application without affecting others, and prints an INFO report.
5. `application:which_applications()` lists running applications with their descriptions and versions.
6. Using `MyApp:start(...)` directly bypasses the controller and loses dependency checks, environment variables, and supervision-tree membership.

## Construction / Recognition

## To Start and Stop an Application

1. Ensure dependencies are listed in the `.app` file and available.
2. Run `application:start(AppName)`.
3. Use the application normally; check status with `application:which_applications()`.
4. Stop it with `application:stop(AppName)`.

## Context & Application

The book contrasts the messy `** exception exit: killed` from the pre-application `ppool` (Ch. 18) with the clean INFO report after `application:stop(ppool)`. It warns: calling `MyApp:start(...)` "works for testing purposes" but "loses a lot of the advantages of actually having an application." The behaviour of the VM on application termination depends on the application's *start type* (`temporary`, `transient`, `permanent`) — covered separately.

## Examples

**Example 1** (Ch. 19): `application:start(ppool).` returns `ok`; the pool can then be used with `ppool:start_pool/3`.

**Example 2** (Ch. 19): `application:stop(ppool).` prints `=INFO REPORT=== ... application: ppool exited: stopped type: temporary`.

## Relationships

## Builds Upon

- **Application callback module** — Its `start/2`/`stop/1` are invoked here.
- **Application controller** — Performs the actual launch and shutdown.

## Related

- **application-start-type** — Determines how the VM reacts to an app's termination.
- **application-dependency** — Checked before an application is allowed to start.

## Common Errors

- **Error**: Starting an application whose dependencies are not started.
  **Correction**: List dependencies in the `.app` file and start them first (or rely on a release/`application:ensure_all_started`).
- **Error**: Calling `MyApp:start(...)` directly in production.
  **Correction**: Use `application:start/1` so dependency checks, env vars, and supervision-tree membership all apply.

## Common Confusions

- **Confusion**: Thinking `application:stop/1` crashes the VM.
  **Clarification**: `application:stop/1` stops just that application cleanly; whether the VM survives an *abnormal* exit depends on the start type.

## Source Reference

Chapter 19: "Building Applications the OTP Way," section "From Chaos to Application."

## Verification Notes

- Definition: Direct quotes from "From Chaos to Application."
- Key Properties: Synthesised from the worked shell session and the warning note.
- Confidence: HIGH — explicitly demonstrated.
