---
# === CORE IDENTIFICATION ===
concept: Erlang Release
slug: erlang-release

# === CLASSIFICATION ===
category: applications-releases
subcategory: packaging
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Packaging, services, and deployment"
chapter_number: 10
pdf_page: null
section: "10.2. Making a release"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - OTP release
  - release

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - application-metadata-file
extends: []
related:
  - rel-file
  - boot-script
  - sys-config
  - release-package
  - target-system
contrasts_with:
  - otp-application
  - target-system

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang/OTP release?"
  - "How does a release differ from an application?"
  - "What does a release contain?"
---

# Quick Definition

A release is the highest level of code packaging in Erlang/OTP: a versioned set of applications plus metadata describing how to start and manage them together as a complete system.

# Core Definition

A release consists of a set of applications together with some metadata specifying how to start and manage those applications as a system. The applications in a release execute together in the same Erlang runtime system. In this respect, a release can be seen as a service definition: the running Erlang VM becomes a system-level service. A release specifies which versions of its applications are required and also has a version number of its own; for example, the release `simple_cache-0.1.4` may require `simple_cache-0.3.0`, `resource_discovery-0.1.0`, `kernel-4.5.6`, and `stdlib-6.0.5` ("Erlang and OTP in Action," Ch. 10, Section 10.2.1).

# Prerequisites

- **OTP application** — A release is built by aggregating applications; you must understand applications before releases.
- **Application metadata file** — Each application's `.app` file provides the version and dependency information a release relies upon.

# Key Properties

1. A release describes a running Erlang runtime system.
2. A release has a version of its own (a version string, conventionally formatted).
3. A release aggregates a number of versioned applications along with metadata on how to manage the system.
4. The applications included are the primary functionality plus all their direct and indirect (transitive) dependencies.
5. Installing a release on a host machine produces a target system.
6. Packaging in Erlang/OTP is a hierarchy: modules group into applications, and applications group into releases.

# Construction / Recognition

## To Construct/Create:
1. Decide which applications should be included (primary apps plus all dependencies).
2. Create a release metadata (`.rel`) file describing the release's contents.
3. Create the boot script (`.script` and `.boot` files) with `systools:make_script/2`.
4. Create a system configuration file (`sys.config`) — optional but typically present.
5. Pack everything in a single package file with `systools:make_tar/2`.

## To Identify/Recognize:
1. Look for a `.rel` file whose first tuple element is the atom `release`.
2. Check that it lists a release name/version pair and an ERTS version.

# Context & Application

- **Typical contexts**: Preparing an Erlang system for deployment as a standalone service.
- **Common applications**: Bundling a service (e.g., the Simple Cache) plus its dependencies for installation on production hosts.
- **Historical/stylistic notes**: The book notes that releases "have been seen as deep magic that only the Erlang illuminati used," but are conceptually straightforward.

# Examples

**Example 1** (Section 10.2.1): The Simple Cache release definitely needs `simple_cache` and `resource_discovery`; both depend on further applications which must all be included.

**Example 2** (Section 10.2.1): Release `simple_cache-0.1.4` requires `simple_cache-0.3.0`, `resource_discovery-0.1.0`, `kernel-4.5.6`, and `stdlib-6.0.5` (Figure 10.2).

# Relationships

## Builds Upon
- **OTP application** — A release aggregates one or more applications.

## Enables
- **Target system** — Installing a release produces a target system.
- **Release package** — A release is packaged into a tarball for deployment.

## Related
- **.rel file** — The metadata file that defines a release.
- **Boot script** — Generated from the `.rel` file to actually start the release.
- **sys.config** — Optional system configuration bundled with a release.

## Contrasts With
- **OTP application** — An application is one unit of functionality; a release combines several into a complete system.
- **Target system** — A release is the specification/package; the target system is the installed, running result.

# Common Errors

- **Error**: Omitting indirect (transitive) dependencies from the release.
  **Correction**: Include the primary applications and ALL their direct and indirect dependencies.

- **Error**: Mismatched application versions between the `.rel` file and the `.app` files.
  **Correction**: Make the version numbers in the `.rel` file match those declared in each application's `.app` file.

# Common Confusions

- **Confusion**: Believing a release and a target system are the same thing.
  **Clarification**: A release is the versioned specification plus packaged artifacts; a target system is what results from installing a release on a host.

# Source Reference

Chapter 10: "Packaging, services, and deployment," Section 10.2 "Making a release" (10.2.1 "Releases"). See Figure 10.2 (releases and versioning).

# Verification Notes

- Definition source: Direct adaptation of Section 10.2.1 prose.
- Confidence rationale: HIGH — the book explicitly defines releases and summarizes their properties in a bulleted list.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs for this chapter set and Agent 2 (`otp-application`).
- Re-extraction notes: Fresh extraction; no prior card existed.
