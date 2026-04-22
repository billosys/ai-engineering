---
concept: Token Tree
slug: token-tree
category: compilation
subcategory: null
tier: foundational
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "01-methodical-introduction"
chapter_number: 1
pdf_page: null
section: "Token trees"
extraction_confidence: high
aliases:
  - "token trees"
  - "tt"
prerequisites: []
extends: []
related:
  - macro-rules
  - syntax-extension
  - fragment-specifier
contrasts_with: []
answers_questions:
  - "What is a token tree in Rust?"
  - "How do token trees differ from tokens and the AST?"
  - "What is the tt fragment specifier?"
  - "Why are token trees important for macros?"
---

# Quick Definition

Token trees are an intermediate representation between raw tokens and the AST. Almost all tokens are token tree leaves, while grouping tokens (`(...)`, `[...]`, `{...}`) form interior nodes that give the tree its structure. Every macro invocation receives a single non-leaf token tree as input.

# Core Definition

Token trees sit between tokens and the AST in the compilation pipeline. The first stage of Rust compilation is tokenisation, which transforms source text into a sequence of tokens (identifiers, integers, keywords, lifetimes, strings, symbols). The second stage is parsing, which transforms tokens into an Abstract Syntax Tree (AST).

Token trees are formed from tokens with a simple structural rule:
- Almost all tokens are also token trees -- specifically, they are **leaves**.
- The "grouping" tokens `(...)`, `[...]`, and `{...}` are the **interior nodes**, and what give token trees their structure.
- It is impossible to have an unpaired paren, bracket, or brace, nor incorrectly nested groups in a token tree.

For the expression `a + b + (c + d[0]) + e`, the token trees are:

```text
<<a>> <<+>> <<b>> <<+>> <<(   )>> <<+>> <<e>>
                   |------v------|
                    <<c>> <<+>> <<d>> <<[   ]>>
                                       |-v-|
                                        <<0>>
```

This has no relationship to the AST the expression would produce. Instead of a single root node, there are nine token trees at the root level.

# Prerequisites

This is a foundational concept. Understanding Rust's compilation pipeline (tokenisation followed by parsing into AST) provides helpful context, but is covered within the same source section.

# Key Properties

1. **Intermediate representation**: Token trees sit between raw tokens and the AST.
2. **Leaves**: Almost all tokens are token tree leaves.
3. **Interior nodes**: Only grouping tokens (`(...)`, `[...]`, `{...}`) form interior nodes.
4. **Always balanced**: Unpaired or incorrectly nested grouping tokens are impossible in a token tree.
5. **Flat at root**: Unlike the AST, a token tree sequence can have multiple root-level elements.
6. **Macro input**: Every macro invocation receives a single non-leaf token tree as input.
7. **`tt` fragment specifier**: The `tt` fragment specifier captures a single token tree, making it the most flexible capture kind.

# Construction / Recognition

## Recognizing token tree structure

Given `a + b + (c + d[0]) + e`:
- Root level has 9 token trees: `a`, `+`, `b`, `+`, `(...)`, `+`, `e`
- The `(...)` interior node contains: `c`, `+`, `d`, `[...]`
- The `[...]` interior node contains: `0`

## Token tree vs. AST

The same expression `1 + 2` as a token tree is three separate trees (`1`, `+`, `2`) at the root level. As an AST, it is a single `BinOp(Add, LitInt(1), LitInt(2))` node.

## Using `tt` in macros

```rust
macro_rules! match_tokens {
    ($a:tt + $b:tt) => { "got an addition" };
    (($i:ident)) => { "got an identifier" };
    ($($other:tt)*) => { "got something else" };
}
```

# Context & Application

Token trees are critical to understanding how macros work in Rust. The macro system operates on token trees, not on raw tokens or AST nodes. When writing macros, you must deal with both token trees (as input) and AST nodes (as output) as distinct things.

The `tt` fragment specifier is the most permissive capture kind -- it captures any single token tree (leaf or interior node). This makes it essential for advanced macro patterns like tt-munchers, push-down accumulation, and callback patterns, where macros need to process arbitrary token sequences one piece at a time.

The distinction between token trees and AST also explains why captured expressions become opaque: once tokens are parsed into an AST node via a capture like `$e:expr`, they become a single opaque token tree leaf that cannot be destructured by subsequent pattern matching.

# Examples

**Token tree visualization** (from "Token trees" section):

The expression `a + b + (c + d[0]) + e` produces:

```text
<<a>> <<+>> <<b>> <<+>> <<(   )>> <<+>> <<e>>
                   |------v------|
                    <<c>> <<+>> <<d>> <<[   ]>>
                                       |-v-|
                                        <<0>>
```

**Token tree vs. AST for `1 + 2`** (from "Source Analysis" section):

As token trees: three separate leaf nodes.
As AST:
```text
+-----------+   +---------+
| BinOp     | +-| LitInt  |
| op: Add   | | | val: 1  |
| lhs: o    |-+ +---------+
| rhs: o    |-+ +---------+
+-----------+ +-| LitInt  |
                | val: 2  |
                +---------+
```

# Relationships

## Enables

- **macro-rules** -- Macro input is always a single non-leaf token tree
- **macro-matcher** -- Matchers operate on token tree sequences
- **fragment-specifier** -- The `tt` specifier captures a single token tree

## Related

- **syntax-extension** -- Syntax extension arguments are non-leaf token trees
- **macro-expansion** -- Expansion replaces macro invocations in the AST

## Contrasts With

- Raw tokens (unstructured flat sequence)
- AST nodes (fully parsed semantic structure)

# Common Errors

1. **Confusing token trees with the AST**: Token trees are structural but not semantic. The expression `a + b * c` has the same flat token tree structure regardless of operator precedence.
2. **Expecting unpaired delimiters**: Token trees always have balanced grouping tokens. You cannot write a macro that matches or produces unpaired brackets.

# Common Confusions

- **Confusion**: Thinking token trees and AST nodes are the same thing.
  **Clarification**: Token trees are a lightweight structural grouping based only on delimiters. The AST is a fully parsed representation with semantic structure (operator precedence, expression nesting, etc.). When writing macros, you deal with both as distinct things.
- **Confusion**: Believing a captured expression can be destructured later.
  **Clarification**: Once input is captured as an `expr` (or any non-`tt` capture), it becomes an opaque AST node wrapped in a single token tree leaf. It cannot be pattern-matched against by subsequent macros. Only `tt` and `ident` captures preserve the ability to match against contents.

# Source Reference

"The Little Book of Rust Macros" by Daniel Keep et al., Chapter 1: "Methodical Introduction," sections "Source Analysis" and "Token trees."

# Verification Notes

- Token tree structure and visualization: directly from source
- AST comparison: directly from source diagrams
- "impossible to have an unpaired paren" -- direct quote from source
- The opaque-AST-node property is from "Captures and Expansion Redux" section
- Confidence: HIGH -- the source provides explicit definitions and detailed visualizations
