---
concept: Release Resource File
slug: release-resource-file
category: applications-releases
subcategory: releases
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
  - ".rel file"
  - rel file
  - release file
prerequisites:
  - erlang-release
  - app-file
extends: []
related:
  - systools
  - release-boot-file
  - reltool
contrasts_with:
  - app-file
answers_questions:
  - "How do I build an Erlang release?"
  - "What is an Erlang release?"
---

# Release Resource File

## Quick Definition

The release resource file (`.rel`) is an Erlang term describing a release: its name and version, the ERTS version, and the applications (with versions and start types) it contains.

## Core Definition

The `.rel` file is the release's "list of ingredients" (Ch. 21, "Releases with systools"). It is a single `{release, ...}` tuple naming the release, the ERTS version, and the list of applications to include.

## Prerequisites

- **Erlang release** — The `.rel` file describes a release.
- **App file** — Each listed application has its own `.app` file the tools cross-check.

## Key Properties

1. Format: `{release, {Name, Vsn}, {erts, ErtsVsn}, [AppSpecs]}.`
2. Each application spec is `{App, Vsn}` or `{App, Vsn, StartType}`.
3. `StartType` is `temporary`, `transient`, or `permanent`.
4. Application versions let you mix libraries from different Erlang versions.
5. The release name and version are independent of the constituent applications.
6. It is conventionally named `<release>-<vsn>.rel` and placed at the top of the release directory.
7. Tools (`systools`, Reltool) read it to compute startup order from app dependencies.

## Construction / Recognition

## To Write a .rel File

1. Get ERTS, `kernel`, and `stdlib` versions via `application:which_applications()`.
2. Write `{release, {"name", "1.0.0"}, {erts, "5.9.1"}, [ ... ]}.`
3. List `kernel` and `stdlib` with their versions.
4. List your applications with versions and start types.
5. Save it as `<name>-<vsn>.rel`.

## Context & Application

The book's `erlcount-1.0.rel` lists ERTS 5.9.1, `kernel` 2.15.1, `stdlib` 1.18.1, `{ppool, "1.0.0", permanent}`, and `{erlcount, "1.0.0", transient}`. Being explicit about versions means "if you have many different Erlang installations on a system, you can still use an older version of `stdlib`." Reltool uses a `rel` *tuple* with the same content inside its `{sys, [...]}` configuration.

## Examples

**Example 1** (Ch. 21): 

```erlang
{release,
 {"erlcount", "1.0.0"},
 {erts, "5.9.1"},
 [{kernel, "2.15.1"},
  {stdlib, "1.18.1"},
  {ppool, "1.0.0", permanent},
  {erlcount, "1.0.0", transient}]}.
```

## Relationships

## Builds Upon

- **Erlang release** — The file specifies a release.
- **App file** — Cross-checked against each application's `.app` file.

## Related

- **systools** — Reads the `.rel` file to generate boot scripts.
- **release-boot-file** — Generated from the `.rel` file.
- **reltool** — Uses an equivalent `rel` tuple in its config.

## Contrasts With

- **app-file** — The `.app` file describes one *application*; the `.rel` file describes a whole *release* of many applications plus ERTS.

## Common Errors

- **Error**: Omitting `kernel` or `stdlib` from the application list.
  **Correction**: Always list them with explicit versions; a release without them will not run.
- **Error**: Guessing version numbers.
  **Correction**: Read them from `application:which_applications()` on the target Erlang.

## Common Confusions

- **Confusion**: Thinking the release version must match the applications' versions.
  **Clarification**: The release name/version are independent; the book's `erlcount` release is 1.0.0 but so happen to be its apps, by coincidence.

## Source Reference

Chapter 21: "Release Is the Word," section "Releases with systools" (the `erlcount-1.0.rel` file).

## Verification Notes

- Definition: Adapted from the "list of ingredients" framing.
- Key Properties: The tuple form copied from the source.
- Confidence: HIGH — explicitly shown with a full example.
