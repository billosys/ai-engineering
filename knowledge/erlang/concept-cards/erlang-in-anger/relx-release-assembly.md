---
concept: Relx Release Assembly
slug: relx-release-assembly
category: tooling
subcategory: releases
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Building Open Source Erlang Software"
chapter_number: 2
pdf_page: null
section: "OTP Releases"
extraction_confidence: high
aliases:
  - "relx"
prerequisites:
  - otp-release
  - rebar3
extends: []
related:
  - project-structure
  - dependency-specification
contrasts_with: []
answers_questions:
  - "How do I build a release with rebar3?"
---

# Quick Definition

`relx` is the library used by both `rebar3` and `erlang.mk` to assemble OTP releases; it is configured by a `relx` tuple in `rebar.config`.

# Core Definition

From Chapter 2, section "OTP Releases": "Both `rebar3` and `erlang.mk` rely on the `relx` library to assemble releases." A `relx` configuration tuple within `rebar.config` for a nested-applications project looks like:

```text
{relx, [
  {release, {demo, "1.0.0"},
    [myapp1, myapp2, ..., recon]},
     
  {include_erts, false} % will use local Erlang install
]}
```

# Prerequisites

- `otp-release` — `relx` assembles releases.
- `rebar3` — the build tool that drives `relx`.

# Key Properties

1. Used by both `rebar3` and `erlang.mk` to assemble releases.
2. Configured via a `{relx, [...]}` tuple inside `rebar.config` (or a separate `relx.config` file).
3. The `{release, {Name, Vsn}, [Apps]}` tuple names the release and lists its top-level applications.
4. `{include_erts, false}` makes the release use the local Erlang install rather than bundling its own VM.
5. `rebar3 release` builds the release into `_build/default/rel/`; `rebar3 tar` produces a deployable tarball such as `_build/default/rel/demo/demo-1.0.0.tar.gz`.
6. Alternatives — `systools` and `reltool` — exist and give more power if `relx`'s defaults are unsatisfactory.

# Construction / Recognition

Add a `{relx, [...]}` tuple to `rebar.config` declaring the release name, version, and applications; choose whether to `include_erts`. Run `rebar3 release` to build, `rebar3 tar` to package for deployment.

# Context & Application

`relx` is the standard mechanism for turning a collection of OTP applications into a bootable, deployable release. It is the bridge between the nested project structure and a production artifact.

# Examples

From Chapter 2, section "OTP Releases": the `{relx, [{release, {demo, "1.0.0"}, [myapp1, myapp2, ..., recon]}, {include_erts, false}]}` tuple is given, followed by: "Calling `rebar3 release` will build a release, to be found in the `_build/default/rel/` directory. Calling `rebar3 tar` will generate a tarball at `_build/default/rel/demo/demo-1.0.0.tar.gz`."

# Relationships

## Builds Upon
- `otp-release` — the artifact it produces.
- `rebar3` — the tool that invokes it.

## Enables
Production-ready, deployable release artifacts.

## Related
- `project-structure` — the nested `apps/` layout feeds `relx`.
- `dependency-specification` — dependencies must be resolved before assembly.

## Contrasts With
Nothing directly — `systools`/`reltool` are alternatives, not contrasts.

# Common Errors

- Setting `include_erts` to `false` and then deploying to a host without a matching Erlang install — the release will not run.

# Common Confusions

- `relx` is a library, not a standalone command you usually invoke directly; you drive it through `rebar3` (or `erlang.mk`) commands like `rebar3 release`.

# Source Reference

Chapter 2: Building Open Source Erlang Software, Section "OTP Releases". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 2, section "OTP Releases."
- Confidence rationale: high — config tuple and commands shown verbatim.
- Uncertainties: none.
- Cross-reference status: Verified
