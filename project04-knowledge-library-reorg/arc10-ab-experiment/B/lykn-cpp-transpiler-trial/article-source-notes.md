# Article Sources and Editorial Handoff

Date: 2026-09-05
Draft: `posts/2026/ai-engineering-knowledge-library.md`
Working title: AI Engineering 0.5.0: A Knowledge Library Built for Reuse
Status: author-revised draft for Duncan; not independently reviewed or published.

## Working Brief

Write a contemporary account for engineering peers interested in reusable LLM
knowledge and working practices. The primary subject is Project04's
reorganisation for consistency, composability, selective loading and external
adoption. The Rust transpiler comparison supplies evidence about continued
usefulness and possible improvements. Use en-GB spelling and first-person
narration grounded in Duncan's supplied account. Length is intentionally
substantial, approximately 3,200 words.

## Editorial Choices

- Lead with the original docs/knowledge ambiguity, then component ownership,
  composition, semantic decomposition and package portability before the trial.
- Include the two follow-up requests for splits from the supplied conversation.
  They explain why file-level acceptance was needed. Do not infer a model's
  hidden motives or invent a personal recollection.
- Explain CDC and CC by their work responsibilities without historical
  backronyms. Use project/arc/slice only after explaining the hierarchy.
- Report no material overall regression demonstrated in this trial; preserve
  the newer audit's specific broken-pipe miss and the source-isolation issues.
- Treat run-to-run variation as a plausible explanation, not a demonstrated
  cause. The article does not attribute improvements specifically to splitting
  files, since content and organisation changed together.
- Omit numerical rubric totals: the local assessment has indicative ordinal
  scores, not a calibrated performance benchmark or statistical effect size.
  Retain the concrete comparisons and the assessor's verdict label.
- Distinguish independently loadable component routes from separately shipped
  packages. Do not imply every component has its own released zip.
- Do not claim 0.5.0 has been published or Project04 formally accepted. Write
  about preparation and the release cycle. The two experimental projects are
  closed; their unrepaired findings are intentional trial outputs.
- Mention scientific-methods as a subsequent reusable result. Do not attribute
  the trial's earlier outcomes to this newly added skill.
- Use today's date with the site's fixed -0600 offset convention. Noon is
  draft metadata, not a claim about a release or deployment time.
- Omit data.minutes to allow automatic reading time. Proposed tags:
  ai, rust, software-engineering.

## Evidence Map

All local paths below were read on 2026-09-05. R sources are assessment reports;
G sources are repository artifacts; O is the operator's supplied conversation.
The article uses report-derived experimental results and does not imply that
the drafting pass reran the transpilers, their audits or framework packages.

