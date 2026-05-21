---
# === CORE IDENTIFICATION ===
concept: Application Resource File
slug: application-resource-file

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-structure
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Applications"
chapter_number: null
pdf_page: null
section: "Application Resource File"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ".app file"
  - "app file"
  - "application specification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
extends: []
related:
  - application-callback-module
  - application-controller
  - application-configuration
  - application-directory-structure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create an OTP application?"
  - "What is an OTP application?"
---

# Quick Definition

The application resource file (`.app` file) is an Erlang term file containing the application specification — a tuple of the application name and a property list defining its modules, dependencies, callback module, configuration, and other metadata.

# Core Definition

According to the OTP Design Principles "Applications" chapter: "To define an application, an application specification is created, which is put in an application resource file, or in short an `.app` file." The file has the format `{application, Application, [Opt1,...,OptN]}.` where `Application` is an atom naming the application and each `Opt` is a `{Key,Value}` tuple defining a property. The file must be named `Application.app`.

# Prerequisites

- **Application** — the .app file defines an application's specification.

# Key Properties

1. Format: `{application, Application, [Opt1,...,OptN]}.` — an Erlang term file.
2. Must be named `Application.app` where `Application` matches the atom in the tuple.
3. All keys are optional; default values are used for omitted keys.
4. Key `mod` — defines the callback module and start argument: `{mod, {Module, StartArgs}}`.
5. Key `description` — short description string (defaults to `""`).
6. Key `vsn` — version number string (defaults to `""`).
7. Key `modules` — list of all modules introduced by this application (used by systools).
8. Key `registered` — names of registered processes (used by systools to detect name clashes).
9. Key `applications` — applications that must be started first (all have dependencies on at least Kernel and STDLIB).
10. Key `env` — configuration parameters as `{Par, Val}` tuples.
11. Key `included_applications` — list of included applications.
12. Key `start_phases` — list of `{Phase, PhaseArgs}` tuples for synchronization.

# Construction / Recognition

## To Construct/Create:
1. For a library application, create a minimal file: `{application, libapp, []}.`
2. For a supervision-tree application, include at minimum the `mod` key: `{application, ch_app, [{mod, {ch_app,[]}}]}.`
3. For packaging with systools, also include `description`, `vsn`, `modules`, `registered`, and `applications`.
4. Place the file in the `ebin` directory (released) or generate it from `.app.src` in `src` (development).

## To Identify/Recognize:
1. A file with the `.app` extension.
2. Contains a single Erlang term in the format `{application, Name, Options}.`
3. Located in the `ebin` directory of a released application.

# Context & Application

The .app file is the metadata descriptor for every OTP application. The application controller reads this file when loading an application. It is essential for the build system (systools) to generate boot scripts and release tar files. In development, a `.app.src` file in the `src` directory is used as a template, with fields like version number filled in during the build step.

# Examples

**Example 1** (applications.md, "Application Resource File"): Minimal .app file for a library application:
```erlang
{application, libapp, []}.
```

**Example 2** (applications.md, "Application Resource File"): Full .app file for the `ch_app` application:
```erlang
{application, ch_app,
 [{description, "Channel allocator"},
  {vsn, "1"},
  {modules, [ch_app, ch_sup, ch3]},
  {registered, [ch3]},
  {applications, [kernel, stdlib, sasl]},
  {mod, {ch_app,[]}}
 ]}.
```

**Example 3** (applications.md, "Configuring an Application"): Including configuration parameters via the `env` key:
```erlang
{application, ch_app,
 [{description, "Channel allocator"},
  {vsn, "1"},
  {modules, [ch_app, ch_sup, ch3]},
  {registered, [ch3]},
  {applications, [kernel, stdlib, sasl]},
  {mod, {ch_app,[]}},
  {env, [{file, "/usr/local/log"}]}
 ]}.
```

# Relationships

## Builds Upon
- **Application** — the .app file is the specification that defines an application.

## Enables
- **Application Controller** — the controller reads the .app file to load and manage the application.
- **Application Callback Module** — the `mod` key identifies the callback module.
- **Application Configuration** — the `env` key provides default configuration parameters.
- **Included Application** — the `included_applications` key lists included applications.
- **Start Phases** — the `start_phases` key defines synchronization phases.

## Related
- **Application Directory Structure** — the .app file resides in the `ebin` directory of the standard structure.
- **Release** — systools uses .app files to generate boot scripts and release packages.

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Not listing all dependency applications in the `applications` key.
  **Correction**: The source states "all applications have dependencies to at least Kernel and STDLIB." Always include all prerequisite applications.

- **Error**: Including a module in more than one application's `modules` list.
  **Correction**: "A module must only be included in one application."

# Common Confusions

- **Confusion**: Confusing the `.app` file with the `.app.src` file.
  **Clarification**: The `.app.src` file (in `src/`) is a build-time template; the `.app` file (in `ebin/`) is the actual resource file read at runtime. The source notes: "By convention a `.app.src` located in the `src` directory is used. This file is nearly identical to the `.app` file, but certain fields, such as the application version, are replaced during the build step."

# Source Reference

OTP Design Principles, "Applications" chapter, "Application Resource File" section (applications.md).

# Verification Notes

- Definition source: Directly quoted from applications.md "Application Resource File" section.
- Confidence rationale: High — extensively documented with format specification, multiple examples, and key descriptions.
- Uncertainties: None.
- Cross-reference status: References application, application-callback-module, application-controller, application-configuration, release.
