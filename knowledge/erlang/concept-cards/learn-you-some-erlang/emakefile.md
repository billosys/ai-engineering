---
concept: Emakefile
slug: emakefile
category: tooling
subcategory: build-tools
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building Applications the OTP Way"
chapter_number: 19
pdf_page: null
section: "Converting the Pool"
extraction_confidence: high
aliases:
  - "Emakefile"
  - "erl -make"
prerequisites:
  - otp-application-structure
extends: []
related:
  - otp-application-structure
  - rebar-build-tool
contrasts_with: []
answers_questions:
  - "How do I structure an OTP application?"
---

# Emakefile

## Quick Definition

An `Emakefile` is a file of Erlang terms telling the compiler which source files to build and with what options. It is consumed by `erl -make` and `make:all/1`.

## Core Definition

The book adds "an Emakefile (appropriately named `Emakefile`, placed in the app's base directory) to help us compile and run things" (Ch. 19, "Converting the Pool"). It is a list of `{Path, Options}` terms; the compiler reads it to know which directories to compile and where to put the `.beam` output.

## Prerequisites

- **OTP application structure** — The `Emakefile` references the `src/`, `test/`, `include/`, and `ebin/` directories.

## Key Properties

1. Named exactly `Emakefile`, placed at the application's base directory.
2. Each entry is `{PathGlob, [Options]}`.
3. Options can include `debug_info`, `{i, "include/"}` (header search path), `{outdir, "ebin/"}` (output directory).
4. Built from the shell with `erl -make`, or in a running VM with `make:all([load])`.
5. Release tools do *not* compile for you — you must run the `Emakefile`s first.

## Construction / Recognition

## To Write an Emakefile

1. Create a file named `Emakefile` in the app's base directory.
2. Add an entry per source directory: `{"src/*", [debug_info, {i,"include/"}, {outdir,"ebin/"}]}.`
3. Add a similar entry for `test/*` if you have tests.
4. Compile with `erl -make`.

## Context & Application

The book's `Emakefile` for `ppool`:

```erlang
{"src/*", [debug_info, {i,"include/"}, {outdir, "ebin/"}]}.
{"test/*", [debug_info, {i,"include/"}, {outdir, "ebin/"}]}.
```

Chapter 21 stresses: before building a release "you'll need to ... compile all your applications. Successively run your Emakefile files (with `erl -make`)" — otherwise "you'll end up with a release without code to run." Modern projects use rebar3 instead, which acts like an Emakefile and more.

## Examples

**Example 1** (Ch. 19): The two-line `ppool` `Emakefile` compiling `src/*` and `test/*` with `debug_info`, `include/` on the search path, output to `ebin/`.

**Example 2** (Ch. 19): `make:all([load])` recompiles and loads all modules from within a running VM.

## Relationships

## Builds Upon

- **OTP application structure** — The `Emakefile` references the standard directories.

## Related

- **rebar-build-tool** — Rebar "can act the way Emakefiles do," superseding hand-written ones.

## Common Errors

- **Error**: Building a release without running the `Emakefile`s first.
  **Correction**: Compile each application with `erl -make`; release tools do not compile for you.

## Common Confusions

- **Confusion**: Confusing `Emakefile` with a Unix `Makefile`.
  **Clarification**: An `Emakefile` is a list of Erlang terms read by the Erlang compiler (`erl -make`), not a `make(1)` build file.

## Source Reference

Chapter 19: "Building Applications the OTP Way," section "Converting the Pool"; compile-first warning in Chapter 21, "Compiling the Applications."

## Verification Notes

- Definition: Adapted from "Converting the Pool."
- Key Properties: `Emakefile` content copied from the source.
- Confidence: HIGH — shown verbatim.