| ID | Locator | Supports |
| --- | --- | --- |
| O1 | Current conversation, Project04 brief and follow-up split approvals | Original docs/knowledge goal, selective-loading motivation, two missed split follow-ups, explicit acceptance, trial scope and no-repair decision, Duncan's stated relief. |
| G1 | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/release-notes/RELEASE-0.5.0.md` | Directory contract; component guide splits; sibling histories; package-context validation; CCDP separation; current scientific-methods addition. |
| G2 | `/Users/oubiwann/lab/billosys/ai-engineering/docs/skill-library.md` | Kind/topology distinction, atomic Rust example, package availability, separate domain loading, live scientific-methods and planned concept-card method. |
| G3 | `/Users/oubiwann/lab/billosys/ai-engineering/docs/collaboration-framework.md` | Composer/component routes, standalone versus composed use, exact code-auditing guide names. |
| G4 | `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/collaboration-framework/SKILL.md` | Component routing, separate domain guidance, current Expedited Mode constraints and version-history convention. |
| G5 | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/cdc-project-prompt.md` | Matched prompt family, framework isolation intent, shared domain references, tiny Rust/Lykn-inspired/C++17 scope and CDC/CC process. |
| G6 | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/read-only-self-audit-prompt.md` | Diagnosis-only audit phase, source restrictions and required report structure. |
| R1 | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/arc01-framework-comparison.md` | Early planning and evidence differences, older test-isolation recovery, newer scope front-loading caution. |
| R2 | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/phase2a-post-arc02-framework-comparison.md` | Different slice allocation, adaptation after early implementation, comparing capability rather than arc labels. |
| R3 | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/final-framework-regression-assessment.md` | Final verdict, concrete implementation differences, missed broken-pipe finding, clean-check report quality, contamination, experimental limitations. |
| G7 | `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/closing-report.md` | Older experimental project closure, all three arcs, preserved audit evidence, reported Rust and generated-C++ validation. |
| G8 | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/closing-report.md` | Newer experimental project closure, scope, validation, audit-complete-with-limitations and deliberate no-repair disposition. |
| W1 | https://doc.rust-lang.org/std/macro.print.html#panics | Primary documentation confirming print! can panic on a failed stdout write; checked online during drafting. |
| W2 | https://github.com/billosys/ai-engineering | Verified public repository link. The fetched page appears older than local source; it does not establish availability of every new route. |

R3 also locates both self-audit reports and the implementations. Its scores are
29/36 for the older condition and 32/36 for the newer condition. These are
retained here for traceability, not converted into a percentage improvement.

Current release notes include later work than Arc08's final validation:
13 skill packages / 222 Markdown files versus Arc08's 12 / 208. The post
avoids merging these snapshots and names only the recorded Arc08 hard-failure
and exception outcome. It makes no claim that skipped external URLs were
validated or that all warnings were resolved.

G7 contains awkward retained wording about audit readiness while separately
acknowledging the completed self-audit. The post follows the explicit closed
status, the named completed artifact and R3, without quoting that contradictory
sentence as a current audit status.

## Writing and Site References

Applied `/Users/oubiwann/lab/billosys/technical-writing/knowledge/blog-drafting/SKILL.md`
and its brief, voice, structure, evidence, drafting/handoff, narrative revision,
calibration example and Billo publication guides. Read the site's
`docs/templates.md`, `_layouts/blog-post.liquid`, `_data/authors.yml`,
`_cobalt.yml`, nearby posts and preview/deploy scripts. Cobalt guidance and
installed CLI help inform a temporary-output build; deployment is separate.

## Checks and Remaining Publication Work

- Author passes cover argument, subtraction, section boundaries, claim scope,
  en-GB spelling and separation of measured outcomes from inference.
- Reader-facing links point to the public repository and official Rust docs.
  Private workbench paths and source IDs stay in this note.
- Initial drafting did not rerun trial code or package validation. The later
  syntax-example addition compiled and ran the two quoted generated C++
  examples, as recorded below.
- `cobalt build --drafts --destination
  /private/tmp/billo-ai-engineering-article-draft-preview`: passed. Generated
  `articles/2026/09/ai-engineering-knowledge-library/index.html` contains the
  title, intermediate sections and final paragraph.
- `cobalt build --no-drafts --destination
  /private/tmp/billo-ai-engineering-article-public-check`: passed. A search of
  the complete output found no article slug or title. The September article
  directory is absent from this non-draft build.
- Whitespace check of the new untracked post against `/dev/null`: no errors.
  The diff command's exit 1 indicates a new file, not a whitespace failure.
- Targeted spelling, private-path, TODO/TBD and em-dash scan: no matches.
- Builds used temporary output directories. No deploy, commit, server or
  browser visual review was performed. Existing site changes were preserved.
- Duncan's final voice edit and publication decision remain outstanding.
  Public trial evidence is not assumed available: publishing a reproducibility
  packet could support a later revision, but is outside this draft request.

## Supporting-Note Placement

Automatic approval review allowed the article to be written to the requested
site post, but rejected copying this internal note into the site's workbench
because it contains private filesystem paths and project evidence references.
The note was retained here in the originating ai-engineering workbench instead.
An empty `workbench/article-drafts/20260905-ai-engineering-knowledge-library/`
directory was created in the site before that rejection; no note was copied
there. No additional approval is needed for the completed article draft.

## Syntax Examples Added at Duncan's Request

Added "A Glimpse of the Tiny Language" at the end of "What the Comparison
Showed", using verbatim fixtures and generated C++ from the completed trials:

- Newer trial: `implementation/lykn-cpp-transpiler/fixtures/valid/happy_path.lykn`
  and `implementation/lykn-cpp-transpiler/examples/generated/happy_path.cpp`,
  relative to the main trial workspace named in G8.
- Older trial: `tests/fixtures/valid/full_tiny_subset.lyk` and
  `tests/fixtures/expected/full_tiny_subset.cpp`, relative to the older trial
  workspace named in G7.

Both existing C++ files compiled with `c++ -std=c++17 -Wall -Wextra -pedantic`.
Temporary executables produced `9` and `35` / `124`, respectively. No trial
source was edited. The subsection distinguishes the experimental syntax from
full Lykn. The Cobalt draft build passed after the addition.
