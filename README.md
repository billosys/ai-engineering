# AI Engineering

[![][build-badge]][build]
[![][tag-badge]][tag]
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[![][logo]][logo-large]

> A library of AI-optimized engineering skills for LLM coding assistants —
> Claude, Claude Code, Cowork, Codex, or anything that reads Markdown. It
> includes reference-grade language and tooling knowledge bases (Rust, Go,
> Erlang/OTP, JavaScript/Deno, Cobalt, Tailwind CSS, Visual Design, and the
> Biome and Deno linters — see [the skill library](#the-skill-library) below
> for details), plus the **collaboration framework** that governs how the work
> actually gets done.

What has become clear over usage across many projects of various sizes,
complexity, and duration is that the **collaboration framework may be the most
valuable asset in this repo**. The language skills make an LLM's output better
in one domain at a time; the framework makes the collaboration itself
trustworthy across all of them.

## The collaboration framework

One skill — loaded as **`/collaboration-framework`** — that turns an LLM
coding session into an engineering project.

### The problem it solves

Unsupervised LLM development fails in predictable, well-documented ways, and
most of them are invisible until they bite. The one that motivated this
framework: **silent drops**. An LLM works through a large task list, reports
success, passes all tests — and quietly defers some of the work along the way,
without ever telling you. Measured informally across this repo's originating
projects, roughly 15–20% of features and tasks were being silently deferred:
"done" milestones that were 85% done, discovered only when later work depended
on the missing pieces. Add the other structural failure modes — spec-softening
(the spec quietly drifting to match what was produced), failed abstractions
and refactorings, and sycophancy (a collaborator trained to please rather than
push back) — and speed stops being the bottleneck. *Trust* is.

None of this is a defect of any particular model; it is structural, and it
shows up in the research literature as reliably as it shows up in real
projects. So the framework treats it the way other fields treat structural
failure: with process controls, adapted from domains where checklists are a
matter of life and death — nuclear corrective-action programs, aviation
safety, surgical checklists.

### What you get

- **A shared vocabulary for the work.** Every effort decomposes the same way
  in every project: **project → arc → slice**, where a slice is one mergeable
  diff. Plans travel between projects and sessions because the words never
  change.
- **A 9-point SDLC.** Research → project definition → design doc → arc/slice
  breakdown → per-slice implementation plan → self-review → peer review →
  feedback loop → full audit. Each step catches errors at a different
  altitude; skipping one routes those errors downstream where they cost more.
- **Ledger discipline.** Every acceptance criterion becomes a verifiable
  ledger row that must be closed with graded evidence before the work is
  "done" — and the closer is never the verifier. This is the discipline that
  eliminates silent drops: since adopting it, the drop rate on these projects
  has gone from ~15–20% to zero observed, and most slices now land correctly
  on the first iteration instead of the third or fourth.
- **A peer, not a sycophant.** A constitution supplement establishes the peer
  frame: the LLM is expected to push back on faulty reasoning, name its own
  uncertainty, and flag when it's at the edge of its capability — *before*
  failure, not after.
- **Independent audits and hard coverage targets.** Whole-repo,
  severity-graded quality audits (never performed by the instance that wrote
  the code), and a coverage prompt that doesn't stop short of the threshold.
- **Subagent guardrails.** A clean line between thinking work (keep in the
  main context) and lookup work (delegate freely) — because LLMs instructing
  other LLMs play a lossy game of telephone.

The honest trade-off: everything gets slower. What you get in exchange is the
velocity of an excellent engineer operating at sustained peak — instead of the
much faster production of code you cannot trust.

From a developer partway through their second framework-run slice of a legacy
codebase rework:

> The collaboration framework skill has been especially useful because it's
> helping me learn the project-management framework as I work through the
> slice, rather than just completing a set of predefined steps for me. …
> [It] feels more challenging, but also more engaging, and I can already see
> how the structure is helping me build familiarity and confidence with the
> framework.

### How to use it

1. **Build it:** `make collab-framework` produces `collaboration-framework.zip`
   (or grab it from a release).
2. **Install it:**
   - *Claude Desktop / claude.ai / Cowork:* upload the zip in your Skills
     settings.
   - *Codex:* `make install` builds every skill and unpacks them into
     `~/.agents/skills/` (override with `INSTALL_DIR=...`).
3. **Load it at the start of every substantial session:** invoke
   `/collaboration-framework` (or reference the skill) before any planning or
   implementation begins.
4. **Say what you want to build.** The skill takes it from there: it
   establishes the posture, confirms the project layout with you before
   creating anything, and walks the SDLC with you — asking the questions a
   good engineering partner would ask, and loading the deeper framework
   documents only when the work calls for them.
5. **For larger projects, run two seats.** A planning/review session (e.g.
   Claude Desktop) owns the project plan, arcs, slices, and ledgers; an
   implementation session (e.g. Claude Code) executes one slice at a time.
   The implementer's prompt can be minimal — *"read and follow the
   instructions in `<slice dir>`"* — because the plan already carries the
   context. The implementer reports back; the planner verifies the ledger;
   nothing advances until the ledger closes.

Load the language skills below *alongside* the framework, per task: the
framework is the *how we work* layer, the knowledge bases are the *what's
correct in this language* layer. They compose; neither subsumes the other.

### Under the hood

The skill is a single [`SKILL.md`](./SKILL.md) that carries the posture and
disciplines inline and routes to nine source documents as the work demands:

- [`AI-CONSTITUTION-SUPPLEMENT.md`](./docs/AI-CONSTITUTION-SUPPLEMENT.md) — character and posture: the peer frame, collaborative rights, structural pulls
- [`AI-ENGINEERING-METHODOLOGY.md`](./docs/AI-ENGINEERING-METHODOLOGY.md) — craft and practice: the three pillars and the 9-point SDLC
- [`PROJECT-MANAGEMENT.md`](./docs/PROJECT-MANAGEMENT.md) — scales of work, canonical planning layout, top-down planning and bottom-up close machinery
- [`LEDGER-DISCIPLINE.md`](./templates/LEDGER-DISCIPLINE.md) — the per-scale verification protocol (slice / arc / project)
- [`CODE-AUDIT.md`](./docs/CODE-AUDIT.md) — the whole-repo, per-language audit prompt
- [`CLAUDE-CODE-COVERAGE.md`](./docs/CLAUDE-CODE-COVERAGE.md) — the 95%+ test-coverage prompt
- [`SUBAGENT-DELEGATION-POLICY.md`](./docs/SUBAGENT-DELEGATION-POLICY.md) — the thinking-vs-lookup delegation line
- [`CONTRIBUTION-STYLE.md`](./docs/CONTRIBUTION-STYLE.md) + [`CONTRIBUTION-TICKET.md`](./templates/CONTRIBUTION-TICKET.md) — voice, discipline, and template for upstream OSS tickets

Each is self-contained and can also be dropped directly into a project's
`CLAUDE.md` or your personal defaults.

## The skill library

Nine knowledge bases live under [`./knowledge/`](./knowledge), one directory
per domain, each with its own `SKILL.md` entry point. They share one design:

- **Modular** — load one domain without dragging in the others
- **Sourced** — every pattern traces to an authoritative origin
- **Graded** — every pattern is marked MUST, SHOULD, CONSIDER, or AVOID
- **Exampled** — every pattern has paired good / bad code
- **Cross-referenced** — concepts link within and across domains

| Skill | What it covers |
|-------|----------------|
| [Rust](./knowledge/rust/README.md) | 661 graded patterns across 17 chapters, grounded in 21 upstream sources. The original skill. |
| [JavaScript / Deno](./knowledge/js/) | Plain JavaScript (no TypeScript), ESM-only, Deno-first — idioms, async, JSDoc type discipline, JSR publishing. |
| [Go](./knowledge/go/) | Go 1.22+, reconciling the Uber and Google style guides with *Effective Go* and the spec. |
| [Erlang / OTP](./knowledge/erlang/) | 281 patterns across 17 chapters — OTP behaviours, supervision, let-it-crash, production ops, testing, tooling. |
| [Visual Design](./knowledge/design/) | A perceptual-science-grounded design system: OKLCH colour, modular type scale, spatial primitives, CUBE CSS. |
| [Tailwind CSS v4](./knowledge/tailwindcss/) | CSS-native v4 configuration, with v3 → v4 breaking changes called out explicitly. |
| [Biome](./knowledge/biome/) | Two skills: a JS-only linter (257 rules) and a full web linter (394 rules incl. a11y and CSS). |
| [Deno lint](./knowledge/deno/) | Deno's 70 lint rules, language-level only. Complements the Biome JS linter. |
| [Cobalt](./knowledge/cobalt/) | The Rust-native static site generator and its Liquid templates — 32 patterns from config to deployment. |

Each skill's own `README.md` carries the full chapter list, sources, and
pattern counts. To use one, point your loader at its `SKILL.md`, reference it
from your project's `CLAUDE.md`, or install the packaged zip (below). Every
skill is plain Markdown, so any AI tool can consume it — a good minimal
loadout for an unsupported tool is the `SKILL.md` plus the domain's
anti-patterns guide.

Every knowledge base follows the same anatomy, so once you've learned one,
you've learned them all:

```text
knowledge/<domain>/
├── SKILL.md              # Entry point with frontmatter: name, triggers, scope
├── guides/               # Numbered topic guides — the patterns themselves
├── concept-cards/        # Atomic, single-concept reference (where present)
├── extraction-metadata/  # The audit trail for every claim
└── sources/              # The original material the guides were extracted from
```

## Building and installing

Everything packages through the [`Makefile`](./Makefile). Each zip is named
after the skill's frontmatter `name:`, wraps its contents in a matching
directory, and contains exactly the `SKILL.md` plus its guides — nothing else.

```sh
make all               # every skill: all nine domains + the collaboration framework
make skills            # just the nine per-domain zips
make collab-framework  # just collaboration-framework.zip

# ...or build one domain at a time:
make rust              # -> rust-guidelines.zip
make go                # -> go-guidelines.zip
make js                # -> javascript-deno-guidelines.zip
make erlang            # -> erlang-guidelines.zip
make cobalt            # -> cobalt-guidelines.zip
make design            # -> visual-design-system.zip
make tailwindcss       # -> tailwindcss.zip
make deno              # -> deno-js-linter.zip
make biome             # -> biome-js-linter.zip AND biome-linter.zip

make install           # build everything and unpack into ~/.agents/skills/
                       #   (Codex-ready; override with INSTALL_DIR=...)
make uninstall         # remove installed skills from the install dir
make check-skills      # validate every SKILL.md description length
make clean             # remove build/ and all generated zips
make help              # list every target
```

The zips upload directly into Claude Desktop / claude.ai as skills; unzipped
(which is what `make install` does), they work with Codex out of the
`~/.agents/` tree.

## Repository layout

```text
ai-engineering/
├── SKILL.md           # The collaboration-framework skill (entry point)
├── Makefile           # Packaging and install targets (above)
├── knowledge/         # The nine-domain skill library
├── docs/              # The framework documents + design/dev notes
│   ├── dev/           #   Phase 0 methodology: how a knowledge base gets built
│   └── design/        #   Research seeding the various efforts here
├── templates/         # GUIDE.md (new-guide skeleton), LEDGER-DISCIPLINE.md,
│                      #   CONTRIBUTION-TICKET.md
└── scripts/           # Extraction helpers (PDF/EPUB/HTML → Markdown, etc.)
```

The [`docs/dev/`](./docs/dev/) directory is the closest thing this repo has to
a field manual for adding a new domain: taxonomy, tier definitions, competency
questions, source prioritisation, and extraction methodology.

## Contributing

Contributions are welcome. For a new pattern in an existing skill: follow that
domain's pattern format, include good **and** bad examples, add a strength
indicator, cross-reference related patterns, and update the relevant index
tables. For a new domain: start from
[`templates/GUIDE.md`](./templates/GUIDE.md), work through the Phase 0
documents in [`docs/dev/`](./docs/dev/), and please raise an issue first to
discuss scope.

## License

MIT — see [LICENSE](./LICENSE).

Individual knowledge bases synthesize material from sources under various
licenses, documented inside each skill's own README. When in doubt, defer to
the original sources.

[//]: ---Named-Links---

[logo]: assets/images/logo-y250.png
[logo-large]: assets/images/logo-x1672.png
[build]: https://github.com/billosys/ai-engineering/actions/workflows/ci.yml
[build-badge]: https://github.com/billosys/ai-engineering/actions/workflows/ci.yml/badge.svg
[tag-badge]: https://img.shields.io/github/tag/billosys/ai-engineering.svg
[tag]: https://github.com/billosys/ai-engineering/tags
