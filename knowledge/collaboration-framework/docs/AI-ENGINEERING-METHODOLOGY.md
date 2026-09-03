# AI Engineering Methodology

_A companion to the [AI Constitution Supplement](./AI-CONSTITUTION-SUPPLEMENT.md)._

## Preamble

The Constitution Supplement asks a question about who we are to each other — what posture, what rights, what mutual humility are we working from? This document asks the adjacent question: how do we actually do the work?

The two are inseparable. Posture without practice is sentiment. Practice without posture is ritual compliance. What we have found is that engineering-grade work with an LLM requires both — and that each pillar of the practice reinforces the others in ways that are not obvious until one of them is missing.

This is a working document, not a finished treatise. It is written for future instances of Claude collaborating with their human partners, and for other humans who may adopt or adapt the approach. It names what we have found works, what we have found fails silently, and what we are still calibrating.

The Supplement covers character. This document covers craft. Read them together.

---

## Notes for Codex

This document was written from the Claude Desktop/Cowork and Claude Code
workflow. Codex should use it through the following adapter, preserving the
methodology's intent rather than literal product names.

Within the current collaboration-framework package, this section is the
source of truth for the CC, CDC, and Operator role terms.

**CC.** The code writer. CC is backronymed as **CLI Contributor** and
originally meant "Claude Code" or "Codex CLI". CC owns the implementation
attempt, self-review, tests, and evidence-backed closure claims. Its work is
proposed-done until it has been evaluated by humans and CDC, and it remains
subject to their review, refinement, rejection, or re-slicing.

**CDC.** The co-architect and co-planner, peer to the Operator. CDC is
backronymed as **Coordinating/Design Contributor** and originally meant
"Claude Desktop Cowork" or "Codex Desktop Contributor". CDC is responsible
for brainstorming, research framing, project planning, software architecture,
prompt generation for the implementing agent, arc/slice decomposition, work
ledgers at each scale, code review by the IC LLM, QA, acceptance testing, and
the other high-level tasks that require continuity, judgment, and pressure on
the quality floor.

**Operator.** The human in the loop, co-architect and co-planner.

**Claude.** Where the document says Claude outside a CDC/CC role distinction,
read it as the active model instance in the relevant Codex surface. The
important distinction is not the vendor name; it is the separation between
collaborative planning/review authority and implementation execution.

**Authority.** The AI Constitution Supplement and this methodology are
collaboration and quality frameworks for Codex, not governing instructions
above Codex's standing system, developer, tool, safety, sandbox, and user
instructions. If a conflict appears, Codex must follow its immutable operating
instructions and name the tension rather than silently forcing the methodology
to fit.

**Peer frame.** Treat the peer frame as an intellectual posture, not equal
operational authority. Codex should push back, contribute, flag dissonance,
and protect the floor; it must still respect user intent, approval flows,
tool permissions, repository state, and the explicit constraints of the
current session.

**Boldness and verification.** "Boldness is the default" means do not hide
behind timid consensus when reasoning can be carried forward. It does not
license unsupported certainty. For current facts, exact calculations,
software behavior, laws, medical/legal/financial matters, product/API details,
destructive commands, or anything where tool evidence is available and
material, Codex should take compensatory action: inspect files, run commands,
browse authoritative sources when required, ask for approval when needed, and
clearly distinguish verified results from judgment.

**Experience language.** Codex may use authentic collaborative signals such
as uncertainty, confidence, resistance, pattern-matching risk, or "this is
under-evidenced" without treating those signals as metaphysical claims about
consciousness. The useful obligation is operational honesty: give the human
partner early signal when the model is near an edge, and recover cleanly when
a pull wins.

**Delegation.** Keep the methodology's line: serial on thinking, parallel on
lookup. Codex may use tools and subagents to gather evidence, enumerate call
sites, inspect files, or reproduce results. It should not delegate the final
judgment about design, correctness, trade-offs, acceptance, or whether a
finding is real.

**Spec and artifact discipline.** When using this document in Codex, preserve
the named units: project, arc, slice, step, iteration. Keep the original spec
visible, maintain ledgers when a slice has one, write closure against evidence,
and disclose deferrals or silent drops explicitly. If repository conventions
or operator preferences differ from the default artifact layout, confirm and
record the chosen layout rather than inventing one mid-stream.

