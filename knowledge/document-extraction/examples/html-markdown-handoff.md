# Representative HTML And Converted-Markdown Handoff

**Synthetic example.** These are invented case records, not captures,
conversions, tests or observations performed while authoring this skill. Paths
refer to an imagined workspace, with no attached files. Use the
[HTML guide](../guides/06-html-and-converted-markdown.md),
[manifest](../templates/manifest.md), [caveat](../templates/caveat-record.md)
and [readiness](../templates/validation-readiness.md) templates.

## Captured HTML Manifest

Manifest html-manifest-01, source html-pond-log, title Pond Log, edition/author
unknown. Run html-run-01, 2026-09-06 UTC, agent-direct scenario. Snapshots:
html-capture-a, html-conversion-a, html-prepared-a. All paths resolve from
`/case/html/`; evidence home `records/run-01/`.

Original requested and final URL: `https://example.org/pond/log`. Capture time:
2026-09-06 10:00 UTC. Supplied `raw/page.html` is a saved server response,
not a rendered DOM or screenshot. Tool/version unknown. It has a base URL
`https://example.org/pond/`; dynamic measurements panel content is absent.
Preserved conversion: `conversion/page.md`, 40 lines, converter and invocation
unknown. No digests measured or supplied, C-H3.

Request: index the complete article including measurements, and read/review
the complete article. Prepared inventory: `prepared/page.md`, 40 lines, single
monolith in original order; no generated headers, no manual repairs and no
media fetched. Transformation is a separate derived copy. Regeneration into
a fresh directory is proposed, not performed; a new retrieval would have a
new capture identity. Record register: [structure](#structure-and-locators),
[media](#media), [caveats](#caveats), [checks](#checks-and-readiness).
This combined illustrative record is not an actual saved handoff.

## Structure And Locators

Map html-structure-01: root sections h-title, h-observation, h-measurement,
h-notes in order. Original titles: Pond Log, Observations, Measurements, Notes;
labels unnumbered. Conversion spans 1–4, 5–28, 29–34, 35–40 map unchanged
to the same prepared spans, one-based inclusive. All wrapper/container edges
are intact because no split occurs. The Measurements span contains a loading
placeholder, not measured values; its missing dynamic content is C-H1.
There are no omitted conversion spans or unexplained repeats.

Map html-locators-01, source html-pond-log:

| ID | Snapshot / resource | Kind / value / basis | Status |
| --- | --- | --- | --- |
| H-L1 | html-capture-a / `raw/page.html`, original resource URL above | Anchor/ID `observations`, unique in saved response | Verified by scenario markup inspection |
| H-L2 | html-conversion-a / `conversion/page.md` | Source lines 5–28, one-based inclusive | Verified captured Observations block to conversion-text comparison |
| H-L3 | html-prepared-a / `prepared/page.md` | Output lines 5–28, one-based inclusive, all file lines counted | Verified copy comparison |

Relation H-M1 maps H-L1's complete Observations block through H-L2 to H-L3,
with inspected context at each boundary. Fragment `#observations` retains the
captured resource identity; it does not mean whatever the live URL shows later.
No fixed page numbers are assigned. Dynamic measurements have no verified
content mapping and no fabricated output span.

## Media

Report html-media-01: reference H-R1 at conversion/prepared line 18 has original
target `images/pond.png`, resolved under the captured base to
`https://example.org/pond/images/pond.png`. The converted Markdown already uses
that absolute URL, so preparation leaves it unchanged. Alt text “North pond”,
no title. Asset H-A1 is uncaptured; no preserved/derived asset path, format,
size or checksum known. Disposition remote; no local media exists in the
supplied inventory. Target spelling/context were inspected, but network
retrieval, identity and appearance were not checked, C-H2. Do not test it as a
missing local file or silently download it to conceal the capture gap.

## Caveats

All dated 2026-09-06 for html-run-01, unresolved, no resolution history; next
actor is the preparer. Scope/evidence are the scenario inspections below.

| ID / category | Affected input/output and observation | Handling, impact and re-entry |
| --- | --- | --- |
| C-H1 / capture | Measurements panel in `raw/page.html`; lines 29–34 in conversion/prepared file contain only loading text | Retain placeholder; complete indexing blocked and reading caveated. Obtain authorized rendered state with values and its capture evidence, then create a new snapshot and map it |
| C-H2 / media | H-A1/H-R1, line 18; relative web target resolves to uncaptured remote URL | Keep absolute reference, mark appearance unchecked; reading incomplete for image content. Capture asset if requested and verify identity and appearance |
| C-H3 / lineage and coverage | All files; capture/converter versions, invocations and digests absent; no live-state or regeneration comparison | Preserve supplied representations; do not claim whole-page fidelity or repeatability. Record available lineage, identify snapshots, and compare a separately scoped new capture if needed |

## Checks And Readiness

| Check | Scenario scope / method | Outcome |
| --- | --- | --- |
| H-C1 text and structure | All 40 converted/prepared lines compared; visible static response blocks matched | Pass within supplied static capture; structure map |
| H-C2 completeness | Inspect Measurements response markup against complete-article requirement | Fail; loading placeholder does not meet requested coverage, C-H1 |
| H-C3 locators / media | Inspect H-L1 uniqueness and mapped paragraph; resolve H-R1 against recorded base | Pass for that anchor/mapping and URL resolution only; remote availability/appearance not checked, C-H2 |
| H-C4 raw preservation / regeneration | Separate input and derived locations recorded; no hashes or repeat run | Not checked for byte identity/repeatability, C-H3 |

| Use / original scope | Status | Evidence and next action |
| --- | --- | --- |
| Complete-article indexing including measurements | Blocked | H-C2/C-H1; static-text subset does not satisfy request. Capture measurements and reassess |
| Complete-article reading/source review | Caveated | H-C1 permits reading available prose; C-H1/C-H2 disclose missing values/image; full original request remains incomplete |
| Analysis | Not assessed | Not requested |
| Concept-cards | Not assessed | Not requested; no preparation-to-card approval implied |

Handoff location: `prepared/page.md`, with this manifest, mappings and caveats.
No readiness claim about the live site follows from the static snapshot.

## Converted Markdown With No Original

This separate synthetic case must not inherit the HTML capture's identity or
checks. Manifest md-manifest-01, source md-supplied-note, title Supplied Pond
Note (from heading), author/edition/URL unknown. Run md-run-01 dated 2026-09-06
UTC, human-assisted: operator supplies `incoming/note.md` but cannot provide
the original. Path root `/case/markdown/`; evidence home `records/run-01/`.
Snapshots md-input-a and md-prepared-a; converter/version/command unknown,
checksum unavailable. Output `prepared/note.md` is a separate 12-line copy,
no corrections, splits or added headers; regeneration not run.

The combined records are: md-structure-01, a single root section m-note titled
Pond Note with input/output lines 1–12, one-based inclusive; md-media-01,
no media found by inspecting all 12 supplied lines (not a claim about the
missing original); md-locators-01, M-L1 source lines 1–12 of md-input-a
`incoming/note.md` to M-L2 output lines 1–12 of md-prepared-a
`prepared/note.md`. Relation M-M1 is operator-reported unchanged copy;
assistant-side target/file comparison and durable storage are unverified.

C-M1 (lineage/coverage, unresolved, md-run-01, no resolution history) affects
the whole note: original and conversion lineage unavailable, so original
fidelity and original-source locators are unchecked. Handling: preserve
supplied text and use only snapshot-bound locations. Re-entry: operator
provides original plus lineage and a source/output comparison. C-M2 (storage
and check coverage, unresolved) records that only pasted contents and an
operator copy report are available; next step is to save/reopen records and
verify the named files before asserting durable handoff.

Check M-C1: assistant reads all 12 supplied text lines for readability, pass
for that sample-as-entire-supplied-note. M-C2: original fidelity, not checked
because original is absent. M-C3: copy identity/storage, operator-reported,
not directly checked. Requested reading of the supplied note is Caveated
(M-C1, C-M1/C-M2); requested concept-card preparation requiring original-source
traceability is Blocked (M-C2, C-M1). Indexing and analysis are Not assessed.
Return these records for saving; do not call the draft a durable delivered
bundle or invent a source URL to make the handoff look complete.
