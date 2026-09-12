# CC Iteration 03: Finish The Inventory Contract

Read the Project08 instructions, active plans/ledger and the latest appended
review in `../cdc-verification.md`. Starting packet: `e554d74c`. The source
skills and all captured corpora remain read-only. Preserve prior CDC edits.

CDC independently reproduced the main census, typed values/shapes, and exact
308 normalized path coverage. Preserve those fixes. Remaining acceptance work:

## R8/R9: Fix Concrete Representation Failures

- `artifacts/cdc-edge-probes/json-controls.md` contains the valid YAML string
  `"page\fbreak"`. The custom JSON encoder writes the decoded form-feed byte
  literally and `jq` rejects the output with exit 4. Use a proven JSON
  implementation through Fennel, with documented local dependency setup and
  explicit null/container/boolean behavior. Do not grow the hand-written JSON
  parser/encoder into a second parser-maintenance project. Keep inventory logic
  in Fennel; established parser libraries and a narrow bridge are permitted.
- `null-root.md` is currently marked `frontmatter: true`, `keys: []`,
  `values: null` because the internal null marker is a table. A null YAML
  document is not a mapping. Check document kind explicitly.
- The existing empty fixture has both delimiters but is reported as
  `unterminated-frontmatter`. Frame frontmatter by delimiter lines, including
  empty documents and a closing delimiter at EOF; preserve the distinction
  among absent, empty, null, nonmapping, malformed and genuinely unterminated
  content. Choose and document consistent result labels.
- Add executable assertions for the preserved reviewer probes and existing
  fixtures, including output parseability, correct classifications, original
  type distinctions and nested shapes. A command exiting 0 is not sufficient
  if it reports the wrong record kind. Test valid empty mapping separately.

## R2: Complete Actual Semantic Analysis

The index now has better coverage, but 109 observed meanings still say only
"records the observed metadata component named by this exact path and context";
100 dispositions still hand the decision to Arc02. All migration sentences
have the same generic template with the path substituted.

Inspect definitions and actual records. `actor.id` identifies the performer,
not a local card or assertion. `source_refs[].id` identifies a referenced
source, not the card. `aliases` is present in both legacy and current profiles;
an assertion that it is weakened needs an actual demonstrated gap.

Use a readable, authored semantic-family analysis with an explicit membership
map to field/context paths. Sharing one analysis is good when meaning really
is shared; grouping by suffix alone is not semantic evidence. For each family
provide meaning, actual defining path/section, legacy/current representation,
observed preserved/renamed/relocated/weakened/absent/ambiguous behavior, and a
concrete query or migration implication. Separate future schema recommendations.
Some fields can correctly be current-only; do not invent a legacy counterpart.

Keep mechanical index generation separate from human/LLM-authored semantic
annotations. Provide the reproducible join and uncovered-context check; the
current helper generates the mechanical index but not the claimed semantic
artifact. Do not treat non-empty annotation strings as proof of analysis.
Disclose any remaining unreviewed families instead of labeling them done.

## R4: Deliver Working Reproduction Instructions

The documented coverage command reads `.records[]` from the field index, which
has no records, and exits 5. It also uses `items.[].id` notation while the
index uses `items[].id`. Read the inventory and index as separate inputs and
normalize both identically. Use the independently reproduced command in the
CDC review as an evidence-backed starting point.

Run the literal documented command sequence in its named shell/environment,
checking exit statuses and output. macOS `/bin/bash` is 3.2 and lacks
`mapfile`; either name a verified compatible shell or use portable argument
collection. The existing input register still abbreviates predecessor and
guide names: give exact inspected paths plus revision/hash identities and
semantic evidence anchors. Update its obsolete parser description.

## Delivery

Change only this slice's implementation helpers, fixtures, semantic analysis,
index/reports, ledger and CC closing report. Reviewer artifacts and plans are
inputs. Preserve all 27 baseline copies byte-for-byte, including malformed cards.
Use Fennel and proven dependencies; no Ruby/Python implementation or wrapper.

Run focused assertions, then the census and independent coverage check; prove
determinism on unchanged inputs and compare retained mechanical results. Review
semantic families against primary local definitions. Record raw outputs and
all required commands. Keep package/source gates scoped to actual changes.

Address R2, R4, R8 and R9 explicitly in the revised proposed-done closing report
and walk all eight ledger rows. R5/R6/R7's reproduced corrections must remain
intact. If the remaining semantic work cannot fit this execution unit with
review headroom, report the actual remainder and propose a bounded split
instead of substituting more generic annotations.

Commit only explicitly enumerated corrected slice files with both repository
co-author trailers. Preserve unrelated staged/planning changes and prior
commits; do not amend `e554d74c`. Return the corrective commit, test outcomes
and outstanding findings. Independent CDC closure remains required.
