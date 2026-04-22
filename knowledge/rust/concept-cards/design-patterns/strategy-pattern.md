---
concept: Strategy Pattern
slug: strategy-pattern
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
  - "strategy"
  - "policy pattern"
  - "policy-based design"
prerequisites:
  - default-trait
extends: []
related:
  - command-pattern
  - visitor-pattern
  - fold-pattern
contrasts_with:
  - command-pattern
answers_questions:
  - "How do I implement the Strategy pattern in Rust?"
  - "How do Rust traits and closures replace traditional OOP strategy objects?"
  - "When should I use traits vs closures for interchangeable algorithms?"
  - "How does Serde use the Strategy pattern?"
---

# Quick Definition

The Strategy pattern (also called Policy) separates the skeleton of an algorithm from its specific implementations, allowing clients to choose an implementation at use time. In Rust, this is naturally expressed through traits (static dispatch) or closures (inline strategies), and the source notes Rust's trait system makes the traditional OOP pattern nearly unnecessary.

# Core Definition

"The basic idea behind the Strategy pattern is that, given an algorithm solving a particular problem, we define only the skeleton of the algorithm at an abstract level, and we separate the specific algorithm's implementation into different parts. In this way, a client using the algorithm may choose a specific implementation, while the general algorithm workflow remains the same." This achieves separation of concerns through Dependency Inversion: "the abstract specification of the class does not depend on the specific implementation of the derived class, but specific implementation must adhere to the abstract specification." (Rust Design Patterns, Ch. 2: Behavioural Patterns, "Strategy (aka Policy)")

# Prerequisites

- **Default trait** -- understanding Rust traits is essential since the Strategy pattern is fundamentally about trait-based polymorphism

# Key Properties

1. Defines an abstract algorithm skeleton (invariant) separate from concrete implementations (strategies)
2. Clients select a specific strategy without affecting the algorithm workflow
3. Achieves separation of concerns and Dependency Inversion
4. In Rust, traits define the strategy interface (e.g., `trait Formatter`)
5. Concrete strategies implement the trait (e.g., `struct Text`, `struct Json`)
6. The algorithm is generic over the trait: `fn generate<T: Formatter>(g: T, ...)`
7. Closures provide a lightweight alternative for simple strategies
8. Rust's standard library already uses this pattern (e.g., `Option::map` accepts strategy closures)
9. Strategies can be organized as: all in one file, separate modules, compiler feature flags, or separate crates

# Construction / Recognition

## Trait-Based Approach:
1. Define a trait representing the strategy interface (e.g., `trait Formatter { fn format(&self, data: &Data, buf: &mut String); }`)
2. Implement the trait for each concrete strategy (e.g., `Text`, `Json`)
3. Write the algorithm as a generic function bounded by the trait: `fn generate<T: Formatter>(g: T, ...)`
4. Clients pass the desired strategy: `Report::generate(Json, &mut s)`

## Closure-Based Approach:
1. Define the algorithm to accept a closure: `fn add<F>(x: u8, y: u8, f: F) -> u8 where F: Fn(u8, u8) -> u8`
2. Clients pass closures or function pointers as strategies: `Adder::add(4, 5, |x, y| x + y)`
3. No trait definition or struct needed for simple strategies

## To Recognize the Pattern:
1. Look for a trait defining an operation that has multiple implementations
2. Check for generic functions bounded by that trait
3. Look for closures passed as algorithm selectors

# Context & Application

The source presents a report generation example where `Report::generate` is generic over `Formatter`. Two strategies (`Text` and `Json`) implement `Formatter` differently. The key advantage is separation of concerns: "`Report` does not know anything about specific implementations of `Json` and `Text`, whereas the output implementations does not care about how data is preprocessed, stored, and fetched."

The source introduces a closure-based alternative with `Adder::add`, demonstrating that Rust closures can serve as lightweight strategies without defining traits. It then shows that Rust's standard library already uses this idiom: `Option::map` accepts a closure strategy for transforming the contained value.

