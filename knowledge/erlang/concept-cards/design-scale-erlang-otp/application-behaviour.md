---
# === CORE IDENTIFICATION ===
concept: Application Behaviour
slug: application-behaviour

# === CLASSIFICATION ===
category: applications-releases
subcategory: applications
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Applications"
chapter_number: 8
pdf_page: 222
section: "The Callback Module"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "application behavior"
  - "application callback module"
  - "application module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
extends:
  - otp-behaviors
related:
  - supervisor
  - application-resource-file
  - start-phases
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP behavior?"
  - "How do I structure an OTP application?"
  - "How does a behavior relate to its callback module?"
  - "What is a callback module?"
---

# Quick Definition

The application behavior is the OTP behavior used to define an application. Its callback module — usually only a few lines long — implements `start/2` and `stop/1`, which start and stop the application's top-level supervisor.

# Core Definition

The application behavior is no different from other OTP behaviors: the generic code lives in the `application` module (part of the `kernel` library), and a callback module contains all of the specific code (Cesarini & Vinoski, p. 208). The callback module must include the `-behavior(application).` directive and the mandatory and optional callbacks. Of all behaviors, the application callback module is the simplest — unless dealing with distributed takeovers/failovers or complex startup strategies, it requires no more than a few simple lines of code. The mandatory callbacks are `start/2` and `stop/1`; optional ones include `prep_stop/1` and `start_phase/3` (pp. 208-210).

# Prerequisites

- **OTP application** — The application behavior exists to implement an OTP application.

# Key Properties

1. Generic code is the `application` module in the `kernel` library.
2. The callback module declares `-behavior(application).`
3. Mandatory callbacks: `start(StartType, StartArgs)` and `stop(Data)`.
4. `start/2` must return `{ok, Pid}` or `{ok, Pid, Data}`, where `Pid` is the top-level supervisor.
5. Optional callbacks: `prep_stop/1` (cleanup before termination) and `start_phase/3` (phased startup).
6. It is the simplest OTP behavior — typically only a few lines.

# Construction / Recognition

## To Construct/Create:
1. Create a module with `-behavior(application).`
2. Export and define `start/2` to call the top-level supervisor's `start_link`.
3. Export and define `stop/1` (often just `ok`).
4. Reference the module in the `.app` file's `mod` key.

## To Identify/Recognize:
1. The module includes `-behavior(application).`
2. It exports `start/2` and `stop/1`.

# Context & Application

- **Typical contexts**: Every normal OTP application has one application callback module.
- **Common applications**: Bootstrapping an application's supervision tree.
- **Historical/stylistic notes**: Because it is so small, the application callback module is often combined with the top-level supervisor's callback module (their callback names do not overlap) — as `sasl.erl` does (p. 229).

# Examples

**Example 1** (p. 209): The `bsc` callback module — `start/2` calls `bsc_sup:start_link()`, `stop/1` returns `ok`.

**Example 2** (p. 230): A combined `bsc` module declaring both `-behavior(application).` and `-behavior(supervisor).`

## Worked Example

The `bsc` application callback module (p. 209):

```erlang
-module(bsc).
-behavior(application).
-export([start/2, stop/1]).

start(_StartType, _StartArgs) ->
    bsc_sup:start_link().

stop(_Data) ->
    ok.
```

`start/2`'s first argument is usually the atom `normal`; the second comes from the `mod` key of the `.app` file.

# Relationships

## Builds Upon
- **OTP behaviour** — The application behavior is one of the standard OTP behaviors.

## Enables
- **Start phases** — The optional `start_phase/3` callback enables phased startup.

## Related
- **Supervisor** — `start/2` typically calls the top-level supervisor's `start_link`.
- **Application resource file** — The `mod` key names the application callback module.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Returning `{ok, Pid, Data}` from `start/2` when the application is later used as an included application with `prep_stop/1`.
  **Correction**: The book notes `Data` cannot be passed through in that case — return `{ok, Pid}` for included applications.

- **Error**: Doing complex initialization directly in `start/2`.
  **Correction**: Keep `start/2` minimal; use start phases for phased synchronization.

# Common Confusions

- **Confusion**: Thinking the application callback module is large and complex.
  **Clarification**: It is the simplest OTP behavior — usually `start/2` just calls a supervisor's `start_link` and `stop/1` returns `ok`.

# Source Reference

Chapter 8: Applications, "The Callback Module" and "Starting and Stopping Applications," pages 208-210. See Figures 9-4 to 9-6.

# Verification Notes

- Definition source: Direct adaptation from pp. 208-209.
- Confidence rationale: HIGH — explicitly defined with the `bsc` callback module shown in full.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
