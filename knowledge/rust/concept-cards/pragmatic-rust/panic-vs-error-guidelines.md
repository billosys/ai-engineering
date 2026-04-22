---
concept: Panic vs. Error Guidelines
slug: panic-vs-error-guidelines
category: error-handling
subcategory: null
tier: foundational
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "01-universal"
chapter_number: 1
pdf_page: null
section: "M-PANIC-IS-STOP, M-PANIC-ON-BUG"
extraction_confidence: high
aliases:
  - "panic is stop"
  - "panic on bug"
  - "panic vs result"
  - "when to panic in Rust"
prerequisites:
  - pragmatic-rust-overview
extends: []
related:
  - application-guidelines
  - naming-and-quality-guidelines
contrasts_with: []
answers_questions:
  - "When should Rust code panic instead of returning an error?"
  - "Are panics exceptions in Rust?"
  - "What are valid reasons to panic?"
  - "Should contract violations panic or return errors?"
  - "How do I decide between panic and Result?"
---

# Quick Definition

Panics in Rust are not exceptions -- they signal immediate program termination. M-PANIC-IS-STOP (v1.0) establishes that panics must never be used for error communication or flow control, while M-PANIC-ON-BUG (v1.0) establishes that detected programming errors (contract violations, broken invariants) must panic rather than return `Error` types, because such errors cannot be meaningfully acted upon at runtime.

# Core Definition

**M-PANIC-IS-STOP** (v1.0): "Panics are not exceptions. Instead, they suggest immediate program termination." Although code must be panic-safe (a survived panic may not lead to inconsistent state), invoking a panic means "this program should stop now." It is not valid to: use panics to communicate errors upstream, use panics to handle self-inflicted error conditions, or assume panics will be caught even by your own code. (Ch. 1, Universal)

**M-PANIC-ON-BUG** (v1.0): "As an extension of M-PANIC-IS-STOP, when an unrecoverable programming error has been detected, libraries and applications must panic, i.e., request program termination. In these cases, no Error type should be introduced or returned, as any such error could not be acted upon at runtime." Contract violations -- breaking invariants either within a library or by a caller -- are programming errors and must therefore panic. (Ch. 1, Universal)

# Prerequisites

- **pragmatic-rust-overview** -- understanding the guideline framework, maturity levels, and the "spirit over letter" principle

# Key Properties

1. Panics signal "stop the program now," not "handle this condition upstream"
2. Code must still be panic-safe: a survived panic must not lead to inconsistent state
3. Applications may compile with `panic = "abort"`, so any panic could immediately terminate the process
4. Valid reasons to panic: programming errors (`x.expect("must never happen")`), const contexts (`const { foo.unwrap() }`), user-requested (providing your own `unwrap()` method), and lock poisoning (another thread already panicked)
5. Detected programming bugs (contract violations, broken invariants) must panic, not return `Error`
6. No `Error` type should exist for conditions that cannot be acted upon at runtime
7. What constitutes a violation is situational -- APIs are not expected to go out of their way to detect them if checks would be impossible or expensive
8. When in doubt, take inspiration from the standard library

# Construction / Recognition

## Deciding Between Panic and Result:
1. Is the condition a programming bug (violated invariant, impossible state)? -> **Panic**
2. Is the condition inherently fallible (parsing, I/O, network)? -> **Return Result**
3. Is the caller expected to handle the condition at runtime? -> **Return Result**
4. Would returning an error create impossible error-handling code that no caller can act on? -> **Panic**
5. Can the type system prevent the bad state entirely? -> **Prefer correct-by-construction** (best option)

## Making It "Correct by Construction":
The guidelines advise: "For any user input or calling sequence that would otherwise panic, you should also explore if you can use the type system to avoid panicking code paths altogether." This is the preferred approach when feasible.

# Context & Application

The panic/error boundary is one of the most important design decisions in Rust APIs. Getting it wrong leads to either fragile code that crashes on recoverable conditions, or bloated error-handling code that can never meaningfully recover from programming bugs.

**Typical contexts:**
- Library API design: deciding whether a function returns `Result` or panics on bad input
- Application error handling: understanding that panics are not a control flow mechanism
- Division by zero, index out of bounds, invariant violations during computation
- Const context evaluation where `Result` cannot be used

# Examples

**Example 1** (Ch. 1, M-PANIC-ON-BUG): A `divide_by(x: u32, y: u32) -> u32` function -- if `y == 0`, panicking is the correct approach because the caller violated the contract. A `divide_by_fast` variant may also omit the check and return an unspecified (but not undefined) result.

**Example 2** (Ch. 1, M-PANIC-ON-BUG): A `parse_uri(s: &str) -> Result<Uri, ParseError>` function -- passing an invalid URI is not a contract violation because parsing is inherently fallible, so a `Result` must be returned.

**Example 3** (Ch. 1, M-PANIC-IS-STOP): An application compiled with `[profile.release] panic = "abort"` -- any invocation of panic will cause an otherwise functioning program to needlessly abort, demonstrating why panics must not be used for error communication.

# Relationships

## Builds Upon
- **pragmatic-rust-overview** -- these guidelines follow the maturity and applicability framework

## Enables
- **application-guidelines** -- M-APP-ERROR (use anyhow/eyre for recoverable application errors) builds on the clear panic/error distinction established here

## Related
- **naming-and-quality-guidelines** -- M-STATIC-VERIFICATION helps catch potential panics via static analysis
- safety-guidelines (covered by another extraction agent) -- M-UNSAFE-IMPLIES-UB relates to undefined behavior that panics help prevent

## Contrasts With
- Exception-based error handling in languages like Java, Python, and C++ where exceptions are used for recoverable conditions
- Returning `Result` for every possible failure, including programming bugs

# Common Errors

- **Error**: Using panics to communicate recoverable errors upstream (treating panic like a Java exception).
  **Correction**: Panics mean "stop the program." Use `Result` for any condition the caller can meaningfully handle.

- **Error**: Returning `Error` types for programming bugs that no caller can act upon.
  **Correction**: If detecting `must_be_even == 3` during an already existing check, panic. Do not invent an error type for invariant violations.

- **Error**: Assuming `catch_unwind` makes panic-as-exception safe.
  **Correction**: Code should not assume panics will be caught. With `panic = "abort"`, `catch_unwind` has no effect.

# Common Confusions

- **Confusion**: Thinking all bad inputs should cause panics.
  **Clarification**: Whether bad input is a contract violation depends on context. `parse_uri("not a uri")` is inherently fallible and returns `Result`. `divide_by(x, 0)` is a programming bug and should panic. The distinction is whether the failure mode is expected in normal operation.

- **Confusion**: Thinking "correct by construction" means you never need to panic.
  **Clarification**: Correct-by-construction designs (using the type system to prevent invalid states) are preferred but not always feasible. When they are not, panicking on detected bugs is the right approach.

# Source Reference

Chapter 1: Universal Guidelines, sections M-PANIC-IS-STOP (v1.0, "To ensure soundness and predictability") and M-PANIC-ON-BUG (v1.0, "To avoid impossible error handling code and ensure runtime consistency"). Both include code examples and the "Correct by Construction" tip.

# Verification Notes

- Definition: Direct quotations from both guideline sections
- Key Properties: Synthesized from the enumerated valid panic reasons and the discussion of contract violations
- Confidence: HIGH -- both guidelines are explicit, include code examples, and cross-reference each other
- Uncertainties: The boundary between "contract violation" and "inherently fallible" is acknowledged as situational by the source itself
- Cross-reference status: All slugs are within this extraction set or reference Agent B's planned cards
