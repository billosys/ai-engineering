# Project01 Path Contract Notes for Project02

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
slice: slice01-source-inventory
status: proposed-done
source-project: project01-harmonise-paths
gate-capture: artifacts/project01-gate-check.txt
```

## Gate Evidence

Project02 execution was gated on Project01 being closed and completely
verified. The gate was checked from the planning worktree before this analysis
began.

Evidence captured in `artifacts/project01-gate-check.txt` includes:

- `../../../project01-harmonise-paths/closing-report.md:5:status: closed`
- `../../../project01-harmonise-paths/closing-report.md:20:DoD verdict: met.`
- `../../../project01-harmonise-paths/project-plan.md:5:status: closed`
- `../../../project01-harmonise-paths/project-plan.md:305-306`: Arc 04 Slice
  03 verified/closed, Arc 04 closed, and Project01 closed with DoD verdict met.
- Project01 slice and arc CDC verification records under
  `../../../project01-harmonise-paths/`.

## Constraints for Project02

### Preserve Source/Package Vocabulary

Project01 closed the source/package path harmonisation project with the
reader-facing distinction intact:

- source clone workflows start from repository paths such as `README.md`,
  `SKILL.md`, `docs/`, `templates/`, and `protocols/ccdp/`;
- generated skill zip workflows start from zip roots named from skill
  frontmatter `name:`;
- unzipped skill workflows must use package-local relative links;
- CCDP is a protocol package built as `ccdp.zip`, not an installable skill zip;
- repo-only or provenance material must be labelled as such and excluded from
  package entrypoint promises.

Project02 must treat those distinctions as source/package constraints when
proposing any collaboration-framework breakout.

### Keep Package Path Checks as Acceptance Gates

Project01's final close report says `make check-package-paths` passed with 12
zips, 171 Markdown files, 0 hard failures, 295 warnings, 3 explicit exceptions,
and 656 skipped external URLs. It also records exception-schema validation and
CCDP package validation.

Project02 implication: any future split of the collaboration-framework source
must preserve or update these package gates deliberately. A new component
boundary is not acceptable until generated zips, package-local Markdown links,
exceptions, and reader guidance are checked in the same release surface.

### Do Not Move Planning Evidence into Source Documentation

Project01 and the current framework PM docs use `.worktrees/planning` as the
planning substrate. Durable slice outputs default to the owning slice's
`artifacts/` directory unless an operator-recorded slice plan says otherwise.

Project02 implication: planning inventory, problem maps, synthesis reports, and
CDC verifications belong in the Project02 planning tree, not in source
`docs/`, root `workbench/`, root `reports/`, or scratch directories. This slice
uses the standard artifact home recorded in `slice-plan.md`: durable analysis
outputs live under `artifacts/`.

### Keep Entrypoints Thin and Stable

Project01 tightened reader-facing guidance so users can distinguish:

- root source checkout guidance;
- skill zip upload guidance;
- unzipped skill install guidance;
- CCDP source and package guidance.

Project02 implication: if the top-level collaboration-framework skill becomes
a composition of smaller components, `README.md` and `SKILL.md` still need to
remain coherent entrypoints. They should route to new component files without
breaking the package-local path contract.

### Treat Current Boundaries as Evidence, Not Authority

Project01 verified paths and packages, not the conceptual correctness of the
current monolithic collaboration-framework boundaries.

Project02 implication: current files are evidence of implemented behavior and
current routing promises. They are not final component boundaries. Slice02 and
Arc02 should test candidate labels against historical problems, load moments,
package behavior, and operator goals.

## Open Questions

- Slice 02: Which path/package constraints are hard compatibility promises, and
  which are only current implementation details?
- Slice 02: Should any future component own `workbench/<DATE>-audit-*.md`
  conventions, or should ledgered audits always prefer slice-local planning
  artifacts?
- Arc 02 operator discussion: If component boundaries change, should package
  names, zip roots, or `SKILL.md` aliases preserve the current monolithic
  collaboration-framework identity?
- Arc 02 decision needed: How much compatibility must be preserved for existing
  Claude Desktop/claude.ai skill imports versus source-clone users?
