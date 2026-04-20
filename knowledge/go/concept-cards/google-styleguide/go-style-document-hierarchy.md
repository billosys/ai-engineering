---
# === CORE IDENTIFICATION ===
concept: Go Style Document Hierarchy
slug: go-style-document-hierarchy

# === CLASSIFICATION ===
category: principles
subcategory: document-structure
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Overview"
chapter_number: 1
pdf_page: null
section: "About"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Go style documents"
  - "style guide hierarchy"
  - "canonical vs normative"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - clarity-principle
  - consistency-principle
  - local-consistency
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the three documents in the Google Go style system?"
  - "What does canonical mean in the context of the Go Style Guide?"
  - "What does normative mean in the context of the Go Style Guide?"
  - "Which Go style documents should I follow?"
  - "What is the difference between canonical and normative?"
---

# Quick Definition

Google's Go style system consists of three documents: the Style Guide (canonical and normative), Style Decisions (normative only), and Best Practices (neither). Each targets a different audience and carries a different level of authority.

# Core Definition

The Google Go Style system is organized into three layered documents. The **Style Guide** is both canonical (prescriptive, enduring rules that all code should follow) and normative (establishes consistency for reviewers). The **Style Decisions** document is normative but not canonical -- it provides more verbose, detailed guidance for readability mentors that may change over time. **Best Practices** is neither canonical nor normative -- it documents patterns that solve common problems but are merely encouraged. The Style Guide takes precedence if any document contradicts it.

# Prerequisites

- **Go language basics** -- Familiarity with Go syntax and tooling
- **Code review process** -- Understanding that these documents support a readability review system

# Key Properties

1. **Style Guide**: Canonical and normative; definitive foundation for all Go style at Google; targets everyone
2. **Style Decisions**: Normative but not canonical; verbose decisions on specific style points with reasoning; targets readability mentors
3. **Best Practices**: Neither canonical nor normative; evolved patterns for common problems; targets anyone interested
4. **Canonical**: Prescriptive and enduring rules; all code (old and new) should follow; not expected to change substantially
5. **Normative**: Agreed-upon style elements for reviewer consistency; may change over time as new data or patterns emerge
6. **Idiomatic**: Prevalent, familiar patterns in Go code that should be preferred over unidiomatic alternatives

# Construction / Recognition

## To Apply:
1. Start with the Style Guide for foundational, non-negotiable rules
2. Consult Style Decisions for detailed guidance on specific style points
3. Refer to Best Practices for recommended patterns that improve uniformity
4. When documents conflict, the Style Guide takes precedence

## To Recognize:
1. A rule described as "canonical" applies to all code and is expected to be enduring
2. A rule described as "normative" is for reviewer consistency but may evolve
3. Guidance in Best Practices is advisory -- encouraged but not required

# Context & Application

This hierarchy exists to balance prescriptiveness with flexibility. The canonical Style Guide is kept deliberately short because everything in it must meet a high bar. Style Decisions can be more detailed and evolve, since programmers are not expected to memorize them -- reviewers use them as a reference. Best Practices captures wisdom that has not been elevated to normative status but is broadly useful.

# Examples

**Example 1 -- Document authority levels**:

| Document          | Normative | Canonical | Primary Audience    |
|-------------------|-----------|-----------|---------------------|
| Style Guide       | Yes       | Yes       | Everyone            |
| Style Decisions   | Yes       | No        | Readability Mentors |
| Best Practices    | No        | No        | Anyone interested   |

**Example 2 -- Applying the hierarchy**:

When a Best Practices recommendation conflicts with the Style Guide, the Style Guide wins. When Style Decisions contradicts the Style Guide, the Style Guide takes precedence and Style Decisions should be updated accordingly.

# Relationships

## Related
- **clarity-principle** -- The first and most important style principle defined in the Style Guide
- **consistency-principle** -- Consistency is the tiebreaker when other principles conflict
- **local-consistency** -- Addresses what to do when the guide is silent on a point

# Common Errors

- **Error**: Treating Best Practices as mandatory rules
  **Correction**: Best Practices are encouraged, not required. Only canonical (Style Guide) rules are mandatory for all code.

- **Error**: Expecting individual programmers to memorize Style Decisions
  **Correction**: Style Decisions is a reference for readability reviewers. Authors are not expected to be familiar with every normative detail.

# Common Confusions

- **Confusion**: Thinking "normative" means the same as "canonical"
  **Clarification**: Canonical means enduring and prescriptive for all code. Normative means establishing consistency for reviewers, but the rules may change over time.

- **Confusion**: Believing the style documents are exhaustive
  **Clarification**: The documents explicitly state they are not exhaustive and do not replace good judgment.

# Source Reference

Chapter 1: Overview, Sections "About", "Documents", and "Definitions".

# Verification Notes

- Definition source: Directly from the Overview document's "About" and "Definitions" sections
- Confidence rationale: HIGH -- the document explicitly defines the hierarchy with a table and detailed definitions
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
