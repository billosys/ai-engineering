---
concept: Application Resource File
slug: app-file
category: applications-releases
subcategory: applications
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building Applications the OTP Way"
chapter_number: 19
pdf_page: null
section: "The Application Resource File"
extraction_confidence: high
aliases:
  - "app file"
  - ".app file"
  - application file
  - application resource file
prerequisites:
  - otp-application
  - otp-application-structure
extends: []
related:
  - application-callback-module
  - application-dependency
  - application-environment-variable
contrasts_with: []
answers_questions:
  - "How do I structure an OTP application?"
  - "What is an OTP application?"
---

# Application Resource File

## Quick Definition

The application resource file (`yourapp.app`) is a file of Erlang terms that tells the VM what an application is, what modules it has, what it depends on, and how to start it. It lives in `ebin/`.

## Core Definition

"This file will tell the Erlang VM what the application is, where it begins, and where it ends. This file lives in the `ebin/` directory. ... This file is usually named `yourapp.app` ... and contains a bunch of Erlang terms defining the application in a way that the VM can understand" (Ch. 19, "The Application Resource File").

Its structure is `{application, ApplicationName, Properties}.` where `Properties` is a list of `{Key, Value}` tuples.

## Prerequisites

- **OTP application** — The `.app` file defines an OTP application.
- **OTP application structure** — It lives in the `ebin/` directory.

## Key Properties

1. Format: `{application, ApplicationName, Properties}.` — `ApplicationName` is an atom.
2. `{description, String}` — short human description (defaults to `""`).
3. `{vsn, String}` — application version, conventionally `Major.Minor.Patch`.
4. `{modules, ModuleList}` — all modules the application introduces; a module belongs to at most one application.
5. `{registered, AtomList}` — names the application registers, for clash detection.
6. `{env, [{Key, Val}]}` — configuration key/value store (see environment variables).
7. `{applications, AtomList}` — applications this one depends on.
8. `{mod, {CallbackMod, Args}}` — the application callback module; its absence makes a library application.
9. `{maxT, Milliseconds}` — maximum run time before shutdown (defaults to `infinity`, rarely used).

## Construction / Recognition

## To Write an .app File

1. Start with `{application, myapp, [ ... ]}.`
2. Add `{description, ...}` and `{vsn, ...}`.
3. List `{modules, [...]}` and `{registered, [...]}`.
4. List dependencies in `{applications, [stdlib, kernel, ...]}`.
5. Add `{mod, {CallbackMod, Args}}` for active applications.
6. Add `{env, [...]}` for default configuration.
7. Place the file in `ebin/` (or `myapp.app.src` in `src/`).

## Context & Application

The book's minimal `ppool.app` lists only `vsn`, `modules`, `registered`, and `mod`. The `erlcount.app` adds `applications` and `env`. For releases (Ch. 21), the book stresses adding `description` and explicitly listing `stdlib` and `kernel` in `applications` — omitting them can break Reltool releases.

## Examples

**Example 1** (Ch. 19): `{application, ppool, [{vsn, "1.0.0"}, {modules, [ppool, ppool_serv, ppool_sup, ppool_supersup, ppool_worker_sup]}, {registered, [ppool]}, {mod, {ppool, []}}]}.`

**Example 2** (Ch. 20): `erlcount.app` adds `{applications, [ppool]}` and `{env, [{directory, "."}, {regex, [...]}, {max_files, 10}]}`.

## Relationships

## Builds Upon

- **OTP application** — The file defines an application.

## Related

- **application-callback-module** — Named in the `{mod, ...}` tuple.
- **application-dependency** — Listed in the `{applications, ...}` tuple.
- **application-environment-variable** — Defined in the `{env, ...}` tuple.

## Common Errors

- **Error**: Listing a module in two applications' `modules` lists.
  **Correction**: A module belongs to at most one application; assign it to exactly one `.app` file.
- **Error**: Omitting `stdlib` and `kernel` from `applications` when building a release.
  **Correction**: Add them explicitly; release tools (especially Reltool) need them.

## Common Confusions

- **Confusion**: Thinking the `registered` list is enforced by the VM.
  **Clarification**: It is "entirely based on trusting the developers to give good data" — used for clash detection, not enforcement.

## Source Reference

Chapter 19: "Building Applications the OTP Way," section "The Application Resource File"; updates for releases in Chapter 21, "Updating the Application Files."

## Verification Notes

- Definition: Direct quotes from "The Application Resource File."
- Key Properties: Each property copied from the source's `variablelist`.
- Confidence: HIGH — every field explicitly documented.
