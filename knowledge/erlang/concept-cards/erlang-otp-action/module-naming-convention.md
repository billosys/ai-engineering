---
# === CORE IDENTIFICATION ===
concept: Module Naming Convention
slug: module-naming-convention

# === CLASSIFICATION ===
category: core-idioms
subcategory: naming
tier: foundational

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
  - module prefix convention
  - flat namespace

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
extends: []
related:
  - behaviour-module-header
  - otp-application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why do Erlang module names need a prefix?"
  - "What is Erlang's flat module namespace?"
  - "How should I name modules in a project?"
---

# Quick Definition

Erlang has a single flat namespace for modules, so module names can collide. The standard practice is to give every module in a project a short common prefix to avoid clashes.

# Core Definition

Erlang has a flat namespace for modules, which means module names can collide (Ch. 3, "Module naming conventions and the flat namespace" sidebar). An experimental Java-like package system exists but never caught on and is not fully supported. If modules are given generic names like `server`, it is easy to end up with two modules from different projects having the same name. To avoid such clashes, the standard practice is to give module names a suitable prefix. The book derives `tr_server` from the first letters of TCP and RPC, and uses the `sc_` prefix (Simple Cache) for the cache application's modules.

# Prerequisites

- **Erlang module** — The convention governs how modules are named.

# Key Properties

1. Erlang uses a single flat namespace for modules.
2. Module names from different projects can collide.
3. The standard practice is a short common project prefix (e.g. `tr_`, `sc_`).
4. The main user-facing API module is often named after the application itself.
5. The package system is experimental and not fully supported.

# Construction / Recognition

## To Apply the Convention:
1. Choose a short prefix derived from the project or application name.
2. Prefix every module in the project with it (e.g. `tr_app`, `tr_sup`, `tr_server`).
3. Name the main API module after the application itself (e.g. `simple_cache`).

# Context & Application

The convention prevents name clashes in a system that loads many applications into one VM with a shared module table.

- **Typical contexts**: Naming all modules in an OTP application.
- **Common applications**: `tr_*` for the TCP RPC app; `sc_*` plus the `simple_cache` API module for the cache app.

# Examples

**Example 1** (Ch. 3): `tr_server` is named from the first two letters of the acronyms TCP and RPC.

**Example 2** (Ch. 6): The Simple Cache application uses the `sc_` prefix for all modules — `sc_app`, `sc_sup`, `sc_store`, `sc_element` — except the front-end API module, which is named `simple_cache`.

# Relationships

## Related
- **behaviour-module-header** — The `-module` attribute uses the prefixed name.
- **otp-application** — Naming conventions like `_app` and `_sup` build on this prefixing.

## Contrasts With
- This is a naming convention; the source draws no direct contrast.

# Common Errors

- **Error**: Naming a module with a generic word like `server`.
  **Correction**: Add a project prefix to avoid collisions in the flat namespace.

# Common Confusions

- **Confusion**: Expecting Erlang to have a package/namespace system like Java.
  **Clarification**: The experimental package system never caught on; the namespace is flat, so prefixes are the practical solution.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.2 "The module header," "Module naming conventions and the flat namespace" sidebar. See also Chapter 6, Table 6.1 and the "Module naming conventions" sidebar.

# Verification Notes

- Definition source: Direct adaptation of the naming-convention sidebars.
- Confidence rationale: HIGH — explicit in dedicated sidebars in two chapters.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slug `erlang-module` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
