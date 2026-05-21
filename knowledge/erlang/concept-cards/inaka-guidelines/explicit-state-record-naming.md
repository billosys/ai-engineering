---
concept: Explicit State Should Be Explicitly Named
slug: explicit-state-record-naming
category: otp-behaviours
subcategory: naming
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Naming"
chapter_number: null
pdf_page: null
section: "Explicit state should be explicitly named"
extraction_confidence: high
aliases:
  - "mod_state record"
  - "state record naming"
  - "state() type"
prerequisites:
  - lowercase-record-names
extends: []
related:
  - encapsulate-otp-apis
  - avoid-records-in-specs
  - use-behaviours
contrasts_with: []
answers_questions:
  - "What is the module-state record convention (#mod_state / -type state())?"
  - "How do I name and type the state record in an OTP behaviour module?"
---

# Quick Definition

Name the state record of an OTP behaviour module `#mod_state{}` (module-prefixed) and define `-type state() :: #mod_state{}` for it in every such module.

# Core Definition

"Name your state records `#mod_state` and use `-type state():: #mod_state{}` in all your modules that implement OTP behaviors" (Inaka, "Explicit state should be explicitly named"). The state record carries a module-prefixed name, and a `state()` type aliases it so the state has a recognizable, dialyzer-checkable identity.

# Prerequisites

- **Record names** — the state record must still obey the lowercase record-naming rule.

# Key Properties

1. The state record name is prefixed with the module name (e.g., `#good_state{}`).
2. A `-type state() :: #mod_state{}` alias is defined in every OTP behaviour module.
3. The `state()` type lets Dialyzer detect leaks of the internal state outside the module.
4. The module prefix disambiguates state tuples when dumped in the shell during debugging.

# Construction / Recognition

## To Apply

1. Define `-record(<module>_state, {...})` for the behaviour's state.
2. Add `-type state() :: #<module>_state{}.`
3. Use `state()` in the specs of `init/1`, `handle_call/3`, etc.

## To Recognize a Violation

1. The state is a bare integer/term, or a record named generically `#state{}`.

# Context & Application

A PR-blocking convention under Naming; applies to modules implementing OTP behaviours.

- **Typical contexts**: `gen_server`, `gen_statem`, `gen_event` callback modules.
- **Common applications**: a counter `gen_server` using `#good_state{value :: pos_integer()}` and `-type state()`.

# Examples

**Example 1** — bad: the `gen_server` carries its state as a bare `pos_integer()` with no record or type.

**Example 2** — good: `-record(good_state, {value :: pos_integer()})` plus `-type state() :: #good_state{}`, used throughout the callback specs.

# Relationships

## Builds Upon

- **Record names** — the state record obeys the general lowercase record-naming rule.

## Related

- **Encapsulate OTP server APIs** — both concern disciplined OTP behaviour modules.
- **Avoid records in specs** — the `state()` type alias is what lets specs avoid raw `#state{}`.
- **Use behaviours** — this rule applies specifically to behaviour implementations.

# Common Errors

- **Error**: Naming every behaviour's state record `#state{}`.
  **Correction**: Prefix it with the module name so shell dumps are unambiguous.

# Common Confusions

- **Confusion**: Thinking the `state()` type is cosmetic.
  **Clarification**: It enables Dialyzer to catch the internal state leaking outside its module.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Naming", guideline "Explicit state should be explicitly named".

# Verification Notes

- Definition source: Direct quote plus paraphrase of the reasoning.
- Confidence rationale: HIGH — explicit rule with full bad/good `gen_server` modules.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
