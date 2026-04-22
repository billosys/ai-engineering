---
concept: Visitor Pattern
slug: visitor-pattern
category: behavioural-pattern
subcategory: null
tier: advanced
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "02-design-patterns"
chapter_number: 2
pdf_page: null
section: "Behavioural Patterns"
extraction_confidence: high
aliases:
  - "visitor"
  - "double dispatch"
  - "AST visitor"
prerequisites:
  - strategy-pattern
extends: []
related:
  - interpreter-pattern
  - fold-pattern
  - strategy-pattern
contrasts_with:
  - fold-pattern
answers_questions:
  - "How do I implement the Visitor pattern in Rust?"
  - "How do I separate traversal from operations on heterogeneous data?"
  - "What are walk functions and how do they relate to visitors in Rust?"
  - "When should I use Visitor vs Fold in Rust?"
---

# Quick Definition

The Visitor pattern encapsulates an algorithm that operates over a heterogeneous collection of objects, allowing multiple algorithms to be written over the same data without modifying it. In Rust, this is typically implemented with a `Visitor<T>` trait containing `visit_*` methods for each data variant, with optional `walk_*` free functions to factor out traversal logic.

# Core Definition

"A visitor encapsulates an algorithm that operates over a heterogeneous collection of objects. It allows multiple different algorithms to be written over the same data without having to modify the data (or their primary behaviour). Furthermore, the visitor pattern allows separating the traversal of a collection of objects from the operations performed on each object." (Rust Design Patterns, Ch. 2: Behavioural Patterns, "Visitor")

# Prerequisites

- **Strategy pattern** -- the Visitor pattern uses the same principle of separating algorithm from structure through traits; understanding trait-based polymorphism is essential

# Key Properties

1. Operates over heterogeneous data (different types in a collection, typically an AST)
2. Multiple algorithms can be defined over the same data without modifying the data types
3. Separates traversal logic from the operations performed on each node
4. In Rust, a `Visitor<T>` trait defines `visit_*` methods for each data variant
5. The generic parameter `T` allows different visitors to produce different result types
6. `walk_*` free functions can factor out shared traversal logic, providing default traversal
7. Visitors can be stateful (the trait takes `&mut self`)
8. In Rust, `walk_*` functions replace the OOP `accept` method pattern
9. Useful for AST processing: interpreters, type checkers, code generators, etc.

# Construction / Recognition

## To Implement a Visitor:
1. Define the data types (e.g., AST nodes): `enum Stmt`, `enum Expr`, `struct Name`
2. Define a `Visitor<T>` trait with a `visit_*` method for each data variant
3. Implement the trait for each concrete algorithm (e.g., `Interpreter`)
4. In each `visit_*` method, match on the variant and recursively visit children
5. Optionally, define `walk_*` free functions that handle traversal and delegate to visitor methods

## Factoring Out Traversal with `walk_*`:
1. When `visit_*` methods return void, traversal logic is often identical across visitors
2. Define `pub fn walk_expr(visitor: &mut Visitor, e: &Expr)` that matches on variants
3. For leaf nodes (e.g., `IntLit`), do nothing
4. For composite nodes (e.g., `Add`, `Sub`), call `visitor.visit_expr` on each child
5. Provide noop default methods in the visitor trait so visitors only override what they need

## To Recognize the Pattern:
1. Look for a trait with multiple `visit_*` methods, one per data variant
2. Check for `walk_*` free functions that handle recursive traversal
3. Look for enum-based data structures (ASTs) with multiple variants

# Context & Application

The source demonstrates the pattern with an AST for a simple expression language: `Stmt` (with `Expr` and `Let` variants), `Expr` (with `IntLit`, `Add`, `Sub`), and `Name`. A `Visitor<T>` trait defines `visit_name`, `visit_stmt`, and `visit_expr`. An `Interpreter` implementation evaluates expressions to `i64`.

The source notes that "one could implement further visitors, for example a type checker, without having to modify the AST data." This is the core benefit -- new algorithms are added as new trait implementations, not modifications to existing data types.

