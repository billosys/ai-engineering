---
# === CORE IDENTIFICATION ===
concept: Included Application
slug: included-application

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
  - "included app"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
  - application-resource-file
  - supervision-tree
  - application-controller
extends:
  - application
related:
  - start-phases
contrasts_with:
  - primary-application

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an included application?"
  - "What distinguishes a primary application from an included application?"
---

# Quick Definition

An included application is an OTP application that has its own directory and `.app` file but is started as part of the supervisor tree of another application rather than having its own application master.

# Core Definition

According to the OTP Design Principles "Included Applications" chapter: "An application can include other applications. An included application has its own application directory and `.app` file, but it is started as part of the supervisor tree of another application." The source further specifies key constraints: "An application can only be included by one other application" and "An included application can include other applications." At runtime, "an included application is in fact part of the primary application, and a process in an included application considers itself belonging to the primary application."

# Prerequisites

- **Application** — an included application is a type of application.
- **Application Resource File** — the included application has its own .app file and is listed in the including application's `included_applications` key.
- **Supervision Tree** — the included application's top supervisor is started by a supervisor in the including application.
- **Application Controller** — the controller automatically loads included applications but does not start them.

# Key Properties

1. Has its own application directory and `.app` file.
2. Started as part of the supervisor tree of another (including) application.
3. Can only be included by one other application.
4. Can itself include other applications (nesting is allowed).
5. The application controller automatically loads included applications when loading the primary application, but does not start them.
6. The top supervisor of the included application must be started by a supervisor in the including application.
7. At runtime, processes in an included application consider themselves belonging to the primary application.
8. Specified in the including application's `.app` file via the `included_applications` key.

# Construction / Recognition

## To Construct/Create:
1. Create the included application with its own directory, modules, and `.app` file.
2. In the including application's `.app` file, add the included application to the `included_applications` key.
3. In the including application's supervisor, add the included application's top supervisor as a child.
4. If synchronization is needed, define start phases in both applications' `.app` files.

## To Identify/Recognize:
1. Listed in another application's `included_applications` key in the .app file.
2. Does not have its own application master at runtime.
3. Its processes report belonging to the primary application via `application:get_application/0`.

# Context & Application

Included applications allow composing complex applications from smaller, self-contained units without requiring each sub-unit to be independently started and stopped. This is useful when multiple application modules need tight coordination and should share a single application lifecycle. The including application takes full responsibility for starting and stopping the included application's supervision tree.

# Examples

**Example 1** (included_applications.md, "Specifying Included Applications"): A primary application `prim_app` including `incl_app`:
```erlang
{application, prim_app,
 [{description, "Tree application"},
  {vsn, "1"},
  {modules, [prim_app_cb, prim_app_sup, prim_app_server]},
  {registered, [prim_app_server]},
  {included_applications, [incl_app]},
  {applications, [kernel, stdlib, sasl]},
  {mod, {prim_app_cb,[]}},
  {env, [{file, "/usr/local/log"}]}
 ]}.
```

**Example 2** (included_applications.md, "Introduction"): "The application controller automatically loads any included applications when loading a primary application, but does not start them. Instead, the top supervisor of the included application must be started by a supervisor in the including application."

# Relationships

## Builds Upon
- **Application** — an included application is an application with a different startup mechanism.
- **Supervision Tree** — the included application's tree is grafted into the including application's tree.

## Enables
- **Start Phases** — start phases exist specifically to synchronize processes across including and included applications.

## Related
- **Application Controller** — loads but does not start included applications.
- **Application Resource File** — the `included_applications` key establishes the relationship.

## Contrasts With
- **Primary Application** — a primary application is not included by any other application; it has its own application master and is independently started/stopped.

# Common Errors

- **Error**: Expecting the application controller to start the included application automatically.
  **Correction**: The controller only loads included applications. The top supervisor of the included application must be explicitly started by a supervisor in the including application.

- **Error**: Including the same application in multiple other applications.
  **Correction**: "An application can only be included by one other application."

# Common Confusions

- **Confusion**: Thinking an included application has its own independent lifecycle.
  **Clarification**: At runtime, "an included application is in fact part of the primary application, and a process in an included application considers itself belonging to the primary application." It shares the primary application's application master.

# Source Reference

OTP Design Principles, "Included Applications" chapter, "Introduction" and "Specifying Included Applications" sections (included_applications.md).

# Verification Notes

- Definition source: Directly quoted from included_applications.md "Introduction" section.
- Confidence rationale: High — explicitly defined with constraints and behavioral details clearly stated.
- Uncertainties: None.
- Cross-reference status: References application, application-resource-file, supervision-tree, application-controller, primary-application, start-phases.
