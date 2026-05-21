---
concept: Release Packaging
slug: release-packaging
category: applications-releases
subcategory: releases
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Release Is the Word"
chapter_number: 21
pdf_page: null
section: "Packaging the Release"
extraction_confidence: high
aliases:
  - release archive
  - release tarball
  - "make_tar"
prerequisites:
  - erlang-release
  - release-boot-file
extends: []
related:
  - systools
  - reltool
contrasts_with: []
answers_questions:
  - "How do I build an Erlang release?"
  - "What is an Erlang release?"
---

# Release Packaging

## Quick Definition

Release packaging is producing a distributable archive of a release — its applications, boot files, and optionally the ERTS — that can be unpacked and run on a target machine.

## Core Definition

`systools:make_tar/2` "will look for your release files and the ERTS ... Running this function call creates an archive file" (Ch. 21, "Packaging the Release"). The archive unpacks into three directories: `erts-<vsn>/` (the ERTS), `lib/` (all needed applications), and `releases/` (boot files and release metadata).

## Prerequisites

- **Erlang release** — Packaging produces a deployable form of a release.
- **Release boot file** — The boot file is part of the packaged archive.

## Key Properties

1. `systools:make_tar("name-vsn", Options)` creates a `name-vsn.tar.gz` archive.
2. The `{erts, Path}` option bundles the ERTS, making the release self-executable.
3. Omitting `{erts, ...}` produces a release that depends on a pre-installed Erlang.
4. An unpacked release has `erts-<vsn>/`, `lib/`, and `releases/` directories.
5. It is run with `./erts-<vsn>/bin/erl -boot releases/<vsn>/start`.
6. The lightest release omits ERTS and is run with the user's own Erlang via `ERL_LIBS`.
7. The book recommends wrapping the run command in a shell script or batch file.

## Construction / Recognition

## To Package and Run a Release

1. Generate the boot file with `systools:make_script` (or use Reltool).
2. Run `systools:make_tar("name-vsn", [{erts, ErtsPath}]).`
3. Unpack `name-vsn.tar.gz` on the target.
4. Run `./erts-<vsn>/bin/erl -boot releases/<vsn>/start` (optionally with absolute paths and `-noshell`).
5. Wrap the command in a script for convenience.

## Context & Application

The book runs the packaged `erlcount` release with `./erts-5.9.1/bin/erl -boot releases/1.0.0/start -erlcount directory '"<path>"' -noshell`, overriding the `directory` env variable and suppressing the shell. It warns there is "no guarantee that a release will work on any system ever": pure Erlang code is portable, but a bundled ERTS is platform-specific — so cross-platform distribution needs per-platform packages or shipping without ERTS.

## Examples

**Example 1** (Ch. 21): `systools:make_tar("erlcount-1.0", [{erts, "/usr/local/lib/erlang/"}]).` creates `erlcount-1.0.tar.gz`.

**Example 2** (Ch. 21): The unpacked release runs with `./erts-5.9.1/bin/erl -boot releases/1.0.0/start -erlcount directory '"/home/ferd/code/..."' -noshell`.

## Relationships

## Builds Upon

- **Erlang release** — Packaging produces a release's deployable form.
- **Release boot file** — Included in the `releases/` directory.

## Related

- **systools** — `make_tar` does the packaging.
- **reltool** — An alternative that also produces packaged releases, with size control.

## Common Errors

- **Error**: Shipping a release with bundled ERTS to a different OS/architecture.
  **Correction**: ERTS is platform-specific; build per-platform packages or omit ERTS.
- **Error**: Including the `.boot` extension in `-boot`.
  **Correction**: Use the path without the extension.

## Common Confusions

- **Confusion**: Thinking every release archive is self-contained.
  **Clarification**: Only releases packaged *with* the `{erts, ...}` option are self-executable; without it, the target must have Erlang installed.

## Source Reference

Chapter 21: "Release Is the Word," section "Packaging the Release."

## Verification Notes

- Definition: Direct quotes from "Packaging the Release."
- Key Properties: Synthesised from the `make_tar` session and the directory layout.
- Confidence: HIGH — explicitly demonstrated.
