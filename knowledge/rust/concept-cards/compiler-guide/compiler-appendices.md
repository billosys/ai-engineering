---
concept: "Appendices: Glossary, Background Topics, and Resources"
slug: compiler-appendices
category: compiler-internals
subcategory: reference
tier: intermediate
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "26-appendices"
chapter_number: 26
pdf_page: null
section: "Background topics, Glossary, Code index, Compiler lecture series, Rust bibliography, Humor"
extraction_confidence: high
aliases:
  - "compiler glossary"
  - "control-flow graph"
  - "dataflow analysis"
  - "de Bruijn index"
  - "monomorphization glossary"
  - "codegen unit"
  - "ICE"
  - "DefId"
  - "TyCtxt"
  - "HIR"
  - "MIR"
  - "free vs bound variables"
  - "variance"
prerequisites: []
extends: []
related:
  - compiler-mir-optimizations
  - compiler-code-generation
  - compiler-debug-info
  - compiler-backends
contrasts_with: []
answers_questions:
  - "What is a control-flow graph and how does it relate to MIR?"
  - "How does dataflow analysis work in the Rust compiler?"
  - "What is a de Bruijn index and why does rustc use them?"
  - "What do common compiler terms like ICE, DefId, HIR, MIR, TyCtxt mean?"
  - "What is the difference between free and bound variables?"
  - "What is a codegen unit (CGU)?"
  - "What is monomorphization in the glossary sense?"
  - "What are the key data structures in the Rust compiler?"
  - "Where can I find compiler lectures and educational videos?"
  - "What academic papers influenced Rust's design?"
---

# Quick Definition

The appendices provide essential reference material for compiler contributors: background topics explaining fundamental concepts (control-flow graphs, dataflow analysis, de Bruijn indices, variance, free vs bound variables), a comprehensive glossary of ~80 compiler terms, a code index mapping key data structures to their declarations, a curated list of compiler lectures and videos, and an annotated bibliography of papers that influenced Rust's design.

# Core Definition

The background topics explain foundational concepts: "A control-flow graph is structured as a set of basic blocks connected by edges. The key idea of a basic block is that it is a set of statements that execute 'together' -- that is, whenever you branch to a basic block, you start at the first statement and then execute all the remainder." (Ch. 26, Background topics)

On dataflow analysis: "Dataflow analysis is a type of static analysis that is common in many compilers. It describes a general technique, rather than a particular analysis. The basic idea is that we can walk over a control-flow graph and keep track of what some value could be. At the end of the walk, we might have shown that some claim is true or not necessarily true." (Ch. 26, Background topics)

The glossary defines the vocabulary of compiler development: terms from "1-ZST" (one-aligned zero-sized type) through "ZST" (zero-sized type), covering all the abbreviations, data structures, and concepts that appear throughout the guide.

# Prerequisites

None -- this chapter is designed as a reference for all levels of compiler contributors.

# Key Properties

