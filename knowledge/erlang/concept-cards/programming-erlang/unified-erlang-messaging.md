---
# === CORE IDENTIFICATION ===
concept: Unified Erlang Messaging
slug: unified-erlang-messaging

# === CLASSIFICATION ===
category: core-idioms
subcategory: message-design
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming Idioms"
chapter_number: 24
pdf_page: null
section: "Maintaining the Erlang View of the World"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - uniform messaging
  - one universal message format

# === TYPED RELATIONSHIPS ===
prerequisites:
  - message-passing
  - middle-man
extends:
  - message-passing
related:
  - multipurpose-server
  - binary
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Erlang processes communicate with each other?"
  - "What is a binary?"
---

# Quick Definition

Unified Erlang messaging is the idiom of using Erlang terms as the single universal message format throughout a system, so no service needs its own ad hoc wire protocol.

# Core Definition

"Once we remove the idea that individual services need to have their different message formats, we can use uniform messaging to solve a range of problems." Erlang terms are used in all messages; a single universal format suffices for client-server requests and responses across many services. This idiom works in a distributed setting because of two BIFs — `term_to_binary(Term)` and its inverse `binary_to_term(Bin)` — which serialize any term to an external representation and reconstruct it exactly ("Maintaining the Erlang View of the World" and "A Multipurpose Server").

# Prerequisites

- **Message-passing** — Unified messaging is a discipline about *what* form messages take.
- **Middle man** — External protocols are normalized into Erlang terms by middle-man processes; without them the unification cannot happen at system boundaries.

# Key Properties

1. It "abstracts out the difference between the different wire protocols" (for example HTTP vs. FTP).
2. Erlang messages require no parser — the receiving process does not parse before processing.
3. Erlang messages can contain terms of arbitrary complexity, unlike flat serialized protocol messages.
4. Erlang messages can cross processor boundaries or be stored in a database in a simple universal serialization format.
5. `binary_to_term/1` reconstructs any term from its external representation; protocols such as HTTP must instead parse input, "which makes the entire process inherently inefficient."

# Construction / Recognition

## To Construct/Create:
1. Choose Erlang terms (tuples, lists, atoms, binaries) as the message format for all internal services.
2. At system boundaries, use middle-man processes to convert external protocols to and from Erlang terms.
3. For network transport or storage, serialize with `term_to_binary/1` and recover with `binary_to_term/1`.
4. Optionally layer compression and encryption via symmetric function pairs around the serialization.

## To Identify/Recognize:
1. All processes exchange Erlang terms; there is no bespoke parsing of message bodies.
2. Network/storage code centers on `term_to_binary`/`binary_to_term`.

# Context & Application

- **Typical contexts**: Multi-protocol servers, distributed systems, and any code that stores or transmits structured data.
- **Common applications**: Sending terms across a network, storing terms in a database, even sending mobile code as `{Mod, Func, Args}` to be `apply`'d remotely.
- **Historical/stylistic notes**: Armstrong: "It's like a world where everybody speaks English (or Mandarin)—it's much easier to communicate."

# Examples

**Example 1** ("A Multipurpose Server"): `send1(Term) -> encrypt(compress(term_to_binary(Term)))` and `receive1(Bin) -> binary_to_term(decompress(decrypt(Bin)))` — a symmetric pair layering compression and encryption over unified term serialization.

**Example 2** ("A Multipurpose Server"): Sending encrypted, compressed mobile code:

```erlang
send_code(Mod, Func, Args) ->
    encrypt(compress(term_to_binary({Mod,Func,Args}))).

receive_code(Bin) ->
    {Mod, Func, Args} = binary_to_term(decompress(decrypt(Bin))),
    apply(Mod, Func, Args).
```

# Relationships

## Builds Upon
- **Message-passing** — Unified messaging fixes the form messages take.

## Enables
- **Multipurpose server** — A single back-end server works because every service speaks one term format.

## Related
- **Binary** — `term_to_binary`/`binary_to_term` move terms in and out of the external binary representation.
- **Middle man** — Translates non-Erlang protocols into the unified term format.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Inventing a separate serialized message format per service.
  **Correction**: Use Erlang terms uniformly; serialize with `term_to_binary` only at transport/storage boundaries.

- **Error**: Hand-parsing message bodies received from another Erlang process.
  **Correction**: Erlang messages need no parser — pattern match on the term directly.

# Common Confusions

- **Confusion**: Thinking `term_to_binary`/`binary_to_term` are like HTTP serialization.
  **Clarification**: They round-trip arbitrary terms exactly with no parsing step, whereas HTTP messages must be flattened and re-parsed.

# Source Reference

Chapter 24: Programming Idioms, Sections "Maintaining the Erlang View of the World" and "A Multipurpose Server."

# Verification Notes

- Definition source: Synthesized from the bulleted advantages list and the `term_to_binary` discussion.
- Confidence rationale: HIGH — the source explicitly enumerates the advantages of uniform Erlang messaging.
- Uncertainties: None.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
