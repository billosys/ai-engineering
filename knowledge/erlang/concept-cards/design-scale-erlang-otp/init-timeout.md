---
# === CORE IDENTIFICATION ===
concept: Behavior Init Timeout
slug: init-timeout

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: behavior-startup
tier: intermediate

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Controlling OTP Behaviors"
chapter_number: 4
pdf_page: 133
section: "Timeouts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "{timeout, Timeout}"
  - startup timeout
  - init callback timeout

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spawn-options
extends: []
related:
  - gen-server
contrasts_with:
  - fsm-timeouts

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before implementing a gen_server?"
  - "How does the sys module relate to OTP behaviors?"
---

# Quick Definition

The `{timeout, Timeout}` start option limits how long a behavior may spend in its `init` callback; if `init` is still running after `Timeout` milliseconds the process is terminated and the start function returns `{error, timeout}`.

# Core Definition

The init timeout limits the time a behavior spends in its `init` function. "If you want to limit the time a behavior spends in its init function, include the option `{timeout, Timeout}`. If after `Timeout` milliseconds the init callback function is still executing, the process is terminated and the start function returns `{error, timeout}`" (Cesarini & Vinoski, p. 133). It is useful in very specific circumstances — often a running system with dynamic children responsible for a transient resource. The authors do *not* recommend it for system startup; instead they suggest minimizing the work done in `init` so as not to slow the startup procedure (p. 133).

# Prerequisites

- **Behavior spawn options** — `{timeout, Timeout}` is one of the entries passed in the behavior's `Opts` field.

# Key Properties

1. Passed as `{timeout, Timeout}` in the behavior's `Opts` field, where `Timeout` is milliseconds.
2. If `init` is still executing after `Timeout` ms, the process is terminated.
3. The start function then returns `{error, timeout}`.
4. The `{error, timeout}` result is returned whether or not the starting process is linked to the behavior.
5. Best suited to dynamic children managing transient resources; not recommended for general system startup.

# Construction / Recognition

## To Apply an Init Timeout:
1. Estimate a reasonable upper bound for the `init` callback's runtime.
2. Pass `[{timeout, Timeout}]` (combined with any debug/spawn options) as the behavior's `Opts` argument.
3. Handle the `{error, timeout}` return from the start function.

# Context & Application

- **Typical contexts**: Dynamic children responsible for a transient resource in a running system.
- **Common applications**: Bounding `init` so a slow or hung resource acquisition cannot stall a process indefinitely.
- **Historical/stylistic notes**: The book advises against using it at system startup — keep `init` fast instead (p. 133).

# Examples

**Example 1** (Ch. 5, p. 137): `test_fsm:start_link(1000, [{timeout, 100}])` — `init/1` sleeps 1000 ms but the timeout is 100 ms, so the start returns `{error, timeout}` whether or not the process is linked to the shell.

# Relationships

## Builds Upon
- **Behavior spawn options** — The init timeout is passed through the same `Opts` field.

## Enables
- *(No downstream concepts in this scope.)*

## Related
- **Generic server** — The init timeout governs the `gen_server:init/1` (and other behaviors') callback.

## Contrasts With
- **FSM timeouts** — The init timeout bounds the *startup* callback and is set once; FSM state timeouts fire repeatedly between events in a running FSM.

# Common Errors

- **Error**: Using `{timeout, Timeout}` to paper over a slow `init` at system startup.
  **Correction**: Minimize the work in `init` instead; reserve the option for dynamic children managing transient resources.

# Common Confusions

- **Confusion**: Thinking the init timeout is the same as a `gen_server`/FSM state timeout.
  **Clarification**: The init timeout applies only to the `init` callback at start time; state timeouts apply to a running behavior waiting for its next message or event.

# Source Reference

Chapter 4: Controlling OTP Behaviors, Section "Timeouts," page 133. See also Chapter 5, page 137, for the `test_fsm` startup-timeout example.

# Verification Notes

- Definition source: Direct quote from p. 133.
- Confidence rationale: HIGH — the source explicitly defines the option and its effect, with a corroborating example in Chapter 5.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
