---
# === CORE IDENTIFICATION ===
concept: Application Master
slug: application-master

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-structure
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Using the main graphical introspection tools"
chapter_number: 5
pdf_page: null
section: "5.1.1 The Appmon GUI"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - application master processes
  - "application master"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - application-behaviour
extends: []
related:
  - root-supervisor
  - starting-an-application
  - appmon
contrasts_with:
  - root-supervisor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an application master?"
  - "Which processes call an application's start and stop callbacks?"
  - "What sits above the root supervisor in a process tree?"
---

# Quick Definition

The application master processes are the two unnamed processes, part of the `application` behaviour container, that the system spawns when an application starts; they call the application's `start/2` and `stop/1` callbacks.

# Core Definition

The application master processes are part of the `application` behaviour container and are spawned by the system when an application starts (Ch. 5, Section 5.1.1). In Appmon's view of a running application, they appear as the two topmost, unnamed processes. You do not need to know anything more about them except that they call the `start` function of the application behaviour module (e.g. `tr_app:start/2`); when the application is shutting down, they similarly call the application behaviour's `stop` function (e.g. `tr_app:stop/1`) as the last thing they do after all other application processes have stopped.

# Prerequisites

- **OTP application** — Application masters belong to a running application.
- **Application behaviour** — The masters call the application behaviour callbacks.

# Key Properties

1. Two unnamed processes per running application.
2. Part of the `application` behaviour container.
3. Spawned by the system when the application starts.
4. They call the application behaviour module's `start/2` callback.
5. They call the application behaviour module's `stop/1` callback last, on shutdown.

# Construction / Recognition

## To Recognize Application Masters:
1. In Appmon's application view, the two topmost unnamed processes are the application masters.
2. They sit above the application's root supervisor in the process tree.

# Context & Application

The application masters are infrastructure: the programmer rarely interacts with them but should recognize them when inspecting a running system.

- **Typical contexts**: Visible at the top of an application's process tree in Appmon.
- **Common applications**: The two unnamed processes above `tr_sup` in the `tcp_rpc` Appmon view.

# Examples

**Example 1** (Ch. 5, Figure 5.3): In the Appmon application window for `tcp_rpc`, the two topmost unnamed processes are the application master processes; they call `tr_app:start/2`.

# Relationships

## Related
- **root-supervisor** — The application masters start (via `start/2`) and sit above the root supervisor.
- **starting-an-application** — Application masters are part of bringing an application up.
- **appmon** — The masters are visible in Appmon's application view.

## Contrasts With
- **root-supervisor** — The application masters are container infrastructure that *call* `start/2`; the root supervisor is what `start/2` *starts*.

# Common Errors

- **Error**: Trying to interact with or kill the application master processes directly.
  **Correction**: They are container infrastructure; manage the application via `application:start/1`/`stop/1`.

# Common Confusions

- **Confusion**: Mistaking the unnamed top processes for the root supervisor.
  **Clarification**: The unnamed top processes are the application masters; the root supervisor is the next process below them.

# Source Reference

Chapter 5: Using the main graphical introspection tools, Section 5.1.1 "The Appmon GUI," discussion of Figure 5.3.

# Verification Notes

- Definition source: Synthesized from the Appmon discussion in Section 5.1.1.
- Confidence rationale: MEDIUM — the book describes them only in passing while explaining Appmon and explicitly says you need not know more.
- Uncertainties: Internal details of the application master are intentionally not covered by the source.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
