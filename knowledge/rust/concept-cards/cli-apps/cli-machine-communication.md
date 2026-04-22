---
concept: CLI Machine Communication
slug: cli-machine-communication
category: cli-development
subcategory: null
tier: intermediate
source: "Command Line Apps in Rust"
source_slug: cli-apps
authors: "The Rust CLI Working Group"
chapter: "Communicating with Machines"
chapter_number: 13
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "machine-readable output"
  - "JSON CLI output"
  - "piping and composability"
  - "structured output"
prerequisites:
  - cli-output
extends:
  - cli-output
related:
  - cli-human-communication
  - cli-argument-parsing
contrasts_with:
  - cli-human-communication
answers_questions:
  - "How do I make CLI output machine-readable?"
  - "How do I detect if output is piped vs. displayed in a terminal?"
  - "What format should I use for structured CLI output?"
  - "How does line-delimited JSON work for CLI tools?"
  - "How do I read piped stdin input in Rust?"
  - "How does ripgrep implement its --json flag?"
---

# Quick Definition

Machine communication is about producing CLI output that other programs can reliably parse and consume -- following the Unix philosophy that "the output of every program [should] become the input to another." This involves detecting whether output goes to a terminal or a pipe, supporting structured formats like JSON, and reading piped stdin input.

# Core Definition

The power of command-line tools comes from composability. To support this, CLI applications should detect whether their output goes to a human at a terminal or to another program via a pipe, and adapt accordingly. The `IsTerminal` trait from `std::io` provides this detection. For machine-readable output, tab-separated values (TSV) is a simple line-based format compatible with tools like `grep`, but it cannot represent mixed message types or nested data. JSON is the preferred structured format: simple enough that parsers exist in every language, powerful enough for complex data. Line-delimited JSON (one JSON document per line) is particularly effective because it supports streaming output of different message types. For input, programs should accept piped stdin (conventionally via a `-` argument) using `std::io::Stdin`.

# Prerequisites

- **CLI output** -- understanding the mechanics of writing to stdout/stderr is needed before adapting output format for different consumers

# Key Properties

1. Use `std::io::IsTerminal` (via `stdout().is_terminal()`) to detect whether output goes to a terminal or pipe
2. When piped, suppress human-oriented formatting (colors, column layouts) and emit one entry per line
3. TSV is simple and grep-friendly but cannot represent mixed message types or nested structures
4. JSON is the preferred structured format -- universally parsable and expressive enough for most cases
5. Line-delimited JSON (one JSON document per line) supports streaming output of different message types
6. Use a `type` field in each JSON object to distinguish message kinds (e.g., "begin", "match", "end", "summary")
7. A `--json` flag is the conventional way to enable machine-readable output
8. For stdin input, use `std::io::Stdin` and the `-` convention to indicate reading from stdin
9. Check that stdin is not interactive (not a tty) when expecting piped input

# Construction / Recognition

## To Add Machine-Readable Output:
1. Add `std::io::IsTerminal` detection to adapt output format automatically
2. Add a `--json` flag (or `--output-format` flag) via your argument parser
3. Define JSON message types with a `type` field for each kind of output
4. Use `serde_json` and the `json!` macro to serialize output
5. Write one JSON document per line (line-delimited JSON) for streaming compatibility
6. Suppress colors and decorative formatting when not outputting to a terminal

## To Add Piped Input Support:
1. Accept `-` as a file argument to indicate stdin
2. Use `std::io::stdin()` to obtain the `Stdin` reader
3. Read lines from stdin the same way you would read from a file
4. Check `stdin().is_terminal()` and show help if stdin is interactive but piped input is expected

# Context & Application

The Unix philosophy of composability is the driving motivation: every program's output should be usable as input to another program. The `ls` command exemplifies adaptive output -- it uses colored columns in a terminal but switches to plain one-per-line output when piped. The ripgrep (`rg`) tool demonstrates best-in-class JSON output: each line is a JSON object with a `type` field ("begin", "match", "end", "summary"), enabling frontends like Visual Studio Code to consume search results as a stream. The `serde_json` crate with its `json!` macro makes producing JSON output straightforward in Rust.

# Examples

**Example 1** (Ch. 13, "Who's reading this?"): Detect terminal vs. pipe using the `IsTerminal` trait: `use std::io::IsTerminal; if std::io::stdout().is_terminal() { println!("I'm a terminal"); } else { println!("I'm not"); }`. This is how `ls` decides whether to use column layout with colors or plain one-per-line output.

**Example 2** (Ch. 13, "Practical example: ripgrep"): ripgrep with `--json` emits line-delimited JSON where each object has a `type` field. A search produces "begin" objects (with file path), "match" objects (with line text, line number, submatch offsets), "end" objects (with per-file stats), and a final "summary" object. Visual Studio Code uses this format to power its code search.

**Example 3** (Ch. 13, "How to deal with input piped into us"): A word-counting program accepts either a filename or `-` for stdin. When `-` is given, it reads lines from `std::io::stdin()`. It checks `stdin().is_terminal()` and shows help if stdin is interactive, because the program expects piped input, not typed input: `echo "hi there friend" | cargo run -- -` outputs "Words from stdin: 3".

# Relationships

## Builds Upon
- **cli-output** -- extends the tutorial output chapter with machine-oriented output strategies

## Enables
- None explicitly

## Related
- **cli-human-communication** -- the two chapters together cover the full spectrum of CLI output design
- **cli-argument-parsing** -- the `--json` and `--output-format` flags are parsed as CLI arguments

## Contrasts With
- **cli-human-communication** -- human output uses colors, columns, and narrative; machine output uses structured formats, one-per-line, and type-tagged JSON

# Common Errors

- **Error**: Always emitting colors and decorative formatting regardless of output destination.
  **Correction**: Use `IsTerminal` to detect piping and suppress colors/formatting when output goes to another program.

- **Error**: Using a single monolithic JSON blob for all output, emitted only at program completion.
  **Correction**: Use line-delimited JSON so consumers can process output incrementally as the program runs, which is especially important for long-running tools.

- **Error**: Not including a `type` field in JSON output objects.
  **Correction**: Different messages (progress, results, errors, summaries) need to be distinguishable. Include a `type` field in each JSON object so consumers can dispatch on message kind.

# Common Confusions

- **Confusion**: Thinking TSV is sufficient for all machine-readable output.
  **Clarification**: TSV works for simple, homogeneous data but cannot represent mixed message types, nested structures, or messages with varying numbers of fields. JSON handles all these cases.

- **Confusion**: Thinking machine-readable and human-readable output are mutually exclusive.
  **Clarification**: The same program can support both. Use `IsTerminal` detection for automatic switching and/or a `--json` flag for explicit control. Default to human-readable when in a terminal.

# Source Reference

Chapter 13: Communicating with Machines. Covers terminal detection with `IsTerminal`, TSV as a simple format, JSON and line-delimited JSON as the preferred structured format, the ripgrep `--json` example, and reading piped stdin input.

# Verification Notes

- Definition source: Synthesized from chapter sections on terminal detection, output formats, JSON output, and stdin handling
- Key Properties: All derived from explicit guidance and examples in Ch. 13
- Confidence rationale: HIGH -- the chapter is the most substantial in this batch (272 lines) with detailed code examples and the ripgrep case study
- Uncertainties: Some code examples use template includes (`{{#include ...}}`) so exact code is not visible, but the text and console output examples are clear
- Cross-reference status: All slugs reference cards in the cli-apps extraction set
