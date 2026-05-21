---
# === CORE IDENTIFICATION ===
concept: Application Controller
slug: application-controller

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
  - application_controller
  - application behaviour container

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - otp-behaviour
extends: []
related:
  - application-start-types
  - application-metadata-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the application controller?"
  - "How does Erlang manage running applications?"
  - "What process loads the .app file?"
---

# Quick Definition

The application controller is the single behaviour-container process per runtime system that loads `.app` files, checks dependencies, and tracks every running application.

# Core Definition

The starting point for an OTP application is an implementation of the `application` behaviour, but there is also an associated behaviour container, known as the *application controller*, which handles all the applications running in the system. There is only one application controller per runtime system, registered under the name `application_controller`, and it is started early in the boot sequence. The controller loads the `.app` file for each application, checks that all the applications it depends on have been started first, and for each running application spawns a pair of application master processes to isolate itself from the application code ("Erlang and OTP in Action," Ch. 10, Section 10.1.3).

# Prerequisites

- **OTP application** — The application controller manages applications; you must understand applications first.
- **OTP behaviour** — The application controller is the container half of the `application` behaviour.

# Key Properties

1. Exactly one application controller per Erlang runtime system.
2. Registered under the name `application_controller`; has a very low process identifier (started early in boot).
3. Loads each application's `.app` file.
4. Checks that an application's dependencies have already been started before starting it.
5. Spawns a pair of application master processes per running application, isolating itself from application code.
6. Architecturally similar to `gen_event`: a single container manages multiple behaviour implementations.

# Construction / Recognition

## To Construct/Create:
This is part of the runtime system; you do not create it. It is started automatically during VM boot.

## To Identify/Recognize:
1. Call `whereis(application_controller)` in the shell — it returns a low-numbered pid.
2. It appears in the output of `registered()` alongside other kernel-level registered processes.

# Context & Application

- **Typical contexts**: Every running Erlang node has an application controller managing its applications.
- **Common applications**: Backs `application:start/1,2` and `application:stop/1`.
- **Historical/stylistic notes**: The internal structure of the `application` behaviour container is more complex than most behaviours, but the `application` module API is straightforward.

# Examples

**Example 1** (Section 10.1.3): `registered()` lists `application_controller` among the early-boot processes; `whereis(application_controller)` returns `<0.6.0>`, showing its low pid.

# Relationships

## Builds Upon
- **OTP behaviour** — It is the container component of the `application` behaviour.

## Enables
- **OTP application** — The controller is what actually starts, stops, and tracks applications.

## Related
- **Application start types** — The controller honors temporary/permanent/transient start types.
- **Application metadata file** — The controller loads the `.app` file.

# Common Errors

- **Error**: Assuming each application has its own controller.
  **Correction**: There is only one `application_controller` per runtime system.

# Common Confusions

- **Confusion**: Confusing the application controller with application master processes.
  **Clarification**: The controller is the single system-wide manager; application masters are the per-application process pairs it spawns to isolate itself from application code.

# Source Reference

Chapter 10: "Packaging, services, and deployment," Section 10.1.3 "How the system manages running applications."

# Verification Notes

- Definition source: Direct adaptation of Section 10.1.3.
- Confidence rationale: HIGH — the book explicitly names and describes the application controller.
- Uncertainties: None.
- Cross-reference status: `otp-application` and `otp-behaviour` owned by Agent 2.
- Re-extraction notes: Fresh extraction; no prior card existed.
