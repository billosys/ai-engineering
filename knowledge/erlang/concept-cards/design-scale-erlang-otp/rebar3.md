---
# === CORE IDENTIFICATION ===
concept: Rebar3
slug: rebar3

# === CLASSIFICATION ===
category: tooling
subcategory: build-tooling
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "System Principles and Release Handling"
chapter_number: 10
pdf_page: 282
section: "Rebar3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - rebar
  - rebar.config
  - relx

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release
extends: []
related:
  - systools
  - release-package
  - release-upgrade
  - otp-application
contrasts_with:
  - systools

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is rebar3 and how does it build releases?"
  - "How do I package, start, and configure a release?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

Rebar3 is a general-purpose Erlang build tool that automates compilation, dependency management, and release/upgrade generation. It uses the `relx` library for release generation and is the recommended tool for greenfield projects.

# Core Definition

Rebar3 is a general build tool that also manages releases and dependencies (Cesarini & Vinoski, p. 303-310, pdf p. 282). It is the second generation of `rebar`, one of the most widely used Erlang build tools, originating in the Erlang community. Rebar3 is comprehensive, addressing dependency management, compilation, and release generation, and is extensible via plug-ins. Its tasks fall into build commands, project-creation commands, dependency-management commands, release-generation commands, and test commands. For release generation, rebar3 uses the `relx` tool rather than the standard `reltool` facility.

# Prerequisites

- **Release** — Rebar3 builds and packages releases; the release concept comes first.

# Key Properties

1. Second generation of `rebar`; community-originated, general-purpose build tool.
2. Configured via a `rebar.config` file containing tuples such as `erl_opts`, `deps`, `relx`, and `profiles`.
3. Uses `relx` (not `reltool` or `systools`) for release generation.
4. `rebar3 new release <name>` scaffolds a release project skeleton.
5. `rebar3 compile` auto-fills the `modules` definition in the generated `.app` file from `src`.
6. `rebar3 release` / `rebar3 tar` / `rebar3 relup` create releases, tarballs, and upgrade files.
7. Profiles (e.g. `prod`) provide alternate settings; invoked via `rebar3 as prod release`.
8. `dev_mode` symlinks sources and excludes `erts`; `prod` profile sets `dev_mode` false and `include_erts` true.
9. Fetches source dependencies (and transitive dependencies) declared in the `deps` tuple.

# Construction / Recognition

## To Build a Release with Rebar3:
1. `rebar3 new release <name> desc="..."` to scaffold the project.
2. Edit `rebar.config` (`deps`, `relx`, `profiles`) as needed.
3. `rebar3 compile` to compile and generate the `.app` file.
4. `rebar3 release` for a development release, or `rebar3 as prod release` for production.
5. `rebar3 as prod tar` to produce a deployable tarball.

## To Recognize It:
1. A `rebar.config` file in the project root.
2. Commands of the form `rebar3 <task>`.

# Context & Application

- **Typical contexts**: Greenfield Erlang projects, or when dependency management becomes complicated.
- **Common applications**: Compilation, dependency fetching, release and upgrade generation, running tests, publishing to the `hex` package system.
- **Historical/stylistic notes**: Older projects sometimes bundled their own `rebar` executable; this is no longer necessary — place one `rebar3` in the shell path.

# Examples

**Example 1** (p. 305): Scaffolding a release project: `rebar3 new release bsc desc="Base Station Controller"` writes `bsc_app.erl`, `bsc_sup.erl`, `bsc.app.src`, `rebar.config`, `config/sys.config`, `config/vm.args`, and more.

**Example 2** (p. 305): A generated `rebar.config` with `erl_opts`, `deps`, a `relx` tuple defining the release, and a `prod` profile.

**Example 3** (p. 309): Adding a dependency — `{deps, [{lager, {git, "git://github.com/basho/lager.git", {tag, "3.0.2"}}}]}` — and `rebar3 compile` fetches `lager` and its transitive dependency `goldrush`.

# Relationships

## Builds Upon
- **Release** — Rebar3 automates building and packaging releases.

## Enables
- **Release package** — `rebar3 tar` produces a deployable tarball.
- **Release upgrade** — `rebar3 relup` generates upgrade files.

## Related
- **OTP application** — Rebar3 manages applications and their `.app.src` files.

## Contrasts With
- **systools** — The low-level OTP library for existing tool chains; rebar3 is the higher-level tool and uses `relx` instead.
- **Reltool** — The standard OTP release tool, widely viewed as difficult to configure; rebar3 uses `relx` to avoid it.

# Common Errors

- **Error**: Editing the generated `.app` file instead of the `.app.src` skeleton.
  **Correction**: Edit `bsc.app.src`; rebar3 regenerates `bsc.app` from it during compilation.

- **Error**: Expecting a default release to be production-ready.
  **Correction**: The default release uses `dev_mode` (symlinked sources, no `erts`); build with `rebar3 as prod release` for production.

# Common Confusions

- **Confusion**: Thinking rebar3 uses `reltool` or `systools` for releases.
  **Clarification**: Rebar3 uses the `relx` tool for release generation.

- **Confusion**: Believing a `rebar3 shell` starts only your application's dependencies.
  **Clarification**: A `rebar3 shell` may start extra applications (e.g. `inets`, `ssl`) that your application does not need.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Rebar3" (including "Generating a Rebar3 Release Project," "Creating a Release with Rebar3," and "Rebar3 Releases with Project Dependencies"), pages 303-310 (pdf p. 282). See also Chapter 11 "Upgrades with Rebar3."

# Verification Notes

- Definition source: Direct adaptation of pp. 303-310.
- Confidence rationale: HIGH — the source devotes a long section to rebar3, its commands, and its configuration.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
