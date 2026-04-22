---
concept: Safety Guidelines
slug: safety-guidelines
category: safety
subcategory: null
tier: foundational
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "05-safety"
chapter_number: 5
pdf_page: null
section: "Safety Guidelines"
extraction_confidence: high
aliases:
  - "unsafe guidelines"
  - "unsound code"
  - "undefined behavior rules"
  - "unsafe Rust rules"
prerequisites:
  - pragmatic-rust-overview
extends: []
related:
  - library-interop-guidelines
  - library-resilience-guidelines
  - performance-guidelines
contrasts_with: []
answers_questions:
  - "When is it appropriate to use unsafe in Rust?"
  - "What is the difference between unsafe, unsound, and undefined behavior?"
  - "What are the valid reasons for using unsafe code?"
  - "How should unsafe code be documented and tested?"
  - "What does it mean for code to be unsound?"
  - "Can safe functions still be dangerous?"
---

# Quick Definition

Safety guidelines defining three rules: `unsafe` may only mark functions where misuse risks undefined behavior, not merely dangerous operations (M-UNSAFE-IMPLIES-UB); `unsafe` requires a valid reason and must follow strict review, testing, and documentation protocols (M-UNSAFE); and unsound code -- seemingly safe code that can produce undefined behavior -- is never permissible (M-UNSOUND).

# Core Definition

The safety guidelines establish the semantic contract for `unsafe` in Rust codebases. M-UNSAFE-IMPLIES-UB enforces that `unsafe` is a technical marker for undefined behavior risk, not a general "danger" annotation: `unsafe fn print_string(x: *const String)` is valid, `unsafe fn delete_database()` is not. M-UNSAFE permits unsafe only for three reasons: novel abstractions (new smart pointers, allocators), performance (`get_unchecked()`), and FFI/platform calls. It forbids ad-hoc unsafe to shorten code, bypass `Send` bounds, or circumvent lifetimes via transmute. Each category has specific checklists: novel abstractions must be minimal, testable, hardened against adversarial code, accompanied by safety reasoning, and pass Miri. M-UNSOUND declares that unsound abstractions are never permissible with no exceptions -- if safe encapsulation is impossible, `unsafe` functions must be exposed with documented proper behavior. (Ch. 5, "Safety Guidelines")

# Prerequisites

- **pragmatic-rust-overview** -- understanding the overall guideline framework and severity levels (must/should) is needed before applying safety rules

# Key Properties

1. **M-UNSAFE-IMPLIES-UB**: The `unsafe` marker may only be applied to functions and traits if misuse implies the risk of undefined behavior (UB); it must not mark functions that are merely dangerous for other reasons
2. **M-UNSAFE**: The only valid reasons for `unsafe` are: (1) novel abstractions, (2) performance after benchmarking, (3) FFI and platform calls
3. Ad-hoc `unsafe` to simplify enum casts via transmute, bypass `Send` bounds, or bypass lifetime requirements is forbidden
4. Novel abstractions must: verify no established alternative exists, be minimal and testable, handle adversarial code (panicking closures, misbehaving `Deref`/`Clone`/`Drop`), include plain-text safety reasoning, pass Miri
5. Performance-motivated `unsafe` must be preceded by benchmarking and accompanied by safety reasoning and Miri validation
6. FFI code should use established interop libraries; generated bindings must document permissible call patterns
7. **M-UNSOUND**: A function is unsound if it appears safe (not marked `unsafe`) but any calling mode could cause undefined behavior, even if only a "remote, theoretical possibility"
8. Unsound code is never acceptable -- this is the one guideline with explicitly no exceptions
9. Soundness boundaries equal module boundaries: safe functions within a module may rely on invariants guaranteed by other functions in that same module

# Construction / Recognition

## To Apply M-UNSAFE-IMPLIES-UB:
1. Before marking a function `unsafe`, verify it can actually cause undefined behavior if misused
2. If a function is dangerous but cannot cause UB (e.g., deletes data), do not mark it `unsafe`

## To Apply M-UNSAFE:
1. Identify which category the unsafe falls into: novel abstraction, performance, or FFI
2. For novel abstractions: check for existing alternatives, ensure minimality, test against adversarial code, write safety comments, run Miri
3. For performance: benchmark first, add safety reasoning, run Miri
4. For FFI: prefer established interop libraries, document binding call patterns

## To Detect Unsoundness:
1. Look for safe functions that use `unsafe` internally without fully encapsulating the safety invariants
2. Check for `unsafe impl Send/Sync for T` where T does not genuinely satisfy those bounds
3. Check for transmute in safe functions that could be called with types violating the transmute assumptions

# Context & Application

