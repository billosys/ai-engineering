---
# === CORE IDENTIFICATION ===
concept: Application-Level API Module
slug: application-api-module

# === CLASSIFICATION ===
category: api-design
subcategory: application-design
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Implementing a caching system"
chapter_number: 6
pdf_page: null
section: "6.4.3 Rounding off with the application-level API module"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - application API module
  - "front-end module"
  - simple_cache module

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - cache-system-design
  - module-naming-convention
extends: []
related:
  - sc-element
  - sc-store
  - server-protocol-hiding
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an application-level API module?"
  - "Why is the cache's API module named simple_cache?"
  - "What does the simple_cache module do?"
---

# Quick Definition

An application-level API module is a single front-end module, conventionally named after the application itself, that provides the interface functions for end users of the application.

# Core Definition

The convention for application-level API modules is to give them the same name as the application (Ch. 6, Section 6.4.3). For the cache, the `simple_cache` module is the API to the `simple_cache` application; it contains the interface functions for end users — `insert/2` (store a key/value pair), `lookup/1` (retrieve a value by key), and `delete/1` (remove a key/value pair). This API does not include functions for starting or stopping the application; that is handled by system functions such as `application:start/1`. The API module ties together the lower-level modules: `insert/2` checks `sc_store` for an existing entry and either replaces the value via `sc_element` or creates a new `sc_element` and inserts the mapping; `lookup/1` resolves the pid via `sc_store` then queries the `sc_element`; `delete/1` resolves the key and delegates to `sc_element:delete/1`.

# Prerequisites

- **OTP application** — The API module is the front end of an application.
- **Process-per-value cache design** — The API module ties together the cache's design.
- **Module naming convention** — The API module is named after the application.

# Key Properties

1. A single front-end module named after the application.
2. Provides the end-user interface functions.
3. Does not include start/stop functions — that is the system's job.
4. Ties together the application's lower-level modules.
5. Hides the lower-level modules and storage details from users.
6. Common pattern: one module acting as a front end with the application's name.

# Construction / Recognition

## To Write an Application API Module:
1. Name the module after the application (e.g. `simple_cache`).
2. Export only the end-user interface functions.
3. Implement each by delegating to the lower-level modules (`sc_store`, `sc_element`).
4. Do not expose start/stop or internal modules.

# Context & Application

The API module is the application's public face — users interact solely through it, oblivious to the supervisor, storage processes, and ETS backing.

- **Typical contexts**: The single public entry point of an OTP application.
- **Common applications**: `simple_cache` is the user API of the `simple_cache` application.

# Examples

**Example 1** (Ch. 6, Listing 6.7): `simple_cache:insert/2` calls `sc_store:lookup/1`; on a hit it uses `sc_element:replace/2`, on a miss it creates a new `sc_element` and inserts a mapping in `sc_store`.

**Example 2** (Ch. 6): `simple_cache:lookup/1` uses a `try` expression — it resolves the pid via `sc_store`, queries the `sc_element`, and returns `{error, not_found}` if any step fails.

# Relationships

## Related
- **sc-element** — The API module delegates value operations to `sc_element`.
- **sc-store** — The API module uses `sc_store` to resolve keys to pids.
- **server-protocol-hiding** — The API module hides the lower-level modules and protocols from users.

## Contrasts With
- This card has no direct contrast within the source's treatment.

# Common Errors

- **Error**: Putting application start/stop functions in the API module.
  **Correction**: Starting and stopping is handled by system functions such as `application:start/1`, not the API module.

# Common Confusions

- **Confusion**: Thinking the API module must implement a behaviour.
  **Clarification**: It is a plain front-end module; the behaviours live in `_app`, `_sup`, and the worker modules.

# Source Reference

Chapter 6: Implementing a caching system, Section 6.4.3 "Rounding off with the application-level API module," Listing 6.7.

# Verification Notes

- Definition source: Direct adaptation of Section 6.4.3.
- Confidence rationale: HIGH — explicit, worked treatment.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
