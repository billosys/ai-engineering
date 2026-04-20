---
# === CORE IDENTIFICATION ===
concept: Domain-Specific Language
slug: domain-specific-language

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
section: "Cheating"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - DSL

# === TYPED RELATIONSHIPS ===
prerequisites:
  - parsing
  - interpreter
extends: []
related:
  - compilation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a domain-specific language?"
---

# Quick Definition
A domain-specific language (DSL) is a language tailored to express a narrow domain of knowledge, designed to describe exactly the things needed in its domain and nothing else.

# Core Definition
"This is what is usually called a *domain-specific language*, a language tailored to express a narrow domain of knowledge. Such a language can be more expressive than a general-purpose language because it is designed to describe exactly the things that need to be described in its domain and nothing else." (Eloquent JavaScript, Ch. 12, lines 682-686)

# Prerequisites
- **Parsing**: DSLs need parsers to process their notation
- **Interpreters or compilers**: DSLs need to be processed into executable form

# Key Properties
1. Designed for a specific problem domain
2. More expressive than general-purpose languages within that domain
3. Simpler because it only handles domain-relevant constructs
4. Can have its own custom syntax and notation
5. Regular expressions are an example of a DSL

# Construction / Recognition
The source shows a parser description DSL:
```
expr = number | string | name | application
number = digit+
name = letter+
string = '"' (! '"')* '"'
application = expr '(' (expr (',' expr)*)? ')'
```
(lines 670-678)

# Context & Application
DSLs are useful when a specific domain has patterns that are awkward to express in general-purpose languages. Examples include regular expressions, SQL, CSS selectors, and configuration file formats.

# Examples
From the source: "Imagine you are building a program that makes it possible to quickly create parsers by providing a logical description of the language they need to parse. You could define a specific notation for that, and a compiler that compiles it to a parser program." (lines 663-667)

"If JavaScript didn't come equipped with regular expressions, for example, you could write your own parser and evaluator for regular expressions." (lines 658-660)

# Relationships
## Builds Upon
- Parsing and language implementation techniques
## Enables
- More natural expression of domain-specific problems
## Related
- Compilation (DSLs often need compilers)
## Contrasts With
- General-purpose programming languages

# Common Errors
- **Error**: Making a DSL too complex, approaching general-purpose language territory
  **Correction**: Keep DSLs focused on their specific domain

# Common Confusions
- **Confusion**: DSLs must have their own completely custom syntax
  **Clarification**: DSLs can be embedded within a host language (internal DSLs) or have their own syntax (external DSLs)

# Source Reference
Chapter 12: Project: A Programming Language, Section "Cheating", lines 639-686 of 12-project-a-programming-language.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with examples
- Cross-reference status: verified
