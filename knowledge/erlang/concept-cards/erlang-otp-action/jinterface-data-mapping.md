---
# === CORE IDENTIFICATION ===
concept: Mapping Erlang Data Structures onto Java
slug: jinterface-data-mapping

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
section: "13.1.3. Mapping Erlang data structures onto Java"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "OtpErlangObject"
  - "Jinterface type-mapping classes"
  - "Erlang-to-Java data marshalling"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - jinterface
extends: []
related:
  - otp-mbox
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are Erlang data types represented in Java with Jinterface?"
  - "How do you build an Erlang tuple in Java?"
  - "How do you convert a received Erlang term into native Java data?"
---

# Quick Definition

Jinterface provides a family of `OtpErlang*` Java classes, all subclasses of `OtpErlangObject`, that directly mirror the Erlang data types so terms can be passed as messages between Java and Erlang.

# Core Definition

All data passed as messages between nodes must be represented using the type-mapping classes Jinterface provides. These classes are a direct representation of the Erlang data types in Java, and all are subclasses of `OtpErlangObject`. Each Erlang type maps to one or more Java classes — for example atoms to `OtpErlangAtom`/`OtpErlangBoolean`, integers to `OtpErlangInt`/`OtpErlangLong`/`OtpErlangShort` and others, lists to `OtpErlangList`/`OtpErlangString`, tuples to `OtpErlangTuple`, and the catch-all term type to `OtpErlangObject`. Compound objects like tuples and lists must be built up incrementally from individually mapped objects (Chapter 13, Section 13.1.3, Table 13.1).

# Prerequisites

- **Jinterface** — These classes are provided by the Jinterface library.
- **Erlang data types** — The classes mirror Erlang's atoms, integers, floats, binaries, lists, tuples, pids, ports, references, and funs.

# Key Properties

1. Every type-mapping class is a subclass of `OtpErlangObject`.
2. The mapping is direct: one Erlang type ↔ one or several Java classes (Table 13.1).
3. Compound values (`OtpErlangTuple`, `OtpErlangList`) are constructed from arrays of already-mapped `OtpErlangObject` elements.
4. Receiving yields an `OtpErlangObject`, which is typically cast to the expected concrete subclass.
5. Accessor methods extract native Java values, e.g. `atomValue()`, `stringValue()`, `intValue()`, `elementAt(i)`.
6. Several Java classes exist per Erlang integer type because Java distinguishes int/long/short/char/byte.

# Construction / Recognition

## To Construct/Create (Erlang term in Java):
1. Build leaf objects: `new OtpErlangAtom("some_atom")`, `new OtpErlangString("Some string")`, `new OtpErlangInt(22)`.
2. Combine into a tuple: `new OtpErlangTuple(new OtpErlangObject[]{anAtom, aString, anInt})`.
3. Send it via a mailbox.

## To Identify/Recognize (Java data from an Erlang term):
1. Receive the message as an `OtpErlangObject`.
2. Cast to the expected type, e.g. `(OtpErlangTuple) msg`.
3. Pull elements with `t.elementAt(i)` and cast each, then call its value accessor.

# Context & Application

- **Typical contexts**: Every message crossing the Erlang/Java boundary in a Jinterface program.
- **Common applications**: The HBase bridge marshals `OtpErlangBinary` keys/values and `OtpErlangAtom` reply tags.
- **Historical/stylistic notes**: The book notes the Java side is more verbose than Erlang because there is no pattern matching to deconstruct terms.

# Examples

**Example 1** (Section 13.1.3): The Erlang term `{some_atom, "Some string", 22}` is built in Java from an `OtpErlangAtom`, an `OtpErlangString`, and an `OtpErlangInt` combined into an `OtpErlangTuple`.

**Example 2** (Section 13.1.3): A received tuple is decoded as `String theAtom = ((OtpErlangAtom) t.elementAt(0)).atomValue();` and similar casts for the other elements.

# Relationships

## Related
- **OtpMbox** — Mailboxes send and receive these `OtpErlangObject` values.
- **term_to_binary/1** — In the HBase bridge, Erlang keys and values are turned into binaries, mapped to `OtpErlangBinary`.

# Common Errors

- **Error**: Casting a received `OtpErlangObject` to the wrong concrete subclass.
  **Correction**: Know the expected message structure, or inspect the object's runtime type before casting.

- **Error**: Trying to mutate a compound object after construction.
  **Correction**: Build compound objects fully from their element arrays at construction time.

# Common Confusions

- **Confusion**: Expecting a single Java class per Erlang type.
  **Clarification**: Some Erlang types map to several Java classes (e.g. integers, atoms), reflecting Java's finer-grained numeric and boolean types.

# Source Reference

Chapter 13: Communication between Erlang and Java via Jinterface, Section 13.1.3 "Mapping Erlang data structures onto Java," Table 13.1.

# Verification Notes

- Definition source: Direct adaptation of Section 13.1.3 and Table 13.1.
- Confidence rationale: HIGH — the mapping is explicitly tabulated and demonstrated.
- Uncertainties: None.
- Cross-reference status: References Agent 1- and Agent 4-owned slugs by name per instructions.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
