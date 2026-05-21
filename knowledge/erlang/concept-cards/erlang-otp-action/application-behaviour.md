---
# === CORE IDENTIFICATION ===
concept: Application Behaviour
slug: application-behaviour

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-structure
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "OTP applications and supervision"
chapter_number: 4
pdf_page: null
section: "4.1.3 The application behaviour"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - application behavior
  - "application callback module"
  - "_app module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-behaviour
  - otp-application
  - app-file
extends:
  - otp-behaviour
related:
  - root-supervisor
  - application-master
  - app-file
  - starting-an-application
contrasts_with:
  - supervisor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the application behaviour?"
  - "What callbacks does the application behaviour require?"
  - "What does the application behaviour module do?"
---

# Quick Definition

The `application` behaviour is the OTP behaviour that provides an active application's startup logic. Its callback module starts the application's root supervisor and is named in the `.app` file's `mod` parameter.

# Core Definition

Every active application needs one module that implements the `application` behaviour (Ch. 4, Section 4.1.3). This module provides the startup logic for the system; at a minimum it provides the point from which the *root supervisor* is started — the grandparent of all the application's processes. The `application` behaviour requires the module to export two callbacks: `start/2` and `stop/1`. `start/2` is called when OTP wants to start the application; it performs the actual startup and must return the process ID of the root supervisor as `{ok, Pid}`. `stop/1` is called on shutdown, after all other application processes have stopped. The common naming convention for this module is `<application-name>_app`.

# Prerequisites

- **OTP behaviour** — The `application` behaviour is one specific behaviour.
- **OTP application** — The behaviour provides an application's startup logic.
- **Application metadata file (.app)** — The `mod` parameter names the behaviour module.

# Key Properties

1. Required for every active application.
2. Requires two callbacks: `start/2` and `stop/1`.
3. `start/2` starts the root supervisor and returns `{ok, Pid}`.
4. `stop/1` performs shutdown cleanup (often just returns `ok`).
5. Named by convention `<application-name>_app`.
6. The `.app` file's `mod` parameter points to this module.

# Construction / Recognition

## To Write an Application Behaviour Module:
1. Create `src/<app>_app.erl` with `-behaviour(application)`.
2. Export `start/2` and `stop/1`.
3. In `start/2`, start the root supervisor (e.g. `<app>_sup:start_link()`) and return `{ok, Pid}`.
4. In `stop/1`, return `ok` (or do any needed cleanup).
5. Name this module in the `.app` file's `mod` parameter.

# Context & Application

The application behaviour module is the launching point OTP uses; the book recommends keeping it small and delegating supervisor setup to the `_sup` module.

- **Typical contexts**: The startup entry point of every active application.
- **Common applications**: `tr_app` starts `tr_sup`; `sc_app` starts `sc_sup` and also initializes the `sc_store` ETS table.

# Examples

**Example 1** (Ch. 4, Listing 4.2): `src/tr_app.erl` implements `application`; `start/2` calls `tr_sup:start_link()` and checks the result; `stop/1` ignores its argument and returns `ok`.

**Example 2** (Ch. 6): `sc_app:start/2` starts `sc_sup` and additionally calls `sc_store:init()` so the ETS table exists before the supervisor runs.

# Relationships

## Builds Upon
- **OTP behaviour** — The `application` behaviour is a concrete behaviour.

## Enables
- **root-supervisor** — `start/2` starts the root supervisor.
- **starting-an-application** — The behaviour module is the launching point.

## Related
- **application-master** — The application master process calls `start/2` and `stop/1`.
- **app-file** — The `mod` parameter names this module.

## Contrasts With
- **supervisor** — The application behaviour provides startup logic and is short-lived in its callbacks; a supervisor is a long-running monitoring process.

# Common Errors

- **Error**: Returning something other than `{ok, Pid}` (the root supervisor's pid) from `start/2`.
  **Correction**: `start/2` must return `{ok, Pid}` with the root supervisor's process ID.

- **Error**: Putting supervisor setup details directly in the `_app` module.
  **Correction**: Keep `_app` small; delegate supervisor construction to the `_sup` module.

# Common Confusions

- **Confusion**: Thinking `start/2`'s arguments are for general configuration.
  **Clarification**: They are the `mod` start arguments; use a config file for general configuration.

# Source Reference

Chapter 4: OTP applications and supervision, Section 4.1.3 "The application behaviour," Listing 4.2 and the "Naming the application behaviour module" sidebar. Chapter 6, Section 6.3.3.

# Verification Notes

- Definition source: Direct adaptation of Section 4.1.3.
- Confidence rationale: HIGH — explicit definition and callback enumeration.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