Serde is highlighted as "a good example of the `Strategy` pattern in action": implementing `Serialize` and `Deserialize` allows full customization, and "we could easily swap `serde_json` with `serde_cbor` since they expose similar methods."

The source also notes that the YAGNI introduction to the chapter states "there is no need for the strategy pattern in Rust because we can just use traits" -- meaning the OOP ceremonial version is unnecessary, but the underlying concept maps directly to Rust's trait system.

# Examples

**Example 1** (Ch. 2, "Strategy" -- Trait-Based): `trait Formatter` defines `format(&self, data: &Data, buf: &mut String)`. `Text` formats as `"key value\n"` lines; `Json` formats as a JSON array. `Report::generate` is generic: `fn generate<T: Formatter>(g: T, s: &mut String)`. Clients call `Report::generate(Text, &mut s)` or `Report::generate(Json, &mut s)`.

**Example 2** (Ch. 2, "Strategy" -- Closures): `Adder::add` accepts a closure `F: Fn(u8, u8) -> u8`. Three strategies are defined as closures: `arith_adder = |x, y| x + y`, `bool_adder` (returns 1 if either input is 1), and `custom_adder = |x, y| 2 * x + y`. No trait or struct is needed.

**Example 3** (Ch. 2, "Strategy" -- Standard Library): `Option::map` demonstrates built-in Strategy usage: `val.map(len_strategy)` applies a `|s: &str| s.len()` closure, while `val.map(first_byte_strategy)` applies `|s: &str| s.bytes().next().unwrap()`.

# Relationships

## Builds Upon
- None explicitly

## Enables
- None explicitly

## Related
- **command-pattern** -- both encapsulate behaviour as objects, but Strategy selects algorithms while Command stores actions for deferred execution
- **visitor-pattern** -- visitors separate algorithms from data structures, similar to how Strategy separates algorithm implementations from the algorithm skeleton
- **fold-pattern** -- fold applies a function across a data structure, often using Strategy-like function parameters

## Contrasts With
- **command-pattern** -- Strategy swaps algorithms at the point of use; Command queues actions for later execution and potential rollback

# Common Errors

- **Error**: Creating a full trait + struct hierarchy for a strategy that could be a simple closure.
  **Correction**: For simple, stateless strategies, closures are more ergonomic and require less boilerplate. Reserve trait-based strategies for when strategies need state or multiple methods.

- **Error**: Tightly coupling the algorithm to a specific strategy, defeating the pattern's purpose.
  **Correction**: "The main advantage is separation of concerns." The algorithm should depend only on the trait interface, not on any concrete strategy.

# Common Confusions

- **Confusion**: Thinking Strategy is unnecessary in Rust because YAGNI says "there is no need for the strategy pattern."
  **Clarification**: The YAGNI statement means the OOP ceremonial version (with abstract base classes and factory methods) is unnecessary. The concept naturally maps to Rust traits and closures -- the pattern is alive, just expressed idiomatically.

- **Confusion**: Thinking trait-based and closure-based approaches are equivalent.
  **Clarification**: Trait-based strategies support multiple methods, associated types, and stateful implementations. Closures work for single-function, lightweight strategies. "For each strategy there must be implemented at least one module" with traits, whereas closures can be defined inline.

# Source Reference

Chapter 2: Design Patterns, "Strategy (aka Policy)" section under Behavioural Patterns. Includes a trait-based report generation example, a closure-based `Adder` example, a standard library `Option::map` example, and references to Serde, the Strategy Wikipedia article, Dependency Injection, Policy Based Design, and a TCP server implementation blog post.

# Verification Notes

- Definition source: Direct quotation from the "Description" subsection of "Strategy (aka Policy)"
- Key Properties: Derived from both approaches (trait-based and closure-based), the Discussion subsection, and the YAGNI introduction
- Confidence rationale: HIGH -- the source provides multiple complete examples, real-world references (Serde, actix), and explicit discussion of advantages/disadvantages
- Uncertainties: None for the pattern itself
- Cross-reference status: command-pattern and visitor-pattern are in this extraction set; default-trait is from Agent 1 (idioms); fold-pattern is from Agent 4 (creational/structural)
