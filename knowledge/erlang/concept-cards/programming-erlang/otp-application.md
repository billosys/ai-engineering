---
# === CORE IDENTIFICATION ===
concept: OTP Application
slug: otp-application

# === CLASSIFICATION ===
category: applications-releases
subcategory: applications
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Making a System with OTP"
chapter_number: 23
pdf_page: null
section: "The Application"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "application"
  - "OTP application behaviour"
  - "-behaviour(application)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - behaviour
  - supervisor
  - supervision-tree
extends: []
related:
  - app-file
  - gen-server
  - error-logger
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP application?"
  - "How do I start and stop an OTP application?"
  - "How is a system packaged in OTP?"
---

# Quick Definition

An OTP application is a specialized way of grouping everything related to one problem — code, supervision tree, configuration — so it can be loaded, started, stopped, and managed uniformly by the OTP system.

# Core Definition

When everything works, "we'll package all our code into an OTP *application*. This is a specialized way of grouping everything that has to do with a particular problem so that it can be started and stopped and managed by the OTP system itself" (Programming Erlang, "Making a System with OTP"). An application consists of an application resource file (the `.app` file) plus an application callback module declaring `-behaviour(application)` and exporting `start/2` and `stop/1`. The `start/2` callback typically starts the top-level supervisor of the application's supervision tree. Applications are administered with `application:load/1`, `application:start/1`, `application:stop/1`, and `application:unload/1`. "When we build complex systems using OTP, we package them as applications. This allows us to start, stop, and administer them uniformly."

# Prerequisites

- **Behaviour** — `application` is an OTP behaviour, declared with `-behaviour(application)`.
- **Supervisor** — an application's `start/2` callback starts a supervisor.
- **Supervision tree** — an application packages a supervision tree as a managed unit.

# Key Properties

1. Groups all code, supervision, and configuration for one problem into a managed unit.
2. Comprises an `.app` resource file and an application callback module.
3. The callback module declares `-behaviour(application)` and exports `start/2` and `stop/1`.
4. `start/2` usually calls the top supervisor's `start_link`.
5. Administered with `application:load`, `start`, `stop`, `unload`.
6. `init:stop()` closes down all running applications in an orderly manner.

# Construction / Recognition

## To Build an OTP Application:
1. Write the `.app` resource file naming the application, version, modules, registered names, dependencies, and `{mod, {CallbackMod, Args}}`.
2. Write the application callback module: `-behaviour(application).`, exporting `start/2` and `stop/1`.
3. Make `start/2` call the top-level supervisor's `start_link`.
4. Load and start it: `application:load(Name)` then `application:start(Name)`.

## To Recognize:
1. A module with `-behaviour(application).` exporting `start/2` and `stop/1` is an application callback module.
2. A `.app` file alongside it specifies the application.

# Context & Application

- **Typical contexts**: Packaging a complete OTP system for uniform start/stop/administration.
- **Common applications**: `sellaprime` is packaged as an OTP application with `sellaprime.app` and `sellaprime_app.erl`.
- **Historical/stylistic notes**: `kernel`, `stdlib`, and `sasl` are themselves loaded OTP applications, visible via `application:loaded_applications()`.

# Examples

**Example 1** ("The Application"): The `sellaprime_app` callback module:

```erlang
-module(sellaprime_app).
-behaviour(application).
-export([start/2, stop/1]).

start(_Type, StartArgs) ->
    sellaprime_supervisor:start_link(StartArgs).
stop(_State) ->
    ok.
```

**Example 2** ("The Application"): The shell session loads, starts, stops, and unloads `sellaprime`: `application:load(sellaprime)`, `application:start(sellaprime)`, `application:stop(sellaprime)`, `application:unload(sellaprime)`.

# Relationships

## Builds Upon
- **Behaviour** — `application` is one of the OTP behaviours.
- **Supervisor** — the application's `start/2` starts a supervisor.
- **Supervision tree** — an application packages a whole supervision tree.

## Enables
- **`.app` file** — the resource file that describes the application.

## Related
- **gen_server** — applications typically consist of gen_servers supervised by a supervisor.
- **The error logger** — applications usually include error logging configuration.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Naming the application callback module differently from the `{mod, ...}` declaration in the `.app` file.
  **Correction**: The callback module must have the same name as the `mod` entry in the `.app` file.

- **Error**: Calling `application:start` without first having the `.app` file findable.
  **Correction**: The `.app` file must be in the directory where Erlang was started, or a subdirectory of it.

# Common Confusions

- **Confusion**: Thinking `application:load` also starts the application.
  **Clarification**: `load` loads the code but does not start it; `application:start` starts it.

- **Confusion**: Believing an application must be stopped explicitly before shutdown.
  **Clarification**: `init:stop()` closes down all running applications in an orderly manner automatically.

# Source Reference

Chapter 23: Making a System with OTP, section "The Application"; also "File System Organization". No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes and code from "The Application".
- Confidence rationale: HIGH — the application behaviour, callback module, and lifecycle are explicitly defined and demonstrated.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card. Canonical slug `otp-application` per extraction instructions.
