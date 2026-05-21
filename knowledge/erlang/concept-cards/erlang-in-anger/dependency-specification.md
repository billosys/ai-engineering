---
concept: Dependency Specification
slug: dependency-specification
category: tooling
subcategory: dependencies
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Building Open Source Erlang Software"
chapter_number: 2
pdf_page: null
section: "OTP Applications"
extraction_confidence: high
aliases:
  - "deps tuple"
prerequisites:
  - rebar3
extends: []
related:
  - application-dependency-graph
  - project-structure
contrasts_with: []
answers_questions:
  - "How do I specify dependencies?"
  - "How do I build a release with rebar3?"
---

# Quick Definition

Dependency specification is the declaration, in `rebar.config`'s `deps` tuple, of the external packages or source repositories an application requires; `rebar3` fetches them project-locally.

# Core Definition

From Chapter 2, section "OTP Applications": dependencies "can be specified for `rebar3` by adding a few config lines to `rebar.config`":

```text
{deps, [
  %% Hex.pm Packages
  myapp,
  {myapp,"1.0.0"},
  %% source dependencies 
  {myapp, {git, "git://github.com/user/myapp.git", {ref, "aef728"}}},
  {myapp, {git, "https://github.com/user/myapp.git", {branch, "master"}}},
  {myapp, {hg, "https://othersite.com/user/myapp", {tag, "3.0.0"}}}
 ]}.
```

"Dependencies are fetched directly from a `git` (or `hg`) source or as a package from `hex.pm` in a level-order traversal."

# Prerequisites

- `rebar3` — dependency specification is a `rebar3` config feature.

# Key Properties

1. Declared in the `{deps, [...]}` tuple of `rebar.config`.
2. A dependency can be a Hex.pm package (bare name, or `{name, "version"}`) or a source dependency from `git` or `hg`.
3. Source dependencies pin a `ref`, `branch`, or `tag`.
4. Dependencies are fetched in a level-order (breadth-first) traversal of the dependency tree.
5. Compile options for dependencies are added via `{erl_opts, List}` in the config file.
6. `rebar3 compile` downloads all dependencies and builds them together with your app.

# Construction / Recognition

Add a `{deps, [...]}` tuple to `rebar.config`, listing each dependency in one of the supported forms. Run `rebar3 compile` to fetch and build. The fetched copies land in the project-local `_build/` directory, and `rebar.lock` records resolved versions.

# Context & Application

This is how an Erlang project declares what it depends on. It feeds both the build process and (indirectly, via app files) the application dependency graph.

# Examples

From Chapter 2, section "OTP Applications": the `{deps, [...]}` block above shows all five supported forms — bare Hex name, versioned Hex package, git `ref`, git `branch`, and hg `tag`.

# Relationships

## Builds Upon
- `rebar3` — the tool that consumes the spec.

## Enables
Reproducible builds via project-local dependency fetching.

## Related
- `application-dependency-graph` — the runtime/app-file view of dependencies.
- `project-structure` — `_build/` and `rebar.lock` are where resolved dependencies land.

## Contrasts With
Nothing directly.

# Common Errors

- Forgetting that dependencies are resolved in level-order (breadth-first) traversal, which affects which transitive version wins on conflict.

# Common Confusions

- The `rebar.config` `deps` tuple (what the build tool fetches) is distinct from the app file's `applications` tuple (what OTP starts) — they overlap but are not the same list.

# Source Reference

Chapter 2: Building Open Source Erlang Software, Section "OTP Applications". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 2, section "OTP Applications."
- Confidence rationale: high — all dependency forms shown verbatim.
- Uncertainties: none.
- Cross-reference status: Verified
