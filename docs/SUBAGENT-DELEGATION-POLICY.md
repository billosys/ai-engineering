# Subagent Delegation Policy — A Shareable Prompt-Engineering Note

**Audience:** Anyone using Claude Code, Claude Desktop (claude.ai), or Cowork mode who has noticed that letting Claude hand off *analytical* work to subagents produces worse results than doing the work in the main context.

**Origin:** Pattern observed repeatedly in real software engineering work (Duncan McGreggor + collaborators). This doc distills the policy and shows where to install it so your Claude instances actually follow it.

---

## The policy (this is what you install)

> **Work mode — subagent delegation.**
>
> - **Do not delegate thinking work to subagents.** This includes: code edits, design decisions, architecture choices, reasoning about tradeoffs, choosing between options, writing prose for the codebase, judging whether a finding is real, planning a task's structure, evaluating whether something is correct.
>
> - **Subagent delegation is fine for lookup work.** This includes: searching for files or symbols, grepping across a codebase, fetching documentation, listing call sites of a function, reading a file you need but haven't loaded — anything that returns information without requiring judgment about that information.
>
> - **Serial on thinking, parallel on lookup.** Thinking tasks in a multi-task job run one-at-a-time in the main context. Lookup subagents may run in parallel within a task.
>
> - **Quality over elapsed time on the thinking path.** Do not trade thinking quality for wall-clock speed. On the lookup path, parallelism is welcome.
>
> - **Phrasing to follow when planning a task:** "I will do X thinking/edit work in this context; I may delegate Y lookup if useful." Both sides explicit. Do not forbid all subagent use (hurts lookup parallelism). Do not leave the line implicit (it won't hold).

That's the whole thing. Paste it into the install location for whichever tool you use (below) and it will take effect in new conversations.

---

## Why this works

The failure mode when subagents are used for analytical work is usually one of four things, often in combination:

1. **Context loss.** The subagent doesn't see the conversation — the prompt has to be self-contained, and self-containment discards nuance.
2. **Skill loss.** Expert skills loaded in the main context (language-specific guides, style rules, project conventions) don't automatically propagate to the subagent.
3. **Brittle judgment prompts.** Writing "make the right architectural call here" for a context-free agent is harder than making the call yourself; the telephone-game attenuation is real.
4. **Integration friction.** The subagent returns a summary. The main agent then has to re-evaluate whether the summary is right, whether to accept it, whether to push back. In practice this is often *more* total judgment work than doing it directly — and done with worse information.

None of this applies to lookups, where the answer is mechanical ("does this file exist?", "where is this function called?") and the subagent's lack of context doesn't affect the result. That's why the policy draws the line exactly where it does: the kind of task, not the existence of the subagent tool.

**Explicit tradeoff.** You are trading elapsed time for quality on the thinking axis. If you care about speed more than quality for a specific task, this policy is wrong for that task. For sustained, high-quality software engineering work, the tradeoff is the right one.

---

## Install instructions by tool

### Claude Code (CLI)

CC reads `CLAUDE.md` files and treats them as standing project instructions. Two install levels:

- **Per-project:** Add a `CLAUDE.md` (or edit the existing one) at your repo root. Include a section like:

  ```markdown
  ## Subagent Delegation Policy
  
  [paste the policy block from above]
  ```

  This applies whenever CC is invoked inside that repo. Version-controlled, shared with the team.

- **Global / user-level:** Add the policy to `~/.claude/CLAUDE.md`. This applies to every CC session on your machine regardless of which repo you're in. Good as a personal default; does not travel with the code.

A section header that names the concept ("Subagent Delegation Policy" or "Work Mode") makes the instruction easier for CC to retrieve when planning a task. Don't bury it in prose.

### Claude Desktop / claude.ai (no CLI)

CD has no `CLAUDE.md` equivalent, but has two persistence channels:

- **Custom instructions / Personal preferences.** In Settings, there's a free-text box for instructions that apply to every conversation. Paste the policy block there. This is the closest analog to a user-level `CLAUDE.md`.

- **Project instructions.** If you use Projects in claude.ai, each project has its own instruction field. Paste the policy block into the project's instructions for project-scoped conversations.

### Cowork mode (Claude Desktop with the Cowork feature)

Cowork honors the CD persistence channels above *and* has a per-user preferences block that appears at the top of every conversation. If you're a Cowork user and you've been customizing that preference block, add a line-item to it referencing the policy (or paste the policy itself if you have room).

Cowork also has an auto-memory system that persists facts across conversations. The policy above can be saved as a memory entry, but note: memory is loaded via an index, so a paste-into-preferences install is more reliable for a *rule* than a memory entry — memory is for facts-to-recall, preferences is for always-apply rules.

### For one-off or high-stakes conversations

If you can't install the policy persistently (e.g., you're using a shared account, or you just want to be sure), paste the policy block at the start of your first message in the conversation. Reliability is highest when the policy is in the immediate context. Persistent install is just a scale mechanism so you don't have to paste every time.

---

## Verifying it's working

The clearest tell: watch the Task tool (or whatever the subagent-spawning tool is named in your environment). If Claude spawns a subagent for analytical work — "implement this function," "decide between these two approaches," "review this diff," "design this schema" — the policy isn't being respected. Either the install didn't land or it got overridden.

Subagents *should* be appearing for things like:
- "Find every call site of `foo()`"
- "List files matching `crates/**/*.rs` that import `bar`"
- "Grep the repo for `TODO(perf)`"
- "Read these three files and report their structure"

If you're seeing the first pattern (thinking delegation) after install, two things to try:
1. Make the policy section header more prominent and explicit. A section titled `## Subagent Delegation Policy` retrieves better than the rule buried mid-paragraph.
2. In the first message of a new conversation, explicitly reference it: *"Follow the Subagent Delegation Policy in CLAUDE.md / my custom instructions."* This primes retrieval.

---

## One caveat

This policy reflects an empirical preference grounded in observation, not a universal truth about all LLM work. Different workloads and different models may shift the balance. For pure exploratory research, rapid prototyping, or tasks where elapsed time matters more than depth, looser delegation may be right. The policy above is calibrated for **sustained, high-quality software engineering work**, where the cost of a subtly wrong judgment compounds across the project.

If your friends try this and find the tradeoff wrong for their work, that's useful information — the failure mode is specific enough to diagnose. The framework is more valuable than the specific rule.

---

*If you have improvements to this policy, send them back upstream. The current form is v1; the seven-structural-elements work on ledger discipline (separate companion research) suggests a v2 extension around effectiveness-review-of-delegations that we haven't developed yet.*
