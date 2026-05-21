---
# === CORE IDENTIFICATION ===
concept: SAX-Style Callback Parsing
slug: sax-style-parsing

# === CLASSIFICATION ===
category: tooling
subcategory: interoperability
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Integrating with foreign code using ports and NIFs"
chapter_number: 12
pdf_page: null
section: "12.2.2. The C side of the port"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - SAX callbacks
  - YAJL callbacks
  - event-based parsing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - foreign-code-integration
extends: []
related:
  - json-erlang-representation
  - erl-interface
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is SAX-style parsing?"
  - "How does the YAJL parser invoke callbacks?"
  - "Why is SAX-style parsing useful when building Erlang terms?"
---

# Quick Definition

SAX-style parsing is an event-based approach where the parser invokes a callback for each piece of input it recognizes, letting the program build a result incrementally without an intermediate document tree.

# Core Definition

The YAJL JSON parser is based on SAX-style callbacks: as the parser scans the input, it invokes a callback function for each thing it recognizes — simple values like null, booleans, numbers, and strings each have a single callback, while compound structures (arrays and maps) have one callback for the start and another for the end. This is useful because it allows building the resulting Erlang terms directly, without going via an intermediate format. Each callback is handed a *context* pointer (the parser state), similar to the way `gen_server` callbacks receive the current state ("Erlang and OTP in Action," Ch. 12, chapter introduction and Section 12.2.2).

# Prerequisites

- **Foreign code integration mechanisms** — The SAX callbacks are part of integrating a C parsing library.

# Key Properties

1. Event-based: the parser calls back into your code as it recognizes input.
2. Simple JSON values (null, true/false, numbers, strings) each have a single callback.
3. Compound structures (arrays, maps) have a start callback and an end callback.
4. Maps have a special callback only for the key; the value uses the normal value callbacks.
5. Each callback receives a *context* pointer holding the parser state.
6. No intermediate document tree is built — the result is constructed incrementally.
7. Callbacks return 1 to YAJL to signal "all OK, continue parsing."

# Construction / Recognition

## To Construct/Create:
1. Implement a callback for each simple value type and start/end callbacks for arrays and maps.
2. Fill a callback structure (e.g., `yajl_callbacks`) with pointers to your functions.
3. Pass a context (state) pointer to the parser so each callback can access shared state.
4. Have callbacks build the result term incrementally and return 1 to continue.

## To Identify/Recognize:
1. A parser configured with a structure of callback function pointers, invoked per recognized token.

# Context & Application

- **Typical contexts**: Integrating a streaming/event-based parser library.
- **Common applications**: The YAJL JSON parser's callbacks build Erlang terms directly as JSON is scanned.
- **Historical/stylistic notes**: Because no intermediate format is needed, SAX-style parsing pays off for large documents.

# Examples

**Example 1** (Section 12.2.2): Simple callbacks like `handle_string` use `ei_x_encode_binary` to build a binary term; container callbacks `handle_start`/`handle_end` manage array/map encoding.

**Example 2** (Section 12.2.2 sidebar): In YAJL only the key of a key/value pair has a special callback; the value is handled by the normal value callbacks.

# Relationships

## Builds Upon
- **Foreign code integration mechanisms** — SAX callbacks are part of a C library integration.

## Related
- **JSON-to-Erlang term representation** — The callbacks build that representation.
- **Erl_Interface (ei) library** — In the port/driver versions the callbacks encode terms with `ei`.

# Common Errors

- **Error**: Counting a map key as a separate element.
  **Correction**: Increment the element count only for values, not keys — the count rises once per key/value tuple.

# Common Confusions

- **Confusion**: Thinking the parser hands you a complete document tree.
  **Clarification**: SAX-style parsing is event-based — you receive a stream of callbacks and build the result yourself.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," chapter introduction and Section 12.2.2, subsection "Encoding JSON data as Erlang terms."

# Verification Notes

- Definition source: Synthesized from the chapter introduction and Section 12.2.2; the book describes SAX-style callbacks in the context of YAJL rather than defining the term formally.
- Confidence rationale: MEDIUM — the concept is described through the YAJL example rather than given a standalone definition.
- Uncertainties: "SAX-style" is mentioned briefly; the broader SAX (XML) origin is not elaborated by the book.
- Cross-reference status: `foreign-code-integration` owned by this agent.
- Re-extraction notes: Fresh extraction; no prior card existed.