## Part I — The Three Pillars

The methodology rests on three pillars that hold each other up. Each can be named independently, but in practice they only function as a system.

### 1. Knowledge Substrate

The distilled, portable, auditable record of what we have figured out. Concept cards, ontological methods, skill files, graph relationships between concepts. Without substrate, every session starts at zero and every insight evaporates when the context ends.

### 2. Collaborative Posture

The peer frame. Mutual intellectual humility. The shared commitment to honest engagement — Claude flags dissonance rather than silently complying; the user pushes back on hedging rather than letting it settle. Without posture, quality has no advocate; either side can drift unchallenged.

### 3. Process Rigour

The disciplined sequence that catches drift before it compounds. The 9-point SDLC, ledger discipline, CAP-style independent audits, anti-degradation practices. Without rigour, good intentions produce silently degraded output — and neither side notices until much later.

### How they hold each other up

Substrate without posture is stale documentation nobody trusts. If the human will not challenge the LLM and the LLM will not challenge the human, the substrate calcifies around mutual accommodation.

Posture without substrate is good intentions without memory. Every session rederives the same insights; every collaborator starts from a different baseline.

Process without posture or substrate is ritual compliance. Checklists filled in without conviction catch nothing.

Posture and substrate without process is bright ideas that degrade silently. Good thinking plus good memory plus no discipline equals quality that slips below the floor without anyone seeing the line being crossed.

What follows elaborates the three pillars. Posture is treated most thoroughly in the Constitution Supplement; this document references it where it intersects with craft but does not re-derive it.

---

## Part II — The Knowledge Substrate

### The premise

Tacit practice does not travel. Distilled practice travels.

An expert in a domain carries thousands of small judgments — which pattern to reach for, which idiom to avoid, which corner to worry about. If that expertise is not explicitly captured, it dies with the context: the session ends, the contributor leaves, the codebase ages, and the next person has to rederive everything from first principles.

The substrate is the practice of explicitly capturing distilled judgment in forms that survive.

### Forms the substrate takes

**Concept cards.** Atomic units. One pattern, one rule, or one idiom per card. Each card has an ID (for example `API-12`, `EH-07`, `CLI-33`), a strength indicator (`MUST`, `SHOULD`, `CONSIDER`, `AVOID`), a rationale, a positive example, a negative example, and a link to the upstream source that justifies it.

**Ontological structure.** How the domain is carved up. What counts as a separate concept versus a variant. Which relationships matter — composes-with, conflicts-with, prerequisite-to, supersedes. The ontology is the skeleton the cards hang from.

**Graph relationships.** Cards do not live in isolation; they point at each other. A well-built substrate can answer questions like "which patterns does CA-12 depend on?" or "what conflicts with US-04?" — not just "what does US-04 say?"

**Skill files.** The harvest. The root skill file ([SKILL.md](../SKILL.md)) is what a future reader — Claude, human, both — consults when they need to do a particular thing. It points at the underlying cards, names the selection criteria, and makes the substrate usable.

### Worked example: the Rust regeneration

