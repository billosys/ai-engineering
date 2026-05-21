---
# === CORE IDENTIFICATION ===
concept: Erlang Startup File
slug: erlang-startup-file

# === CLASSIFICATION ===
category: tooling
subcategory: environment
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Compiling and Running Your Program"
chapter_number: 10
pdf_page: null
section: "Executing a Set of Commands When the System Is Started"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - ".erlang file"
  - ".erlang"
  - "Erlang init file"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - code-path
  - erlang-shell
  - running-erlang-programs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the .erlang file?"
  - "How do I run commands automatically when Erlang starts?"
  - "Where do I set the code path persistently?"
---

# Quick Definition

The `.erlang` file is a startup file containing Erlang code that the runtime reads and evaluates when it boots. It is the usual place to set the code path and run other initialization commands.

# Core Definition

The conventional place to set the load path is "a file called `.erlang` in your home directory." More generally, "you can put any Erlang code in this file — when you start Erlang, it first reads and evaluates all the commands in this file" (Armstrong, "Compiling and Running Your Program," "Executing a Set of Commands When the System Is Started"). If a `.erlang` file also exists in the *current* directory when Erlang starts, "it will take precedence over the `.erlang` in your home directory," letting Erlang behave differently depending on where it is launched.

# Prerequisites

This is a foundational concept within this chapter — it has no prerequisites among the chapter's other concepts.

# Key Properties

1. Named `.erlang`; located in the home directory by default.
2. Read and evaluated automatically at runtime startup.
3. May contain any Erlang code, not just path commands.
4. A `.erlang` in the current directory takes precedence over the one in the home directory.
5. `init:get_argument(home)` reveals where Erlang thinks your home directory is.

# Construction / Recognition

## To Construct/Create:
1. Create a file named `.erlang` in your home directory.
2. Put initialization expressions in it — typically `code:add_patha/1`/`add_pathz/1` calls.
3. Optionally add an `io:format` print so a local `.erlang` is not silently forgotten.
4. Start Erlang; the commands run automatically.

## To Identify/Recognize:
1. Output appearing before the Erlang banner at startup often comes from `.erlang`.
2. `init:get_argument(home)` confirms the directory searched for the home `.erlang`.

# Context & Application

- **Typical contexts**: Persistently configuring the code path; per-project startup behavior via a local `.erlang`.
- **Common applications**: Adding project directories to the load path; loading helper modules; setting up the environment.
- **Historical/stylistic notes**: Armstrong suggests including print statements in a local startup file "otherwise, you might forget about the local startup file, which could be very confusing."

# Examples

**Example 1** ("Executing a Set of Commands When the System Is Started"): A `.erlang` containing `io:format("Hi, I'm in your .erlang file~n").` prints that line before the `Eshell` banner when `erl` starts.

**Example 2** ("Modifying the Development Environment"): The usual convention is to put `code:add_patha`/`add_pathz` commands in `.erlang` so the load path is set on every startup.

**Example 3** ("Executing a Set of Commands When the System Is Started"): `init:get_argument(home)` returns `{ok,[["/home/joe"]]}`, showing Erlang's notion of the home directory.

# Relationships

## Builds Upon
- This is foundational within the chapter.

## Enables
- **Code path** — `.erlang` is the standard place to populate the code path persistently.

## Related
- **The Erlang shell** — `.erlang` runs before the shell starts.
- **Running Erlang programs** — Startup configuration affects how programs are launched.

## Contrasts With
- None.

# Common Errors

- **Error**: Creating a local `.erlang` and later being confused by unexpected startup behavior in that directory.
  **Correction**: Add an `io:format` print to local startup files so their presence is visible.

- **Error**: Putting `.erlang` in the wrong directory because the home directory was assumed.
  **Correction**: Run `init:get_argument(home)` to confirm where Erlang looks.

# Common Confusions

- **Confusion**: Thinking `.erlang` can only set the code path.
  **Clarification**: It may contain any Erlang code; path setup is just the common use.

- **Confusion**: Believing the home `.erlang` always wins.
  **Clarification**: A `.erlang` in the current directory takes precedence over the home one.

# Source Reference

Chapter 10: "Compiling and Running Your Program," sections "Modifying the Development Environment" and "Executing a Set of Commands When the System Is Started." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the `.erlang` discussion in the named sections.
- Confidence rationale: HIGH — the file and its behavior are described explicitly.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-10 cards.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
