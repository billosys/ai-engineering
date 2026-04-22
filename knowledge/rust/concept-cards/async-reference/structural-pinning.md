---
concept: Structural Pinning
slug: structural-pinning
category: type-system
subcategory: null
tier: advanced
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Pinned fields, structural pinning, and pin projection"
extraction_confidence: high
aliases:
  - "pin projection"
  - "field-level pinning"
  - "pinning propagation"
  - "structural pin"
prerequisites:
  - pin-type
  - pinning
  - pinned-self
  - unpin-trait
extends:
  - pin-type
  - pinned-self
related:
  - pin-project-crate
  - pin-and-drop
  - self-referential-type
contrasts_with: []
answers_questions:
  - "What is structural pinning (pin projection)?"
  - "How do I implement pin projection for a struct?"
  - "What distinguishes structural pinning from non-structural pinning of fields?"
---

# Quick Definition

Structural pinning is when the pinned-ness of an aggregate object propagates to a specific field, expressed through a projection method `fn get_field(self: Pin<&mut Self>) -> Pin<&mut Field>`. Whether pinning projects to a field is a design choice made by the type implementer, not an automatic property.

# Core Definition

"Given that an object is pinned, what does that tell us about the 'pinned'-ness of its fields? The answer depends on choices made by the implementer of the datatype, there is no universal answer (indeed it can be different for different fields of the same object)." (Ch. 2, "Pinned fields, structural pinning, and pin projection")

"If the pinned-ness of an object propagates to a field, we say the field exhibits 'structural pinning' or that pinning is projected with the field. In this case there should be a projection method `fn get_field(self: Pin<&mut Self>) -> Pin<&mut Field>`. If the field is not structurally pinned, then a projection method should have signature `fn get_field(self: Pin<&mut Self>) -> &mut Field`." (Ch. 2, "Pinned fields, structural pinning, and pin projection")

"Implementing either method (or implementing similar code) requires `unsafe` code and either choice has safety implications. Pin-propagation must be consistent, a field must always be structurally pinned or not, it is nearly always unsound for a field to be structurally pinned at some times and not at others." (Ch. 2, "Pinned fields, structural pinning, and pin projection")

# Prerequisites

- **Pin type** — Must understand `Pin<Ptr>` to understand what it means for a field to be projected through `Pin`
- **Pinning** — Must understand the pinning contract to reason about what propagation means
- **Pinned self** — Projection methods take `self: Pin<&mut Self>`, requiring understanding of pinned self-types
- **Unpin trait** — Structural pinning interacts with `Unpin` — a struct cannot be `Unpin` unless all structurally pinned fields are

# Key Properties

1. Structural pinning is a per-field design decision, not automatic — different fields of the same struct can have different pinning propagation
2. Structurally pinned field: `fn get_field(self: Pin<&mut Self>) -> Pin<&mut Field>` — returns a pinned reference
3. Non-structurally pinned field: `fn get_field(self: Pin<&mut Self>) -> &mut Field` — returns a plain mutable reference
4. Pin-propagation must be consistent: a field must always be either structurally pinned or not (mixing is nearly always unsound)
5. Implementing pin projection requires `unsafe` code regardless of the choice
6. A struct can be `Unpin` even if a non-structurally-pinned field is `!Unpin`
7. A struct cannot be `Unpin` if any structurally pinned field is `!Unpin`
8. Structurally pinned fields must be dropped before they are moved, even during panics

# Construction / Recognition

## To Decide Whether a Field Should Be Structurally Pinned

