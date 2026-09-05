# Context Packets

Use this guide when preparing lookup work for a subagent or parallel tool. A
context packet must be self-contained enough for evidence collection without
smuggling design decisions, implementation choices, or review judgment into the
delegated task.

For the delegation decision, load
[`01-when-to-delegate.md`](./01-when-to-delegate.md). For integrating returned
evidence, load [`03-result-integration.md`](./03-result-integration.md).

## Packet Purpose

A context packet makes lookup work reproducible. It tells the delegated context
what evidence to gather, where to look, what to ignore, and how to report
results so the parent context can inspect them.

The packet does not authorize the delegated context to decide what the evidence
means.

## Required Fields

Include:

- task intent;
- repository or artifact root;
- exact files, directories, symbols, commands, or search patterns to inspect;
- exclusions such as generated, vendored, dependency, or build-output trees;
- required source instructions or local conventions relevant to the lookup;
- expected output shape;
- citation or evidence requirements;
- explicit non-goals;
- reminder that the parent context owns design, edit, review, and acceptance
  judgment.

## Good Packet Shape

```text
Find every source reference to the legacy delegation-policy filename under
knowledge/, docs/, AGENTS.md, Makefile, assets/, and workbench/release-notes/.
Exclude build/ and target/. Return file:line matches only. Do not recommend
edits; the parent context will decide route repairs.
```

This is a lookup: bounded paths, exact target, clear exclusions, checkable
output, no design decision.

## Bad Packet Shape

```text
Figure out how to split the delegation policy and update the docs.
```

This delegates thinking. It asks the subagent to choose the architecture,
perform the source edit, and decide the documentation contract.

## Keeping Packets Lean

Add enough context to make the lookup accurate, but do not paste the whole
project history when a path list and evidence contract are enough.

Good packets name:

- current task;
- relevant constraints;
- exact evidence needed;
- output format.

They avoid:

- broad "summarize everything" requests;
- design choices disguised as lookup;
- acceptance language such as "confirm this is correct";
- unbounded recursive reading without a stopping rule.

## Output Contract

Prefer outputs the parent context can verify directly:

- file lists;
- file:line matches;
- command output excerpts;
- headings and section maps;
- table rows copied from source;
- pass/fail status with the command that produced it.

Do not accept ungrounded summaries as sufficient evidence.
