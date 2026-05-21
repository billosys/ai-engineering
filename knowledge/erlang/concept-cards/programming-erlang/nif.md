---
# === CORE IDENTIFICATION ===
concept: NIF (Natively Implemented Function)
slug: nif

# === CLASSIFICATION ===
category: tooling
subcategory: interfacing
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Interfacing Techniques"
chapter_number: 15
pdf_page: null
section: "Advanced Interfacing Techniques"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "NIFs"
  - "natively implemented function"
  - "natively implemented functions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - port
extends: []
related:
  - linked-in-driver
  - c-node
contrasts_with:
  - port-program

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a NIF?"
  - "How does a NIF differ from a port program?"
  - "Why are NIFs unsafe?"
---

# Quick Definition

A NIF (natively implemented function) is a function written in C (or another natively compiled language) and linked into the Erlang VM, with direct access to Erlang's internal data structures.

# Core Definition

NIFs are *natively implemented functions* — functions written in C (or some language that compiles to native code) and linked into the Erlang VM (Chapter 15, "Advanced Interfacing Techniques"). NIFs pass arguments directly onto the Erlang processes' stacks and heaps and have direct access to all the Erlang internal data structures. They are among the *unsafe* interfacing techniques: because the foreign code runs inside the Erlang VM, errors in it might crash the Erlang system, but they are more efficient than using an external process. Examples and up-to-date information are kept in an online archive (`git://github.com/erlang/nifs.git`), since the technique evolves faster than Erlang itself.

# Prerequisites

- **Port** — NIFs are presented as an alternative to the port-based interfacing model; understanding ports frames the comparison.

# Key Properties

1. A NIF is a function written in C or another natively compiled language.
2. NIFs are linked into the Erlang VM.
3. NIFs pass arguments directly onto Erlang processes' stacks and heaps.
4. NIFs have direct access to all Erlang internal data structures.
5. They are an *unsafe* technique — a bug can crash the Erlang VM — but more efficient than an external process.

# Construction / Recognition

## To Use a NIF (per the source's overview):
1. Write the function in C (or a native-code language).
2. Link it into the Erlang VM.
3. Consult the online archive for current API and build details.

## To Recognize It:
1. Look for Erlang functions implemented by native code loaded into the VM.
2. Distinguish NIFs (tight VM integration) from port programs (external processes).

# Context & Application

- **Typical contexts**: Performance-critical functions needing direct access to Erlang's internals.
- **Common applications**: The book points to the online NIF archive for examples; it does not develop one in the chapter.
- **Historical/stylistic notes**: The book deliberately keeps NIF details in an online archive because the technique changes more rapidly than the language.

# Examples

**Example 1** (Chapter 15, "Advanced Interfacing Techniques"): The book describes NIFs as functions that "pass arguments directly onto the Erlang processes' stacks and heaps and have direct access to all the Erlang internal data structure."

**Example 2** (Chapter 15): The source does not provide an inline code example for NIFs; it points readers to `git://github.com/erlang/nifs.git`.

# Relationships

## Builds Upon
- The in-VM interfacing model also used by linked-in drivers.

## Enables
- High-performance native functions with direct access to Erlang internals.

## Related
- **Linked-in driver** — another in-VM technique, but obeying the port-driver protocol.
- **C-node** — another advanced interfacing technique.

## Contrasts With
- **Port program** — a port program runs as an isolated external process (safe); a NIF runs inside the VM with direct heap access (unsafe, faster).

# Common Errors

- **Error**: Using a NIF for code that may crash or block, risking the whole VM.
  **Correction**: NIFs run in the VM; reserve them for trusted, well-behaved code, or use a port for risky code.
- **Error**: Relying on the book for current NIF build steps.
  **Correction**: Consult the online archive, since the technique evolves faster than Erlang.

# Common Confusions

- **Confusion**: A NIF is just a port program written in C.
  **Clarification**: A NIF is linked into the VM with direct access to internal data structures; a port program is an isolated external process communicating over a byte stream.
- **Confusion**: NIFs can be written in any language.
  **Clarification**: NIFs require C or another language that compiles to native code, since they link into the VM.

# Source Reference

Chapter 15: Interfacing Techniques, section "Advanced Interfacing Techniques" (the "NIFS" description).

# Verification Notes

- Definition source: Direct adaptation of the "NIFS" description in "Advanced Interfacing Techniques."
- Confidence rationale: HIGH — NIFs are explicitly defined, though the detailed API is deferred to an online archive.
- Uncertainties: No inline code example in the source; card stays at the source's overview level.
- Cross-reference status: Slugs match planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
