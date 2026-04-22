---
concept: Fold Pattern
slug: fold-pattern
category: creational-pattern
subcategory: null
tier: advanced
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "02-design-patterns"
chapter_number: 2
pdf_page: null
section: "Fold"
extraction_confidence: high
aliases:
  - "folder pattern"
  - "tree fold"
  - "recursive data structure fold"
prerequisites:
  - visitor-pattern
extends: []
related:
  - visitor-pattern
  - strategy-pattern
contrasts_with:
  - visitor-pattern
answers_questions:
  - "How do I transform a recursive data structure into a new one in Rust?"
  - "How do I map over an AST or tree while producing a new tree?"
  - "What is the difference between fold and visitor in Rust?"
---

# Quick Definition

The Fold pattern runs an algorithm over each item in a collection of data (typically a recursive/tree structure like an AST) to produce a new item per node, creating a whole new collection. It separates traversal logic from per-node transformation, following the functional programming tradition of immutable transformation over in-place mutation.

# Core Definition

"Run an algorithm over each item in a collection of data to create a new item, thus creating a whole new collection." A trait defines `fold_*` methods for each node type with default implementations that recursively fold children. Concrete implementations override specific `fold_*` methods to customize transformation while inheriting default traversal for unchanged node types. The pattern is used extensively in the Rust compiler. (Ch. 2, "Fold")

# Prerequisites

- **visitor-pattern** -- the fold pattern is closely related to the visitor; understanding visitor traversal helps distinguish fold's creation of new data from visitor's in-place operation

# Key Properties

1. A `Folder` trait defines one `fold_*` method per node type in the data structure
2. Default implementations recursively fold children, so concrete folders only override nodes they care about
3. Each `fold_*` method returns a new node, producing a transformed copy of the data structure
4. Leaf node defaults typically return the node unchanged; inner node defaults reconstruct by folding children
5. The original data structure can be consumed (owned pointers), borrowed (requiring clones), or reference-counted (best of both worlds)
6. The pattern favors immutability: fresh data structures rather than in-place mutation

# Construction / Recognition

## To Implement the Fold Pattern:
1. Define the recursive data structure (e.g., an AST with `Stmt`, `Expr`, `Name` types)
2. Define a `Folder` trait with one `fold_*` method per node type
3. Provide default implementations that recursively fold children and reconstruct parent nodes
4. For leaf nodes, the default can simply return the node unchanged
5. Implement the trait for a concrete folder struct, overriding only the node types that need transformation
6. The folder struct may carry mutable state between nodes

## To Recognize the Pattern:
1. A trait with `fold_*` methods that return new nodes of the same (or similar) type
2. Default methods that recurse through the data structure
3. The input data structure is consumed or borrowed; a new structure is produced

# Context & Application

The fold pattern is common in functional languages and aligns with Rust's preference for immutability. "Using fresh data structures, rather than mutating old ones, makes reasoning about the code easier in most circumstances."

The pattern appears extensively in the Rust compiler itself, where "folder" is used for AST-to-HIR transformations and similar passes. The source notes the etymology is unclear -- the term is used in the compiler, though the operation resembles a map more than a traditional fold (which reduces a collection to a single value).

The choice of pointer type creates a three-way trade-off: `Box` pointers allow efficient reuse of unchanged nodes but consume the original; borrowed references preserve the original but require cloning even unchanged nodes; reference-counted pointers (`Rc`/`Arc`) give best of both worlds but are less ergonomic.

# Examples

**Example 1** (Ch. 2, "Fold" -- Example): The source defines an AST with `Stmt` (Expr, Let), `Name`, and `Expr` (IntLit, Add, Sub) types. A `Folder` trait provides `fold_name`, `fold_stmt`, and `fold_expr` methods. A `Renamer` struct implements `Folder` by overriding only `fold_name` to replace every name with "foo", using default methods for all other nodes. "The result of running the Renamer on an AST is a new AST identical to the old one, but with every name changed to foo."

**Example 2** (Ch. 2, "Fold" -- Discussion): The source describes folding an AST into a HIR tree: "A folder can also be defined to map one data structure to a different (but usually similar) data structure. For example, we could fold an AST into a HIR tree."

# Relationships

## Builds Upon
- **visitor-pattern** -- fold shares the concept of walking a data structure and performing per-node operations

## Enables
- Compiler passes (AST transformations, lowering to intermediate representations)
- Immutable tree transformations without manual recursion boilerplate

## Related
- **strategy-pattern** -- both separate an algorithm from the data it operates on

## Contrasts With
- **visitor-pattern** -- "the visitor does not create a new data structure nor consume the old one" while fold produces a new structure
- Iterator `fold` -- iterator fold reduces a collection to a single value; this pattern maps a data structure to a new data structure of the same shape

# Common Errors

- **Error**: Forgetting to recursively fold children in a custom `fold_*` override.
  **Correction**: When overriding a `fold_*` method for an inner node, remember to call the appropriate `fold_*` methods on children, or explicitly decide not to recurse.

- **Error**: Using borrowed references when the original is not needed, causing unnecessary cloning.
  **Correction**: If the original data structure is not needed after folding, use owned types (`Box`) for efficiency. Use `Rc`/`Arc` if both preservation and efficiency matter.

# Common Confusions

- **Confusion**: Confusing the fold pattern with Iterator's `fold` method.
  **Clarification**: Iterator `fold` reduces a sequence to a single value. This fold pattern transforms a data structure into a new data structure of the same (or similar) shape -- it is "more like a map than a fold in the usual sense."

- **Confusion**: Thinking fold and visitor are interchangeable.
  **Clarification**: The visitor pattern walks a structure and performs side effects or accumulates a result without creating a new structure. Fold always produces a new (or transformed) data structure.

# Source Reference

Chapter 2: Design Patterns, "Fold" section (Creational Patterns). Includes a complete AST example with `Folder` trait, `Renamer` implementation, and discussion of the efficiency/reusability trade-off between `Box`, borrowed references, and reference-counted pointers.

# Verification Notes

- Definition source: Direct quotation from "Description" subsection
- Key Properties: Derived from the code example and "Discussion" subsection
- Confidence rationale: HIGH -- the source provides a complete code example, clear motivation, and detailed discussion of trade-offs
- Uncertainties: The source itself notes the etymology is unclear and the operation is "more like a map than a fold in the usual sense"
- Cross-reference status: `visitor-pattern` and `strategy-pattern` are from Agent 3's extraction set
