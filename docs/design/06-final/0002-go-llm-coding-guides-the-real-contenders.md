---
number: 2
title: "Go LLM coding guides: the real contenders"
author: "design and"
component: All
tags: [change-me]
created: 2026-04-20
updated: 2026-04-20
state: Final
supersedes: null
superseded-by: null
version: 1.0
---

# Go LLM coding guides: the real contenders

**The best Go guides for AI agent consumption are not the popular Cursor rule collections — they're a small wave of Anthropic-style SKILL.md repositories shipped in late 2025/early 2026, plus the Uber, Google, and bahlo style guides which remain the gold-standard source of GOOD/BAD example pairs.** Almost every entry in the big "awesome-cursorrules" and cursor.directory ecosystems is persona-style directive text ("you are an expert in Go… do X, avoid Y") with no paired code counterexamples, and therefore fails the user's core criterion. The strongest LLM-native option is **samber/cc-skills-golang**, which mandates `// ✓ Good` / `// ✗ Bad — <reason>` pairs via a repo-wide `CLAUDE.md` authoring standard and publishes a measured `EVALUATIONS.md`. The strongest non-LLM source remains the **Uber Go Style Guide**, whose side-by-side Bad/Good markdown tables are effectively ready-to-train example pairs. The user's known baseline, **cxuu/golang-skills**, sits just behind samber in quality but ahead in concision. Below is a ranked, annotated inventory so the user can later pick which guide contributes what to a synthesis.

## Tier 1: LLM-native Go SKILL.md repositories

These are purpose-built for AI agents (Anthropic Agent Skills format: SKILL.md with YAML frontmatter, progressive disclosure via `references/`, tight token budgets). They are the most directly usable, but quality of the DO/DON'T pairs varies.

**samber/cc-skills-golang** — https://github.com/samber/cc-skills-golang — is the single strongest candidate. It lists ~43 skill folders spanning naming, error-handling, concurrency, context, testing, performance, benchmarking, CLI, code-style, linter, modernize, safety, security, observability, troubleshooting, database, DI (wire/dig/fx), design patterns, gRPC, GraphQL, project-layout, documentation, plus library-specific skills (testify, slog, cobra, viper, swagger, temporal, samber/do, lo, mo, ro). A root `CLAUDE.md` enforces the format `// ✗ Bad — <reason>` paired with `// ✓ Good`, giving the **most consistent and reason-annotated DO/DON'T pairs of any Go resource surveyed**. Verified snippet from `golang-linter`: `//nolint:errcheck // fire-and-forget logging, error is not actionable` (Good) vs bare `//nolint` (Bad). `EVALUATIONS.md` scores each skill's "error-rate gap" (e.g., golang-error-handling −26%, golang-modernize −61%), the only repo with empirical skill validation. MIT license. Strict token budgets (~100/1000–2500/10k). Excels across virtually every target domain; weakest on pure project-structure opinion. **Rating 10/10 as a base.**

**cxuu/golang-skills** — https://github.com/cxuu/golang-skills — the user's known baseline. 16 skills (naming, error-handling, concurrency, testing, performance, code-review, linting, project-layout, security, style-core, control-flow, interfaces, packages, declarations, documentation, defensive), Apache-2.0, ~76 stars, last commit March 2026. Each SKILL.md is kept under ~225 lines by design and sources itself explicitly from Uber + Google style guides. DO/DON'T is expressed via inline `// Good` / `// Bad` comments plus `> **Normative**` vs `> **Advisory**` tier markers and ASCII decision trees (the naming skill's decision flow is exemplary). 51 trigger + 15 quality evals in `evals/evals.json`. **Strengths**: tightness, decision-tree pedagogy, strong source attribution. **Weaknesses**: smaller coverage than samber; no DB/observability/DI skills. **Rating 9/10.**

**saisudhir14/claude-skills** — https://github.com/saisudhir14/claude-skills — 9 Go-specific skills (error-handling, concurrency, testing, performance, code-review, linting, project-layout, security, plus a root SKILL.md). Its unique value is **most-modern Go coverage**: Go 1.21→1.25 features including `errors.Join`, typed atomics, range-over-func iterators, `t.Context`, `T.Chdir`, `b.Loop`, `synctest`, `runtime.AddCleanup`, weak pointers, `os.Root`, container-aware `GOMAXPROCS`, experimental `json/v2`, and generic type aliases. MIT, small (6 stars). **Caveat**: body-level DO/DON'T quality could not be directly verified in this pass due to GitHub access errors; the README claims compliance across 20+ agents. **Rating 7/10 (provisional, pending body inspection)** — worth fetching for Go 1.25 content even if overall format is weaker than samber.

**JetBrains go-modern-guidelines** — ships via Claude Code `/use-modern-go` command and detects Go version from `go.mod` to enforce version-appropriate modern syntax. Referenced in https://blog.jetbrains.com/go/2026/02/20/write-modern-go-code-with-junie-and-claude-code/ . Framed as "modern vs obsolete" which plausibly yields paired examples. Vendor-authored and therefore credible. **Worth a direct fetch by the user** — this is the most likely source for well-curated before/after pairs around Go version upgrades.

