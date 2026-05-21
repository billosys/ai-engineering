---
concept: erlang.mk
slug: erlang-mk
category: tooling
subcategory: build-tools
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Building Open Source Erlang Software"
chapter_number: 2
pdf_page: null
section: "Building Open Source Erlang Software"
extraction_confidence: high
aliases: []
prerequisites:
  - otp-application
extends: []
related:
  - rebar3
  - relx-release-assembly
contrasts_with:
  - rebar3
answers_questions:
  - "What build tool should I use for Erlang?"
---

# Quick Definition

`erlang.mk` is an alternative Erlang build tool — "a very fancy makefile" — that offers more flexibility than `rebar3` but a bit less support for production and releases.

# Core Definition

From Chapter 2: "The main build tools supported are `rebar3` and `erlang.mk`. ... the latter is a very fancy makefile that offers a bit less for production and releases but allows more flexibility."

# Prerequisites

- `otp-application` — `erlang.mk` builds OTP applications and releases.

# Key Properties

1. Implemented as a makefile rather than a standalone tool.
2. Offers more flexibility than `rebar3`, at the cost of a bit less production/release tooling.
3. Like `rebar3`, relies on the `relx` library to assemble releases.
4. `erlang.mk` applications tend to be supported by `rebar3` as dependencies, and the reverse is also true — the two ecosystems interoperate.

# Construction / Recognition

A project using `erlang.mk` is recognized by a `Makefile` that includes `erlang.mk`. Release assembly still goes through `relx`, configured similarly to a `rebar3` project.

# Context & Application

`erlang.mk` is the choice for teams that want makefile-level flexibility. The book focuses on `rebar3` because it is the de-facto standard, but treats `erlang.mk` as a fully supported, interoperable alternative.

# Examples

From Chapter 2: "Both `rebar3` and `erlang.mk` rely on the `relx` library to assemble releases." Chapter 1's footnotes also point to `erlang.mk`'s documentation for understanding relx-based releases.

# Relationships

## Builds Upon
- `otp-application` — the unit it builds.

## Enables
- `relx-release-assembly` — `erlang.mk` drives `relx` for releases.

## Related
- `rebar3` — the standard alternative; the two interoperate as dependency sources.

## Contrasts With
- `rebar3` — `rebar3` is a standalone build tool and package manager and the de-facto standard; `erlang.mk` is a flexible makefile with less production/release support.

# Common Errors

- Assuming `erlang.mk` and `rebar3` projects cannot consume each other — they can; each can use the other's applications as dependencies.

# Common Confusions

- "A bit less for production and releases" does not mean `erlang.mk` cannot build releases — it still uses `relx`; the difference is in convenience and tooling.

# Source Reference

Chapter 2: Building Open Source Erlang Software. (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 2.
- Confidence rationale: high — explicitly described and contrasted with `rebar3`.
- Uncertainties: the source gives only a brief characterization of `erlang.mk`.
- Cross-reference status: Verified
