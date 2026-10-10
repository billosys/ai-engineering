# Five-dimension semantic review procedure — proposed method

**Purpose and boundary.** This procedure defines later source-grounded review of the Project10 baseline. It does not perform semantic acceptance, create a Project08 schema, alter cards, or grant mutation authority. The accepted contract requires all 233 card identities, five distinct semantic dimensions, eight live design files, and allocated Design Evidence Set (DES) findings. Slice02 maps readiness and method; the final Arc02 execution-group allocation remains Slice03 work.

## Ordered review

1. **Pin and read.** Record card paths/hashes and revisions; source originals/captures and prepared snapshot hashes; source/claim guide revisions; active method and prompt revisions; actor, role and date. Read each complete card body, examples, implementation mappings, typed relationships, prerequisites and question coverage. Read relevant sources in full cited context and any qualifying or contradictory spans. Preserve unavailable inputs rather than substituting card metadata.
2. **Inventory assertions.** Assign a stable local claim ID to every substantive assertion with exact card line span and text. Separate (a) source-attribution/history claims, (b) mathematical/technical truth, (c) scope, attribution and conditions, (d) advice/heuristics and analogies, and (e) relationships/CQ coverage. A card-level summary does not replace the assertion list.
3. **Inspect evidence.** For each assertion, resolve the source locator against a pinned snapshot, inspect sufficient surrounding context, and record literal evidence spans. Search relevant contradictions and qualifications in the declared scope. Treat bibliographic identity, extraction confidence, structural validity and source readability as distinct from warrant.
4. **Record five results separately.** Apply the five dimensions below, each with its own result, reason, evidence and coverage: source faithfulness; factual/mathematical/technical correctness; scope and attribution; internal, cross-card and live-guide consistency; relationship and competency-question coverage. Name blocked inputs and their owners. A statement may be faithful to its source and false or outdated as a present-day claim; record both results.
5. **Revise only under authority.** Correct, qualify or remove only under an explicit assigned mutation scope. Preserve prior text/hash, reason, source comparison and affected dependencies. Recheck revised assertions and implicated relationship/CQ/guide mappings at the new revision. Reconcile disagreements rather than silently choosing the newest/longest statement. CC self-check remains same-context; independent CDC review is a separate result and gate.
6. **Reconcile population and handoff.** Reconcile all original 233 card identities to additions, splits, merges, removals or unchanged identities. Account for assertion-level coverage, every repeated live-guide claim and all unresolved dimensions. Do not let a whole-card summary conceal a missing claim/dimension. Report failures, blocked/not-assessed work, owner and falsifiable re-entry condition; preserve counterevidence and acceptance gates.

## Five dimensions

| Dimension | Question | Minimum evidence boundary |
|---|---|---|
| Source faithfulness | Does the assertion accurately represent what its identified source says? | Exact source snapshot span plus qualifying context; source identity and locator basis. |
| Correctness | Is the proposition true/technically valid within its declared present-day domain? | Appropriate primary/technical evidence and domain method, separate from a faithful quotation/paraphrase. |
| Scope and attribution | Are conditions, population, date, edition, author, uncertainty, inference and normative status represented accurately? | Exact source context and explicit boundary/attribution; do not generalize a bounded observation. |
| Internal/cross-card/guide consistency | Does it conflict with other assertions, implementation examples, live guides or accepted contracts? | Named revisions and exact paired spans; consistency is not proof that either assertion is true. |
| Relationship/CQ coverage | Is the relation itself warranted, and does mapped evidence answer each required CQ component for its intended use? | Edge meaning/direction/support and CQ component-to-claim/source spans; endpoint existence or populated lists alone do not count. |

## Local claim-result record shape

Use a compact record in the owning evidence home; this is a procedural shape, not a new schema or runtime:

