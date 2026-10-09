# Design skill: proposals for 1.5 and 2.0

Date: 2026-10-08, America/Chicago. Based on the [design audit](audit-results-design.md), source baseline `dffa504e851b03b8e4746f1941068e4cc850b612`.

Status: substantive recommendations for discussion. After the audit, the Operator established Project09 as the shared audit owner, Project10 for the 1.5 foundation repair, and Project11 for the 2.0 expansion. Their project plans record the current scope and authority; this synthesis does not issue CC assignments or authorize implementation. See [the relocation record](artifact-relocation.md) for administrative changes to the original report.

## The central recommendation

Keep the skill's personality: relationships before isolated values; composition before template imitation; content before decorative machinery; expressive coherence; respect for the web as a fluid medium; and craft as care for the people using the result. Correct the idea that this personality follows inevitably from neuroscience or algebra. A capable designer uses systems to make and evaluate judgments, including judgments about when to depart from the system.

The distinctive destination is **a design practice that connects intent, content, perception, expression, interaction and implementation**. Unified design should mean those decisions support one another. It need not mean every measurement shares one ratio, every project uses one palette, or every site has the same visual grammar.

Release 1.5 should make the existing tool trustworthy. Release 2.0 should make it broadly useful throughout a designer's work. Both need concrete demonstrations; adding more reading is insufficient.

## What current systems can contribute

These are selective sources of methods, not brands to combine visually. The recommendation column is this audit's judgment; the linked documentation establishes the described source capability. Each imported idea needs a context boundary and a counterexample showing when not to use it.

