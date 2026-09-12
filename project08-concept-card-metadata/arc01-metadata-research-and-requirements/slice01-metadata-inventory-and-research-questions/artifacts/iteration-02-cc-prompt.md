# CC Iteration 02: Preserve Types And Complete Semantic Inventory

Read the Project08 instructions, project/arc/slice plans, ledger and the appended
Iteration 01 CDC review in `../cdc-verification.md`. This is still Arc01
Slice01. The operator approved the prior commit `e2ea1e68`; no Ruby code entered
that commit. Preserve that improvement and the existing baseline bytes.

The remaining failures affect the original no-loss inventory requirement.
Do not treat this as another schema-design assignment. Arc02 chooses the future
schema; Slice01 must describe observed meaning and whether the existing
representations preserve, weaken, relocate or omit it.

## Work

1. **R6: preserve values and types.** The current parser emits YAML `true` as
   JSON `1` and `false` as `""`. These collide with an integer and an empty
   string. Use the proven YAML parser with an explicit supported boolean/type
   policy and preserve those values through JSON serialization. Numeric values,
   quoted numeric strings, booleans, null, empty strings/maps/lists must remain
   distinguishable. Report the YAML dialect and date/tag behavior honestly.
   Do not recover types by heuristically guessing from already-coerced values.
2. Define stable typed shapes rather than reducing every non-null scalar to
   `scalar`. Sequence shape members must be structured data, not JSON documents
   embedded as strings. Keep parser interoperability narrow and reporting/shape
   traversal in Fennel as required by the language decision. The current
   `parser-records` embeds hashing, frontmatter framing and all shape/report
   construction in Perl despite comments claiming otherwise. A minimal,
   documented parser bridge is permitted; correct the implementation/comments
   without replacing one full foreign-language helper with another.
3. Add assertions with independently specified expected outcomes. Use the
   reviewer fixture `artifacts/cdc-type-probes/types.md` as a regression input.
   Test true/false versus 1/0 versus quoted strings, empty/null/missing values
   and nested sequence-of-mapping fields. Existing malformed/nonmapping/empty/
   unterminated/missing-root fixtures must still pass. Demonstrating that two
   runs repeat the same bug is not a correctness test.
4. **R7: enumerate complete paths and contexts.** The 307-entry index omits
   30 object-key paths that exist in the parsed data, mostly null or empty.
   Examples: `coverage_assertions.0.id`, `coverage_assertions.0.covered_refs`,
   `operator_acceptance.required`, `endpoint_roles.from_role`, and
   `source_spans.0.source_ref`. Walk objects and arrays without truthiness
   filtering, including null/false/empty leaves and containers. Define whether
   sequence paths use concrete indices or a normalized wildcard. Recompute
   occurrence counts, record kinds, shapes and evidence for every context,
   including template nulls. Store a reproducible Fennel index-generation and
   coverage-check route; no hidden ad hoc generation step. Report missing and
   extraneous paths against an independently derived expected set.
5. **R2, continued: do the semantic crosswalk.** All 307 entries currently use
   the identical `inventory-observed; Arc02 must...` disposition and the
   identical generic migration sentence. Replace these with actual observed
   meanings and field-specific loss/query implications. Explicitly map fields
   to shared semantic analyses only where their meaning is demonstrably the
   same; do not inflate the artifact with repeated boilerplate.

   Examples of the required level of analysis: `coverage_assertions[].id`
   identifies a coverage assertion, not a card; losing it prevents results from
   targeting that assertion. `operator_acceptance.required` is a requirement
   flag, not an acceptance outcome; false must not become empty text.
   `endpoint_roles.from_role` labels a directional endpoint role and remains
   an observed field when null. Trace these claims to real guide/template
   definitions and compare their observed behavior across relevant record sets.
   Keep recommended future changes visibly separate from observed dispositions.
6. **R4/R5, continued: finish evidence and close-packet reconciliation.**
   Replace `<the nine roots ...>` placeholders with executable invocations.
   Register exact prose-input paths and identities, not abbreviated guide names
   or predecessor numbers. Provide exact index-generation/coverage commands,
   setup/version probes and observed results. Remove current assertions that the
   CompCogNeuro checkout is absent; a clearly dated historical statement may be
   retained. Correct the artifact inventory (Fennel, no active Ruby helper;
   14+13 baseline files), walk all eight ledger rows, and distinguish commit-time
   state from the earlier uncommitted observations. Reconcile the research
   agenda to the completed crosswalk without selecting a future schema.

## Scope, Verification And Commit

Write only this slice's helper, fixtures, index, evidence reports, ledger and
CC closing report. Reviewer artifacts are inputs; preserve CDC's findings and
fixture. Add narrowly necessary test/generation helpers under this slice's
`artifacts/` and list them explicitly. Source skills, historical prompts and
corpora, Project06 and other projects remain outside this correction.

Run semantic/type assertions and path-coverage checks before the whole census.
Then rerun all nine roots twice, compare outputs, derive counts, regenerate the
index and inspect semantic coverage. Explain count changes instead of targeting
307. Verify all preserved baseline checksums, source status and whitespace.
Do not repair the three historical malformed baseline cards.

Update all eight ledger rows and write a revised proposed-done report with R2,
R4, R5, R6 and R7 dispositions, exact evidence, and any remaining limits.
Do not mark a row done because a field name is merely present in an index.
If the semantic analysis needs another bounded unit, expose the actual remainder
and a proposed split; do not declare that unfinished analysis delivered.

The earlier hold was released by the operator. Commit only the corrected
slice files using an explicitly enumerated filename list in both staging and
`git commit --only --`; preserve unrelated staged changes. Include both
required co-author trailers. Do not amend or rewrite the operator-approved
`e2ea1e68` commit. No Ruby/Python source or disguised wrapper is permitted.
Return the corrective commit, actual validation outcomes, unresolved findings
and revised CC proposed-done status. CDC closure remains a separate step.
