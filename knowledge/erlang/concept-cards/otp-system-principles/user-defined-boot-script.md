---
# === CORE IDENTIFICATION ===
concept: User-Defined Boot Script
slug: user-defined-boot-script

# === CLASSIFICATION ===
category: applications-releases
subcategory: system-startup
tier: advanced

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "System Principles"
chapter_number: null
pdf_page: null
section: "User-Defined Boot Scripts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - custom boot script
  - application-specific boot script

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boot-script
  - default-boot-scripts
extends:
  - boot-script
related:
  - init-module
  - erlang-runtime-system
contrasts_with:
  - default-boot-scripts

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a user-defined boot script?"
  - "How do boot scripts relate to release resource files (.rel)?"
  - "What is a boot script in Erlang/OTP?"
---

# Quick Definition

A user-defined boot script is a custom boot script generated from a release resource file (`.rel`) using `systools:make_script/1,2`, specifying exactly which applications to load and start for a particular deployment.

# Core Definition

It is sometimes useful or necessary to create a user-defined boot script. This is especially true when running Erlang in embedded mode. While it is possible to manually create a boot script, it is preferable to generate it from a release resource file called `Name.rel` using the function `systools:make_script/1,2`. This requires that the source code is structured as applications according to the OTP design principles. The `systools:make_script` function generates both the `.script` and `.boot` files from the `.rel` file. To generate only the binary `.boot` file from an existing `.script` file, the function `systools:script2boot(File)` can be used.

Source: "User-Defined Boot Scripts" section of OTP System Principles documentation (Ericsson AB).

# Prerequisites

- **boot-script** — user-defined boot scripts are a specialized form of boot script
- **default-boot-scripts** — understanding the defaults helps motivate why custom scripts are needed

# Key Properties

1. Generated from a release resource file (`Name.rel`)
2. Created using `systools:make_script/1,2` (preferred method)
3. Requires source code structured as OTP applications
4. Especially important when running in embedded mode
5. Can be manually created, but generation from `.rel` is preferable
6. `systools:script2boot/1` converts a `.script` file to `.boot` format independently
7. The `.rel` file format is documented in the SASL application

# Construction / Recognition

## To Construct/Create:
1. Structure your code as OTP applications following OTP design principles
2. Create a release resource file (`Name.rel`) listing your applications and their versions
3. Call `systools:make_script("Name")` or `systools:make_script("Name", Options)` to generate `Name.script` and `Name.boot`
4. Use the generated boot script with `erl -boot Name`
5. Alternatively, if you already have a `.script` file, call `systools:script2boot("Name")` to generate only the `.boot` file

## To Identify/Recognize:
1. A `.rel` file defines the release and its constituent applications
2. A corresponding `.script`/`.boot` pair generated from that `.rel` file is a user-defined boot script
3. The boot script will reference application-specific modules beyond Kernel and STDLIB

# Context & Application

User-defined boot scripts are essential for production Erlang/OTP deployments. When running in embedded mode, all code must be loaded at startup according to the boot script — there is no dynamic code loading. The user-defined boot script specifies exactly which applications (and their dependencies) should be loaded and started. This is the foundation of the OTP release concept: a `.rel` file defines the release, and `systools:make_script` generates the boot script that brings that release to life. This workflow is typically automated by release tools like `rebar3` or `relx`.

# Examples

**Example 1** (System Principles section): The recommended workflow for creating a user-defined boot script:

```erlang
%% Given a release resource file my_release.rel,
%% generate my_release.script and my_release.boot
systools:make_script("my_release").
```

**Example 2** (System Principles section): Converting an existing `.script` to `.boot`:

```erlang
%% Convert my_release.script to my_release.boot
systools:script2boot("my_release").
```

**Example 3** (System Principles section): Using the generated boot script:

```text
% erl -boot my_release
```

# Relationships

## Builds Upon
- **boot-script** — user-defined boot scripts extend the general boot script concept
- **default-boot-scripts** — user-defined scripts go beyond what the defaults provide

## Enables
- Production OTP releases — user-defined boot scripts are the mechanism by which releases start their specific set of applications

## Related
- **init-module** — the init process interprets user-defined boot scripts just as it interprets default ones
- **erlang-runtime-system** — the runtime system uses the boot script for startup, especially in embedded mode

## Contrasts With
- **default-boot-scripts** — default scripts are pre-built and only start standard applications; user-defined scripts are generated from `.rel` files and start application-specific code

# Common Errors

- **Error**: Manually editing a `.boot` file instead of regenerating from the `.rel` file.
  **Correction**: Always modify the `.rel` file and regenerate with `systools:make_script/1,2`. The `.boot` file is a binary format not intended for manual editing.

- **Error**: Calling `systools:make_script/1,2` when the source code is not structured as OTP applications.
  **Correction**: Structure your code as proper OTP applications with `.app` files before generating boot scripts. `systools:make_script` requires OTP application structure.

- **Error**: Forgetting to include all dependency applications in the `.rel` file.
  **Correction**: The `.rel` file must list all applications and their versions, including transitive dependencies. `systools:make_script` will report errors for missing applications.

# Common Confusions

- **Confusion**: The `.rel` file is the boot script.
  **Clarification**: The `.rel` file is a release resource file that describes which applications comprise a release. The boot script (`.script`/`.boot`) is generated from the `.rel` file and contains the actual instructions for loading code and starting applications.

- **Confusion**: User-defined boot scripts can only be created with `systools`.
  **Clarification**: The source states that "while it is possible to manually create a boot script, it is preferable to generate it" from a `.rel` file. Manual creation is possible but not recommended.

# Source Reference

"User-Defined Boot Scripts" subsection of "Boot Scripts" section, "System Principles" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (source explicitly describes the process and rationale for user-defined boot scripts)
- Confidence rationale: The source provides clear instructions and the relationship to `.rel` files and `systools`
- Uncertainties: The exact format of `.rel` files is not detailed in this section; it references the SASL documentation
- Cross-reference status: verified against source text
