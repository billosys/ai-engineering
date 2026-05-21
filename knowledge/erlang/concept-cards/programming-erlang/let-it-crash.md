---
# === CORE IDENTIFICATION ===
concept: Let It Crash
slug: let-it-crash

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: error-philosophy
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Errors in Concurrent Programs"
chapter_number: 13
pdf_page: null
section: "Error Handling Philosophy"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "let-it-crash"
  - "corrective programming"
  - "non-defensive programming"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - link
extends: []
related:
  - error-handling-philosophy
  - exit-signal
  - keep-alive-process
  - supervisor
contrasts_with:

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between error handling in sequential and concurrent programs?"
  - "What must I know before writing concurrent programs?"
  - "Why does Erlang encourage crashing instead of defensive coding?"
---

# Quick Definition

"Let it crash" is the Erlang practice of writing problem-solving code with as little defensive error checking as possible, allowing a process to terminate immediately when something goes wrong and letting a separate process correct the error.

# Core Definition

"Let it crash" is one of the two phrases that sum up the Erlang philosophy for building fault-tolerant software (the other being "let some other process fix the error"). Applications are built in two parts: a part that solves the problem and a part that corrects errors. The problem-solving part is written assuming all function arguments are correct and that programs execute without errors; it carries as little defensive code as possible. When something goes wrong, the process crashes immediately rather than attempting to continue (Chapter 13, "Error Handling Philosophy"). This produces a clean separation between code that solves problems and code that fixes them, and a dramatic reduction in code volume.

# Prerequisites

- **Process** — Crashing is only safe because Erlang systems have many processes; the failure of one is not catastrophic.
- **Link** — The error-correction half of the strategy relies on links (or monitors) so another process learns of the crash.

# Key Properties

1. The problem-solving code assumes all arguments are correct and contains minimal defensive code.
2. The error-correcting code is separate and often generic, reusable across many applications.
3. Crashing immediately flags the first place an error occurs, giving good diagnostics.
4. Crashing avoids making matters worse by performing further computation on bad data.
5. It simplifies architecture: the application and error recovery are two separate problems, not one interleaved problem.

# Construction / Recognition

## To Apply "Let It Crash":
1. Write the problem-solving function clauses for the expected, correct inputs only.
2. Do not add argument-checking or guard code purely to "guard against" failures.
3. Arrange a separate observing process (via links or monitors) to detect the crash.
4. Put corrective action (ignore, log, restart) in that observing process.

## To Recognize It:
1. Look for modules with no defensive `case`/`try` wrappers around normal logic.
2. Look for a paired supervisor or monitoring process that handles failures generically.

# Context & Application

- **Typical contexts**: Concurrent and fault-tolerant Erlang systems; the foundation of OTP supervision.
- **Common applications**: Database transactions abort and roll back on error; an OS closes files/sockets of a crashed process and restores a stable state.
- **Historical/stylistic notes**: Contrasts sharply with C-style defensive programming, which is necessary in single-process applications where a crash kills the whole application.

# Examples

**Example 1** (Chapter 13, "Why Crash?"): The book enumerates the advantages of crashing immediately — no defensive code, no need to decide what to do, no compounding errors, good diagnostics, simpler architecture.

**Example 2** (Chapter 13, "Programming for Fault Tolerance"): The function `F` waits for a message `X` then computes `list_to_atom(X)`. Sending the atom `hello` causes a `badarg` crash with no defensive code; the crash is caught and reported by a separate `on_exit` handler.

# Relationships

## Builds Upon
- **Error handling philosophy** — "Let it crash" is one half of the remote-detection-and-handling philosophy.

## Enables
- **Supervisor** — OTP supervisors institutionalize the "let it crash, restart it" pattern.
- **Keep-alive process** — Restarting a crashed process is a direct application.

## Related
- **Exit signal** — The crash produces an exit signal that propagates to linked processes.

## Contrasts With
- **Defensive programming** — Defensive programming intertwines error-checking with logic; "let it crash" separates them.

# Common Errors

- **Error**: Adding `try...catch` around everything "just in case," recreating defensive programming.
  **Correction**: Only catch where you can genuinely correct an error locally; otherwise let the process crash.
- **Error**: Letting a process crash with no linked or monitoring process to detect it.
  **Correction**: Always pair crashing code with an observer that takes corrective action.

# Common Confusions

- **Confusion**: "Let it crash" means error handling is ignored.
  **Clarification**: Errors are handled — but remotely, in a separate generic process, not inline.
- **Confusion**: Crashing is acceptable in any language.
  **Clarification**: It is safe in Erlang specifically because of cheap isolated processes and links; in single-process languages a crash kills the whole application.

# Source Reference

Chapter 13: Errors in Concurrent Programs, sections "Error Handling Philosophy" (subsections "Let It Crash" and "Why Crash?") and "Programming for Fault Tolerance."

# Verification Notes

- Definition source: Direct adaptation of the "Let It Crash" and "Why Crash?" subsections.
- Confidence rationale: HIGH — the source explicitly names and explains the philosophy at length.
- Uncertainties: None.
- Cross-reference status: Slugs chosen to match planned cards in this chapter (`error-handling-philosophy`, `exit-signal`, `keep-alive-process`) and canonical cards (`process`, `link`, `supervisor`).
- Re-extraction notes: Fresh extraction; no pre-existing card.
