---
# === CORE IDENTIFICATION ===
concept: gen_server code_change/3 Callback
slug: gen-server-code-change

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
extraction_confidence: low

# === VARIANTS (authority control) ===
aliases:
  - "code_change/3"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - behaviour-callback-section
extends:
  - behaviour-callback-section
related:
  - gen-server-terminate
  - gen-server-init
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the gen_server code_change/3 callback?"
  - "Which gen_server callback is involved in hot code upgrades?"
---

# Quick Definition

`code_change/3` is the `gen_server` callback invoked during a hot code upgrade; it lets a server migrate its state from an old version of the code to a new one.

# Core Definition

`code_change/3` is one of the six functions of the `gen_server` behaviour interface (Ch. 3, "Components of a behaviour"; Listing 3.1). It is the hook that supports hot code change: it takes the old version, the current state, and an `Extra` term, and returns `{ok, State}` with the (possibly transformed) state for the new code. The book defers detailed treatment of code change to later chapters; in the minimal `gen_server` module it simply returns `{ok, State}` unchanged.

# Prerequisites

- **gen_server behaviour** — `code_change/3` is a `gen_server` callback.
- **Behaviour callback function section** — `code_change/3` lives in the callback section.

# Key Properties

1. One of the six required `gen_server` interface callbacks.
2. Invoked during a hot code upgrade of the server.
3. Takes `OldVsn`, the current state, and an `Extra` term.
4. Returns `{ok, State}` with the state adapted for the new code.
5. In the minimal implementation it returns `{ok, State}` unchanged.

# Construction / Recognition

## To Write code_change/3:
1. Match `OldVsn`, `State`, and `Extra`.
2. Transform the state to the shape the new code expects.
3. Return `{ok, NewState}` — return `{ok, State}` if no migration is needed.

# Context & Application

`code_change/3` exists so a long-running server can be upgraded in place without losing state. The book introduces it only as a required interface function and covers code change itself elsewhere.

- **Typical contexts**: Hot code upgrades of running OTP systems.
- **Common applications**: Migrating a server's state record when its definition changes between releases.

# Examples

**Example 1** (Ch. 3, Listing 3.1): The minimal `gen_server` module's `code_change(_OldVsn, State, _Extra) -> {ok, State}.` — required by the interface, returning the state unchanged.

**Example 2** (Ch. 3): `tr_server` exports `code_change/3` as one of the six `gen_server` callbacks; the chapter notes the details of code change are returned to later in the book.

# Relationships

## Builds Upon
- **Behaviour callback function section** — `code_change/3` is one of its callbacks.

## Related
- **gen-server-terminate** / **gen-server-init** — The other lifecycle callbacks.

## Contrasts With
- This card has no contrast within the source's treatment.

# Common Errors

- **Error**: Omitting `code_change/3` from the callback module.
  **Correction**: It is one of the six required interface functions; export and define it even if trivially.

# Common Confusions

- **Confusion**: Thinking `code_change/3` runs on every restart.
  **Clarification**: It runs specifically during a hot code upgrade, not on ordinary restarts.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.1.2 (Listing 3.1) and Section 3.2.4. Detailed code-change treatment is deferred to later chapters.

# Verification Notes

- Definition source: Inferred from Listing 3.1 and the brief interface description; the chapter does not define code change in depth.
- Confidence rationale: LOW — the source lists `code_change/3` as a required callback but defers explanation to later chapters.
- Uncertainties: Detailed semantics of `OldVsn`/`Extra` are not covered in these chapters.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
