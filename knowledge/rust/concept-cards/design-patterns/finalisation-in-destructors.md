---
concept: Finalisation in Destructors
slug: finalisation-in-destructors
category: idiom
subcategory: null
tier: intermediate
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "Finalisation in destructors"
extraction_confidence: high
aliases:
  - "RAII cleanup"
  - "Drop for finalisation"
  - "destructor cleanup pattern"
  - "scope guard pattern"
  - "finally alternative in Rust"
prerequisites:
  - constructor-idiom
extends: []
related:
  - default-trait
  - mem-take-replace
contrasts_with: []
answers_questions:
  - "How do I run cleanup code when a function exits in Rust?"
  - "Does Rust have finally blocks?"
  - "How do I use Drop for resource cleanup?"
  - "What happens to destructors during a panic?"
  - "How do I guarantee code runs on function exit?"
---

# Quick Definition

Rust has no `finally` blocks. Instead, use an object's destructor (the `Drop` trait) to run code that must execute before a scope exits. The destructor runs regardless of whether the function returns normally, returns early via `?`, or panics (during stack unwinding).

# Core Definition

"Rust does not provide the equivalent to `finally` blocks - code that will be executed no matter how a function is exited. Instead, an object's destructor can be used to run code that must be run before exit." (Ch. 1, "Finalisation in destructors")

"If a function has multiple return points, then executing code on exit becomes difficult and repetitive (and thus bug-prone). This is especially the case where return is implicit due to a macro. A common case is the `?` operator which returns if the result is an `Err`, but continues if it is `Ok`. `?` is used as an exception handling mechanism, but unlike Java (which has `finally`), there is no way to schedule code to run in both the normal and exceptional cases. Panicking will also exit a function early." (Motivation)

# Prerequisites

- **constructor-idiom** -- understanding how to construct the guard object that will be dropped

# Key Properties

1. Destructors run when an object goes out of scope, whether via normal return, early return, or panic (during unwinding)
2. The `Drop` trait provides the destructor: `fn drop(&mut self)`
3. The guard object must be assigned to a named variable (not `_` alone, which drops immediately)
4. Variable names starting with `_` (e.g., `_exit`) suppress "unused variable" warnings while keeping the object alive until scope end
5. The guard should be a value or uniquely owned pointer (e.g., `Box<Foo>`), not a shared pointer (`Rc`)
6. The finalizer should not be moved or returned from the function
7. Destructors are NOT guaranteed to run in all cases: infinite loops, crashes, and double-panics can prevent them
8. A destructor that panics during unwinding causes the thread to abort immediately

# Construction / Recognition

## To Implement This Pattern:
1. Define a struct to act as a guard/finalizer
2. Implement `Drop` for the struct, placing cleanup code in `fn drop(&mut self)`
3. Create an instance of the guard at the point where cleanup should begin being tracked
4. Assign it to a variable (e.g., `let _guard = MyGuard;`)
5. The destructor will run when the variable goes out of scope

## Critical Rules:
- Do NOT name the variable `_` (underscore alone) -- this drops immediately
- DO name it `_something` if it's only used for finalisation (suppresses unused warnings)
- Do NOT use `Rc` or shared ownership -- the guard could outlive the function
- Do NOT move or return the guard -- it must be dropped in the original scope

# Context & Application

This pattern is Rust's answer to `try`/`finally` in Java, `defer` in Go, and `with` statements in Python. It leverages Rust's deterministic destruction (RAII) to ensure cleanup happens without explicit `finally` blocks.

**Typical contexts:**
- Releasing locks (MutexGuard)
- Closing file handles
- Flushing buffers
- Logging function exit
- Restoring state after temporary modifications
- Any resource cleanup that must happen regardless of exit path

**How Rust's stack unwinding works:** "In Rust, destructors are run when an object goes out of scope. This happens whether we reach the end of block, there is an early return, or the program panics. When panicking, Rust unwinds the stack running destructors for each object in each stack frame. So, destructors get called even if the panic happens in a function being called."

**Double-panic behavior:** "If a destructor panics while unwinding, there is no good action to take, so Rust aborts the thread immediately, without running further destructors."

# Examples

**Example 1** (Ch. 1, "Finalisation in destructors"): Using a guard struct to print "exit" whenever the function returns:

```rust,ignore
fn baz() -> Result<(), ()> {
    // some code
}

fn bar() -> Result<(), ()> {
    // These don't need to be defined inside the function.
    struct Foo;

    // Implement a destructor for Foo.
    impl Drop for Foo {
        fn drop(&mut self) {
            println!("exit");
        }
    }

    // The destructor of _exit will run however the function `bar` is exited.
    let _exit = Foo;
    // Implicit return with `?` operator.
    baz()?;
    // Normal return.
    Ok(())
}
```

Whether `baz()` returns `Ok` (and `bar` continues to `Ok(())`) or `Err` (and `bar` returns early via `?`), the destructor of `_exit` prints "exit". If `bar` panics, the destructor still runs during unwinding.

# Relationships

## Builds Upon
- **constructor-idiom** -- the guard object must be constructed to start the finalisation scope

## Enables
- RAII guards for resource management

## Related
- **mem-take-replace** -- another pattern for managing owned values in complex control flow
- **default-trait** -- guard types may implement Default

## Contrasts With
- `finally` blocks in Java/C#/Python (Rust has no equivalent language construct)
- `defer` in Go (similar effect but different mechanism)

# Common Errors

- **Error**: Naming the guard variable `_` (bare underscore), which drops it immediately.
  **Correction**: Use `_guard` or `_exit` -- the underscore prefix suppresses warnings while keeping the value alive until scope end.

- **Error**: Putting critical finalisation logic in a destructor and relying on it being absolutely guaranteed.
  **Correction**: "Destructors cannot be relied on as finalizers where it is absolutely essential that finalisation happens." Infinite loops, crashes before exit, and double-panics can prevent destructors from running.

- **Error**: Panicking inside a destructor.
  **Correction**: "You must take extra care in your destructors not to panic, since it could leave resources in an unexpected state." A panic during unwinding aborts the thread immediately.

# Common Confusions

- **Confusion**: Thinking destructors always run in Rust.
  **Clarification**: "It is not guaranteed that destructors will run. For example, if there is an infinite loop in a function or if running a function crashes before exit. Destructors are also not run in the case of a panic in an already panicking thread."

- **Confusion**: Thinking you can return or move the guard and still get the cleanup behavior.
  **Clarification**: "The finalizer must be assigned into a variable" and "the finalizer should not be moved or returned." It "must be kept alive until the end of the function and must then be destroyed."

- **Confusion**: Thinking `Rc<Guard>` works as a finalizer.
  **Clarification**: "If a shared pointer (such as `Rc`) is used, then the finalizer can be kept alive beyond the lifetime of the function." Use owned values or `Box`.

# Source Reference

Chapter 1: Idioms, "Finalisation in destructors" section. Covers Description, Example, Motivation, Advantages, Disadvantages, and Discussion (including stack unwinding behavior and double-panic). See also: RAII guards pattern (patterns/behavioural/RAII.md).

# Verification Notes

- Definition: Direct quotation from the Description and Motivation subsections
- Key Properties: All from explicit statements in the source, including Discussion section details
- Example: Directly from the source with original code
- Confidence: HIGH -- the source provides thorough description with code, motivation, and detailed discussion of edge cases
- Uncertainties: None
- Cross-reference status: All slugs reference cards in this extraction set