```yaml
claim_id: local stable ID
card: {path: exact path, sha256: pinned card hash, span: one-based inclusive lines, assertion: exact text}
evidence: [{type: source-span | technical-source | counterevidence, snapshot_sha256: exact hash, locator: typed value, span: one-based inclusive lines/pages, observation: what it says}]
dimensions:
  source_faithfulness: {outcome: ..., reason: ..., evidence_refs: [...]}
  correctness: {outcome: ..., reason: ..., evidence_refs: [...]}
  scope_attribution: {outcome: ..., reason: ..., evidence_refs: [...]}
  consistency: {outcome: ..., reason: ..., evidence_refs: [...]}
  relationship_cq_coverage: {outcome: ..., reason: ..., evidence_refs: [...]}
actor: {name: ..., role: CC | CDC | Operator, date: ..., method_revision: ...}
subject_history: {prior_revision: ..., revised_revision: ..., dependencies: [...]}
blocked: {input: ..., owner: ..., reentry_check: ...}
disposition: {proposed: retain | qualify | correct | remove | unresolved, rationale: ...}
independent_review: {state: pending | completed, reviewer: ..., result_ref: ...}
```

Use explicit `not assessed`, `blocked`, `partial`, or a contract-defined result as appropriate, with a reason. Do not manufacture a standard enum or make absence equal pass. A verification state requires a recoverable result tied to the exact subject revision.

## Population and finding allocation

- Retain the accepted baseline denominator of 233 cards; group by literal primary-source pair only for accounting, never as semantic verdict.
- The accepted portability contract's eight live files are `knowledge/design/SKILL.md`, `knowledge/design/version-history.md`, and six guides: `design.md`, `colour.md`, `layout.md`, `type.md`, `foundations-of-design.md`, and `breaking-the-layout-monoculture.md`. Repeated factual/technical claims are individually mapped and reviewed wherever they recur; one card result does not close its guide occurrence.
The accepted contract §5 assigns the following 16 findings. This table preserves primary owners, cross-references, outcomes, checks and outstanding inputs; allocation is not acceptance. Final Arc02 execution-group allocation and sequence remains Slice03 work.

| Finding | Primary owner; cross-reference | Required downstream outcome | Verification and outstanding input |
|---|---|---|---|
| DES-001 | Arc01 contract; Arc04/05 | Remove the C&B default and preserve existing supplied identity. | Generic and existing-brand fresh-context tasks; inspect entire live payload/package. C&B scope is settled by Operator; wording/profile remains proposed. |
| DES-002 | Arc02 theory; Arc03 accessibility/layout; Arc04/05 | Scope scientific/perceptual claims; allow contextual judgment. | Claim-level source review and counterexamples across the 233-card population and guides. Source availability and claim register required. |
| DES-003 | Arc02 theory | Correct the claim that interpolating two geometric endpoint scales remains geometric. | Reproduce declared intermediate values/ratios for each retained example. Exact example/configuration is pending CDC/Operator choice. |
| DES-004 | Arc02 theory; Arc04 examples | Use one declared configuration and consistent generated values. | Recompute endpoints, negative steps, interior widths, rounding and root-size changes. Example parameters remain proposal. |
| DES-005 | Arc03 accessibility/typesetting; Arc02/05 | Remove `vi`-as-accessibility guarantee; preserve user preferences and test text enlargement separately from reflow. | Actual text-size and reflow specimens at named environments. No browser/AT test was run in this slice. |
| DES-006 | Arc03 accessibility; Arc04/05 | Establish keyboard, focus, semantics, reading-order, motion and complete color-pair floor. | Inspect retained interactive examples against the floor and maintained patterns. Specify runtime/environment and actual token pairs. |
| DES-007 | Arc02 theory/evidence | Correct full sRGB-to-Oklab nonlinear pipeline and scope OKLCH claims. | Check linearization, cube-root and matrices against identified technical source; verify card claims. Original Oklab source is cited in audit; card source claims still need full review. |
| DES-008 | Arc02 theory; Arc04 package | Treat token layers as contextual architecture rather than a universal DTCG rule. | Compare exact source-system generations and validate any actual exported format. Pin current source docs before release. |
| DES-009 | Arc02 layout; Arc03/05 | Use intrinsic layout first while allowing content/behavior/user-preference breakpoints and scoped measure. | Dense-interface case needs and justifies a breakpoint; check content change and target contexts. |
| DES-010 | Arc04 guides/package | Repair package routes, converted markup, examples and declared dependencies. | Build and inspect isolated package; resolve every shipped link/snippet. `make design` and package gates belong to later authorized source work. |
| DES-011 | Arc03 typography; Arc04/05 | Provide transferable type selection/typesetting, axis verification, fallback/loading, script coverage and readable functional examples. | Named fonts/axes and fallback specimen plus large text/missing font checks; broader multilingual scope remains Project11 unless Project10's accepted floor requires it. |
| DES-012 | Arc02 evidence; Arc04/05 | Scope CHI observation and remove unsupported broad causal interpretation. | Obtain/inspect full paper before claims stronger than abstract; compare repeated-layout use by task. Audit records failed PDF retrieval; resolve later. |
| DES-013 | Arc02 evidence; Arc04 package | Add source/claim traceability, accurate source/readiness states and limited installed promise. | Reconcile each source/claim/CQ and population; identify missing Arnheim/Cleland/Tschichold originals and other source snapshots. Slice02 owns acquisition/readiness planning. |
| DES-014 | Arc04 workflow; Project11 capability extension | Add a bounded brief/context route before visual styling and state the 1.5 promise. | Follow fresh brief through question/assumption, relevant guidance, choice and review. Connected research/prototype practice remains Project11. |
| DES-015 | Arc02 full corpus; coordinate Project08 | Review all cards and correct cross-domain errors only with claim-level evidence; keep unavailable originals unresolved. | Complete five-dimension review for every card, track revisions/claims/source spans, preserve Project08 boundaries. Current targeted audit is not a verdict. |
| DES-016 | Arc02 full corpus | Repair literal escapes where normal prose is damaged without blindly decoding legitimate code examples. | Compare before/after text for all affected posts, preserving meaning/provenance; manifest baseline remains denominator. |
- Count relationship edges, endpoint revisions and CQ answer components separately. Check source warrant on the relation/coverage assertion itself. A resolved endpoint, reciprocal navigation or filled `answers_questions` field is not answerability.

