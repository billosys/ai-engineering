---
# === CORE IDENTIFICATION ===
concept: OTP Application
slug: otp-application

# === CLASSIFICATION ===
category: applications-releases
subcategory: applications
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Applications"
chapter_number: 8
pdf_page: 222
section: "How Applications Run"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "application"
  - "Erlang/OTP application"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervision-tree
extends: []
related:
  - application-behaviour
  - application-resource-file
  - application-controller
  - library-application
  - application-types
contrasts_with:
  - library-application

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP application?"
  - "How do I structure an OTP application?"
  - "How does an application relate to its supervision tree?"
  - "What distinguishes an OTP application from a release?"
---

# Quick Definition

An OTP application is a reusable unit that packages a supervision tree, modules, and other resources together, and can be configured, started, and stopped as a whole. It is the basic building block of large Erlang systems.

# Core Definition

The application behavior allows you to package together supervision trees, modules, and other resources into one semi-independent unit, providing the basic building blocks of large Erlang systems (Cesarini & Vinoski, p. 203). An application is a means of packaging resources — modules, processes, registered names, configuration files, and even non-Erlang code — into reusable components. Applications can be configured, started, and stopped as a whole, and one application can depend on another, with the runtime starting and stopping them in the proper order (pp. 204-205). To the Erlang runtime all applications look the same; it does not distinguish between them in how it loads, runs, or terminates them.

# Prerequisites

- **Supervision tree** — A normal application starts and manages a supervision tree; understanding the tree is required.

# Key Properties

1. Packages supervision trees, modules, registered names, and configuration into one unit.
2. Can be loaded, started, stopped, and unloaded as a whole.
3. Can declare dependencies on other applications, which the runtime starts in order.
4. Two kinds exist: normal applications (start a top-level supervisor) and library applications (no supervisor).
5. Every application must be packaged with a resource file (the `.app` file).
6. An Erlang node typically consists of many loosely coupled applications.

# Construction / Recognition

## To Construct/Create:
1. Package code in the standard directory structure (`ebin`, `src`, `priv`, `include`).
2. Write a callback module with `-behavior(application).` exporting `start/2` and `stop/1`.
3. Write the `.app` resource file describing modules, dependencies, the callback module, etc.
4. Start with `application:start(Application)`.

## To Identify/Recognize:
1. A directory named `<name>-<version>` with `ebin`, `src`, `priv`, `include`.
2. An `.app` resource file in `ebin`.
3. A callback module with the `application` behavior (for normal applications).

# Context & Application

- **Typical contexts**: Every component of an Erlang node — standard (`mnesia`, `sasl`, `os_mon`), generic third-party (`lager`, `exometer`), and business-logic applications.
- **Common applications**: Encapsulating functionality for reuse beyond what modules allow; building releases.
- **Historical/stylistic notes**: Full user applications bundled with their dependencies form a *release* — e.g. Yaws, Riak, RabbitMQ, MongooseIM (p. 204).

# Examples

**Example 1** (pp. 211-212): The `bsc` (Base Station Controller) application — callback module `bsc`, `.app` file listing modules and the `sasl`/`kernel`/`stdlib` dependencies.

**Example 2** (pp. 210-211): Loading and starting the `sasl` application from the standard distribution.

## Worked Example

The `bsc` application callback module (p. 209):

```erlang
-module(bsc).
-behavior(application).
%% Application callbacks
-export([start/2, stop/1]).

start(_StartType, _StartArgs) ->
    bsc_sup:start_link().

stop(_Data) ->
    ok.
```

`application:start(bsc)` loads the modules, starts the master processes, and calls `bsc:start/2`, which starts the top-level supervisor.

# Relationships

## Builds Upon
- *(none)*

## Enables
- **Application behaviour** — The application is implemented through the application behavior.

## Related
- **Application resource file** — Every application must have one.
- **Application controller** — The VM process that loads and runs applications.
- **Application types** — Determine what an application's termination does to the node.

## Contrasts With
- **Library application** — A library application contains modules but starts no supervision tree.

# Common Errors

- **Error**: Starting an application before its declared dependencies.
  **Correction**: Use `application:ensure_all_started/1`, or start dependencies (`kernel`, `stdlib`, `sasl`, ...) first.

- **Error**: Bundling source code and the compiler with a production release.
  **Correction**: Ship only `ebin` and `priv`; deploy tested beam files from the repository.

# Common Confusions

- **Confusion**: Using "application" in its everyday sense.
  **Clarification**: In OTP, "application" means specifically an OTP application — a packaged unit — not a program in the broad sense.

- **Confusion**: Equating an application with a release.
  **Clarification**: A release is a bundle of applications and their dependencies that can run as a standalone node; an application is one component of it.

# Source Reference

Chapter 8: Applications, "How Applications Run" and "The Application Structure," pages 203-208.

# Verification Notes

- Definition source: Direct adaptation from pp. 203-205.
- Confidence rationale: HIGH — the application concept is explicitly defined and elaborated throughout the chapter.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
