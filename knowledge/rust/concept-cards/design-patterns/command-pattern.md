---
concept: Command Pattern
slug: command-pattern
category: behavioural-pattern
subcategory: null
tier: intermediate
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "02-design-patterns"
chapter_number: 2
pdf_page: null
section: "Behavioural Patterns"
extraction_confidence: high
aliases:
  - "command"
  - "action pattern"
  - "transaction pattern"
prerequisites:
  - constructor-idiom
extends: []
related:
  - strategy-pattern
  - interpreter-pattern
contrasts_with:
  - strategy-pattern
answers_questions:
  - "How do I encapsulate actions as objects in Rust?"
  - "What are the different approaches to implementing the Command pattern in Rust?"
  - "When should I use trait objects vs function pointers vs Fn trait objects for commands?"
---

# Quick Definition

The Command pattern separates actions into their own objects and passes them as parameters. In Rust, this can be implemented via trait objects, function pointers, or `Fn` trait objects, each with different trade-offs between flexibility, performance, and ergonomics.

# Core Definition

"The basic idea of the Command pattern is to separate out actions into its own objects and pass them as parameters." The pattern encapsulates actions or transactions as objects that can be "executed or invoked in some order later at different time." Commands "may also be triggered as a result of some event" and "might be undoable." (Rust Design Patterns, Ch. 2: Behavioural Patterns, "Command")

# Prerequisites

- **Constructor idiom** -- commands are constructed as objects (structs or closures) before being passed to an invoker; familiarity with Rust's struct construction patterns is assumed

# Key Properties

1. Actions are encapsulated as objects (structs, function pointers, or closures)
2. Commands can be stored in collections and executed later in a defined order
3. Commands can be undoable (e.g., `execute` paired with `rollback`)
4. Commands can be triggered by events (user input, data arrival)
5. Three implementation approaches in Rust: trait objects, function pointers, `Fn` trait objects
6. Trait objects use dynamic dispatch; function pointers use static dispatch
7. Function pointers implement all three traits `Fn`, `FnMut`, and `FnOnce`, so closures can be passed where function pointers are expected
8. Command logs can be stored for replay (e.g., crash recovery)

# Construction / Recognition

## Approach 1: Using Trait Objects
1. Define a trait with `execute` and `rollback` methods (or similar action methods)
2. Implement the trait for each concrete command struct
3. Store commands as `Vec<Box<dyn Migration>>` (or equivalent trait object collection)
4. Iterate over the collection to execute or rollback in order

## Approach 2: Using Function Pointers
1. Define a type alias for the function pointer signature: `type FnPtr = fn() -> String`
2. Create a `Command` struct holding execute and rollback function pointers
3. Store commands in a `Vec<Command>` and invoke them via `(cmd.execute)()`
4. Pass either named functions or closures at the call site

## Approach 3: Using `Fn` Trait Objects
1. Define a type alias: `type Migration<'a> = Box<dyn Fn() -> &'a str>`
2. Store execute and rollback closures in separate vectors
3. Use generic bounds `E: Fn() -> &'a str + 'static` for the add method
4. Invoke closures directly from the vectors

## To Recognize the Pattern:
1. Look for actions stored in collections for deferred execution
2. Look for an invoker that iterates over stored actions
3. Check for execute/undo or do/rollback method pairs

# Context & Application

The source uses a database migration example: `create table` and `add field` operations are encapsulated as commands, each knowing how to undo itself (`drop table`, `remove field`). A `Schema` struct acts as the invoker, collecting commands and executing them in order or rolling them back in reverse order.

The source notes that `actix` uses trait objects "when it registers a handler function for routes" as a real-world application of this pattern.

The discussion highlights a key trade-off: "If our commands are small and may be defined as functions or passed as a closure then using function pointers might be preferable since it does not exploit dynamic dispatch. But if our command is a whole struct with a bunch of functions and variables defined as separated module then using trait objects would be more suitable."

# Examples

**Example 1** (Ch. 2, "Command" -- Trait Objects): A `Migration` trait defines `execute` and `rollback` methods returning `&str`. Concrete types `CreateTable` and `AddField` implement the trait. A `Schema` stores `Vec<Box<dyn Migration>>` and provides `execute()` (forward iteration) and `rollback()` (reverse iteration with `.rev()`).

**Example 2** (Ch. 2, "Command" -- Function Pointers): A `Command` struct holds two `fn() -> String` pointers. `Schema` stores `Vec<Command>`. At the call site, both closures (`|| "create table".to_string()`) and named functions (`add_field`, `remove_field`) can be passed, since function pointers implement `Fn`, `FnMut`, and `FnOnce`.

**Example 3** (Ch. 2, "Command" -- `Fn` Trait Objects): `Migration<'a>` is defined as `Box<dyn Fn() -> &'a str>`. `Schema<'a>` stores separate `executes` and `rollbacks` vectors. The `add_migration` method accepts generic closures with `E: Fn() -> &'a str + 'static` bounds.

# Relationships

## Builds Upon
- None explicitly

## Enables
- None explicitly

## Related
- **strategy-pattern** -- both patterns encapsulate behaviour, but Command focuses on deferred execution and undo, while Strategy focuses on interchangeable algorithms
- **interpreter-pattern** -- both may use trait objects to encapsulate different operations

## Contrasts With
- **strategy-pattern** -- Strategy selects an algorithm at configuration time, while Command stores sequences of actions for later execution and potential rollback

# Common Errors

- **Error**: Using dynamic dispatch (trait objects) for simple, small commands where function pointers would suffice.
  **Correction**: "If our commands are small and may be defined as functions or passed as a closure then using function pointers might be preferable since it does not exploit dynamic dispatch."

- **Error**: Forgetting to reverse the iterator when implementing rollback.
  **Correction**: Use `.rev()` on the iterator to process commands in reverse order for rollback, as shown in all three approaches.

# Common Confusions

- **Confusion**: Thinking function pointers and closures are incompatible in the function pointer approach.
  **Clarification**: "Function pointers implement all three traits `Fn`, `FnMut`, and `FnOnce` we could as well pass and store closures instead of function pointers." Both can be used interchangeably where the signature matches.

- **Confusion**: Thinking trait objects are always the best approach for Command in Rust.
  **Clarification**: Rust offers three distinct approaches with different trade-offs. "As performance, there is always a trade-off between performance and code simplicity and organisation. Static dispatch gives faster performance, while dynamic dispatch provides flexibility."

# Source Reference

Chapter 2: Design Patterns, "Command" section under Behavioural Patterns. Three approaches are presented: "Using trait objects," "Using function pointers," and "Using `Fn` trait objects." The Discussion section compares the approaches and references `actix` as a real-world example.

# Verification Notes

- Definition source: Direct quotation from the "Description" subsection of "Command"
- Key Properties: Derived from all three approach sections and the Discussion
- Confidence rationale: HIGH -- the source provides three complete, runnable code examples with detailed discussion of trade-offs
- Uncertainties: None for the pattern itself; the actix reference is mentioned but not elaborated
- Cross-reference status: strategy-pattern is in this extraction set; constructor-idiom is from Agent 1 (idioms)
