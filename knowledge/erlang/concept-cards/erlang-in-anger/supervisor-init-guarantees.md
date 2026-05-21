---
concept: Supervisor Init Guarantees
slug: supervisor-init-guarantees
category: fault-tolerance
subcategory: supervision
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Building Open Source Erlang Software"
chapter_number: 2
pdf_page: null
section: "It's About the Guarantees"
extraction_confidence: high
aliases:
  - "It's about the guarantees"
prerequisites:
  - synchronous-supervision-startup
  - let-it-crash
extends: []
related:
  - connect-in-init-anti-pattern
  - application-start-types
contrasts_with: []
answers_questions:
  - "What state belongs in a process's init function?"
  - "Why do supervisors require stable initialization?"
---

# Quick Definition

A supervised process's initialization must establish a stable, known state — a guarantee, not a best effort — so that processes started afterward can rely on the rest of the system already being healthy.

# Core Definition

From Chapter 2, section "It's About the Guarantees": "Restarting a process is about bringing it back to a stable, known state. From there, things can be retried. When the initialization isn't stable, supervision is worth very little. An initialized process should be stable no matter what happens." And: "Supervised processes *provide guarantees* in their initialization phase, *not a best effort*."

The book's principle: "it's all about the guarantees."

# Prerequisites

- `synchronous-supervision-startup` — because startup is synchronous and ordered, a process's init must be trustworthy before later processes start.
- `let-it-crash` — supervision's value depends on restarting *to a stable state*.

# Key Properties

1. Initialization must reach a stable, known state, no matter what happens.
2. If init is not stable, supervision provides little more than a `try ... catch` in a loop.
3. A process should only guarantee, during init, something it can ensure "no matter what happens."
4. A guarantee that cannot be met (e.g. a required precondition is missing) should crash the node — it is a system-wide assertion failure.
5. What belongs in init: configuration files, file-system access (e.g. logging), dependable local resources (opening UDP ports for logs), restoring stable state from disk or network — even if syncing gigabytes takes 10+ minutes.
6. What does not belong in init: connections to non-local databases and external services, whose failure is expected during normal operation.

# Construction / Recognition

When writing `init/1`: ask "can I guarantee this is true no matter what?" If yes (local, dependable resources), include it and load it synchronously. If no (remote services), do not make its presence a guarantee — initialize the *manager* of the resource instead, and reconnect later.

# Context & Application

This principle governs the boundary between what a process synchronously establishes at boot and what it handles dynamically afterward. It is the reason the book opposes cooldown supervisors: the fix for unstable init is to weaken the guarantee, not to delay restarts.

# Examples

From Chapter 2, section "It's About the Guarantees": "You could force a connection during initialization if you know the database is on the same host and should be booted before your Erlang system... If, on the other hand, your database is on a remote host, you should expect the connection to fail... the only guarantee you can make in the client process is that your client will be able to handle requests, but not that it will communicate to the database. It could return `{error, not_connected}` on all calls during a net split."

# Relationships

## Builds Upon
- `synchronous-supervision-startup` — synchronous boot is what makes guarantees meaningful.
- `let-it-crash` — restarts only help if they restore a stable state.

## Enables
- `connect-in-init-anti-pattern` — defines the standard the anti-pattern violates.

## Related
- `application-start-types` — another lever for deciding how much failure a system tolerates.

## Contrasts With
Nothing directly.

# Common Errors

- Guaranteeing a remote dependency in init, which makes a transient network failure crash the whole boot.
- Adding a cooldown to a supervisor instead of weakening an over-strong init guarantee.

# Common Confusions

- "Provide guarantees" does not mean "never fail." If a genuine precondition is unmet, crashing the node is the *correct* outcome — a failed system-wide assertion.
- The callers of a client, not the client itself, should decide how much failure they tolerate.

# Source Reference

Chapter 2: Building Open Source Erlang Software, Sections "It's About the Guarantees," "Side Effects," and "In a nutshell". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 2, section "It's About the Guarantees."
- Confidence rationale: high — the principle is stated and developed at length.
- Uncertainties: none.
- Cross-reference status: Verified
