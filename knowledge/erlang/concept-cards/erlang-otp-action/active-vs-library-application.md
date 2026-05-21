---
# === CORE IDENTIFICATION ===
concept: Active vs Library Application
slug: active-vs-library-application

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
  - active application
  - library application

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
extends:
  - otp-application
related:
  - application-behaviour
  - root-supervisor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between an active and a library application?"
  - "Does a library application need to be started?"
  - "What is a root supervisor's role in an active application?"
---

# Quick Definition

An active application is a living system with a life cycle that must be started to be useful; a library application is a passive collection of modules used by other applications and never started or stopped.

# Core Definition

OTP applications come in two kinds (Ch. 4, "Active versus library applications" sidebar). *Library applications* are nothing but a collection of modules to be used by other applications — they are passive and do not need to be started or stopped (the Erlang/OTP `stdlib` is an example). *Active applications* are living things that are started, run for some time, and eventually shut down; an active application has a *root supervisor* whose job is to manage the application's processes. Both kinds use the same directory layout and metadata files and fit into the overall OTP application framework; the main difference is that active applications have a life cycle and must be started to be useful. The book focuses on active applications.

# Prerequisites

- **OTP application** — Active and library are the two kinds of application.

# Key Properties

1. Library application: passive collection of modules; not started or stopped.
2. Active application: a living system with a life cycle; must be started.
3. An active application has a root supervisor managing its processes.
4. Both kinds use the same directory layout and metadata files.
5. The `mod` parameter in the `.app` file is what makes an application active.

# Construction / Recognition

## To Recognize the Kind:
1. Check the `.app` file for a `mod` parameter — present means active, absent means library.
2. An active application's `.app` file names an `application` behaviour module.

# Context & Application

The distinction tells you whether `application:start/1` does meaningful work (active) or merely makes modules available (library).

- **Typical contexts**: Deciding whether an application needs an `application` behaviour module and a supervisor.
- **Common applications**: `tcp_rpc` and `simple_cache` are active; `stdlib` is a library application.

# Examples

**Example 1** (Ch. 4): `stdlib` is given as the example library application — a passive collection of modules.

**Example 2** (Ch. 4): `tcp_rpc` is an active application with a root supervisor (`tr_sup`) managing the `tr_server` process.

# Relationships

## Builds Upon
- **OTP application** — Active and library are the two kinds.

## Related
- **application-behaviour** — Active applications implement it; library applications do not.
- **root-supervisor** — An active application has one; a library application does not.

## Contrasts With
- The two kinds are themselves the contrast within this card.

# Common Errors

- **Error**: Adding an `application` behaviour module to a pure library application.
  **Correction**: Library applications need no `mod` parameter and no behaviour module.

# Common Confusions

- **Confusion**: Thinking every application must be started.
  **Clarification**: Only active applications have a life cycle; library applications are just modules and are never started.

# Source Reference

Chapter 4: OTP applications and supervision, Section 4.1 "OTP applications," "Active versus library applications" sidebar.

# Verification Notes

- Definition source: Direct adaptation of the "Active versus library applications" sidebar.
- Confidence rationale: HIGH — explicit definition in a dedicated sidebar.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
