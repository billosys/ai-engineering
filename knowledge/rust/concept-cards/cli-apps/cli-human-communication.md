---
concept: CLI Human Communication
slug: cli-human-communication
category: cli-development
subcategory: null
tier: intermediate
source: "Command Line Apps in Rust"
source_slug: cli-apps
authors: "The Rust CLI Working Group"
chapter: "Communicating with Humans"
chapter_number: 12
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "human-readable output"
  - "CLI UX patterns"
  - "user-facing output"
prerequisites:
  - cli-output
extends:
  - cli-output
related:
  - cli-machine-communication
  - cli-error-reporting
  - cli-conventions
contrasts_with:
  - cli-machine-communication
answers_questions:
  - "How should a CLI communicate progress to users?"
  - "What log levels should a CLI application use?"
  - "How do I handle panic messages for end users?"
  - "What makes CLI output user-friendly?"
  - "How should log messages be structured for readability?"
---

# Quick Definition

Human communication in CLI applications covers how to present output that is clear, consistent, and informative to users at a terminal -- including progress reporting, structured log levels, and user-friendly panic messages via the `human-panic` crate.

# Core Definition

CLI output for humans should tell a story about what the application is doing and how it impacts the user. When everything is fine, report progress with informative but concise messages using consistent prefixes and sentence structure so logs are easily skimmable. For non-nominal states, use strict, consistent log levels so users can control verbosity via `--verbose` flags or the `RUST_LOG` environment variable. The `log` crate defines five levels in increasing severity: trace, debug, info, warning, error -- with info as a sensible default. When the program crashes (panics), default Rust panic messages are developer-oriented and confusing to end users; the `human-panic` crate provides friendly, actionable crash reports instead.

# Prerequisites

- **CLI output** -- the tutorial chapter on writing output to the terminal covers the mechanics; this chapter addresses *what* to output

# Key Properties

1. Progress messages should be informative but concise, avoiding overly technical terms
2. Use consistent prefixes and sentence structure across all log messages so output is easily skimmable and greppable
3. Each log message should provide enough context to be useful in a filtered log without being verbose
4. The five standard log levels (trace, debug, info, warning, error) should be used consistently, with info as the default
5. Users should control verbosity via `--verbose` flags or `RUST_LOG` environment variable
6. The user should never feel the application is doing something mysterious they cannot follow
7. For long-running actions, show a timeline of steps or a progress bar
8. Custom panic handlers (e.g., `human-panic`) replace developer-oriented crash output with user-friendly messages

# Construction / Recognition

## To Design Good Human Output:
1. For normal operation, show a timeline of steps (e.g., "[1/7] Adding WASM target...")
2. Use consistent message prefixes (e.g., `=>`, `[INFO]`, `[WARN]`)
3. Define severity levels and apply them consistently across all messages
4. Add `--verbose` / `-v` flag support to let users control output detail
5. For long-running operations, add progress bars (e.g., via the `indicatif` crate)
6. Add `human-panic` with `setup_panic!()` at the start of `main` for user-friendly crash reports
7. Test that output reads as a coherent narrative from the user's perspective

## To Recognize Poor Human Output:
1. Log messages with inconsistent formatting or severity levels
2. Technical jargon or internal identifiers exposed to users
3. Long periods of silence during processing with no progress indication
4. Raw Rust panic messages shown to end users

# Context & Application

This chapter builds on the tutorial's output chapter by shifting focus from the mechanics of writing to stdout/stderr to the UX design of what to communicate. The wasm-pack example demonstrates best practices: numbered steps ("[1/7]", "[2/7]"), clear prefixes ("[WARN]", "[INFO]"), and a completion summary ("Done in 1 second"). The `human-panic` crate addresses the common problem of Rust's default panic output (e.g., "thread 'main' panicked at ...") being meaningless to users who do not have access to source code -- replacing it with a friendly message that asks users to submit a crash report file.

# Examples

**Example 1** (Ch. 12, "Example log statements"): A good error message is self-contained: `error: could not find Cargo.toml in /home/you/project/`. A good progress sequence uses consistent formatting: `=> Downloading repository index` / `=> Downloading packages...`

**Example 2** (Ch. 12, "Example log statements"): The wasm-pack output demonstrates an exemplary pattern -- numbered steps like "[1/7] Adding WASM target..." through "[7/7] Running WASM-bindgen...", interspersed with "[WARN]" and "[INFO]" messages at appropriate severity, ending with "Done in 1 second".

**Example 3** (Ch. 12, "When panicking"): With `human-panic`, a panic produces: "Well, this is embarrassing. foo had a problem and crashed. To help us diagnose the problem you can send us a crash report." -- along with a path to a generated report file and the authors' contact information, rather than the default "thread 'main' panicked at..." output.

# Relationships

## Builds Upon
- **cli-output** -- this chapter extends the tutorial output chapter with UX-focused guidance

## Enables
- None explicitly

## Related
- **cli-error-reporting** -- error reporting mechanics underpin the user-facing error messages
- **cli-conventions** -- exit codes and documentation complement human communication

## Contrasts With
- **cli-machine-communication** -- human output prioritizes readability and narrative; machine output prioritizes parsability and structure

# Common Errors

- **Error**: Using inconsistent log levels, making filtered output unreliable.
  **Correction**: Define clear criteria for each severity level and apply them uniformly. A heavily logging application with inconsistent levels provides less information than a non-logging application.

- **Error**: Not providing any output during long-running operations.
  **Correction**: Show progress indicators, step counts, or status messages so the user never feels the application is doing something mysterious.

# Common Confusions

- **Confusion**: Thinking more logging is always better.
  **Clarification**: "A heavily logging application that doesn't follow strict logging levels provides the same amount, or even less information than a non-logging application." Consistency and appropriate severity matter more than volume.

- **Confusion**: Thinking default Rust panic messages are acceptable for end users.
  **Clarification**: Default panic output like "thread 'main' panicked at 'Hello, world!', src/main.rs:2:5" is useful for developers but confusing for users who lack source code access. Use `human-panic` to provide actionable crash reports.

# Source Reference

Chapter 12: Communicating with Humans. Covers output during normal operation, log levels and the `log` crate, example log statements from wasm-pack, and custom panic handling with the `human-panic` crate.

# Verification Notes

- Definition source: Synthesized from chapter sections on normal operation, logging, and panic handling
- Key Properties: All derived from explicit guidance in Ch. 12
- Confidence rationale: HIGH -- the chapter provides clear guidelines with concrete examples (wasm-pack output, human-panic output)
- Uncertainties: None significant
- Cross-reference status: All slugs reference cards in the cli-apps extraction set
