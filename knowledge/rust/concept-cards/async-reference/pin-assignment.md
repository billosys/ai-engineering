---
concept: Pin Assignment
slug: pin-assignment
category: type-system
subcategory: null
tier: advanced
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Assigning to a pinned pointer"
extraction_confidence: high
aliases:
  - "Pin::set"
  - "assigning pinned data"
  - "writing to a pinned pointer"
prerequisites:
  - pin-type
  - pinning
  - structural-pinning
extends:
  - pin-type
related:
  - pin-and-drop
contrasts_with: []
answers_questions:
  - "Can I assign a new value to a pinned pointer?"
  - "How does Pin::set work?"
  - "What happens to the old value when assigning into a pinned pointer?"
---

# Quick Definition

Assigning into a pinned pointer is generally safe via `Pin::set`, which drops the old pinned value (fulfilling the pinning contract) and moves a new value into the pinned place. Direct `*p = ...` syntax does not work; field-level assignment requires unsafe code and careful reasoning.

# Core Definition

"It is generally safe to assign into a pinned pointer. Although this can't be done in the usual way (`*p = ...`), it can be done using `Pin::set`. More generally, you can use unsafe code to assign into fields of the pointee." (Ch. 2, "Assigning to a pinned pointer")

"Using `Pin::set` is always safe since the previously pinned pointee will be dropped, fulfilling the pin requirements and the new pointee is not pinned until the move into the pinned place is complete." (Ch. 2, "Assigning to a pinned pointer")

"Copying one pinned object into another pinned place can only be done in unsafe code, how safety is maintained depends on the individual object. There is no general violation of the pinning requirements - the object being replaced is not moving and nor is the object being copied. However, the validity of the object being replaced may have safety requirements which are usually protected by pinning, but in this case must be established by the programmer." (Ch. 2, "Assigning to a pinned pointer")

# Prerequisites

- **Pin type** — Must understand `Pin<Ptr>` and its guarantees to understand why assignment requires special handling
- **Pinning** — The pinning contract determines what is safe during assignment
- **Structural pinning** — Field-level assignment interacts with structural pinning choices

# Key Properties

1. `*p = ...` does not work for pinned pointers — the normal assignment syntax is unavailable
2. `Pin::set` is safe and always valid — it drops the old value, fulfilling the pin contract, then moves the new value in
3. The new value is not pinned until the move into the pinned place is complete
4. Assigning into individual fields requires unsafe code but does not automatically violate pinning requirements
5. When assigning to fields, the object as a whole must remain valid (e.g., self-references must be consistent)
6. Copying one pinned object into another pinned place requires unsafe code and type-specific reasoning
7. When copying a self-referential struct, internal references must be updated to point to the new location

# Construction / Recognition

## To Replace a Pinned Value

1. Use `Pin::set(pinned_ptr, new_value)` — this is always safe
2. The old value is dropped automatically (fulfilling the pinning contract)
3. The new value is moved into the pinned place
4. The new value becomes pinned only after the move completes

## To Assign to Fields of a Pinned Value

1. This requires `unsafe` code
2. Ensure the object as a whole remains valid after the field assignment
3. Update any self-references or cross-references that may be affected by the changed field
4. The pinning requirements are not automatically violated, but other invariants may be

# Context & Application

Pin assignment comes up when implementing future combinators or state machines that need to replace their inner state while pinned. The most common safe pattern is using `Pin::set` to replace the entire value. Field-level assignment is rarer and typically only needed in hand-written futures with complex internal state transitions.

The source provides a concrete example of the subtlety: "if we have a struct with two fields `a` and `b` where `b` refers to `a`, that reference requires pinning to remain valid. If such a struct is copied into another place, then the value of `b` must be updated to point to the new `a` rather than the old one." (Ch. 2, "Assigning to a pinned pointer")

# Examples

**Safe whole-value replacement** (Ch. 2, "Assigning to a pinned pointer"):
> "`Pin::set` is always safe since the previously pinned pointee will be dropped, fulfilling the pin requirements and the new pointee is not pinned until the move into the pinned place is complete."

**Self-referential copy hazard** (Ch. 2, "Assigning to a pinned pointer"):
> "if we have a struct with two fields `a` and `b` where `b` refers to `a`, that reference requires pinning to remain valid. If such a struct is copied into another place, then the value of `b` must be updated to point to the new `a` rather than the old one."

# Relationships

## Builds Upon
- **Pin type** — `Pin::set` is a method on `Pin<Ptr>`

## Enables
(none specific)

## Related
- **Pin and drop** — `Pin::set` triggers drop of the old value, which must respect the drop guarantee
- **Structural pinning** — Field-level assignment interacts with whether fields are structurally pinned

## Contrasts With
(none)

# Common Errors

- **Error**: Using `*p = new_value` to assign into a pinned pointer.
  **Correction**: The dereference-assign syntax does not work with `Pin`. Use `Pin::set(p, new_value)` instead.

- **Error**: Copying a self-referential struct into a pinned place without updating internal references.
  **Correction**: After copying, any self-references (e.g., a field pointing to another field) must be updated to refer to the new location, not the old one.

# Common Confusions

- **Confusion**: Believing that assigning into a pinned pointer violates the pinning contract.
  **Clarification**: `Pin::set` is safe because it drops the old value first (fulfilling the contract) and the new value is not pinned until the move is complete. The contract is upheld throughout.

- **Confusion**: Thinking field-level assignment is always unsafe because the object is pinned.
  **Clarification**: Field-level assignment does not automatically violate pinning requirements, but it does require unsafe code because the programmer must ensure the object's other invariants remain satisfied.

# Source Reference

Chapter 2: Pinning, section "Assigning to a pinned pointer."

# Verification Notes

- Definition source: Direct quotations from Ch. 2, "Assigning to a pinned pointer" section (lines 226-233 of source)
- Confidence rationale: HIGH — the source provides explicit rules and examples for both safe and unsafe assignment scenarios
- Uncertainties: None
- Cross-reference status: Slugs verified against co-extracted concepts (pin-type, pinning, structural-pinning, pin-and-drop)
