---
# === CORE IDENTIFICATION ===
concept: OTP Application
slug: otp-application

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-structure
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "OTP applications and supervision"
chapter_number: 4
pdf_page: null
section: "4.1 OTP applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - application
  - "OTP app"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
  - supervision
extends: []
related:
  - application-organization
  - app-file
  - application-behaviour
  - supervisor
  - root-supervisor
  - active-vs-library-application
  - starting-an-application
contrasts_with:
  - erlang-release

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP application?"
  - "What does the word application mean in OTP?"
  - "How is an OTP application different from just a group of modules?"
---

# Quick Definition

An OTP application is a software component consisting of a number of modules bundled with metadata files and organized on disk by convention, so the system can start, stop, and manage it as a single named entity.

# Core Definition

In the context of OTP, the word *application* has a specific meaning: an application is a software component consisting of a number of modules bundled together with a few additional metadata files, and organized on disk according to certain conventions (Ch. 4, "Terminology: applications" sidebar). This lets the system know which applications are installed and lets you start or stop an application by its name. Applications are the way you package related modules in Erlang — the focus is not on packaging for distribution but on being able to treat a bunch of modules as a single entity. Superficially they are groups of related code; more often they are living things that start up, do their work, and shut down.

# Prerequisites

- **Erlang module** — An application bundles a number of modules.
- **Supervision** — Active applications are managed by a root supervisor and its tree.

# Key Properties

1. A software component: modules plus metadata files, organized on disk by convention.
2. Can be started and stopped by name.
3. May be a *library application* (passive code) or an *active application* (a living system).
4. An active application has a root supervisor managing its processes.
5. A running active application is essentially a tree of processes.
6. Applications declare dependencies on other applications.

# Construction / Recognition

## To Create an OTP Application:
1. Conform to the standard directory structure (`doc`, `ebin`, `include`, `priv`, `src`).
2. Add the application metadata in the form of the `.app` file.
3. Create a module that implements the `application` behaviour to start the application.

# Context & Application

Applications are the unit of packaging and lifecycle management in OTP. Conforming to the structure and basing code on OTP libraries raises fault tolerance by an order of magnitude.

- **Typical contexts**: Any deliverable Erlang subsystem; `stdlib` and `kernel` are themselves applications.
- **Common applications**: The `tcp_rpc` application wrapping `tr_server`; the `simple_cache` application.

# Examples

**Example 1** (Ch. 4): The `tcp_rpc` application wraps the `tr_server`, `tr_sup`, and `tr_app` modules into one named, startable unit.

**Example 2** (Ch. 4): The Erlang/OTP `stdlib` is given as an example of a library application — nothing but modules for others to use.

# Relationships

## Builds Upon
- **Erlang module** — An application bundles modules.

## Enables
- **starting-an-application** — An application can be started by name.
- **root-supervisor** — An active application starts a root supervisor.

## Related
- **application-organization** — The standard directory layout.
- **app-file** — The metadata file describing the application.
- **application-behaviour** — The behaviour implemented to start an application.
- **active-vs-library-application** — The two kinds of application.

## Contrasts With
- **release** — A release aggregates a number of applications into a complete deliverable system; an application is one component.

# Common Errors

- **Error**: Treating "application" loosely as any group of modules.
  **Correction**: In OTP, an application has a precise meaning — modules plus metadata, on-disk conventions.

# Common Confusions

- **Confusion**: Thinking an application and a release are the same.
  **Clarification**: An application is one component; a release aggregates multiple applications into a complete system.

# Source Reference

Chapter 4: OTP applications and supervision, Section 4.1 "OTP applications," including the "Terminology: applications" and "Active versus library applications" sidebars and Section 4.1.4 ("Application structure summary").

# Verification Notes

- Definition source: Direct adaptation of the "Terminology: applications" sidebar.
- Confidence rationale: HIGH — explicit, dedicated definition in the source.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slugs `erlang-module`, `supervision` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
