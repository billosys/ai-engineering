---
# === CORE IDENTIFICATION ===
concept: Scope Manager
slug: scope-manager

# === CLASSIFICATION ===
category: ast-analysis
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/scope-manager-interface.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ScopeManager"
  - "eslint-scope"
  - "variable scope analysis"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - custom-rules
  - custom-parsers
extends:
  - custom-rules
related:
  - rule-context-object
  - code-path-analysis
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does ESLint track variable scopes?"
  - "What are the Scope, Variable, Reference, and Definition interfaces?"
  - "How do you find all variables declared in a scope?"
  - "How do you detect unresolved references?"
---

# Quick Definition
The ScopeManager is ESLint's interface for variable scope analysis, providing access to all scopes, variables, references, and definitions in a program through a hierarchy of Scope objects built by eslint-scope.

# Core Definition
The ScopeManager object (based on eslint-scope, a fork of escope) holds all variable scopes in a program. It provides:

**ScopeManager** methods:
- `acquire(node, inner)`: Get the scope of a given AST node
- `getDeclaredVariables(node)`: Get variables defined by a node
- `addGlobals(names)`: Add variables to global scope and resolve references (ESLint core only)

**Scope** objects represent individual scopes with types: `"block"`, `"catch"`, `"class"`, `"class-field-initializer"`, `"class-static-block"`, `"for"`, `"function"`, `"function-expression-name"`, `"global"`, `"module"`, `"switch"`, `"with"`. Key fields: `type`, `upper` (parent scope), `childScopes`, `variables`, `references`, `through` (unresolved references), `set` (Map of variable names to Variable objects), `block` (AST node), `variableScope`, `isStrict`.

**Variable** objects contain: `name`, `scope`, `identifiers` (Identifier AST nodes), `references`, `defs` (Definition objects).

**Reference** objects contain: `identifier` (AST node), `from` (scope), `resolved` (Variable or null), `writeExpr`, `init` (boolean). Methods: `isWrite()`, `isRead()`, `isWriteOnly()`, `isReadOnly()`, `isReadWrite()`.

**Definition** objects contain: `type` (one of CatchClause, ClassName, FunctionName, ImplicitGlobalVariable, ImportBinding, Parameter, Variable), `name` (Identifier node), `node` (enclosing node), `parent`.

# Prerequisites
- Understanding of JavaScript scoping rules
- Understanding of ASTs and custom ESLint rules

# Key Properties
1. **Hierarchical scopes** -- Scopes form a tree with `upper`/`childScopes` relationships
2. **Variable tracking** -- Variables have identifiers, references, and definition objects
3. **Reference resolution** -- References link to their resolved Variable or null for unresolved
4. **through references** -- Unresolved references in a scope, useful for detecting global usage
5. **Scope types** -- 12 scope types covering all JavaScript scoping mechanisms
6. **variableScope** -- Points to the nearest function/global/module scope (where `var` declarations live)

# Construction / Recognition
Accessed in rules via `context.sourceCode.getScope(node)` or `context.sourceCode.getDeclaredVariables(node)`. Custom parsers can provide a custom ScopeManager via `parseForESLint()`.

# Context & Application
The scope manager powers rules like `no-unused-vars`, `no-undef`, and `no-shadow`. It enables rules to understand variable declarations, track where variables are read or written, and identify unresolved references. Custom parsers for experimental syntax can provide custom scope analysis by returning a `scopeManager` from `parseForESLint()`.

# Examples
From extend/scope-manager-interface.md:
- `scope.through` -- array of references that could not be resolved in the scope
- `variable.defs` -- array of Definition objects showing how a variable was declared
- `reference.isWrite()` / `reference.isRead()` -- determine access patterns
- Definition types: `"Variable"` (VariableDeclarator), `"Parameter"` (function params), `"ImportBinding"` (import specifiers)

# Relationships
## Used By
- rule-context-object (via context.sourceCode.getScope())
- custom-parsers (can provide custom ScopeManager)

## Related
- code-path-analysis

# Common Errors
1. Confusing `scope.variables` with `scope.set` -- `variables` is an array, `set` is a Map
2. Looking for implicit globals in `scope.variables` -- they are in `scope.implicit.variables` on the global scope
3. Looking for references to implicit globals in `variable.references` -- they are always empty; check `scope.through` instead

# Source Reference
- extend/scope-manager-interface.md: Complete ScopeManager, Scope, Variable, Reference, and Definition interfaces

# Verification Notes
- High confidence: all interfaces and properties enumerated directly from the documentation