**Smaller/single-skill Go SKILL.md repos worth scanning:**
- `madflojo/go-style-agent-skill` — single go-style-guide skill with references for BENCHMARKS, CONFIG, CONCURRENCY, DOCUMENTATION, ERRORS, INTERFACES, LAYOUT, LOGGING, REVIEW-CHECKLIST, TESTING. Installable via `gh skill install`. Go 1.21+, errors.Join, log/slog.
- `peixotorms/odinlayer-skills` — notable for a `go-concurrency` skill with verbatim `// BAD: context in struct` vs `// GOOD: context as first parameter` pairs. Good concurrency-specific contribution.
- `gapupfade/claude-skills-Sr.Dev` — `skills/golang-pro/SKILL.md` with references for concurrency, interfaces, generics, testing, project-structure. Senior-dev persona.
- `manutej/luxor-claude-marketplace` — `golang-backend-development` SKILL.md in luxor-backend-toolkit plugin.
- `darrenoakey/claude-skill-golang` — emphasizes zero-fabrication testing and mandatory quality gates (gofmt/go vet/golangci-lint). Format unverified.
- `thealish/golang-skill` — minimal single-file, multi-agent compatible.
- `openshift/hypershift/.claude/skills/effective-go` — thin pointer to official Effective Go; useful only as a reference model.

## Tier 2: Traditional style guides that are the gold source for DO/DON'T pairs

These are human-oriented but their example-pair format makes them the highest-quality *raw material* for an LLM skill. Almost every Tier 1 repo derives from these.

**Uber Go Style Guide** — https://github.com/uber-go/guide/blob/master/style.md — **the single best source of Go GOOD/BAD pairs on the internet**. Renders 50+ rules as two-column markdown `Bad | Good` tables with rationale prose. Section coverage: pointers-to-interfaces, interface compliance, receivers/interfaces, zero-value mutexes, slice/map copying at boundaries, defer cleanup, channel sizing, enum starts, time package, errors (types/wrapping/naming), type-assertion handling, no-panic, atomics, no-mutable-globals, no-init, exit-in-main, field tags, goroutine lifetimes (no fire-and-forget, wait-for-exit, none-in-init), performance (strconv vs fmt, string↔byte, container capacity), style (import groups/ordering, nesting, unnecessary else, variable declarations, scope, raw strings, struct/map initialization, Printf naming), patterns (test tables, functional options). **Gaps**: project/repo structure, HTTP handlers, DI, observability, generics. **LLM-adaptability 9/10.** Scoped to "last two Go releases" (modern).

**Google Go Style Guide** — https://google.github.io/styleguide/go/ spanning three documents: `/guide` (canonical short principles), `/decisions` (normative, very long, the main payload), `/best-practices` (non-normative supplemental). Uses vertically-stacked `// Good:` / `// Bad:` code-comment blocks rather than side-by-side tables, which makes extraction slightly harder but still automatable. **Strongest coverage of naming** (definitive initialism table), error structure, `%w` wrapping semantics, documentation conventions, test doubles (stubs/fakes), global-state avoidance, and concurrency philosophy. **Unique strength**: rationale-rich — explains *why* behind each rule. **Weaknesses**: not every rule has both halves; project structure absent; bans third-party assertion libs (Google-internal). **LLM-adaptability 8/10.**

**bahlo/go-styleguide** — https://github.com/bahlo/go-styleguide — the **cleanest explicit `Don't:` / `Do:` heading format** of any Go guide, but narrow (~15–20 rules: error context, dependencies, import grouping, no-globals, small-main, linters/formatters, structured logging, no-side-effects, pure functions, no-over-interfacing, no-under-packaging, signal handling, no-unadorned-returns, canonical import paths, table-driven tests). **Format 9/10, coverage 5/10.** Best used as a template or to seed high-confidence pairs for the handful of topics it covers.

**Go Code Review Comments** — https://go.dev/wiki/CodeReviewComments — canonical community rule list (~30 items) but prose-dominant with few explicit pairs. Use as a *rationale and completeness-check reference*, not as a primary example-pair source. **Rating 6/10.**

**Effective Go** — https://go.dev/doc/effective_go — foundational but largely unchanged since 2009 and written as an essay; examples illustrate rather than contrast. Wrong format for direct extraction. **Rating 4/10** — cite for authority, don't mine for pairs.

## Tier 3: Domain-specialized resources

Use these to plug coverage gaps in any tier-1 repo.

**Error handling.** Dave Cheney's "Don't just check errors, handle them gracefully" (https://dave.cheney.net/2016/04/27/dont-just-check-errors-handle-them-gracefully) defines the sentinel/typed/opaque taxonomy every other guide uses. Pairs are implicit (anti-pattern → fix) rather than formatted, but the reasoning is definitive. Pair with Uber's Errors section and Google's `%w` semantics coverage.

