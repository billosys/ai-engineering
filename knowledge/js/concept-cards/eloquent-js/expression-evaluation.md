---
# === CORE IDENTIFICATION ===
concept: Expression Evaluation
slug: expression-evaluation

# === CLASSIFICATION ===
category: language-implementation
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Programming Language"
chapter_number: 12
pdf_page: null
section: "The evaluator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - evaluator
  - eval

# === TYPED RELATIONSHIPS ===
prerequisites:
  - syntax-tree
  - scope-in-interpreter
extends: []
related:
  - special-form
  - interpreter
contrasts_with:
  - compilation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does an interpreter evaluate expressions?"
---

# Quick Definition
Expression evaluation is the process of traversing a syntax tree and computing the value each node represents, using a scope to resolve variable names.

# Core Definition
"What can we do with the syntax tree for a program? Run it, of course! And that is what the evaluator does. You give it a syntax tree and a scope object that associates names with values, and it will evaluate the expression that the tree represents and return the value that this produces." (Eloquent JavaScript, Ch. 12, lines 287-290)

# Prerequisites
- **Syntax tree**: The evaluator operates on parsed syntax trees
- **Scope**: Understanding how names are resolved to values

# Key Properties
1. Handles different node types differently (value, word, apply)
2. Value nodes return their literal value directly
3. Word nodes look up names in the current scope
4. Apply nodes evaluate the operator, check for special forms, then call the function with evaluated arguments
5. The recursive structure of the evaluator mirrors the recursive structure of the language

# Construction / Recognition
```javascript
function evaluate(expr, scope) {
  if (expr.type == "value") {
    return expr.value;
  } else if (expr.type == "word") {
    if (expr.name in scope) {
      return scope[expr.name];
    } else {
      throw new ReferenceError(
        `Undefined binding: ${expr.name}`);
    }
  } else if (expr.type == "apply") {
    let {operator, args} = expr;
    if (operator.type == "word" &&
        operator.name in specialForms) {
      return specialForms[operator.name](expr.args, scope);
    } else {
      let op = evaluate(operator, scope);
      if (typeof op == "function") {
        return op(...args.map(arg => evaluate(arg, scope)));
      } else {
        throw new TypeError("Applying a non-function.");
      }
    }
  }
}
```
(lines 295-319)

# Context & Application
Evaluation is the core of any interpreter. The same principle applies to any language: traverse the syntax tree and compute values based on node types and the current environment.

# Examples
From the source: "The evaluator has code for each of the expression types. A literal value expression produces its value. (For example, the expression `100` evaluates to the number 100.) For a binding, we must check whether it is actually defined in the scope and, if it is, fetch the binding's value." (lines 323-327)

"Applications are more involved. If they are a special form, like `if`, we do not evaluate anything---we just pass the argument expressions, along with the scope, to the function that handles this form." (lines 330-333)

# Relationships
## Builds Upon
- Syntax tree (the input to evaluation)
- Scope (for resolving names)
## Enables
- Running programs written in the language
## Related
- Special forms (handled differently from regular function calls)
## Contrasts With
- Compilation (which transforms rather than directly executes)

# Common Errors
- **Error**: Evaluating arguments of special forms before passing them to the handler
  **Correction**: Special forms receive unevaluated arguments and decide which to evaluate

# Common Confusions
- **Confusion**: Evaluation and parsing are the same phase
  **Clarification**: Parsing produces a syntax tree; evaluation computes values from it

# Source Reference
Chapter 12: Project: A Programming Language, Section "The evaluator", lines 283-355 of 12-project-a-programming-language.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Complete evaluator code with explanation
- Cross-reference status: verified
