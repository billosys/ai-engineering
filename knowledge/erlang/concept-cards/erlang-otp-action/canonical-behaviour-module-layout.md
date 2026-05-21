---
# === CORE IDENTIFICATION ===
concept: Canonical Behaviour Implementation Module Layout
slug: canonical-behaviour-module-layout

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
section: "3.2.1 Canonical module layout for a behaviour implementation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - module layout
  - "canonical module layout"
  - "behaviour module sections"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - behaviour-callback-module
  - erlang-module
extends: []
related:
  - behaviour-module-header
  - behaviour-api-section
  - behaviour-callback-section
  - process-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the canonical layout of a behaviour implementation module?"
  - "What are the four sections of a behaviour module?"
  - "How should I organize the code in a gen_server module?"
---

# Quick Definition

The canonical behaviour implementation module layout is a standard four-section ordering — Header, API, Behaviour interface, Internal functions — that makes every behaviour module recognizable and easy to read.

# Core Definition

One of the nice things about behaviours is that they give a great amount of consistency. To make behaviour implementation files even more recognizable, the book recommends a canonical layout consisting of four sections, appearing in file order (Ch. 3, Section 3.2.1, Table 3.1):

1. **Header** — module attributes and boilerplate; no exported functions; file-level EDoc.
2. **API** — the programmer interface, how the world interacts with the module; functions exported; function-level EDoc.
3. **Behaviour interface** — the callback functions required by the behaviour interface; functions exported; EDoc optional.
4. **Internal functions** — helper functions for the API and behaviour interface; not exported; EDoc optional.

# Prerequisites

- **Behaviour callback module** — The layout organizes a behaviour callback module.
- **Erlang module** — The sections are arranged within an ordinary module file.

# Key Properties

1. Consists of exactly four sections in a fixed order.
2. Header: attributes/boilerplate, no exports, file-level EDoc.
3. API: programmer interface, exported, function-level EDoc.
4. Behaviour interface: required callbacks, exported, optional EDoc.
5. Internal functions: helpers, not exported, optional EDoc.

# Construction / Recognition

## To Lay Out a Behaviour Module:
1. Start with the Header: file comment block, `-module`, `-behaviour`, `-export`, macros, records.
2. Add the API section with exported wrapper functions and `@doc`/`@spec`.
3. Add the Behaviour interface section with the required callbacks.
4. End with Internal functions used by the API and callbacks.

# Context & Application

The layout pays off when reading unfamiliar code: any behaviour module looks the same, so the reader knows where to find the public surface, the framework callbacks, and the helpers.

- **Typical contexts**: Every `gen_server`, `supervisor`, or `application` callback module the book writes.
- **Common applications**: `tr_server`, `tr_sup`, `tr_app`, `sc_element` all follow this layout.

# Examples

**Example 1** (Ch. 3, Table 3.1): The four sections — Header, API, Behaviour interface, Internal functions — are tabulated with their export and EDoc rules.

**Example 2** (Ch. 3): `tr_server.erl` is built section by section: header (Listing 3.2), API (Listing 3.3), callbacks (Listings 3.4–3.5), internal functions (Listing 3.6).

# Relationships

## Related
- **behaviour-module-header** — The first section.
- **behaviour-api-section** — The second section.
- **behaviour-callback-section** — The third section.
- **process-type** — The "one process type per module" rule complements this layout.

## Contrasts With
- This is an organizational convention; the source draws no direct contrast.

# Common Errors

- **Error**: Scattering API, callbacks, and helpers throughout the file.
  **Correction**: Group them into the four canonical sections in order.

- **Error**: Exporting internal helper functions.
  **Correction**: Internal functions are not exported; only API and behaviour interface functions are.

# Common Confusions

- **Confusion**: Thinking the layout is enforced by the compiler.
  **Clarification**: It is a recommended convention for readability, not a language rule.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.1 "Canonical module layout for a behaviour implementation," Table 3.1.

# Verification Notes

- Definition source: Direct adaptation of Section 3.2.1 and Table 3.1.
- Confidence rationale: HIGH — explicit tabulated definition in the source.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
