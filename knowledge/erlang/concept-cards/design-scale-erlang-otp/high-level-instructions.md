---
# === CORE IDENTIFICATION ===
concept: High-Level Upgrade Instructions
slug: high-level-instructions

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
section: "High-Level Instructions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - update instruction
  - load_module instruction
  - synchronized code replacement
  - simple code replacement

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application-upgrade-file
extends: []
related:
  - low-level-instructions
  - release-upgrade-file
  - code-change-callback
contrasts_with:
  - low-level-instructions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are high-level upgrade instructions?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

High-level upgrade instructions are the recommended, abstract actions written in an `.appup` file — such as `update`, `load_module`, `add_application` — that `systools` translates into low-level `relup` commands when generating the upgrade script.

# Core Definition

Actions in an `.appup` file are grouped into high-level and low-level instructions, with high-level instructions being mapped to low-level ones when the upgrade scripts are generated (Cesarini & Vinoski, p. 346-348, pdf p. 336). For the sake of simplicity, you are encouraged to use high-level instructions and avoid low-level ones where possible, even though they can be mixed. The `update` instruction and its variants perform *synchronized code replacements*, where all processes dependent on `Mod` are suspended before the new module is loaded and resumed afterward; `load_module` performs a *simple code replacement* where no process needs suspending.

# Prerequisites

- **Application upgrade file** — High-level instructions are written in `.appup` files; that file concept comes first.

# Key Properties

1. Written in `.appup` files; translated to low-level instructions when the `relup` is generated.
2. Recommended over low-level instructions for simplicity; the two can be mixed.
3. `{update, Mod}` and variants — synchronized code replacement (suspend dependent processes, load, purge, resume).
4. `{update, Mod, supervisor}` — for supervisor callback modules when changing the supervisor spec.
5. `{update, Mod, {advanced, Extra}, ...}` — invokes `Mod:code_change/3,4` with `Extra`.
6. `{update, ...}` variants can set `DepMods`, `Timeout`, `PrePurge`/`PostPurge`, and `ModType` (`static`/`dynamic`).
7. `{load_module, Mod}` and variants — simple code replacement, no process suspension; for library modules.
8. `{add_module, Mod}` / `{delete_module, Mod}` — add/delete modules between releases.
9. `{add_application, ...}` / `{remove_application, ...}` / `{restart_application, ...}` — application-level actions.

# Construction / Recognition

## To Use High-Level Instructions:
1. In the `.appup` file, list actions like `{update, Mod, {advanced, Extra}}` for behavior modules needing state change.
2. Use `{load_module, Mod}` for library modules where no process needs suspending.
3. Use `{add_application, App}` / `{restart_application, App}` for application-level changes.
4. Let `systools:make_relup/3,4` translate them to low-level `relup` commands.

## To Recognize Them:
1. Atoms/tuples like `update`, `load_module`, `add_module`, `add_application` in an `.appup` file.

# Context & Application

- **Typical contexts**: Writing `.appup` files for release upgrades.
- **Common applications**: Synchronized replacement of behavior modules; simple replacement of library modules; adding or restarting applications.
- **Historical/stylistic notes**: For the vast majority of use cases, high-level instructions are enough; low-level instructions are reserved for complex upgrades.

# Examples

**Example 1** (p. 345): The coffee `.appup` uses `update` with `{advanced, {}}` — `update` loads the new module and `{advanced, {}}` triggers the `code_change/4` call passing `{}` as the last argument: `{update, coffee_fsm, {advanced, {}}}`.

**Example 2** (p. 347): `{update, Mod, supervisor}` is used when `Mod` is a supervisor callback module and the supervisor specification returned by `init/1` is changing.

**Example 3** (p. 348): `{load_module, Mod}` is a simple code replacement — used for library modules or extending functionality that does not affect running processes.

# Relationships

## Builds Upon
- **Application upgrade file** — High-level instructions are the contents of `.appup` files.

## Enables
- **Release upgrade file** — High-level instructions translate into the `relup`'s low-level commands.

## Related
- **Code change callback** — `{advanced, Extra}` instructions invoke `code_change`.

## Contrasts With
- **Low-level instructions** — High-level instructions are abstract and recommended; low-level instructions are the granular commands they translate into.

# Common Errors

- **Error**: Reaching for low-level instructions when a high-level one would do.
  **Correction**: Use high-level instructions wherever possible; they are simpler and cover the vast majority of cases.

- **Error**: Using a plain `update` when behavior state must change.
  **Correction**: Use `{update, Mod, {advanced, Extra}}` so `code_change/3,4` is invoked; plain `update`/`soft` does not call it.

# Common Confusions

- **Confusion**: Thinking high- and low-level instructions cannot be mixed.
  **Clarification**: They can be mixed in the same `.appup` file, though high-level is recommended.

- **Confusion**: Believing `update` always calls `code_change`.
  **Clarification**: `code_change` is invoked only when `{advanced, Extra}` is included; omitting it (or `soft`) skips `code_change`.

# Source Reference

Chapter 11: Release Upgrades, section "High-Level Instructions," pages 346-348 (pdf p. 336).

# Verification Notes

- Definition source: Direct adaptation of pp. 346-348.
- Confidence rationale: HIGH — the source explicitly lists and describes each high-level instruction.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
