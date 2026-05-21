---
# === CORE IDENTIFICATION ===
concept: Start Phases
slug: start-phases

# === CLASSIFICATION ===
category: applications-releases
subcategory: applications
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Applications"
chapter_number: 8
pdf_page: 222
section: "Start Phases"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "start phase"
  - "start_phases"
  - "start_phase/3"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - application-behaviour
  - application-resource-file
extends: []
related:
  - included-applications
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I package, start, and configure a release?"
  - "How do I structure an OTP application?"
---

# Quick Definition

Start phases let an application be brought up in named stages: after the supervision tree starts but before `application:start/1` returns, the callback `start_phase/3` is invoked once per phase declared in the `.app` file.

# Core Definition

Some systems are so complex that it is not enough to start each application one at a time; applications need to be started in phases and synchronized with each other (Cesarini & Vinoski, p. 225). Phases are declared in the `.app` file's `start_phases` property as a list of `{Phase, Args}` tuples. The application callback module must export `start_phase(StartPhase, StartType, Args)`; this function is called for every declared phase, after the supervision tree has been started but before `application:start(Application)` returns. Each phase invokes operations and sets internal state that allows or disallows requests — for example moving the node through an *administration state* and then an *operational state* (pp. 225-226).

# Prerequisites

- **OTP application** — Start phases stage the startup of an OTP application.
- **Application behaviour** — `start_phase/3` is an optional application callback.
- **Application resource file** — Phases are declared in the `.app` file's `start_phases` property.

# Key Properties

1. Declared in the `.app` file: `{start_phases, [{Phase, Args}, ...]}`.
2. The callback module exports `start_phase(StartPhase, StartType, Args)`.
3. `start_phase/3` is called once per declared phase.
4. Phases run after the supervision tree starts, but before `application:start/1` returns.
5. `StartType` is `normal`, `{takeover, Node}`, or `{failover, Node}`.
6. For included applications, set the main `.app` file's `mod` to `{application_starter, [Mod, Args]}`; only phases the main and included applications share are invoked for the included ones.

# Construction / Recognition

## To Construct/Create:
1. Add `{start_phases, [{Phase, Args}, ...]}` to the `.app` file.
2. Export and define `start_phase/3` in the application callback module.
3. For included applications, use `{mod, {application_starter, [Mod, Args]}}`.

## To Identify/Recognize:
1. A `start_phases` property in the `.app` file.
2. A `start_phase/3` function exported from the application callback module.

# Context & Application

- **Typical contexts**: Complex nodes that must synchronize startup across subsystems.
- **Common applications**: Loading Mnesia tables, then enabling administration, then enabling operational traffic.
- **Historical/stylistic notes**: The book describes a three-phase instant-messaging node: load routing tables, enable the administration state, then enable the operational state (pp. 225-226).

# Examples

**Example 1** (p. 226): Adding `{start_phases, [{init, []}, {admin, []}, {oper, []}]}` to `bsc.app` and defining `start_phase/3` to print each phase.

**Example 2** (p. 224): `top_app` defining `start`, `admin`, `stop` phases; only the `admin` phase shared with included `bsc` triggers `bsc`'s `start_phase/3`.

## Worked Example

Declaring phases and defining the callback (p. 226):

```erlang
%% In bsc.app
{start_phases, [{init, []}, {admin, []}, {oper, []}]}

%% In bsc.erl
start_phase(StartPhase, StartType, Args) ->
    io:format("bsc:start_phase(~p,~p,~p).~n", [StartPhase, StartType, Args]).
```

Starting the application then prints `init`, `admin`, `oper` in order.

# Relationships

## Builds Upon
- *(none)*

## Enables
- *(none)*

## Related
- **Included applications** — Start phases are the main reason to use included applications, enabling cross-application startup coordination.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Defining `start_phases` in the `.app` file but not exporting `start_phase/3`.
  **Correction**: The callback module must export and define `start_phase/3`, or startup fails.

- **Error**: Expecting a phase defined only in an included application (not the top-level one) to fire.
  **Correction**: Only phases shared with the top-level application trigger `start_phase/3` for included applications.

# Common Confusions

- **Confusion**: Thinking `start_phase/3` runs before the supervision tree.
  **Clarification**: Phases run *after* the supervision tree is started, but before `application:start/1` returns.

# Source Reference

Chapter 8: Applications, "Start Phases" and "Start Phases in Included Applications," pages 225-226, 222-224.

# Verification Notes

- Definition source: Direct adaptation from pp. 225-226.
- Confidence rationale: HIGH — explicitly defined with `.app` declarations, the callback, and a shell run shown.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
