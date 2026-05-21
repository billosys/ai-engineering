---
# === CORE IDENTIFICATION ===
concept: Application Resource File (.app)
slug: app-file

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
  - ".app file"
  - "application resource file"
  - "application specification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
extends: []
related:
  - supervisor
  - error-logger
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an .app file?"
  - "How does OTP know how to start an application?"
---

# Quick Definition

The `.app` file is the application resource file: an Erlang term that describes an OTP application — its name, version, modules, registered processes, dependencies, and the application callback module to start.

# Core Definition

To finish an OTP application "we have to do now is write a file with the extension `app` that contains information about our application" (Programming Erlang, "The Application"). The `.app` file holds a single `{application, Name, [Properties]}` term. Its key properties are `description`, `vsn` (version), `modules` (all modules belonging to the application), `registered` (registered process names), `applications` (other applications it depends on, e.g. `kernel`, `stdlib`), `mod` (`{CallbackMod, Args}` — the application callback module), and `start_phases`. When `application:start(Name)` runs, "the application controller then looks for a `{mod, ...}` declaration" in the `.app` file to find the callback module. The `.app` file must be in the directory where Erlang was started, or a subdirectory of it.

# Prerequisites

- **OTP application** — the `.app` file is the descriptor of an OTP application.

# Key Properties

1. A single Erlang term: `{application, Name, [Properties]}`.
2. `description` — a human-readable description string.
3. `vsn` — the application version string.
4. `modules` — the list of all modules belonging to the application.
5. `registered` — the registered process names the application uses.
6. `applications` — other applications this one depends on (typically includes `kernel`, `stdlib`).
7. `mod` — `{CallbackMod, Args}`, naming the application callback module.
8. Must be locatable: in the start directory or a subdirectory.

# Construction / Recognition

## To Write a .app File:
1. Create a file named `<appname>.app`.
2. Write a `{application, Name, [...]}` term.
3. Fill in `description`, `vsn`, `modules`, `registered`, `applications`, and `mod`.
4. Ensure the `mod` callback module name matches the application callback module file.
5. Place the file where Erlang can find it at startup.

## To Recognize:
1. A file with the `.app` extension containing an `{application, ...}` term is an application resource file.

# Context & Application

- **Typical contexts**: Every OTP application has exactly one `.app` resource file.
- **Common applications**: `sellaprime.app` describes the prime-number-shop application.
- **Historical/stylistic notes**: `kernel`, `sasl`, and `stdlib` each have their own `.app` files, reflected in `application:loaded_applications()` output.

# Examples

**Example 1** ("The Application"): The `sellaprime.app` resource file:

```erlang
{application, sellaprime,
 [{description, "The Prime Number Shop"},
  {vsn, "1.0"},
  {modules, [sellaprime_app, sellaprime_supervisor, area_server,
             prime_server, lib_lin, lib_primes, my_alarm_handler]},
  {registered,[area_server, prime_server, sellaprime_super]},
  {applications, [kernel,stdlib]},
  {mod, {sellaprime_app,[]}},
  {start_phases, []}
 ]}.
```

**Example 2** ("The Application"): After `application:load(sellaprime)`, `application:loaded_applications()` shows `{sellaprime,"The Prime Number Shop","1.0"}` — the description and version come straight from the `.app` file.

# Relationships

## Builds Upon
- **OTP application** — the `.app` file is the descriptor that makes a directory of code into an application.

## Enables
- (No further concepts in this chapter build on the `.app` file.)

## Related
- **Supervisor** — the `mod` callback named in the `.app` file usually starts a supervisor.
- **The error logger** — production applications pair the `.app` file with an error-logger `.config` file.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Placing the `.app` file where Erlang cannot find it at startup.
  **Correction**: It must be in the directory Erlang was started in, or a subdirectory of it.

- **Error**: Listing a wrong or missing module in `modules`.
  **Correction**: `modules` must list all modules belonging to the application so they can be loaded and unloaded together.

# Common Confusions

- **Confusion**: Confusing the `.app` resource file with a `.config` configuration file.
  **Clarification**: The `.app` file describes the application's structure; the `.config` file (used with `-config`) configures subsystems like the error logger.

- **Confusion**: Thinking the `.app` file contains executable code.
  **Clarification**: It contains a single descriptive Erlang term; the code lives in the modules it lists.

# Source Reference

Chapter 23: Making a System with OTP, section "The Application"; also "File System Organization". No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes and code from "The Application".
- Confidence rationale: HIGH — the `.app` file is explicitly shown and its `mod` lookup behaviour described.
- Uncertainties: The `start_phases` property is shown but not explained in the chapter; described here only as a property present in the file.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
