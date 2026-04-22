---
concept: Macro Matcher
slug: macro-matcher
category: macro-system
subcategory: null
tier: intermediate
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "01-methodical-introduction"
chapter_number: 1
pdf_page: null
section: "Matching"
extraction_confidence: high
aliases:
  - "macro pattern"
  - "macro matching"
  - "matcher"
prerequisites:
  - macro-rules
  - token-tree
extends: []
related:
  - metavariable
  - fragment-specifier
  - macro-repetition
contrasts_with: []
answers_questions:
  - "How does pattern matching work in macro_rules!?"
  - "What can appear in a macro pattern?"
  - "What happens when no macro rule matches?"
  - "Why does the order of macro rules matter?"
---

# Quick Definition

A macro matcher is the pattern (left-hand side) of a `macro_rules!` rule. It specifies what input token trees the rule will match. Matchers can contain literal token trees, captures (`$name:kind`), and repetitions (`$(...)*`). Rules are tried top-to-bottom, and the first complete match wins.

# Core Definition

When a macro is invoked, the `macro_rules!` interpreter goes through the rules one by one, in lexical order. For each rule, it tries to match the contents of the input token tree against that rule's pattern. A pattern must match the entirety of the input to be considered a match. If the input matches, the invocation is replaced by the expansion; otherwise, the next rule is tried. If all rules fail, macro expansion fails with an error.

Matchers can contain:
1. **Literal token trees** -- tokens that must be matched exactly
2. **Captures** -- `$name:kind` patterns that match grammar categories and bind results
3. **Repetitions** -- `$(...) sep rep` patterns that match repeated sequences

A critical constraint: once the parser begins consuming tokens for a capture, it cannot stop or backtrack. This means rule ordering is critical -- more-specific rules must come before less-specific ones.

# Prerequisites

- **macro-rules** -- Matchers are one half of a `macro_rules!` rule
- **token-tree** -- Matchers operate on the contents of the input token tree

# Key Properties

1. **Top-to-bottom matching**: Rules are tried in lexical order; first complete match wins.
2. **Complete match required**: The pattern must match the entire input, not just a prefix.
3. **No backtracking**: Once the parser starts consuming tokens for a capture, it cannot backtrack to try an alternative interpretation.
4. **Literal matching**: Patterns can contain literal token trees that must appear exactly in the input.
5. **Grouping-agnostic**: The specific delimiter used at invocation (`()`, `[]`, `{}`) is not part of the match -- only the contents matter.
6. **Follow-set restrictions**: Certain captures have restrictions on what tokens can follow them, to guard against future syntax changes.

# Construction / Recognition

## Empty pattern

```rust
macro_rules! four {
    () => { 1 + 3 };
}
```

Matches only empty input: `four!()`, `four![]`, or `four!{}`.

## Literal token matching

```rust
macro_rules! gibberish {
    (4 fn ['spang "whammo"] @_@) => { ... };
}
```

Every token in the pattern must appear exactly in the input.

## Ordering matters -- unreachable rules

```rust
macro_rules! dead_rule {
    ($e:expr) => { ... };       // captures any expression
    ($i:ident +) => { ... };    // NEVER reachable!
}
```

Invoking `dead_rule!(x+)` causes a compile error, not a fallthrough to the second rule, because the parser starts parsing `x+` as an expression, sees `x` is valid, then tries to continue parsing the `+` as part of the expression but finds no right-hand operand.

# Context & Application

Understanding matchers is essential for writing correct macros. The no-backtracking rule is the most important practical constraint: it means you must write rules from most-specific to least-specific. If a greedy capture like `$e:expr` appears first, it will consume tokens eagerly and potentially cause parse errors rather than falling through to more specific rules.

The follow-set restrictions exist to protect against future Rust syntax changes. For example, `$e:expr` can only be followed by `=>`, `,`, or `;`. This prevents a macro from relying on specific parsing behavior that might change if Rust's expression grammar evolves.

# Examples

**No-backtracking demonstration** (from "Captures and Expansion Redux" section):

```rust
macro_rules! dead_rule {
    ($e:expr) => { ... };
    ($i:ident +) => { ... };
}
```

Invoking `dead_rule!(x+)`: the parser starts matching `$e:expr`, sees `x` as a valid expression start, then sees `+` which is valid in an expression (binary addition). With no right-hand side for the addition, the parser panics and aborts compilation with a syntax error -- it does NOT try the second rule.

**Follow-set restrictions** (from "Captures and Expansion Redux" section):

| Capture kind | Can be followed by |
|---|---|
| `item` | anything |
| `block` | anything |
| `stmt` | `=>` `,` `;` |
| `pat` | `=>` `,` `=` `if` `in` |
| `expr` | `=>` `,` `;` |
| `ty` | `,` `=>` `:` `=` `>` `;` `as` |
| `ident` | anything |
| `path` | `,` `=>` `:` `=` `>` `;` `as` |
| `meta` | anything |
| `tt` | anything |

# Relationships

## Builds Upon

- **token-tree** -- Matchers match against the contents of the input token tree
- **macro-rules** -- Matchers are the left-hand side of macro rules

## Enables

- **metavariable** -- Captures within matchers bind input to named variables
- **macro-repetition** -- Repetition patterns within matchers

## Related

- **fragment-specifier** -- The `kind` part of `$name:kind` captures
- **macro-expansion** -- The right-hand side that uses matcher captures

# Common Errors

1. **Rules ordered from general to specific**: Putting `($e:expr)` before `($i:ident +)` makes the second rule unreachable. Always order from most-specific to least-specific.
2. **Violating follow-set restrictions**: Placing a token after a capture that isn't in the allowed follow set causes a compile error. For example, `$e:expr $i:ident` is invalid because `ident` is not in the follow set for `expr`.
3. **Expecting backtracking**: Writing rules that depend on the parser "giving up" on one interpretation and trying another. The parser never backtracks.

# Common Confusions

- **Confusion**: Expecting macro matching to work like regex with backtracking.
  **Clarification**: Macro pattern matching has no backtracking. Once the parser commits to consuming tokens for a capture, it must succeed or the entire compilation aborts. This is why rule ordering is critical.
- **Confusion**: Thinking the invocation delimiters matter.
  **Clarification**: `my_macro!(...)`, `my_macro![...]`, and `my_macro!{...}` all match the same patterns. The delimiters are not part of the matched content.

# Source Reference

"The Little Book of Rust Macros" by Daniel Keep et al., Chapter 1: "Methodical Introduction," sections "Matching" and "Captures and Expansion Redux."

# Verification Notes

- Matching semantics: directly from "Matching" section
- No-backtracking rule and `dead_rule` example: directly from "Captures and Expansion Redux" section
- Follow-set table: directly enumerated in the source (as of Rust 1.3)
- Confidence: HIGH -- explicit, detailed coverage with illustrative examples
