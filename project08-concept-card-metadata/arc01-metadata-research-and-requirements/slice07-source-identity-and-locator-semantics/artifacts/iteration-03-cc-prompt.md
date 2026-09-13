# CC Iteration 03: Preserve Historical Source Conventions

Read the latest CDC review of e99fddbb, current plans/ledger, the original
assignment and its required load set. This is a narrow continuation of
S7-R1/S7-R2 in the same twenty-pair slice. S7-R3 is resolved; five criteria
are now CDC-reproduced. Preserve the successful registry/current-locator and
executable-replay repairs.

## Remaining Work

1. Complete the historical meanings/dispositions for source_slug, pdf_page
   and chapter_number, plus section where its fallback role is relevant.
   Both registered guides define source_slug as a directory name; v3.2 adds
   the shared leaf convention under sources/md/ and concept-cards/. Distinguish
   this intended local path relation from sampled actual layout and from global
   identity. Do not describe the directory interpretation as newly introduced.
2. Preserve the guides' rule that pdf_page comes from chapter metadata.
   Separate that intended input relationship from observed card values, body
   citations, coordinate basis and unverified extraction lineage. Do not infer
   which original header produced a sampled card or invent a page offset.
3. Inspect/register v3.2's Non-Integer Chapter Numbers and Sources with No PDF
   (Pure Markdown or HTML-Origin) sections. Retain documented null cases and
   section/fragment fallback in affected meanings and evidence. Observed null
   alone does not prove its reason; normative guidance is not proof that every
   historical card followed it.
4. Add a literal source-family census using the frozen data, not only pooled
   music/Erlang totals. Group by observed source_slug, retain all seven fields'
   shapes/missingness and relevant value distinctions, and explain the patterns
   relevant to the historical source/locator comparison. CDC supplies example
   page/chapter counts as a diagnostic, not your complete execution record.
   Keep the existing broad totals as a cross-check. Inspect additional named
   records only where needed for a supported comparison, registering them.
5. Update registry and prose together so these distinctions remain discoverable
   through each affected meaning and membership. Extend and execute the existing
   replay with the actual new queries/inspection route; retain both evidence
   layers, all hashes, exact-set, preservation and whitespace checks.
   Reconcile handoff and closing report with the narrow corrections.

Do not restart current locator research or change accepted meanings without
a concrete new contradiction. No new schema, extraction, helper, source edit,
package/install, runtime, actual mapping or source-support verification.
No new memberships, source-family normalization, or unsupported migration.
If any criterion remains unmet, leave it open explicitly.

## Scope And Commit

Only these six existing files under
project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice07-source-identity-and-locator-semantics/
may be edited and committed:

- artifacts/semantic-membership.json
- artifacts/semantic-evidence.md
- artifacts/validation-evidence.md
- artifacts/handoff.md
- ledger.md
- closing-report.md

Keep every criterion unchanged and preserve CDC authorship on reproduced rows.
Give every row its disposition/evidence in the report, retain the artifact
inventory and scope-as-specified/delivered bubble-up, and disposition the
remaining parts of S7-R1/S7-R2. The 47 accepted / 20 assigned / 488 other pairs,
parent gates and later P-14 trial remain unchanged.

Enumerate actual full planning-relative filenames in both staging and
git commit --only -- <filenames>; no directories, globs or commit -a. Inspect
the staged diff, preserve unrelated work and include both trailers:

~~~text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
~~~

Return the scoped commit, concrete historical distinctions preserved, executed
checks and any residual limits. Do not edit plans, prompts or CDC verification.
CDC independently reviews the completed comparison before slice closure.
