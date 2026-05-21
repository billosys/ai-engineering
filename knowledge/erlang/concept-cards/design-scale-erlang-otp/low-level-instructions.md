---
# === CORE IDENTIFICATION ===
concept: Low-Level Upgrade Instructions
slug: low-level-instructions

# === CLASSIFICATION ===
category: applications-releases
subcategory: release-upgrades
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Release Upgrades"
chapter_number: 11
pdf_page: 336
section: "Low-Level Instructions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - relup instructions
  - point_of_no_return
  - load_object_code

# === TYPED RELATIONSHIPS ===
prerequisites:
  - high-level-instructions
  - release-upgrade-file
extends: []
related:
  - application-upgrade-file
  - code-change-callback
  - upgrading-the-emulator-and-core-applications
contrasts_with:
  - high-level-instructions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are low-level upgrade instructions?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

Low-level upgrade instructions are the granular commands that make up a `relup` file — `load_object_code`, `suspend`, `load`, `code_change`, `resume`, and others. High-level `.appup` instructions are translated into them when the upgrade script is generated.

# Core Definition

`relup` files consist of low-level instruction sets generated from the `.appup` files; for complex upgrades you can write your files using low-level instructions or edit generated ones by hand (Cesarini & Vinoski, p. 341-343, pdf p. 336). Each instruction performs one granular step of the upgrade: reading object code, suspending processes, loading or removing modules, purging old versions, invoking `code_change`, resuming processes, or restarting the emulator. The `point_of_no_return` instruction marks where the system can no longer recover; a crash after it restarts the old release.

# Prerequisites

- **High-level instructions** — Low-level instructions are what high-level ones translate into; understanding high-level instructions comes first.
- **Release upgrade file** — Low-level instructions are the contents of the `relup` file.

# Key Properties

1. Make up the `relup` file; high-level `.appup` instructions translate into them.
2. `{load_object_code, {App, Vsn, ModuleList}}` — reads modules into memory but does not load them into the runtime.
3. `point_of_no_return` — appears once; a crash after it restarts the old release.
4. `{load, {Module, PrePurge, PostPurge}}` — makes a `load_object_code`d module the current version.
5. `{apply, {Mod, Func, ArgList}}` — calls `apply/3`; can replace `code_change`.
6. `{remove, ...}`, `{purge, ModuleList}` — make a version old / purge old versions.
7. `{suspend, ...}` / `{resume, ModuleList}` — suspend and resume dependent behaviors.
8. `{code_change, [{Module, Extra}]}` / `{code_change, Mode, ...}` — triggers `code_change/3,4` (`Mode` is `up` or `down`).
9. `{stop, ...}` / `{start, ModuleList}` — terminate / restart children via the supervisor.
10. `restart_new_emulator` — restarts the VM when upgrading `erts`/core applications (executed first).
11. `restart_emulator` — restarts the VM for a non-core upgrade; must be the last instruction.

# Construction / Recognition

## To Write or Edit Low-Level Instructions:
1. For complex upgrades, write the `relup` directly or edit a generated one.
2. Place `point_of_no_return` after `load_object_code` instructions.
3. Order suspend -> load -> code_change -> resume for synchronized replacements.
4. Put `restart_emulator` last if a VM restart is needed for a non-core upgrade.

## To Recognize Them:
1. Atoms/tuples like `load_object_code`, `point_of_no_return`, `suspend`, `load`, `code_change`, `resume` in a `relup` file.

# Context & Application

- **Typical contexts**: Complex upgrades that high-level instructions cannot fully express.
- **Common applications**: Hand-editing `relup` files; understanding what a generated `relup` actually does.
- **Historical/stylistic notes**: If worried about instruction order, use high-level instructions and let `systools:make_relup/3,4` generate the `relup`.

# Examples

**Example 1** (p. 340): The coffee `relup`'s upgrade instruction sequence:

```erlang
[{load_object_code,{coffee,"1.1",[coffee_fsm]}},
 point_of_no_return,
 {suspend,[coffee_fsm]},
 {load,{coffee_fsm,brutal_purge,brutal_purge}},
 {code_change,up,[{coffee_fsm,{}}]},
 {resume,[coffee_fsm]}]
```

**Example 2** (p. 342): `point_of_no_return` is placed after the `load_object_code` instruction; crashes after it restart the old version of the system.

# Relationships

## Builds Upon
- **High-level instructions** — Low-level instructions are the translation target of high-level ones.
- **Release upgrade file** — Low-level instructions are the contents of the `relup`.

## Related
- **Application upgrade file** — Can also contain low-level instructions directly.
- **Code change callback** — The `{code_change, ...}` instruction triggers it.
- **Upgrading the emulator and core applications** — Uses `restart_new_emulator`.

# Common Errors

- **Error**: Placing instructions after `restart_emulator`.
  **Correction**: `restart_emulator` must be the last instruction; anything after it is ignored.

- **Error**: Hand-ordering low-level instructions and getting the sequence wrong.
  **Correction**: If unsure of ordering, write high-level instructions and let `systools:make_relup/3,4` generate the `relup`.

# Common Confusions

- **Confusion**: Confusing `restart_new_emulator` with `restart_emulator`.
  **Clarification**: `restart_new_emulator` is for `erts`/core upgrades and runs first; `restart_emulator` is for non-core upgrades and runs last.

- **Confusion**: Thinking `load_object_code` loads the module into the runtime.
  **Clarification**: It only reads the modules into memory; `load` makes them the current version.

# Source Reference

Chapter 11: Release Upgrades, section "Low-Level Instructions," pages 341-343 (pdf p. 336).

# Verification Notes

- Definition source: Direct adaptation of pp. 341-343.
- Confidence rationale: HIGH — the source explicitly lists and describes each low-level instruction.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
