---
# === CORE IDENTIFICATION ===
concept: Restart Intensity and Period
slug: restart-intensity-and-period

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
section: "The restart specification"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "MaxRestart and MaxTime"
  - "MaxR and MaxT"
  - "restart frequency"
  - "restart threshold"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
  - supervisor-specification
extends: []
related:
  - restart-strategy
  - cyclic-restart
  - error-kernel
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a supervisor and define its child specifications?"
  - "What is a supervisor?"
---

# Quick Definition

The restart intensity and period are the two numbers in a supervisor's restart configuration that cap how many child restarts are allowed in a given time window before the supervisor itself gives up and terminates.

# Core Definition

The last two elements in the restart tuple are `MaxRestart` and `MaxTime`. `MaxRestart` (the *intensity*) specifies the maximum number of restarts all child processes are allowed in `MaxTime` (the *period*) seconds. If the maximum number of restarts is reached within that time, the supervisor itself terminates with reason `shutdown`, escalating the termination to its higher-level supervisor (Cesarini & Vinoski, p. 180). In effect, the supervisor is given `MaxRestart` chances to solve the problem; if crashes still occur within `MaxTime` seconds, restarting is not solving the problem and the issue is escalated upward (p. 180). In the map form (Erlang 18.0+) these are the `intensity` and `period` keys.

# Prerequisites

- **Supervisor** — Intensity and period are properties of a supervisor.
- **Supervisor specification** — They are the second and third elements of the supervisor's restart tuple/map.

# Key Properties

1. `MaxRestart`/`intensity` is the maximum number of restarts allowed.
2. `MaxTime`/`period` is the time window, in seconds, over which restarts are counted.
3. Exceeding the limit causes the supervisor to terminate with reason `shutdown`.
4. Termination escalates the problem to the higher-level supervisor.
5. They give the supervisor a bounded number of chances to recover before escalating.

# Construction / Recognition

## To Construct/Create:
1. Estimate how many restarts in what window indicate a problem restarting cannot fix.
2. Place `MaxR` and `MaxT` after the strategy in the restart tuple, or set `intensity` and `period` in the map.

## To Identify/Recognize:
1. They are the two integers following the strategy atom in `{Strategy, MaxR, MaxT}`.
2. The `intensity` and `period` keys in the map form.

# Context & Application

- **Typical contexts**: Every supervisor specification.
- **Common applications**: Bounding cyclic restarts; controlling how quickly a problem escalates up the tree.
- **Historical/stylistic notes**: The book warns against using editor-skeleton default values, which often do not reflect real operating conditions (p. 184).

# Examples

**Example 1** (p. 175): `frequency_sup` uses `{rest_for_one, 2, 3600}` — a maximum of two abnormal terminations per hour.

**Example 2** (p. 184): `phone_sup` uses `{one_for_one, 10, 3600}` — ten restarts per hour.

## Worked Example

Intensity 2, period 3600 in `frequency_sup` (p. 175):

```erlang
{ok,{{rest_for_one, 2, 3600}, ChildSpecList}}.
```

If more than two children terminate abnormally within 3,600 seconds, `frequency_sup` terminates with reason `shutdown` and its parent must handle the escalation.

# Relationships

## Builds Upon
- *(none)*

## Enables
- **Error kernel** — Escalation thresholds let unrecoverable failures rise to a supervisor that can fix them.

## Related
- **Restart strategy** — Intensity and period accompany the strategy in the restart tuple.
- **Cyclic restart** — Intensity/period are the mechanism that bounds and escalates cyclic restarts.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Setting the intensity so high that genuine cyclic restarts never escalate.
  **Correction**: Choose a threshold that lets unrecoverable problems propagate to a supervisor able to fix them.

- **Error**: Counting legitimate, frequent normal events (e.g. connectivity errors) as abnormal terminations, exhausting the intensity.
  **Correction**: Treat events that occur under normal operation as normal terminations so they do not consume the restart budget.

# Common Confusions

- **Confusion**: Thinking `MaxRestart` limits restarts of a single child.
  **Clarification**: It counts restarts of *all* children under that supervisor within the period.

# Source Reference

Chapter 7: Supervisors, "The restart specification," page 180.

# Verification Notes

- Definition source: Direct adaptation from p. 180.
- Confidence rationale: HIGH — explicitly defined as intensity and period with escalation behavior described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
