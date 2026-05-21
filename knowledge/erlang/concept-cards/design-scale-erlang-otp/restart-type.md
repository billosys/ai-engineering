---
# === CORE IDENTIFICATION ===
concept: Restart Type
slug: restart-type

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Supervisors"
chapter_number: 7
pdf_page: 188
section: "The child specification"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "RestartType"
  - "restart directive"
  - "permanent"
  - "transient"
  - "temporary"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - child-specification
extends: []
related:
  - restart-strategy
  - application-types
contrasts_with:
  - restart-strategy

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a child specification?"
  - "How do I write a supervisor and define its child specifications?"
---

# Quick Definition

The restart type is the field of a child specification that tells a supervisor whether to restart *that one child* after it terminates: `permanent` (always), `transient` (only after abnormal termination), or `temporary` (never).

# Core Definition

The `RestartType` field of a child specification tells the supervisor how to react to a child's own termination (Cesarini & Vinoski, p. 181). Setting it to `permanent` ensures the child is always restarted, irrespective of whether its termination is normal or abnormal. Setting it to `transient` restarts the child only after abnormal termination. Setting it to `temporary` means the child is never restarted after termination. In the map form (Erlang 18.0+) it is the optional `restart` key.

# Prerequisites

- **Child specification** — The restart type is one field of a child specification.

# Key Properties

1. Three values: `permanent`, `transient`, `temporary`.
2. `permanent` — always restarted, normal or abnormal termination.
3. `transient` — restarted only after abnormal termination.
4. `temporary` — never restarted.
5. It governs the fate of *one* child; it is independent of the supervisor's restart *strategy*.

# Construction / Recognition

## To Construct/Create:
1. Decide whether the child should always, sometimes, or never be restarted.
2. Place the chosen atom as the third tuple element, or the `restart` map key, of the child specification.

## To Identify/Recognize:
1. It is the third element of a child-spec tuple, or the `restart` key in the map form.

# Context & Application

- **Typical contexts**: Every child specification.
- **Common applications**: `permanent` for core long-lived services; `transient` for processes that should restart only on failure; `temporary` for short-lived dynamic children.
- **Historical/stylistic notes**: In the dynamic-children example, phone FSMs are `transient` — if a phone is shut off the worker terminates normally and is not restarted, but a crash restarts it (p. 185).

# Examples

**Example 1** (p. 175): In `frequency_sup`, both `freq_overload` and `frequency` are `permanent` workers.

**Example 2** (pp. 185, 187): In `phone_sup` and `simple_phone_sup`, phone FSM children are `transient`.

## Worked Example

A `permanent` child versus a `transient` child (pp. 175, 187):

```erlang
%% Permanent: restarted on any termination
{Module, {Module, start_link, []}, permanent, 2000, worker, [Module]}

%% Transient: restarted only after abnormal termination
{ms, {phone_fsm, start_link, []}, transient, 2000, worker, [phone_fsm]}
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- *(none)*

## Related
- **Restart strategy** — Together they determine restart behavior; the type governs one child, the strategy governs its siblings.
- **Application types** — Application `permanent`/`transient`/`temporary` types use the same names with analogous (but distinct) semantics.

## Contrasts With
- **Restart strategy** — The restart strategy decides what happens to *other* children; the restart type decides what happens to *this* child.

# Common Errors

- **Error**: Making a short-lived per-request child `permanent`.
  **Correction**: Use `temporary` (or `transient`) so a child that finishes its task is not pointlessly restarted.

# Common Confusions

- **Confusion**: Confusing `transient` here with the `transient` application type.
  **Clarification**: A `transient` child is restarted after abnormal termination; a `transient` *application* affects other applications and the VM only on abnormal termination — related names, different scopes.

# Source Reference

Chapter 7: Supervisors, "The child specification," page 181.

# Verification Notes

- Definition source: Direct adaptation from p. 181.
- Confidence rationale: HIGH — explicitly defined with all three values.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