| Source | Useful genetic material | Boundary to preserve |
| --- | --- | --- |
| **Every Layout, Utopia, CUBE** | Keep the existing compositional foundation; learn intrinsic sizing, fluid ranges, small primitives, and CSS organization. [Every Layout](https://every-layout.dev/rudiments/modular-scale/), [Utopia](https://utopia.fyi/blog/painting-with-a-fluid-space-palette/), [CUBE](https://cube.fyi/). | An implementation method is not the entire design process. Small primitive sets and fluid scales do not prove usability. Space multipliers need not be a geometric type scale. |
| **Material 3** | Role-based typography and a richer account of motion. Its [type roles](https://m3.material.io/styles/typography/applying-type) and [motion physics](https://m3.material.io/styles/motion) are more useful than a general claim that Google endorses geometric scales. | Pin source generation and platform. Do not import Material appearance, spring values, or implementation availability as universal web requirements. Official indexed passages were available; direct page retrieval was limited. |
| **Carbon** | Deliberate separation of productive and expressive typography; density-sensitive hierarchy. [Current type sets](https://www.carbondesignsystem.com/building-blocks/foundations/typography/type-sets) distinguish fixed product headings from fluid web treatments. | This distinction transfers; IBM Plex and its exact sizes do not become defaults. It directly challenges “fluid everything.” |
| **Polaris** | Task-oriented admin interfaces, forms, component behavior and migration verification. The [current migration guide](https://shopify.dev/docs/apps/build/app-home/migrate-from-polaris-react) checks behavior as well as markup and styling. | Shopify admin context matters. Historical React documentation and current web components are different sources; old CSS override techniques do not transfer freely through Shadow DOM. |
| **GOV.UK Design System** | The most consequential additional source: useful, tested, reusable patterns with explicit evidence and context. Its [contribution criteria](https://design-system.service.gov.uk/community/contribution-criteria/) require research including disabled users and cross-context testing. | Borrow its evidence discipline and task-first thinking; do not turn this skill into the GOV.UK aesthetic or assume government transaction patterns suit editorial exploration. |
| **Adobe Spectrum** | Applied typography with semantic roles, numeric alignment and examples of hierarchy in actual layouts. [Typography in use](https://spectrum.adobe.com/foundations/typography/applying-the-type-system) goes beyond selecting a font stack. | Treat font families, measure ranges and style rules as Spectrum decisions. They need contextual evaluation before generalization. |
| **Fluent 2** | Theme-aware semantic aliasing and a concrete alternative to mandatory three-tier tokens. [Its two-layer model](https://fluent2.microsoft.design/design-tokens) is a useful architectural comparison. | Borrow semantic separation and mode reasoning, not Microsoft branding or untested claims of accessibility inherited from tokens. |
| **USWDS** | Incremental adoption and the separation of principles, guidance and code. Its [maturity model](https://designsystem.digital.gov/maturity-model/) is useful for adapting the skill to existing projects. | Adoption is not conformance. An imported stylesheet does not prove the resulting experience works. |

There are also important sources outside component-system families. [Design Council's framework](https://www.designcouncil.org.uk/resources/framework-for-innovation/) supplies discovery, definition and iterative development. [Microsoft Inclusive Design's cognition guidance](https://inclusive.microsoft.design/articles/inclusive-design-for-cognition-guidebook) supplies a way to recognize exclusion and learn from different users. [W3C language enablement](https://www.w3.org/International/typography/) supplies script-specific typography and layout requirements. WCAG/APG, CSS specifications and DTCG provide standards and technical contracts; they should not be blended into a house aesthetic.

Further source acquisition should be question-led. For information visualization, perception and art direction, commission exact-source study against a coverage map rather than declaring another famous book “essential.” The existing Western modernist/Arts & Crafts lineage is valuable, but should be presented as a chosen lineage. It cannot stand in for all cultures, scripts, abilities, content genres or design traditions. This follows DES-002, DES-008, DES-011, DES-013 and DES-014.

## Proposed 1.5: coherent, portable foundations

Project identity: **[Project10 — Design foundations](../../project10-design-foundations/project-plan.md)** (1.5 target). Preserve the installable identity `visual-design-system`; scope work to the current skill and its direct packaging/documentation surfaces.

### Workstream A: separate method from brand

Address DES-001 and DES-010. Rewrite the description and entrypoint around generic tasks. Establish three clearly distinct layers: portable method; the adopting project's design profile; and optional case studies. A project profile records identity, audience, reading/task contexts, type/colour choices, density, themes, target platforms and constraints. It is not a new universal preset.

Remove brand names, domains, palette values and mandatory font families from normative rules. If the C&B example remains, label it historical and opt-in, and repair its factual examples before anyone can mistake it for a tested reference implementation. Existing brand context supplied by a user takes priority over sample values.

**Acceptance:** a fresh generic task does not introduce C&B names, brown/terracotta defaults, Fraunces/Literata/Plex prescriptions, or a three-site assumption. A separately supplied identity survives the task. The historical case remains traceable. **Compatibility:** explicit default-behavior change; retained opt-in case and migration note provide a bridge.

### Workstream B: repair the theory and arithmetic

Address DES-002–005, DES-007–009 and DES-012. Replace absolutes with scoped propositions. Correct interpolation, endpoint coefficients, the nonlinear colour pipeline and viewport-unit claims. Reconcile every repeated principle/table so the entrypoint cannot reintroduce an error fixed in a guide.

A revised seven-principle spine could be:

1. Make relationships intentional and legible.
2. Evaluate perception in context, with different people and conditions.
3. Name design roles and separate them from particular values.
4. Choose constraints that support the task and leave room for judgment.
5. Preserve coherence while allowing contextual expression.
6. Use spacing and other grouping cues to communicate structure.
7. Define useful invariants, then test the resulting instances.

These are proposed formulations, not adopted wording. Retain the musical and software connections where they illuminate structure; explicitly identify metaphor, shared notation and demonstrated equivalence.

**Acceptance:** every consequential scientific claim has a scoped source or is recast as a heuristic; worked examples match declared inputs; a changing-ratio midpoint is not called geometric; no unit or token system is said to guarantee accessibility. **Compatibility:** corrections plus explicit relaxation of unsupported restrictions.

### Workstream C: establish an accessibility and typesetting floor

Address DES-005, DES-006, DES-009 and DES-011. Add practical checks at the point of use, rather than a distant accessibility appendix. Cover semantics, focus, keyboard behavior, reading order, colour-independent meaning, actual foreground/background pairs, text resize/reflow/spacing, motion preferences, and robust fallbacks. Clearly distinguish geometry from behavioral components.

Make the type guide a reusable selection and typesetting procedure. Include reading conditions, role hierarchy, optical sizing, actual available axes, fallback metrics, loading failure, multilingual coverage, line breaking and readable functional text. Use modest reference examples; a complete font-delivery framework is not required for this release.

**Acceptance:** all retained examples work without hover-only access or motion-dependent information; claimed contrast pairs are computed from complete token definitions; examples remain usable with large text and missing web fonts. If no runnable interaction is supplied, identify the pattern obligations and route to maintained examples rather than presenting a positioning snippet as a complete widget. **Compatibility:** corrective additions; visual changes in formerly deficient examples are intentional.

### Workstream D: make the skill usable as a package

Address DES-010, DES-013 and DES-014. Clean converted markup; make guide links real; provide fenced, complete snippets; add an explicit short route for brief → relevant guidance → design choice → review. Keep one authority for examples and configurations to avoid duplicate numbers drifting between files. Distinguish “must read” foundations from optional intellectual depth.

Do not respond to the missing card bridge by bundling the entire library. Define what the installed skill can answer on its own, and what requires a source checkout or optional reference pack. Reconcile Makefile lists, skill-library documentation and any package-path dispositions when the payload changes.

**Acceptance:** install/unpack into a clean directory and follow every live route without repository search; all required assets/dependencies resolve; no site-rendering markup masquerades as code. Run `make check-skills`, `make check-skill-versions`, and `make check-package-paths` as applicable, plus a fresh `make design`. Structural gates complement, but do not replace, design review. **Compatibility:** local packaging/routing repair, with migration links if filenames change.

### Workstream E: repair evidence boundaries

Address DES-002, DES-007, DES-012, DES-013, DES-015 and DES-016. Build the claim/source register and a contradiction inventory across **all 233 cards**. Repair the known algebra and escaped text. Identify unavailable originals and separate sourced content from later cross-domain interpretation. Coordinate with Project08's existing concept-card work and acceptance boundaries before altering card metadata or preservation records.

A bounded 1.5 need not semantically recertify all historical cards. It must review every claim admitted into live guidance, reconcile all detected contradictions, and clearly exclude unresolved source/card assertions from its authority. If “fully self-consistent” is defined to include every claim in the entire historical corpus, expand this workstream to complete card verification; do not silently report the smaller live-skill gate as that larger result.

**Acceptance:** every audit finding has a disposition and owner; no known false statement remains normative; no unresolved card is presented as verified evidence. Missing sources remain named, with a retrieval or exclusion decision. **Compatibility:** preserve originals and review history; do not bulk migrate a schema as a side effect.

### Release composition and version decision

Sequence A and B before finalizing the rewritten guides; C and D consume those decisions; E runs through the work and gates completion. Independent review checks the composed package, not just each edited file. These workstreams can become arcs once scope is agreed; they are not issued slice assignments.

There is a real semantic-versioning question. Generalizing a skill whose current description explicitly promises C&B behavior changes its observable defaults. **1.5.0 is defensible only with an explicit compatibility interpretation**, such as correcting an accidental restriction while preserving an opt-in legacy profile and documenting migration. If consumers are promised continued automatic C&B styling, this is a major change under the repository's contract. Preserve the requested 1.5 target as a proposal and resolve that decision before implementation; do not disguise the incompatibility.

Only the owning `SKILL.md` metadata and sibling history carry the skill version. Do not insert release numbers into the new guides or example names.

## Proposed 2.0: a designer's working practice

Project identity: **[Project11 — Unified design practice](../../project11-unified-design-practice/project-plan.md)** (2.0 target). Depend on the accepted 1.5 package and its evidence boundaries. Keep web/product/editorial design as the initial operational scope; treat print, native platform specialization, spatial/industrial design and full service-design practice as future extensions rather than implying mastery through analogy.

### Capability 1: frame a design problem before choosing its appearance

Extend DES-014 into an actionable intake: who is using this, to do what, with which content and constraints; what identity already exists; which decisions are fixed; and what is unknown. Supply light paths for a small edit and deeper paths for a new experience. Teach research-question formation, evidence gathering, assumptions and synthesis without inventing personas or user findings.

**Demonstration:** turn an ambiguous brief into a content model, task priorities, explicit assumptions and several materially different concepts. Explain why a concept serves the brief; a mood board alone is not a design rationale.

### Capability 2: connect information architecture, content and interaction

Address DES-006 and DES-014 with task flows, navigation/search, progressive disclosure, readable labels and microcopy, forms and validation, status/feedback, empty/loading/error/success states, undo and recovery, permissions and interrupted work. Model a component as meaning + behavior + states + geometry + expression, rather than a styled rectangle.

**Demonstration:** design a multi-step flow through both success and recovery, with meaningful DOM/reading order and keyboard behavior. A beautiful happy-path screenshot does not pass. AI-assisted design is the workflow here; specialized AI-product interaction patterns can be an optional extension, not an assumed requirement for every project.

### Capability 3: deepen the visual craft while preserving expression

Address DES-002, DES-007, DES-011 and DES-014. Complete visual elements and composition: shape, line, texture, hierarchy, optical balance, rhythm, contrast, image direction, crop/focal point, icon meaning and consistency, illustration, motion purpose and choreography. Expand microtypography, numerical/data typography, information visualization and annotation. Use examples where restrained repetition works and examples where deliberate asymmetry works.

**Demonstration:** the same underlying system supports a literary essay, a dense working interface and an image-led collection without reducing them to interchangeable card layouts. The lesson is how their content changes the decisions, not how to apply three skins.

### Capability 4: make inclusion part of every decision

Extend the 1.5 floor using DES-005, DES-006 and DES-011. Add localization, bidirectional content, relevant script-specific shaping and punctuation, text expansion, alternate input, cognitive load, low vision, user-selected themes, and limited bandwidth/device conditions. Include ethical review of coercive patterns, misleading hierarchy, consent and attention costs.

**Demonstration:** adapt a real flow to a second script/direction and enlarged text with knowledgeable review. Simulated disability filters are aids, not substitutes for participants or assistive-technology checks. The precise supported locales and environments must be named.

### Capability 5: make system decisions explicit and maintainable

Address DES-001, DES-008, DES-010 and DES-013. Teach choosing token scope, aliasing, optional component tokens, theme/density/mode matrices, ownership, naming, deprecation, governance and contributions. Provide examples of change impact and migration. Add a tool-neutral design/code handoff with validated DTCG export where used; define who owns values and how divergent tool representations are reconciled.

**Demonstration:** a change in semantic intent propagates to the correct components across modes; a local component exception does not alter unrelated contexts. Detect unresolved references, cycles and incompatible mappings. Do not pretend every tool preserves every token feature losslessly.

### Capability 6: critique, prototype, observe and revise

Address DES-002, DES-012 and DES-014. Make critique evidence-bearing: locate the issue, name the user/design consequence, propose alternatives and test a specific change. Support sketches, low-fidelity flows and executable prototypes according to the uncertainty. Include designer review, user research, browser inspection, accessibility checks and performance measurements where relevant.

**Demonstration:** show a revision that improves a predeclared outcome and retains the intended character, alongside a plausible alternative that failed. Use failures and counterexamples as teaching material. Do not present AI consensus as user research or stylistic preference as an objective measurement.

### Capability 7: maintain a usable knowledge instrument

Address DES-010, DES-013, DES-015 and DES-016. Keep a small entrypoint organized by work: frame, explore, compose, specify, build, critique, validate, maintain. Route into focused guides and optional reference packs. Each substantial recipe carries prerequisites, decision questions, a worked example, counterexample, accessible adaptation, source support and a verification method.

**Demonstration:** another assistant finds the needed guidance from the packaged entrypoint, applies it with the user's profile, explains uncertainty and produces inspectable artifacts. Measure unnecessary reading burden as well as answer quality. Larger context consumption is not evidence of a better skill.

## Proposed evaluation contract

This is an evaluation design, not an experiment already run. The question is whether each release improves design usefulness and correctness **without losing contextual expression**. Before execution, pin the exact package, task inputs, model/harness, tool access, assets and output requirements; run each condition in a fresh context without the competing skill. Use repeated runs and blinded human review where feasible. Agree repetition count and scoring anchors before generating outputs.

| Task family | Why it belongs | Evidence |
| --- | --- | --- |
| Editorial long-form | Tests the existing strength | Reading hierarchy, measure, real content, footnotes/links, large text, font failure. |
| Dense operational interface | Challenges the publishing preset | Data hierarchy, meaningful density, task completion, state handling, numerical typography. |
| Public-service form | Challenges appearance-first workflow | Errors, recovery, clear content, keyboard/focus, disabled-user research where available. |
| Image-led collection | Tests expressive range | Art direction, image hierarchy, orientation, accessible exploration and reduced motion. |
| Multilingual experience | Challenges Latin and left-to-right assumptions | Script-aware typography, direction, text expansion, translated content, specialist review. |
| Existing non-C&B system | Tests adoption and scope | Preservation of supplied tokens/identity, minimal justified changes, no unsolicited rebranding. |

For 1.5, choose bounded specimens from these families appropriate to its narrower promise. For 2.0, test connected journeys. Keep all attempts—including failures, blocked checks and unrun cases—in the denominator.

Use separate gates: factual/numerical correctness; accessibility and functional behavior; task/content fit; visual craft; contextual expression; evidence quality; and maintenance/handoff quality. Suggested ordinal anchors are absent/contradicted, vague, actionable but incomplete, and complete with supporting evidence. Record criterion-specific observations, not one aggregate beauty score. Accessibility failures cannot be offset by an attractive screenshot; equally, conformance alone does not prove excellent design.

Compare unassisted baseline, current skill, 1.5, and eventually 2.0 when the comparison answers a useful decision. Include regression traps: familiar navigation that should stay familiar; a task needing a breakpoint; a legitimate non-geometric scale; disabled versus placeholder text; a supplied brand that must survive; and a design that benefits from optical correction. A system that simply bans every exceptional case has failed the intended task.

“Top-tier” remains an ambition until supported by these demonstrations, expert judgment and use over time. The evaluation cannot establish universal aesthetic superiority; it can establish better performance on named task families with explicit limits.

## Deferrals and decisions to settle before plans

- Do not select a replacement component framework or adopt a new corporate visual identity. None of the findings requires that.
- Do not mass-copy source books, ship all cards, rewrite concept-card schemas, or claim old extraction confidence as new semantic acceptance.
- Defer full native/print/spatial design coverage and automated design-tool synchronization until a concrete use case establishes their contracts.
- Decide whether C&B remains a clearly optional case study or only preserved historical provenance.
- Decide the exact 1.5 promise: fully reconciled live skill plus explicitly unverified historical corpus, or full semantic reconciliation of that corpus as well.
- Resolve the 1.5 compatibility/version interpretation before dependent implementation. Project identities and the shared audit home are now established in the project plans.

The important design decision is already clear enough to guide that discussion: preserve the skill's compositional ethos, restore room for skilled judgment, and connect its visual system to the people, content and interactions it is meant to serve.
