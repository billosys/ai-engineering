---
# === CORE IDENTIFICATION ===
concept: Links
slug: links

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-supervision
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Links"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - process link
  - link/1
  - spawn_link
  - linked set

# === TYPED RELATIONSHIPS ===
prerequisites:
  - processes-and-message-passing
extends: []
related:
  - exit-signals
contrasts_with:
  - monitors

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a process link in Erlang?"
  - "How do links relate to monitors?"
  - "What concepts are needed before building a supervision tree?"
---

# Quick Definition

A link is a bidirectional connection between two processes. When either linked process terminates, an exit signal is sent to the other, which by default also terminates.

# Core Definition

"Calling `link(Pid)` in a process A creates a bidirectional link between processes A and Pid. Calling `spawn_link/3` has the same effect as calling `spawn/3` followed by `link/1`, except that it is executed atomically, eliminating the race condition where a process terminates between the spawn and the link. A link from the calling process to Pid is removed by calling `unlink(Pid)`" (Cesarini & Vinoski, p. 36). "If two Erlang processes are linked, when either of them terminates, an exit signal is sent to the other, which will then itself terminate. The terminated process will in turn send the exit signal to all the processes in its linked set, propagating it through the system" (p. 36).

# Prerequisites

- **Processes and message passing** — Links connect processes and are "effectuated with" message passing; the process model is required.

# Key Properties

1. A link is bidirectional: it affects both processes equally.
2. `link(Pid)` creates a link; `unlink(Pid)` removes it.
3. `spawn_link/3` spawns and links atomically, avoiding a spawn-then-link race.
4. When a linked process terminates, an exit signal is sent to the other.
5. By default, an abnormal exit signal terminates the receiving process, propagating through the linked set.
6. Linking to a nonexistent process terminates the linking process.
7. Default behavior can be modified by trapping exits.

# Construction / Recognition

## To Construct:
1. Call `link(Pid)` to link to an existing process.
2. Or call `spawn_link/3` to spawn a linked process atomically.
3. Call `unlink(Pid)` to break the link.

## To Recognize:
1. Look for `link/1`, `spawn_link`, or `unlink/1` calls.

# Context & Application

- **Typical contexts**: Building supervision; tying a server's lifetime to its parent.
- **Common applications**: "A server that controls access to resources links to a client while that client has access to a particular resource" (p. 37), so the server learns if the client dies.
- **Historical/stylistic notes**: Links are the primitive on which supervisors are built.

# Examples

**Example 1** (p. 37): A resource-controlling server links to a client holding a resource; if the client terminates, the server is informed so it can reallocate the resource, and may `unlink` when the client returns the resource.

**Example 2** (p. 36): `spawn_link/3` equals `spawn/3` + `link/1` done atomically.

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- **Exit signals** — Links are the channel along which exit signals propagate.

## Related
- *(none additional)*

## Contrasts With
- **Monitors** — Monitors are unidirectional and never kill the observer; links are bidirectional and propagate termination.

# Common Errors

- **Error**: Using `spawn/3` then `link/1` separately.
  **Correction**: Use `spawn_link/3` to avoid the race where the process dies between the two calls.
- **Error**: Linking a client to a server when you only want one-way observation.
  **Correction**: A server crash would then kill the client; use a monitor instead.

# Common Confusions

- **Confusion**: Thinking a link only propagates termination one way.
  **Clarification**: Links are bidirectional — either process's death affects the other.

# Source Reference

Chapter 1: Introducing Erlang, Section "Links and Monitors for Supervision" / "Links," pages 36-38. See Figures 2-2 and 2-3.

# Verification Notes

- Definition source: Direct quotes from pp. 36-37.
- Confidence rationale: HIGH — explicit definition and usage pattern.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
