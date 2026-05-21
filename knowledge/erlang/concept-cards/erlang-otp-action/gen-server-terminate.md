---
# === CORE IDENTIFICATION ===
concept: gen_server terminate/2 Callback
slug: gen-server-terminate

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: generic-server
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Writing a TCP-based RPC service"
chapter_number: 3
pdf_page: null
section: "3.2.4 The callback function section"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "terminate/2"
  - cleanup callback

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - behaviour-callback-section
extends:
  - behaviour-callback-section
related:
  - gen-server-init
  - gen-server-code-change
  - sc-store
contrasts_with:
  - gen-server-init

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the gen_server terminate/2 callback do?"
  - "When is terminate/2 called?"
  - "Where should a gen_server clean up resources?"
---

# Quick Definition

`terminate/2` is the `gen_server` callback invoked when the server is shutting down; it is the place to clean up resources before the process dies.

# Core Definition

`terminate/2` is one of the six `gen_server` interface callbacks. When a `gen_server` shuts down, it calls the `terminate/2` callback to give the implementation a chance to clean things up (Ch. 6, Section 6.4.1). In the minimal `gen_server` module it simply returns `ok`; in real servers it performs cleanup work. It takes two arguments: the termination reason and the final server state. When the process dies, the server state vanishes on its own, so `terminate/2` is needed only for cleanup that the state's disappearance does not cover — such as external mappings.

# Prerequisites

- **gen_server behaviour** — `terminate/2` is a `gen_server` callback.
- **Behaviour callback function section** — `terminate/2` lives in the callback section.

# Key Properties

1. Called when the `gen_server` is shutting down.
2. Takes the termination reason and the final state.
3. The place to release resources not handled by the vanishing state.
4. In trivial servers it just returns `ok`.
5. Runs as the last thing before the process dies.

# Construction / Recognition

## To Write terminate/2:
1. Match the reason and state arguments.
2. Perform any external cleanup (closing handles, removing mappings).
3. Return `ok` (the minimal implementation returns `ok` directly).

# Context & Application

`terminate/2` matters when a process holds resources outside its own state — files, sockets, or entries in a shared table.

- **Typical contexts**: Releasing external resources on shutdown.
- **Common applications**: `sc_element:terminate/2` calls `sc_store:delete(Pid)` to remove the key-to-pid mapping when the storage process dies.

# Examples

**Example 1** (Ch. 3, Listing 3.1/3.5): The minimal and `tr_server` `terminate/2` callbacks return `ok` because nothing special is needed on shutdown.

**Example 2** (Ch. 6): `sc_element:terminate/2` calls `sc_store:delete(Pid)` so the key-to-pid mapping is removed no matter how the element terminates.

# Relationships

## Builds Upon
- **Behaviour callback function section** — `terminate/2` is one of its callbacks.

## Related
- **gen-server-code-change** — Another of the lifecycle callbacks.
- **sc-store** — `sc_element:terminate/2` calls into `sc_store` to clean up.

## Contrasts With
- **gen-server-init** — `terminate/2` runs at shutdown; `init/1` runs at startup.

# Common Errors

- **Error**: Forgetting to clean up external resources, expecting state disappearance to handle everything.
  **Correction**: State vanishes automatically, but external mappings (e.g. in ETS) must be removed explicitly in `terminate/2`.

# Common Confusions

- **Confusion**: Thinking `terminate/2` always runs on every shutdown.
  **Clarification**: It runs as part of an orderly `gen_server` shutdown; the book uses it for the cleanup the vanishing state cannot cover.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.4 (Listings 3.1 and 3.5). Chapter 6: Implementing a caching system, Section 6.4.1 (`sc_element:terminate/2`, Listing 6.5).

# Verification Notes

- Definition source: Synthesized from the Chapter 3 callback listings and the Chapter 6 `terminate/2` discussion.
- Confidence rationale: MEDIUM — the book uses and explains `terminate/2` but never gives it a single formal definition.
- Uncertainties: None significant.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
