---
# === CORE IDENTIFICATION ===
concept: Application Directory Structure
slug: application-directory-structure

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
section: "Directory Structure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "OTP directory structure"
  - "application directory layout"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
  - application-resource-file
extends: []
related:
  - release
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create an OTP application?"
---

# Quick Definition

The application directory structure is the standardized layout of directories and files that an OTP application follows, with required directories like `src` and `ebin`, and optional directories like `priv`, `include`, `doc`, and `test`.

# Core Definition

According to the OTP Design Principles "Applications" chapter: "When packaging code using systools, the code for each application is placed in a separate directory, `lib/Application-Vsn`, where `Vsn` is the version number." The structure defines where source code, compiled beams, include files, private data, documentation, and tests reside. A development structure omits the version number from the directory name, while a released structure follows a stricter layout with `ebin` as a required directory.

# Prerequisites

- **Application** — the directory structure exists to organize an application's files.
- **Application Resource File** — the .app file resides within this directory structure.

# Key Properties

1. Development structure: `${application}/` with `src` (required), `priv` (optional), `include` (optional), `doc` (recommended), `test` (recommended).
2. Released structure: `${application}-${version}/` with `ebin` (required, contains .beam and .app files), `src` (optional), `priv` (optional), `include` (optional).
3. The `.app.src` file lives in `src/` during development; the `.app` file lives in `ebin/` when released.
4. The `priv` directory holds runtime assets; accessed via `code:priv_dir/1`.
5. `priv/lib` for shared-object files (NIFs, linked-in drivers); `priv/bin` for executables (port programs).
6. Code for other languages (C, Java, Go) goes in `c_src`, `java_src`, `go_src` directories.
7. Directory names should not be capitalized; empty directories should be omitted.
8. The code server automatically uses code from the directory with the highest version number.

# Construction / Recognition

## To Construct/Create:
1. Create the application root directory named after the application (no version in development).
2. Create `src/` — place Erlang source files and `.app.src` here.
3. Create `ebin/` (for released systems) — place `.beam` files and the `.app` file here.
4. Optionally create `include/` for public header files, `priv/` for runtime assets, `doc/` for documentation, `test/` for test suites.
5. For released systems, name the directory `${application}-${version}`.

## To Identify/Recognize:
1. A directory containing at least `src/` (development) or `ebin/` (released) subdirectories.
2. Contains an `.app` or `.app.src` file.
3. Follows the naming convention `${application}` or `${application}-${version}`.

# Context & Application

The standard directory structure ensures that OTP tools (systools, code server, release handling) can locate and manage application code. Even when not using systools, following this convention is recommended because Erlang/OTP itself is packaged this way. The code server relies on this structure to find and load the correct version of application modules.

# Examples

**Example 1** (applications.md, "Directory Structure"): Development directory structure:
```text
─ ${application}
  ├── doc
  │   ├── internal
  │   ├── examples
  │   └── src
  ├── include
  ├── priv
  ├── src
  │   └── ${application}.app.src
  └── test
```

**Example 2** (applications.md, "Directory Structure for a Released System"): Released directory structure:
```text
─ ${application}-${version}
  ├── bin
  ├── doc
  │   ├── html
  │   ├── man[1-9]
  │   ├── pdf
  │   ├── internal
  │   └── examples
  ├── ebin
  │   └── ${application}.app
  ├── include
  ├── priv
  │   ├── lib
  │   └── bin
  └── src
```

# Relationships

## Builds Upon
- **Application** — the directory structure organizes the files of an application.
- **Application Resource File** — the .app file is placed within this structure.

## Enables
- **Release** — systools uses this directory structure to package applications into releases.

## Related
- **Release** — releases expect applications to follow this directory structure.

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Placing the `.app` file outside of `ebin/` in a released application.
  **Correction**: The source states that for a released system, "The `.app` file must also be placed here [in `ebin`]."

- **Error**: Capitalizing directory names.
  **Correction**: The source states "Directory names should not be capitalized."

# Common Confusions

- **Confusion**: Confusing the development and released directory structures.
  **Clarification**: In development, the version number is omitted from the directory name and `.app.src` lives in `src/`. In a released system, the directory is `${application}-${version}` and the `.app` file is in `ebin/`.

# Source Reference

OTP Design Principles, "Applications" chapter, "Directory Structure" section (applications.md).

# Verification Notes

- Definition source: Directly from applications.md "Directory Structure" section with both development and released layouts quoted.
- Confidence rationale: High — extensively documented with directory trees and detailed descriptions of each subdirectory.
- Uncertainties: None.
- Cross-reference status: References application, application-resource-file, release.
