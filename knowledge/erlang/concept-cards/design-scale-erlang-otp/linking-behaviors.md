---
# === CORE IDENTIFICATION ===
concept: Linking Behaviors
slug: linking-behaviors

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Generic Servers"
chapter_number: 3
pdf_page: 96
section: "Linking Behaviors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_server:start"
  - "gen_server:start_link"
  - behavior parent link

# === TYPED RELATIONSHIPS ===
prerequisites:
  - starting-a-gen-server
  - links
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why should a behavior be linked to its parent?"
  - "What is the difference between gen_server:start and gen_server:start_link?"
---

# Quick Definition

`gen_server:start_link` links a behavior to its parent so the two share fate; `gen_server:start` starts it unlinked. Behaviors should normally be linked, so subsystems shut down cleanly without orphan processes.

# Core Definition

"When you start behaviors in the shell, you link the shell process to them. If the shell process terminates abnormally, its EXIT signal will propagate to the behaviors it started and cause them to terminate. Generic servers can be started without linking them to their parent by calling `gen_server:start/3` or `gen_server:start/4`. Use these functions with care, and preferably only for development and testing purposes, because behaviors should always be linked to their parent" (Cesarini & Vinoski, p. 99). "When shutting down a subsystem, you need to be 100% certain that all processes associated with that subsystem are terminated, and avoid leaving any orphan processes lingering. The only way to do so with certainty is using links."

# Prerequisites

- **Starting a gen_server** — Linking is a property of which start function you choose.
- **Links** — A behavior's parent link is an ordinary process link.

# Key Properties

1. `gen_server:start_link/3,4` starts the behavior linked to the calling (parent) process.
2. `gen_server:start/3,4` starts the behavior *unlinked*.
3. An unlinked start should be used only for development and testing.
4. Behaviors should normally be linked to their parent.
5. Links are the only way to be certain all of a subsystem's processes terminate together.
6. Without links, shutting down a subsystem risks leaving orphan processes.

# Construction / Recognition

## To Construct:
1. Use `gen_server:start_link/3,4` so the behavior is linked to its parent.
2. Reserve `gen_server:start/3,4` for development and testing only.

## To Recognize:
1. `start_link` indicates a linked behavior; `start` indicates an unlinked one.

# Context & Application

- **Typical contexts**: Behaviors started under supervisors as part of a subsystem.
- **Common applications**: Ensuring a subsystem can be shut down with no lingering processes.
- **Historical/stylistic notes**: Erlang systems can run for years, surviving upgrades and abnormal restarts — reliable shutdown via links is part of that.

# Examples

**Example 1** (p. 99): The unlinked start functions:

```erlang
gen_server:start(NameScope,Mod,Args,Opts)
gen_server:start(Mod,Args,Opts) ->
    {ok, Pid} | {error, {already_started, Pid}}
```

**Example 2** (p. 99): Starting a behavior in the shell links the shell process to it; an abnormal shell exit propagates and terminates the behavior.

# Relationships

## Builds Upon
- **Starting a gen_server** — Linking is determined by the chosen start function.
- **Links** — A behavior's parent link is a standard process link.

## Enables
- *(none specific in scope)*

## Related
- *(none additional)*

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Using `gen_server:start` in production code.
  **Correction**: Use `gen_server:start_link` so the behavior is linked to its parent; reserve `start` for development and testing.

# Common Confusions

- **Confusion**: Thinking `start` and `start_link` differ only cosmetically.
  **Clarification**: `start_link` links the behavior to its parent (shared fate); `start` leaves it unlinked, risking orphan processes on shutdown.

# Source Reference

Chapter 3: Generic Servers, Section "Linking Behaviors," page 99.

# Verification Notes

- Definition source: Direct quotes from p. 99.
- Confidence rationale: HIGH — explicit treatment of start vs. start_link.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
