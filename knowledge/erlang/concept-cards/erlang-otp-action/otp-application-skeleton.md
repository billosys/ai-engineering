---
# === CORE IDENTIFICATION ===
concept: OTP Application Skeleton
slug: otp-application-skeleton

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-structure
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Implementing a caching system"
chapter_number: 6
pdf_page: null
section: "6.3 Creating the basic OTP application skeleton"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - application skeleton
  - "basic application structure"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - application-organization
  - app-file
  - application-behaviour
  - root-supervisor
extends:
  - otp-application
related:
  - cache-system-design
  - simple-one-for-one
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP application skeleton?"
  - "What are the steps to create the basic application structure?"
  - "What do you build before adding real functionality?"
---

# Quick Definition

An OTP application skeleton is the minimal runnable application structure — directory layout, `.app` file, application behaviour module, and root supervisor — created before any real functionality is added.

# Core Definition

The starting point for any good Erlang project is creating a proper OTP application (Ch. 6, Section 6.3). The book builds the cache "from the other end": with no real functionality, only a design, it first sets up an *application skeleton* and then adds code to it. Setting up the application structure consists of four steps: (1) create a standard application directory layout; (2) write the `.app` file; (3) write the application behaviour implementation module (`<app>_app`); (4) implement the top-level supervisor (`<app>_sup`). The result is a working application skeleton that can be started and stopped from the Erlang shell even though it has no real functionality yet.

# Prerequisites

- **OTP application** — The skeleton is the bare form of an OTP application.
- **OTP application directory organization** — Step one of building the skeleton.
- **Application metadata file (.app)** — Step two.
- **Application behaviour** — Step three.
- **Root supervisor** — Step four.

# Key Properties

1. The minimal runnable form of an active OTP application.
2. Built in four steps: directory layout, `.app` file, `_app` module, `_sup` module.
3. Can be started and stopped before any real functionality exists.
4. Created before, not after, the application's actual logic.
5. Functionality is then added incrementally to the skeleton.

# Construction / Recognition

## To Create an Application Skeleton:
1. Create the top-level directory and `doc`, `ebin`, `include`, `priv`, `src` subdirectories.
2. Write `ebin/<app>.app` with the application metadata.
3. Write `src/<app>_app.erl` implementing the `application` behaviour.
4. Write `src/<app>_sup.erl` implementing the root supervisor.

# Context & Application

The skeleton-first approach lets you verify the application starts and stops cleanly before investing in functionality.

- **Typical contexts**: Beginning any new OTP project.
- **Common applications**: The `simple_cache` skeleton — `sc_app` and `sc_sup` — created before `sc_element`, `sc_store`, and the API.

# Examples

**Example 1** (Ch. 6, Section 6.3): The `simple_cache` directory tree, the `simple_cache.app` file listing `sc_app` and `sc_sup`, and the `sc_app` and `sc_sup` modules together form the application skeleton.

**Example 2** (Ch. 6): The skeleton can be started from the shell and run, but does nothing useful until `sc_element`, `sc_store`, and `simple_cache` are added.

# Relationships

## Builds Upon
- **OTP application** — The skeleton is a bare application.

## Related
- **cache-system-design** — The skeleton is the first build step of the cache design.
- **simple-one-for-one** — The skeleton's `sc_sup` uses this strategy.

## Contrasts With
- This is a build approach; the source draws no direct contrast.

# Common Errors

- **Error**: Writing functionality before establishing the application structure.
  **Correction**: Build the skeleton first, verify it starts and stops, then add functionality.

# Common Confusions

- **Confusion**: Thinking the skeleton must do something useful.
  **Clarification**: A skeleton is intentionally functionality-free; it only proves the application starts and stops correctly.

# Source Reference

Chapter 6: Implementing a caching system, Section 6.3 "Creating the basic OTP application skeleton" (Sections 6.3.1–6.3.4).

# Verification Notes

- Definition source: Direct adaptation of Section 6.3.
- Confidence rationale: HIGH — explicit, step-by-step treatment.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
