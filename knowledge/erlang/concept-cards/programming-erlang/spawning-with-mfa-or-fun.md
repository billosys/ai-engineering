---
# === CORE IDENTIFICATION ===
concept: Spawning with MFAs or Funs
slug: spawning-with-mfa-or-fun

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-creation
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Concurrent Programming"
chapter_number: 12
pdf_page: null
section: "Spawning with MFAs or Funs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "spawn MFA vs fun"
  - "MFA"
  - "module-function-arguments"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spawn
extends:
  - spawn
related:
  - process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I spawn with an MFA versus a fun?"
  - "What is an MFA?"
  - "Why does dynamic code upgrade need spawn(MFA)?"
---

# Quick Definition

When spawning a process you can pass either an explicit module, function name, and argument list (an MFA) or a fun. The MFA form supports dynamic code upgrade; the fun form does not.

# Core Definition

"Spawning a function with an explicit module, function name, and argument list (called an MFA) is the proper way to ensure that our running processes will be correctly updated with new versions of the module code if it is compiled while it is being used. The dynamic code upgrade mechanism does not work with spawned funs. It works only with explicitly named MFAs" (Armstrong, "Concurrent Programming," "Spawning with MFAs or Funs"). The guidance: "If you don't care about dynamic code upgrade or you are certain that your program will never be changed in the future, use the `spawn(Fun)` form of `spawn`. If in doubt, use `spawn(MFA)`."

# Prerequisites

- **Spawn** — This concept is the choice between the two argument forms of `spawn`.

# Key Properties

1. An MFA is an explicit module, function name, and argument list — `spawn(Mod, Func, Args)`.
2. The fun form is `spawn(Fun)`.
3. The MFA form supports dynamic code upgrade; running processes pick up recompiled code.
4. The fun form does *not* support dynamic code upgrade.
5. Default guidance: use `spawn(Fun)` if upgrade is irrelevant; otherwise — and "if in doubt" — use `spawn(MFA)`.
6. For the MFA form the function must be exported; for the fun form it need not be.

# Construction / Recognition

## To Construct/Create:
1. If the process may need its code upgraded while running, spawn with an MFA: `spawn(?MODULE, loop, [])`.
2. If upgrade is irrelevant or impossible, the `spawn(fun() -> ... end)` form is fine.

## To Identify/Recognize:
1. `spawn(Mod, Func, Args)` is the MFA form; `spawn(fun() -> ... end)` is the fun form.
2. Long-lived server loops spawned with `?MODULE` are typically MFA-spawned for upgradeability.

# Context & Application

- **Typical contexts**: Choosing how to start long-lived processes; designing for hot code upgrade.
- **Common applications**: MFA-spawned server loops in upgradeable systems; fun-spawned short-lived tasks.
- **Historical/stylistic notes**: The concurrent-program template uses `spawn(?MODULE, loop, [])` — the MFA form — precisely so the loop survives code upgrades.

# Examples

**Example 1** ("Spawning with MFAs or Funs"): The recommendation — "If in doubt, use `spawn(MFA)`" — because only the MFA form supports dynamic code upgrade.

**Example 2** ("A Concurrent Program Template"): `start() -> spawn(?MODULE, loop, []).` — the MFA form, used so the spawned loop is upgradeable.

**Example 3** ("Processes Are Cheap"): `spawn(fun() -> wait() end)` — the fun form, used for short-lived test processes where upgrade does not matter.

# Relationships

## Builds Upon
- **Spawn** — This is the decision about which `spawn` form to use.

## Enables
- (Enables correct dynamic code upgrade of spawned processes when the MFA form is chosen.)

## Related
- **Process** — The choice affects how a long-lived process behaves under code upgrade.

## Contrasts With
- None — the contrast is between the two forms themselves, captured within this card.

# Common Errors

- **Error**: Spawning a long-lived, upgradeable server loop with `spawn(Fun)`.
  **Correction**: Use the MFA form so dynamic code upgrade reaches the running process.

- **Error**: Using the MFA form but forgetting to export the spawned function.
  **Correction**: The MFA form requires `Func/length(Args)` to be exported from `Mod`.

# Common Confusions

- **Confusion**: Thinking the two `spawn` forms are fully interchangeable.
  **Clarification**: Only the MFA form participates in dynamic code upgrade; the fun form does not.

- **Confusion**: Believing `spawn(Fun)` is always inferior.
  **Clarification**: It is fine when code upgrade is irrelevant or the program will not change; it also avoids needing an export.

# Source Reference

Chapter 12: "Concurrent Programming," section "Spawning with MFAs or Funs." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct quotes of the MFA-vs-fun guidance from the named section.
- Confidence rationale: HIGH — the trade-off is stated explicitly.
- Uncertainties: None.
- Cross-reference status: Cross-refs verified against KB slugs.
- Re-extraction notes: Fresh extraction; new card (no prior file).
