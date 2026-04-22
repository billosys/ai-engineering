---
concept: Macro Pattern Composition
slug: macro-pattern-composition
category: macro-patterns
subcategory: null
tier: advanced
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "05-annotated-examples"
chapter_number: 5
pdf_page: null
section: "Ook!"
extraction_confidence: high
aliases:
  - "combined macro patterns"
  - "macro architecture"
  - "complex macro design"
prerequisites:
  - macro-rules
  - tt-muncher
  - push-down-accumulation
  - internal-rules
  - callback-pattern
extends:
  - tt-muncher
  - internal-rules
related:
  - ast-coercion
  - macro-parsing
  - macro-invocation-design
  - incremental-macro-development
contrasts_with: []
answers_questions:
  - "How do you combine multiple macro patterns into a complete macro system?"
  - "How do you implement a complex language interpreter as a macro?"
  - "How do you handle nested loops or recursive structures in macro parsing?"
  - "What does a real-world complex macro look like?"
---

# Quick Definition

Macro pattern composition is the practice of combining multiple macro patterns -- TT munching, push-down accumulation, internal rules, TT bundling, and abacus counters -- into a single coherent macro that implements complex behaviour. The Ook! example demonstrates this by implementing a complete Turing-complete esoteric language interpreter as a `macro_rules!` macro.

# Core Definition

The Ook! implementation in Chapter 5 serves as an annotated case study of how the individual patterns from Chapters 3 and 4 compose together in practice. The macro uses:

- **Internal rules** (`@start`, `@e`, `@x`, `@s`) to separate the macro into distinct processing phases: initialisation, execution/parsing, loop extraction, and loop skipping.
- **TT munching** (`@e` rules) to parse opcodes two tokens at a time from the input, emitting Rust code and recursing on the tail.
- **Push-down accumulation** (`@x` rules) to extract the body of a loop into a buffer (`$($buf:tt)*`) for separate processing.
- **TT bundling** to forward a group of seven symbol bindings (`($a, $i, $inc, $dec, $r, $w, $re)`) as a single `$syms:tt` through intermediate rules.
- **Abacus counters** (using `@` tokens as depth markers) to track nesting depth when extracting or skipping nested loops.

# Prerequisites

- **macro_rules!** -- the entire implementation uses declarative macros
- **TT muncher** -- opcode parsing is a textbook TT muncher
- **Push-down accumulation** -- loop body extraction accumulates opcodes in a buffer
- **Internal rules** -- phases are separated with `@` prefixes
- **Callback pattern** -- extracted loop bodies are "called back" to the `@e` rules for execution

# Key Properties

1. A single macro can implement a complete language interpreter through pattern composition
2. Internal rules partition the macro into logically distinct phases with different responsibilities
3. TT bundling reduces forwarding complexity -- seven variables become one `$syms:tt`
4. Nested structures (loops within loops) require a depth counter, implemented as a token abacus
5. Two parallel rule sets (`@x` for extraction, `@s` for skipping) handle the "inside" and "after" a loop
6. The recursion limit may need to be raised significantly: the Ook! "Hello World" requires `#![recursion_limit = "158"]`
7. A catch-all entry rule matching `$($Ooks:tt)*` is dangerous and can cause infinite recursion during debugging

# Construction / Recognition

## To Construct a composed macro:
1. Identify the processing phases (e.g., setup, parse, extract, skip)
2. Assign each phase an internal rule prefix (`@start`, `@parse`, etc.)
3. Bundle shared context into a single TT group for forwarding
4. Implement each phase using the appropriate pattern (TT munching for parsing, accumulation for extraction)
5. Use depth counters (abacus) when handling nested structures
6. Define a single public entry rule that delegates to `@start`
7. During development, temporarily prefix the entry rule to avoid infinite-recursion fallthrough

## To Recognise:
1. A macro with many `@`-prefixed rule sections
2. A `$syms:tt` parameter bundling multiple bindings
3. Multiple recursive rule sets that call each other across phases
4. Depth tracking using token counters

# Context & Application

The source presents the Ook! implementation as a proof that `macro_rules!` is Turing-complete, but the architectural lessons apply to any complex macro. The key insight is that patterns compose orthogonally: internal rules handle organisation, TT munching handles parsing, accumulation handles output construction, TT bundling handles parameter forwarding, and abacus counters handle state tracking. Each pattern solves one problem, and together they solve the whole problem.

The source also demonstrates practical debugging advice: "When you are writing, modifying, or debugging a macro like this, it is wise to temporarily prefix rules such as this one with something, such as `@entry`. This prevents the infinite recursion case, and you are more likely to get matcher errors at the appropriate place."

# Examples

