---
# === CORE IDENTIFICATION ===
concept: Target System Creation
slug: target-system-creation

# === CLASSIFICATION ===
category: applications-releases
subcategory: deployment
tier: advanced

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Creating and Upgrading a Target System"
chapter_number: null
pdf_page: null
section: "Creating a Target System"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "target_system:create/1"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - target-system
  - release
extends: []
related:
  - target-system-installation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a target system?"
  - "What does target_system:create/1 do?"
---

# Quick Definition

Target system creation is the process of building a self-contained tar archive from a `.rel` file using `target_system:create/1`, which generates boot scripts, packages applications and ERTS, and prepares the archive for installation.

# Core Definition

As described in OTP System Principles, creating a target system requires a `.rel` file specifying the ERTS version and included applications, then calling `target_system:create/1`. This function performs a multi-step process: generating boot scripts via `systools:make_script/2`, building a tar archive via `systools:make_tar/2`, and restructuring the archive to include `bin/`, `log/`, and `releases/start_erl.data`.

# Prerequisites

- A working Erlang/OTP system structured according to OTP design principles.
- A `.rel` file specifying the ERTS version and all applications to include.
- All application code available on the code path.

# Key Properties

1. Reads the `.rel` file and creates a `plain.rel` containing only Kernel and STDLIB.
2. Generates `.script` and `.boot` files for both the full release and the plain (Kernel+STDLIB) release.
3. Creates a `.tar.gz` archive containing `erts-<version>/bin/`, `releases/`, and `lib/` directories.
4. Restructures the archive: deletes `erl` and `start` from `erts-<version>/bin/` (regenerated during install).
5. Copies `plain.boot` to `bin/start.boot` for the basic target system.
6. Copies `epmd`, `run_erl`, and `to_erl` to `bin/`.
7. Creates `log/` directory and `releases/start_erl.data` with ERTS and release version strings.
8. If a `sys.config` file exists in the current directory alongside the `.rel` file, it is included automatically.
9. If a `relup` file exists (for upgrades), it is included automatically.

# Construction / Recognition

## To Construct/Create:
1. Write a `.rel` file (e.g., `mysystem.rel`) specifying `{release, {Name, Vsn}, {erts, ErtsVsn}, [AppSpecs]}`.
2. Start Erlang with the code path including all application `ebin` directories.
3. Call `target_system:create("mysystem")`.
4. The result is a `mysystem.tar.gz` file ready for installation.

## To Identify/Recognize:
1. A `.tar.gz` file produced by `target_system:create/1`.
2. Contains `bin/start.boot`, `bin/epmd`, `bin/run_erl`, `bin/to_erl`.
3. Contains `releases/start_erl.data` and `releases/<version>/start.boot`.

# Context & Application

The `target_system` module is provided as an example in the `sasl` application. The creation step is performed on a development machine; the resulting tar archive is then transferred to the target machine for installation. The `plain.boot` file (copied to `bin/start.boot`) enables basic target system startup with only Kernel and STDLIB, while the full boot file in `releases/<version>/start.boot` boots all applications.

# Examples

**Example 1** (Creating a Target System section): The `.rel` file and creation call:

```erlang
%% mysystem.rel
{release,
 {"MYSYSTEM", "FIRST"},
 {erts, "5.10.4"},
 [{kernel, "2.16.4"},
  {stdlib, "1.19.4"},
  {sasl, "2.3.4"},
  {pea, "1.0"}]}.
```

```text
% erl -pa /home/user/target_system/myapps/pea-1.0/ebin
1> target_system:create("mysystem").
```

**Example 2** (Creating a Target System section): The resulting tar archive contents:

```text
erts-5.10.4/bin/
releases/FIRST/start.boot
releases/FIRST/mysystem.rel
releases/mysystem.rel
lib/kernel-2.16.4/
lib/stdlib-1.19.4/
lib/sasl-2.3.4/
lib/pea-1.0/
```

# Relationships

## Builds Upon
- **target-system** — creation is the first step in producing a target system
- **release** — uses the `.rel` file format and `systools` functions

## Enables
- **target-system-installation** — the tar archive produced by creation is the input to installation

## Related
- **target-system-upgrade** — creating a new version uses the same `target_system:create/1` process

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Not having all application `ebin` directories on the code path when calling `target_system:create/1`.
  **Correction**: Use `-pa` flags to ensure all application paths are available before calling create.

- **Error**: Forgetting to include the `sasl` application in the `.rel` file.
  **Correction**: The `sasl` application provides `release_handler` functionality needed for upgrades; include it.

# Common Confusions

- **Confusion**: Thinking the `.rel` file lists only custom applications.
  **Clarification**: The `.rel` file must list all applications to include, both standard OTP (Kernel, STDLIB, SASL) and custom ones, each with their exact version numbers.

- **Confusion**: Wondering why `mysystem.rel` appears twice in the tar archive.
  **Clarification**: The file is duplicated in both `releases/` and `releases/FIRST/` because the archive may be unpacked without `release_handler`, which would otherwise copy it.

# Source Reference

"Creating a Target System" section, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Direct from source text with detailed step-by-step description.
- Confidence rationale: High — exhaustive procedural description in the source.
- Uncertainties: None.
- Cross-reference status: References target-system, target-system-installation, target-system-upgrade.
