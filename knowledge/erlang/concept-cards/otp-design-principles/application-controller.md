---
# === CORE IDENTIFICATION ===
concept: Application Controller
slug: application-controller

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
section: "Application Controller"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "application_controller"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
extends: []
related:
  - application-master
  - application-resource-file
  - application-configuration
contrasts_with:
  - application-master

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the application controller relate to the application master?"
  - "What is an OTP application?"
---

# Quick Definition

The application controller is a process registered as `application_controller`, started as part of the Kernel application, that coordinates all operations on applications including loading, unloading, starting, and stopping them.

# Core Definition

According to the OTP Design Principles "Applications" chapter: "When an Erlang runtime system is started, a number of processes are started as part of the Kernel application. One of these processes is the application controller process, registered as `application_controller`." The source further states: "All operations on applications are coordinated by the application controller." The `application` module in Kernel provides the API (`load`, `unload`, `start`, `stop`) that delegates to the application controller.

# Prerequisites

- **Application** — the application controller manages the lifecycle of applications.

# Key Properties

1. A process started as part of the Kernel application at runtime startup.
2. Registered as `application_controller`.
3. Coordinates all operations on applications: loading, unloading, starting, stopping.
4. Reads and stores information from the .app file when loading an application.
5. Checks that all dependency applications are running before starting an application.
6. Creates an application master for each started application.
7. Automatically loads included applications when loading a primary application.
8. Accessible through the `application` module API.

# Construction / Recognition

## To Construct/Create:
1. The application controller is created automatically — it is started as part of the Kernel application when the Erlang runtime boots. There is no manual construction.

## To Identify/Recognize:
1. The process registered as `application_controller`.
2. The process that responds to `application:load/1`, `application:start/1`, etc.
3. Part of the Kernel application's process hierarchy.

# Context & Application

The application controller is the central coordinator for the OTP application lifecycle. Every call to `application:start/1`, `application:stop/1`, `application:load/1`, or `application:unload/1` goes through this process. It maintains an internal database of loaded application specifications (from .app files) and running application status. For distributed applications, it works alongside the `dist_ac` (distributed application controller) process.

# Examples

**Example 1** (applications.md, "Loading and Unloading Applications"): Loading an application causes the controller to read and store the .app file information:
```erlang
1> application:load(ch_app).
ok
2> application:loaded_applications().
[{kernel,"ERTS  CXC 138 10","2.8.1.3"},
 {stdlib,"ERTS  CXC 138 10","1.11.4.3"},
 {ch_app,"Channel allocator","1"}]
```

**Example 2** (applications.md, "Loading and Unloading Applications"): Unloading erases the application from the controller's internal database:
```erlang
3> application:unload(ch_app).
ok
4> application:loaded_applications().
[{kernel,"ERTS  CXC 138 10","2.8.1.3"},
 {stdlib,"ERTS  CXC 138 10","1.11.4.3"}]
```

**Example 3** (applications.md, "Starting and Stopping Applications"): When starting, the controller checks dependencies, loads if needed, then creates an application master:
```erlang
5> application:start(ch_app).
ok
6> application:which_applications().
[{kernel,"ERTS  CXC 138 10","2.8.1.3"},
 {stdlib,"ERTS  CXC 138 10","1.11.4.3"},
 {ch_app,"Channel allocator","1"}]
```

# Relationships

## Builds Upon
- **Application** — the controller manages the lifecycle of all applications.

## Enables
- **Application Master** — the controller creates an application master for each started application.
- **Included Application** — the controller automatically loads included applications.

## Related
- **Application Resource File** — the controller reads .app files when loading applications.
- **Application Configuration** — the controller manages configuration parameter access.

## Contrasts With
- **Application Master** — the controller is the single global coordinator; the master is a per-application process that directly manages one application's supervision tree. The controller creates the master.

# Common Errors

- **Error**: Thinking that loading an application also loads its code (beam files).
  **Correction**: The source explicitly notes: "Loading/unloading an application does not load/unload the code used by the application. Code loading is handled in the usual way by the code server."

# Common Confusions

- **Confusion**: Confusing the application controller with the application master.
  **Clarification**: There is one application controller per node (global coordinator). Each running application has its own application master (per-application process). The controller creates masters when starting applications.

# Source Reference

OTP Design Principles, "Applications" chapter, "Application Controller" and "Loading and Unloading Applications" and "Starting and Stopping Applications" sections (applications.md).

# Verification Notes

- Definition source: Directly quoted from applications.md "Application Controller" section.
- Confidence rationale: High — explicitly defined with process registration name and role clearly stated.
- Uncertainties: None.
- Cross-reference status: References application, application-master, application-resource-file, application-configuration.
