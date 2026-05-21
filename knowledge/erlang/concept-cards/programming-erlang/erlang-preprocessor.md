---
# === CORE IDENTIFICATION ===
concept: Erlang Preprocessor
slug: erlang-preprocessor

# === CLASSIFICATION ===
category: tooling
subcategory: compilation
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Erlang Preprocessor"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "epp"
  - preprocessor

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - macro
  - include-files
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the Erlang preprocessor do?"
  - "How do I inspect preprocessor output?"
---

# Quick Definition

The Erlang preprocessor (`epp`) runs automatically before compilation, expanding macros and inserting include files into the source.

# Core Definition

"Before an Erlang module is compiled, it is automatically processed by the Erlang preprocessor. The preprocessor expands any macros that might be in the source file and inserts any necessary include files" ("The Rest of Sequential Erlang", *Erlang Preprocessor*). Ordinarily its output is not examined, but when debugging a faulty macro you can save it: the OS command `erlc -P some_module.erl` produces a listing file `some_module.P` showing the result of preprocessing.

# Prerequisites

This is a foundational tooling concept with no prerequisites within this source.

# Key Properties

1. Runs automatically before every module compilation.
2. Expands macros in the source file.
3. Inserts include files.
4. Its output is not normally inspected.
5. `erlc -P some_module.erl` saves the preprocessed output to `some_module.P`.

# Construction / Recognition

## To Construct/Create:
1. Nothing to construct — the preprocessor runs as part of normal compilation.

## To Identify/Recognize:
1. To see preprocessor output, run `erlc -P some_module.erl` and read the generated `.P` file.

# Context & Application

- **Typical contexts**: every compilation; explicitly invoked output only when debugging macros.
- **Common applications**: diagnosing a faulty macro by inspecting the `.P` listing.
- **Historical/stylistic notes**: the preprocessor program is named `epp`.

# Examples

**Example 1** (*Erlang Preprocessor*): saving preprocessed output:

```
$ erlc -P some_module.erl
```

This produces a listing file `some_module.P`.

# Relationships

## Builds Upon
- This is a foundational tooling concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Macro** — The preprocessor expands `?MacroName` references.
- **Include files** — The preprocessor inserts files named by `-include`.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Expecting macro expansion to happen at runtime.
  **Correction**: Macros are expanded by the preprocessor before compilation, not at runtime.

# Common Confusions

- **Confusion**: Thinking the preprocessor must be invoked manually.
  **Clarification**: It runs automatically on every compile; `erlc -P` is only for inspecting its output.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Erlang Preprocessor".

# Verification Notes

- Definition source: Direct quotation from *Erlang Preprocessor*.
- Confidence rationale: HIGH — the source explicitly describes the preprocessor and the `-P` flag.
- Uncertainties: None.
- Cross-reference status: Slugs `macro`, `include-files` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
