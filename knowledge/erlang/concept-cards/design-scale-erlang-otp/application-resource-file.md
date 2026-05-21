---
# === CORE IDENTIFICATION ===
concept: Application Resource File
slug: application-resource-file

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
section: "Application Resource Files"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "app file"
  - ".app file"
  - "application specification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
extends: []
related:
  - application-behaviour
  - application-environment
  - application-structure
  - included-applications
  - start-phases
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I structure an OTP application?"
  - "What is an OTP application?"
---

# Quick Definition

The application resource file (the `.app` file) is the mandatory specification packaged with every application: a tagged tuple listing the application's modules, dependencies, registered names, environment, and callback module.

# Core Definition

Every application must be packaged with a resource file, often referred to as the *app file*; it contains a specification of configuration data, resources, and information needed to start the application (Cesarini & Vinoski, p. 212). The specification is a tagged tuple of the format `{application, Application, Properties}`, where `Application` is an atom naming the application and `Properties` is a list of tagged tuples. Standard properties (all optional, defaulted if omitted) include `description`, `vsn`, `modules`, `registered`, `applications` (dependencies), `env`, `mod` (the callback module and start args), `id`, `included_applications`, and `start_phases` (pp. 212-215).

# Prerequisites

- **OTP application** — The resource file describes and configures an OTP application.

# Key Properties

1. Mandatory for every application; lives in the `ebin` directory.
2. Format: `{application, Application, Properties}`.
3. `description`, `vsn` — descriptive string and version string.
4. `modules` — the modules of the application (one-to-one with beam files in `ebin`).
5. `registered` — registered process names, to detect clashes.
6. `applications` — dependency list, used to order startup.
7. `env` — `{Key, Value}` environment variables.
8. `mod` — `{Module, Args}` callback module; omitting it makes the application a library application.
9. Optional: `id`, `included_applications`, `start_phases`.

# Construction / Recognition

## To Construct/Create:
1. Write `{application, Name, [...]}.` with the desired properties.
2. List `description`, `vsn`, `modules`, `registered`, `applications`, `env`, `mod`.
3. Save it as `<name>.app` in the `ebin` directory.

## To Identify/Recognize:
1. A file named `<name>.app` in `ebin`.
2. Contents are an Erlang term `{application, Name, Properties}`.

# Context & Application

- **Typical contexts**: Every OTP application; loaded when the application is loaded or started.
- **Common applications**: Declaring modules and dependencies; controlling release generation.
- **Historical/stylistic notes**: The `modules` list is also used to check the module namespace for clashes between applications (p. 214).

# Examples

**Example 1** (p. 213): The `sasl.app` resource file — `description`, `vsn`, `modules`, `registered`, `applications [kernel, stdlib]`, `env`, `mod {sasl, []}`.

**Example 2** (pp. 211-212): The `bsc.app` file for the Base Station Controller.

## Worked Example

The `bsc` application resource file (pp. 211-212):

```erlang
{application, bsc,
 [{description, "Base Station Controller"},
  {vsn, "1.0"},
  {modules, [bsc, bsc_sup, frequency, freq_overload,
             logger, simple_phone_sup, phone_fsm]},
  {registered, [bsc_sup, frequency, frequency_sup,
                overload, simple_phone_sup]},
  {applications, [kernel, stdlib, sasl]},
  {env, []},
  {mod, {bsc, []}}]}.
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- **Application environment** — The `env` property defines the application's environment variables.
- **Included applications** — The `included_applications` property declares subapplications.
- **Start phases** — The `start_phases` property enables phased startup.

## Related
- **Application behaviour** — The `mod` property names the application callback module.
- **Application structure** — The `.app` file lives in `ebin`.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Omitting a beam file from the `modules` list.
  **Correction**: A module in `ebin` not listed in `modules` will not be loaded automatically with the application.

- **Error**: Omitting the `applications` dependency list.
  **Correction**: Although it defaults to empty, almost all applications must list their dependencies (`kernel`, `stdlib`, often `sasl`).

# Common Confusions

- **Confusion**: Thinking omitting `mod` is an error.
  **Clarification**: Omitting `mod` is valid — it makes the application a *library application* with no supervision tree started at startup.

# Source Reference

Chapter 8: Applications, "Application Resource Files" and "The Base Station Controller Application File," pages 212-215.

# Verification Notes

- Definition source: Direct adaptation from pp. 212-215.
- Confidence rationale: HIGH — explicitly defined with the `sasl.app` and `bsc.app` files shown and every property described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