## Analytical cases and false-upgrade controls

| Case input | Expected handling | False upgrade caught / actual limit |
|---|---|---|
| Munsell Hue Circle asserts Cleland “Chapter 4: I. Hue, pp. 4-6”; frontmatter gives `chapter: "I. Hue"`, `chapter_number: 4`, `pdf_page: 4`; no original was supplied. | Preserve every raw value; identify physical/printed page basis as unknown; block source-faithfulness and any page-based claim until exact Cleland edition and scan are pinned. The public 1937 listing is only an acquisition candidate. | Prevents `pdf_page: 4` or high extraction confidence from being presented as a checked PDF page or proof the passage supports the whole card. This case was inspected at card-body level only; no original comparison occurred. |
| Golden Ratio card has `section: null` but raw reference names Brown's opening, two article sections, and Bringhurst “Shaping the Page” in Further Reading. | Map Brown's actual local heading anchors; record Bringhurst separately as further reading/secondary citation. Keep Brown's quoted/hedged statements distinct from mathematical claims and the card's added historical/music/CSS propositions. | Prevents null section from erasing usable locator evidence and prevents a further-reading title or source fidelity from proving every card assertion. No full semantic review was performed. |
| Butterick card names “Headings”; substring scan finds references to headings in other pages, including a cross-link in `text-formatting.md`; prepared `headings.md` has title/URL and HTML body boundary but no Markdown heading. | Resolve the unique page by exact page title plus URL, inspect the complete prepared page boundary/context, use line spans without inventing an anchor, and separately record unknown original capture fidelity. | Prevents substring candidate count or fabricated heading from proving identity. The locator is prepared navigation only, not source fidelity. |
| Card faithfully attributes a mathematical/CSS statement to an article, but adds a present-day claim about mathematical validity or CSS behavior. | Score source faithfulness and correctness separately; establish the latter from appropriate current technical evidence, scoped to the relevant version/environment. Keep the article's limits and the card's added inference visible. | Prevents “the source says this” from being upgraded to “this is true now.” No such broad correctness audit was attempted here. |
| Existing relationship endpoints resolve and card has a question populated, but CQ answerability is asserted. | Break the CQ into required components; map each to exact claim/source/edge revisions; test whether an actual bounded answer follows with stated assumptions. Review edge meaning/direction/support separately. | Prevents endpoint existence, reciprocal navigation, or a filled question field from being upgraded to supported relation, adequate coverage, or answerability. No graph/CQ corpus review was performed here. |

This method contains analytical examples only. It does not establish that any other claim was read, supported, verified, reconciled, or accepted.
