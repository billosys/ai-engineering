---
concept: OTP Application
slug: otp-application
category: applications-releases
subcategory: applications
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building an Application"
chapter_number: 18
pdf_page: null
section: "A Pool of Processes"
extraction_confidence: high
aliases:
  - application
  - Erlang application
prerequisites:
  - otp-behaviour
  - supervisor
  - supervision-tree
extends: []
related:
  - application-behaviour
  - app-file
  - otp-application-structure
  - erlang-release
contrasts_with:
  - library-application
answers_questions:
  - "What is an OTP application?"
  - "How does an OTP application relate to a release?"
  - "What concepts precede building an OTP application?"
---

# OTP Application

## Quick Definition

An OTP application is a group of related code and processes that uses OTP behaviours and is wrapped in a structure telling the VM how to start it up and tear it down.

## Core Definition

"An Erlang application is a group of related code and processes. An OTP application specifically uses OTP behaviors for its processes, and then wraps them in a very specific structure that tells the VM how to set everything up and then tear it down" (Ch. 18, opening).

Chapter 19 elaborates that OTP applications provide a directory structure, configuration handling, environment variables, dependency-respecting start/stop, and conflict detection / live upgrades.

## Prerequisites

- **OTP behaviour** — An OTP application's processes use OTP behaviours.
- **Supervisor** — An application is started through a top-level supervisor.
- **Supervision tree** — The application's processes form a supervision tree.

## Key Properties

1. It is a group of related code and processes built from OTP behaviours.
2. It is "wrapped" by an application resource file and (usually) an application callback module.
3. It can be started and stopped as a unit, with dependencies respected.
4. It has a standard directory layout (`ebin/`, `include/`, `priv/`, `src/`).
5. It can declare configuration via environment variables.
6. The application's processes are rooted in a single supervision tree started by its callback module.
7. Modules, the standard library, and the kernel are themselves applications.

## Construction / Recognition

## To Build an OTP Application

1. Implement the functionality using OTP behaviours (`gen_server`, `gen_event`, supervisors).
2. Arrange the supervision tree so a single call starts everything.
3. Add an application resource (`.app`) file describing the application.
4. Add an application callback module implementing `start/2` and `stop/1`.
5. Start it with `application:start(AppName)`.

## Context & Application

Chapter 18 builds the `ppool` process pool using OTP components but stops short of the full "wrapping up." Chapter 19 completes the wrapping, turning `ppool` into a proper OTP application. The reward for the wrapping is consistency, tooling support, dependency management, environment variables, and participation in the VM's overall supervision and shutdown.

The book warns against calling `MyApp:start(...)` directly: doing so "loses a lot of the advantages of actually having an application" — it is no longer in the VM's supervision tree, cannot access environment variables, and skips dependency checks.

## Examples

**Example 1** (Ch. 18–19): `ppool` — a process-pool application with a multi-level supervision tree.

**Example 2** (Ch. 20): `erlcount` — an application that depends on `ppool` and counts regex matches in Erlang source files.

## Relationships

## Builds Upon

- **Supervision tree** — The application's processes form one.

## Related

- **application-behaviour** — The behaviour that wraps an application.
- **app-file** — The resource file describing the application.
- **otp-application-structure** — The standard directory layout.
- **erlang-release** — Applications are packaged into releases.

## Contrasts With

- **library-application** — A library application has no processes to start and thus no callback module.

## Common Errors

- **Error**: Starting an application with `MyApp:start(...)` instead of `application:start(MyApp)`.
  **Correction**: Use `application:start/1` so the app joins the VM's supervision tree and dependency machinery.

## Common Confusions

- **Confusion**: Thinking merely using OTP behaviours makes code an OTP application.
  **Clarification**: "Merely using OTP components isn't enough" — the code must also be wrapped with an `.app` file and (for active apps) a callback module.

## Source Reference

Chapter 18: "Building an Application," opening section "A Pool of Processes"; concept extended in Chapter 19, "Building Applications the OTP Way."

## Verification Notes

- Definition: Direct quote from Chapter 18's opening.
- Key Properties: Synthesised from Chapter 18's intro and Chapter 19's list of what OTP applications provide.
- Confidence: HIGH — explicitly defined; this is a cross-chapter shared slug referenced by other agents.
