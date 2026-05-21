---
# === CORE IDENTIFICATION ===
concept: sc_hbase Request/Reply Protocol
slug: sc-hbase-protocol

# === CLASSIFICATION ===
category: distribution
subcategory: foreign-integration
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Communication between Erlang and Java via Jinterface"
chapter_number: 13
pdf_page: null
section: "13.3.1. The Erlang side: sc_hbase.erl"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "sc_hbase protocol"
  - "Erlang-HBase message protocol"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-hbase-bridge
  - message-passing
extends: []
related:
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What message protocol does the Erlang-HBase bridge use?"
  - "Why does sc_hbase use make_ref/0 in its requests?"
  - "Why are keys and values converted with term_to_binary on the Erlang side?"
---

# Quick Definition

The `sc_hbase` module defines a tagged tuple protocol — request tuples with an action tag, sender pid, unique reference, key, and optional value; reply tuples matched by that reference — for talking to the HBase Java node.

# Core Definition

The Erlang HBase API is a single module, `sc_hbase`, in the `simple_cache` application, exposing `put`, `get`, and `delete`. These functions are wrappers around a simple message-based protocol, much like a `gen_server` interface. Each request is a tuple containing a request tag (`put`, `get`, or `delete`), the sender's pid, a reference created with `make_ref()` to uniquely identify the request, the database key, and optionally a value (for `put`). The reference ensures the matching `receive` only accepts the reply to that specific request, so no stray messages can confuse it. Keys and values are converted to binaries with `term_to_binary/1`, making the Java side oblivious to the stored data. Each request has an `after` timeout (Chapter 13, Section 13.3.1).

# Prerequisites

- **Erlang-HBase bridge** — This protocol is the contract between the bridge's two sides.
- **Message passing** — Requests and replies are ordinary Erlang messages.

# Key Properties

1. Request tuples: `{Tag, SenderPid, Ref, Key}` for `get`/`delete`, `{Tag, SenderPid, Ref, Key, Value}` for `put`.
2. Reply tuples are matched against the `Ref` so only the intended reply is accepted.
3. `Ref` is produced by `make_ref/0`, guaranteeing uniqueness.
4. Keys and values are run through `term_to_binary/1` before sending.
5. Every API function takes the Java node name as its first argument.
6. The Java mailbox is hardcoded as `hbase_server`; each call has an `after 3000 -> {error, timeout}` clause.
7. `get` converts the returned binary back with `binary_to_term`; `not_found` yields `{error, not_found}`; `delete` always returns `ok`.

# Construction / Recognition

## To Construct/Create:
1. In the API function, create a fresh reference: `Ref = make_ref()`.
2. Send the request: `{hbase_server, Node} ! {Tag, self(), Ref, term_to_binary(Key) [, term_to_binary(Value)]}`.
3. `receive` only `{reply, Ref, Result}` — the bound `Ref` filters out other messages.
4. Add an `after Timeout -> {error, timeout}` clause.

# Context & Application

- **Typical contexts**: Any request/reply protocol over distribution where stray messages must be excluded.
- **Common applications**: `sc_hbase:put/3`, `get`, and `delete` use this protocol against the HBase Java node.
- **Historical/stylistic notes**: The book notes the mailbox name `hbase_server` is hardcoded as a known entry point, though multiple HBase nodes could each have a distinct name.

# Examples

**Example 1** (Section 13.3.1): `delete/2` runs `Ref = make_ref()`, sends `{delete, self(), Ref, term_to_binary(Key)}`, then `receive {reply, Ref, ok} -> ok after 3000 -> {error, timeout} end`.

**Example 2** (Section 13.3.1): `get` takes the binary value from the reply and runs it back through `binary_to_term`, returning `{error, not_found}` if the reply is `not_found`.

# Relationships

## Related
- **term_to_binary/1** — Used to serialize keys and values for the byte-oriented Java/HBase side.
- **Selective receive** — The bound `Ref` makes the `receive` accept only the matching reply.

# Common Errors

- **Error**: Reusing a reference or omitting it, so a `receive` accepts an unrelated reply.
  **Correction**: Generate a fresh `make_ref()` per request and bind it in the `receive` pattern.

- **Error**: Forgetting the `after` timeout, so a missing Java reply blocks forever.
  **Correction**: Always include an `after Timeout -> {error, timeout}` clause.

# Common Confusions

- **Confusion**: Thinking the Java side must understand the Erlang term structure of keys and values.
  **Clarification**: `term_to_binary/1` turns them into opaque binaries; HBase and the Java code only see bytes.

# Source Reference

Chapter 13: Communication between Erlang and Java via Jinterface, Section 13.3.1 "The Erlang side: sc_hbase.erl."

# Verification Notes

- Definition source: Direct adaptation of Section 13.3.1 and the `delete/2` listing.
- Confidence rationale: HIGH — the protocol and rationale are explicitly described.
- Uncertainties: None.
- Cross-reference status: References Agent 1- and Agent 4-owned slugs by name per instructions.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
