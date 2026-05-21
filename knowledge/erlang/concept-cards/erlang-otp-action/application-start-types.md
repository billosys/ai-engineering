---
# === CORE IDENTIFICATION ===
concept: Application Start Types
slug: application-start-types

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-management
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Packaging, services, and deployment"
chapter_number: 10
pdf_page: null
section: "10.1.3. How the system manages running applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - temporary application
  - permanent application
  - transient application

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - application-controller
extends: []
related:
  - target-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the application start types in OTP?"
  - "What is the difference between a temporary and a permanent application?"
  - "What happens to the runtime system when a permanent application terminates?"
---

# Quick Definition

An application's start type — temporary, permanent, or transient — determines what happens to the whole runtime system if that application terminates.

# Core Definition

When an application is started with `application:start(AppName)`, it gets the default type `temporary`: even if it terminates unexpectedly, the rest of the runtime system is unaffected and only a crash report is generated. An application started with `application:start(AppName, permanent)` is considered required for the target system to function: if it terminates for any reason, the entire runtime system shuts down so everything can be restarted from scratch. The type `transient` can also be specified, but for normal OTP applications it behaves just like `permanent` ("Erlang and OTP in Action," Ch. 10, Section 10.1.3).

# Prerequisites

- **OTP application** — Start types are an attribute of applications being started.
- **Application controller** — The controller honors the start type when an application terminates.

# Key Properties

1. `temporary` is the default for `application:start/1`; termination affects only that application (a crash report).
2. `permanent` marks an application as required; its termination shuts down the entire runtime system.
3. `transient` behaves just like `permanent` for normal OTP applications.
4. A full system restart following a permanent-application failure can be handled by an external OS *heart process* (see the `heart` module).

# Construction / Recognition

## To Construct/Create:
1. Start an application with `application:start(AppName)` for `temporary`.
2. Start with `application:start(AppName, permanent)` to mark it required.
3. Start with `application:start(AppName, transient)` for transient semantics.

## To Identify/Recognize:
1. Inspect the call used to start the application, or the release/boot configuration.

# Context & Application

- **Typical contexts**: Configuring which applications are critical to a target system.
- **Common applications**: Core service applications are started `permanent` so a failure triggers a clean full restart.
- **Historical/stylistic notes**: The `heart` module (part of `kernel`) lets an external OS process restart the whole node.

# Examples

**Example 1** (Section 10.1.3): `application:start(AppName)` yields a `temporary` application — an unexpected termination only generates a crash report.

**Example 2** (Section 10.1.3): `application:start(AppName, permanent)` makes the application required; its termination shuts down the whole runtime system for a from-scratch restart.

# Relationships

## Builds Upon
- **OTP application** — Start types parameterize how an application is started.

## Enables
- **Target system** — Marking applications permanent defines which failures should restart the whole node.

## Related
- **Application controller** — Enforces start-type semantics.

# Common Errors

- **Error**: Relying on `transient` to mean "restart this application only."
  **Correction**: For normal OTP applications `transient` behaves like `permanent` — termination brings down the whole node.

# Common Confusions

- **Confusion**: Thinking `temporary` means the application is unimportant.
  **Clarification**: `temporary` simply means the runtime system is not torn down if the application crashes; it is the default.

# Source Reference

Chapter 10: "Packaging, services, and deployment," Section 10.1.3 "How the system manages running applications," subsection "Application start types."

# Verification Notes

- Definition source: Direct adaptation of Section 10.1.3.
- Confidence rationale: HIGH — the book explicitly defines all three start types.
- Uncertainties: None.
- Cross-reference status: `otp-application` owned by Agent 2.
- Re-extraction notes: Fresh extraction; no prior card existed.
