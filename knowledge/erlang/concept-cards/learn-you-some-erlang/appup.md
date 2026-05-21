---
concept: Appup File
slug: appup
category: production-ops
subcategory: code-upgrades
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Leveling Up in the Process Quest"
chapter_number: 22
pdf_page: null
section: "Adding Appup Files"
extraction_confidence: high
aliases:
  - "appup"
  - ".appup file"
  - "application upgrade file"
prerequisites:
  - hot-code-loading
  - otp-application
extends: []
related:
  - relup
  - code-change-callback
contrasts_with:
  - relup
answers_questions:
  - "What is an appup file?"
  - "How do I tell OTP what to change when upgrading an application?"
  - "What instructions go in an appup file?"
---

# Appup File

## Quick Definition

An appup file is a list of Erlang instructions describing how to upgrade (or downgrade) a single OTP application from one version to another. It is named `ApplicationName.appup` and placed in the application's `ebin/` directory.

## Core Definition

The book defines appups as "files containing instructions on how to update individual applications" (Ch. 22). An appup file contains lists of tuples and atoms telling OTP what to do, in which direction, and for which versions. Its general format is:

```erlang
{NewVersion,
 [{VersionUpgradingFrom, [Instructions]}],
 [{VersionDownGradingTo, [Instructions]}]}.
```

It accepts lists of versions because an application can be upgraded or downgraded to/from many versions. The file must be named `NameOfYourApp.appup` and placed in the app's `ebin/` directory (Ch. 22, "Adding Appup Files").

## Prerequisites

- **Hot-code-loading** — Appups are the structured way to script safe live code upgrades
- **Otp-application** — Appups operate at the granularity of a single application

## Key Properties

1. Format is `{NewVsn, [{FromVsn, Instructions}], [{ToVsn, Instructions}]}` — new version, upgrade clauses, downgrade clauses
2. High-level instructions are usually all you need (low-level ones also exist)
3. `{add_module, Mod}` — module loaded for the first time
4. `{load_module, Mod}` — already-loaded module that was modified (loads new version on upgrade, old version on downgrade)
5. `{delete_module, Mod}` — module removed from the VM
6. `{update, Mod, {advanced, Extra}}` — suspends processes running `Mod`, calls `code_change` with `Extra`, then resumes them
7. `{update, Mod, supervisor}` — redefines a supervisor's `init` to change restart strategy or child specs
8. `{apply, {M, F, A}}` — calls `apply(M, F, A)`
9. Module dependencies can be expressed with `{load_module, Mod, [ModDeps]}` so a command runs only after dependency modules are handled

## Construction / Recognition

### To write an appup file

1. Identify which modules changed between versions
2. Classify each: new (`add_module`), modified-no-suspension (`load_module`), modified-needs-suspension (`update`), or removed (`delete_module`)
3. Write the upgrade clause `{OldVsn, [Instructions]}` in dependency order
4. Write the downgrade clause, typically with the instructions reversed
5. Save as `AppName.appup` in the app's `ebin/` directory

## Context & Application

Appups are an input to relup generation. The relup generator detects added/removed applications automatically, so appups need no special instructions for that.

## Examples

**Example** (Ch. 22): `processquest-1.1.0`'s appup file —

```erlang
{"1.1.0",
 [{"1.0.0", [{add_module, pq_quest},
             {load_module, pq_enemy},
             {load_module, pq_events},
             {update, pq_player, {advanced, []}, [pq_quest, pq_events]}]}],
 [{"1.0.0", [{update, pq_player, {advanced, []}},
             {delete_module, pq_quest},
             {load_module, pq_enemy},
             {load_module, pq_events}]}]}.
```

**Example** (Ch. 22): `sockserv-1.0.1`'s appup, brief because only one module changed and needed no suspension —

```erlang
{"1.0.1",
 [{"1.0.0", [{load_module, sockserv_serv}]}],
 [{"1.0.0", [{load_module, sockserv_serv}]}]}.
```

## Relationships

### Builds Upon

- **Hot-code-loading** — Appups encode the suspend/change/resume mechanics declaratively

### Enables

- **Relup** — Appups for each application are combined into a release-level relup

### Related

- **Code-change-callback** — `{update, Mod, {advanced, Extra}}` triggers the module's `code_change`

### Contrasts With

- **Relup** — An appup covers one application; a relup covers a whole release

## Common Errors

- **Error**: Placing instructions out of dependency order so a module is updated before a module it depends on.
  **Correction**: Order instructions so dependencies are handled first, or declare them with `{update, Mod, {advanced, Extra}, [ModDeps]}`.
- **Error**: Putting the appup file somewhere other than the app's `ebin/` directory.
  **Correction**: It must be `AppName.appup` inside `ebin/`.

## Common Confusions

- **Confusion**: Thinking `{load_module, Mod}` always loads a newer version.
  **Clarification**: It loads the new version on upgrade and the old version on downgrade — direction depends on context.
- **Confusion**: Believing you must list app add/remove instructions yourself.
  **Clarification**: The relup generator detects added and removed applications automatically.

## Source Reference

Chapter 22, "Leveling Up in the Process Quest," section "Adding Appup Files." See the instruction list and the two appup file listings for `processquest-1.1.0` and `sockserv-1.0.1`.

## Verification Notes

- Definition: Direct adaptation from "Adding Appup Files"
- Key Properties: All instruction types explicit in source
- Confidence: HIGH — the chapter enumerates the format and instructions precisely
- Cross-references: `relup`, `hot-code-loading`, `code-change-callback` planned in this chapter
