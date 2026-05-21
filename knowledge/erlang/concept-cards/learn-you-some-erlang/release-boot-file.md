---
concept: Release Boot File
slug: release-boot-file
category: applications-releases
subcategory: releases
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Release Is the Word"
chapter_number: 21
pdf_page: null
section: "Creating a Boot File"
extraction_confidence: high
aliases:
  - boot file
  - boot script
  - ".boot file"
prerequisites:
  - erlang-release
  - release-resource-file
extends: []
related:
  - systools
  - release-packaging
contrasts_with: []
answers_questions:
  - "How do I build an Erlang release?"
  - "What is an Erlang release?"
---

# Release Boot File

## Quick Definition

A boot file is the binary file the Erlang VM starts from. It is compiled from a boot script — a list of tuples giving startup instructions such as loading the standard library and kernel.

## Core Definition

"Erlang's VM can start itself with a basic configuration taken from something called a *boot file*. ... That boot file will give basic instructions such as 'load the standard library,' 'load the kernel application,' 'run a given function,' and so on. That boot file is a binary file created from a *boot script* ... which contains tuples that will represent these instructions" (Ch. 21, "Creating a Boot File").

## Prerequisites

- **Erlang release** — The boot file starts a release.
- **Release resource file** — The boot script/file is generated from the `.rel` file.

## Key Properties

1. The VM always starts from some boot file — even a plain `erl` uses a default one.
2. A boot *script* (`.script`) is a human-readable list of `{script, ...}` tuples; the boot *file* (`.boot`) is its binary form.
3. Boot scripts are not written by hand — they are generated from the `.rel` file.
4. `systools:make_script("name-vsn", [local])` generates both the `.script` and `.boot`.
5. The `local` option lets the release run from anywhere, not just the current installation.
6. The VM is pointed at a boot file with the `-boot` argument (path without the `.boot` extension).

## Construction / Recognition

## To Create and Use a Boot File

1. Write the `.rel` resource file.
2. From the release directory: `systools:make_script("name-vsn", [local]).`
3. This produces `name-vsn.script` and `name-vsn.boot`.
4. Start the VM with `erl -boot releases/<vsn>/start` (no `.boot` suffix).

## Context & Application

The book jokingly shows the raw `{script, {Name, Vsn}, [...]}` form and then says "No one really takes the time to do that" — boot scripts are generated. Reltool also produces a boot file, picked automatically when the release's `erl` binary is run (`boot_rel`). When `boot_rel` is not specified, Reltool needs a release named `start_clean` to use as the default.

## Examples

**Example 1** (Ch. 21): `systools:make_script("erlcount-1.0", [local]).` creates `erlcount-1.0.script` and `erlcount-1.0.boot`.

**Example 2** (Ch. 21): The packaged release is run with `./erts-5.9.1/bin/erl -boot releases/1.0.0/start`.

## Relationships

## Builds Upon

- **Release resource file** — The boot script is generated from the `.rel` file.

## Related

- **systools** — `make_script` generates the boot file.
- **release-packaging** — The boot file ends up in the release's `releases/` directory.

## Common Errors

- **Error**: Including the `.boot` extension in the `-boot` argument.
  **Correction**: Give the path *without* the extension, e.g. `-boot releases/1.0.0/start`.

## Common Confusions

- **Confusion**: Thinking the boot script is something you author by hand.
  **Clarification**: It is generated from the `.rel` file by `systools` or Reltool; hand-writing it is impractical.

## Source Reference

Chapter 21: "Release Is the Word," section "Creating a Boot File"; usage in "Packaging the Release."

## Verification Notes

- Definition: Direct quotes from "Creating a Boot File."
- Key Properties: Synthesised from the `make_script` discussion.
- Confidence: HIGH — explicitly defined.
