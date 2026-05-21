---
# === CORE IDENTIFICATION ===
concept: Primary Application
slug: primary-application

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-structure
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Included Applications"
chapter_number: null
pdf_page: null
section: "Introduction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "primary app"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
  - included-application
extends:
  - application
related:
  - application-master
  - application-controller
  - start-phases
contrasts_with:
  - included-application

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a primary application from an included application?"
---

# Quick Definition

A primary application is an OTP application that is not included by any other application; it has its own application master, is independently started and stopped, and may include other applications within its supervisor tree.

# Core Definition

According to the OTP Design Principles "Included Applications" chapter: "An application that is not included by any other application is called a primary application." A primary application has its own application master (created by the application controller), manages its own lifecycle, and can contain included applications whose supervisor trees are grafted into its own. When start phases are used, the primary application's application master orchestrates the `start_phase` callbacks for both itself and its included applications.

# Prerequisites

- **Application** — a primary application is a type of application.
- **Included Application** — the concept of "primary" is defined in contrast to "included."

# Key Properties

1. Not included by any other application.
2. Has its own application master created by the application controller.
3. Independently started with `application:start/1` and stopped with `application:stop/1`.
4. Can include other applications via the `included_applications` key in its .app file.
5. Takes responsibility for starting the top supervisors of its included applications.
6. When start phases are used, the primary application defines the superset of phases.
7. The application master calls `Module:start(normal, StartArgs)` and then orchestrates start phase callbacks.

# Construction / Recognition

## To Construct/Create:
1. Create an application with a callback module, .app file, and supervision tree.
2. Do not list it in any other application's `included_applications` key.
3. Optionally include other applications via the `included_applications` key.
4. If using start phases with included applications, set the `mod` key to `{application_starter, [Module, StartArgs]}`.

## To Identify/Recognize:
1. An application not listed in any other application's `included_applications` key.
2. Has its own application master at runtime.
3. Started independently via `application:start/1`.

# Context & Application

Most OTP applications are primary applications. The distinction between primary and included only matters when one application needs to embed another within its supervisor tree. The primary application is the independently deployable unit — it owns the application master, defines the lifecycle boundary, and orchestrates the startup sequence for any included applications.

# Examples

**Example 1** (included_applications.md, "Introduction"): The Mermaid diagram shows a primary application at the top of a tree, with included applications as children. The primary application owns the entire hierarchy.

**Example 2** (included_applications.md, "Synchronizing Processes during Startup"): When `prim_app` starts with included `incl_app` and start phases:
```erlang
application:start(prim_app)
 => prim_app_cb:start(normal, [])
 => prim_app_cb:start_phase(init, normal, [])
 => prim_app_cb:start_phase(go, normal, [])
 => incl_app_cb:start_phase(go, normal, [])
ok
```
Here `prim_app` is the primary application that orchestrates the entire startup sequence.

**Example 3** (included_applications.md, "Synchronizing Processes during Startup"): For a primary application with start phases, the `mod` key uses `application_starter`:
```erlang
{mod, {application_starter,[prim_app_cb,[]]}}
```

# Relationships

## Builds Upon
- **Application** — a primary application is an application that is not included by any other.
- **Included Application** — the concept is defined in contrast to included applications.

## Enables
- **Start Phases** — the primary application defines the superset of phases for itself and its included applications.

## Related
- **Application Master** — a primary application has its own application master.
- **Application Controller** — the controller starts primary applications directly.

## Contrasts With
- **Included Application** — an included application is started as part of another application's supervisor tree, not independently.

# Common Errors

- **Error**: Forgetting to use `application_starter` in the `mod` key when the primary application uses start phases with included applications.
  **Correction**: The source requires: "The value of the `mod` key of the including application must be set to `{application_starter,[Module,StartArgs]}`."

# Common Confusions

- **Confusion**: Thinking "primary" is a special application type that must be declared.
  **Clarification**: "Primary" simply means "not included by any other application." It is the default state — any application that is not listed in another application's `included_applications` key is primary.

# Source Reference

OTP Design Principles, "Included Applications" chapter, "Introduction" and "Synchronizing Processes during Startup" sections (included_applications.md).

# Verification Notes

- Definition source: Directly quoted from included_applications.md "Introduction" section.
- Confidence rationale: High — explicitly defined with a clear one-sentence definition.
- Uncertainties: None.
- Cross-reference status: References application, included-application, application-master, application-controller, start-phases.
