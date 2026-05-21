---
concept: Reverse Polish Notation Calculator
slug: reverse-polish-notation-calculator
category: functions-pattern-matching
subcategory: worked-examples
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Functionally Solving Problems"
chapter_number: 8
pdf_page: null
section: "Reverse Polish Notation Calculator"
extraction_confidence: high
aliases:
  - "RPN calculator"
  - "postfix calculator"
  - "stack calculator"
prerequisites:
  - fold
  - pattern-matching
  - tail-recursion
extends:
  - fold
related:
  - functional-problem-solving-approach
contrasts_with: []
answers_questions:
  - "How do I implement a Reverse Polish Notation calculator in Erlang?"
  - "How can a fold be used to evaluate a stack-based expression?"
---

# Reverse Polish Notation Calculator

## Quick Definition

A worked example that evaluates Reverse Polish (postfix) arithmetic expressions by tokenizing a string and folding over the tokens with a list used as a stack. Operands are pushed; operators pop their operands and push the result.

## Core Definition

In Reverse Polish notation (RPN) the operator follows its operands, so `(2 + 2) / 5` is written `2 2 + 5 /`. The chapter builds a `calc` module that reads such expressions. The string is split with `string:tokens/2`, and the resulting token list is processed by `lists:foldl/3`. The accumulator is a list acting as a stack: numbers are read and consed on top; an operator pops the two top numbers, applies itself, and conses the result back. At the end exactly one element — the result — should remain, enforced by pattern matching `[Res]` (Hébert, ch. 8, "Reverse Polish Notation Calculator").

## Prerequisites

- **Fold** — The entire evaluation is a single `lists:foldl/3` over the token list
- **Pattern matching** — Operator clauses such as `rpn("+", [N1,N2|S])` match both the operator string and the stack shape
- **Tail recursion** — `foldl` is itself tail recursive; understanding accumulators is needed to choose the stack as accumulator

## Key Properties

1. The expression is represented as a whitespace-delimited string, tokenized into a list of strings
2. An Erlang list serves as the stack; the cons operator `[Head|Tail]` is exactly a push
3. `lists:foldl/3` walks the token list once with the stack as accumulator
4. Each operator clause precedes the catch-all number clause so operators are not mistaken for operands
5. Binary operators pop two values (`[N1,N2|S]`); unary ones such as `ln` pop one (`[N|S]`)
6. A correct expression leaves exactly one value on the stack; the `[Res]` match crashes otherwise ("let it crash")

## Construction / Recognition

## To Build the RPN Calculator

1. Write `rpn/1` to tokenize the input: `lists:foldl(fun rpn/2, [], string:tokens(L, " "))`, then match `[Res]` and return `Res`
2. Write a `read/1` helper that converts a token to a number via `string:to_float/1`, falling back to `list_to_integer/1`
3. Write `rpn/2` with one clause per operator, e.g. `rpn("+", [N1,N2|S]) -> [N2+N1|S];`
4. Add the catch-all clause last: `rpn(X, Stack) -> [read(X)|Stack].`
5. Test with the `=` operator as an assertion in an `rpn_test/0` function

## Examples

> **Worked trace** (ch. 8): `10 4 3 + 2 * -` evaluates to `-4` — push 10, 4, 3; `+` pops 4,3 pushes 7; push 2; `*` pops 7,2 pushes 14; `-` pops 10,14 pushes -4.
>
> **Operator clauses** (ch. 8): `rpn("/", [N1,N2|S]) -> [N2/N1|S];` and `rpn("ln", [N|S]) -> [math:log(N)|S];`.
>
> **Test assertions** (ch. 8): `-4 = rpn("10 4 3 + 2 * -")` and `87 = rpn("90 3 -")`.

## Relationships

## Builds Upon

- **Fold** — The calculator is essentially one fold with a stack accumulator

## Related

- **Functional problem-solving approach** — The chapter's general method of which this is the first instance

## Common Errors

- **Error**: Placing the number catch-all clause before operator clauses
  **Correction**: Operator clauses must come first, or `"+"` is pushed as data instead of applied
- **Error**: Reversing operand order for non-commutative operators
  **Correction**: For `[N1,N2|S]`, `N2` is the deeper (earlier) operand, so subtraction is `N2-N1`

## Common Confusions

- **Confusion**: Believing RPN needs operator-precedence parsing
  **Clarification**: RPN has no precedence and no parentheses; a single left-to-right stack pass suffices
- **Confusion**: Thinking the crash on a bad expression is a flaw
  **Clarification**: It is deliberate "let it crash" design — the `[Res]` match rejects malformed input

## Source Reference

Chapter 8, "Functionally Solving Problems," section "Reverse Polish Notation Calculator" (including subsections "How RPN Calculators Work," "Creating an RPN Calculator," "Testing the Code").

## Verification Notes

- Definition and steps: directly adapted from the `calc.erl` listings in ch. 8
- Worked trace: from the source's `10 4 3 + 2 * -` walkthrough
- Confidence: HIGH — fully worked example with complete code and tests
- Cross-references: `fold` owned by Agent 1 (Ch 1-7); referenced not recreated
