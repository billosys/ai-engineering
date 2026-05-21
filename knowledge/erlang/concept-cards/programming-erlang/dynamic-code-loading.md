---
# === CORE IDENTIFICATION ===
concept: Dynamic Code Loading
slug: dynamic-code-loading

# === CLASSIFICATION ===
category: applications-releases
subcategory: code-management
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Dynamic Code Loading"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - hot code loading
  - code upgrade
  - code swapping

# === TYPED RELATIONSHIPS ===
prerequisites:
  - module-attributes
extends: []
related:
  - function-reference
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does dynamic code loading work?"
  - "How many versions of a module can run at once?"
  - "What happens to processes running old code when a module is recompiled?"
---

# Quick Definition

Dynamic code loading lets a running Erlang system replace a module's code: every fully qualified call `Mod:Func(...)` always reaches the latest version of the module, even while code is executing.

# Core Definition

"Dynamic code loading is one of the most surprising features built into the heart of Erlang... The idea is simple: every time we call `someModule:someFunction(...)`, we'll always call the latest version of the function in the latest version of the module, even if we recompile the module while code is running in this module" ("The Rest of Sequential Erlang", *Dynamic Code Loading*). "Erlang can have two versions of a module running at any one time, the current version and an old version. When you recompile a module, any process running code in the old version is killed, the current version becomes the old version, and the newly compiled module becomes the current version." It works like a two-slot shift register: adding new code junks the oldest version, so some processes can run old code while others run new code simultaneously.

# Prerequisites

- **Module attributes** — Correct module/file naming is required for automatic code loading to work.

# Key Properties

1. A fully qualified `Mod:Func(...)` call always reaches the latest loaded version of `Mod`.
2. Recompiling a module makes all callers use the new version on their next qualified call.
3. At most two versions of a module exist at once: current and old.
4. Recompiling promotes current to old and the new module to current.
5. Processes still running the now-superseded old version are killed.
6. Some processes can run old code while others run new code at the same time.

# Construction / Recognition

## To Construct/Create:
1. Recompile a module with `c(Mod)` in the running shell; existing processes pick up the new code on their next external call to it.

## To Identify/Recognize:
1. After a recompile, all processes (old and new) calling `b:x()` start seeing the new return value.
2. A third recompile of a module kills any processes still running its oldest version.

# Context & Application

- **Typical contexts**: upgrading code in long-running systems without stopping them.
- **Common applications**: the `a`/`b` example — recompiling `b` makes both old and new `a` processes call the new `b:x()`.
- **Historical/stylistic notes**: function references that include the module name provide switch-over points for code upgrade; see also `purge_module`.

# Examples

**Example 1** (*Dynamic Code Loading*): two long-running `a` processes call `b:x()` in a loop:

```erlang
b:x() -> 1.   %% original
b:x() -> 2.   %% after recompile
```

After recompiling `b`, both existing `a` processes print `b:x() = 2` — they automatically call the new version of `b`. If `b` is recompiled twice while old `a` processes persist, the processes running the oldest version of `a` are killed.

# Relationships

## Builds Upon
- **Module attributes** — `-module` naming must match the file for automatic loading.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Function reference** — Module-qualified function references are switch-over points for code upgrade.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Naming a module differently from its `.erl` file.
  **Correction**: Use `modname.erl` for module `modname`, or automatic code loading will not work correctly.

- **Error**: Assuming an unlimited number of module versions can coexist.
  **Correction**: Only two versions coexist; a third recompile kills processes still on the oldest version.

# Common Confusions

- **Confusion**: Thinking recompiling a module instantly switches every running process.
  **Clarification**: A process picks up the new version on its next fully qualified external call; a process inside an old version continues there until it makes such a call (or is killed when its version is purged).

- **Confusion**: Believing local (non-qualified) calls also switch versions mid-loop.
  **Clarification**: It is the fully qualified `Mod:Func` call that always resolves to the latest version.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Dynamic Code Loading".

# Verification Notes

- Definition source: Direct quotation and adaptation from *Dynamic Code Loading*.
- Confidence rationale: HIGH — the source explains the mechanism in depth with a worked `a`/`b` example.
- Uncertainties: None.
- Cross-reference status: Slug `module-attributes` extracted in this chapter; `function-reference` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
