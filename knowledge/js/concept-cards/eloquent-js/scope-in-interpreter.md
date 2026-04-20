---
# === CORE IDENTIFICATION ===
concept: Scope in Interpreter
slug: scope-in-interpreter

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
section: "The environment"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - environment
  - scope object

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scope
  - object
  - prototype
extends:
  - scope
related:
  - expression-evaluation
  - runtime-environment
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is scope implemented in an interpreter?"
---

# Quick Definition
In the Egg interpreter, scope is implemented as a plain JavaScript object where property names are binding names and property values are their values, with prototype chains representing nested scopes.

# Core Definition
"The scope accepted by `evaluate` is an object with properties whose names correspond to binding names and whose values correspond to the values those bindings are bound to." "We'll use object prototype chains to represent nested scopes so that the program can add bindings to its local scope without changing the top-level scope." (Eloquent JavaScript, Ch. 12, lines 454-457, 521-523)

# Prerequisites
- **Scope**: Understanding variable scoping concepts
- **Object**: Scope is implemented as a JavaScript object
- **Prototype**: Nested scopes use prototype chains

# Key Properties
1. Global scope is an object created with `Object.create(null)`
2. Each new scope is created with `Object.create(parentScope)`
3. Name lookup traverses the prototype chain (inner to outer scope)
4. Functions create their own local scope for parameters
5. The `define` form adds bindings to the current scope object

# Construction / Recognition
```javascript
const topScope = Object.create(null);
topScope.true = true;
topScope.false = false;

function run(program) {
  return evaluate(parse(program), Object.create(topScope));
}
```
(lines 467-517)

Function scope:
```javascript
specialForms.fun = (args, scope) => {
  // ...
  return function(...args) {
    let localScope = Object.create(scope);
    for (let i = 0; i < args.length; i++) {
      localScope[params[i]] = args[i];
    }
    return evaluate(body, localScope);
  };
};
```
(lines 554-576)

# Context & Application
This technique demonstrates a simple but effective way to implement lexical scoping using JavaScript's prototype chain as the scope lookup mechanism.

# Examples
From the source, closures work because the `fun` form captures the scope:
```javascript
run(`
do(define(f, fun(a, fun(b, +(a, b)))),
   print(f(4)(5)))
`);
// -> 9
```
(lines 714-718)

"The way we have defined `fun` allows functions in Egg to reference the surrounding scope, allowing the function's body to use local values that were visible at the time the function was defined, just like JavaScript functions do." (lines 702-705)

# Relationships
## Builds Upon
- JavaScript objects and prototype chains
## Enables
- Variable resolution, closures, and nested scopes in the interpreter
## Related
- Expression evaluation (uses scope for name lookup)
## Contrasts With
- Compilation-based scope resolution (which can use fixed memory locations)

# Common Errors
- **Error**: Using `define` to update a variable in an outer scope creates a local binding instead
  **Correction**: Need a separate `set` form that traverses the prototype chain to find and update the binding

# Common Confusions
- **Confusion**: Scope objects are the same as regular JavaScript objects
  **Clarification**: They are regular objects, but used specifically to represent name-value mappings with prototype-chain-based lookup

# Source Reference
Chapter 12: Project: A Programming Language, Sections "The environment" and "Functions", lines 451-576, 740-767 of 12-project-a-programming-language.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Implementation clearly shown and explained
- Cross-reference status: verified
