---
# === CORE IDENTIFICATION ===
concept: Reference
slug: reference

# === CLASSIFICATION ===
category: data-types
subcategory: identifiers
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.2.7 Pids, ports, and references"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - ref
  - "make_ref"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-term
extends:
  - erlang-term
related:
  - pid
  - port-identifier
  - bif
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a reference in Erlang?"
  - "How do you create a reference?"
  - "What are references used for?"
---

# Quick Definition

A reference (or ref) is a unique one-off label, created with `make_ref()`. References are used as unique cookies or tokens.

# Core Definition

"The third data type of this family is *references* (often called *refs*). They're created with the function `make_ref()` and are printed by the shell on the form `#Ref<0.0.0.39>`. References are used as unique one-off labels or cookies" (Chapter 2, section 2.2.7). They belong to the same family of identifier data types as pids and port identifiers.

# Prerequisites

- **Erlang term** — a reference is a kind of term.

# Key Properties

1. A reference is a unique one-off label.
2. It is created by the `make_ref()` function.
3. The shell prints it as `#Ref<0.0.0.39>`.
4. References are used as unique labels or cookies.
5. They are part of the identifier family alongside pids and port identifiers.

# Construction / Recognition

## To Construct/Create:
1. Call `make_ref()` to obtain a fresh, unique reference.
2. Use it as a token to tag and later recognize something.

# Context & Application

- **Typical contexts**: Tagging requests so a reply can be matched to its request.
- **Common applications**: Unique cookies; correlating asynchronous messages.
- **Historical/stylistic notes**: References are heavily used by OTP's call mechanisms to match replies to calls.

# Examples

**Example 1** (section 2.2.7): References are created with `make_ref()` and printed by the shell as `#Ref<0.0.0.39>`.

**Example 2** (section 2.2.7): The book describes references as "unique one-off labels or cookies."

# Relationships

## Builds Upon
- **Erlang term** — a reference is a term.

## Enables
- Unique tagging and correlation of messages or tokens.

## Related
- **Pid** and **port identifier** — references belong to the same identifier family.
- **Built-in function** — `make_ref()` is a BIF.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Reusing the same reference where a fresh unique label is needed.
  **Correction**: Call `make_ref()` each time a new unique label is required.

# Common Confusions

- **Confusion**: Thinking a reference points at a memory location (like a pointer or reference in other languages).
  **Clarification**: An Erlang reference is just a unique opaque label, not a pointer to mutable storage.

# Source Reference

Chapter 2: Erlang language essentials, section 2.2.7 "Pids, ports, and references," "References" subsection.

# Verification Notes

- Definition source: Direct adaptation from section 2.2.7.
- Confidence rationale: HIGH — references and `make_ref()` are explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
