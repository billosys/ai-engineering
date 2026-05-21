---
# === CORE IDENTIFICATION ===
concept: Checking Data at the Borders
slug: check-the-borders

# === CLASSIFICATION ===
category: error-handling
subcategory: design-principles
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Writing a TCP-based RPC service"
chapter_number: 3
pdf_page: null
section: "3.2.4 The callback function section"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "check the borders"
  - "border checking"
  - "let it crash"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - supervisor
  - sc-store
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does checking data at the borders mean in Erlang?"
  - "Why don't Erlang programs check data repeatedly?"
  - "How does border checking relate to let-it-crash?"
---

# Quick Definition

Checking data at the borders is the Erlang design principle of validating data as it crosses from the untrusted outside world into trusted code — and not re-checking it afterward.

# Core Definition

Checking data as it passes from the untrusted world into the trusted inner sanctum of your code is a fundamental design principle of Erlang programs (Ch. 3, "Check the borders" sidebar). After you verify that data conforms to your expectations, there is no need to check it repeatedly: you can code for the correct case and let supervision take care of the rest. The reduction in code size and in programming errors (through improved readability) can be significant. Any remaining errors, because they are not masked, show up as process restarts in the logs, which lets you correct problems as they occur — "let it crash."

# Prerequisites

- **Process** — The principle relies on processes crashing and being restarted by supervision.

# Key Properties

1. Validate data once, at the boundary between untrusted and trusted code.
2. Do not re-check data after it has been validated.
3. Internal code can assume the correct case.
4. Reduces code size and the number of programming errors.
5. Unmasked errors surface as process restarts in the logs.

# Construction / Recognition

## To Apply Border Checking:
1. Identify where untrusted data enters your system (sockets, user input, etc.).
2. Validate it there — fail fast if it does not conform.
3. Write internal code for the correct case only, without defensive re-checks.
4. Let supervision restart any process that crashes on bad data.

# Context & Application

The principle works hand in hand with let-it-crash and supervision: clean internal code plus boundary checks plus restarts.

- **Typical contexts**: Parsing external input; internal library functions that trust their callers.
- **Common applications**: `tr_server`'s `do_rpc/2` wraps untrusted parsing in a `try`; `sc_store`'s `insert/2` does no type checking because it trusts its callers (internal code).

# Examples

**Example 1** (Ch. 3): `do_rpc/2` wraps the parsing of outside-world data in a `try` expression so a crash prints an error and continues rather than killing the server.

**Example 2** (Ch. 6): `sc_store:insert/2` deliberately does no type checking — it is internal code that trusts its callers; sanity is checked at the borders, not afterward.

# Relationships

## Related
- **supervisor** — Supervision catches and restarts processes that crash on unchecked errors.
- **sc-store** — `sc_store` exemplifies trusting internal callers and not re-checking.

## Contrasts With
- This is a design principle; the source draws no direct contrast.

# Common Errors

- **Error**: Defensively re-validating the same data at every internal layer.
  **Correction**: Check once at the border; let internal code assume correctness.

# Common Confusions

- **Confusion**: Thinking "let it crash" means never checking anything.
  **Clarification**: It means check at the borders, then let unmasked internal errors crash the process so supervision can act.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.4, "Check the borders" sidebar. See also Chapter 6, Section 6.4.2 ("Creating and updating entries").

# Verification Notes

- Definition source: Direct adaptation of the "Check the borders" sidebar.
- Confidence rationale: HIGH — explicit definition in a dedicated sidebar.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slug `process` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
