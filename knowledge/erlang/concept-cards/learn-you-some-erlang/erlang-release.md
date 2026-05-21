---
concept: Erlang Release
slug: erlang-release
category: applications-releases
subcategory: releases
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Release Is the Word"
chapter_number: 21
pdf_page: null
section: "Release Is the Word"
extraction_confidence: high
aliases:
  - release
  - OTP release
prerequisites:
  - otp-application
  - application-dependency
extends: []
related:
  - release-resource-file
  - systools
  - reltool
  - release-boot-file
contrasts_with: []
answers_questions:
  - "What is an Erlang release?"
  - "How does an OTP application relate to a release?"
  - "How do I build an Erlang release?"
---

# Erlang Release

## Quick Definition

An Erlang release is a packaged, deployable system bundling a set of OTP applications with the minimal resources and dependencies — optionally including the Erlang Run-Time System itself.

## Core Definition

"OTP releases are part of a system made to help package applications with the minimal resources and dependencies" (Ch. 21, opening). A minimal release for the `erlcount` application bundles an Erlang Run-Time System (ERTS), the standard library, the kernel library, and the application(s) themselves. The book covers two ways to build releases: `systools` and Reltool.

## Prerequisites

- **OTP application** — A release packages OTP applications.
- **Application dependency** — Release tools use dependency lists to order startup.

## Key Properties

1. A release bundles one or more OTP applications plus the libraries they need (`kernel`, `stdlib`).
2. It may include the ERTS, making it self-executable, or omit it to rely on an installed Erlang.
3. It is described by a release resource (`.rel`) file.
4. From the `.rel` file, tools generate a boot file/script the VM starts from.
5. A packaged release expands to `erts-<vsn>/`, `lib/`, and `releases/` directories.
6. Each application in a release can be marked `temporary`, `transient`, or `permanent`.
7. The release version is independent of its constituent applications' versions.

## Construction / Recognition

## To Build a Release

1. Add `description` and explicit `kernel`/`stdlib` dependencies to every app's `.app` file.
2. Compile all applications.
3. Write a `.rel` resource file listing ERTS, libraries, and applications.
4. Generate a boot file (with `systools` or Reltool).
5. Package the release into a tarball (optionally with ERTS).

## Context & Application

The book frames releases as the missing step: "we haven't shipped a single Erlang executable yet!" A release is what turns compiled applications into "a functioning Erlang system you can easily deploy or ship." It warns there is "no guarantee that a release will work on any system ever" — pure Erlang code is portable but the bundled ERTS may not be, so cross-platform distribution needs per-platform packages or shipping without ERTS.

**Tooling note:** The book uses `systools` and Reltool. Modern projects typically build releases with **rebar3** (which uses `relx` underneath); the underlying `.rel`/boot-file concepts are unchanged.

## Examples

**Example 1** (Ch. 21): The `erlcount 1.0.0` release bundles ERTS, `kernel`, `stdlib`, `ppool`, and `erlcount`.

**Example 2** (Ch. 21): A packaged release unpacks to `erts-5.9.1/`, `lib/`, and `releases/`; it is run with `./erts-5.9.1/bin/erl -boot releases/1.0.0/start`.

## Relationships

## Builds Upon

- **OTP application** — Releases package applications.

## Related

- **release-resource-file** — The `.rel` file describing the release.
- **systools** — One tool for building releases.
- **reltool** — A more powerful release-building tool.
- **release-boot-file** — Generated from the release for the VM to start from.

## Common Errors

- **Error**: Building a release without first compiling all applications.
  **Correction**: Run each `Emakefile` with `erl -make`; release tools do not compile for you.
- **Error**: Assuming a release with bundled ERTS runs on any OS.
  **Correction**: The ERTS is platform-specific; ship per-platform packages or omit ERTS.

## Common Confusions

- **Confusion**: Thinking the release version equals its applications' versions.
  **Clarification**: The release has its own version, "unrelated to the `ppool` and `erlcount` applications."

## Source Reference

Chapter 21: "Release Is the Word," opening and sections "Releases with systools" and "Releases with Reltool."

## Verification Notes

- Definition: Direct quote from the chapter opening.
- Key Properties: Synthesised from the systools ingredient list and packaging discussion.
- Confidence: HIGH — explicitly defined; cross-chapter shared slug referenced by other agents.
