---
concept: When Programming Defensively, Do So On Client Side
slug: client-side-defensive-programming
category: fault-tolerance
subcategory: suggestions
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Suggestions & Great Ideas"
chapter_number: null
pdf_page: null
section: "When programming defensively, do so on client side"
extraction_confidence: high
aliases:
  - "client-side validation"
  - "defensive programming placement"
  - "validate on the outermost layer"
prerequisites: []
extends: []
related:
  - encapsulate-otp-apis
  - tagged-tuple-messages
contrasts_with: []
answers_questions:
  - "Where should input validation happen — client side or server side?"
  - "What distinguishes when defensive validation belongs on the client vs. server side?"
---

# Quick Definition

Do input validation on the outermost (client-side) layers of your code, before calls cross into a server process.

# Core Definition

"Do validations on the outmost layers of your code" (Inaka, "When programming defensively, do so on client side"). When you choose to program defensively, place the checks in the API/client function — typically via a guard on the function head — so a bad argument crashes the caller rather than triggering a round-trip to (and possible crash of) the `gen_server` behind it.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Validation belongs in the outermost layer (the API/client function).
2. A guard on the API function head rejects bad input before the server is contacted.
3. This avoids an unnecessary round-trip and a potential `gen_server` crash.
4. This is a "Suggestion & Great Idea" — advisory, not a PR-blocking rule.

# Construction / Recognition

## To Apply

1. Add a guard to the API function head (`good(X) when is_integer(X) -> ...`).
2. Provide a clause that rejects invalid input (e.g., `throw({invalid_input, X})`).

## To Recognize a Candidate

1. An API function forwards unchecked input straight to `gen_server:call/2`.

# Context & Application

A "Suggestion & Great Idea" — advisory; does not by itself block a PR.

- **Typical contexts**: API functions wrapping a `gen_server`.
- **Common applications**: `good(X) when is_integer(X) -> gen_server:call(?MODULE, {add, X})`.

# Examples

**Example 1** — bad: `bad(X) -> gen_server:call(?MODULE, {add, X})` — no validation; a bad `X` reaches the server.

**Example 2** — good: `good(X) when is_integer(X) -> gen_server:call(?MODULE, {add, X}); good(X) -> throw({invalid_input, X})`.

# Relationships

## Related

- **Encapsulate OTP server APIs** — the API function is the right place for these guards.
- **Use atoms or tagged tuples for messages** — the rejection uses a tagged `{invalid_input, X}`.

# Common Errors

- **Error**: Forwarding unchecked input into a `gen_server`, leaving the server to crash on it.
  **Correction**: Guard the API function so the caller crashes early instead.

# Common Confusions

- **Confusion**: Thinking defensive checks belong deep in the server.
  **Clarification**: Placing them at the client edge avoids the round-trip and contains the crash on the caller side — part of choosing *where* to crash.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Suggestions & Great Ideas", guideline "When programming defensively, do so on client side".

# Verification Notes

- Definition source: Direct quote plus paraphrase of the reasoning.
- Confidence rationale: HIGH — explicit suggestion with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
