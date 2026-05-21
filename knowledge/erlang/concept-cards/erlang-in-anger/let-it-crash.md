---
concept: Let It Crash
slug: let-it-crash
category: fault-tolerance
subcategory: failure-philosophy
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Introduction"
chapter_number: null
pdf_page: null
section: "On Running Software"
extraction_confidence: high
aliases:
  - "Let it fail"
prerequisites: []
extends: []
related:
  - supervisor-restart-strategy
  - supervision-tree-navigation
  - otp-application
contrasts_with: []
answers_questions:
  - "What is the let it crash philosophy?"
  - "Why does Erlang restart processes instead of preventing all errors?"
---

# Quick Definition

"Let it crash" is the Erlang/OTP design philosophy in which programmers handle only the errors they know how to handle and delegate the rest to a supervisor or the virtual machine, which restarts the failing process back to a known-stable state.

# Core Definition

Erlang takes the approach that failures will happen no matter what — whether developer-, operator-, or hardware-related — and that it is rarely practical or even possible to remove all errors from a system. From the Introduction, section "On Running Software": "Because you can now deal with failure, and because the cost of weeding out all of the complex bugs from a system before it hits production is often prohibitive, programmers should only deal with the errors they know how to handle, and leave the rest for another process (a supervisor) or the virtual machine to deal with."

Because most bugs are transient, restarting a process back to a state known to be stable when an error is encountered is a surprisingly effective strategy.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Failure is treated as inevitable and survivable, not something to be prevented at all costs.
2. Programmers handle only the errors they understand; unknown errors are escalated to a supervisor or the VM.
3. Restarting brings a process back to a known-stable state, which is effective because most bugs are transient (Jim Gray: 131 of 132 bugs are transient — non-deterministic and often gone on retry).
4. The system does not collapse the first time something bad touches it, which permits live observation and interactive repair in production ("being a doctor").
5. The book reframes the idea against an analogy: most languages provide only "hygiene" (preventing germs); Erlang adds an "immune system" (surviving and dealing with run-time errors).
6. The community now often favors the gentler phrasing "let it fail."

# Construction / Recognition

The typical workflow: write code that handles expected error cases explicitly; for everything else, let the process crash. A supervisor detects the crash and restarts the process from its initialization state. Group processes under supervisors so that a crash returns the relevant subsystem to a blank, stable slate rather than attempting to recover corrupted state.

# Context & Application

This philosophy underlies the entire OTP supervision model. It is the rationale for supervision trees, restart strategies, and synchronous, guarantee-providing initialization. It also enables a distinctive operational practice: because a node survives most failures, an operator can connect to a live system, inspect it, and perform "surgery" without taking the system down.

# Examples

From the Introduction, section "On Running Software": Erlang is likened to the human body's immune system, "whereas most other languages only care about hygiene to make sure no germ enters the body." The book also notes that simply restarting processes back to a stable state "can be a surprisingly good strategy" because most bugs are transient (footnote citing Jim Gray's "Why Do Computers Stop and What Can Be Done About It?").

# Relationships

## Builds Upon
Nothing within this source — it is the founding premise.

## Enables
- `supervisor-restart-strategy` — restart strategies are the mechanism that implements "let it crash."
- `supervision-tree-navigation` — supervision trees exist because crashes are escalated upward.

## Related
- `otp-application` — the structural unit organized around supervision.

## Contrasts With
The "prevent all errors" mindset of most other languages, described in the Introduction as relying purely on "hygiene."

# Common Errors

- Treating "let it crash" as "write sloppy code." It is not an excuse to skip error handling; it is a decision about *which* errors to handle (the ones you understand) and which to escalate.
- Catching every exception in a loop instead of allowing a supervisor to restart to a known-stable state.

# Common Confusions

- "Let it crash" does not mean the whole system goes down. A single process crashes; its supervisor restarts it, and the rest of the system continues.
- It is not negligence: life-critical systems are explicitly excluded from this approach (Introduction footnote).

# Source Reference

Introduction, Section "On Running Software". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the Introduction, section "On Running Software."
- Confidence rationale: high — the source explicitly defines and motivates the concept at length.
- Uncertainties: none.
- Cross-reference status: Verified
