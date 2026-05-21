---
# === CORE IDENTIFICATION ===
concept: Application Master
slug: application-master

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-runtime
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Applications"
chapter_number: null
pdf_page: null
section: "Starting and Stopping Applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
  - application-controller
  - application-callback-module
extends: []
related:
  - supervision-tree
  - start-phases
contrasts_with:
  - application-controller

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the application controller relate to the application master?"
---

# Quick Definition

The application master is a per-application process created by the application controller when starting an application; it serves as the group leader for all processes in the application, calls the callback module's `start/2` and `stop/1`, and manages the application's shutdown.

# Core Definition

According to the OTP Design Principles "Applications" chapter: "the application controller creates an application master for the application." The source further explains: "The application master establishes itself as the group leader of all processes in the application and will forward I/O to the previous group leader." The purpose of the application master being group leader is "to easily keep track of which processes that belong to the application." The master starts the application by calling the callback function `start/2` and stops it by telling the top supervisor to shut down, then calling `stop/1`.

# Prerequisites

- **Application** — the application master manages one application's runtime lifecycle.
- **Application Controller** — the controller creates the application master.
- **Application Callback Module** — the master invokes the callback module's functions.

# Key Properties

1. Created by the application controller when an application is started.
2. One application master per running application (per-application process).
3. Establishes itself as the group leader of all processes in the application.
4. Forwards I/O to the previous group leader.
5. Starts the application by calling `Module:start(StartType, StartArgs)`.
6. Stops the application by telling the top supervisor to shut down.
7. After the supervision tree terminates, calls `Module:stop(State)` for cleanup.
8. Enables `application:get_application/0` and `application:get_env/1` to work correctly.
9. Ensures all processes belonging to the application are terminated on stop.

# Construction / Recognition

## To Construct/Create:
1. The application master is created automatically by the application controller when `application:start/1` is called. There is no manual construction.

## To Identify/Recognize:
1. The group leader of processes within a running application.
2. The process that directly called the application callback module's `start/2`.
3. Created after the application controller verifies all dependency applications are running.

# Context & Application

The application master is the bridge between the application controller (the global coordinator) and the individual application's supervision tree. By making itself the group leader, it establishes a process-ownership boundary: it can track which processes belong to the application. This mechanism supports clean shutdown (all application processes are terminated) and runtime introspection (`application:get_application/0`).

# Examples

**Example 1** (applications.md, "Starting and Stopping Applications"): When `application:start(ch_app)` is called, the application controller creates an application master which then calls `ch_app:start(normal, [])` to start the supervision tree.

**Example 2** (applications.md, "Starting and Stopping Applications"): On stop: "The application master stops the application by telling the top supervisor to shut down. The top supervisor tells all its child processes to shut down, and so on; the entire tree is terminated in reverse start order. The application master then calls the application callback function `stop/1` in the module defined by the `mod` key."

**Example 3** (included_applications.md, "Synchronizing Processes during Startup"): When start phases are used, the application master calls `Module:start_phase(Phase, Type, PhaseArgs)` for each phase defined for the primary application and its included applications, in top-down, left-to-right order.

# Relationships

## Builds Upon
- **Application Controller** — the controller creates the application master.
- **Application Callback Module** — the master calls `start/2` and `stop/1` on the callback module.
- **Application** — one master exists per running application.

## Enables
- **Supervision Tree** — the master initiates creation of the supervision tree via `start/2`.
- **Start Phases** — the master orchestrates start phase callbacks for included applications.

## Related
- **Supervision Tree** — the master starts and stops the top supervisor.

## Contrasts With
- **Application Controller** — the controller is a single global process; the master is a per-application process. The controller coordinates all applications; the master manages one application's lifecycle.

# Common Errors

- **Error**: Attempting to manually create or interact with the application master process.
  **Correction**: The application master is an internal OTP mechanism. Interact with applications through the `application` module API.

# Common Confusions

- **Confusion**: Thinking the application controller directly starts the supervision tree.
  **Clarification**: The controller creates the application master, and the master calls the callback module's `start/2` which starts the supervision tree. The master, not the controller, is the direct manager of the application's processes.

- **Confusion**: Thinking the group leader role is incidental.
  **Clarification**: The group leader mechanism is how OTP tracks process ownership. It enables `application:get_application/0` and ensures all application processes are terminated when the application stops.

# Source Reference

OTP Design Principles, "Applications" chapter, "Starting and Stopping Applications" section (applications.md).

# Verification Notes

- Definition source: Directly quoted from applications.md "Starting and Stopping Applications" section including the Note about group leader purpose.
- Confidence rationale: High — explicitly defined with detailed description of role, purpose, and behavior.
- Uncertainties: None.
- Cross-reference status: References application-controller, application-callback-module, supervision-tree, start-phases.
