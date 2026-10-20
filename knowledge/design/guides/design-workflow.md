# From a Brief to a Revised Design

Use this guide when a design task needs a clear direction before detailed
layout, colour or type work. It joins the task and its evidence to a brief,
alternatives, a reasoned choice, critique and a concrete revision. Keep it
proportionate: a small page change may need a paragraph and a sketch, while a
larger interface may need several prototypes and observations.

This is a local synthesis for varied design work. GOV.UK's user-needs guidance
is written for designing government services and calls for research and
validation in that setting. Its content-design guidance also emphasizes the
task, amount, format and placement of content. Borrow the evidence distinctions
and content-led questions that fit your work; GOV.UK branding, style rules and
public-service research requirements do not become universal design mandates.
See [Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs)
and [Understand content design](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design/).

## 1. Start with the task and what is already known

Name the work to be done, its intended output and the material already in
hand. Look at the supplied content and assets before proposing a composition.
Separate four kinds of input so a design assumption cannot quietly turn into
a finding:

| Input | Record |
|---|---|
| Observed evidence | What the supplied content, existing interface, research or task walkthrough actually shows; name its source. |
| Assumptions | What seems plausible but has not been checked, including inferred audiences and tasks. |
| Constraints | Fixed identity, content, routes, platform, schedule, implementation limits and required accessibility targets. |
| Unknowns | Questions that could change the choice, who can answer them and the next useful check. |

Do not invent personas, analytics, preferences or observed success to fill a
gap. If important evidence is unavailable, make a reversible proposal, name
the unknown and choose a real next check, such as checking an existing content
source with its owner or walking a prototype through the intended task. A
research stage is useful when it can change a consequential decision; it is
not a prerequisite before every design.

## 2. Write a small brief with observable outcomes

Turn the inputs into a brief that is short enough to guide a choice. Include
the task and content, relevant readers or users, supplied identity, constraints,
priorities and the conditions in which the design will be used. Mark each
audience or task statement as evidence or assumption. Then predeclare what you
will look for when inspecting a design and what would count as a failure.

Outcomes should describe an observable task or property, not a promise that a
design will be effective. For example: “In a keyboard walkthrough at the
target viewport, a reader can reach the primary action, identify the current
section and return to the article.” Record where focus gets lost or where the
section state becomes ambiguous. This is a check plan; its result is unknown
until someone performs it under the stated conditions.

### A compact illustrative brief

The following made-up community tool-library scenario demonstrates the format;
it is not user research or a report of real participants.

| Field | Filled brief |
|---|---|
| Task and material | Help a visitor find the next opening time and understand how to borrow. Inputs are a supplied hours sheet, a list of tools, a borrowing explainer, a logo and one existing signup URL. |
| Evidence | The supplied hours sheet contains the opening times; the supplied explainer describes borrowing steps. No interviews, search logs or analytics were supplied. |
| Assumptions | A first-time visitor may want the next opening time before browsing the whole catalogue. This has not been confirmed with visitors. |
| Constraints | Keep the name, logo, hours, signup URL and essential instructions. The first version is a responsive web page. |
| Priorities | First make opening time and borrowing route easy to find; then support browsing the tool list. |
| Planned success observations | In a content-and-prototype walkthrough, a reader can point to the next opening time and the borrowing route without interpreting a decorative label. |
| Credible failure observations | The hours are buried below a long introduction, the signup action is mistaken for the catalogue, or the borrowing steps are separated from the action that starts them. |
| Unknown and next check | Confirm the hours with the person who maintains the schedule. If the structure survives that check, ask a few intended visitors to walk through the page before treating the task assumption as supported. |

## 3. Make alternatives that change the experience

Develop at least two concepts against the same brief and constraints. Change
the hierarchy, content grouping, reading rhythm or interaction priorities so
the alternatives create meaningfully different routes through the task. Give
each concept enough shape to compare: a section order, a rough layout, a
storyboard or a small interactive prototype. A palette swap, new adjectives or
two names for the same structure do not make distinct alternatives.

For each concept, explain what receives attention first, what becomes easier,
what moves later or becomes denser, and which brief priority is better served.
Keep supplied identity and required content in view. The [layout guide](layout.md)
helps reason about hierarchy and spatial relationships; use [type](type.md)
and [colour](colour.md) when those decisions arise. Their methods are optional
and do not replace an existing project system.

| Compare | Ask |
|---|---|
| Task fit | Which priority is immediately visible, and which requires another step? |
| Content | What is grouped, separated, summarized or moved, and does that preserve meaning? |
| Rhythm and density | Where does the reader pause, scan, compare or read at length? What becomes crowded? |
| Interaction | What can be selected, expanded, searched or followed? What happens at rest and after an action? |
| Constraints and identity | Which supplied assets, labels, routes or implementation boundaries shape the concept? |
| Risk and unknowns | What assumption could reverse the choice, and what is the smallest useful check? |

## 4. Choose provisionally, then inspect actual use

Choose the concept that best serves the brief's stated priorities and
constraints. Give the reasons, the trade-off accepted and the uncertainty that
could change the choice. A provisional choice keeps work moving without
claiming that a preference or effectiveness has been tested.

Inspect a concrete artifact with the planned task and conditions: follow its
links, read its actual content, operate its controls or walk through a
prototype. Record what was inspected, by whom, at which viewport or input mode,
and what happened. If no participant or running implementation is available,
say that plainly and use a content or prototype inspection only for the
questions it can answer. Do not present an imagined walkthrough as user
research or a code sketch as a browser-tested result.

## 5. Critique one decision and revise it

Compare the artifact with the predeclared success and failure observations.
Separate required accessibility checks from taste, task fit and unproven
effectiveness. Correctness, keyboard operation, focus visibility, reading
order, text enlargement, reflow and applicable contrast checks need evidence
from the relevant artifact or running interface. An attractive impression is
not a substitute for them; a passing technical check does not decide whether
the composition serves the task.

Name at least one concrete decision to keep, change or test. Tie the revision
to what was actually observed, or to a labeled design hypothesis if it has not
been observed with users. State what changed and what the next check should
look for. Do not add a universal beauty score or call agreement among designers
user validation.

## 6. Hand off the decision and next check

Leave a compact handoff that a designer or implementer can act on:

1. **Brief:** task, supplied content and identity, constraints, priorities,
   evidence, assumptions and unknowns.
2. **Alternatives and choice:** the meaningful differences, trade-offs and
   provisional reason for the selected direction.
3. **Artifact and observation:** the design inspected, actual conditions,
   observed result and unrun checks.
4. **Revision:** the specific decision changed or retained, why, and the next
   check with its owner.

Do not turn this into an evidence bureaucracy. Link to existing source material
where possible; retain only the notes needed to make the decision, artifact,
observation and revision understandable. The [optional LFE example](examples/lfe-workflow.md)
shows this route applied to one actual homepage with a supplied project
identity. Its values and conclusions apply to LFE alone.
