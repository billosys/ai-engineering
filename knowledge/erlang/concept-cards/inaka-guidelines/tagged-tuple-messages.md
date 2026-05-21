---
concept: Use Atoms Or Tagged Tuples For Messages
slug: tagged-tuple-messages
category: processes-concurrency
subcategory: misc
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Misc"
chapter_number: null
pdf_page: null
section: "Use atoms or tagged tuples for messages"
extraction_confidence: high
aliases:
  - "tagged tuples"
  - "message tagging"
  - "human-readable messages"
prerequisites: []
extends: []
related:
  - avoid-boolean-parameters
  - encapsulate-otp-apis
  - lowercase-atoms
contrasts_with: []
answers_questions:
  - "What is a tagged-tuple message?"
  - "How should I format messages sent between processes?"
---

# Quick Definition

When sending a message between processes, send either a single human-readable atom or a tuple with a human-readable atom in element 1.

# Core Definition

"When sending a message between processes, you should typically either send a single, human-readable atom, or a tuple with a human-readable atom placed in element 1. This includes messages being sent via `gen_server:call` and the like" (Inaka, "Use atoms or tagged tuples for messages"). The leading atom tags the message with its purpose.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A message is a single descriptive atom, or a tuple tagged by a descriptive atom in position 1.
2. The rule covers raw `!` sends and `gen_server:call`/`cast` payloads.
3. Tagging clarifies a message's purpose for readers and debuggers.
4. It is a PR-rejection rule under Misc.

# Construction / Recognition

## To Apply

1. Send `reload_config` (a bare atom) or `{set_count, 123}` (atom-tagged tuple).
2. Place the tag in element 1; data follows.

## To Recognize a Violation

1. A message is a bare number, a bare pid, or a tuple whose first element is not a descriptive atom (`{123, set_count}`, `{make_ref(), notify, ...}`).

# Context & Application

A PR-blocking convention under Misc.

- **Typical contexts**: inter-process messages, `gen_server` call/cast payloads.
- **Common applications**: `gen_server:call(Pid, {set_count, 123})`, `Pid ! {notify, make_ref(), <<"hello world">>}`.

# Examples

**Example 1** — bad: `Pid ! -1`, `gen_server:cast(Pid, self())`, `gen_server:call(Pid, {123, set_count})`.

**Example 2** — good: `gen_server:cast(Pid, reload_config)`, `gen_server:call(Pid, {set_count, 123})`, `gen_server:call(Pid, get_count)`.

# Relationships

## Related

- **Avoid boolean parameters** — both favor human-readable atoms over opaque values.
- **Encapsulate OTP server APIs** — both make message intent traceable.
- **Lowercase atoms** — the tag atoms follow the atom-naming rule.

# Common Errors

- **Error**: Putting the tag in element 2 (`{123, set_count}`).
  **Correction**: Put the descriptive atom in element 1 (`{set_count, 123}`).

# Common Confusions

- **Confusion**: Thinking any tuple is "tagged."
  **Clarification**: The tag must be a *human-readable atom* in *element 1* — a `make_ref()` or integer there does not qualify.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Misc", guideline "Use atoms or tagged tuples for messages".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