**Example 1** (Ch. 5, "Ook!"): TT munching with TT bundling for opcode parsing:

```rust
macro_rules! Ook {
    // Termination
    (@e $syms:tt; ()) => {};

    // Increment pointer -- munch two tokens, emit code, recurse
    (@e ($a:expr, $i:expr, $inc:expr, $dec:expr, $r:expr, $w:expr, $re:expr);
        (Ook. Ook? $($tail:tt)*))
    => {
        $i = ($i + 1) % MEM_SIZE;
        Ook!(@e ($a, $i, $inc, $dec, $r, $w, $re); ($($tail)*));
    };
    // ... similar rules for each opcode
}
```

**Example 2** (Ch. 5, "Ook!"): Loop extraction using push-down accumulation with depth tracking:

```rust
    // Close outermost loop -- process buffered tokens
    (@x $syms:tt; (); ($($buf:tt)*);
        (Ook? Ook! $($tail:tt)*))
    => {
        Ook!(@e $syms; ($($buf)*));
    };

    // Enter nested loop -- increment depth, add to buffer
    (@x $syms:tt; ($($depth:tt)*); ($($buf:tt)*);
        (Ook! Ook? $($tail:tt)*))
    => {
        Ook!(@x $syms; (@ $($depth)*); ($($buf)* Ook! Ook?); ($($tail)*));
    };

    // Exit nested loop -- decrement depth, add to buffer
    (@x $syms:tt; (@ $($depth:tt)*); ($($buf:tt)*);
        (Ook? Ook! $($tail:tt)*))
    => {
        Ook!(@x $syms; ($($depth)*); ($($buf)* Ook? Ook!); ($($tail)*));
    };
```

**Example 3** (Ch. 5, "Ook!"): The entry point with the "dangerous catch-all" warning:

```rust
    // Entry point -- catch-all that can cause infinite recursion
    ($($Ooks:tt)*) => {
        Ook!(@start $($Ooks)*)
    };
```

# Relationships

## Builds Upon
- **tt-muncher** -- opcode parsing is a TT muncher
- **push-down-accumulation** -- loop body extraction uses accumulation
- **internal-rules** -- phases are separated with `@` prefixes
- **callback-pattern** -- loop bodies are passed back to the execution phase

## Enables
- Understanding of how to design and debug arbitrarily complex macros

## Related
- **ast-coercion** -- complex macro outputs often need coercion
- **macro-parsing** -- the enum parser (Ch. 4) is a simpler example of the same composition approach
- **incremental-macro-development** -- the source implicitly demonstrates building up complexity step by step

## Contrasts With
- None explicitly -- procedural macros are the practical alternative for this level of complexity

# Common Errors

- **Error**: A catch-all entry rule like `($($tts:tt)*) => { my_macro!(@start $($tts)*) }` causes infinite recursion when no internal rule matches.
  **Correction**: During development, prefix the entry rule (e.g., `(@entry $($tts:tt)*)`) to get matcher errors instead of infinite recursion. Remove the prefix only when the macro is complete.

- **Error**: Forgetting to track depth when extracting nested loops, causing extraction to stop at the first close-delimiter instead of the matching one.
  **Correction**: Use an abacus counter (or similar depth tracking) that increments on entering nested structures and decrements on exiting them. Only terminate extraction when depth is zero.

# Common Confusions

- **Confusion**: Thinking this level of macro complexity is practical for production code.
  **Clarification**: The source explicitly notes this is a proof of Turing-completeness, not a recommended practice. The Ook! "Hello World" requires recursion limit 158 and compiles slowly. "Esolang-as-macro remains a decidedly *non-viable* method of development with Rust." The patterns themselves, however, are practical individually and in simpler combinations.

- **Confusion**: Thinking TT bundling is required for all multi-parameter forwarding.
  **Clarification**: TT bundling is an optimisation for readability and maintenance. You can always explicitly list all parameters in every rule. Bundling becomes valuable when many intermediate rules need to forward parameters they do not inspect.

# Source Reference

Chapter 5: Annotated Examples, "Ook!" section. The complete macro is presented with annotations explaining each section's role. The source identifies which patterns from Chapters 3-4 are used in each part: internal rules, TT munching, push-down accumulation, TT bundling, and abacus counters.

# Verification Notes

- Definition source: Derived from the annotated implementation and the source's own identification of patterns used
- Key Properties: All from explicit statements in the source annotations
- Confidence rationale: HIGH -- the source thoroughly annotates each section with pattern identification and expansion traces
- Uncertainties: None for the pattern composition concept; specific recursion limits are version-dependent
- Cross-reference status: All slugs reference cards in this extraction set or Agent A/B sets
