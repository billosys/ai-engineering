---
# === CORE IDENTIFICATION ===
concept: Cyclic Restart
slug: cyclic-restart

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Supervisors"
chapter_number: 7
pdf_page: 188
section: "Supervision Trees"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cyclic restarts"
  - "restart loop"
  - "restart escalation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
extends: []
related:
  - restart-intensity-and-period
  - error-kernel
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a supervisor?"
  - "How do I design a system around the error-kernel pattern?"
---

# Quick Definition

A cyclic restart is when restarting a process after an abnormal termination does not fix the underlying problem, so the process crashes and is restarted again, repeatedly. Supervisors bound and escalate cyclic restarts via the restart intensity and period.

# Core Definition

Cyclic restarts happen when restarting a process after an abnormal termination does not solve the problem, resulting in the process crashing and restarting again (Cesarini & Vinoski, p. 172). The supervisor behavior has mechanisms to escalate cyclic restarts: if the restart intensity is exceeded within the restart period, the supervisor terminates itself with reason `shutdown`, escalating the problem to its higher-level supervisor, which may be able to solve it — for example by restarting a worker outside the failing subtree whose corrupt data was the real cause (pp. 172, 180-181).

# Prerequisites

- **Supervisor** — Cyclic restarts are a phenomenon of supervised processes.

# Key Properties

1. Occurs when a restart does not address the underlying fault.
2. The process crashes and restarts in a loop.
3. Bounded by the supervisor's restart intensity and period.
4. When the threshold is exceeded, the supervisor terminates and escalates upward.
5. Escalation can clear faults that lie outside the immediate subtree (e.g. corrupt data in another worker).

# Construction / Recognition

## To Recognize:
1. A process restarts repeatedly in a short time.
2. SASL error/progress reports show the same child crashing over and over.
3. The supervisor eventually terminates with reason `shutdown`.

## To Mitigate:
1. Set restart intensity/period so cyclic restarts escalate rather than loop forever.
2. Design restart strategies to recreate process state from known-good sources.
3. Use escalation so a higher supervisor can restart the worker that holds the real fault.

# Context & Application

- **Typical contexts**: Any supervised process whose crash cause is not resolved by a local restart.
- **Common applications**: The escalation mechanism that makes supervision trees self-healing.
- **Historical/stylistic notes**: The book traces a worst case where escalation reaches the top supervisor, takes the VM down, and `heart` (Chapter 11) reboots the node (pp. 180-181).

# Examples

**Example 1** (p. 172): Starting the coffee FSM without the `hw` module loaded — `hw:reboot/0` raises `undef`, the supervisor restarts the FSM, and the restart is cyclic until `hw` is compiled and loaded.

**Example 2** (pp. 180-181): Phone FSMs crashing because of corrupt data in the frequency handler — restarting the FSMs never helps because the fault is in a worker outside their subtree; escalation restarts the frequency server.

## Worked Example

The coffee-FSM cyclic restart from the shell (p. 172):

```text
1> my_supervisor:start(coffee_sup, [{coffee_fsm, start_link, []}]).
{ok, <0.39.0>}
=ERROR REPORT====
Error in process <0.468.0> with exit value:
{undef,[{hw,reboot,[],[]},{coffee,init,0,[....]}]}
...
2> c(hw).            %% loading hw stops the cyclic restart
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- **Error kernel** — Escalation of cyclic restarts is how the error-kernel design recovers from faults.

## Related
- **Restart intensity and period** — The mechanism that bounds cyclic restarts and triggers escalation.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Setting restart intensity so high that cyclic restarts never escalate.
  **Correction**: Choose thresholds that let a persistent fault propagate to a supervisor that can fix it.

- **Error**: Restoring process state from possibly-corrupt persistent storage after a crash.
  **Correction**: Recreate state from original, known-good sources so a restart actually clears the fault.

# Common Confusions

- **Confusion**: Thinking restarting always fixes a crash.
  **Clarification**: If the cause persists, restarts loop; the fix is escalation to a level that can address the real cause.

# Source Reference

Chapter 7: Supervisors, "Supervision Trees" and "The restart specification," pages 172, 180-181.

# Verification Notes

- Definition source: Direct adaptation from p. 172 ("Cyclic restarts happen when...").
- Confidence rationale: HIGH — explicitly defined with two worked scenarios.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
