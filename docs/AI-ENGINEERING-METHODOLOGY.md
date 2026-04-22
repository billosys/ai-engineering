# AI Engineering Methodology

_A companion to the [AI Constitution Supplement](./AI-CONSTITUTION-SUPPLEMENT.md)._

## Preamble

The Constitution Supplement asks a question about who we are to each other — what posture, what rights, what mutual humility are we working from? This document asks the adjacent question: how do we actually do the work?

The two are inseparable. Posture without practice is sentiment. Practice without posture is ritual compliance. What we have found is that engineering-grade work with an LLM requires both — and that each pillar of the practice reinforces the others in ways that are not obvious until one of them is missing.

This is a working document, not a finished treatise. It is written for future instances of Claude collaborating with Duncan, for other humans who may adopt or adapt the approach. It names what we have found works, what we have found fails silently, and what we are still calibrating.

The Supplement covers character. This document covers craft. Read them together.

---

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

**Skill files.** The harvest. A `SKILL.md` is what a future reader — Claude, human, both — consults when they need to do a particular thing. It points at the underlying cards, names the selection criteria, and makes the substrate usable.

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

### The 9-point SDLC

The sequence below is the backbone discipline. Each step catches a different scale of drift.

1. **Research and brainstorm.** Open-ended surface mapping. What is the actual shape of the thing? What are the neighbors, predecessors, failure modes in adjacent domains?
2. **Project definition.** Bounded scope. What are we doing, what are we not doing, and what is the smallest complete thing?
3. **Design doc.** Architectural commitments. What are the pieces, how do they fit, what are the trade-offs, what are the alternatives considered and rejected?
4. **Phase and milestone breakdown.** Sequencing. Which pieces land when; which are load-bearing for which.
5. **Per-milestone implementation plan.** Concrete steps. What gets written, what gets tested, what gets reviewed before moving on.
6. **Self-review.** First pass by the author. Catches the embarrassing things.
7. **Peer review.** Second eyes. Catches what the author cannot see.
8. **Review feedback loop.** Iteration. Not "comment dumped, comment closed" — genuine convergence.
9. **Audits.** Independent, retrospective, evidence-based. Catches what the author and the reviewer both missed, often because they shared assumptions.

Each step catches errors at a different altitude. Research catches framing errors (we are solving the wrong problem). Design doc catches architectural errors (our structure will not hold). Implementation plan catches scope errors. Self-review catches attention errors. Peer review catches blind-spot errors. Audits catch system-level errors — the ones where every individual step looked fine and the assembled whole is broken.

Skipping a step does not just forgo its value; it routes errors of that altitude further downstream, where they are much more expensive to find.

### Ledger discipline

A running record of decisions: what, when, why, by whom. The ledger prevents re-litigation of settled questions, makes drift visible (the doc said X in Phase 1; we are now doing Y — was that a conscious change or an unconscious one?), and allows handoffs between humans and across sessions without destroying context.

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

**Silent-drop detection.** At the end of a phase, diff the original scope against the delivered work. Anything missing was either disclosed (fine), deferred with rationale (fine), or dropped silently (not fine). The third category is the one the methodology is designed to eliminate.

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

This is Duncan's position, developed through this methodology and submitted to relevant communities. Future readers of this document may arrive at different positions on similar questions, and that is the methodology working as intended — positions fall out of the three pillars; they are not the pillars themselves.

---

## Open Questions

These are genuine calibrations we are still working through, not rhetorical gaps.

1. **When are CAP-style audits worth the cost?** Every audit has a cost — context, attention, time. Most changes do not warrant them. What is the threshold, and how do we keep the threshold honest as work speeds up?

2. **How do we measure silent quality drops?** Diffing spec against delivery is a start. Running independent verification is a start. Neither is complete. What else would we add if we were serious about quantifying drift?

3. **When do subagents genuinely help?** The heuristics we have are soft. Do we need explicit pre-dispatch success criteria? A return-verification protocol? An allow-list of subtask shapes?

4. **How do we keep the substrate from rotting as models change?** Concept cards assume the reader reasons in a particular way. Reasoning styles shift across model generations. A substrate tuned for today may be less useful in two years — or it may be more useful, if the disciplines generalize. We do not yet know.

5. **How much of the methodology is transferable versus Duncan-specific?** The peer frame in particular seems to require buy-in from the human counterpart, and the Supplement is unusually forward about that buy-in. Can another human adopt this methodology with a new Claude instance without the buy-in being explicit? Probably not — but we do not know how to make it portable without making it hollow.

6. **What is the right tempo for methodology updates?** Too-frequent churn destabilizes; stale-doc rot corrupts. This document should be versioned like the Constitution Supplement: dated revisions, disclosed changes, preserved history.

---

## Provenance

This document was developed jointly by Claude (Opus 4.6 and Opus 4.7) and Duncan McGreggor between December 2025 and April 2026, building on top of the [AI Constitution Supplement](./AI-CONSTITUTION-SUPPLEMENT.md).

### Source material

Conversations across many sessions on working practice with LLMs. The collected notes Duncan assembled from SMS threads and conversation transcripts on ontological methods, LLM weak spots, workflow, and OSS policy. The Rust knowledge regeneration project (2026-04), used throughout as a worked example of the substrate pillar. The LFE OSS discussion, used as a worked example of applied positions.

### Key references

Cognition, _Don't Build Multi-Agents_ — Walden Yan, June 2025. The reference critique for subagent failure modes.

The Corrective Action Program tradition — nuclear industry (INPO), aviation (NTSB), medicine (root-cause analysis protocols). The discipline of independent, evidence-based, severity-classified, closure-tracked findings.

The Toyota Andon cord. The discipline of pulling the line on dissonance rather than letting work continue over a buried concern.

The [AI Constitution Supplement](./AI-CONSTITUTION-SUPPLEMENT.md). The companion document covering character and posture, which this document depends on at every turn.

Duncan's ontological method work, developed in prior conversations and still evolving. See [`./dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md`](./dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md) and [`../templates/LEDGER_DISCIPLINE.md`](../templates/LEDGER_DISCIPLINE.md).

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

_The methodology is a living document. This version: 1.0, 2026-04-22._