1. If the field is an address-sensitive part of the aggregate (e.g., another field references into it, or it contains self-references): it **must** be structurally pinned
2. If the aggregate's pinning correctness depends on the field staying in place: it **must** be structurally pinned
3. If the field is generic content in a collection (the collection doesn't rely on the address of its items): it should **not** be structurally pinned
4. If you want the aggregate to be `Unpin` regardless of the field: the field should **not** be structurally pinned

## To Implement Pin Projection

1. Choose for each field: structurally pinned or not
2. For structurally pinned fields, write `unsafe` projection methods returning `Pin<&mut Field>`
3. For non-structurally pinned fields, write `unsafe` projection methods returning `&mut Field`
4. Ensure the aggregate's `Drop` implementation respects all structurally pinned fields
5. Ensure the aggregate's `Unpin` impl is consistent (not `Unpin` if any structurally pinned field is `!Unpin`)
6. Or use the `pin-project` crate to generate safe projections automatically

# Context & Application

Structural pinning is the mechanism by which pinning guarantees compose across data structures. It is essential when implementing custom futures that contain sub-futures as fields — the sub-futures are typically structurally pinned because the aggregate future's correctness depends on them remaining at stable addresses.

The source explains the key design principle: "Pinning should project to a field if the field is an address-sensitive part of the aggregate datatype. That is, if the aggregate being pinned depends on the field being pinned, then pinning must project to that field." (Ch. 2, "Pinned fields, structural pinning, and pin projection")

Conversely, generic collections typically do not structurally pin their contents: "for a generic collection, pinning does not need to project to its contents since the collection does not rely on their behaviour (that's because the collection cannot rely on the implementation of the generic items it contains, so the collection itself cannot rely on the addresses of its items)." (Ch. 2)

# Examples

**Structurally pinned field projection** (Ch. 2, "Pinned fields, structural pinning, and pin projection"):
> Signature: `fn get_field(self: Pin<&mut Self>) -> Pin<&mut Field>`

**Non-structurally pinned field projection** (Ch. 2, "Pinned fields, structural pinning, and pin projection"):
> Signature: `fn get_field(self: Pin<&mut Self>) -> &mut Field`

**When to structurally pin** (Ch. 2):
> "if there is a reference from another part of the aggregate into the field, or if there is a self-reference within the field, then pinning must project to the field"

**When NOT to structurally pin** (Ch. 2):
> "for a generic collection, pinning does not need to project to its contents since the collection does not rely on their behaviour"

# Relationships

## Builds Upon
- **Pin type** — Structural pinning defines how `Pin` guarantees compose through field access
- **Pinned self** — Projection methods use `self: Pin<&mut Self>`

## Enables
- **Pin project crate** — Macro crates automate the unsafe boilerplate of pin projection

## Related
- **Pin and drop** — Structurally pinned fields must be dropped before moved, requiring careful `Drop` implementations
- **Self-referential type** — Self-references between fields are the primary motivation for structural pinning

## Contrasts With
(none)

# Common Errors

- **Error**: Implementing pin projection without `unsafe`, or assuming it can be done in safe code.
  **Correction**: All pin projection implementations require `unsafe` code. Use the `pin-project` crate if you want safe projection generated for you.

- **Error**: Moving a structurally pinned field while the aggregate is pinned.
  **Correction**: Under no circumstance can code move the contents of a structurally pinned field while the aggregate is pinned. This would violate the pinning contract.

- **Error**: Implementing `Unpin` for a struct that has a structurally pinned `!Unpin` field.
  **Correction**: A struct cannot be `Unpin` unless all of its structurally pinned fields are also `Unpin`.

# Common Confusions

- **Confusion**: Believing that pinning an object automatically pins all its fields.
  **Clarification**: Pinning propagation is a per-field design choice. Some fields may be structurally pinned while others are not. There is no universal rule.

- **Confusion**: Thinking structural vs. non-structural pinning can be switched dynamically.
  **Clarification**: "Pin-propagation must be consistent, a field must always be structurally pinned or not, it is nearly always unsound for a field to be structurally pinned at some times and not at others."

- **Confusion**: Thinking a struct must be `!Unpin` if any field is `!Unpin`.
  **Clarification**: A struct can be `Unpin` even if a field is `!Unpin`, as long as that field is treated as non-structurally pinned.

# Source Reference

Chapter 2: Pinning, section "Pinned fields, structural pinning, and pin projection."

# Verification Notes

- Definition source: Direct quotations from Ch. 2, "Pinned fields, structural pinning, and pin projection" section (lines 202-213 of source)
- Confidence rationale: HIGH — the source provides detailed, explicit rules for structural pinning with clear criteria for when to use it
- Uncertainties: None
- Cross-reference status: Slugs verified against Agent A concepts (pinning, unpin-trait, self-referential-type) and co-extracted concepts (pin-type, pinned-self, pin-project-crate, pin-and-drop)
