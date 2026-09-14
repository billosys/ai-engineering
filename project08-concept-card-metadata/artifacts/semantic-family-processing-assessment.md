# Semantic-Family Processing Assessment And Operator Decision

Date: 2026-09-14
Status: operator-accepted planning direction, not metadata/schema acceptance.
Basis: discussion after Arc01 Slice09 CDC closure at planning `eb0669f9`.
Artifact home: project-level `artifacts/`, explicitly requested by the operator.

## Preserved Assessment

The following preserves Sofie's write-up from the discussion, excluding only
the conversation's memory-citation footer.

Yes. I think the work so far has bought us something important: **we can now distinguish genuine information loss from differences in representation, and both from things the old or new material never actually specified.** That gives the remaining work a much stronger foundation.

### What Remains

The 440 are **field-path/record-kind combinations, not 440 independent research problems**. A reference structure appearing in several record types creates several entries, even when much of its interpretation can be shared.

The remaining work falls into several overlapping areas:

- **Relationships and competency questions.** Legacy prerequisites, extensions, related concepts, contrasts, and answerable questions; current relationship edges and CQ records. This is closest to your original "what must I master before writing a fugue?" capability.
- **Extraction provenance.** Actors, methods, prompts, inputs, intended scope, actual coverage, worker contributions, and outputs.
- **Evidence and confidence.** What was assessed, by whom, against what criteria, and whether the assessment concerns extraction fidelity, source support, or something else.
- **Validation and verification.** What a check actually establishes, its target and coverage, and what it cannot prove.
- **Reconciliation, preservation, and admission.** What happens when records conflict or change, what survives, and what a decision authorizes.
- **Shared reference structures and representation differences.** Repeated fields, alternative names, scalar versus structured values, and distinctions between populated examples and template placeholders.

For scale, the remainder includes 49 pairs on relationship-edge records, 50 on competency questions, 59 on extraction runs, and 62 on concept cards. Those are **record-based counts**, not independent semantic workloads.

### What Processing Involves

For each coherent family, we need to establish:

1. **What the documents prescribe.** Read the relevant prompts, guides, templates, and field definitions.
2. **What the records actually do.** Inspect populated examples and corpus distributions, including absence, nulls, empty containers, and contradictory usages.
3. **What the difference means operationally.** Would a reader, extractor, validator, or graph importer behave differently? Could information or capability disappear?
4. **What we know versus what remains undecided.** Record supported interpretations, conflicts, and specific questions for research or design.

Take `prerequisites`: recognizing "a list of concept identifiers" is only the beginning. We also need to preserve which concept depends on which, how identifiers resolve, and whether a replacement representation supports prerequisite traversal. The current edge template specifies a direction convention, but **that alone does not demonstrate equivalent ingestion or querying**.

Conversely, a missing revision-inheritance rule should not force us to invent one. A well-supported finding that the rule is unspecified is a legitimate inventory result.

### Our Options

**1. Continue with small, sequential packets.**
This gives tight review boundaries and predictable ownership. It remains useful for genuinely difficult areas, but repeats shared context and verification work. I would retain it selectively, not make it the universal approach.

**2. Organize around semantic families, with shared evidence and explicit exceptions.**
For example, establish the common reference mechanics once, then explain each reference's particular role. A validation reference and a preservation reference may share a shape without sharing meaning or authority.

This is my preferred backbone. Every pair remains accounted for; we reduce duplicated explanation, not scrutiny.

**3. Organize around capabilities and bring selected research forward.**
Start with questions such as: "Can we preserve prerequisite traversal?" or "Can an importer distinguish source evidence from operator approval?" Trace the relevant fields across record types and use small fixtures to expose ambiguities.

This gets us closer to your actual objectives sooner. Its risk is prematurely choosing a design or overlooking less visible fields, so it needs the exhaustive inventory alongside it. Bringing research forward would also require an explicit adjustment to the current sequencing.

### What Acceptance Requires

I would keep these requirements:

- Every remaining pair has an explicit, evidence-backed treatment, either directly or through a clearly applicable shared rule with its specific role recorded.
- Documented rules, observed conventions, contradictions, and unknowns remain distinguishable.
- Claims about populated usage have actual examples or census evidence. Template-only findings are labeled accordingly.
- Important differences have concrete consequences recorded, not merely "consider during architecture."
- Coverage, evidence references, hashes, and reproduction checks pass through a reusable validation route.
- Independent review checks the semantic claims and counterexamples, not just registry completeness.
- A final combined review checks for omissions and contradictions across packets.

Crucially, **accepting this analysis does not mean accepting the future metadata design**. Design acceptance needs loss analysis and demonstrated lookup/query behavior. Skill acceptance then needs the separate real extraction runs and historical comparisons we have already committed to.

### My Recommendation

Use **family-based analysis, ordered by capability importance**, with small packets where ambiguity warrants them. I would prioritize relationships/CQs, establish reusable treatment of references and provenance, and then work through evidence and lifecycle decisions with their authority boundaries intact.

That preserves the value of everything already done while making the remaining effort increasingly cumulative. We should neither demand a finished architecture from an inventory nor let "inventory complete" stand in for proof that the resulting cards serve your purposes.

I am keeping this as a proposal for our discussion; nothing has been reopened or changed.

## Operator Assessment And Authorization

The final pause sentence above records the state when the assessment was given;
it is superseded by the operator's subsequent authorization below.

The operator agrees fully with the approach, considers the hard work to date
well spent, and explicitly wants the same tightly bounded, iterative method
used again when needed. Semantic orientation is preferred because it aligns
with the work's ontological roots. The change is a modest pivot and clearer
vision, not a repudiation of prior evidence or permission to lower standards.

The operator requests preservation of this write-up, a new project-plan version
retaining the prior planning and work, reconciliation of current-arc loose ends,
and preparation of the next arc through its first slice.

## Planning Consequences

- Preserve 115 accepted pairs and the frozen 555-pair coverage floor.
- Transfer all 440 unfinished pairs and every integration/research/UAT-design
  obligation explicitly within Project08. Transfer is not semantic completion.
- Reuse family-level evidence with per-member roles and exceptions; do not
  infer equivalence from shared spelling or shape.
- Allow targeted primary-source research during family analysis. Final
  requirements and architecture still require composed evidence.
- Keep substantive CC corrections and independent review. CDC may make small,
  attributed replay/documentation completions and rerun them, but cannot
  substitute self-authored semantics for independent semantic acceptance.
- Retain 4.x continuity, 4.9.x intent, body refinement, all fresh-run minima,
  the Complete Musician trial, five source types and conditional full-book work.
- Arc06 is next in dependency order; existing Arc02-05 identifiers remain stable.

See [transition obligations](./arc01-transition-obligations.md) and the updated
[project plan](../project-plan.md). The coverage snapshot is mechanical evidence,
not a finished family classification or a project-completion percentage.
