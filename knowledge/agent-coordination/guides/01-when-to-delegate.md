# When To Delegate

Use this guide when deciding whether a task belongs in the main context, a
parallel lookup, or a delegated subagent. It preserves the original
thinking-versus-lookup policy while making the decision rule independently
loadable.

For self-contained handoff material, load
[`02-context-packets.md`](./02-context-packets.md). For integrating returned
evidence, load [`03-result-integration.md`](./03-result-integration.md). For
failure modes, load [`04-anti-patterns.md`](./04-anti-patterns.md).

## Core Policy

Do not delegate thinking work to subagents. Thinking work includes:

- code edits;
- design decisions;
- architecture choices;
- reasoning about tradeoffs;
- choosing between options;
- writing prose for the codebase;
- judging whether a finding is real;
- planning a task's structure;
- evaluating whether something is correct.

Subagent delegation is fine for lookup work. Lookup work includes:

- searching for files or symbols;
- grepping across a codebase;
- fetching documentation;
- listing call sites of a function;
- reading a file the main context has not loaded yet;
- enumerating evidence without judging what the evidence means.

The line is the kind of task, not the existence of a subagent tool.

## Operating Rule

Serial on thinking, parallel on lookup.

Thinking tasks in a multi-step job run one at a time in the main context.
Lookup subagents or parallel tools may run in parallel inside a task when the
result can be independently inspected.

Quality beats elapsed time on the thinking path. Do not trade thinking quality
for wall-clock speed. On the lookup path, parallelism is useful when it returns
checkable evidence.

## Planning Phrase

When planning a task, make both sides explicit:

```text
I will do X thinking/edit/review work in this context; I may delegate Y lookup
if useful.
```

Do not forbid all subagent use; that wastes lookup parallelism. Do not leave the
line implicit; it will not hold under pressure.

## Why The Boundary Exists

Thinking delegation fails in four recurring ways:

1. **Context loss.** The subagent does not see the conversation. A
   self-contained prompt discards nuance.
2. **Skill loss.** Expert skills, style rules, and project conventions loaded
   in the main context do not automatically propagate.
3. **Brittle judgment prompts.** Asking a context-starved agent to make the
   right architectural call is usually harder than making the call directly.
4. **Integration friction.** The subagent returns a summary. The main context
   still has to evaluate whether the summary is right, whether to accept it,
   and whether to push back.

None of this applies to mechanical lookups where the answer is evidence the
parent context can inspect.

## Good Delegation Shapes

Good delegated work returns evidence:

- "Find every call site of `foo()`."
- "List files matching `crates/**/*.rs` that import `bar`."
- "Grep the repo for `TODO(perf)`."
- "Read these three files and report their headings and exported symbols."

Bad delegated work asks for judgment:

- "Implement this function."
- "Decide between these approaches."
- "Review this diff."
- "Design this schema."

## Caveat

This policy is calibrated for sustained, high-quality software engineering
work, where the cost of subtly wrong judgment compounds across the project. For
pure exploratory research, rapid prototyping, or tasks where elapsed time
matters more than depth, looser delegation may be acceptable, but that is a
different operating mode and must be named explicitly.

## Component History

The agent-coordination component history lives at
[`../version-history.md`](../version-history.md).
