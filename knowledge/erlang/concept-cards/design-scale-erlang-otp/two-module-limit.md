---
# === CORE IDENTIFICATION ===
concept: Two-Module Limit
slug: two-module-limit

# === CLASSIFICATION ===
category: applications-releases
subcategory: code-loading
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Release Upgrades"
chapter_number: 11
pdf_page: 336
section: "Two-Module Limit"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - two-version limit
  - old and current code
  - module version limit

# === TYPED RELATIONSHIPS ===
prerequisites:
  - software-upgrade
extends: []
related:
  - module-versioning
  - fully-qualified-function-call
  - code-change-callback
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why can only two versions of a module exist in the runtime?"
  - "What must I understand before performing release upgrades?"
---

# Quick Definition

The two-module limit is the rule that the Erlang runtime allows at most two versions of any module loaded at once — an old version and a current version. It is legacy debt from a design decision in the original JAM virtual machine.

# Core Definition

The two-module version limit is legacy debt from a design decision taken to simplify the JAM virtual machine (the most-used VM at the time) and to preserve memory in an architecture where memory was scarce (Cesarini & Vinoski, p. 337-338, pdf p. 336). At any one time the runtime can hold two versions of code for the same module: the old and the current. In the JAM, to garbage collect code you had to walk every process's stack to determine which module version it was using — a very time-consuming activity the developers preferred to avoid, so they simplified it with the two-module limitation.

# Prerequisites

- **Software upgrade** — The two-module limit is the constraint that makes upgrades work the way they do; the upgrade concept comes first.

# Key Properties

1. At most two versions of a module are loaded at once: old and current.
2. It is legacy debt from the JAM virtual machine's design.
3. The design simplified code garbage collection and preserved scarce memory.
4. Garbage-collecting code would have required walking every process's stack for return addresses.
5. Today the right design would allow unlimited versions, garbage-collected when unused.
6. When a third version is loaded, the current becomes old, the old is purged, and processes still on the now-deleted old version are unconditionally terminated.

# Construction / Recognition

## To Work Within the Limit:
1. Load a new version — it becomes current, the previous current becomes old.
2. Ensure all processes have migrated off the old version (via fully qualified calls) before loading a third version.
3. Use the `-vsn` attribute or md5 digest to identify which version is which.

## To Recognize a Violation:
1. A process is unconditionally terminated when a third version is loaded while it still runs the oldest.

# Context & Application

- **Typical contexts**: Reasoning about what happens during repeated upgrades.
- **Common applications**: Planning upgrade sequences so no process is left on a soon-to-be-purged version.
- **Historical/stylistic notes**: The JAM (Joe's Abstract Machine) was the most-used VM when the decision was made; memory was scarce then.

# Examples

**Example 1** (p. 343): With versions 1.0 and 1.1 of the coffee module loaded, loading another version — even 1.0 again — would terminate the coffee FSM process because it runs the now-deleted old version; the current becomes old and the newly loaded module becomes current.

**Example 2** (p. 337): A process running an old module version that is forcefully removed by `code:purge(Module)` is unconditionally terminated.

# Relationships

## Builds Upon
- **Software upgrade** — The two-module limit shapes how upgrades behave.

## Related
- **Module versioning** — The `-vsn` attribute distinguishes the two coexisting versions.
- **Fully qualified function call** — How a process moves from the old version to the current.
- **Code change callback** — Migrates state during the transition between versions.

# Common Errors

- **Error**: Loading a new module version while processes still run the old version.
  **Correction**: Migrate all processes to the current version (via fully qualified calls) before loading a third version, or they are killed.

- **Error**: Calling `code:purge/1` on a module still in use by old-version processes.
  **Correction**: Purging unconditionally terminates processes still on that old version; ensure none remain or accept the termination.

# Common Confusions

- **Confusion**: Thinking the two-module limit is a deliberate modern design choice.
  **Clarification**: It is legacy debt from the JAM VM; a modern design would allow unlimited versions with garbage collection.

- **Confusion**: Believing three versions can briefly coexist.
  **Clarification**: Loading a third version immediately purges the oldest and kills any process still running it.

# Source Reference

Chapter 11: Release Upgrades, section "Two-Module Limit," pages 337-338 (pdf p. 336).

# Verification Notes

- Definition source: Direct adaptation of pp. 337-338.
- Confidence rationale: HIGH — the source explicitly explains the two-module limit and its JAM-VM origin.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