These guidelines codify Rust's safety philosophy at the project level. The distinction between unsafe (a technical UB risk marker) and dangerous (can cause harm without UB) is critical because conflating them causes "warning fatigue" -- developers stop paying attention to `unsafe` if it appears on merely dangerous functions. The unsoundness rule reflects Rust's core promise: safe code cannot cause UB. The module-boundary exception acknowledges that soundness is maintained at the module level, not the function level, allowing internal implementation flexibility.

# Examples

**Example 1** (Ch. 5, M-UNSAFE-IMPLIES-UB -- Valid vs invalid): Valid: `unsafe fn print_string(x: *const String) { }` -- dereferencing a raw pointer risks UB. Invalid: `unsafe fn delete_database() { }` -- dangerous but no UB risk.

**Example 2** (Ch. 5, M-UNSOUND -- Unsound patterns): `fn unsound_ref<T>(x: &T) -> &u128 { unsafe { std::mem::transmute(x) } }` -- a safe function that transmutes arbitrary types. `struct AlwaysSend<T>(T); unsafe impl<T> Send for AlwaysSend<T> {}` -- blanket Send for all T regardless of actual thread safety.

**Example 3** (Ch. 5, M-UNSOUND -- Module boundary soundness): A `MyDevice(*const u8)` struct with a safe `fn get(&self) -> u8 { unsafe { *self.0 } }` is acceptable because `new()` guarantees the pointer is valid, and both functions are in the same module. The safety invariant is maintained at the module boundary.

**Example 4** (Ch. 5, M-UNSAFE -- Adversarial code checklist): Novel abstractions must become invalid (poisoned) if a closure panics, and must assume any safe trait is misbehaving, especially `Deref`, `Clone`, and `Drop`.

# Relationships

## Builds Upon
- **pragmatic-rust-overview** -- the safety guidelines use the must/should severity framework from the overview

## Enables
- Correct, reviewable unsafe code through structured checklists
- Security hardening through strict unsoundness prohibition

## Related
- **library-interop-guidelines** -- escape hatches (M-ESCAPE-HATCHES) use `unsafe`, governed by these safety rules
- **library-resilience-guidelines** -- mockable syscalls reduce the need for unsafe FFI in library code
- **performance-guidelines** -- performance optimization is one of the three valid reasons for unsafe

## Contrasts With
- Projects that use `unsafe` liberally for convenience or code shortening
- Projects that mark dangerous (but UB-free) operations as `unsafe`

# Common Errors

- **Error**: Using `unsafe impl Send for MyWrapper<T> {}` as a blanket implementation to make a type work with Tokio.
  **Correction**: This creates unsound code. Either make the inner type genuinely Send-compatible or redesign the API to not require Send.

- **Error**: Using `transmute` in a safe function to "simplify" enum-to-integer conversion.
  **Correction**: Use safe alternatives like `as` casts or `From` implementations. If transmute is truly needed, the function must be marked `unsafe` or the invariants must be fully encapsulated within the module.

- **Error**: Skipping Miri testing for unsafe code because "it obviously works."
  **Correction**: The guidelines mandate Miri testing for all novel abstractions and performance-motivated unsafe code. Miri catches undefined behavior that may not manifest in normal testing.

# Common Confusions

- **Confusion**: Thinking `unsafe` means "this function is dangerous" or "be careful calling this."
  **Clarification**: `unsafe` is a technical term meaning "misuse may cause undefined behavior." A safe function can be very dangerous (`delete_database()`), and an unsafe function, when properly used, is usually benign (`vec.get_unchecked()`).

- **Confusion**: Believing that if UB is only a "remote theoretical possibility," the code is still sound.
  **Clarification**: The source is explicit: "Even if causing undefined behavior is only a 'remote, theoretical possibility' requiring 'weird code', the function is unsound."

- **Confusion**: Thinking each unsafe function must independently prove its safety.
  **Clarification**: Soundness boundaries equal module boundaries. A safe function may rely on invariants guaranteed by other functions in the same module, as long as the module as a whole maintains safety.

# Source Reference

Chapter 5: Safety Guidelines. Contains three guidelines: M-UNSAFE-IMPLIES-UB (v1.0), M-UNSAFE (v0.2), M-UNSOUND (v1.0). M-UNSAFE is the most detailed with separate checklists for novel abstractions, performance, and FFI. M-UNSOUND includes an explicit "No Exceptions" warning box and a tip about module-boundary soundness. References: Nomicon, Unsafe Code Guidelines, Miri, cheats.rs adversarial code section.

# Verification Notes

- Definition source: Direct from section headings, `<why>` tags, and explanatory text
- Key Properties: Derived from checklists, code examples, and explicit rules in each guideline
- Confidence rationale: HIGH -- all three guidelines have clear definitions, code examples, and the source explicitly marks M-UNSOUND as having "no exceptions"
- Uncertainties: None
- Cross-reference status: pragmatic-rust-overview, library-interop-guidelines, performance-guidelines are from sibling extraction sets
