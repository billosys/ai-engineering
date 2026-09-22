# Layout and identifiers

This is a default filesystem profile for repositories adopting this skill.
It is a local convention, not a CERN standard. Existing collections may retain
another documented profile.

```text
labs/
  README.md                         lab index and local conventions
  lab01-<slug>/
    README.md                       scope, stewardship, experiment index
    journal/
      README.md                     chronological entry index
      YYYY-MM-DD-01-<slug>.md
    procedures/                     reusable setup and operating instructions
    resources/                      shared inputs with an inventory
    inbox/                          new material awaiting disposition
    experiment01-<slug>/
      README.md                     question, kind, status, record links
      protocol.md                   method selected using scientific-methods
      inputs/README.md              input identities and locations
      code/                         acquisition or experiment implementation
      runs/
        README.md                   planned slots and actual attempts
        run0001/
          run.md                    attempt record
          raw/                      captured observations and logs
          derived/                  transformations specific to this attempt
      analysis/
        README.md                   cross-run recipes and source mapping
        figures/                    figures and underlying data references
      report.md                     findings, evidence, limits, next questions
```

Only create directories when they contain useful material. A new lab needs
its README and an entry in the collection index. A bounded experiment needs
its README and method in `protocol.md`; a short protocol is sufficient for a
small inquiry. A run needs its record before execution. Create a journal index
with its first entry and a run index with the first scheduled or actual attempt.

## Identity rules

- Allocate `labNN` across the collection, `experimentNN` within its lab, and
  `runNNNN` within its experiment. Use at least two/two/four digits; allow
  growth beyond the minimum width without renumbering history.
- Use the next unused number; inspect both directories and the index, including
  retired entries. Resolve concurrent allocation conflicts before publication.
  Do not recycle numbers or renumber to close gaps.
- A run's full identity includes its lab and experiment. Use that full path
  in cross-lab references. Slugs are lowercase words separated by hyphens.
- Keep issued paths stable. Change display titles freely in a README. If a
  move is necessary, preserve a forwarding record and an old-to-new mapping.
- Journal names use the entry's stated local date and a daily sequence. Record
  the timezone/UTC offset inside; distinguish event time from writing time.

## Navigation and state

Each index links down to its children; each child entrypoint links to its
parent. Use Markdown links with relative paths inside a repository. Link
cross-repository evidence to a commit or release when identity matters.

Lab states: `active`, `paused`, `retired`. Experiment states: `draft`, `ready`,
`running`, `paused`, `concluded`, `abandoned`. These track activity, not truth:
a concluded experiment can be inconclusive. Run states and outcomes are
specified in [run records](./05-run-records.md).

Keep current summaries in entrypoints and dated changes in records/Git history.
A changed summary should point to the superseded finding when it matters.
