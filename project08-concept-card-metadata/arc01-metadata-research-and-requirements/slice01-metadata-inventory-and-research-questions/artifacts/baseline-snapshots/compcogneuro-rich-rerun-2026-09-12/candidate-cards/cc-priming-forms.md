---
record_type: concept-card
id: cc-priming-forms
revision: 2
title: Priming: Weight-Based And Activation-Based
concept_slug: priming_forms
aliases: [weight-based priming, activation-based priming]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.8.0", path: "knowledge/concept-cards/SKILL.md"}
actor: {id: codex, role: extractor, mode: agent-direct}
created_at: 2026-09-12
source_refs: [{id: ccn-book, revision: e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d, path: "/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-07.md"}]
claim_refs: [{id: claim-priming-forms-r2, revision: 1, path: "#claim-priming-forms-r2"}]
source_support_refs: [{id: support-priming-forms-r2, revision: 1, path: "#support-priming-forms-r2"}]
cq_refs: [{id: cq-priming-forms-duration, revision: 1, path: "#cq-priming-forms-duration"}]
run_refs: [{id: run-compcogneuro-rich-rerun-20260912, revision: 1, path: "../README.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct extraction from chapter-07.md lines 153-162; simulation and external behavioral literature not inspected.", scope: "Priming subsection"}
verification_state: unassessed
reconciliation_state: unassessed
memory_admission_ref: null
---

# Concept Card: Priming: Weight-Based And Activation-Based

## Concept Boundary

This card covers the source's distinction between weight-based and
activation-based priming as nonconscious memory influences on behavior. It
excludes familiarity recognition, working memory, the `priming` simulation, and
full behavioral literature on priming.

## Quick Definition And Core Definition

Quick definition: priming is a mostly nonconscious memory effect in which prior
processing speeds or biases later behavior, and it can arise from changed
weights or residual activation.

Core definition: the source describes priming as a behavioral effect such as
faster reaction time or increased response probability following prior
exposure. Weight-based priming reflects synaptic changes and can be durable;
activation-based priming reflects residual neural activity and is short-lived.

## Prerequisites And Key Properties

- Priming can come from perceptual and association cortex, away from the
  hippocampal focus.
- The effect is typically measured behaviorally rather than accessed
  subjectively.
- Weight-based priming can persist for long periods.
- Activation-based priming disappears when the relevant neural firing dissipates.
- Hippocampal lesions do not eliminate the stem-completion priming effect
  described by the source.

## Construction Or Recognition

Recognize priming when prior exposure changes reaction time or response
probability without requiring conscious recollection. Distinguish the mechanism
when the source indicates either weight changes or residual activation.

## Context And Application

The concept appears after recognition memory as the source moves further away
from hippocampal recollection. It helps separate nonconscious memory traces
from consciously accessible familiarity and recollection.

## Examples

The source uses a stem-completion task: prior exposure to a possible completion
word can increase the likelihood that a participant later completes the stem
with that word. This example is source-reported; no experiment was independently
reviewed.

## Common Errors And Common Confusions

- Confusing priming with conscious familiarity. The source says priming is
  mostly below awareness.
- Treating activation-based priming as durable. The source says it disappears
  as neural firing dissipates.
- Treating weight decay in models as obviously compatible with long-lived
  priming. The source says year-long priming constrains such decay assumptions.

## Source Reference And Support Map

| Assertion | Locator | Support Scope |
| --- | --- | --- |
| Priming manifests as reaction-time speedup or increased response probability. | `chapter-07.md` line 153 | Direct source statement. |
| Weight-based and activation-based priming are distinguished by mechanism and duration. | `chapter-07.md` line 155 | Direct source statement. |
| Stem completion can reveal priming and survives hippocampal lesions. | `chapter-07.md` lines 157-162 | Direct source example. |

## Claims And Evidence

### Claim `claim-priming-forms-r2`

The source distinguishes weight-based priming from activation-based priming by
mechanism and persistence: weight-based priming reflects longer-lasting
learning changes, while activation-based priming reflects short-lived residual
activity.

### Support `support-priming-forms-r2`

Support is direct from `chapter-07.md` lines 153-162. The `priming` simulation
at line 166 was not run, and external behavioral studies were not inspected.

## Relationships And Competency Questions

- Specializes: memory forms, because it applies weight-based versus
  activation-based mechanisms to priming.
- Contrasts with: recognition dual process, because priming is not normally
  consciously accessible in the source's account.

### CQ `cq-priming-forms-duration`

How does the source distinguish weight-based from activation-based priming?

Expected answer scope: activation-based priming depends on residual firing and
is short-lived; weight-based priming reflects synaptic change and can last much
longer.

## Provenance And Preparation Limits

The selected source was directly readable Markdown. The simulation, figures,
and external studies were not inspected.

## Extraction Notes And Review Boundaries

This revision improves over the Arc07 compact candidate by preserving the
behavioral example, common confusions, and relationship to memory forms.

## Lifecycle And Prior Value

Candidate only. No operator acceptance, independent verification,
reconciliation, preservation, or memory admission exists.

## Handoff And Remaining Work

If the full book is processed, this card should be checked against the
simulation appendix or external priming examples only if those become in-scope.