For the Rust-idiomatic approach, the source presents `walk_*` functions as a replacement for the OOP `accept` method: "In Rust, the common way to do this is to provide `walk_*` functions for each datum." The `walk_expr` example shows traversal logic factored into a free function that calls `visitor.visit_expr` for composite nodes.

The source notes the visitor can be stateful: the trait takes `&mut self`, allowing information to be communicated between nodes during traversal. This distinguishes it from a purely functional approach.

# Examples

**Example 1** (Ch. 2, "Visitor" -- AST Interpreter): An AST with `Stmt` and `Expr` enums. `Visitor<T>` trait has `visit_name`, `visit_stmt`, `visit_expr`. `Interpreter` implements `Visitor<i64>`: `visit_expr` matches `IntLit(n) => n`, `Add(lhs, rhs) => self.visit_expr(lhs) + self.visit_expr(rhs)`, `Sub(lhs, rhs) => self.visit_expr(lhs) - self.visit_expr(rhs)`.

**Example 2** (Ch. 2, "Visitor" -- `walk_*` Functions): `pub fn walk_expr(visitor: &mut Visitor, e: &Expr)` matches on `Expr` variants. For `IntLit(_)`, it does nothing. For `Add(lhs, rhs)` and `Sub(lhs, rhs)`, it calls `visitor.visit_expr(lhs)` and `visitor.visit_expr(rhs)`. This factors out traversal so individual visitors only need to implement node-specific logic.

# Relationships

## Builds Upon
- None explicitly

## Enables
- None explicitly

## Related
- **interpreter-pattern** -- interpreters often use visitors to walk ASTs; the Visitor example itself is an AST interpreter
- **strategy-pattern** -- both use traits to swap algorithm implementations; Visitor specializes this for heterogeneous data traversal
- **fold-pattern** -- fold is similar to visitor but "produces a new version of the visited data structure" rather than computing a result in-place

## Contrasts With
- **fold-pattern** -- "The fold pattern is similar to visitor but produces a new version of the visited data structure." Visitor computes a result (or modifies state) while traversing; Fold produces a transformed copy of the data

# Common Errors

- **Error**: Mixing traversal logic into every visitor implementation, duplicating code.
  **Correction**: Factor traversal into `walk_*` free functions and provide noop default methods. Individual visitors then only override the methods where they need custom behavior.

- **Error**: Making the visitor immutable (`&self`) when it needs to accumulate state across nodes.
  **Correction**: The trait uses `&mut self` because "using a visitor object (rather than a functional approach) allows the visitor to be stateful and thus communicate information between nodes."

# Common Confusions

- **Confusion**: Thinking Visitor is only useful for ASTs.
  **Clarification**: The source states the pattern "is useful anywhere that you want to apply an algorithm to heterogeneous data." ASTs are the common case, but any heterogeneous collection benefits from the pattern.

- **Confusion**: Expecting Rust visitors to use the `accept` method from OOP implementations.
  **Clarification**: "In other languages (e.g., Java) it is common for data to have an `accept` method which performs the same duty." In Rust, `walk_*` free functions replace `accept`, which is more idiomatic because it keeps traversal logic outside the data types.

# Source Reference

Chapter 2: Design Patterns, "Visitor" section under Behavioural Patterns. Includes an AST definition with `Stmt`/`Expr`/`Name`, a `Visitor<T>` trait, an `Interpreter` implementation, a `walk_expr` function example, and a reference to the Fold pattern as a related alternative.

# Verification Notes

- Definition source: Direct quotation from the "Description" subsection of "Visitor"
- Key Properties: Derived from the example code, the Discussion subsection, and the Motivation subsection
- Confidence rationale: HIGH -- the source provides complete (though `ignore`-tagged) code examples with clear discussion of Rust-specific idioms (walk functions vs accept methods)
- Uncertainties: The example code is marked `rust,ignore` (not fully compilable as shown), but the pattern description is complete
- Cross-reference status: strategy-pattern and interpreter-pattern are in this extraction set; fold-pattern is from Agent 4 (creational/structural)
