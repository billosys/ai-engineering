---
# === CORE IDENTIFICATION ===
concept: Supervisor Specification
slug: supervisor-specification

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
section: "The Supervisor Specification"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "SupervisorSpec"
  - "supervisor flags"
  - "SupFlags"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
extends: []
related:
  - restart-strategy
  - restart-intensity-and-period
  - child-specification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a supervisor and define its child specifications?"
  - "What is a supervisor?"
---

# Quick Definition

The supervisor specification is the value a supervisor's `init/1` callback returns: a two-element structure pairing the restart strategy with the list of child specifications. It tells OTP how the supervisor restarts children and which children it manages.

# Core Definition

The supervisor specification is a tuple containing two elements (Cesarini & Vinoski, p. 178): the nongeneric information about the restart strategy for that particular supervisor, and the child specifications relevant to all the static workers the supervisor starts and manages. In tuple form `init/1` returns `{ok,{{RestartStrategy,MaxR,MaxT},[ChildSpec]}}`. From Erlang 18.0 onward the restart part can instead be a map: `#{strategy => strategy(), intensity => non_neg_integer(), period => pos_integer()}` — which the book recommends because all fields are named (p. 177).

# Prerequisites

- **Supervisor** — The supervisor specification is the configuration a supervisor's `init/1` returns; it has no meaning outside a supervisor.

# Key Properties

1. It has two parts: the restart tuple/map and the child specification list.
2. Tuple form: `{{RestartStrategy, MaxR, MaxT}, [ChildSpec]}`.
3. Map form (Erlang 18.0+): `{#{strategy => ..., intensity => ..., period => ...}, [ChildSpec]}`.
4. `init/1` returns it wrapped as `{ok, SupervisorSpec}`, or returns `ignore` to terminate the supervisor with reason `normal`.
5. The book recommends maps over tuples on Erlang 18.0+ for readability.
6. `supervisor:check_childspecs/1` validates the child specification list.

# Construction / Recognition

## To Construct/Create:
1. Choose a restart strategy (`one_for_one`, `one_for_all`, `rest_for_one`, `simple_one_for_one`).
2. Choose the restart intensity (`MaxR`) and period (`MaxT`).
3. Build a child specification for each statically started child.
4. Return `{ok, {SupFlags, ChildSpecList}}` from `init/1`.

## To Identify/Recognize:
1. It is the argument inside the `{ok, ...}` returned by a `supervisor` callback's `init/1`.
2. Its first element configures restarts; its second is a list of child specs.

# Context & Application

- **Typical contexts**: The return value of every supervisor callback module's `init/1`.
- **Common applications**: Declaring the restart policy and the static children of a supervisor.
- **Historical/stylistic notes**: The book warns that supervisor specs "are easy to get wrong" — programmers copy specs or use editor-skeleton defaults that do not reflect real conditions (p. 184).

# Examples

**Example 1** (p. 175): `frequency_sup`'s `init/1` returns `{ok,{{rest_for_one, 2, 3600}, ChildSpecList}}`.

**Example 2** (p. 177): The same spec written with a map: `SupFlags = #{strategy => rest_for_one, intensity => 2, period => 3600}`.

## Worked Example

Map-form supervisor specification (p. 177):

```erlang
init(_) ->
    ChildSpecList = [child(overload), child(frequency)],
    SupFlags = #{strategy => rest_for_one,
                 intensity => 2, period => 3600},
    {ok, {SupFlags, ChildSpecList}}.
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- **Supervisor** — `init/1` returns the supervisor specification to configure the supervisor.

## Related
- **Restart strategy** — The first element of the spec.
- **Restart intensity and period** — `MaxR` and `MaxT` within the restart part.
- **Child specification** — The list forming the second element.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Copying a supervisor specification from another application without adjusting intensity/period.
  **Correction**: Pick values that reflect the real conditions under which this application runs.

- **Error**: Returning a bare spec instead of `{ok, Spec}` from `init/1`.
  **Correction**: `init/1` must return `{ok, SupervisorSpec}` (or `ignore`).

# Common Confusions

- **Confusion**: Thinking the tuple and map forms behave differently.
  **Clarification**: They are equivalent; the map (Erlang 18.0+) is just a more readable encoding of the same configuration.

# Source Reference

Chapter 7: Supervisors, "The Supervisor Specification," pages 178-184. See Figure 8-6 (supervisor specification).

# Verification Notes

- Definition source: Direct adaptation from p. 178.
- Confidence rationale: HIGH — explicitly defined as a two-element structure with tuple and map forms shown.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
