---
concept: systools
slug: systools
category: tooling
subcategory: release-tools
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Release Is the Word"
chapter_number: 21
pdf_page: null
section: "Releases with systools"
extraction_confidence: high
aliases:
  - "systools application"
prerequisites:
  - erlang-release
  - release-resource-file
extends: []
related:
  - release-boot-file
  - release-packaging
  - reltool
contrasts_with:
  - reltool
answers_questions:
  - "How do I build an Erlang release?"
  - "What is an Erlang release?"
---

# systools

## Quick Definition

`systools` is the simplest OTP tool for building Erlang releases. From a `.rel` file it generates a boot script and boot file, and it can package a release into a distributable tarball.

## Core Definition

"The `systools` application is the simplest one to use to build Erlang releases. It's the Easy-Bake Oven of Erlang releases" (Ch. 21, "Releases with systools"). Given a `.rel` file, `systools:make_script/2` produces the boot script and boot file, and `systools:make_tar/2` produces a release archive.

## Prerequisites

- **Erlang release** — `systools` builds releases.
- **Release resource file** — `systools` operates on the `.rel` file.

## Key Properties

1. The simplest release-building tool; less powerful than Reltool.
2. `systools:make_script("name-vsn", Options)` generates `.script` and `.boot` files.
3. The `local` option makes the release runnable from anywhere, not just the current installation.
4. `systools:make_tar("name-vsn", Options)` produces a `.tar.gz` release archive.
5. The `{erts, Path}` option to `make_tar` bundles ERTS, making the release self-executable.
6. It reads app dependency lists to figure out correct startup order automatically.
7. Run it from the release directory with `erl -env ERL_LIBS .`

## Construction / Recognition

## To Build a Release with systools

1. Compile all applications.
2. Write the `.rel` file.
3. Start `erl -env ERL_LIBS .` from the release directory.
4. Run `systools:make_script("name-vsn", [local]).` → `.script` + `.boot`.
5. Run `systools:make_tar("name-vsn", [{erts, ErtsPath}]).` → `name-vsn.tar.gz`.
6. Unpack and run with `./erts-<vsn>/bin/erl -boot releases/<vsn>/start`.

## Context & Application

The book uses `systools` as the gentle introduction to releases before the more powerful Reltool. Its limitations: "We have very little control over how things are done. Manually specifying the path to the boot file and whatnot is kind of painful. Moreover, the files are a bit large." Omitting the `{erts, ...}` option produces a release that depends on Erlang already being installed.

## Examples

**Example 1** (Ch. 21): `1> systools:make_script("erlcount-1.0", [local]).` → creates `erlcount-1.0.script` and `erlcount-1.0.boot`.

**Example 2** (Ch. 21): `2> systools:make_tar("erlcount-1.0", [{erts, "/usr/local/lib/erlang/"}]).` → creates `erlcount-1.0.tar.gz`.

## Relationships

## Builds Upon

- **Release resource file** — `systools` reads the `.rel` file.

## Related

- **release-boot-file** — `make_script` generates it.
- **release-packaging** — `make_tar` produces the archive.

## Contrasts With

- **reltool** — Reltool gives far more control (size reduction, profiles, filters) at the cost of more complexity; `systools` is simpler but coarser.

## Common Errors

- **Error**: Running `systools` before compiling the applications.
  **Correction**: Compile first with `erl -make`; "you'll end up with a release without code to run."
- **Error**: Expecting a non-ERTS release to run on a machine without Erlang.
  **Correction**: Pass `{erts, Path}` to `make_tar` to bundle ERTS.

## Common Confusions

- **Confusion**: Thinking `make_script` produces the deployable package.
  **Clarification**: `make_script` only generates the boot script/file; `make_tar` produces the distributable archive.

## Source Reference

Chapter 21: "Release Is the Word," section "Releases with systools" (subsections "Creating a Boot File" and "Packaging the Release").

## Verification Notes

- Definition: Direct quote from "Releases with systools."
- Key Properties: Synthesised from the `make_script`/`make_tar` worked sessions.
- Confidence: HIGH — explicitly demonstrated.
