---
# === CORE IDENTIFICATION ===
concept: Behaviour Module Header
slug: behaviour-module-header

# === CLASSIFICATION ===
category: core-idioms
subcategory: module-layout
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Writing a TCP-based RPC service"
chapter_number: 3
pdf_page: null
section: "3.2.2 The module header"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - module header
  - file header

# === TYPED RELATIONSHIPS ===
prerequisites:
  - canonical-behaviour-module-layout
extends:
  - canonical-behaviour-module-layout
related:
  - edoc
  - behaviour-callback-module
  - module-naming-convention
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What goes in a behaviour module header?"
  - "What is in the file-level comment block of an Erlang module?"
  - "How do you declare that a module implements a behaviour?"
---

# Quick Definition

The behaviour module header is the first section of a behaviour implementation module: the file-level comment block plus module attributes — `-module`, `-behaviour`, `-export` declarations — and any macros and records.

# Core Definition

The module header is the first of the four canonical sections of a behaviour implementation module (Ch. 3, Section 3.2.2). It begins with a file-level header comment block whose lines start with three `%` characters (the convention for file-level comments) and which carries EDoc annotations such as `@author`, `@copyright`, `@doc`, and `@end`. The first non-comment item is the `-module(...)` attribute, whose name must match the file name. Next comes the `-behaviour(...)` attribute, which tells the compiler the module implements a particular behaviour so it can warn about missing or unexported interface functions. Then come the `-export` declarations — typically two, one for API functions and one for behaviour callbacks. The header ends with optional application-specific declarations: macros (for constants such as default port and a `SERVER` alias) and record definitions for the process state.

# Prerequisites

- **Canonical behaviour module layout** — The header is the first section of that layout.

# Key Properties

1. Starts with a `%%%` file-level comment block carrying EDoc tags.
2. Contains `-module(Name)`, with `Name` matching the file name.
3. Contains a `-behaviour(...)` attribute so the compiler can check callback exports.
4. Has (usually two) `-export` declarations — API functions and behaviour callbacks.
5. Ends with optional macros and record definitions for process state.

# Construction / Recognition

## To Write a Header:
1. Add the `%%%` file comment block with `@author`, `@copyright`, `@doc`, `@end`.
2. Add `-module(name)` matching the file name.
3. Add `-behaviour(behaviour_name)`.
4. Add an `-export` for API functions and one for behaviour callbacks.
5. Define macros (constants, `SERVER` alias) and the state `-record`.

# Context & Application

The header establishes identity, behaviour conformance, the public surface, and the shape of process state — everything a reader needs before reading the code.

- **Typical contexts**: The top of any `gen_server`/`supervisor`/`application` callback module.
- **Common applications**: The `tr_server.erl` header defines a default-port macro, a `SERVER` macro aliasing `?MODULE`, and a `#state{}` record.

# Examples

**Example 1** (Ch. 3, Section 3.2.2): The `tr_server` file-level comment block uses `@author`, `@copyright`, `@doc`, and `@end`.

**Example 2** (Ch. 3, Listing 3.2): The full `tr_server.erl` header — `-module(tr_server)`, `-behaviour(gen_server)`, two `-export` lists, macros, and a `#state{}` record.

# Relationships

## Builds Upon
- **Canonical behaviour module layout** — The header is its first section.

## Related
- **edoc** — The header comment block carries EDoc tags.
- **behaviour-callback-module** — The header declares the behaviour the module implements.
- **module-naming-convention** — The `-module` name follows naming conventions.

## Contrasts With
- This is a structural section; the source draws no direct contrast.

# Common Errors

- **Error**: Giving `-module` a name that differs from the file name.
  **Correction**: The module name must correspond to the file name.

- **Error**: Forgetting that attributes and definitions must end with a period.
  **Correction**: All attributes and function definitions end with `.`.

# Common Confusions

- **Confusion**: Thinking `%%%` is required for file-level comments.
  **Clarification**: A single `%` is sufficient; `%%%` is a readability convention for file-level commentary.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.2 "The module header." See Listing 3.2 and Table 3.2 (basic EDoc tags), and the "Module naming conventions and the flat namespace" sidebar.

# Verification Notes

- Definition source: Direct adaptation of Section 3.2.2.
- Confidence rationale: HIGH — explicit, detailed treatment in the source.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