1. **Control-flow graph (CFG)**: Basic blocks contain sequential statements ending with a terminator; loops appear as cycles; `break` translates to a path out of the cycle; rustc performs dataflow analysis over the MIR CFG
2. **Dataflow analysis**: Tracks properties at each CFG point; when a block has multiple parents, a merge function combines values (e.g., "and" for must-be-initialized analysis); supports both forward and backward analysis
3. **De Bruijn indices**: Represent variable binding using only integers; invariant under variable renaming; rustc uses them to represent generic types; index counts levels up from the use site to the binding site
4. **Variance**: Determines how changes to a generic parameter affect subtyping; e.g., `Vec<T>` is covariant in `T`
5. **Free vs bound variables**: A bound variable is declared within an expression (e.g., `|a| a * 2` binds `a`); a free variable references something outside (e.g., `a + b` where `a` and `b` are defined externally); applies to both variables and lifetime regions
6. **Key glossary terms -- compiler IRs**: AST (abstract syntax tree, reflects surface syntax), HIR (high-level IR after desugaring), MIR (mid-level IR for borrowck and codegen), LLVM IR (for codegen backend)
7. **Key glossary terms -- identifiers**: `DefId` (unique definition identifier), `HirId` (HIR node identifier), `NodeId` (AST node, being phased out), `BodyId` (refers to function/const body)
8. **Key glossary terms -- types**: `Ty<'tcx>` (internal type representation), `TyCtxt<'tcx>` (central data structure, the "typing context"), `ParamEnv` (information about generic parameters)
9. **Key glossary terms -- compilation concepts**: ICE (internal compiler error), codegen unit (CGU, unit of LLVM parallel compilation and incremental reuse), monomorphization (stamping out generic code for concrete types), LTO (link-time optimization, ThinLTO variant), CTFE (compile-time function evaluation)
10. **Key glossary terms -- advanced**: niche (invalid bit patterns usable for layout optimizations, e.g., `NonZero*`), discriminant (value encoding active enum variant), tag (runtime encoding of discriminant, either direct or via niche), NLL (non-lexical lifetimes), placeholder (handling of "for-all" types)
11. **Code index**: Maps 18 key structs to their chapters and source declarations, including `Compiler`, `TyCtxt`, `Ty`, `Span`, `Session`, `SourceMap`, `TokenStream`
12. **Bibliography categories**: Type system papers (region-based memory, traits, uniqueness), concurrency papers (work stealing, scheduling, synchronization), papers about Rust (RustBelt, Oxide, Patina, Servo), and recommended compiler textbooks

# Construction / Recognition

## To Look Up a Compiler Term:
1. Check the glossary table for the term or its abbreviation
2. Follow the linked chapter for deeper explanation
3. Deprecated terms are marked with a thumbs-down emoji (e.g., "trans" renamed to "codegen", "substs" renamed to "generic arguments")

## To Find a Key Data Structure:
1. Consult the Code Index table for the struct name
2. The table provides: kind, short description, relevant chapter, and direct link to source declaration
3. Key structures: `TyCtxt` (central context), `Ty` (type representation), `Span` (source location), `Session` (compilation session)

## To Understand a Dataflow Analysis:
1. Identify the property being tracked (e.g., "is variable initialized?")
2. Walk the CFG from entry, updating the property at each statement
3. At merge points (blocks with multiple predecessors), apply the merge function
4. "and" merge for "must" properties (conservative); "or" merge for "may" properties

# Context & Application

The appendices serve as the compiler contributor's desk reference. The glossary alone defines approximately 80 terms, many with links to relevant chapters. Understanding these terms is essential for reading compiler source code, participating in compiler discussions on Zulip, and contributing patches.

The background topics section is particularly valuable for contributors coming from outside the compiler community. Control-flow graphs and dataflow analysis are foundational concepts that underpin much of MIR-based analysis (borrow checking, initialization checking, liveness analysis). The de Bruijn index explanation helps make sense of how generics are represented internally. The free-vs-bound variable distinction is critical for understanding lifetime regions in the borrow checker.

The bibliography is historically significant: papers like "Region based memory management in Cyclone" and "Traits: composable units of behavior" directly influenced Rust's ownership system and trait design. The "Papers about Rust" section documents the growing academic analysis of Rust itself, from early formalizations (Patina) through the comprehensive RustBelt proof of Rust's type system soundness.

The lecture series provides video explanations from compiler team members on topics ranging from type systems and closures to async-await internals and Cranelift. These are invaluable for visual/auditory learners or for understanding topics that are difficult to convey in text.

# Examples

**Example 1** (Ch. 26, CFG for an if statement): Rust code:
```rust
a = 1;
if some_variable { b = 1; } else { c = 1; }
d = 1;
```
Compiles to four MIR basic blocks: BB0 (assign `a`, branch), BB1 (`b = 1`, goto BB3), BB2 (`c = 1`, goto BB3), BB3 (`d = 1`).

