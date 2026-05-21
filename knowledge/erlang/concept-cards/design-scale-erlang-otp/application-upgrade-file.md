---
# === CORE IDENTIFICATION ===
concept: Application Upgrade File
slug: application-upgrade-file

# === CLASSIFICATION ===
category: applications-releases
subcategory: release-files
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Release Upgrades"
chapter_number: 11
pdf_page: 336
section: "Application Upgrade Files"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - appup file
  - ".appup file"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-upgrade
extends: []
related:
  - high-level-instructions
  - low-level-instructions
  - release-upgrade-file
  - code-change-callback
  - erlang-otp-file-types
contrasts_with:
  - release-upgrade-file
  - application-resource-file

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an application upgrade file?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

An application upgrade file (`.appup`) holds the set of instructions for upgrading or downgrading between versions of one application. It is named after the application, placed in its `ebin` directory, and consumed by `systools` to generate the `relup`.

# Core Definition

An application upgrade file contains a set of actions to be executed when upgrading or downgrading to other versions of the same application (Cesarini & Vinoski, p. 342-344, pdf p. 336). Application upgrade files are similar in concept to app files because they are used by `systools` to create the upgrade script. They have the name of the application with the `.appup` suffix and are placed in the `ebin` directory alongside the app file. The file is a tuple `{Vsn, [{UpFromV, InstructionsU}, ...], [{DownToV, InstructionsD}, ...]}`, where `Vsn` is the version being upgraded to, `UpFromV` are the versions upgraded from, and `DownToV` are the versions downgradeable to.

# Prerequisites

- **Release upgrade** — `.appup` files are inputs to a release upgrade; the release-upgrade concept comes first.

# Key Properties

1. Named `ApplicationName.appup`, placed in the application's `ebin` directory.
2. Holds a tuple `{Vsn, [{UpFromV, InstructionsU}], [{DownToV, InstructionsD}]}`.
3. `Vsn` is the version being upgraded to; can be an exact string or a binary regular expression.
4. `UpFromV`/`DownToV` can be exact version strings or binaries with regular expressions matching version ranges.
5. Regular expressions test with `re:run(Vsn, RegExp)`.
6. Instructions are divided into high-level and low-level; high-level are translated to low-level when the `relup` is generated.
7. `{Vsn, [], []}` (two empty lists) means no actions are needed.
8. Since OTP 17, `.appup` files are included in every standard application; before that, only some core applications had them.

# Construction / Recognition

## To Create an Application Upgrade File:
1. Name the file `AppName.appup` and place it in the application's `ebin`.
2. Write `{Vsn, UpFromList, DownToList}` where `Vsn` is the target version.
3. Populate `UpFromList`/`DownToList` with `{FromVsn, Instructions}` tuples.
4. Use high-level instructions where possible; mix in low-level only when necessary.

## To Recognize It:
1. A file with the `.appup` suffix in an application's `ebin` directory.
2. List existing ones with `ls lib/*/ebin/*.appup` in the Erlang root.

# Context & Application

- **Typical contexts**: Defining how each changed application moves between versions during an upgrade.
- **Common applications**: Generating the `relup` file; describing upgrade/downgrade instruction sets per application.
- **Historical/stylistic notes**: OTP standard applications usually allow upgrading or downgrading by two revisions.

# Examples

**Example 1** (p. 343): The `sasl.appup` file for version 2.6.1, using binary regular expressions:

```erlang
{"2.6.1",
 [{<<"2\\.[5-6](\\.[0-9]+)*">>,[restart_new_emulator]},
  {<<"2\\.4(\\.[0-9]+)*">>,[restart_new_emulator]}],
 [{<<"2\\.[5-6](\\.[0-9]+)*">>,[restart_new_emulator]},
  {<<"2\\.4(\\.[0-9]+)*">>,[restart_new_emulator]}]
}.
```

**Example 2** (p. 345): The coffee application's `coffee.appup` file:

```erlang
{"1.1",
 [{"1.0", [{update, coffee_fsm, {advanced, {}}}]}],
 [{"1.0", [{update, coffee_fsm, {advanced, {}}}]}]
}.
```

# Relationships

## Builds Upon
- **Release upgrade** — `.appup` files are required inputs to a release upgrade.

## Enables
- **Release upgrade file** — `.appup` files (with `.rel` files) generate the `relup`.

## Related
- **High-level instructions** — The actions a high-level `.appup` typically contains.
- **Low-level instructions** — High-level `.appup` actions translate to these.
- **Code change callback** — `{advanced, Extra}` instructions trigger `code_change`.

## Contrasts With
- **Release upgrade file** — The `.appup` is per-application; the `relup` is per-release and holds the generated low-level commands.
- **Application resource file** — The `.app` file describes an application; the `.appup` describes how to upgrade between its versions.

# Common Errors

- **Error**: Forgetting to escape backslashes in regular-expression version patterns.
  **Correction**: Erlang uses `\` to escape characters, so a literal period in a regex is `\\.`.

- **Error**: Placing the `.appup` file outside the `ebin` directory.
  **Correction**: It must sit in the application's `ebin` directory alongside the `.app` file so `systools` finds it.

# Common Confusions

- **Confusion**: Thinking `Vsn` must be an exact version string.
  **Clarification**: It can be a binary holding a regular expression that matches multiple application versions.

- **Confusion**: Believing the `.appup` file holds the executed upgrade commands.
  **Clarification**: It holds high-level (and optionally low-level) instructions; the executed low-level commands end up in the generated `relup`.

# Source Reference

Chapter 11: Release Upgrades, section "Application Upgrade Files," pages 342-346 (pdf p. 336). See also Table 11-1 (Erlang/OTP file types), Chapter 10 p. 311.

# Verification Notes

- Definition source: Direct adaptation of pp. 342-344.
- Confidence rationale: HIGH — the source explicitly defines the `.appup` file, its naming, placement, and structure.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
