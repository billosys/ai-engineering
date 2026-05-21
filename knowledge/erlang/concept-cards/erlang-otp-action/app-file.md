---
# === CORE IDENTIFICATION ===
concept: Application Metadata File (.app)
slug: app-file

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
section: "4.1.2 Adding the application metadata"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - .app file
  - "dot app file"
  - application metadata file
  - application resource file

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - application-organization
extends:
  - otp-application
related:
  - application-behaviour
  - starting-an-application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the .app file?"
  - "What metadata does an OTP application's .app file contain?"
  - "What does the mod parameter in the .app file do?"
---

# Quick Definition

The `.app` file is the OTP application metadata file: a plain Erlang term stored in `ebin/<application-name>.app` that tells the system how to start the application and how it relates to others.

# Core Definition

The application metadata is expressed as plain Erlang terms in a text file called `<application-name>.app` stored in the `ebin` directory (Ch. 4, Section 4.1.2). It is used by OTP to understand how the application should be started and how it fits with other applications. The file contains a single Erlang term terminated by a period: a 3-tuple `{application, Name, Params}`, where `Name` is the application name as an atom and `Params` is a list of `{Key, Value}` pairs. The main parameters are:

- **description** — A short description of the application.
- **vsn** — The version string, suggested form `<major>.<minor>.<patch>`.
- **modules** — A list of all modules in the application.
- **registered** — The registered process names the application uses (declaration only; does not perform registration).
- **applications** — Applications that must be started before this one.
- **mod** — Tells OTP how to start the application: `{Module, StartArgs}`, where `Module` implements the `application` behaviour.

# Prerequisites

- **OTP application** — The `.app` file describes an application.
- **OTP application directory organization** — The `.app` file lives in `ebin`.

# Key Properties

1. Stored as `ebin/<application-name>.app`; the file name matches the application name.
2. Contains a single `{application, Name, Params}` term terminated by a period.
3. `description`, `vsn`, `modules`, `registered`, `applications`, `mod` are the main parameters.
4. `registered` only declares names; it does not perform registration.
5. The `mod` parameter names the `application` behaviour module and makes the application active.
6. `application:start/1` searches the code path for `.app` files.

# Construction / Recognition

## To Write a .app File:
1. Create `ebin/<application-name>.app`.
2. Write `{application, name, [ ... ]}.` with a trailing period.
3. Fill in `description`, `vsn`, `modules`, `registered`, `applications`.
4. Add `{mod, {Module, []}}` for an active application.

# Context & Application

The `.app` file is what lets the system start an application by name without a module of that name existing.

- **Typical contexts**: Every OTP application has exactly one `.app` file.
- **Common applications**: `ebin/tcp_rpc.app` lists `tr_app`, `tr_sup`, `tr_server` and `{mod, {tr_app, []}}`.

# Examples

**Example 1** (Ch. 4, Listing 4.1): `ebin/tcp_rpc.app` — `{application, tcp_rpc, [{description, ...}, {vsn, "0.1.0"}, {modules, [...]}, {registered, [tr_sup]}, {applications, [kernel, stdlib]}, {mod, {tr_app, []}}]}.`

**Example 2** (Ch. 6): `ebin/simple_cache.app` follows the same shape with `{mod, {sc_app, []}}`.

# Relationships

## Builds Upon
- **OTP application** — The `.app` file is the application's metadata.

## Related
- **application-behaviour** — The `mod` parameter names the behaviour module.
- **starting-an-application** — `application:start/1` reads the `.app` file.

## Contrasts With
- This is a metadata file; the source draws no direct contrast.

# Common Errors

- **Error**: Giving the `.app` file a name that does not match the application name.
  **Correction**: The `.app` file name must match the application name.

- **Error**: Using `mod` start arguments for general configuration.
  **Correction**: Do not use them for configuration — use a proper config file instead.

# Common Confusions

- **Confusion**: Thinking the `registered` parameter performs the registration.
  **Clarification**: It only declares which names the application registers, helping with upgrades and duplicate-name warnings.

# Source Reference

Chapter 4: OTP applications and supervision, Section 4.1.2 "Adding the application metadata," Listing 4.1 and Table 4.2.

# Verification Notes

- Definition source: Direct adaptation of Section 4.1.2 and Table 4.2.
- Confidence rationale: HIGH — explicit, tabulated definition.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
