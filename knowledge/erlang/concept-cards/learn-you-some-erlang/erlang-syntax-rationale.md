---
concept: Erlang Syntax Rationale
slug: erlang-syntax-rationale
category: data-types
subcategory: syntax
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Appendix B. On Erlang's Syntax"
chapter_number: null
pdf_page: null
section: "The Template"
extraction_confidence: high
aliases:
  - "ant turd tokens"
  - "comma semicolon period"
prerequisites: []
related: []
contrasts_with: []
answers_questions:
  - "Why does Erlang use comma, semicolon, and period the way it does?"
  - "How should I read Erlang's punctuation?"
---

# Erlang Syntax Rationale

## Quick Definition

Erlang's punctuation — comma, semicolon, period — separates and terminates expressions, clauses, and forms rather than lines; it derives from Prolog and is best read by thinking in expressions, not lines.

## Core Definition

Erlang draws its syntax from Prolog, which explains the punctuation that newcomers nickname the "ant turd tokens" (`,`, `;`, `.`). The key to reading it is to abandon line-based thinking and think in *expressions* (anything that returns a value) and *forms* (module attributes and function declarations, which return nothing). The comma (`,`) separates expressions. The semicolon (`;`) separates function clauses and the branches of expressions like `if`/`case`. The period (`.`) terminates a form (in modules) or an expression (in the shell). Because `;` *separates* rather than *terminates*, the last branch or clause needs no trailing token (Chapter, Appendix B, "The Template").

## Prerequisites

This is a foundational concept with no prerequisites within this source.

## Key Properties

1. Erlang's syntax derives from Prolog
2. `,` (and) separates expressions
3. `;` (or) separates function clauses and expression branches (`if`, `case`, etc.)
4. `.` (done) terminates a form in a module, or an expression in the shell
5. `if ... end`, `case ... of ... end`, `begin ... end`, `fun() -> ... end`, `try ...` are all expressions and yield a value
6. `;` separates, so the final clause/branch carries no `;` — only the next token its context requires
7. The same construct may be followed by `,`, `;`, or `.` depending on its position

## Recognition

## Three Ways to Read Erlang Punctuation

1. **The Template** — see code as a fixed template `head(Args) [Guard] -> Expr1, Expr2, ..., ExprN;` repeated per clause, ending in `.`
2. **The English Sentence** — read clauses like a list of items ("if it's sunny: sunscreen, water, hat;")
3. **And, Or, Done** — read `,` as *and*, `;` as *or*, `.` as *being done*, so a function is nested logical statements

## Context & Application

The appendix exists to help newcomers who program around Erlang's syntax without ever becoming comfortable with it. The author's recommended approach is the Template: stop thinking in terminated lines (as in C or Java) and instead fill a predefined template. The "And, Or, Done" reading is presented as the most elegant. The conclusion: the syntax is only intimidating, not difficult.

## Examples

**Example** (Appendix B, "The Template"): `fac(0) -> 1; fac(N) -> N * fac(N-1).` — `;` separates the two clauses, `.` ends the form.

**Example** (Appendix B): an `if` written with leading separators —
`if X < 0 -> negative ; X > 0 -> positive ; X == 0 -> zero end` — makes clear `;` goes *between* branches, not after them.

## Relationships

This concept stands largely on its own as a reading aid; it relates broadly to Erlang module and function syntax.

## Common Errors

- **Error**: Putting a `;` after the last function clause or expression branch
  **Correction**: `;` separates; the final clause/branch takes no `;` — it takes `.` (or `,`/`;` per its enclosing context)

## Common Confusions

- **Confusion**: Treating `,`/`;`/`.` as line terminators like `;` in C
  **Clarification**: They separate and terminate *expressions, clauses, and forms* — think in expressions, not lines

## Source Reference

Appendix B: On Erlang's Syntax, sections "The Template," "The English Sentence," "And, Or, Done.," and "In Conclusion."

## Verification Notes

- Definition: Direct adaptation from Appendix B
- Key Properties: All explicit in the appendix
- Confidence: HIGH — the appendix is entirely devoted to this concept
- Cross-references: none — this is a standalone reading-aid concept
