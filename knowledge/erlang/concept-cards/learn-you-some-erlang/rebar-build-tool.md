---
concept: Rebar Build Tool
slug: rebar-build-tool
category: tooling
subcategory: build-tools
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building Applications the OTP Way"
chapter_number: 19
pdf_page: null
section: "The Application Resource File"
extraction_confidence: medium
aliases:
  - rebar
  - rebar3
prerequisites:
  - otp-application-structure
extends: []
related:
  - app-file
  - otp-application-structure
  - reltool
contrasts_with: []
answers_questions:
  - "How do I structure an OTP application?"
---

# Rebar Build Tool

## Quick Definition

Rebar is the community Erlang build tool. It understands OTP application principles, compiles code, fetches dependencies, and (with later versions) wraps release tooling.

## Core Definition

"Rebar is an Erlang build tool used by the community in general. It understands the principles behind OTP applications and can act the way Emakefiles do. It can also fetch dependencies from git and mercurial repositories as needed" (Ch. 19, "The Application Resource File," note).

## Prerequisites

- **OTP application structure** — Rebar assumes and operates on the standard layout.

## Key Properties

1. It is the community's general-purpose Erlang build tool.
2. It understands OTP application principles.
3. It can compile code, replacing the role of `Emakefile` files.
4. It fetches dependencies from git and mercurial repositories.
5. If using a standard OTP structure with rebar, the `modules` list in the `.app` file is handled for you.
6. It can also wrap release tooling (Emakefile + Reltool).

## Construction / Recognition

## To Recognise Rebar's Role

1. It builds and manages OTP applications and their dependencies.
2. It removes the need to maintain `Emakefile`s and manual `modules` lists.
3. It can drive release creation by wrapping the lower-level release tools.

## Context & Application

The book mentions rebar in passing as the community-standard alternative to hand-written `Emakefile`s. In Chapter 21 it notes: "these days, Erlang programmers seem to really love the idea of having all these releases handled for them by a tool called rebar, which will act as a wrapper over Emakefile files and Reltool. ... The rebar tool uses configuration files that are nearly the same."

**Tooling note:** The book describes the original `rebar`. Modern Erlang projects use **rebar3**, the current standard, which manages dependencies, builds, tests, and releases (via `relx`). Understanding the underlying `.app` file, Reltool, and release structure remains valuable regardless of which tool drives them.

## Examples

**Example 1** (Ch. 19): With a standard OTP structure and rebar, the `{modules, [...]}` list in the `.app` file is generated/handled automatically rather than maintained by hand.

**Example 2** (Ch. 21): Rebar acts as a wrapper over `Emakefile` files and Reltool to produce releases.

## Relationships

## Related

- **app-file** — Rebar can generate/maintain the `.app` file's `modules` list.
- **otp-application-structure** — Rebar assumes the standard directory layout.
- **reltool** — Rebar wraps Reltool for release building.

## Common Errors

- **Error**: Hand-maintaining the `modules` list while also using rebar.
  **Correction**: Let rebar handle it; manual lists drift out of sync.

## Common Confusions

- **Confusion**: Thinking rebar replaces the need to understand `.app` files and releases.
  **Clarification**: Rebar uses "configuration files that are nearly the same"; understanding Reltool and the release structure underneath is still worthwhile.

## Source Reference

Chapter 19: "Building Applications the OTP Way," note in "The Application Resource File"; further mention in Chapter 21, "Reltool Recipes" (the closing note).

## Verification Notes

- Definition: Direct quote from the Chapter 19 note.
- Key Properties: Synthesised from the Chapter 19 and Chapter 21 mentions.
- Confidence: MEDIUM — the book mentions rebar only briefly in notes; the rebar3 tooling note is added for currency.
