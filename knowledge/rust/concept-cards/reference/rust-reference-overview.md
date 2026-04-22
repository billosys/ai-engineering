---
concept: Rust Reference Overview
slug: rust-reference-overview
category: language-specification
subcategory: null
tier: foundational
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Introduction / Notation / Crates and Source Files"
chapter_number: 0
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Rust Reference"
  - "grammar notation"
  - "crate compilation model"
  - "source file organization"
  - "crate module tree"
  - "main function requirements"
prerequisites: []
extends: []
related:
  - lexical-structure-input-and-keywords
  - lexical-structure-tokens-and-literals
  - reference-macros-by-example
  - reference-procedural-macros
contrasts_with: []
answers_questions:
  - "What is The Rust Reference and what does it cover?"
  - "What grammar notation does the Reference use?"
  - "What is a crate in Rust's compilation model?"
  - "How are Rust source files organized into modules?"
  - "What are the requirements for the main function?"
  - "What does the no_main attribute do?"
  - "What is the crate_name attribute?"
  - "What is the hard cut operator in the grammar?"
---

# Quick Definition

The Rust Reference is the primary specification for the Rust programming language, covering syntax, semantics, and rules for stable Rust. It uses a formal grammar notation with lexer and syntax productions, and defines the compilation model where each compilation processes a single crate -- a unit of compilation, linking, versioning, and distribution containing a tree of nested module scopes.

# Core Definition

The Rust Reference is the normative document for stable Rust. It is not an introduction to the language, not a standard library reference, and does not document `rustc` internals or Cargo specifics. It describes only stable features; unstable features are covered in the Unstable Book. The compiled program is treated as a black box -- the Reference specifies observable behavior, not permitted optimizations.

The **grammar notation** uses a two-level system: CAPITAL names (e.g., `KW_IF`, `INTEGER_LITERAL`) denote tokens produced by the lexer, while _ItalicCamelCase_ names (e.g., `_LetStatement_`, `_Item_`) denote syntactical productions. Key notation includes: `x?` for optional, `x*` for zero-or-more, `x+` for one-or-more, `|` for alternation, `!` for negative lookahead, and `^` for the **hard cut operator**. The hard cut prevents all backtracking past the cut point -- once everything to its left has matched, the remaining sequence must match or parsing fails unconditionally. This is necessary because some Rust tokens (like `c"..."`) begin with a prefix that is itself a valid token (like the identifier `c`).

Rust's semantics observe a **phase distinction** between compile-time and run-time. The compilation model centers on **crates**: each compilation processes a single crate in source form and produces a single crate in binary form (executable or library). A crate contains a tree of nested module scopes, with the top-level module being anonymous. Every source file describes a module; every module need not have its own source file. Source files have the `.rs` extension, are encoded as UTF-8, and contain a sequence of zero or more Item definitions optionally preceded by inner attributes.

A crate containing a `main` function can be compiled to an executable. The `main` function must take no arguments, must not declare trait or lifetime bounds or where clauses, and its return type must implement the `Termination` trait. The `main` function may be an import from another module or crate.

# Prerequisites

This is the foundational framing for the entire Rust Reference. General familiarity with Rust syntax and the concept of compilation is assumed.

# Key Properties

1. The Reference covers only stable Rust; each language release (every six weeks) produces a corresponding Reference version
2. Grammar uses ordered alternation: the parser tries alternatives left to right and takes the first match
3. Sequences have higher precedence than `|` alternation in the grammar
4. The hard cut operator (`^`) prevents all backtracking past the cut point, distinguishing it from a soft cut which only prevents backtracking within the immediately enclosing ordered choice
5. String table productions represent keywords, operators, and similar tokens as listings of printable strings, assumed to be the result of a DFA-driven lexical analysis phase
6. Each crate has a canonical module path for every item within its module tree
7. The anonymous crate module can have inner attributes that apply to the crate as a whole (e.g., `#![crate_name = "projx"]`, `#![crate_type = "lib"]`)
8. Rule identifiers (e.g., `r[crate.main.restriction]`) appear before each language rule to provide stable cross-reference links
9. The `no_main` attribute disables emitting the `main` symbol, useful when another linked object defines `main`
10. The `crate_name` attribute specifies the crate name; it must be non-empty and contain only Unicode alphanumeric or `_` characters

# Construction / Recognition

## Reading the Reference

