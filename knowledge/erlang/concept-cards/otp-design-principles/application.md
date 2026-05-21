---
# === CORE IDENTIFICATION ===
concept: Application
slug: application

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-structure
tier: foundational

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Applications"
chapter_number: null
pdf_page: null
section: "Application Concept"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "OTP application"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - supervision-tree
  - behaviour
  - release
  - application-callback-module
  - application-resource-file
  - application-controller
contrasts_with:
  - library-application

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP application?"
  - "How do I create an OTP application?"
---

# Quick Definition

An OTP application is a component that implements specific functionality and can be started and stopped as a unit, as well as reused in other systems.

# Core Definition

According to the OTP Design Principles "Applications" chapter: "After creating code to implement a specific functionality, you might consider transforming it into an application — a component that can be started and stopped as a unit, as well as reused in other systems." An application is one of the fundamental structural units in OTP, consisting of a callback module, an application resource file (.app), and typically a supervision tree.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A component that can be started and stopped as a unit.
2. Reusable across different systems.
3. Requires an application callback module describing how to start and stop it.
4. Requires an application resource file (.app) specifying modules, dependencies, and the callback module.
5. Code is placed in a pre-defined directory structure when packaged using systools.
6. Must be loaded before it can be started; loading reads the .app file.

# Construction / Recognition

## To Construct/Create:
1. Create an application callback module that describes how the application is started and stopped.
2. Create an application specification and place it in an application resource file (.app).
3. Specify which modules the application consists of and the name of the callback module in the .app file.
4. If using systools, place code in a separate directory following the pre-defined directory structure.

## To Identify/Recognize:
1. Has an `.app` file defining its specification.
2. Has a callback module implementing the `application` behaviour (unless it is a library application).
3. Can be started with `application:start/1` and stopped with `application:stop/1`.

# Context & Application

Applications are the primary unit of code organization and deployment in OTP. Every non-trivial Erlang system is composed of multiple applications. The Kernel and STDLIB are themselves applications that every other application depends on. Applications provide a standardized way to package, configure, start, and stop related functionality.

# Examples

**Example 1** (applications.md, "Application Concept"): The steps to create an application are: (1) create an application callback module describing how the application is started and stopped, (2) create an application specification in an .app file specifying modules and the callback module.

**Example 2** (applications.md, "Loading and Unloading Applications"): Loading the `ch_app` application and querying loaded applications:
```erlang
1> application:load(ch_app).
ok
2> application:loaded_applications().
[{kernel,"ERTS  CXC 138 10","2.8.1.3"},
 {stdlib,"ERTS  CXC 138 10","1.11.4.3"},
 {ch_app,"Channel allocator","1"}]
```

# Relationships

## Builds Upon
- No prerequisites — this is a foundational OTP concept.

## Enables
- **Application Callback Module** — defines how the application starts and stops
- **Application Resource File** — specifies the application's metadata and structure
- **Application Controller** — manages loading, starting, and stopping applications
- **Included Application** — applications can include other applications
- **Distributed Application** — applications can be distributed across nodes

## Related
- **Supervision Tree** — an application with processes is typically implemented as a supervision tree
- **Release** — a release is composed of multiple applications
- **Behaviour** — the `application` behaviour formalizes the callback interface

## Contrasts With
- **Library Application** — a library application cannot be started or stopped, and has no callback module

# Common Errors

- **Error**: Forgetting to specify dependent applications in the `applications` key of the .app file.
  **Correction**: Always list at least Kernel and STDLIB in the `applications` key, plus any other applications your application depends on.

# Common Confusions

- **Confusion**: Thinking "application" means the same as a running program or executable.
  **Clarification**: In OTP, an application is a reusable component — a single running Erlang system (a release) is composed of many applications.

# Source Reference

OTP Design Principles, "Applications" chapter, "Application Concept" section (applications.md).

# Verification Notes

- Definition source: Directly quoted from applications.md "Application Concept" section.
- Confidence rationale: High — explicitly defined as a core concept with detailed description and examples.
- Uncertainties: None.
- Cross-reference status: References supervision-tree, behaviour, release (existing/planned cards).
