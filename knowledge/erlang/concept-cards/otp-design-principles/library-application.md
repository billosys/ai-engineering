---
# === CORE IDENTIFICATION ===
concept: Library Application
slug: library-application

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-types
tier: foundational

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Overview"
chapter_number: null
pdf_page: null
section: "Applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "library app"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
extends:
  - application
related:
  - supervision-tree
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a library application in Erlang/OTP?"
  - "How does a library application differ from an application with processes?"
---

# Quick Definition

A library application is an Erlang/OTP application that has no processes and consists only of a collection of functional modules.

# Core Definition

According to the OTP Design Principles Overview: "The simplest applications do not have any processes, but consist of a collection of functional modules. Such an application is called a library application." The source gives STDLIB as an example of a library application. This contrasts with applications that have processes, which are "easiest implemented as a supervision tree using the standard behaviours."

# Prerequisites

- **Application** — a library application is a specific type of OTP application.

# Key Properties

1. Contains no processes — only functional modules.
2. Represents the simplest form of an OTP application.
3. Follows the OTP application directory structure for modules.
4. STDLIB is cited as an example of a library application.

# Construction / Recognition

## To Construct/Create:
1. Organize functional modules into the standard OTP application directory structure.
2. Create an application resource file (`.app` file) without a `mod` key.
3. Do not define a supervision tree or start any processes.

## To Identify/Recognize:
1. An OTP application with no `mod` key in its `.app` file (no application callback module starting processes).
2. Contains only functional (stateless) modules — no gen_server, gen_event, or supervisor modules.
3. No supervision tree.

# Context & Application

Library applications are used for collections of utility functions, data structures, and algorithms that do not require their own processes. The OTP standard libraries themselves (STDLIB) are organized this way. The application concept in OTP "applies both to program structure (processes) and directory structure (modules)," so even process-free code is organized as applications to fit into the OTP release structure.

# Examples

**Example 1** (design_principles.md, "Applications"): "An example of a library application is STDLIB." The source also notes that Kernel and STDLIB are the two applications forming the minimal Erlang/OTP system.

# Relationships

## Builds Upon
- **Application** — a library application is a type of OTP application.

## Enables
- No direct dependents within this source.

## Related
- **Supervision Tree** — applications with processes use supervision trees; library applications do not.
- **release** — library applications are included in releases alongside process-based applications.

## Contrasts With
- Applications with processes (which are implemented as supervision trees).

# Common Errors

- **Error**: Trying to start a supervision tree in a library application.
  **Correction**: If processes are needed, the application is not a library application. Implement it as a regular application with a supervision tree.

# Common Confusions

- **Confusion**: Thinking all OTP applications must have processes.
  **Clarification**: Library applications have no processes — they are purely functional module collections packaged as OTP applications for the directory structure and release system.

# Source Reference

OTP Design Principles, Overview, "Applications" section (design_principles.md).

# Verification Notes

- Definition source: Directly quoted from design_principles.md "Applications" section.
- Confidence rationale: High — explicitly defined with a named example (STDLIB).
- Uncertainties: None.
- Cross-reference status: References application, supervision-tree, release (planned cards).