**Concurrency.** Uber's "Goroutine Lifetimes" sub-section is the best compact reference; `peixotorms/odinlayer-skills` `go-concurrency` has clean `BAD:/GOOD:` pairs on context-in-struct, worker pools, fan-in/out, semaphore, WaitGroup, Once, select patterns; `samber/cc-skills-golang` `golang-concurrency` + `golang-context` split is cleanest for AI consumption.

**Interface design.** Google Go Best Practices' Interfaces section is the **most-nuanced take on "accept interfaces, return structs"** — explicitly tells you *not* to define interfaces before use and not to export test-double implementations. Dave Cheney's "SOLID Go Design" (https://dave.cheney.net/2016/08/20/solid-go-design) is the prose companion.

**Project layout.** The widely-cited `golang-standards/project-layout` is controversial (see issue #117 and Laurent Senta's critique at https://laurentsv.com/blog/2024/10/19/no-nonsense-go-package-layout.html). For an authoritative baseline, cite the **official go.dev guidance**: https://go.dev/doc/modules/layout . For production examples, reference `ardanlabs/service` (Bill Kennedy) and `bxcodec/go-clean-arch`. None have DO/DON'T pairs — they're exemplars, not rule files.

**Testing.** Google Decisions has strong opinions (table-driven subtests, no exported test doubles, minimal interfaces for testing). `samber/cc-skills-golang/golang-stretchr-testify` covers assert-vs-require with clear rationale if the project uses testify. `saisudhir14/claude-skills/go-testing` has the best modern coverage (`T.Context`, `T.Chdir`, `b.Loop`, `synctest`).

**Performance.** Uber Performance section (strconv vs fmt, string↔byte, preallocation) plus `samber/cc-skills-golang/golang-performance` and `golang-benchmark` (benchstat methodology, pprof workflow, diagnose-before-fix) together cover the space well.

**HTTP/API/gRPC.** `samber/cc-skills-golang/golang-grpc` is the best LLM-native take. For HTTP stdlib, `PatrickJS/awesome-cursorrules/go-servemux-rest-api-cursorrules` is LLM-formatted but directive-only (no pairs). The `agentsmd.net` Go Microservices AGENTS.md template is broader but similarly thin on paired examples.

## Tier 4: Notable but fail the DO/DON'T requirement

Documented here so the user doesn't waste effort revisiting them.

The curated Cursor and Claude rule ecosystems were investigated thoroughly and **virtually none of their Go entries contain paired code counterexamples**. They are persona-style prompts ("you are an expert in Go…") with imperative bullet lists. The best among them are worth mentioning for scope inspiration but not as synthesis inputs:

- **VoltAgent/awesome-claude-code-subagents/golang-pro.md** — 277 lines, the most comprehensive topical Go checklist (Go 1.21+ idioms, concurrency mastery, error handling, pprof, sync.Pool, fuzzing, gRPC, circuit breakers, graceful shutdown, K8s operators, escape analysis, CGO). Zero code snippets or paired examples.
- **cursor.directory Go microservices rules** (Ehsan Davari) — well-organized headings covering clean architecture, OpenTelemetry, circuit breakers, retry/backoff, Redis rate limiting, table-driven tests, golangci-lint, GoDoc. No code pairs.
- **PatrickJS/awesome-cursorrules Go entries** — six rule files (basic, backend-scalability, servemux-rest-api, fiber, temporal-dsl, htmx-go-basic). Only one (backend-scalability) shows any worked code, and it lacks a contrasting bad example.
- **sanjeed5/awesome-cursor-rules-mdc/rules-mdc/go.mdc** — generator-produced MDC; content not verified but the generator (Exa + Gemini) typically produces directives without paired anti-examples.
- **steipete/agent-rules** — archived, Swift-focused, **no Go content**.

## How to combine them later (practical guidance, not synthesis)

When the user moves to synthesis, the natural pattern is: **adopt samber/cc-skills-golang's `CLAUDE.md` authoring standard and skill layout as the backbone** (because it enforces reason-annotated ✓/✗ pairs), **seed the core skills from cxuu/golang-skills** (for its tight <225-line skills and Uber/Google source attribution), **mine Uber Go Style Guide for raw example pairs** (because they're already side-by-side), **layer Google Decisions for naming and error-wrapping rigor**, **add saisudhir14 or JetBrains go-modern-guidelines for Go 1.22–1.25 features**, and **plug gaps with domain-specific Dave Cheney and Google Best Practices excerpts**. Skip Tier 4 entirely — rewriting them as paired examples is nearly as much work as writing fresh content.

## Conclusion

The universe of Go LLM coding guides is shallower than the Cursor/Claude rule collections suggest: **only three repositories are genuinely LLM-native with paired examples** (samber/cc-skills-golang, cxuu/golang-skills, saisudhir14/claude-skills), and their quality is built on top of two underlying human-oriented gold standards (Uber and Google). The single most important insight from this survey is that **most "AI Go rules" online are persona-prompts without contrastive examples, and should not be treated as candidates for serious synthesis**. The three tier-1 skill repos — particularly samber/cc-skills-golang with its measured EVALUATIONS.md — represent the current state of the art, and together with the Uber and Google style guides they provide more than enough raw material to build an authoritative Go SKILL.md bundle.
