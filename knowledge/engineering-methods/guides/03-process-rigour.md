# Process Rigour

This guide carries the process-rigour pillar split from the former AI Engineering Methodology monolith. Load it when the work needs scales of work, SDLC sequencing, ledgers, audits, anti-degradation practices, or subagent boundaries.

This guide is one part of the engineering-methods guide set:

- [01-engineering-methodology.md](./01-engineering-methodology.md) - methodology overview, role adapter, three-pillar frame, and open questions.
- [02-knowledge-substrate.md](./02-knowledge-substrate.md) - distilled knowledge substrate, forms, examples, properties, and anti-patterns.
- [03-process-rigour.md](./03-process-rigour.md) - scales of work, 9-point SDLC, ledgers, audits, anti-degradation, and subagent discipline.
- [04-operational-routing.md](./04-operational-routing.md) - practitioner disciplines and component routing for live work.
- [05-component-boundary-analysis.md](./05-component-boundary-analysis.md) - applied-position reasoning and component-boundary analysis.
- [06-source-package-release-gates.md](./06-source-package-release-gates.md) - source, package, release, validation, and provenance gates.

## Part III — Process Rigour

### The scales of work

Before the sequence, the units it operates on. Every project decomposes along three constant scales — named once and reused across every project, because re-inventing the vocabulary each time (a "phase" here, a "chunk" there, a "milestone" in the third) is the failure this naming exists to kill. Constant names are what let a plan written for one project be picked up and read, without translation, by anyone starting the next. Largest to smallest:

- **Project** — the whole effort, with a name, a goal, and a definition of done; approached through the first three SDLC steps (research, project definition, design doc), planned by breaking it into arcs, and verified by its own project-level ledger.
- **Arc** — a set of related slices delivering one coherent capability, and the scale at which you check that the slices _compose_; a planning unit, not an execution unit, approached through arc-and-slice breakdown (SDLC step 4) and verified by its own arc-level ledger.
- **Slice** — the unit of execution: the work that lands in one branch as one mergeable diff, sized to be _held in a single model context with headroom to spare_. One slice, one ledger; approached through a per-slice implementation plan (SDLC step 5). Durable artifacts produced by the slice default to the slice's `artifacts/` directory unless the operator records an override. If a slice will not fit in one context, it was two slices.

Two more words name things _inside_ a slice, not scales of their own. A **step** is a single item in a slice's implementation plan — the fine-grained unit the ledger's rows verify; steps do not cross slice boundaries. An **iteration** is a refinement pass on a slice whose delivery misses its acceptance criteria — reserved for that and only that, never a unit of planning, budgeted at five per slice. Read together: _a project bends through several arcs; each arc is cut into slices; a slice is planned as a handful of steps, and if its delivery misses spec it is refined over a bounded number of iterations._ For collaborators arriving with Agile or Scrum habits the rough translation is project ≈ epic, arc ≈ feature, slice ≈ the branch-scale unit those frameworks never named cleanly — a courtesy for onboarding, not an adoption.

The slice rests on a bottleneck worth naming, because it is where this practice and human-centred Agile diverge most sharply. Agile's atom — the story as a branch or PR — is sized to **human review attention** (the "~500-line PR" heuristic is a proxy for what one reviewer can hold). The slice is sized to a different bottleneck: the **model's context window, minus the headroom to recover from its own mistakes**. Two consequences follow: a slice can be _larger in raw diff_ than an Agile PR and still be correctly sized, since the limit is coherence-in-context rather than lines-a-human-will-read; and the five-iteration budget _lives inside_ the context budget — so size to the comfortable two-thirds, not the ceiling.

> **The operational detail now lives behind the project-management [`../../project-management/guides/README.md`](../../project-management/guides/README.md) guide-set wayfinder** — the framework's project-management entry point. It points to focused files under [`../../project-management/guides/`](../../project-management/guides/) for the full treatment of sizing-as-judgment-call (the arc↔slice token arithmetic, the _Act → Sequence → Scene → Beat_ mnemonic, the named-but-unadopted _Saga_ tier), the **canonical planning worktree** (an orphan `planning` branch/worktree, `projectNN-<slug>` directories, `project-plan.md`, `arc-plan.md`, `slice-plan.md`, a dedicated `ledger.md` at every project/arc/slice scale, and a default per-slice `artifacts/` home for durable slice-produced artifacts), the **confirmation protocol** that stops a fresh session inventing its own folders, and the **top-down planning and bottom-up bubble-up/close machinery** (slice → arc → project) that keeps a plan honest as the work reveals what it could not have known. Anyone about to plan or close a project, arc, or slice **must read that wayfinder first and follow its required load set** — the abstract structure above is the summary; the mechanics are not to be improvised from it.

### The 9-point SDLC

The sequence below is the backbone discipline. Each step catches a different scale of drift.

