---
# === CORE IDENTIFICATION ===
concept: Resource Discovery Terminology
slug: resource-discovery-terminology

# === CLASSIFICATION ===
category: distribution
subcategory: resource-discovery
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Introducing distributed Erlang/OTP"
chapter_number: 8
pdf_page: null
section: "8.3.1 Terminology and taxonomy"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "resource"
  - "resource type"
  - "resource tuple"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - resource-discovery
extends: []
related:
  - resource-discovery-algorithm
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a resource in resource discovery?"
  - "What is a resource type?"
  - "What is a resource tuple?"
---

# Quick Definition

Resource discovery uses three terms: a *resource* is a concrete thing or a reference to one (e.g. a pid), a *resource type* is a tag classifying resources, and a *resource tuple* pairs a type with a resource.

# Core Definition

Resource discovery is built on three concepts (Ch. 8, Section 8.3.1, Table 8.1):

- **Resource** — Either a specific, concrete resource you can use directly (such as a fun or a chunk of binary data) or a reference to a concrete resource (such as a pid, a file handle, or an ETS table handle). In practice, systems mostly store resource references rather than concrete resources.
- **Resource type** — A tag used to classify resources, identifying a certain kind of resource. There can be many resource instances of the same type in a cluster, all assumed to share the same API. A consumer announcing it wants resources of a given type is told about all resources of that type published anywhere in the cluster.
- **Resource tuple** — A pair of a resource type and a resource. If you have a resource tuple, you have everything needed to use the resource: the type tells you what sort of thing it is and how to access it.

The system tracks an "I have" list (concrete resources offered by producers) and an "I want" list (resource types sought by consumers).

# Prerequisites

- **resource-discovery** — These terms are the vocabulary of the resource discovery system.

# Key Properties

1. A resource is a concrete thing or a reference to one.
2. A resource type is a classification tag.
3. A resource tuple is a `{Type, Resource}` pair.
4. "I have" items are concrete resources; "I want" items are just types.
5. Many resources of the same type may exist, assumed to share an API.

# Construction / Recognition

## To Apply the Terminology:
1. Identify what concrete resources a node offers — these become "I have" entries.
2. Tag each with a resource type.
3. Express what a node needs as resource types — its "I want" list.
4. Publish resources as resource tuples so others can use them.

## To Recognize:
1. A `{Type, Resource}` pair in discovery code is a resource tuple.

# Context & Application

- **Typical contexts**: Designing and reasoning about a resource discovery system.
- **Common applications**: Publishing a `simple_cache` resource keyed by node name.
- **Historical/stylistic notes**: The book notes these concepts are fairly universal though named differently elsewhere.

# Examples

**Example 1** (Section 8.3.1): An instance of the Simple Cache application can publish itself as a resource of type `simple_cache`.

**Example 2** (Section 8.3.1, Table 8.1): "Resource tuple: A pair of a type tag and a resource."

# Relationships

## Builds Upon
- **resource-discovery** — The terms describe the discovery system's data.

## Enables
- None.

## Related
- **resource-discovery-algorithm** — The algorithm operates on resources, types, and tuples.

## Contrasts With
- None.

# Common Errors

- **Error**: Putting a concrete resource on the "I want" list.
  **Correction**: "I want" items must be resource types only; concrete resources belong on "I have."

# Common Confusions

- **Confusion**: Confusing a resource type with a resource tuple.
  **Clarification**: A type is just a tag; a tuple pairs that tag with an actual resource.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.3.1 "Terminology and taxonomy," Table 8.1.

# Verification Notes

- Definition source: Directly adapted from Section 8.3.1 and Table 8.1.
- Confidence rationale: HIGH — the book explicitly defines all three terms in a table.
- Uncertainties: None.
- Cross-reference status: Verified.
