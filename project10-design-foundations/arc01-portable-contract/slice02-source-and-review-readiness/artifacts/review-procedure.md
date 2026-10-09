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
- Preserve the accepted finding ownership: DES-001 Arc01; DES-002/003/004/007/008/012/013 Arc02; DES-005/006/009/011 Arc03; DES-010/011/013 Arc04/05 as cross-referenced in the contract. Follow each finding's specified downstream outcome and check; allocation is not acceptance. The final Arc02 execution-group allocation and sequence remains Slice03 work.
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
