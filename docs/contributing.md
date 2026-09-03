# Contributing

Contributions should preserve the repository's split between explanatory docs
and knowledge substrate. Put user-facing orientation in `docs/`; put skill
source material, guide content, provenance, examples, and owner-local templates
under the relevant `knowledge/` or `protocols/` root.

## Before Changing Files

1. Identify the owning surface.
2. Check whether the change is source material, package behavior, user-facing
   explanation, or protocol material.
3. Run `git status --short --untracked-files=all` so the change scope is clear.
4. Keep commits focused; generated zips should not be committed unless a
   release process explicitly asks for them.

## Updating An Existing Skill

For a small content change, edit the owning `knowledge/<surface>/` files and
run the relevant validation:

```sh
make check-skills
make check-package-paths
```

If the change affects generated package behavior, build the affected package or
run `make all` before validating package paths.

## Adding New Guide Material

Use [`templates/GUIDE.md`](../templates/GUIDE.md) when starting a new reusable
guide. Place the finished guide under the owning knowledge root, usually in
`knowledge/<surface>/guides/`.

If the guide is only explaining where material lives or how users should
navigate the repository, it may belong under `docs/` instead. Avoid copying a
full skill guide into `docs/`; link to the source guide.

## Adding A New Skill Surface

New skill surfaces need more than a new file. At minimum, define the skill
entrypoint, guide set, source/provenance expectations, package target, package
validation, and install route. If skill kind or topology wording is important
to the change, keep the axes separate: kind names what the skill is about, and
topology names how it composes.

## Protocol Changes

CCDP changes live under [`protocols/ccdp/`](../protocols/ccdp/) and use the
CCDP-specific targets:

```sh
make ccdp
make ccdp-package
make check-ccdp-package
```

Do not fold protocol package changes into installable skill package changes
unless a plan explicitly changes that boundary. CCDP is a protocol
distribution, not an installable skill package.

## Documentation Changes

Use `docs/` for reader orientation: what exists, how to choose it, how to
build or install it, and where the source material lives. When editing docs,
run:

```sh
git diff --check
rg -n "\[[^\]]+\]\([^\)]+\)|https?://|docs/|knowledge/|protocols/|templates/|Makefile|package" README.md docs
```

For broader documentation or package-facing changes, also run the package and
CCDP validation targets named above.
