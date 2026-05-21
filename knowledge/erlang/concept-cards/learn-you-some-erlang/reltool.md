---
concept: Reltool
slug: reltool
category: tooling
subcategory: release-tools
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Release Is the Word"
chapter_number: 21
pdf_page: null
section: "Releases with Reltool"
extraction_confidence: high
aliases:
  - "reltool"
prerequisites:
  - erlang-release
  - release-resource-file
extends: []
related:
  - systools
  - release-packaging
  - rebar-build-tool
contrasts_with:
  - systools
answers_questions:
  - "How do I build an Erlang release?"
  - "What is an Erlang release?"
---

# Reltool

## Quick Definition

Reltool is the more powerful OTP release-building tool. It works from a `{sys, [...]}` configuration file and gives fine-grained control over what goes into a release, at the cost of more complexity.

## Core Definition

"It is possible to do better with Reltool, as we get a lot more power, although the trade-off is increased complexity. Reltool works from a configuration file" of the form `{sys, [Options]}` (Ch. 21, "Releases with Reltool"). The configuration takes information at three levels: release-wide, application-specific, and module-specific.

## Prerequisites

- **Erlang release** — Reltool builds releases.
- **Release resource file** — Reltool's `rel` tuple plays the role of the `.rel` file.

## Key Properties

1. Configured by a single `{sys, [...]}` term.
2. Three configuration levels: release-wide, per-application (`app` tuples), per-module.
3. Essential options: `lib_dirs` (where applications reside), `rel` (apps to start, like a `.rel` file), `boot_rel` (which release the included `erl` boots).
4. `incl_cond` (`include` / `exclude` / `derived`) controls which applications are pulled in.
5. `profile` (`development`, `standalone`, `embedded`) controls what files are kept.
6. `excl_app_filters` / `incl_app_filters` filter files in or out by regular expression.
7. `app_file` (`strip`/`all`) and `debug_info` (`strip`/`keep`) trade size against debuggability.
8. When `boot_rel` is unspecified, a release named `start_clean` is the default.

## Construction / Recognition

## To Build a Release with Reltool

1. Write a `{sys, [...]}` config with at least `lib_dirs`, `rel`, and `boot_rel`.
2. Set `incl_cond` and per-`app` overrides to control inclusion.
3. Pick a `profile` (`embedded` for the smallest releases).
4. Add `excl_app_filters` (e.g. `"_tests.beam$"`) to drop unwanted files.
5. Generate and package the release.

## Context & Application

The book gives Reltool recipes: a development release (defaults, optionally `incl_cond, include` to grab everything); excluding a specific application with an `app` tuple overriding `incl_cond`; importing only part of a library with `incl_app_filters`; and minimal releases using `profile, embedded` plus stripping. A general release weighs ~35 MB; a minimized one drops to under 20 MB, most of which is the ~18.5 MB ERTS. The book notes Reltool *needs* `kernel`/`stdlib` listed in the app files or the release will not run.

## Examples

**Example 1** (Ch. 21): Minimal config — `{sys, [{lib_dirs, ["..."]}, {rel, "erlcount", "1.0.0", [kernel, stdlib, ppool, erlcount]}, {boot_rel, "erlcount"}]}.`

**Example 2** (Ch. 21): A size-reduced config sets `{profile, embedded}`, `{app_file, strip}`, `{debug_info, strip}`, `{incl_cond, exclude}`, and `{excl_app_filters, ["_tests.beam$"]}`.

## Relationships

## Builds Upon

- **Release resource file** — Reltool's `rel` tuple mirrors the `.rel` file.

## Related

- **systools** — The simpler alternative.
- **release-packaging** — Reltool produces packaged releases.
- **rebar-build-tool** — Wraps Reltool to automate releases.

## Contrasts With

- **systools** — `systools` is the simple "Easy-Bake Oven"; Reltool is more powerful and more complex, with size control, profiles, and filters.

## Common Errors

- **Error**: Omitting `kernel`/`stdlib` from the app files when using Reltool.
  **Correction**: The book stresses this is "absolutely vital" — Reltool releases need them or the VM cannot even shut down cleanly.
- **Error**: Expecting a single Reltool option to work in isolation.
  **Correction**: "You need a bunch of these options at once or nothing will work."

## Common Confusions

- **Confusion**: Thinking `incl_cond, include` plus an exclude on one app is the way to get a *minimal* release.
  **Clarification**: For minimal releases, start restrictive (`incl_cond, exclude` or `derived`) and explicitly include only what you need.

## Source Reference

Chapter 21: "Release Is the Word," sections "Releases with Reltool," "Reltool Options," and "Reltool Recipes."

## Verification Notes

- Definition: Direct quotes from "Releases with Reltool."
- Key Properties: Synthesised from the options and recipes sections.
- Confidence: HIGH — extensively documented with worked configs.
