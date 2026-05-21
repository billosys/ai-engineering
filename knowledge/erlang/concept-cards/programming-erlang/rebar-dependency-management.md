---
# === CORE IDENTIFICATION ===
concept: Rebar Dependency Management
slug: rebar-dependency-management

# === CLASSIFICATION ===
category: tooling
subcategory: dependency-management
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Third-Party Programs"
chapter_number: 25
pdf_page: null
section: "Integrating External Programs with Our Code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - rebar.config deps
  - recursive dependency fetching

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rebar
extends:
  - rebar
related:
  - otp-application-skeleton
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I include a GitHub project in my own Erlang application?"
  - "How does rebar fetch and compile dependencies?"
---

# Quick Definition

Rebar dependency management is the mechanism by which rebar reads a `rebar.config` `deps` list and recursively fetches and compiles each declared dependency (and its dependencies) from GitHub.

# Core Definition

To include a third-party program in a project, you create a `rebar.config` "dependencies file" in the project's top-level directory listing the deps. The command `rebar get-deps` "fetched bitcask from GitHub and stored it in a subdirectory called deps." Because a dependency may itself depend on other programs (a "recursive dependency"), "Rebar recursively fetches any dependencies that bitcask might require and stores them in the deps subdirectory" ("Integrating External Programs with Our Code"). `rebar compile` then builds the fetched dependencies.

# Prerequisites

- **Rebar** — Dependency management is a feature of the rebar tool; you must have rebar installed and know its commands.

# Key Properties

1. Dependencies are declared in a `rebar.config` file as a `{deps, [...]}` list.
2. Each dep entry names the app, a version regex, and a git source: `{Name, ".*", {git, Url, Ref}}`.
3. `rebar get-deps` fetches all declared dependencies into a `deps` subdirectory.
4. Fetching is recursive: a dependency's own dependencies are pulled automatically.
5. `rebar compile` builds the fetched dependency code.
6. Dependencies may be local (a `deps` dir inside the project) or shared (a `deps` dir outside, used by several projects).

# Construction / Recognition

## To Construct/Create:
1. Create a `rebar.config` in the project's top-level directory.
2. Add a `{deps, [...]}` list with one `{Name, VsnRegex, {git, Url, Ref}}` tuple per dependency.
3. Run `rebar get-deps` to fetch dependencies (recursively) into `deps`.
4. Run `rebar compile` to build them.
5. Ensure the runtime code path includes each dependency's `ebin` directory (e.g., via a `-pa` flag or `code:add_path/1` in `${HOME}/.erlang`).

## To Identify/Recognize:
1. A `rebar.config` containing a `deps` tuple.
2. A `deps/` directory populated with cloned git repositories.

# Context & Application

- **Typical contexts**: Any project that reuses third-party Erlang code.
- **Common applications**: Pulling in `bitcask`, `cowboy`, `ranch`, etc. from GitHub. A shared `erlang_imports` directory can hold deps reused by many local projects.
- **Historical/stylistic notes**: The book uses rebar 2.x git deps; modern `rebar3` adds Hex package support, but the `rebar.config` `deps` concept is the same.

# Examples

**Example 1** ("Integrating External Programs with Our Code" — `bertie/rebar.config`): Declaring `bitcask` as a dependency:

```erlang
{deps, [
  {bitcask, ".*", {git, "git://github.com/basho/bitcask.git", "master"}}
]}.
```

**Example 2** ("Integrating External Programs with Our Code"): Running `make`/`rebar get-deps` pulls `bitcask` and, recursively, the `meck` library that `bitcask` uses for testing — `Pulling meck from {git,"git://github.com/eproxus/meck"}`.

**Example 3** ("Making a Local Copy of the Dependencies"): A shared `rebar.config` listing `cowboy`, `ranch`, and `bitcask`; `rebar get-deps` recursively also pulls `proper` (a dependency of cowboy).

# Relationships

## Builds Upon
- **Rebar** — Dependency management is one of rebar's core capabilities.

## Enables
- Reuse of third-party libraries such as bitcask and cowboy in your own application.

## Related
- **OTP application skeleton** — Dependencies are typically OTP applications fetched into a project's layout.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Forgetting to add fetched dependencies to the code path before running the program.
  **Correction**: Pass `-pa deps/<name>/ebin` on the command line, or add the paths in `${HOME}/.erlang`.

- **Error**: Listing only direct dependencies and manually fetching transitive ones.
  **Correction**: Let `rebar get-deps` recurse; it fetches transitive dependencies automatically.

# Common Confusions

- **Confusion**: Thinking each project must store its own copy of every dependency.
  **Clarification**: You can keep a shared dependency directory outside the project and point Erlang at it, avoiding duplication.

# Source Reference

Chapter 25: Third-Party Programs, Sections "Integrating External Programs with Our Code" and "Making a Local Copy of the Dependencies." See the `bertie/rebar.config` and `bertie/Makefile` listings.

# Verification Notes

- Definition source: Direct adaptation from "Integrating External Programs with Our Code."
- Confidence rationale: HIGH — the source gives the exact `rebar.config` syntax and shows recursive fetching output.
- Uncertainties: rebar 2.x git-only deps; modern `rebar3` also supports Hex packages.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
