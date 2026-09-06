# AI Engineering

[![][build-badge]][build]
[![][tag-badge]][tag]
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[![][logo]][logo-large]

_Last updated: 2026-09-02._

AI Engineering is a library of Markdown skill packages, guide material,
planned method material, support templates, and protocol distributions for
LLM coding assistants. It is built around a simple split:

- [`docs/`](./docs/) explains the repository for human readers.
- [`knowledge/`](./knowledge/) stores the source and derived material consumed
  by skills and packages.
- [`protocols/`](./protocols/) stores protocol distributions such as CCDP.

## Start Here

- [Repository overview](./docs/repository-overview.md)
- [Skill library](./docs/skill-library.md)
- [Collaboration framework](./docs/collaboration-framework.md)
- [Knowledge library anatomy](./docs/knowledge-library-anatomy.md)
- [Building and installing](./docs/building-and-installing.md)
- [Protocols](./docs/protocols.md)
- [Contributing](./docs/contributing.md)
- [Origins](./docs/ORIGINS.md)

## What Is Here

The repository currently includes:

- domain/tooling skill packages for Rust, Go, Erlang/OTP, C++,
  JavaScript/Deno, Cobalt, Tailwind CSS, Visual Design, Biome, and Deno lint;
- the [`scientific-methods`](./knowledge/scientific-methods/SKILL.md) method
  skill for practical inquiry, controlled comparison, experiment planning,
  evaluation rubrics, evidence capture, and regression analysis;
- the [`collaboration-framework`](./knowledge/collaboration-framework/SKILL.md) composite
  framework/operational skill, with its framework material under
  [`knowledge/`](./knowledge/);
- reusable support material such as the
  [`templates/GUIDE.md`](./templates/GUIDE.md) support template;
- the Composite Cognition Dispatch Protocol under
  [`protocols/ccdp/`](./protocols/ccdp/).

## Quick Commands

```sh
make help              # list package, validation, and install targets
make all               # build all installable skill zips into target/skills/
make collab-framework  # build target/skills/collaboration-framework.zip
make check-skills      # validate SKILL.md descriptions
make check-package-paths
make install           # install built skills into ~/.agents/skills
```

CCDP is packaged separately from installable skills:

```sh
make ccdp
make ccdp-package
make check-ccdp-package
```

## Repository Layout

```text
ai-engineering/
├── README.md          # repository orientation
├── Makefile           # package, validation, install, and CCDP targets
├── docs/              # end-user repository documentation
├── knowledge/         # skill source and derived knowledge substrate
├── protocols/         # protocol distributions, including CCDP
├── templates/         # cross-cutting templates, including GUIDE.md
├── scripts/           # package and validation helpers
└── assets/            # README images and other public assets
```

## Current Boundaries

The `docs/` guides are explanatory wrappers. They should help readers choose,
install, build, and contribute without duplicating the full material under
`knowledge/`.

Skill kind and topology are separate. Kind says what a skill is about, such as domain/tooling, framework/operational, or method work. Topology says how a skill composes: an atomic skill is loaded for one clear, self-contained purpose, while a composite skill selects, sequences, routes, governs, composes, etc., multiple loadable components.

The [`rust`](./knowledge/rust/SKILL.md) skill is an example of an atomic domain/tooling skill. Whereas 
[`collaboration-framework`](./knowledge/collaboration-framework/SKILL.md) is a composite
framework/operational skill and remains the daily-driver composer for most users of the ai-engineering repo. To clear up an additional conceptual point, protocols (such as CCDP) are RFC-style documents, not an installable skill packages.

## License

MIT - see [LICENSE](./LICENSE).

Individual knowledge bases synthesize material from sources under various
licenses, documented inside each skill's own source materials. When in doubt,
defer to the original sources.

[//]: ---Named-Links---

[logo]: assets/images/logo-y250.png
[logo-large]: assets/images/logo-x1672.png
[build]: https://github.com/billosys/ai-engineering/actions/workflows/ci.yml
[build-badge]: https://github.com/billosys/ai-engineering/actions/workflows/ci.yml/badge.svg
[tag-badge]: https://img.shields.io/github/tag/billosys/ai-engineering.svg
[tag]: https://github.com/billosys/ai-engineering/tags