**Example 2** (Ch. 26, Dataflow analysis for initialization): Tracking whether `x` is initialized:
```txt
 Init (A) -- init=false      init=false (else path)
    |   \                         |
    |    B: x = 1 -- init=true   |
    |      /                     |
  C: dbg!(x) -- merge(false, true) = false => ERROR
```
Because the "else" path from A reaches C without initializing `x`, the merge function ("and") produces `init=false`, and the compiler reports "x may not be initialized before use."

**Example 3** (Ch. 26, De Bruijn indices for closures):
```rust
|x| {
    f(x)     // de Bruijn index of x is 1 (bound 1 level up)
    |y| {
        g(x, y) // index of x is 2 (bound 2 levels up)
                 // index of y is 1 (bound 1 level up)
    }
}
```

# Relationships

## Builds Upon
- General compiler theory (CFGs, dataflow, type theory)
- The entire Rust compiler architecture (the glossary references all chapters)

## Enables
- Onboarding new compiler contributors (vocabulary and foundational concepts)
- Cross-referencing compiler source code (Code Index)
- Understanding compiler design decisions (bibliography)

## Related
- **compiler-mir-optimizations** -- uses CFG and dataflow analysis concepts
- **compiler-code-generation** -- references codegen units, monomorphization, LTO
- **compiler-debug-info** -- references DWARF, span, and source mapping concepts
- **compiler-backends** -- references library formats, metadata, and LLVM

## Contrasts With
- Language-level documentation (the glossary covers compiler internals, not user-facing language features)
- The Rust Reference glossary (which covers user-facing terms; this glossary covers implementor terms)

# Common Errors

- **Error**: Using the deprecated term "trans" for code generation.
  **Correction**: The glossary marks "trans" with a deprecation indicator: "Short for translation, the code to translate MIR into LLVM IR. Renamed to codegen."

- **Error**: Using "substs" or "substitutions" for generic arguments.
  **Correction**: "Nowadays referred to as the list of generic arguments in the compiler (but note that strictly speaking these two concepts differ, see the literature)."

- **Error**: Confusing discriminant and variant index.
  **Correction**: The discriminant is "the underlying value associated with an enum variant" (can be overridden by user, e.g., `True = 42`). The variant index is "purely internal," assigning indices starting at 0.

# Common Confusions

- **Confusion**: Thinking a zero-sized type (ZST) has no values.
  **Clarification**: "Since 2^0 = 1, such types can have exactly one value. For example, () (unit) is a ZST." An uninhabited type (like `enum Foo {}`) has zero values, which is different from a ZST.

- **Confusion**: Thinking fat pointers and wide pointers are different concepts.
  **Clarification**: The glossary defines "fat pointer" with note: "'Fat pointers' are also known as 'wide pointers', and 'double pointers.'" All three terms refer to a two-word value carrying an address plus metadata.

- **Confusion**: Thinking dataflow analysis can prove properties absolutely.
  **Clarification**: Dataflow analysis must be conservative at merge points because "we cannot know statically" which path is taken at runtime (due to Rice's Theorem). It proves "must" or "may" properties, not exact behavior.

# Source Reference

Chapter 26: Background topics (control-flow graphs with MIR examples, dataflow analysis with initialization tracking, universally/existentially quantified types, de Bruijn indices, variance, free vs bound variables/regions), Glossary (~80 terms covering IRs, identifiers, types, compilation concepts, deprecated terms), Code Index (18 key data structures with chapters and source links), Compiler Lecture Series (videos on type systems, closures, Chalk, Polonius, Miri, async, code generation), Rust Bibliography (type system papers, concurrency papers, papers about Rust), Humor (weird-exprs test, Ferris Rap, bastion of the turbofish).

# Verification Notes

- Definition source: Direct quotations from Ch. 26 Background topics on CFGs and dataflow analysis
- Key Properties: Covers all major sections across 687 lines including the full glossary and bibliography
- Confidence rationale: HIGH -- reference material with clear definitions and well-organized tables
- Uncertainties: Glossary terms evolve with compiler development (e.g., ongoing NodeId to HirId migration); lecture links may become stale
- Cross-reference status: All other cards in this extraction set are referenced
