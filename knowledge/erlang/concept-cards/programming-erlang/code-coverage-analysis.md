---
# === CORE IDENTIFICATION ===
concept: Code Coverage Analysis
slug: code-coverage-analysis

# === CLASSIFICATION ===
category: testing
subcategory: coverage
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Profiling, Debugging, and Tracing"
chapter_number: 21
pdf_page: null
section: "Testing Code Coverage"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - cover
  - "coverage analyzer"
  - "coverage analysis"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-profiling-tools
contrasts_with:
  - erlang-profiling-tools

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is code coverage analysis?"
  - "How do I find lines of code that are never executed?"
  - "How do I use the cover tool?"
---

# Quick Definition

Code coverage analysis counts how many times each line of code is executed. The `cover` tool reports these counts so you can find lines that never run — potential errors or dead code — and design tests to exercise them.

# Core Definition

"We use coverage analysis to count the number of times each line of code in our programs has been executed. Lines that have been executed zero times might indicate an error or dead code that you might be able to remove. Finding lines that are executed a large number of times might help you optimize your program" (chapter introduction). The coverage analyzer is the `cover` tool: a module is compiled for coverage with `cover:compile/1`, the program is run, and `cover:analyse_to_file/1` writes a results file annotating each line with its execution count. Lines marked with zero are particularly interesting because their correctness has never been exercised. "Designing test cases that cause all the coverage counts to be greater than zero is a valuable method of systematically finding hidden faults in our programs."

# Prerequisites

This is a foundational testing/tooling concept within this chapter — it has no prerequisites among the concepts of these chapters.

# Key Properties

1. Counts how many times each line of code is executed.
2. The tool is the `cover` module.
3. Lines executed zero times may indicate an error or removable dead code.
4. Lines executed many times may point to optimization opportunities.
5. Results are written to a file (`Module.COVER.out`) with per-line counts on the left.
6. Forcing every line to be executed by test cases is a "surefire" way to find obscure bugs.

# Construction / Recognition

## To Run Coverage Analysis:
1. Start the coverage analyzer with `cover:start()`.
2. Compile the module for coverage with `cover:compile(Module)`.
3. Run the program so the code executes.
4. Write results with `cover:analyse_to_file(Module)`.
5. Inspect the output file; investigate any lines marked with zero.

## To Recognize:
1. Look for `cover:start()`, `cover:compile/1`, and `cover:analyse_to_file/1` calls.
2. Look for a `*.COVER.out` results file.

# Context & Application

Coverage analysis turns "which lines have I never tested?" into a concrete checklist.

- **Typical contexts**: Testing — auditing which lines are exercised by a test suite.
- **Common applications**: Designing new test cases to force zero-count lines to execute.
- **Historical/stylistic notes**: Armstrong applied this to the original Erlang JAM compiler; afterward there were about three bug reports in two years and then none.

# Examples

**Example 1** ("Testing Code Coverage"): Coverage of the SHOUTcast server.

```erlang
1> cover:start().            %% start the coverage analyser
2> cover:compile(shout).     %% compile shout.erl for coverage
3> shout:start().            %% run the program
4> cover:analyse_to_file(shout).   %% analyse the results
{ok,"shout.COVER.out"}
```

**Example 2** ("Testing Code Coverage"): In the output file, lines prefixed `131..|` were executed 131 times and lines prefixed `0..|` were never executed — for instance the `Max = Stop - OffSet` branch of `send_file/6`.

# Relationships

## Builds Upon
- (Foundational tooling concept within this chapter.)

## Enables
- (No card depends on this concept.)

## Related
- **Erlang profiling tools** — Both measure execution; profiling focuses on time/call counts, coverage on per-line execution.

## Contrasts With
- **Erlang profiling tools** — Profiling answers "where does time go?"; coverage answers "which lines never run?".

# Common Errors

- **Error**: Running the program before compiling the module with `cover:compile/1`.
  **Correction**: Compile the module for coverage first, then run it, then analyze.

- **Error**: Ignoring zero-count lines.
  **Correction**: Zero-count lines have never been tested; design test cases to force them to execute.

# Common Confusions

- **Confusion**: Believing high coverage counts indicate a fast program.
  **Clarification**: Counts indicate execution frequency, not speed; many-times lines are optimization candidates, but timing comes from profiling.

# Source Reference

Chapter 21: "Profiling, Debugging, and Tracing", chapter introduction and section "Testing Code Coverage" (including the "The Best of All Test Methods?" sidebar).

# Verification Notes

- Definition source: Direct quotes from the chapter introduction and "Testing Code Coverage".
- Confidence rationale: HIGH — the `cover` workflow and its purpose are explicitly described with a worked example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
