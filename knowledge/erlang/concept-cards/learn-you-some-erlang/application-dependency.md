---
concept: Application Dependency
slug: application-dependency
category: applications-releases
subcategory: applications
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Count of Applications"
chapter_number: 20
pdf_page: null
section: "The Application File"
extraction_confidence: high
aliases:
  - "applications tuple"
  - app dependency
prerequisites:
  - app-file
  - otp-application
extends: []
related:
  - application-start-and-stop
  - erlang-release
contrasts_with:
  - included-application
answers_questions:
  - "How do I structure an OTP application?"
  - "How does an OTP application relate to a release?"
---

# Application Dependency

## Quick Definition

An application dependency is another application that must be loaded and/or started before yours. Dependencies are declared in the `.app` file's `{applications, AtomList}` tuple.

## Core Definition

"`{applications, AtomList}` ... is a list of applications on which yours depends. The application system of Erlang will make sure they were loaded and/or started before allowing yours to do so. All applications depend at least on `kernel` and `stdlib`" (Ch. 19, "The Application Resource File"). In Chapter 20: "the `applications` tuple gives a list of all the applications that should be started before `erlcount`. If you try to start it without that, you'll get an error message."

## Prerequisites

- **App file** — Dependencies are declared in the `.app` file.
- **OTP application** — Both the dependent and the dependency are OTP applications.

## Key Properties

1. Declared as `{applications, [App1, App2, ...]}` in the `.app` file.
2. The application system ensures dependencies are loaded/started first.
3. Every application depends on at least `kernel` and `stdlib`.
4. Starting an application whose dependencies are missing produces an error.
5. OTP uses the list to determine whether an application can be loaded or started.
6. Release tools use dependency lists to compute correct startup order.

## Construction / Recognition

## To Declare Dependencies

1. Identify which other applications your code requires at runtime.
2. Add them to `{applications, [...]}` in the `.app` file.
3. Include `kernel` and `stdlib` explicitly (required for releases).
4. Ensure those applications are available so the system can start them first.

## Context & Application

The `erlcount` application depends on `ppool`, so its `.app` file lists `{applications, [ppool]}` (and, for releases, `{applications, [stdlib, kernel, ppool]}`). The book stresses: "It is important to add your dependencies, given OTP has mechanisms to know whether an application can be loaded or started based on this list. Not adding them is doing a disservice to yourself."

## Examples

**Example 1** (Ch. 20): `erlcount.app` declares `{applications, [ppool]}` — `ppool` must start before `erlcount`.

**Example 2** (Ch. 21): For releases, both apps are updated — `ppool` gets `{applications, [stdlib, kernel]}` and `erlcount` gets `{applications, [stdlib, kernel, ppool]}`.

## Relationships

## Builds Upon

- **App file** — Dependencies live in the `applications` tuple.

## Related

- **application-start-and-stop** — Dependencies are checked at start time.
- **erlang-release** — Releases use dependency lists to order startup.

## Contrasts With

- **included-application** — A dependency is a *separate* started application; an included application is started as part of another and cannot be reused.

## Common Errors

- **Error**: Omitting a dependency from the `applications` list.
  **Correction**: List every runtime dependency; otherwise the start fails or the system cannot order startup.
- **Error**: Forgetting `kernel` and `stdlib` when building a release.
  **Correction**: List them explicitly — release tools (Reltool especially) need them.

## Common Confusions

- **Confusion**: Thinking listing a dependency automatically starts it in plain `application:start/1`.
  **Clarification**: `application:start/1` only *checks* dependencies; it does not start them. Releases and `application:ensure_all_started/1` handle ordered startup.

## Source Reference

Chapter 20: "The Count of Applications," section "The Application File"; original definition in Chapter 19, "The Application Resource File."

## Verification Notes

- Definition: Direct quotes from both chapters.
- Key Properties: Synthesised from the `applications` tuple description.
- Confidence: HIGH — explicitly defined.
