---
concept: CLI Signal Handling
slug: cli-signal-handling
category: cli-development
subcategory: null
tier: intermediate
source: "Command Line Apps in Rust"
source_slug: cli-apps
authors: "The Rust CLI Working Group"
chapter: "Signal Handling"
chapter_number: 9
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Ctrl-C handling"
  - "graceful shutdown"
  - "signal handler"
prerequisites:
  - cli-rust-getting-started
extends: []
related:
  - cli-error-reporting
  - cli-human-communication
contrasts_with: []
answers_questions:
  - "How do I handle Ctrl-C in a Rust CLI application?"
  - "How do I gracefully shut down a CLI tool?"
  - "What crates help with signal handling in Rust?"
  - "How do I handle Unix signals in async Rust?"
  - "What happens when a user presses Ctrl-C a second time?"
---

# Quick Definition

Signal handling in Rust CLI applications involves intercepting OS-level signals (most commonly Ctrl-C / SIGINT) and reacting to them gracefully -- closing network connections, removing temporary files, or resetting system settings -- rather than relying on the default immediate-exit behavior.

# Core Definition

Command-line applications need to react to signals sent by the operating system. The most common is Ctrl-C, which typically tells a process to terminate. On Unix systems (Linux, macOS, FreeBSD), processes receive signals and can handle them in a program-defined way or ignore them. Windows uses Console Handlers and structured exception handling instead. If an application does not need graceful shutdown, the default OS handling (exit immediately, let the OS clean up) is fine. For applications that must properly close network connections, remove temporary files, or reset system settings, explicit signal handling is necessary.

# Prerequisites

- **CLI Rust getting started** -- understanding basic Rust CLI structure and how the main function works is needed before adding signal handling

# Key Properties

1. The `ctrlc` crate provides cross-platform Ctrl-C handling with a simple callback API
2. For real-world programs, set an `Arc<AtomicBool>` in the signal handler and check it periodically in hot loops or when waiting on threads
3. The `signal-hook` crate handles additional Unix signals beyond SIGINT (e.g., SIGTERM, SIGHUP)
4. Channels (e.g., via `crossbeam-channel`) can be used instead of shared booleans -- the signal handler emits a value, and application code uses channel select as a synchronization point
5. For async/tokio applications, `signal-hook`'s `tokio-support` feature provides `futures::Stream`-based signal handling via `.into_async()`
6. When a user presses Ctrl-C a second time while the first is being handled, the typical behavior is to quit immediately

# Construction / Recognition

## To Add Signal Handling to a CLI:
1. Determine whether graceful shutdown is needed (network connections, temp files, system settings)
2. If only Ctrl-C is needed, add the `ctrlc` crate
3. For broader Unix signal support, use `signal-hook`
4. Choose a communication pattern: shared `Arc<AtomicBool>`, channel-based, or async stream
5. In the signal handler, set the flag or send to the channel
6. In application hot loops and wait points, check the flag or select on the channel
7. Handle the case of a second Ctrl-C by allowing immediate exit

## To Recognize the Need for Signal Handling:
1. The application manages external resources (network, files, hardware)
2. The application performs long-running operations that users may want to interrupt
3. Clean shutdown semantics are required (e.g., "goodbye" messages to peers)

# Context & Application

Signal handling sits at the boundary between OS process management and application logic. On Unix, signals are the primary inter-process communication mechanism for lifecycle events. The Rust ecosystem provides layered crate support: `ctrlc` for the simple common case, `signal-hook` for comprehensive signal handling, and async integration for tokio-based applications. The channel-based approach is particularly idiomatic in Rust because it integrates naturally with `crossbeam-channel`'s `select!` macro, allowing signal handling to be composed with other event sources.

# Examples

**Example 1** (Ch. 9, "First off: Handling Ctrl+C"): The `ctrlc` crate provides the simplest approach -- register a closure that runs on Ctrl-C. However, simply printing a message is not useful alone; a real program should set a shared `Arc<AtomicBool>` in the handler and check it in hot loops or thread waits, breaking when it becomes true.

**Example 2** (Ch. 9, "Using channels"): Instead of a shared boolean, create a channel and have the signal handler send a value on it. Application code uses `crossbeam-channel`'s `select!` to wait on either the signal channel or other work channels, providing clean synchronization between signal handling and application logic.

**Example 3** (Ch. 9, "Using futures and streams"): For tokio-based async applications, enable `signal-hook`'s `tokio-support` feature and call `.into_async()` on `Signals` types to get a `futures::Stream`, integrating signal handling into the async event loop.

# Relationships

## Builds Upon
- **cli-rust-getting-started** -- basic CLI application structure is needed before adding signal handling

## Enables
- None explicitly

## Related
- **cli-error-reporting** -- signal handling is part of the broader error and shutdown story
- **cli-human-communication** -- informing users about shutdown progress relates to UX patterns

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Only printing a message in the Ctrl-C handler without actually triggering shutdown logic.
  **Correction**: Set a shared `Arc<AtomicBool>` or send on a channel so the main application loop can detect the signal and begin cleanup.

- **Error**: Not handling a second Ctrl-C, leaving the user stuck during a long cleanup.
  **Correction**: Track whether Ctrl-C has already been received; on the second press, exit immediately.

# Common Confusions

- **Confusion**: Thinking signal handling works the same on all platforms.
  **Clarification**: Unix uses signals (SIGINT, SIGTERM, etc.) while Windows uses Console Handlers. Cross-platform crates like `ctrlc` abstract this difference, but more advanced signal handling (SIGHUP, SIGUSR1) is Unix-specific.

- **Confusion**: Thinking the `ctrlc` crate handles all signal types.
  **Clarification**: `ctrlc` only handles Ctrl-C (SIGINT). For other Unix signals, use `signal-hook`.

# Source Reference

Chapter 9: Signal Handling. Covers cross-platform considerations, the `ctrlc` crate for basic Ctrl-C handling, `signal-hook` for broader signal support, channel-based patterns with `crossbeam-channel`, and async integration via tokio.

# Verification Notes

- Definition source: Synthesized from chapter opening paragraphs and subsection explanations
- Key Properties: All derived from explicit guidance in Ch. 9
- Confidence rationale: HIGH -- the chapter provides clear, specific guidance with code examples and crate recommendations
- Uncertainties: Code examples use template includes (`{{#include ...}}`) so exact code is not visible, but the surrounding text explains the patterns clearly
- Cross-reference status: Prerequisite and related slugs reference cards in the cli-apps extraction set
