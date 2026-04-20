---
# === CORE IDENTIFICATION ===
concept: Special Form
slug: special-form

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
section: "Special forms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - special syntax
  - language construct

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expression-evaluation
  - syntax-tree
extends: []
related:
  - interpreter
  - scope-in-interpreter
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a special form in a programming language?"
---

# Quick Definition
A special form is a language construct (like `if` or `while`) that does not evaluate all its arguments before executing, unlike regular function calls.

# Core Definition
"The `specialForms` object is used to define special syntax in Egg. It associates words with functions that evaluate such forms." The reason `if` must be a special form: "all arguments to functions are evaluated before the function is called, whereas `if` should evaluate only *either* its second or its third argument, depending on the value of the first." (Eloquent JavaScript, Ch. 12, lines 360-396)

# Prerequisites
- **Expression evaluation**: Understanding how normal expressions are evaluated
- **Syntax tree**: Special forms receive unevaluated syntax tree nodes

# Key Properties
1. Arguments are NOT evaluated before the form is invoked
2. The special form handler receives raw expression nodes and the scope
3. The handler decides which arguments to evaluate and when
4. Examples include `if`, `while`, `do`, `define`, and `fun`
5. Distinguished from regular function calls in the evaluator

# Construction / Recognition
```javascript
specialForms.if = (args, scope) => {
  if (args.length != 3) {
    throw new SyntaxError("Wrong number of args to if");
  } else if (evaluate(args[0], scope) !== false) {
    return evaluate(args[1], scope);
  } else {
    return evaluate(args[2], scope);
  }
};
```
(lines 365-373)

# Context & Application
Special forms are necessary in any language for constructs that need lazy or conditional evaluation of their arguments, such as conditionals, loops, and variable definitions.

# Examples
From the source, `while` as a special form:
```javascript
specialForms.while = (args, scope) => {
  if (args.length != 2) {
    throw new SyntaxError("Wrong number of args to while");
  }
  while (evaluate(args[0], scope) !== false) {
    evaluate(args[1], scope);
  }
  return false;
};
```
(lines 401-413)

And `define`:
```javascript
specialForms.define = (args, scope) => {
  if (args.length != 2 || args[0].type != "word") {
    throw new SyntaxError("Incorrect use of define");
  }
  let value = evaluate(args[1], scope);
  scope[args[0].name] = value;
  return value;
};
```
(lines 441-448)

# Relationships
## Builds Upon
- Expression evaluation (special forms are a special case in the evaluator)
## Enables
- Control flow (if, while), variable binding (define), function definition (fun)
## Related
- Interpreter design
## Contrasts With
- Regular function calls (where all arguments are evaluated first)

# Common Errors
- **Error**: Evaluating arguments before passing them to a special form
  **Correction**: Special forms must receive unevaluated argument expressions

# Common Confusions
- **Confusion**: Special forms are functions
  **Clarification**: Special forms look like function calls syntactically but have different evaluation rules

# Source Reference
Chapter 12: Project: A Programming Language, Section "Special forms", lines 357-448 of 12-project-a-programming-language.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Multiple examples with clear explanation
- Cross-reference status: verified
