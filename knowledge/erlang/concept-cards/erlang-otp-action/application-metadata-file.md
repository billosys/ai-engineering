---
# === CORE IDENTIFICATION ===
concept: Application Metadata File
slug: application-metadata-file

# === CLASSIFICATION ===
category: applications-releases
subcategory: metadata
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Packaging, services, and deployment"
chapter_number: 10
pdf_page: null
section: "10.1.2. Metadata"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - .app file
  - app file
  - application resource file

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
extends: []
related:
  - rel-file
  - application-controller
  - application-dependency-transitivity
contrasts_with:
  - rel-file

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the .app file?"
  - "What metadata does an application's .app file contain?"
  - "Why is the vsn tuple important?"
---

# Quick Definition

The `.app` file is the metadata file for a single OTP application — a single Erlang term listing its modules, dependencies, version, and how to start it.

# Core Definition

Most applications are active, not mere libraries, so OTP needs a certain amount of information to know how an application is started, what other applications it depends on, and so on. This information is contained in the `.app` file. The file is a single Erlang `{application, Name, [...]}` tuple containing keys such as `description`, `vsn`, `modules`, `registered`, `applications` (dependencies), and `mod` (the application callback module). One piece of information is particularly important in the context of releases: the `vsn` tuple, which specifies the current version of the application ("Erlang and OTP in Action," Ch. 10, Section 10.1.2).

# Prerequisites

- **OTP application** — The `.app` file is metadata describing one application.

# Key Properties

1. Contains a single Erlang tuple `{application, Name, [KeyValueList]}` terminated by a period.
2. `description` — a human-readable description string.
3. `vsn` — the application's version string (critical for releases).
4. `modules` — the list of modules belonging to the application.
5. `registered` — names of processes the application registers.
6. `applications` — the applications this one depends on (e.g., `kernel`, `stdlib`).
7. `mod` — the application callback module and its start argument, e.g. `{sc_app, []}`.

# Construction / Recognition

## To Construct/Create:
1. Write a file `Name.app` containing one `{application, Name, [...]}` tuple.
2. Fill in `description`, `vsn`, `modules`, `registered`, `applications`, and `mod`.
3. Place it in the application's `ebin` directory.

## To Identify/Recognize:
1. A file with the `.app` extension whose content begins with the atom `application`.

# Context & Application

- **Typical contexts**: Every OTP application carries a `.app` file.
- **Common applications**: The `application_controller` reads it to start and manage the application.
- **Historical/stylistic notes**: Version numbers in the `.app` file must match those referenced from a release's `.rel` file.

# Examples

**Example 1** (Listing 10.1): The `simple_cache.app` file declares `{vsn, "0.3.0"}`, a `modules` list, `{registered, [sc_sup]}`, `{applications, [kernel, sasl, stdlib, mnesia, resource_discovery]}`, and `{mod, {sc_app, []}}`.

# Relationships

## Builds Upon
- **OTP application** — Metadata for a single application.

## Enables
- **Erlang release** — Release `.rel` files reference application versions declared in `.app` files.

## Related
- **Application controller** — Loads and checks the `.app` file.
- **Application dependency transitivity** — The `applications` key declares direct dependencies.

## Contrasts With
- **.rel file** — The `.app` file describes one application; the `.rel` file describes a whole release of applications.

# Common Errors

- **Error**: Letting the `vsn` in the `.app` file drift out of sync with what the `.rel` file references.
  **Correction**: Keep application version numbers consistent between `.app` and `.rel` files.

# Common Confusions

- **Confusion**: Confusing the `.app` file with the `.rel` file.
  **Clarification**: `.app` is per-application metadata; `.rel` is per-release metadata listing many applications.

# Source Reference

Chapter 10: "Packaging, services, and deployment," Section 10.1.2 "Metadata." See Listing 10.1 (`simple_cache.app`).

# Verification Notes

- Definition source: Direct adaptation of Section 10.1.2 and Listing 10.1.
- Confidence rationale: HIGH — the book explicitly describes the `.app` file and shows a complete example.
- Uncertainties: None.
- Cross-reference status: `otp-application` owned by Agent 2.
- Re-extraction notes: Fresh extraction; no prior card existed.
