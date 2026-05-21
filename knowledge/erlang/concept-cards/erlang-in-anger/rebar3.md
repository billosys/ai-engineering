---
concept: rebar3
slug: rebar3
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
  - erlang-mk
  - dependency-specification
  - relx-release-assembly
  - project-structure
contrasts_with:
  - erlang-mk
answers_questions:
  - "How do I build a release with rebar3?"
  - "What build tool should I use for Erlang?"
---

# Quick Definition

`rebar3` is the de-facto standard Erlang build tool and package manager, used to develop, fetch dependencies for, and release Erlang libraries and systems in a repeatable manner.

# Core Definition

From Chapter 2: "The main build tools supported are `rebar3` and `erlang.mk`. The former is a build tool and package manager trying to make it easy to develop and release Erlang libraries and systems in a repeatable manner." The book focuses on `rebar3` "given it's the de-facto standard."

# Prerequisites

- `otp-application` — `rebar3` builds OTP applications and releases.

# Key Properties

1. Both a build tool and a package manager.
2. Keeps everything project-local: build artifacts and dependency copies go in a `_build/` directory; no mainstream Erlang tool installs packages globally (except as a local cache of unbuilt packages).
3. Generates the `_build/` directory and the `rebar.lock` file automatically.
4. Configured through `rebar.config` (dependencies via `{deps, ...}`, compile options via `{erl_opts, List}`).
5. `erlang.mk` applications tend to be usable as `rebar3` dependencies, and vice versa.
6. Relies on the `relx` library to assemble releases.

# Construction / Recognition

Common commands from Chapter 2:
- `rebar3 compile` — downloads all dependencies, then builds them and your app at once.
- `rebar3 release` — builds a release into `_build/default/rel/`.
- `rebar3 tar` — generates a deployable tarball (e.g. `_build/default/rel/demo/demo-1.0.0.tar.gz`).

# Context & Application

`rebar3` is the standard tool for building, dependency-managing, and releasing open-source Erlang software. The presence of `rebar.config`, `rebar.lock`, and a `_build/` directory signals a `rebar3`-managed project.

# Examples

From Chapter 2: "You can call `rebar3 compile`, which will download all dependencies, and then build them and your app at once." And: "Calling `rebar3 release` will build a release, to be found in the `_build/default/rel/` directory."

# Relationships

## Builds Upon
- `otp-application` — the unit it builds.

## Enables
- `relx-release-assembly` — `rebar3` drives `relx` to assemble releases.
- `dependency-specification` — `rebar.config` declares dependencies.

## Related
- `project-structure` — `rebar3` defines the `_build/`, `rebar.lock` layout.

## Contrasts With
- `erlang-mk` — the alternative build tool: a fancy makefile offering more flexibility but a bit less for production and releases.

# Common Errors

- Distributing the `_build/` directory when publishing source code — Chapter 2 says to ship *without* it, since other developers' apps may depend on the same applications and the build system de-duplicates.

# Common Confusions

- `rebar3` does not install packages globally; dependencies are project-local by design to avoid inter-project conflicts.
- Some projects vendor a copy of `rebar3` itself; you may still install it globally or keep a local copy for a specific version.

# Source Reference

Chapter 2: Building Open Source Erlang Software. (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 2.
- Confidence rationale: high — explicitly described with commands.
- Uncertainties: none.
- Cross-reference status: Verified
