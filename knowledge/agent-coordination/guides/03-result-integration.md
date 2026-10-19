# Result Integration

Use this guide after lookup results return from a subagent or parallel tool.
Result integration is always a parent-context responsibility.

For delegation decisions, load
[`01-when-to-delegate.md`](./01-when-to-delegate.md). For context packet design,
load [`02-context-packets.md`](./02-context-packets.md). For recurring failure
modes, load [`04-anti-patterns.md`](./04-anti-patterns.md).

## Autonomous Mode contributor returns

For contributor subagents assigned under
[Autonomous Mode](../../engineering-methods/guides/01-engineering-methodology.md#autonomous-mode),
CDC inspects actual diffs and evidence, reconciles findings, and records the
verdict and follow-through against the exact candidate. Implementation returns
remain proposed-done until independent verification. An assigned independent
reviewer's reproduced checks may establish verification; do not reduce that
review to lookup or promote a summary to reproduced evidence. When CDC
implemented or repaired work, acceptance depends on another context's review
of that work and affected evidence. Preserve attribution and unresolved findings.
The remaining sections describe ordinary lookup integration.

## Parent-Context Responsibility

The parent context must independently inspect and integrate returned evidence.
Do not treat a subagent summary as verified just because it is plausible or
well formatted.

The parent context owns:

- deciding whether the delegated lookup answered the question;
- checking the cited files, lines, commands, or artifacts when they matter;
- resolving contradictions between lookup results;
- connecting the evidence to design, implementation, review, or closure
  judgment;
- recording any uncertainty or deferral.

## Integration Steps

1. Match each returned item to the original context packet.
2. Check that required paths, exclusions, and output fields were honored.
3. Spot-check or re-run enough evidence to trust the result.
4. Read primary source material yourself before making a design or edit
   decision from it.
5. Merge results into the task narrative with explicit evidence strength.
6. Name gaps, contradictions, stale assumptions, or missing scope.

## Evidence Strength

Returned lookup results are not the same thing as independent verification.
They are inputs. Treat them as asserted or attested until the parent context
checks the underlying artifact or command.

When exactness matters, cite the primary file, line, command, or generated
artifact, not the delegated summary.

## Handling Conflicts

If two lookups conflict:

- inspect the primary sources directly;
- prefer current workspace state over memory or old summaries;
- record which result was stale, incomplete, or out of scope;
- do not average contradictory claims.

If the conflict cannot be resolved within scope, preserve it as a named
uncertainty or deferral.

## Closing A Delegated Lookup

A lookup is complete when:

- the original packet's requested evidence is returned;
- exclusions were respected;
- missing areas are named;
- the parent context has inspected enough primary evidence to use the result;
- the final work product cites primary evidence rather than trusting the
  subagent summary.

If these conditions are not met, either issue a narrower follow-up lookup or do
the remaining inspection in the main context.