1. For specific questions: jump to the relevant chapter or use keyword search
2. For general learning: browse the table of contents and follow cross-links
3. Terms in *italics* define the term; subsequent uses link back to the definition section
4. Edition differences are marked in edition blocks (e.g., `[!EDITION-2018]`)
5. Grammar blocks have toggleable syntax diagrams: squares are non-terminal rules, rounded rectangles are terminals

## Crate and Source File Organization

1. A crate is invoked with a single source file as input (the crate root)
2. That source file may cause other source files to be loaded as modules
3. Module names and locations in the module tree are defined externally (by a `mod` item or the crate name itself)
4. Module definitions can be nested within one file
5. Source files may begin with a shebang line (e.g., `#!/usr/bin/env rustx`)

# Context & Application

The Reference serves as the authoritative specification for Rust language behavior. It complements The Rust Programming Language book (which teaches), the Standard Library documentation (which covers APIs), the `rustc` book (which covers the compiler tool), and the Cargo book (which covers the build system). The grammar notation is derived from parsing expression grammars (PEGs), with the hard cut operator introduced by Mizushima et al. Understanding the notation is essential for reading any formal grammar production throughout the Reference.

The crate compilation model is fundamental to Rust: unlike languages with header files or separate compilation of individual source files, Rust compiles one crate at a time as a coherent unit. This design enables whole-crate analysis, optimization, and the module privacy system that underpins unsafe code soundness.

# Examples

**Example 1** (Ch. 1, Notation): The hard cut prevents ambiguous tokenization:
```text
c"\0" -- without the cut after `c"`, this could backtrack and lex as
         identifier `c` followed by string literal "\0". The cut after
         the opening `c"` delimiter prevents this.
```

**Example 2** (Ch. 4, Crates): A source file with crate-level attributes:
```rust
#![crate_name = "projx"]
#![crate_type = "lib"]
#![warn(non_camel_case_types)]
```

**Example 3** (Ch. 4, Main Functions): The `main` function can be an import:
```rust
mod foo {
    pub fn bar() {
        println!("Hello, world!");
    }
}
use foo::bar as main;
```

# Relationships

## Builds Upon
(none -- this is the foundational overview for all Reference content)

## Enables
- **lexical-structure-input-and-keywords** -- the grammar notation defined here is used in all lexical productions
- **lexical-structure-tokens-and-literals** -- token definitions use the notation system
- **reference-macros-by-example** -- macro grammar uses the notation system
- **reference-procedural-macros** -- procedural macro definitions reference crate structure

## Related
- **reference-macros-by-example** -- macros extend syntax, which the Reference formally specifies
- **reference-procedural-macros** -- proc macros must be defined in the crate root

## Contrasts With
(none)

# Common Errors

- **Error**: Treating the Reference as a tutorial or introduction to Rust.
  **Correction**: The Reference assumes background familiarity with the language. Use "The Rust Programming Language" book for learning; use the Reference for precise definitions of language rules.

- **Error**: Expecting the Reference to document `rustc` behavior or optimizations.
  **Correction**: The Reference specifies observable behavior (the "black box" model). It does not specify what optimizations are allowed or disallowed.

# Common Confusions

- **Confusion**: Thinking a crate is the same as a package or a source file.
  **Clarification**: A crate is a unit of compilation producing a single binary artifact. A package (Cargo concept) may contain multiple crates. A crate contains a module tree that may span multiple source files, but each compilation starts from a single root source file.

- **Confusion**: Assuming `main` must be defined directly in the crate root source file.
  **Clarification**: The `main` function may be an import from any module or even an external crate, as long as it satisfies the signature requirements (`no args, return type implements Termination`).

# Source Reference

Chapter 0: Introduction -- scope, conventions, rule identifiers, editions. Chapter 1: Notation -- grammar notation table, hard cut operator, string table productions, syntax diagrams. Chapter 4: Crates and Source Files -- crate compilation model, module tree, source file organization, main function requirements, `no_main` attribute, `crate_name` attribute.

# Verification Notes

- Definition source: Direct synthesis from Ch. 0 (144 lines), Ch. 1 (78 lines), and Ch. 4 (142 lines)
- Key Properties: Items 1-5 from notation chapter; items 6-10 from crates chapter; all directly stated in source
- Confidence rationale: HIGH -- the source provides explicit normative definitions
- Uncertainties: Rule identifiers are noted as "currently in flux" and may change between releases
- Cross-reference status: All slugs reference cards in this Reference extraction set
