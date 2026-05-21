---
# === CORE IDENTIFICATION ===
concept: sc_element Storage Process
slug: sc-element

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-design
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Implementing a caching system"
chapter_number: 6
pdf_page: null
section: "6.4.1 Coding the sc_element processes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - sc_element
  - "storage element"
  - "cache element process"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - simple-one-for-one
  - cache-system-design
extends:
  - gen-server
related:
  - sc-store
  - application-api-module
  - gen-server-timeout
  - supervisor-start-child
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an sc_element process?"
  - "How does the cache store an individual value?"
  - "How does sc_element handle lease expiry?"
---

# Quick Definition

An `sc_element` is a `gen_server` process that holds a single cached value. One such process is spawned per key/value pair, and it self-terminates when its lease expires.

# Core Definition

`sc_element` is the module holding the code for the child processes of `sc_sup`; a new `sc_element` process is spawned each time new data is entered into the cache, to hold the data associated with a particular key (Ch. 6, Section 6.4.1). The processes are based on the `gen_server` behaviour and keep the data in the `gen_server` state. The module defines a `DEFAULT_LEASE_TIME` macro and a state record with three fields: the stored value, the lease time, and a start timestamp. `sc_element` has four API operations — `create` (with a `create/1` short form for the default lease), `fetch`, `replace`, and `delete` — plus `start_link/2`. `create/2` hides the delegation to `sc_sup:start_child/2`; `fetch` uses a synchronous `call`, while `replace` and `delete` use asynchronous `cast`. The `init/1` callback records the start time in Gregorian seconds and sets a server timeout for lease management; if the process is not accessed within the lease period, a `timeout` message reaches `handle_info/2`, which shuts the process down. `terminate/2` calls `sc_store:delete(Pid)` to remove the key mapping.

# Prerequisites

- **gen_server behaviour** — Each `sc_element` is a `gen_server`.
- **simple_one_for_one supervision** — `sc_element` processes are children of the `sc_sup` `simple_one_for_one` supervisor.
- **Process-per-value cache design** — `sc_element` realizes the per-value-process idea.

# Key Properties

1. A `gen_server` process holding one cached value in its state.
2. One process is spawned per key/value pair.
3. State record has three fields: value, lease time, start timestamp.
4. API operations: `create`/`create/1`, `fetch`, `replace`, `delete`, plus `start_link/2`.
5. `fetch` uses synchronous `call`; `replace` and `delete` use asynchronous `cast`.
6. Uses a server timeout for lease expiry; on timeout it self-terminates.
7. `terminate/2` calls `sc_store:delete(Pid)` to clean up the key mapping.

# Construction / Recognition

## To Implement sc_element:
1. Write a `gen_server` module with a `DEFAULT_LEASE_TIME` macro and a state record.
2. Provide `create/2` (and `create/1`) that delegate to `sc_sup:start_child/2`.
3. Provide `start_link/2` that calls `gen_server:start_link/3` without registering a name.
4. Implement `fetch` via `call`, `replace` and `delete` via `cast`.
5. In `init/1`, record the start time and set the lease timeout.
6. In `handle_info/2`, shut down on the lease `timeout`; in `terminate/2`, call `sc_store:delete/1`.

# Context & Application

`sc_element` is the cache's value-storage layer; making each value its own process makes lease management trivial.

- **Typical contexts**: The per-value worker processes of the Simple Cache.
- **Common applications**: Storing one cached package listing per URL key.

# Examples

**Example 1** (Ch. 6, Listing 6.5): `sc_element:handle_cast/2` returns `noreply` for `{replace, Value}` (stays alive with new state) and `stop` with reason `normal` for `delete` (terminates).

**Example 2** (Ch. 6, Figure 6.7): `sc_element:create/2` → `sc_sup:start_child/2` → `supervisor:start_child/2` → `sc_element:start_link/2` → `gen_server:start_link/3` — the full call flow when a new element is added.

# Relationships

## Builds Upon
- **gen_server behaviour** — `sc_element` is a `gen_server`.

## Related
- **sc-store** — `sc_element:terminate/2` calls `sc_store:delete/1`.
- **application-api-module** — `simple_cache` calls `sc_element` to create, replace, and delete values.
- **gen-server-timeout** — Lease expiry uses the server timeout mechanism.

## Contrasts With
- This card has no direct contrast within the source's treatment.

# Common Errors

- **Error**: Calling `sc_element:start_link/2` directly to create a cache element.
  **Correction**: Use `sc_element:create/2`, which delegates to the supervisor so the process is supervised.

- **Error**: Forgetting to re-set the server timeout in a callback clause.
  **Correction**: Set the timeout in every callback clause, or it reverts to `infinity` and the lease never expires.

# Common Confusions

- **Confusion**: Thinking `sc_element` processes are registered by name.
  **Clarification**: They are not — there can be many of them; callers must hold their pids.

# Source Reference

Chapter 6: Implementing a caching system, Section 6.4.1 "Coding the sc_element processes," Listings 6.3–6.5 and Figure 6.7.

# Verification Notes

- Definition source: Direct adaptation of Section 6.4.1.
- Confidence rationale: HIGH — explicit, worked treatment.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
