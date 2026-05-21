---
# === CORE IDENTIFICATION ===
concept: Atom Table and Atom Performance
slug: atom-performance

# === CLASSIFICATION ===
category: performance
subcategory: memory
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Optimization and performance"
chapter_number: 14
pdf_page: null
section: "14.3.1. Atoms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "atom table"
  - "atom"
  - "list_to_existing_atom"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - data-type-sizes
extends: []
related:
  - small-integer-performance
  - bif-performance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are atoms stored and why are they efficient?"
  - "Why can creating atoms dynamically be a memory leak?"
  - "When should you use list_to_existing_atom/1?"
---

# Quick Definition

An atom occupies one word holding an index into a per-node atom table; atoms are fast but are never garbage collected, so creating them dynamically from untrusted data can crash the node.

# Core Definition

Atoms are similar to small integers: each occurrence uses only one word of memory, holding an index into an atom table where the actual name string is stored. The name uses a little memory but is stored only once per Erlang node. Comparing two atoms for equality is therefore as fast as comparing two small integers, which makes atoms efficient as labels in tagged tuples. Atoms are added to the table when a module containing them is loaded, when a node receives a message containing a new atom, or when `list_to_atom/1` is called. Crucially, atoms are not garbage collected: the only way to clear the table is to restart the node. The table has a limited size (currently just over a million entries); overflowing it crashes the VM with a "system limit" error (Chapter 14, Section 14.3.1).

# Prerequisites

- **Memory sizes of Erlang data types** — Atoms are the 1-word entry in Table 14.1.

# Key Properties

1. Each atom occurrence is one word: an index into the atom table.
2. The name string is stored once per node, not per occurrence.
3. Atom equality comparison is as fast as small-integer comparison.
4. Atoms are added to the table on module load, on inbound messages with new atoms, or via `list_to_atom/1`.
5. Atoms are never garbage collected; only a node restart clears the table.
6. The atom table is limited to just over a million entries; overflow crashes the VM with a "system limit" error.
7. `list_to_existing_atom/1` converts a string only to an already-known atom, throwing an exception otherwise.

# Construction / Recognition

## To Construct/Create (safely):
1. Use atoms freely for static, known sets of identifiers.
2. Never create arbitrary atoms from untrusted input.
3. When converting strings that might match atoms, use `list_to_existing_atom/1` rather than `list_to_atom/1`.

# Context & Application

- **Typical contexts**: Labels in tagged tuples, status codes, configuration keys.
- **Common applications**: The book warns that a server converting inbound strings to atoms is open to a denial-of-service attack by flooding it with unique strings.
- **Historical/stylistic notes**: A novice habit of generating atoms like `x1`, `x2`, ... can silently leak until the table overflows.

# Examples

**Example 1** (Section 14.3.1 sidebar): Generating atoms on the fly (`x1`...`x187634`) works for short-lived programs but overflows the table in a long-running production system.

**Example 2** (Section 14.3.1): A server transforming incoming strings into atoms can be brought down by an attacker sending many unique strings.

# Relationships

## Related
- **Small integers and tagged representation** — Atoms share the one-word immediate representation and fast comparison.
- **BIF and operator performance** — `list_to_atom/1` is a BIF whose atom-table cost must be considered.

# Common Errors

- **Error**: Calling `list_to_atom/1` on untrusted external strings.
  **Correction**: Use `list_to_existing_atom/1`, or keep the data as strings or binaries.

# Common Confusions

- **Confusion**: Thinking unused atoms are eventually reclaimed.
  **Clarification**: Atoms are never garbage collected; the table is only cleared by restarting the node.

# Source Reference

Chapter 14: Optimization and performance, Section 14.3.1 "Atoms," including the "Creating atoms dynamically can be a memory leak" sidebar.

# Verification Notes

- Definition source: Direct adaptation of Section 14.3.1.
- Confidence rationale: HIGH — atom storage and the leak hazard are explicit.
- Uncertainties: The "just over a million" table-size figure is implementation-era-specific.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