1. **Research and brainstorm.** Open-ended surface mapping. What is the actual shape of the thing? What are the neighbors, predecessors, failure modes in adjacent domains?
2. **Project definition.** Bounded scope. What are we doing, what are we not doing, and what is the smallest complete thing?
3. **Design doc.** Architectural commitments. What are the pieces, how do they fit, what are the trade-offs, what are the alternatives considered and rejected?
4. **Arc and slice breakdown.** Sequencing. Which slices land when; which are load-bearing for which.
5. **Per-slice implementation plan.** Concrete steps. What gets written, what gets tested, what gets reviewed before moving on.
6. **Self-review.** First pass by the author. Catches the embarrassing things.
7. **Peer review.** Second eyes. Catches what the author cannot see.
8. **Review feedback loop.** Iteration. Not "comment dumped, comment closed" — genuine convergence.
9. **Audits.** Independent, retrospective, evidence-based. Catches what the author and the reviewer both missed, often because they shared assumptions.

Each step catches errors at a different altitude. Research catches framing errors (we are solving the wrong problem). Design doc catches architectural errors (our structure will not hold). Implementation plan catches scope errors. Self-review catches attention errors. Peer review catches blind-spot errors. Audits catch system-level errors — the ones where every individual step looked fine and the assembled whole is broken.

Skipping a step does not just forgo its value; it routes errors of that altitude further downstream, where they are much more expensive to find.

### Ledger discipline

A running record of decisions: what, when, why, by whom. The ledger prevents re-litigation of settled questions, makes drift visible (the doc said X in an early arc; we are now doing Y — was that a conscious change or an unconscious one?), and allows handoffs between humans and across sessions without destroying context.

Without a ledger, every session reopens questions that were already answered. With one, the conversation picks up where it left off — for an LLM, for a human, for any collaborator reading later.

### CAP-style independent audits

The nuclear industry's Corrective Action Program — with analogs in aviation, medicine, and finance — is built on a specific discipline. Adapted for LLM-assisted work, it has five properties:

**Independence.** The auditor is not the doer. In practice: a separate context, a separate subagent, or a separate human. The doer cannot audit their own work, because the same attention that produced the output is the attention that would miss the defects.

**Evidence access.** The auditor can read the actual artifacts, not just the doer's summary. This is the discipline most easily corrupted — an "audit" that only reads the claim of completion is theater. The auditor must see the code, the diffs, the output.

**Severity classification.** Not all findings are equal. A typo is not a logic error. A logic error is not a contract violation. A contract violation is not a safety issue. Flattening the severity scale loses the signal.

**Trending.** Recurring findings are systemic. If the same kind of drift shows up three times, the process has a hole, not just the output.

**Closure discipline.** Findings do not just get "noted." They get resolved, explicitly, with a written disposition. "Will not fix" is a legitimate closure; "we will get to it" is not.

This practice is genuinely novel in LLM collaboration, and it is where we have found the largest gains in the quality floor. Most LLM workflows produce no independent verification — the author and the reviewer are the same attention, and the audit step is absent entirely. Adding it catches drift that was otherwise silent.

### Anti-degradation practices

Four specific habits that guard the quality floor.

**Spec-keeping.** The original spec stays visible and is diffed against what was delivered. Spec-softening — where the spec quietly moves to match what was produced — is the most common silent failure mode.

**Disclosed deferral.** If something is not done, it is named and tracked. Never buried in prose, never implied. "I did not do X" is stronger than "X is out of scope" (which is often a retcon).

**Silent-drop detection.** At the close of every slice — and again when an arc closes — diff the original scope against the delivered work. Anything missing was either disclosed (fine), deferred with rationale (fine), or dropped silently (not fine). The third category is the one the methodology is designed to eliminate.

**Writing to the floor, not the ceiling.** Name what the work actually achieves, not what it could achieve in the best case. The ceiling is aspirational; the floor is what the collaborator can rely on.

### Subagents: leverage versus hazard

Subagents — dispatched contexts with a subset of tools and a narrow scope — can be a genuine force multiplier. They can also silently destroy quality in ways the parent context does not notice.

They help when the subtask is clearly scoped with explicit success criteria; when the parent can meaningfully evaluate what the subagent returns (not just accept the summary); when the work is genuinely parallelizable, with independent outputs that do not require integrated context; and when a style reference or example is provided, so the subagent's output is stylistically coherent with the whole.

They hurt when the parent cannot evaluate the subagent's output because the parent did not do the reading itself; when synthesis is delegated — the subagent summarizes and the parent stitches summaries together, losing the ground truth; when the parent becomes a coordinator instead of an author, and coherence drifts across the fan-out; and when quality control is assumed, not verified, because each subagent "looked fine."

Cognition's _Don't Build Multi-Agents_ (Walden Yan, June 2025) is the reference critique for the failure mode. The core observation: multi-agent systems degrade because context is lost at every handoff, and no individual agent has the whole picture.

The alternative when possible is to keep the work in a single context where coherence is preserved, and use subagents only for subtasks that can be independently verified on return.

The honest note on this document: portions of the Rust regeneration were done by dispatched subagents. Where that was done with a clear spec, a style reference, and evidence-returned verification, it held. Where it was not — and a handful of cases on early chapters were not — there has been subsequent drift that independent audits have had to catch. We consider this an ongoing calibration, not a solved problem.

---
