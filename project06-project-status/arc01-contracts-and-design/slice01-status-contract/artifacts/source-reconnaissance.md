# Source and consumer reconnaissance

Inspected 2026-09-06 by the coordinating contributor. This is source inspection
and planning input, not a code audit, independent verification, or consumer UAT.

## Revisions and authority

| Repository/tree | Observed HEAD | State and use |
| --- | --- | --- |
| ai-engineering main | 5f10690256d96bcb0a163ce0ca5b1a6edf7d56ab | Clean at initial check; current skill/packaging source |
| ai-engineering planning | 16b5818 (short ID observed) | Clean before this project bootstrap; existing Projects01–05 |
| Rootstock planning | 9ec7c469b97e54b675bfc1b7857ccbdc078bf413 | Clean at trial inspection; private status source |
| Lykn planning | ef0a1155cb65884456c5eaf52bdaa49af0d50055 | Hardware project has tracked edits and untracked artifacts; working-tree observations are not all commit-pinned |

Source locator: Rootstock's `.worktrees/planning/status/` under the repository
the operator supplied. Consumer locator: Lykn lang's `.worktrees/planning/`.
Read those repositories in place; do not vendor their raw private content into
this public skill. Refresh revisions/state before implementation or adoption.

Routing update, 2026-09-06: the operator subsequently created branch
`feature/project-status` in `.worktrees/project-status-feature`, observed at
`31d96b1` with a clean working tree when routing was updated. That worktree is
now the source-read, implementation and validation home. The main observation
above is retained as historical reconnaissance, not a current execution route.

## Rootstock extraction evidence

The status tree contains one hub status JSON, three project status JSON files,
eight arc status JSON files, their HTML counterparts, a lessons pair, two
scripts, six Jinja templates and one shared CSS file. No formal status schema
files were found in the inspected repository/worktree filename search. The
JSON documents lack `$schema`; the data examples and template reads currently
form the effective contract.

`status/scripts/render-status.py` uses Python/Jinja2 and a hard-coded `PAGES`
manifest for 13 pages, including lessons. It resolves its root from its own
location, supports historical sibling-worktree data paths, defaults missing
generation dates to today, skips absent data with a message, and embeds shared
CSS. `setup-venv.sh` creates a local environment and installs unpinned Jinja2.
The renderer disables autoescaping and does not enable strict undefined-field
handling or schema validation. These observations motivate explicit contracts;
they are not an instruction to copy every behavior.

Template source observations:

- Project views: Frontier, Instrument, Spine. Arc view: child sequence,
  evidence/gates, findings and close criteria. Hub: portfolio and a
  Rootstock-specific reconciliation/port lane. Lessons is adjacent material.
- CSS uses shared light/dark OKLCH tokens and separate neutral evidence pips
  versus status-colored indicators. Fonts still reference Google Fonts despite
  CSS embedding; static pages should have an explicit offline-font policy.
- `project_status.html.jinja` renders unconditional “Nothing blocked,”
  “check green,” “no drift,” and topological-sort/refreshed-on-read claims.
  The inspected renderer consumes authored JSON without implementing that
  graph or world-state reconciliation.
- `arc_status.html.jinja` reads finding `id`, `text`, `disp`, and `disp_cls`.
  Four arc documents contain findings missing some of these fields; several
  instead supply title/detail. Default Jinja missing-field behavior can lose
  information while rendering successfully.
- The frontdoor arc supplies gate_filled=6 while the arc template draws four
  gates. Slice displays use six. Gate meaning needs a named contract.
- The partner-gateway project summary says slices_done/total=24/31, while the
  nine arc rows sum to 19/26. The inspection establishes disagreement, not
  which count reflects authoritative planning. Coverage/count semantics must
  allow a check to detect or explain such differences.
- Project/arc titles and theme storage retain ODM-specific strings; the hub
  contains source-branch-specific workflow prose. Generalisation requires
  an explicit extraction map and fictional examples.

No renderer was run against the original tree. Browser policy blocked the local
HTML URL during reconnaissance, so the view observations are based on template,
CSS and generated-file source, not visual acceptance of rendered pages.

## Lykn planning scope

The planning README and six project plans were inspected, along with the
migration plan, planning governance and representative research, hardware and
decimal-wrapper arc plans. Counts below are top-level directories, not a census
of open work or verified capabilities.

| Project | Declared plan status | Arc directories | Direct slice directories |
| --- | --- | --- | --- |
| project01-mvp | historical-archive | 18 | 0 |
| project02-language-toolchain-alignment | active | 19 | 0 |
| project03-language-evolution | research | 0 | 3 |
| project04-c-lang | research-seed | 1 | 0 |
| project05-hardware | active | 7 | 0 |
| project06-planning-reorg | implemented-awaiting-operator-review | 3 | 0 |

The MVP plan explicitly calls its arcs approximate capability groupings and
declines to fabricate historical slices. Alignment has decimal arc wrappers
that preserve prior standalone-slice records without creating new acceptance
claims. Evolution's three research slices live directly under the project.
C-target research has an arc but no current slice-plan files. Hardware has
ongoing edits in its project plan and first arc/slices; evidence can be physical
measurement or operator attestation, not just automated software tests.

The migration plan states that mechanical verification is delivered while
operator review of approximate historical grouping remains pending, and that
this does not block using the planning tree. This is a current source statement,
not an independently repeated migration check in Project06. Do not turn that
pending review into a toolkit prerequisite or a verified-closed status.

The baseline contains 48 top-level arc directories across six projects. This
does not imply 48 required arc-status pages: the operator requested all project
statuses and open arcs. Their actual adoption census requires reading current
plans, ledgers and verification, resolving uncertainty with the operator, and
recording the then-current revision/local changes. The status rebuild remains
future consumer work after a usable toolkit candidate exists.

## Reproduction routes

- Use `git worktree list`, `git rev-parse HEAD`, and `git status --short` in
  each named repository/worktree to refresh identity and state.
- Enumerate Rootstock's `status/` and parse all `*status.json`; inspect field
  keys and template reads. Sum project arc rows separately from authored totals.
- Enumerate Lykn's top-level `project*/arc*/` and `project*/slice*/`; read each
  project-plan header and the representative arc plans described above.
- Read current ai-engineering Makefile package lists and staging functions.
  Framework bundling has an explicit file list; standalone component staging
  must also be checked for new support-directory inclusion. Packaging design
  must demonstrate scripts, schemas, templates and examples survive both paths.

No consumer modifications, private payload copies, hardware operations, package
builds, or delivery-status reclassifications were performed for this inventory.
