---
# === CORE IDENTIFICATION ===
concept: Included Applications
slug: included-applications

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
section: "Included Applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "included application"
  - "subapplications"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - application-resource-file
extends: []
related:
  - start-phases
  - supervisor
contrasts_with:
  - otp-application

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I structure an OTP application?"
  - "What is an OTP application?"
---

# Quick Definition

An included application is an application listed in another application's `included_applications` property; it is loaded with the main application but its supervision tree is started by the main application's top-level supervisor, not on its own.

# Core Definition

In an app resource file you may specify the `included_applications` parameter, listing applications included as subapplications of the main one (Cesarini & Vinoski, p. 215). When the main application is started, all included applications are loaded but not started; it is up to the top-level supervisor of the main application to start the included applications' supervision trees, either as dynamic children or as static children returned from `init/1` (p. 221). In every node an included application may be included only once by other applications — this avoids clashes in the application namespace. The primary reason to use included applications instead of a flat structure is to coordinate start phases (pp. 221-222).

# Prerequisites

- **OTP application** — An included application is an OTP application embedded in another.
- **Application resource file** — Inclusion is declared via the `.app` file's `included_applications` property.

# Key Properties

1. Declared in the main application's `.app` file via `included_applications`.
2. Loaded with the main application, but *not* started automatically.
3. The main application's top-level supervisor starts the included application's supervision tree.
4. An included application may be included only once per node (namespace safety).
5. Their directories sit in the `lib` directory alongside other applications.
6. The main reason to use them over a flat structure is start-phase coordination.

# Construction / Recognition

## To Construct/Create:
1. Add `{included_applications, [App, ...]}` to the main application's `.app` file.
2. Have the main application's top-level supervisor start each included application's supervision tree (calling its `start/2` or its top-level supervisor's `start_link`).
3. To coordinate start phases, set the main `.app` file's `mod` to `{application_starter, [Mod, Args]}`.

## To Identify/Recognize:
1. An `included_applications` property in an application's `.app` file.
2. The included application loads but does not start its own supervision tree.

# Context & Application

- **Typical contexts**: Composing a top-level application out of subapplications with coordinated startup.
- **Common applications**: Synchronizing included applications' start phases with the main application.
- **Historical/stylistic notes**: The book stresses that if you need several identical supervision trees in a node, use a standalone library application instead — included applications must be unique (p. 222).

# Examples

**Example 1** (pp. 223-224): `top_app` includes `bsc` via `included_applications`; `top_app`'s `start/2` calls `bsc_sup:start_link()` to start the included application's tree.

**Example 2** (p. 224): The shell run showing `top_app` start phases interleaving with `bsc`'s common `admin` phase.

## Worked Example

The `top_app.app` resource file declaring an included application (pp. 223-224):

```erlang
{application, top_app,
 [{description, "Included Application Example"},
  {vsn, "1.0"},
  {modules, [top_app]},
  {applications, [kernel, stdlib, sasl]},
  {included_applications, [bsc]},
  {start_phases, [{start, []}, {admin, []}, {stop, []}]},
  {mod, {application_starter, [top_app, []]}}]}.
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- **Start phases** — Included applications exist mainly to enable cross-application start-phase coordination.

## Related
- **Supervisor** — The main application's top-level supervisor starts the included application's tree.

## Contrasts With
- **OTP application** — A normal (non-included) application starts its own supervision tree via its application master; an included application's tree is started by the including application's supervisor.

# Common Errors

- **Error**: Including the same application in two different applications on one node.
  **Correction**: An included application may be included only once per node; otherwise registered-name and module clashes occur.

- **Error**: Returning `{ok, Pid, Data}` from an included application's `start/2`.
  **Correction**: `Data` cannot be passed through to `prep_stop/1` for an included application; return `{ok, Pid}`.

# Common Confusions

- **Confusion**: Thinking included applications start themselves.
  **Clarification**: They are loaded but not started; the including application's top-level supervisor must start their supervision trees.

# Source Reference

Chapter 8: Applications, "Included Applications" and "Start Phases in Included Applications," pages 221-224.

# Verification Notes

- Definition source: Direct adaptation from pp. 221-222.
- Confidence rationale: HIGH — explicitly defined with the `top_app` example and resource file shown.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
