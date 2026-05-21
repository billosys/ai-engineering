---
# === CORE IDENTIFICATION ===
concept: System Configuration File
slug: sys-config

# === CLASSIFICATION ===
category: applications-releases
subcategory: configuration
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Packaging, services, and deployment"
chapter_number: 10
pdf_page: null
section: "10.2.5. System configuration"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - sys.config
  - .config file
  - configuration file

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-release
extends: []
related:
  - boot-script
  - target-system
  - application-metadata-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the sys.config file?"
  - "What is the structure of a .config file?"
  - "How is application configuration supplied to a release?"
---

# Quick Definition

`sys.config` is a release's system configuration file — a single Erlang term mapping application names to key/value option lists, supplied to the runtime at startup.

# Core Definition

The system configuration file provides configuration settings for a release. The standard name is `sys.config`, though any name ending in `.config` is acceptable. Like the `.app` and `.rel` files, the `.config` file contains a single Erlang term followed by a period. The outer term is a list of tuples; each tuple is a pair of an application name and a corresponding list of key/value pairs specifying options for that application. It is optional but typically present, and is passed to the runtime via the `-config` flag when starting a target system ("Erlang and OTP in Action," Ch. 10, Section 10.2.5).

# Prerequisites

- **Erlang release** — `sys.config` configures the applications of a release.

# Key Properties

1. Standard filename `sys.config`; any `.config` extension works.
2. Contains a single Erlang term (a list) terminated by a period.
3. The outer list holds `{AppName, [{Key, Value}, ...]}` tuples.
4. Each inner list configures one application's environment variables.
5. Optional, but a release usually includes one.
6. Bundled into a release package inside the `releases/<version>` directory.

# Construction / Recognition

## To Construct/Create:
1. Create a file `sys.config`.
2. Write a list of `{AppName, [{Key, Value}, ...]}` tuples, terminated by a period.
3. Pass it at startup with the `-config` flag (without the `.config` extension).

## To Identify/Recognize:
1. A `.config` file whose content is a list of `{atom, list}` pairs.

# Context & Application

- **Typical contexts**: Supplying production configuration without hardcoding values in code.
- **Common applications**: Configuring where `sasl` stores its error log, and supplying `simple_cache` the names of contact nodes.
- **Historical/stylistic notes**: Application code reads these values with functions like `application:get_env/2`, falling back on defaults when no setting is present.

# Examples

**Example 1** (Listing 10.3): The `sys.config` for `simple_cache` specifies where the `sasl` application stores its error log and what the contact-node names are for the `simple_cache` application.

**Example 2** (Section 10.2.6): `erl -sname cache -boot ./simple_cache -config ./sys` starts the target system using `sys.config`.

# Relationships

## Builds Upon
- **Erlang release** — `sys.config` configures a release's applications.

## Enables
- **Target system** — Provides the configuration a target system reads at startup.

## Related
- **Boot script** — Supplied together with the boot file when starting a system.
- **Application metadata file** — Configures the same applications declared in `.app` files.

# Common Errors

- **Error**: Passing the full filename including `.config` to the `-config` flag.
  **Correction**: Give the name without the `.config` extension (e.g., `-config ./sys`).

# Common Confusions

- **Confusion**: Thinking `sys.config` replaces values inside the `.app` file.
  **Clarification**: `sys.config` supplies the application environment at runtime; application code reads it (e.g., via `application:get_env/2`) and may fall back on code defaults.

# Source Reference

Chapter 10: "Packaging, services, and deployment," Section 10.2.5 "System configuration." See Listing 10.3 (the `sys.config` file) and Figure 10.3 (release components).

# Verification Notes

- Definition source: Direct adaptation of Section 10.2.5.
- Confidence rationale: HIGH — the book explicitly describes the `.config` file structure.
- Uncertainties: Listing 10.3 is presented as an image in the source; structure described from the surrounding prose.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
