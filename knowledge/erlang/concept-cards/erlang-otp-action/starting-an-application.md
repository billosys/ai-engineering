---
# === CORE IDENTIFICATION ===
concept: Starting an OTP Application
slug: starting-an-application

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
section: "4.3 Starting the application"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "application:start/1"
  - launching an application

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - app-file
  - application-behaviour
extends:
  - otp-application
related:
  - application-master
  - app-file
contrasts_with:
  - erlang-release

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you start an OTP application?"
  - "What does application:start/1 do?"
  - "How does the system find an application's modules from just its name?"
---

# Quick Definition

An OTP application is started by calling `application:start/1` with the application name; the function finds the `.app` file on the code path and uses it to launch the application.

# Core Definition

With the `.beam` files compiled into `ebin` and the `ebin` directory on the code path, an application is launched by calling the standard library function `application:start/1`, passing the application name as an atom (Ch. 4, Section 4.3). Just as Erlang searches the code path for `.beam` files to load modules, `application:start/1` searches the code path for `.app` files; finding the application's metadata file tells it everything it needs to know — in particular, which `application` behaviour module to use to kick-start the application. The book notes that starting an application this way is for manual testing, not production systems (where releases are used instead).

# Prerequisites

- **OTP application** — The thing being started.
- **Application metadata file (.app)** — `application:start/1` reads it.
- **Application behaviour** — The `.app` file's `mod` parameter names the module that does the startup.

# Key Properties

1. Started with `application:start(Name)` from the Erlang shell.
2. `application:start/1` searches the code path for `.app` files.
3. The `.app` file tells it which `application` behaviour module to start.
4. The `ebin` directory must be on the code path (e.g. via `erl -pa ebin`).
5. Starting this way is for manual testing, not production.

# Construction / Recognition

## To Start an Application:
1. Compile sources into `ebin` (`erlc -o ebin src/*.erl`).
2. Start Erlang with `ebin` on the code path (`erl -pa ebin`).
3. Call `application:start(AppName)` in the shell.

# Context & Application

`application:start/1` is the manual way to bring an application to life during development.

- **Typical contexts**: Manual testing of an application in the Erlang shell.
- **Common applications**: `application:start(tcp_rpc)` launches the TCP RPC server; `application:start(simple_cache)` launches the cache.

# Examples

**Example 1** (Ch. 4): After `erl -pa ebin`, `1> application:start(tcp_rpc).` returns `ok` and the application is running.

**Example 2** (Ch. 6): `application:start(simple_cache).` returns `ok`, after which the three `simple_cache` API functions can be used.

# Relationships

## Builds Upon
- **OTP application** — Starting brings an application to life.

## Related
- **app-file** — `application:start/1` finds and reads the `.app` file.
- **application-master** — Started as part of bringing the application up.

## Contrasts With
- **release** — In production, a release boots the whole system properly; `application:start/1` is for manual testing only.

# Common Errors

- **Error**: Calling `application:start/1` without `ebin` on the code path.
  **Correction**: Start Erlang with `erl -pa ebin` so the `.app` and `.beam` files are found.

# Common Confusions

- **Confusion**: Wondering how the system finds the modules when no module has the application's name.
  **Clarification**: `application:start/1` finds the `.app` file on the code path, which lists the modules and the `mod` startup module.

# Source Reference

Chapter 4: OTP applications and supervision, Section 4.3 "Starting the application."

# Verification Notes

- Definition source: Direct adaptation of Section 4.3.
- Confidence rationale: HIGH — explicit, worked treatment in the source.
- Uncertainties: None.
- Cross-reference status: References planned `release` card (owned by another agent) and chapter-group cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
