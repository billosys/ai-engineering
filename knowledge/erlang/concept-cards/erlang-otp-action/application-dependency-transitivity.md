---
# === CORE IDENTIFICATION ===
concept: Application Dependency Transitivity
slug: application-dependency-transitivity

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
  - transitive dependencies
  - indirect dependencies

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - application-metadata-file
extends: []
related:
  - erlang-release
  - rel-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is dependency transitivity between applications?"
  - "What is an indirect dependency?"
  - "Why must a release include indirect dependencies?"
---

# Quick Definition

If application A depends on B and B depends on C, then A depends indirectly on C — the depends-on relation is transitive, so a release must include all such indirect dependencies.

# Core Definition

Applications usually have dependencies declared in their `.app` files. In general there may also be indirect dependencies: if application A depends on application B, which in turn depends on application C, then application A depends indirectly on application C, because the depends-on relation is transitive. When building a release, the included applications are those required for the primary functionality plus all their direct and indirect dependencies ("Erlang and OTP in Action," Ch. 10, Section 10.1.2 sidebar "Dependencies and transitivity").

# Prerequisites

- **OTP application** — Transitivity describes relationships between applications.
- **Application metadata file** — Direct dependencies are declared in the `.app` file's `applications` key.

# Key Properties

1. The depends-on relation between applications is transitive.
2. A direct dependency is one listed in an application's own `.app` file.
3. An indirect dependency is reached through a chain of one or more direct dependencies.
4. Practically all applications depend directly on `kernel` and `stdlib`.
5. A release must contain the complete closure of direct and indirect dependencies.

# Construction / Recognition

## To Construct/Create:
1. Read the `applications` key of the primary application's `.app` file.
2. Recursively read the `applications` key of every dependency.
3. The union of all reachable applications is the dependency closure.

## To Identify/Recognize:
1. Trace the `applications` lists across `.app` files; any application reachable but not directly listed is an indirect dependency.

# Context & Application

- **Typical contexts**: Determining the complete application list for a release.
- **Common applications**: `simple_cache` depends directly on `kernel`, `stdlib`, `mnesia`, `resource_discovery`, and `sasl`; any of those bringing in further dependencies makes them indirect dependencies of `simple_cache`.
- **Historical/stylistic notes**: The book recommends running `systools:make_script` to discover the correct versions of all transitive dependencies.

# Examples

**Example 1** (Section 10.1.2): If A depends on B and B depends on C, then A depends indirectly on C.

**Example 2** (Section 10.2.2): A target system for `simple_cache` needs `simple_cache` and `resource_discovery` plus all the applications they depend on directly or indirectly: `stdlib`, `kernel`, `sasl`, and `mnesia`.

# Relationships

## Builds Upon
- **Application metadata file** — Direct dependencies come from the `applications` key.

## Enables
- **Erlang release** — A release must include the full transitive dependency closure.

## Related
- **.rel file** — Must list every application, direct and indirect.

# Common Errors

- **Error**: Listing only the primary application's direct dependencies in a release.
  **Correction**: Include the complete transitive closure of all direct and indirect dependencies.

# Common Confusions

- **Confusion**: Believing an application only depends on what its own `.app` file lists.
  **Clarification**: It also depends on everything those dependencies depend on, recursively.

# Source Reference

Chapter 10: "Packaging, services, and deployment," Section 10.1.2 "Metadata," sidebar "Dependencies and transitivity."

# Verification Notes

- Definition source: Direct adaptation of the "Dependencies and transitivity" sidebar.
- Confidence rationale: HIGH — the book explicitly defines transitivity of dependencies.
- Uncertainties: None.
- Cross-reference status: `otp-application` owned by Agent 2.
- Re-extraction notes: Fresh extraction; no prior card existed.
