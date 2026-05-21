---
# === CORE IDENTIFICATION ===
concept: Erlang Test Frameworks
slug: test-frameworks

# === CLASSIFICATION ===
category: testing
subcategory: test-tooling
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Profiling, Debugging, and Tracing"
chapter_number: 21
pdf_page: null
section: "Frameworks for Testing Erlang Code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Common Test Framework"
  - "property-based testing"
  - QuickCheck
  - proper

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - code-coverage-analysis
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What test frameworks are available for Erlang?"
  - "What is property-based testing?"
  - "What is the Common Test Framework?"
---

# Quick Definition

For complex projects, Erlang offers automated test frameworks: the Common Test Framework (part of OTP) for general test automation, and property-based testing tools (QuickCheck, proper) that generate random test cases from declared system properties.

# Core Definition

"For complex projects, you'll want to set up a test framework and integrate it with your build system" ("Frameworks for Testing Erlang Code"). The chapter names two approaches:

- **Common Test Framework** — part of the Erlang/OTP distribution; "It provides a complete set of tools for automating tests. The common test framework is used to test the Erlang distribution itself and to test many Ericsson products."
- **Property-based testing** — "relatively new and an extremely good technique for shaking out hard-to-find bugs." Instead of writing individual test cases, you "describe the properties of the system in a form of predicate logic"; the tools then "generate random test cases that are consistent with the properties of the system and check that these properties are not violated." Two tools exist: QuickCheck, a commercial program from the Swedish company Quviq, and `proper`, an open-source tool inspired by QuickCheck.

# Prerequisites

This is a foundational tooling concept within this chapter — it has no prerequisites among the concepts of these chapters.

# Key Properties

1. The Common Test Framework ships with Erlang/OTP
2. Common Test is used to test the Erlang distribution itself and many Ericsson products
3. Property-based testing describes system properties in predicate logic rather than writing explicit test cases
4. Property-based tools generate random test cases consistent with the declared properties
5. QuickCheck is a commercial property-based tool from Quviq
6. `proper` is an open-source property-based tool inspired by QuickCheck
7. Test frameworks are intended to be integrated with the build system for complex projects

# Construction / Recognition

## To Choose a Test Framework:

1. For general automated test suites integrated with the build, use the Common Test Framework
2. For shaking out hard-to-find bugs, use property-based testing
3. With property-based testing, declare the system's properties as predicates rather than writing per-case tests
4. Let the tool generate random cases and check the properties hold

## To Recognize:

1. Common Test suites (test modules driven by OTP's `common_test`)
2. Property declarations driving QuickCheck or `proper`

# Context & Application

- **Typical contexts**: Complex projects needing automated, repeatable testing integrated with the build
- **Common applications**: Common Test for end-to-end and integration test suites; property-based testing for finding obscure edge-case bugs
- **Historical/stylistic notes**: Property-based testing was "relatively new" at the time of writing; QuickCheck originated the approach and `proper` followed

# Examples

The chapter provides no worked code for the test frameworks; it gives a survey with references — footnote 32 points to Quviq (QuickCheck) and footnote 33 to the `proper` repository.

# Relationships

## Builds Upon

- (Foundational tooling concept within this chapter.)

## Enables

- (No card depends on this concept.)

## Related

- **Code coverage analysis** — coverage measures which lines the tests exercise; complements a test framework

## Contrasts With

- None — the two framework approaches are complementary, not opposed

# Common Errors

- **Error**: Hand-writing exhaustive test cases for edge-case-heavy code
  **Correction**: Use property-based testing — declare properties and let the tool generate random cases

# Common Confusions

- **Confusion**: Thinking property-based testing replaces example-based testing entirely
  **Clarification**: It is a complementary technique focused on hard-to-find bugs; Common Test still drives conventional automated suites

- **Confusion**: Believing QuickCheck and proper are the same tool
  **Clarification**: QuickCheck is a commercial Quviq product; `proper` is a separate open-source tool inspired by it

# Source Reference

Chapter 21: "Profiling, Debugging, and Tracing," section "Frameworks for Testing Erlang Code." See footnotes 32 (Quviq) and 33 (proper).

# Verification Notes

- Definition source: Direct quotes from "Frameworks for Testing Erlang Code"
- Confidence rationale: HIGH — both framework approaches and the named tools are explicitly described
- Uncertainties: The book gives only a survey, with no code examples
- Cross-reference status: Slugs verified against existing inventory
- Re-extraction notes: Fresh extraction; new card
