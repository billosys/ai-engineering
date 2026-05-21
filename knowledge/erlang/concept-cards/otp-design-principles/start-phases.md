---
# === CORE IDENTIFICATION ===
concept: Start Phases
slug: start-phases

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-runtime
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Included Applications"
chapter_number: null
pdf_page: null
section: "Synchronizing Processes during Startup"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "start_phases"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
  - included-application
  - primary-application
  - application-callback-module
  - application-master
extends: []
related:
  - application-resource-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an included application?"
  - "What distinguishes a primary application from an included application?"
---

# Quick Definition

Start phases are a mechanism for synchronizing processes during startup across a primary application and its included applications, defined as ordered `{Phase, PhaseArgs}` tuples in the `.app` file and invoked via `Module:start_phase/3` callbacks.

# Core Definition

According to the OTP Design Principles "Included Applications" chapter: "If there is a need for synchronization between processes in the including and included applications, this can be achieved by using start phases." Start phases are defined by the `start_phases` key in the `.app` file as a list of `{Phase, PhaseArgs}` tuples, where `Phase` is an atom and `PhaseArgs` is a term. The application master calls `Module:start_phase(Phase, Type, PhaseArgs)` for the primary application and each included application in top-down, left-to-right order, for each phase defined for the primary application.

# Prerequisites

- **Application** — start phases are an application-level mechanism.
- **Included Application** — start phases exist to synchronize between including and included applications.
- **Primary Application** — the primary application defines the superset of phases.
- **Application Callback Module** — the `start_phase/3` callback must be implemented.
- **Application Master** — the master orchestrates the phase callbacks.

# Key Properties

1. Defined in the `.app` file as `{start_phases, [{Phase, PhaseArgs}]}`.
2. `Phase` is an atom; `PhaseArgs` is any term.
3. The primary application's `mod` key must use `{application_starter, [Module, StartArgs]}` when start phases are used.
4. Startup sequence: (1) `Module:start(normal, StartArgs)` for the primary app, (2) then each phase is called in order for the primary app and all included apps.
5. Phases are called in top-down, left-to-right order across the application inclusion tree.
6. If a phase is not defined for an included application, the callback is not called for that phase and application.
7. The included application's phases must be a subset of the primary application's phases.
8. Included applications that themselves contain included applications must use `{application_starter, [Module, StartArgs]}` in their `mod` key.

# Construction / Recognition

## To Construct/Create:
1. In the primary application's `.app` file, add `{start_phases, [{init,[]}, {go,[]}]}`.
2. Set the primary application's `mod` to `{application_starter, [Module, StartArgs]}`.
3. In each included application's `.app` file, add `{start_phases, [{go,[]}]}` (a subset of the primary's phases).
4. Implement `start_phase(Phase, Type, PhaseArgs)` in each application's callback module.

## To Identify/Recognize:
1. The `start_phases` key in a `.app` file.
2. The `mod` key using `application_starter` instead of a direct callback module.
3. A callback module implementing `start_phase/3`.

# Context & Application

Start phases solve the problem of ordered initialization when multiple applications (a primary and its included applications) need to coordinate their startup. Without start phases, the including application simply starts the included application's top supervisor, but there is no mechanism for the included application's processes to synchronize with the including application's processes. Start phases provide defined synchronization points during the startup sequence.

# Examples

**Example 1** (included_applications.md, "Synchronizing Processes during Startup"): Primary application `.app` with start phases:
```erlang
{application, prim_app,
 [{description, "Tree application"},
  {vsn, "1"},
  {modules, [prim_app_cb, prim_app_sup, prim_app_server]},
  {registered, [prim_app_server]},
  {included_applications, [incl_app]},
  {start_phases, [{init,[]}, {go,[]}]},
  {applications, [kernel, stdlib, sasl]},
  {mod, {application_starter,[prim_app_cb,[]]}},
  {env, [{file, "/usr/local/log"}]}
 ]}.
```

**Example 2** (included_applications.md, "Synchronizing Processes during Startup"): Included application with a subset of phases:
```erlang
{application, incl_app,
 [{description, "Included application"},
  {vsn, "1"},
  {modules, [incl_app_cb, incl_app_sup, incl_app_server]},
  {registered, []},
  {start_phases, [{go,[]}]},
  {applications, [kernel, stdlib, sasl]},
  {mod, {incl_app_cb,[]}}
 ]}.
```

**Example 3** (included_applications.md, "Synchronizing Processes during Startup"): The complete callback sequence when starting `prim_app`:
```erlang
application:start(prim_app)
 => prim_app_cb:start(normal, [])
 => prim_app_cb:start_phase(init, normal, [])
 => prim_app_cb:start_phase(go, normal, [])
 => incl_app_cb:start_phase(go, normal, [])
ok
```
Note that `incl_app` does not participate in the `init` phase because it only defines the `go` phase.

# Relationships

## Builds Upon
- **Included Application** — start phases exist to synchronize between including and included applications.
- **Primary Application** — the primary application defines the superset of phases.
- **Application Callback Module** — `start_phase/3` is a callback function.
- **Application Master** — the master calls the phase callbacks.

## Enables
- No further concepts — start phases are a leaf mechanism.

## Related
- **Application Resource File** — the `start_phases` key is defined in the .app file.
- **Failover** — the source notes that if an application has `start_phases` defined, failover uses `Module:start({failover, Node}, StartArgs)` instead of `Module:start(normal, StartArgs)`.

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Defining phases in the included application that are not defined in the primary application.
  **Correction**: "The set of specified phases must be a subset of the set of phases specified for the primary application."

- **Error**: Using the direct callback module in `mod` instead of `application_starter` for the primary application.
  **Correction**: "The value of the `mod` key of the including application must be set to `{application_starter,[Module,StartArgs]}`."

# Common Confusions

- **Confusion**: Thinking start phases replace the normal `start/2` callback.
  **Clarification**: `start/2` is still called first to create the supervision tree. Start phases provide additional synchronization points after the tree is started.

- **Confusion**: Thinking the included application's `Module:start/2` is called.
  **Clarification**: `Module:start/2` is "called only for the primary application." The included application's `StartArgs` in the `mod` key is ignored; only `start_phase/3` is called for included applications.

# Source Reference

OTP Design Principles, "Included Applications" chapter, "Synchronizing Processes during Startup" section (included_applications.md).

# Verification Notes

- Definition source: Directly quoted from included_applications.md "Synchronizing Processes during Startup" section.
- Confidence rationale: High — explicitly defined with detailed rules, .app file examples, and a complete callback sequence.
- Uncertainties: None.
- Cross-reference status: References included-application, primary-application, application-callback-module, application-master, application-resource-file, failover.
