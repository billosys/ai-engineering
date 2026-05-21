---
concept: No Module Or Function Name Macros
slug: no-module-or-function-name-macros
category: core-idioms
subcategory: macros
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Macros"
chapter_number: null
pdf_page: null
section: "No module or function name macros"
extraction_confidence: high
aliases:
  - "no name macros"
  - "SERVER macro anti-pattern"
prerequisites: []
extends:
  - avoid-macros
related:
  - uppercase-macro-names
contrasts_with: []
answers_questions:
  - "Why shouldn't I use a macro for a module or function name?"
---

# Quick Definition

Don't use macros to stand in for module or function names.

# Core Definition

"Don't use macros for module or function names" (Inaka, "No module or function name macros"). Names like `-define(SERVER, ?MODULE)` or `-define(TM, another_module)` are disallowed; the actual module/function name is written out.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Module names are not hidden behind macros.
2. Function names are not hidden behind macros.
3. The motivation is shell debugging: copy-pasted code with name macros cannot run.
4. It is a PR-rejection rule under Macros.

# Construction / Recognition

## To Apply

1. Write `?MODULE` directly (it is a permitted predefined macro) rather than aliasing it to `?SERVER`.
2. Write the target module's real name (`another_module:handle(...)`).

## To Recognize a Violation

1. A `-define` aliases a module or function name (`-define(SERVER, ?MODULE)`, `-define(TM, another_module)`).

# Context & Application

A PR-blocking convention under Macros.

- **Typical contexts**: `gen_server` modules that alias `?MODULE` to `?SERVER`.
- **Common applications**: `gen_server:call(?MODULE, ...)` instead of `gen_server:call(?SERVER, ...)`.

# Examples

**Example 1** — bad: `-define(SERVER, ?MODULE)` and `-define(TM, another_module)`, then `gen_server:call(?SERVER, ...)` and `?TM:handle(...)`.

**Example 2** — good: `gen_server:call(?MODULE, ...)` and `another_module:handle(...)`.

# Relationships

## Builds Upon

- **No Macros** — this is a specific, called-out case of the general macro-avoidance rule.

## Related

- **Uppercase macros** — companion macro rule.

# Common Errors

- **Error**: Defining `?SERVER` as `?MODULE` "for clarity."
  **Correction**: Use `?MODULE` directly; it is already a permitted predefined macro.

# Common Confusions

- **Confusion**: Thinking a name macro improves readability.
  **Clarification**: It breaks the very common debugging workflow of copying lines into the shell, where macros do not expand.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Macros", guideline "No module or function name macros".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
