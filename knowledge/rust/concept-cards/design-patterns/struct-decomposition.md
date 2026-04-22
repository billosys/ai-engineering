---
concept: Struct Decomposition for Independent Borrowing
slug: struct-decomposition
category: structural-pattern
subcategory: null
tier: intermediate
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "02-design-patterns"
chapter_number: 2
pdf_page: null
section: "Struct decomposition for independent borrowing"
extraction_confidence: high
aliases:
  - "struct splitting"
  - "decompose struct for borrowing"
  - "independent field borrowing"
prerequisites:
  - clone-to-satisfy-borrow-checker
extends: []
related:
  - newtype-pattern
  - clone-to-satisfy-borrow-checker
contrasts_with: []
answers_questions:
  - "How do I borrow different fields of a struct independently?"
  - "How do I work around the borrow checker when a struct has many fields?"
  - "When should I split a large struct into smaller structs?"
---

# Quick Definition

When a large struct causes borrow checker conflicts -- because borrowing one field prevents independent use of other fields -- decompose it into several smaller structs, then compose them back into the original. Each sub-struct can then be borrowed independently, resolving the conflict while often leading to a better overall design.

# Core Definition

"Sometimes a large struct will cause issues with the borrow checker -- although fields can be borrowed independently, sometimes the whole struct ends up being used at once, preventing other uses. A solution might be to decompose the struct into several smaller structs. Then compose these together into the original struct. Then each struct can be borrowed separately and have more flexible behaviour." The source adds: "This will often lead to a better design in other ways: applying this design pattern often reveals smaller units of functionality." (Ch. 2, "Struct decomposition for independent borrowing")

# Prerequisites

- **clone-to-satisfy-borrow-checker** -- understanding how the borrow checker constrains simultaneous access motivates why decomposition is needed as a more principled alternative to cloning

# Key Properties

1. A large struct is split into multiple smaller structs, each representing a coherent subset of fields
2. The smaller structs are composed back into the original struct as fields
3. Functions that previously took the whole struct now take only the specific sub-structs they need
4. The borrow checker can independently track borrows of each sub-struct field
5. The pattern relies on Rust's ability to borrow struct fields independently (e.g., `a.b` and `a.c` are distinct)
6. The smaller structs often reveal natural units of functionality

# Construction / Recognition

## To Apply Struct Decomposition:
1. Identify a struct where the borrow checker prevents simultaneous access to independent fields
2. Group related fields into smaller, cohesive structs (often as newtype wrappers)
3. Replace the original struct's fields with instances of these smaller structs
4. Update functions to accept only the sub-structs they actually need, rather than the whole struct
5. Borrow sub-struct fields independently through the parent struct

## To Recognize When This Pattern is Needed:
1. Compiler errors about conflicting mutable and immutable borrows on the same struct
2. A function borrows the whole struct but only needs some fields
3. A large struct accumulates many unrelated fields over time

# Context & Application

This pattern is unique to Rust in the sense that other languages without a borrow checker do not require it. However, the source notes that "making smaller units of functionality often leads to cleaner code: a widely acknowledged principle of software engineering, independent of the language."

The pattern relies on the borrow checker's ability to track field borrows independently: "the borrow checker knows that a.b and a.c are distinct and can be borrowed independently, it does not try to borrow all of a." This means the pattern works because Rust tracks borrows at the field level, not the struct level.

The source warns that sometimes the smaller structs may not form good abstractions, producing a worse design -- "that is probably a 'code smell', indicating that the program should be refactored in some way."

# Examples

**Example 1** (Ch. 2, "Struct decomposition" -- problematic code): A `Database` struct with `connection_string: String`, `timeout: u32`, `pool_size: u32`. Taking `&mut db.connection_string` and then calling `print_database(&db)` fails because the mutable borrow of one field conflicts with the immutable borrow of the whole struct.

**Example 2** (Ch. 2, "Struct decomposition" -- solution): The fields are extracted into newtype structs: `ConnectionString(String)`, `Timeout(u32)`, `PoolSize(u32)`. The `Database` struct composes these. `print_database` now takes the three sub-structs individually: `fn print_database(connection_str: ConnectionString, timeout: Timeout, pool_size: PoolSize)`. This allows `&mut db.connection_string` and `db.timeout`/`db.pool_size` to be borrowed independently.

# Relationships

## Builds Upon
- **clone-to-satisfy-borrow-checker** -- decomposition is a more principled alternative to cloning to resolve borrow conflicts

## Enables
- More flexible APIs that accept only the data they need
- Better separation of concerns within large structs

## Related
- **newtype-pattern** -- the sub-structs are often newtypes wrapping a single field

## Contrasts With
- Keeping a monolithic struct and working around borrow checker issues with cloning or `RefCell`

# Common Errors

- **Error**: Decomposing into sub-structs that do not form coherent abstractions.
  **Correction**: The source warns this produces a worse design and is "a 'code smell', indicating that the program should be refactored in some way." Group fields into sub-structs that represent meaningful concepts.

- **Error**: Assuming the borrow checker always requires decomposition for field-level borrowing.
  **Correction**: Rust can borrow individual fields independently in many cases. Decomposition is needed when functions take a reference to the whole struct, not when accessing fields directly.

# Common Confusions

- **Confusion**: Thinking this pattern is needed whenever a struct has many fields.
  **Clarification**: The pattern is specifically for resolving borrow checker conflicts. A large struct with many fields that does not cause borrowing issues does not need decomposition.

- **Confusion**: Thinking this is a workaround or hack for Rust's borrow checker.
  **Clarification**: The source emphasizes it "often leads to a better design in other ways" by revealing natural units of functionality. It is a design improvement, not just a borrow checker workaround.

# Source Reference

Chapter 2: Design Patterns, "Struct decomposition for independent borrowing" section (Structural Patterns). Includes a before/after `Database` example demonstrating borrow checker conflict and resolution through decomposition into `ConnectionString`, `Timeout`, and `PoolSize` newtypes.

# Verification Notes

- Definition source: Direct quotation from "Description" subsection
- Key Properties: Derived from the code examples and "Discussion" subsection
- Confidence rationale: HIGH -- complete code example with before/after, clear motivation, and explicit discussion of trade-offs
- Uncertainties: None
- Cross-reference status: `newtype-pattern` from Agent 3; `clone-to-satisfy-borrow-checker` from Agent 5
