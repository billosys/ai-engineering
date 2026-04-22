---
concept: Design Principles Overview
slug: design-principles-overview
category: design-principles
subcategory: null
tier: foundational
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "Additional Resources"
chapter_number: 5
pdf_page: null
section: "Design principles"
extraction_confidence: medium
aliases:
  - "SOLID principles"
  - "software design principles"
  - "DRY KISS SOLID"
prerequisites: []
extends: []
related:
  - strategy-pattern
  - newtype-pattern
  - builder-pattern
contrasts_with: []
answers_questions:
  - "What are the key software design principles referenced in Rust Design Patterns?"
  - "How do SOLID, DRY, and KISS apply to Rust?"
  - "What design principles complement Rust's pattern language?"
---

# Quick Definition

A survey of established software design principles that complement Rust's design patterns. These include SOLID (five object-oriented principles), composition over inheritance (CRP), DRY, KISS, Law of Demeter, Design by Contract, Encapsulation, Command-Query Separation, Principle of Least Astonishment, and several principles from Bertrand Meyer's Object-Oriented Software Construction.

# Core Definition

The source provides a reference catalog of design principles that inform good software design across languages, including Rust. While these principles originated in object-oriented contexts, they apply broadly. The catalog covers:

**SOLID:**
- **Single Responsibility Principle (SRP)**: A class should only have a single responsibility; only changes to one part of the specification should affect the class.
- **Open/Closed Principle (OCP)**: Software entities should be open for extension, but closed for modification.
- **Liskov Substitution Principle (LSP)**: Objects should be replaceable with instances of their subtypes without altering program correctness.
- **Interface Segregation Principle (ISP)**: Many client-specific interfaces are better than one general-purpose interface.
- **Dependency Inversion Principle (DIP)**: Depend upon abstractions, not concretions.

**Other Principles:**
- **Composition over Inheritance (CRP)**: Classes should favor polymorphic behavior and code reuse by composition over inheritance.
- **DRY**: Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.
- **KISS**: Most systems work best if kept simple; simplicity should be a key goal in design.
- **Law of Demeter (LoD)**: A given object should assume as little as possible about the structure of anything else, following the principle of information hiding.
- **Design by Contract (DbC)**: Define formal, precise, and verifiable interface specifications with preconditions, postconditions, and invariants.

# Prerequisites

None -- these are language-agnostic design principles.

# Key Properties

1. SOLID principles address class/module-level design: single responsibility, open/closed, substitutability, interface segregation, and dependency inversion
2. Composition over inheritance is particularly relevant to Rust, which does not support struct inheritance and favors composition with traits
3. DRY and KISS are meta-principles about reducing redundancy and complexity
4. Law of Demeter limits coupling by restricting what an object should know about other objects' internals
5. Design by Contract formalizes interfaces with preconditions, postconditions, and invariants
6. Encapsulation bundles data with methods and restricts direct access to internal state
7. Command-Query Separation (CQS) states that functions should not produce abstract side effects; only commands (procedures) should have side effects
8. Principle of Least Astonishment (POLA) states that components should behave in ways users expect
9. Meyer's principles (from Object-Oriented Software Construction) add: Linguistic-Modular-Units, Self-Documentation, Uniform-Access, Single-Choice, and Persistence-Closure

# Construction / Recognition

## Applying These Principles in Rust:

- **SRP** maps to keeping modules and structs focused on a single concern
- **OCP** maps to using traits for extensibility without modifying existing code
- **LSP** maps to ensuring trait implementations honor the trait's contract
- **ISP** maps to defining small, focused traits rather than large "god traits"
- **DIP** maps to depending on traits (abstractions) rather than concrete types
- **CRP** is naturally enforced by Rust, which has no struct inheritance -- composition with embedded structs and trait delegation is the standard approach
- **CQS** aligns with Rust's distinction between `&self` (query) and `&mut self` (command) methods
- **POLA** aligns with Rust's preference for explicit over implicit behavior

# Context & Application

The source presents these principles as a brief reference catalog in the "Additional Resources" chapter, providing one-line to one-paragraph definitions with Wikipedia links. These principles are not Rust-specific but form the intellectual foundation that many of the patterns and anti-patterns in the book build upon. For example, the Deref polymorphism anti-pattern violates the Principle of Least Astonishment; the strategy pattern implements the Open/Closed Principle; and Rust's trait system naturally supports Interface Segregation and Dependency Inversion.

# Examples

**Example 1** (Ch. 5, "Design principles", CQS): Bertrand Meyer's formulation: "Functions should not produce abstract side effects...only commands (procedures) will be permitted to produce side effects." In Rust, this maps to the convention that `&self` methods are queries (no mutation) and `&mut self` methods are commands (may mutate), enforced by the borrow checker.

**Example 2** (Ch. 5, "Design principles", Uniform-Access): Meyer's principle: "All services offered by a module should be available through a uniform notation, which does not betray whether they are implemented through storage or through computation." In Rust, this is achieved through methods that may compute a value or return a stored field, with the caller unable to distinguish between the two.

# Relationships

## Builds Upon
- General software engineering knowledge

## Enables
- Understanding the rationale behind specific Rust design patterns and anti-patterns
- Making principled design decisions when Rust-specific patterns do not directly apply

## Related
- **strategy-pattern** -- implements the Open/Closed Principle
- **newtype-pattern** -- supports encapsulation and type safety
- **builder-pattern** -- separates construction from representation (SRP)

## Contrasts With
- None in this extraction set

# Common Errors

- **Error**: Applying OO inheritance-based interpretations of these principles directly to Rust (e.g., thinking LSP requires class inheritance).
  **Correction**: In Rust, these principles apply through traits and composition. LSP means trait implementations should honor the trait's documented contract. OCP means extending behavior via new trait implementations, not modifying existing ones.

- **Error**: Over-applying DRY by creating premature abstractions.
  **Correction**: DRY should be balanced with KISS. Sometimes a small amount of duplication is preferable to a complex abstraction that couples unrelated concerns.

# Common Confusions

- **Confusion**: Thinking these principles are irrelevant to Rust because they originated in OO contexts.
  **Clarification**: While the terminology is OO (classes, interfaces), the underlying ideas about modularity, coupling, and abstraction apply universally. Rust's traits, modules, and ownership system provide different mechanisms to achieve the same goals.

- **Confusion**: Treating these principles as absolute rules.
  **Clarification**: They are guidelines and heuristics, not laws. The source presents them as a reference catalog of principles that inform design decisions, not as mandatory requirements.

# Source Reference

Chapter 5: Additional Resources, "Design principles" section. The source provides a catalog format with principle names, Wikipedia links, and brief definitions (one sentence to one paragraph each). Many definitions quote Bertrand Meyer's Object-Oriented Software Construction.

# Verification Notes

- Definition source: Direct quotations from the source's brief definitions
- Key Properties: Compiled from all principles listed in the section
- Confidence rationale: MEDIUM -- the source material is a brief reference catalog rather than an in-depth treatment; definitions are accurate but shallow
- Uncertainties: The Rust-specific applications in "Construction / Recognition" are inferred interpretations, not stated in the source
- Cross-reference status: `strategy-pattern`, `newtype-pattern`, and `builder-pattern` reference cards from other extraction agents
