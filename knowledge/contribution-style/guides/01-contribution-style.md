# Contribution Style

This guide owns the voice and discipline for upstream tickets, issues, PR
notes, documentation fixes, and questions filed against projects you do not
maintain. Load it when the question is how the contribution should sound, how
strongly it can claim something, or how to respect maintainer ownership.

For the filing workflow and on-disk artifact shape, load
[02-upstream-ticket-workflow.md](./02-upstream-ticket-workflow.md). For the
copyable ticket skeleton, use the package-local
[CONTRIBUTION-TICKET.md](../templates/CONTRIBUTION-TICKET.md) template.

## Why This Exists

A ticket is a public artifact. It is read once by the maintainer who decides
whether to act, then again, sometimes years later, by the next contributor to
find it through search. Both readers have less context than the author. The
job of the ticket is to give them just enough to act without making them do
the author's reading.

Most tickets fail in one of two directions: they are too thin, with no
reproduction, evidence, or file references; or they are too thick, with a wall
of speculation and several problems entangled. Both fail the same underlying
test: they make the reader do work that was the author's job.

The engineering-methods guide
[`01-engineering-methodology.md`](../../engineering-methods/guides/01-engineering-methodology.md)
provides the spine: write to the floor, flag dissonance early, and treat
calibrated honesty as the other face of bold assertion. This guide applies
those disciplines to the public artifact of an upstream ticket.

## The Voice

Friendly, specific, calibrated, and respectful of the maintainer's time and
their ownership of the project.

Friendly means you are asking someone to spend attention on your problem.
Specific means the ticket points at concrete files, lines, examples, and
observed behavior rather than asking the maintainer to infer the issue.
Calibrated means you say exactly what you verified and exactly what you are
inferring. Respectful of ownership means the project belongs to the
maintainer: you are proposing, not directing.

The voice should sound like a note from a thoughtful colleague who knows this
codebase well, addressed to another colleague who knows it much better.

## Calibrated Honesty

A ticket that asserts more than the author knows is worse than no ticket at
all. It costs the maintainer attention and erodes trust for future tickets from
the same source. Three habits keep assertion calibrated.

### Mark Confidence Explicitly

State what you read directly and what you inferred. For any claim, ask whether
you actually verified it or whether you are extrapolating. When the answer is
extrapolating, say so.

Useful tickets distinguish "we read these three backends directly" from "we
did not line-by-line verify the remaining backend." That turns an overclaim
into a precise, checkable contribution.

### Disclose Your Own Bias

When there is more than one reasonable fix and you have a preference, label
your preference as a preference. The maintainer can then weigh your taste
against theirs without having to reverse-engineer it.

This applies to feature design choices, error-handling philosophies, naming,
and any other place where maintainer judgment is the deciding factor.

### Pre-empt The Obvious Red Herring

If there is a related-looking code path that is not the problem, say so before
the maintainer wastes time on it. The point is not to sound clever; it is to
remove a likely false trail so the actionable claim is easier to inspect.

## Question Tickets

When you suspect a bug but have not reproduced it, file a question, not a bug.
Mark it as a draft in the local header so the operator can decide whether to
file now or hold for reproduction.

The body should say what you read, what you think it implies, why you cannot
confirm it, and what experiment would settle it. Offer the maintainer the cheap
out: if they already know the answer, that answer resolves the whole ticket.

A question ticket reads as a contribution when it does disambiguation work for
the maintainer. A speculative bug report reads as noise when it asks the
maintainer to do that work.

## Respect Maintainer Ownership

You did not write this code. You are asking for the maintainer's attention,
their patience with your proposed change, and, if it lands, their future
maintenance burden.

Use "A possible fix" and "Suggested wording," not "Required change" or "Must
be implemented as." Code suggestions belong in fenced blocks labelled as
suggestions. Close sections without pressure on shape or timing.

Before proposing a new function or behavior, name the analogous pattern the
project already has. The maintainer's decision gets cheaper when the proposal
extends a pattern they already chose instead of introducing a preference that
appears to come from outside the project.

If you file several related tickets, cross-link them once they exist. Make the
cluster legible without forcing the maintainer to reconstruct the relationship.

## What To Leave Out

- Named greetings. Use a generic greeting unless there is a real relationship.
- Severity labels like "critical" or "blocker." Describe the consequence and
  let the maintainer assign the label.
- Restating the project's own docs at the maintainer. Cite specific lines, not
  concepts they already know.
- Pressure on timing. Usually say nothing about timing.
- Wall-of-text speculation. Do the reasoning yourself; if the answer is still
  uncertain, write a question ticket.
- Multiple problems in one ticket. File one ticket per problem and cross-link
  related tickets.
- Dense emoji use. Warmth is useful; excess visual noise weakens seriousness.

## Sizing

Ticket length depends on the shape, but the same rule applies everywhere:
enough to act on, nothing past that.

- Confirmed bug: usually 80 to 120 lines of Markdown.
- Additive feature: usually 150 to 200 lines because proposal shape and
  semantics need more room.
- Documentation fix: usually 30 to 60 lines, with smaller preferred.
- Unconfirmed question: usually 70 to 100 lines and marked as a draft in the
  local header.

A ticket longer than the upper bound is usually trying to do more than one
thing. A ticket shorter than the lower bound is usually missing the file-line
specificity that makes it actionable.

## Tone Under Pressure

The hardest version of this discipline is filing a ticket about a bug that has
cost significant time. Do not vent. The maintainer did not cost you time; a
bug landed where you happened to step on it.

Describe the consequence at production volume and let the maintainer feel the
cost themselves. A ticket that reads slightly frustrated will often be read as
more frustrated than written.

Read terse maintainer replies the same way. Open source maintainers carry a
heavy correspondence load; brevity is often conservation of attention, not
hostility. Reply with the same calibrated warmth you opened with.

## Relationship To The Framework

Contribution tickets are the methodology applied to a hard case: a public
artifact, addressed to a stranger, on a project you do not control. Everything
the framework asks for inside the repo, including writing to the floor,
calibrated uncertainty, disclosed deferral, and respect for ownership, applies
with double force when the audience is outside the team.

Whether a ticket was drafted with LLM assistance is not the useful axis. What
matters is whether the contributor understands what they submitted, whether it
meets the project's quality bar, and whether it was produced with rigor
appropriate to its scale.
