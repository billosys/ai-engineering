---
concept: Application Start Type
slug: application-start-type
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
  - start type
  - "temporary application"
  - "transient application"
  - "permanent application"
prerequisites:
  - application-start-and-stop
extends: []
related:
  - child-restart-type
  - erlang-release
contrasts_with:
  - child-restart-type
answers_questions:
  - "What is an OTP application?"
  - "How does an OTP application relate to a release?"
---

# Application Start Type

## Quick Definition

The start type — `temporary`, `transient`, or `permanent` — passed to `application:start/2` controls how the whole VM reacts when an application terminates.

## Core Definition

"We can give different arguments to `application:start/1`. Depending on the arguments, the VM will react differently to termination of one of its applications" (Ch. 19, "From Chaos to Application"). The three types:

- **`temporary`** — abnormal end is reported; the application terminates without restarting; the VM keeps running.
- **`transient`** — abnormal end is reported, all other applications are stopped, and the VM shuts down.
- **`permanent`** — *any* end (normal or abnormal) stops all applications and shuts the VM down.

## Prerequisites

- **Application start and stop** — Start type is an argument to `application:start/2`.

## Key Properties

1. Passed as the second argument to `application:start(AppName, Type)`.
2. `temporary` — the default; termination affects only that application.
3. `transient` — abnormal termination brings the whole VM down; normal termination does not.
4. `permanent` — both normal and abnormal termination bring the whole VM down.
5. With `permanent`/`transient`, the VM "prefers to die sanely" rather than continue with a vital application broken.
6. `application:stop(AppName)` always stops just that application, regardless of start type.

## Construction / Recognition

## To Choose a Start Type

1. Non-critical, optional application → `temporary`.
2. Application whose abnormal failure should bring the system down → `transient`.
3. Vital application the whole system depends on → `permanent`.

## Context & Application

In the book's example, `application:stop(ppool)` prints `type: temporary` because `ppool` was started with the default `temporary` type. The book frames `permanent`/`transient` as the VM giving up: "something has gone very, very wrong ... the VM has lost all hope in your program ... the VM prefers to die sanely." Release `.rel` files (Ch. 21) likewise let you mark each application `temporary`, `transient`, or `permanent`.

## Examples

**Example 1** (Ch. 19): `application:stop(ppool)` reports `type: temporary` — `ppool` ran as a temporary application.

**Example 2** (Ch. 21): The `erlcount-1.0.rel` file marks `{ppool, "1.0.0", permanent}` and `{erlcount, "1.0.0", transient}`.

## Relationships

## Builds Upon

- **Application start and stop** — Start type is a parameter of starting an application.

## Related

- **erlang-release** — Release files specify each application's start type.

## Contrasts With

- **child-restart-type** — Uses the same three words for *child processes* under a supervisor; here they govern *whole applications* and the VM's fate.

## Common Errors

- **Error**: Starting a vital application as `temporary`, so its failure goes unnoticed.
  **Correction**: Use `permanent` for applications the system cannot run without.

## Common Confusions

- **Confusion**: Conflating application start types with supervisor child restart types.
  **Clarification**: They share the names `temporary`/`transient`/`permanent` but apply at different levels — child restart governs whether a *process* is restarted; application start type governs whether the *VM* shuts down.

## Source Reference

Chapter 19: "Building Applications the OTP Way," section "From Chaos to Application"; start types in release files in Chapter 21, "Releases with systools."

## Verification Notes

- Definition: Direct quotes and the three-type `variablelist` from Chapter 19.
- Key Properties: Adapted from that list.
- Confidence: HIGH — explicitly defined.
