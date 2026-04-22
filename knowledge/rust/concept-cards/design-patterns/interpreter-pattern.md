---
concept: Interpreter Pattern
slug: interpreter-pattern
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
  - "interpreter"
  - "DSL pattern"
  - "recursive descent pattern"
prerequisites:
  - constructor-idiom
extends: []
related:
  - visitor-pattern
  - command-pattern
contrasts_with: []
answers_questions:
  - "How do I implement the Interpreter pattern in Rust?"
  - "How can I use macro_rules! as a form of the Interpreter pattern?"
  - "What is the relationship between DSLs, grammars, and the Interpreter pattern?"
---

# Quick Definition

The Interpreter pattern expresses recurring problem instances in a simple domain-specific language and implements an interpreter to solve them. In Rust, this can be done via a traditional recursive descent parser operating on a grammar, or via `macro_rules!` which defines custom syntax expanded at compile time.

# Core Definition

"If a problem occurs very often and requires long and repetitive steps to solve it, then the problem instances might be expressed in a simple language and an interpreter object could solve it by interpreting the sentences written in this simple language." For any kind of problem, we define "a domain specific language, a grammar for this language, an interpreter that solves the problem instances." (Rust Design Patterns, Ch. 2: Behavioural Patterns, "Interpreter")

# Prerequisites

- **Constructor idiom** -- the Interpreter struct is constructed with standard Rust patterns before use

# Key Properties

1. Defines a domain-specific language (DSL) for expressing problem instances
2. Specifies a grammar (context-free grammar with terminal symbols, non-terminal symbols, start symbol, and production rules)
3. Implements an interpreter that processes sentences in the DSL
4. In Rust, the traditional approach uses a recursive descent parser with an iterator over characters
5. Rust's `macro_rules!` provides a compile-time alternative: define special syntax and rules for expanding into source code
6. The `macro_rules!` approach is evaluated at compile time rather than runtime
7. The pattern is not limited to formal language parsing -- it is about "expressing problem instances in a more specific way"

# Construction / Recognition

## Traditional Recursive Descent Parser Approach:
1. Define terminal and non-terminal symbols for the grammar
2. Identify production rules (e.g., `exp -> exp + term`, `term -> 0 | 1 | ... | 9`)
3. Create an `Interpreter` struct holding a character iterator (`std::str::Chars<'a>`)
4. Implement methods corresponding to non-terminals (e.g., `interpret` for `exp`, `term` for `term`)
5. Use `while let` and `match` to consume and process tokens
6. Build the output incrementally (e.g., push to a mutable `String`)

## Rust `macro_rules!` Approach:
1. Identify a computation that benefits from compact syntax
2. Define a `macro_rules!` with appropriate matchers (e.g., `$($element:expr),*`)
3. Implement the expansion logic in the macro body
4. Users invoke the macro with the custom syntax (e.g., `norm!(x, 1, 2)`)

## To Recognize the Pattern:
1. Look for a problem solved by defining a mini-language or notation
2. Look for grammar-based parsing or `macro_rules!` defining custom syntax
3. Check for recursive processing of structured input

# Context & Application

The source presents two complementary approaches. The first is a traditional infix-to-postfix expression translator: given a grammar over digits and `+`/`-` operators, a recursive descent parser converts infix expressions like `2+3` into postfix `23+`. The `Interpreter` struct holds a `Chars` iterator and implements `interpret` (for the `exp` non-terminal) and `term` (for the `term` non-terminal).

The second approach uses `macro_rules!` to compute Euclidean length of n-dimensional vectors. The source notes: "There may be a wrong perception that the Interpreter design pattern is about design grammars for formal languages and implementation of parsers for these grammars. In fact, this pattern is about expressing problem instances in a more specific way and implementing functions/classes/structs that solve these problem instances."

The source references the Dragon Book (Compilers: Principles, Techniques, and Tools) for further grammar transformation techniques such as removing left recursion.

# Examples

**Example 1** (Ch. 2, "Interpreter" -- Recursive Descent): An `Interpreter<'a>` struct wraps `std::str::Chars<'a>`. The `interpret` method processes the `exp` production rule, calling `term` for each operand and appending operators after both operands (postfix). Parsing `"1-2+3-4"` produces `"12-3+4-"`.

**Example 2** (Ch. 2, "Interpreter" -- `macro_rules!`): A `norm!` macro computes Euclidean length: `norm!(x, 1, 2)` expands to code that squares each element, sums them, and takes the square root. The source notes this "might be easier to express and more efficient than packing `x,1,2` into a `Vec` and calling a function computing the length."

# Relationships

## Builds Upon
- None explicitly

## Enables
- None explicitly

## Related
- **visitor-pattern** -- visitors operate on heterogeneous data structures (like ASTs) that interpreters may produce or consume
- **command-pattern** -- both patterns deal with encapsulated operations; commands encapsulate actions, interpreters encapsulate language processing

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Assuming the Interpreter pattern is only about building parsers for formal languages.
  **Correction**: "This pattern is about expressing problem instances in a more specific way and implementing functions/classes/structs that solve these problem instances." `macro_rules!` is a valid Interpreter pattern implementation in Rust.

- **Error**: Applying the grammar directly without transformation (e.g., leaving left recursion in a recursive descent parser).
  **Correction**: "This grammar should be further transformed depending on what we are going to do with it. For example, we might need to remove left recursion." The source references the Dragon Book for these techniques.

# Common Confusions

- **Confusion**: Thinking `macro_rules!` is unrelated to the Interpreter pattern.
  **Clarification**: The source explicitly presents `macro_rules!` as an implementation of the Interpreter pattern: "Rust language has `macro_rules!` that allow us to define special syntax and rules on how to expand this syntax into source code." This is a compile-time DSL.

- **Confusion**: Thinking the simple example (digits and `+`/`-`) represents the limits of the pattern.
  **Clarification**: The example is deliberately simplified. The pattern scales to more complex grammars; the source notes that grammar transformation techniques from compiler theory apply when extending the approach.

# Source Reference

Chapter 2: Design Patterns, "Interpreter" section under Behavioural Patterns. Includes a context-free grammar definition, a recursive descent parser implementation, a `macro_rules!` example, and references to the Wikipedia article on Interpreter pattern, context-free grammars, and `macro_rules!` documentation.

# Verification Notes

- Definition source: Direct quotation from the "Description" subsection of "Interpreter"
- Key Properties: Derived from the grammar definition, parser implementation, and macro example
- Confidence rationale: HIGH -- the source provides complete runnable code for both approaches with clear discussion
- Uncertainties: The grammar transformation details are deferred to the Dragon Book; the source does not elaborate
- Cross-reference status: visitor-pattern and command-pattern are in this extraction set; constructor-idiom is from Agent 1
