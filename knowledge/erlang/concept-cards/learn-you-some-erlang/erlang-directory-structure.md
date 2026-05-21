---
concept: Erlang Directory Structure
slug: erlang-directory-structure
category: processes-concurrency
subcategory: application-design
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Designing a Concurrent Application"
chapter_number: 13
pdf_page: null
section: "Lay Them Foundations"
extraction_confidence: high
aliases:
  - "standard directory structure"
  - "project layout"
  - "Emakefile"
prerequisites: []
extends: []
related:
  - concurrent-application-design
contrasts_with: []
answers_questions:
  - "How do I structure an Erlang project's directories?"
  - "How do I build a multi-module Erlang project?"
---

# Erlang Directory Structure

## Quick Definition

The standard Erlang project layout uses four directories — `ebin/` for compiled files, `include/` for shared headers, `priv/` for executables, and `src/` for source — reflecting OTP conventions.

## Core Definition

When laying foundations for the reminder application, the chapter prescribes "a standard Erlang directory structure": `ebin/` "is where files will go once they are compiled"; `include/` "is used to store *.hrl* files that are to be included by other applications (the private *.hrl* files are usually kept inside the *src/* directory)"; `priv/` "is used for executables that might need to interact with Erlang, such as specific drivers"; and `src/` "is where all *.erl* files stay." Variations add `conf/`, `doc/`, and `lib/` or `deps/` for third-party libraries, "but the four in our structure usually stay the same, given that they're part of the standard OTP practices." The chapter also shows building such a project with an `Emakefile` (Erlang terms describing the compile recipe) run via `erl -make` or `make:all([load])` (Hébert, ch. 13, "Lay Them Foundations," "A Test Drive").

## Prerequisites

This is a foundational organizational concept with no prerequisites within this chapter.

## Key Properties

1. `ebin/` — compiled `.beam` files
2. `include/` — `.hrl` header files meant to be included by other applications
3. `priv/` — executables and drivers that interact with Erlang
4. `src/` — `.erl` source files (and private `.hrl` files)
5. Optional additions: `conf/` (config), `doc/` (documentation), `lib/` or `deps/` (third-party libraries)
6. The four core directories are part of standard OTP practice
7. An `Emakefile` (Erlang terms) describes the compile recipe; built via `erl -make` or `make:all/1`

## Construction / Recognition

## To Set Up a Project

1. Create `ebin/`, `include/`, `priv/`, and `src/`
2. Put `.erl` source files in `src/`; shared headers in `include/`
3. Write an `Emakefile` specifying `debug_info`, include paths, and `{outdir, "ebin"}`
4. Build with `erl -make` from the project root, or `make:all([load])` from the shell
5. Start the shell with `erl -pa ebin/` so the VM finds the compiled modules

## Examples

> **Emakefile** (ch. 13): `{'src/*', [debug_info, {i, "src"}, {i, "include"}, {outdir, "ebin"}]}.`
>
> **Loading the path** (ch. 13): `erl -pa ebin/` — "the `-pa` *directory* option tells the Erlang VM to add that path to the places it can look for modules."

## Relationships

## Related

- **Concurrent application design** — Laying out directories is an early step of the design method

## Common Errors

- **Error**: Starting the shell without `-pa ebin/` after compiling into `ebin/`
  **Correction**: Use `erl -pa ebin/` so the VM can locate the compiled modules

## Common Confusions

- **Confusion**: Thinking the layout is arbitrary
  **Clarification**: The four core directories are standard OTP practice and are expected by OTP tooling

## Source Reference

Chapter 13, "Designing a Concurrent Application," sections "Lay Them Foundations" and "A Test Drive."

## Verification Notes

- Directory roles and Emakefile: directly from ch. 13
- Confidence: HIGH — explicitly prescribed