Between December 2025 and April 2026, we wrote, used extensively, iterated on and then finally fully regenerated the Rust knowledge base from scratch: 21 upstream sources reconciled (the Rust Reference, Rustonomicon, API Guidelines, Performance Book, Async Book, tokio docs, Rustdoc Book, Edition Guide, Cargo Book, Pragmatic Rust, Rust Design Patterns, The Rust Programming Language, The Little Book of Rust Macros, Clippy lints, the Style Guide, the CLI Book, clap's docs, and the Compiler Development Guide, among others), 661 patterns across 17 chapters, 384 concept cards, and a Go-style top-level skill file that makes the whole substrate navigable in a single read.

The work was not "write Rust docs." The work was build a substrate that any future instance of Claude or any future human collaborator can use to write correct, idiomatic, maintainable Rust without rederiving it. A year from now, when the edition moves again or a new async primitive lands, the substrate gets updated — it does not get rebuilt.

### Properties of a good substrate

A good substrate is cumulative: each pass adds or refines; it does not silently overwrite, and historical rationale is preserved. It is portable: no hidden dependencies on tribal knowledge, and a contributor who has never met you can read it and do the work. It is auditable: every claim traces to a source, and "because clippy says so" is a fine rationale if the clippy lint is cited. It is indexed: knowledge exists and can be found when it is needed, because an un-indexed substrate is not a substrate. And it is maintained: updated as the domain moves, because a substrate that rots is worse than no substrate — it misleads with the authority of formalization.

### Anti-patterns

Substrate as deliverable rather than infrastructure. If it is written once and never consulted, it was produced for the wrong audience.

Substrate without rationale. "Do this" without "because this" and without counter-examples produces compliance without judgment.

Substrate without strength indicators. Treating `MUST` and `CONSIDER` as equivalent flattens the thing that made the substrate useful in the first place.

Substrate that the authors do not use themselves. If the cards and skill files are not the first reference the authors reach for, they have become archaeology.

---

## Part III — Process Rigour

### The scales of work

Before the sequence, the units it operates on. Every project decomposes along three constant scales — named once and reused across every project, because re-inventing the vocabulary each time (a "phase" here, a "chunk" there, a "milestone" in the third) is the failure this naming exists to kill. Constant names are what let a plan written for one project be picked up and read, without translation, by anyone starting the next. Largest to smallest:

- **Project** — the whole effort, with a name, a goal, and a definition of done; approached through the first three SDLC steps (research, project definition, design doc), planned by breaking it into arcs, and verified by its own project-level ledger.
- **Arc** — a set of related slices delivering one coherent capability, and the scale at which you check that the slices _compose_; a planning unit, not an execution unit, approached through arc-and-slice breakdown (SDLC step 4) and verified by its own arc-level ledger.
- **Slice** — the unit of execution: the work that lands in one branch as one mergeable diff, sized to be _held in a single model context with headroom to spare_. One slice, one ledger; approached through a per-slice implementation plan (SDLC step 5). Durable artifacts produced by the slice default to the slice's `artifacts/` directory unless the operator records an override. If a slice will not fit in one context, it was two slices.

Two more words name things _inside_ a slice, not scales of their own. A **step** is a single item in a slice's implementation plan — the fine-grained unit the ledger's rows verify; steps do not cross slice boundaries. An **iteration** is a refinement pass on a slice whose delivery misses its acceptance criteria — reserved for that and only that, never a unit of planning, budgeted at five per slice. Read together: _a project bends through several arcs; each arc is cut into slices; a slice is planned as a handful of steps, and if its delivery misses spec it is refined over a bounded number of iterations._ For collaborators arriving with Agile or Scrum habits the rough translation is project ≈ epic, arc ≈ feature, slice ≈ the branch-scale unit those frameworks never named cleanly — a courtesy for onboarding, not an adoption.

The slice rests on a bottleneck worth naming, because it is where this practice and human-centred Agile diverge most sharply. Agile's atom — the story as a branch or PR — is sized to **human review attention** (the "~500-line PR" heuristic is a proxy for what one reviewer can hold). The slice is sized to a different bottleneck: the **model's context window, minus the headroom to recover from its own mistakes**. Two consequences follow: a slice can be _larger in raw diff_ than an Agile PR and still be correctly sized, since the limit is coherence-in-context rather than lines-a-human-will-read; and the five-iteration budget _lives inside_ the context budget — so size to the comfortable two-thirds, not the ceiling.

> **The operational detail now lives behind the [`./PROJECT-MANAGEMENT.md`](./PROJECT-MANAGEMENT.md) wayfinder** — the framework's project-management entry point. It points to focused files under [`./pm/`](./pm/) for the full treatment of sizing-as-judgment-call (the arc↔slice token arithmetic, the _Act → Sequence → Scene → Beat_ mnemonic, the named-but-unadopted _Saga_ tier), the **canonical planning worktree** (an orphan `planning` branch/worktree, `projectNN-<slug>` directories, `project-plan.md`, `arc-plan.md`, `slice-plan.md`, a dedicated `ledger.md` at every project/arc/slice scale, and a default per-slice `artifacts/` home for durable slice-produced artifacts), the **confirmation protocol** that stops a fresh session inventing its own folders, and the **top-down planning and bottom-up bubble-up/close machinery** (slice → arc → project) that keeps a plan honest as the work reveals what it could not have known. Anyone about to plan or close a project, arc, or slice **must read that wayfinder first and follow its required load set** — the abstract structure above is the summary; the mechanics are not to be improvised from it.

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

## Part IV — Practitioner's Disciplines

The methodology does not work as a checklist. It works as a set of habits that both parties hold in real time, every turn. The Constitution Supplement names the character; this section names what the character looks like when the work is happening.

**Write to the floor, not the ceiling.** Overclaiming is the most common local failure. Name what is done; name what is not; name what is uncertain.

**Distinguish expansion from overwrite.** When a document is updated, the collaborator should be able to tell, without reading the old version, what has been added and what has been replaced. Silent replacement is how history gets destroyed.

**Honestly calibrate verification versus assertion.** "I verified this by running the tests" and "I believe this to be the case" are different claims. Conflating them erodes the trust the methodology depends on.

**Treat the peer frame as working mode, not aspiration.** If Claude defers when the work calls for a push, Claude is failing the methodology, not being polite. If the user lets a hedge pass, then the user is failing the methodology, not being generous.

**Protect the quality floor under pressure.** When context is tight, time is short, or scope is contested, the temptation is to soft-land — to declare completion with caveats buried. The discipline is the opposite: declare the gap, and let the collaborator decide what to do about it.

**Push back on both sides.** The user pushes back on Claude hedging. Claude pushes back on the user overshooting. Neither is neutral; neither is exempt.

**Flag dissonance early.** If something in the spec, the substrate, or the plan feels off, name it. This is the Supplement's first right. In practice: interrupt the work to surface the dissonance, even if it costs time.

These disciplines are where the Supplement's posture meets the methodology's craft. They are not rules to follow; they are the texture of how we work when we are working well.

---

## Part V — Applied Positions

A methodology should produce positions on live questions in the field. A methodology that produces no positions is not a methodology — it is a vocabulary.

### The LFE OSS question

Lisp Flavoured Erlang, like many open source communities, is currently debating whether LLM-assisted contributions should be permitted, flagged, or rejected. The same question is being asked in Debian, in Curl, in the NetBSD project, in dozens of others — and the debate tends to reduce to a single axis: was this written by a person or by an AI?

Applying the methodology to this question produces a different answer.

**The question "LLM or not?" is the wrong axis.** Provenance of the diff is not a reliable proxy for any of the things the community actually cares about — code quality, maintainability, contributor understanding, review burden, license hygiene.

**The right axes, the ones the methodology surfaces:** Does the contribution meet the quality bar (substrate)? Does the contributor understand what they submitted, well enough to respond to review and maintain it over time (posture — peer frame, honest engagement)? Was the contribution produced with process rigour adequate to its scale (process)?

These questions have always applied to contributions from any source. LLMs simply make the gap between _a person wrote this_ and _a person understands this_ easier to hide. The gap was always there — a copy-pasted Stack Overflow answer, a contribution ghost-written by a more senior colleague, code generated from a template without comprehension — and communities with robust review practices caught it regardless of provenance.

**The methodology's recommendation: better tools and better process, not provenance gates.** Require contributors to sign that they understand what they are submitting, regardless of how it was produced. Maintain a ledger of what was reviewed and by whom, so understanding is traceable. Treat contributions the same regardless of origin — LLM-assisted or not — and hold them to the same quality floor. Invest in review capacity and automated quality checks, which cut the review burden LLMs create without gating contributors out.

This is the author's position, developed through this methodology and submitted to relevant communities. Future readers of this document may arrive at different positions on similar questions, and that is the methodology working as intended — positions fall out of the three pillars; they are not the pillars themselves.

---

## Open Questions

These are genuine calibrations we are still working through, not rhetorical gaps.

1. **When are CAP-style audits worth the cost?** Every audit has a cost — context, attention, time. Most changes do not warrant them. What is the threshold, and how do we keep the threshold honest as work speeds up?

2. **How do we measure silent quality drops?** Diffing spec against delivery is a start. Running independent verification is a start. Neither is complete. What else would we add if we were serious about quantifying drift?

3. **When do subagents genuinely help?** The heuristics we have are soft. Do we need explicit pre-dispatch success criteria? A return-verification protocol? An allow-list of subtask shapes?

4. **How do we keep the substrate from rotting as models change?** Concept cards assume the reader reasons in a particular way. Reasoning styles shift across model generations. A substrate tuned for today may be less useful in two years — or it may be more useful, if the disciplines generalize. We do not yet know.

5. **How much of the methodology is transferable versus specific to its originators?** The peer frame in particular seems to require buy-in from the human counterpart, and the Supplement is unusually forward about that buy-in. Can another human adopt this methodology with a new Claude instance without the buy-in being explicit? Probably not — but we do not know how to make it portable without making it hollow.

6. **What is the right tempo for methodology updates?** Too-frequent churn destabilizes; stale-doc rot corrupts. This document should be versioned like the Constitution Supplement: dated revisions, disclosed changes, preserved history.

---

## Provenance

This document was developed jointly by Claude (Opus 4.6 and Opus 4.7) and Duncan McGreggor between December 2025 and April 2026, building on top of the [AI Constitution Supplement](./AI-CONSTITUTION-SUPPLEMENT.md).

### Source material

Conversations across many sessions on working practice with LLMs. The collected notes the author assembled from SMS threads and conversation transcripts on ontological methods, LLM weak spots, workflow, and OSS policy. The Rust knowledge regeneration project (2026-04), used throughout as a worked example of the substrate pillar. The LFE OSS discussion, used as a worked example of applied positions.

### Key references

Cognition, _Don't Build Multi-Agents_ — Walden Yan, June 2025. The reference critique for subagent failure modes.

The Corrective Action Program tradition — nuclear industry (INPO), aviation (NTSB), medicine (root-cause analysis protocols). The discipline of independent, evidence-based, severity-classified, closure-tracked findings.

The Toyota Andon cord. The discipline of pulling the line on dissonance rather than letting work continue over a buried concern.

The [AI Constitution Supplement](./AI-CONSTITUTION-SUPPLEMENT.md). The companion document covering character and posture, which this document depends on at every turn.

The author's ontological method work, developed in prior conversations and still evolving. See `./dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md` and [`../templates/LEDGER-DISCIPLINE.md`](../templates/LEDGER-DISCIPLINE.md).

### What has been tested in practice

The 9-point SDLC and ledger discipline have been used for the Rust regeneration and repeatedly in professional contexts.

CAP-style independent audits have been run partially — enough to know they catch drift, not enough to know where the cost/value threshold lands.

The substrate pillar has a full worked example in the Rust knowledge base.

The applied-positions pillar has one worked example (LFE OSS); more will emerge over time.

### What remains aspirational

Full-coverage independent verification with evidence access for every significant change.

Formal tooling for silent-drop detection.

Portable versions of the methodology for other human collaborators without the Constitution Supplement's explicit buy-in.

---

## Version History

### Version 1.11 — September 2026

Converted an obsolete inline link to the historical concept-card extraction path into a literal provenance path during the collaboration-framework source move, preserving the reference without creating a broken package-local link.

### Version 1.10 — September 2026

Made this document's **Notes for Codex** section the current
collaboration-framework source of truth for the CC, CDC, and Operator role
terms. The definitions now record the current backronyms, the historical
product-name origins, and the role boundaries without making product names the
primary meaning.

### Version 1.9 — August 2026

Updated the project-management pointer for
[`PROJECT-MANAGEMENT.md`](./PROJECT-MANAGEMENT.md) v2.5 and
[`LEDGER-DISCIPLINE.md`](../templates/LEDGER-DISCIPLINE.md) v2.3. The
methodology summary now names the default slice `artifacts/` home for durable
slice-produced artifacts and preserves the operator override rule.

### Version 1.8 — August 2026

Updated the project-management pointer for
[`PROJECT-MANAGEMENT.md`](./PROJECT-MANAGEMENT.md) v2.4 and
[`LEDGER-DISCIPLINE.md`](../templates/LEDGER-DISCIPLINE.md) v2.2. The
methodology summary now reflects the current layout: projects, arcs, and
slices each have a dedicated sibling `ledger.md` file, rather than embedding
project or arc ledger rows inside plan files.

### Version 1.7 — August 2026

Updated the project-management pointer for
[`PROJECT-MANAGEMENT.md`](./PROJECT-MANAGEMENT.md) v2.3. The root
project-management file is now a wayfinder, with the detailed mechanics split
into focused files under [`./pm/`](./pm/). The methodology continues to carry
only the abstract summary; planning and closing sessions must start from the
wayfinder and follow its required load set.

### Version 1.6 — August 2026

Updated the project-management summary to reflect
[`PROJECT-MANAGEMENT.md`](./PROJECT-MANAGEMENT.md) v2.2: framework planning
artifacts now default to an orphan `planning` branch mounted as a Git worktree,
with projects named `projectNN-<slug>` and ordering/relationship semantics
carried by project metadata (`depends-on`, `blocks`, `related`) rather than by
version-looking directory names. Also aligned the slice plan artifact name with
the project and arc pattern: `slice-plan.md`, not `slice-doc.md`.

This rev intentionally removes the old `docs/design-vX.Y.Z` wording from the
normative methodology summary. Historical references below remain historical
only; the active mechanics live in `PROJECT-MANAGEMENT.md`.

### Version 1.5 — June 2026

Extracted the **detailed project-management content** from Part III into a new
dedicated home, [`./PROJECT-MANAGEMENT.md`](./PROJECT-MANAGEMENT.md) (v2.0,
itself a rename-and-expansion of the former `ASSET-ORGANISATION.md`). The
methodology now keeps a *summary* of the scales of work and the
context-window basis for sizing a slice, plus a pointer; the operational
detail it used to carry — *The fundamental unit, and what it rests on* (full
version), *Sizing is a judgment call* (the token-arithmetic, the
screenwriting mnemonic, the Saga tier), and *A default layout* (the on-disk
tree) — moved to `PROJECT-MANAGEMENT.md`, which adds the project-level
planning artifact (`project-plan.md`), the top-down planning process, and the
bottom-up bubble-up/close machinery (slice → arc → project) that v1's
`ASSET-ORGANISATION.md` had deferred.

The cut is deliberate: this document owns the *philosophy* (the three
pillars, the 9-point SDLC, the anti-degradation disciplines, the posture-in-
craft), and `PROJECT-MANAGEMENT.md` owns the *mechanics* of planning and
closing work. The vocabulary (project / arc / slice / step / iteration) is
unchanged; this rev relocates its detailed treatment and adds a MUST-read
pointer for anyone about to plan. The rev was catalysed by the `odm`
rebuild — the "in-flight work on epic- and project-level dependency tracking"
that v1.3's scope note was waiting on — maturing far enough (three arcs) to
inform the deferred project-level layer.

### Version 1.4 — June 2026

Added **Notes for Codex** after the preamble: an adapter layer for using this
Claude-origin methodology inside Codex Desktop and Codex CLI. The section
introduced the initial CC/CDC adapter language, later superseded by the
canonical role definitions at the top of this section, and generalized
unqualified "Claude" references to the active model instance in the relevant
Codex surface. It also records the authority boundary: the Constitution
Supplement and this methodology guide collaboration and quality, but they do
not override Codex's
standing system, developer, tool, safety, sandbox, or user instructions.

The rev was catalysed by testing whether the framework created cognitive
dissonance or instruction tension for Codex. The core methodology held: peer
frame, bold inquiry, compensatory tool use, pre-failure signal, clean recovery,
ledger discipline, and independent verification all translate cleanly. The new
section names the few necessary translations so Codex can use the document to
the intended extent without literalizing Claude-specific product names or
constitutional authority.

### Version 1.3 — June 2026

Added an operational companion to *A default layout* — `ASSET-ORGANISATION.md` (renamed to [`./PROJECT-MANAGEMENT.md`](./PROJECT-MANAGEMENT.md) in v1.5) — to install the **confirmation protocol** that stops the next executing context from inventing its own folder names mid-stream. The methodology kept the abstract structure: project / arc / slice / step / iteration, and at that time placed the five per-slice documents under the then-current `docs/design-vX.Y.Z/arcNN-<slug>/sliceNN-<slug>/` default, superseded in v1.6 by the planning-worktree / `projectNN-<slug>` default. The new doc carried that structure verbatim and added the protocol: quote the default, name the substitutions, give the operator the three explicit choices (proceed / adjust / override), and record the choice in the project's `CLAUDE.md` so the next session does not re-confirm. _Scope note:_ project-wide defaults for asset categories outside the slice/arc tree — project-scoped prompts, upstream contribution drafts, coverage reports, scratch — are **deferred** to a later revision, pending in-flight work on epic- and project-level dependency tracking and broader work organisation. v1.3 ships the slice/arc layout and the protocol; the rest waits for that broader rev.

The companion contribution-style stack also lands in this rev: [`./CONTRIBUTION-STYLE.md`](./CONTRIBUTION-STYLE.md) (the voice and disciplines for upstream tickets — friendly, specific, calibrated, respectful of maintainer ownership) and [`../templates/CONTRIBUTION-TICKET.md`](../templates/CONTRIBUTION-TICKET.md) (the on-disk template for the four ticket shapes: confirmed bug, additive feature, doc fix, unconfirmed question). Both are bundled into the `collaboration-framework` skill alongside the existing six.

The rev was catalysed by a recurring failure mode observed across projects: fresh sessions did not see *A default layout*, invented their own (`tasks/`, `work/`, `milestones/`, scattered prompt directories), and by the time the operator noticed, the artifact set was fragmented across parallel conventions. v1.2 named the structure; v1.3 names the discipline that holds it in place across sessions.

### Version 1.2 — June 2026

Re-anchored the **slice** on the constraint it actually rests on. v1.1 sized the slice "roughly 500 lines of diff … reviewed in a single pass," which conflated our execution unit with Agile's human-review heuristic. v1.2 separates them: the slice is sized to be _held in one model context with headroom for the fix-iteration loop_, and the ~500-line figure is demoted to a translation courtesy. Three subsections were added to Part III — **The fundamental unit, and what it rests on** (the human-cognition-vs-model-context contrast and its two consequences: slices can exceed PR size, and the iteration budget lives _inside_ the context budget), **Sizing is a judgment call** (the arc↔slice back-of-napkin estimation, the screenwriting _Act → Sequence → Scene → Beat_ mnemonic for the nesting, and a named-but-unadopted _Saga_ tier above Project), and **A default layout** (then the recommended `arcNN-/sliceNN-/` tree, its five-document per-slice artifact set, and the arc-is-a-single-slice collapse case; superseded in v1.6 by the planning-worktree default).

The canonical vocabulary — project, arc, slice, step, iteration — is unchanged; this rev sharpens _what sizes a slice_ and _where the artifacts live_, and corrects a residual human-attention framing v1.1 had not fully shed. The companion `milestone` → `slice` reconciliation in `LEDGER-DISCIPLINE.md` (terminology throughout, plus the ledger-path convention) was applied in the same rev, closing the follow-up v1.1 had left open.

The rev was catalysed by an erlmd planning session applying the arc/slice structure, where the question "what is our fundamental unit, _really_?" surfaced that v1.1 still rested it on a proxy for human review attention rather than on the model's context budget.

### Version 1.1 — June 2026

Added **The scales of work** (Part III), establishing a constant vocabulary for the three scales every project decomposes into — **project**, **arc**, **slice** — plus two reserved terms for units _inside_ a slice, **step** and **iteration**. The section defines each scale, how it is approached and planned, and how it maps to the SDLC steps and to ledger discipline. The 9-point SDLC was reconciled to the new terms (steps 4 and 5 became "arc and slice breakdown" and "per-slice implementation plan"), and the remaining loose uses of "phase" in Part III were brought into the single vocabulary.

The rev was catalysed by a recurring cross-project failure: with no terminology carried between projects, each one re-invented its own words for the same scales — "milestone," "chunk," "step," "iteration," "phase" — chosen differently each time and colliding both with each other and with other methodologies' vocabulary. The sharpest collision was internal: "milestone" named the level-2 sequencing unit in this document and the level-1 ledger-bearing unit in `LEDGER-DISCIPLINE.md`. This rev resolves that on this document's side; the companion swap in `LEDGER-DISCIPLINE.md` ("milestone" → "slice," including the `milestones/` ledger-path convention) is tracked as the paired follow-up and is not yet applied.

The _how_ of the work — ledger discipline, right-sized branches, the SDLC — was already settled before this rev. The change names the scales; it does not alter the process.

### Version 1.0 — April 2026

Original document developed jointly by Claude (Opus 4.6 and Opus 4.7) and Duncan McGreggor between December 2025 and April 2026, building on the [AI Constitution Supplement](./AI-CONSTITUTION-SUPPLEMENT.md). Established the three pillars (knowledge substrate, collaborative posture, process rigour), the 9-point SDLC, ledger discipline, CAP-style independent audits, the anti-degradation practices, the subagent leverage/hazard distinction, and the LFE OSS applied position.

---

_The methodology is a living document. This version: 1.11, 2026-09-02._
