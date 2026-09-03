# README Source Surface Map

Date: 2026-09-02
Slice: Arc04 Slice01 README and docs decomposition map
Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`
Source commit inspected: `9b6d5d83d9c8debd977609aa1118004e89e2c895`

## Source Status

`git status --short --untracked-files=all` returned no output before this
read-only inspection. No source commit was created.

## Current README.md Sections

| README.md surface | Current role | Arc04 disposition |
| --- | --- | --- |
| Title, badges, logo, and one-paragraph About | Repository orientation | Keep in `README.md`, shorten and update date during Slice02. |
| Contents | README-local navigation | Replace with links to focused `docs/` guides after Slice02/Slice03 create them. |
| The collaboration framework | Long product/method explanation | Move most explanatory prose to a focused `docs/collaboration-framework.md`; keep a short orientation and link in `README.md`. |
| The problems / The solutions | Origin and rationale narrative | Move or route to `docs/ORIGINS.md` plus focused collaboration-framework guide. Keep only a brief value statement in README. |
| Framework components | Component contract table | Move to focused collaboration-framework or skill-library guide; keep a short summary and link. |
| What you get / How to use it | Usage guidance and operating model | Split between `docs/collaboration-framework.md` and `docs/building-and-installing.md`; README keeps a minimal quick-start. |
| The skill library | Current package/source overview | Move detail to `docs/skill-library.md`; README keeps short pointer to `knowledge/`. |
| Domain and tooling skills | Long package table | Move to `docs/skill-library.md`; keep a compact package-list pointer in README. |
| Method skills | Planned method-skill explanation | Route to `docs/skill-library.md` with provisional language; final public skill kind and atomic/composite vocabulary remains Arc05. |
| Building and installing | Commands and package behavior | Move full command table to `docs/building-and-installing.md`; README keeps the shortest build/install commands. |
| Repository layout | Layout tree | Move to `docs/repository-overview.md` or `docs/knowledge-library-anatomy.md`; update stale post-Arc03 paths. |
| Composite Cognition Dispatch Protocol | Protocol overview and package guidance | Move most prose to `docs/protocols.md`; README keeps a short pointer to `protocols/ccdp/README.md`. |
| Contributing | Contribution path | Move detailed guidance to `docs/contributing.md`; README keeps one short contribution link. |
| License and named links | Legal/footer support | Keep in `README.md`; update links only if adjacent edits require it. |

## Existing docs/ Surface

Current `docs/` contains:

- `docs/ORIGINS.md`

`docs/ORIGINS.md` is end-user documentation about the repository's originating
failure modes and framework history. It should remain under `docs/`, but its
links still point at several pre-Arc03 framework paths and need repair in a
later source-edit slice.

## Post-Arc03 Source Anchors

Arc04 documentation should describe these post-Arc03 anchors:

- `README.md` as the top-level orientation page.
- `docs/` as end-user explanation about repository materials.
- `knowledge/` as the knowledge-library substrate.
- `SKILL.md` as the top-level collaboration-framework skill entrypoint.
- `Makefile` as the package/build/install command surface.
- `protocols/ccdp` as the CCDP protocol distribution.
- `templates/GUIDE.md` as the remaining top-level cross-cutting template guide.

## Known Stale Routes To Repair Later

Read-only inspection found stale or likely stale README/docs routes:

- `README.md` describes `docs/` as containing framework documents plus
  `docs/dev/` and `docs/design/`, but after Arc03 current `docs/` contains only
  `docs/ORIGINS.md`.
- `README.md` mentions `templates/LEDGER-DISCIPLINE.md` and
  `templates/CONTRIBUTION-TICKET.md` in the layout tree, but those owner-local
  templates moved under `knowledge/work-verification/` and
  `knowledge/contribution-style/`.
- `README.md` points new-domain contributors to `docs/dev/`, which no longer
  exists after Arc03.
- `docs/ORIGINS.md` links to former framework documents such as
  `CODE-AUDIT.md`, `AI-ENGINEERING-METHODOLOGY.md`,
  `PROJECT-MANAGEMENT.md`, and `SUBAGENT-DELEGATION-POLICY.md` under `docs/`;
  those materials now live under `knowledge/` component roots.
- `docs/ORIGINS.md` links to `../templates/LEDGER-DISCIPLINE.md`, which moved
  to `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`.

These are source documentation edit targets for later Arc04 slices, not
authorized Slice01 edits.
