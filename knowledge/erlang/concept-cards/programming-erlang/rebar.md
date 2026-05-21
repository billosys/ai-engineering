---
# === CORE IDENTIFICATION ===
concept: Rebar
slug: rebar

# === CLASSIFICATION ===
category: tooling
subcategory: build-tools
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Third-Party Programs"
chapter_number: 25
pdf_page: null
section: "Making a Shareable Archive and Managing Your Code with Rebar"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - rebar build tool

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - rebar-dependency-management
  - otp-application-skeleton
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create, compile, and package an Erlang project?"
  - "What is the de facto standard tool for managing Erlang projects?"
---

# Quick Definition

Rebar is the de facto standard build tool for Erlang: it creates new projects, compiles them, packages them, and integrates them with other projects.

# Core Definition

"Rebar, written by Dave Smith, has become the de facto standard for managing Erlang projects. Using rebar, the user can create new projects, compile the projects, package them, and integrate them with other projects. Rebar is integrated with GitHub so users can easily fetch other rebar projects from GitHub and integrate them with their applications" ("Third-Party Programs" introduction). Rebar generates standard OTP application boilerplate and drives the compile process from a project directory.

# Prerequisites

This is a foundational tooling concept with no prerequisites within this source.

# Key Properties

1. It is the de facto standard tool for managing Erlang projects.
2. It can create new projects, compile, package, and integrate them.
3. It generates standard OTP application boilerplate via `rebar create-app appid=Name`.
4. It is integrated with GitHub for fetching and reusing other projects.
5. It is distributed as a self-contained executable (itself a zip file).

# Construction / Recognition

## To Construct/Create:
1. Install rebar: obtain the prebuilt binary, make it executable, and put it on your `PATH`.
2. Verify the install with `rebar -V`.
3. In a project directory, run `rebar create-app appid=Name` to generate OTP boilerplate.
4. Run `rebar compile` to build the project.

## To Identify/Recognize:
1. A project with a `rebar.config` file and a `src/<name>.app.src` is a rebar project.
2. Builds are driven by `rebar` subcommands rather than raw `erlc`.

# Context & Application

- **Typical contexts**: Managing, building, and publishing any non-trivial Erlang project.
- **Common applications**: Creating an open-source project, compiling it, and publishing it on GitHub.
- **Historical/stylistic notes**: The book uses rebar 2.x (`rebar 2.0.0 R14B04`); the modern successor is `rebar3`. The taxonomy targets OTP 27+, where `rebar3` is standard, but the book's mechanics (`create-app`, `compile`, `rebar.config` deps) carry over conceptually.

# Examples

**Example 1** ("Making a Shareable Archive..."): Verifying the install:

```
$ rebar -V
rebar 2.0.0 R14B04 20120604_145614 git 0f24d93
```

**Example 2** ("Making an OTP Application"): Generating boilerplate and compiling:

```
$ rebar create-app appid=bertie
==> bertie (create-app)
Writing src/bertie.app.src
Writing src/bertie_app.erl
Writing src/bertie_sup.erl

> rebar compile
==> bertie (compile)
Compiled src/bertie.erl
```

# Relationships

## Builds Upon
- This is a foundational tooling card; it builds on no other card.

## Enables
- **Rebar dependency management** — Rebar's `rebar.config` and `get-deps` mechanism builds on the tool.
- **OTP application skeleton** — `rebar create-app` generates the standard application layout.

## Related
- **Rebar dependency management** — A core rebar feature.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Building each module by hand with `erlc` instead of using the tool.
  **Correction**: Use `rebar compile`, which finds and compiles the whole project consistently.

- **Error**: Hand-creating the OTP application/supervisor files.
  **Correction**: Run `rebar create-app appid=Name` to generate `*.app.src`, `*_app.erl`, and `*_sup.erl`.

# Common Confusions

- **Confusion**: Thinking rebar only compiles code.
  **Clarification**: It also scaffolds projects, fetches dependencies, packages, and integrates projects.

# Source Reference

Chapter 25: Third-Party Programs, Section "Making a Shareable Archive and Managing Your Code with Rebar" (subsections "Installing Rebar," "Making an OTP Application").

# Verification Notes

- Definition source: Direct quote from the chapter introduction.
- Confidence rationale: HIGH — the source explicitly defines rebar and walks through its use.
- Uncertainties: The book predates `rebar3`; install mechanics differ in modern OTP.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
