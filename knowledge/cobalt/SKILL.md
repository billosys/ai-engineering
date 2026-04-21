---
name: cobalt-guidelines
description: |
  Comprehensive guidelines for building, extending, and deploying static sites
  with Cobalt — a Rust-native static site generator powered by Liquid
  templates — grounded in the official Cobalt documentation, the
  `cobalt-org/cobalt.rs` source, the `cobalt-config` schema, and the Rust
  `liquid` crate family (`liquid`, `liquid-core`, `liquid-lib`, `liquid-derive`).
  Use when: installing Cobalt, scaffolding a new site, authoring pages or
  posts, designing layouts and includes, writing Liquid templates (`{{ }}`
  output, `{% %}` logic, filters, tags, control flow), configuring
  `_cobalt.yml`, setting up permalinks, pagination, RSS, syntax highlighting,
  Sass/SCSS, data files, draft/publish workflow, debugging builds with
  `cobalt debug`, deploying to GitHub Pages / GitLab CI / self-hosting, or
  extending Cobalt programmatically in Rust via `cobalt::Config`,
  `liquid::ParserBuilder`, `Template`, `Object`/`Value`, and the
  `ObjectView`/`ValueView` traits.
---

# Cobalt Static Site Generator Skill

## Overview

This skill gives you the distilled, opinionated workflow for **Cobalt** — the
Rust static site generator — and the **Liquid** template language it runs on.
It reconciles the official Cobalt user guide, the `cobalt.rs` repository
conventions, the `cobalt-config` schema, and the Rust `liquid` crate API into
a single guide (`01-cobalt-static-site-generation.md`) of 32 numbered patterns
(`CB-01`…`CB-32`), each with a strength indicator (MUST / SHOULD / CONSIDER /
AVOID), a short summary, paired Bad/Good examples, a rationale, and
cross-references. The guide is backed by a corpus of **80 single-concept
cards** in `concept-cards/cobalt/` that cover every tag, filter, config field,
CLI subcommand, and Rust API surface in finer-grained detail.

The target environment is **Cobalt 0.19+** (built on `cobalt-config` and the
`liquid` crate family at their 0.26+ / 0.26+ / 2.0-track versions). The
default toolchain assumes **`cobalt-bin`** installed via `cargo install
cobalt-bin`, a **Rust 1.70+** toolchain if you extend Cobalt programmatically,
and **Liquid templates** authored against the Shopify-style standard library
exposed through `ParserBuilder::with_stdlib()`.

## When to Use This Skill

Activate this skill when the task involves:

- **Installing or upgrading Cobalt** — `cargo install cobalt-bin`, Homebrew,
  or the upstream `gh-install` script
- **Scaffolding a site** — `cobalt init`, laying out `_layouts/`, `_includes/`,
  `_data/`, `_sass/`, `_defaults/`, and `posts/`
- **Authoring content** — pages vs. posts, frontmatter, Markdown body,
  draft/publish workflow, `cobalt new` and `cobalt publish`
- **Writing Liquid templates** — `{{ }}` output, `{% %}` logic, filters,
  for/if/unless/case, `assign`/`capture`, `include`, `layout`
- **Designing layouts and partials** — layout chaining, `{{ page.content }}`,
  includes, data-file-driven navigation
- **Configuring the site** — `_cobalt.yml`, posts options, permalink
  templates, RSS, pagination, site variables, source/destination paths,
  syntax highlighting, Sass, minification
- **Debugging a build** — `cobalt debug files`, `cobalt debug highlight`,
  explaining why a file was excluded, why a permalink resolved a particular
  way, or why a template variable is empty
- **Deploying** — GitHub Pages, GitLab CI, self-hosted static hosting
- **Extending Cobalt in Rust** — `cobalt::Config`, `cobalt::build()`,
  `liquid::ParserBuilder`, `Template`, `Object`/`Value`, `ObjectView` /
  `ValueView`, custom filters and tags
- **Reviewing or refactoring a Cobalt site** — auditing for the anti-patterns
  in `CB-32`, validating permalink hygiene, checking draft/publish state,
  verifying pipeline assumptions

If the task is purely Rust-ecosystem code (no Cobalt, no Liquid, no static
site), prefer the `rust-guidelines` skill instead. The two are complementary
— when you extend Cobalt programmatically, load both.

## Document Locations

This skill ships a single authoritative guide plus a rich concept-card
library:

**Guide (1):**

- `knowledge/cobalt/guides/01-cobalt-static-site-generation.md` — the 32
  numbered patterns (`CB-01`…`CB-32`) covering the full Cobalt + Liquid
  workflow from install to programmatic extension, ending with a Summary
  Table and a Related Guidelines / External References footer.

**Supporting material:**

- `knowledge/cobalt/concept-cards/cobalt/` — **80 single-concept cards**
  covering every Liquid tag, filter, object, and every Cobalt CLI command,
  config field, and Rust API surface. Each card is YAML-frontmattered with
  source, authors, aliases, typed relationships, and competency questions.
- `knowledge/cobalt/extraction-metadata/cobalt/` — provenance and
  meta-documents: `competency-questions.md`, `domain-taxonomy.md`,
  `extraction-log.md`, `notation-conventions.md`.
- `knowledge/cobalt/sources/md/cobalt-docs/` — the upstream Cobalt
  documentation in markdown.
- `knowledge/cobalt/sources/html/cobalt/` — the upstream Cobalt site
  snapshot.
- `knowledge/cobalt/sources/html/liquid*/` — rustdoc for the
  `liquid`, `liquid_core`, `liquid_lib`, `liquid_derive`, `liquid_bin`, and
  `liquid_help_md` crates. Use these when you need exact type signatures,
  trait bounds, or filter semantics.

The guide is the normative artefact. The concept cards are the fastest way to
look up a single tag, filter, CLI subcommand, or config field without
loading the whole guide; the rustdoc sources are the ground truth for the
Rust API surface when extending Cobalt programmatically.

## Document Selection Guide

Cobalt is a single-guide skill, so loading is mostly concept-card-driven.
Anchor to `CB-32` (common pitfalls) on any task — it is the cheap safety net.

| Task | Load These |
|------|------------|
| **Any Cobalt task** | `01-cobalt-static-site-generation.md` (start with Summary Table + `CB-32`) |
| **Install / first-site scaffolding** | `CB-01`…`CB-05` + `concept-cards/cobalt/installation.md`, `cobalt-init.md`, `directory-structure.md` |
| **Authoring pages / posts** | `CB-06`…`CB-09` + `concept-cards/cobalt/{page,post,frontmatter,permalink-templates,pretty-urls}.md` |
| **Liquid templating** | `CB-10`…`CB-18` + `concept-cards/cobalt/{liquid-template-language,output-tags,logic-tags,string-filters,array-filters,for-block,if-block,unless-block,case-block,assign-tag,capture-block,include}.md` |
| **Layouts and includes** | `CB-12`, `CB-13` + `concept-cards/cobalt/{layout,layouts-directory,layout-field,includes-directory,include}.md` |
| **Site configuration** | `CB-19` + `concept-cards/cobalt/{cobalt-configuration-file,site-options,source-directory,destination-directory,build-options}.md` |
| **RSS feeds** | `CB-20` + `concept-cards/cobalt/rss-feed.md` |
| **Pagination** | `CB-23` + `concept-cards/cobalt/{pagination,pagination-include-types,paginator-variable}.md` |
| **Syntax highlighting / Sass** | `CB-22`, `CB-24` + `concept-cards/cobalt/{syntax-highlighting,sass-scss-support}.md` |
| **Debugging a build** | `CB-25` + `concept-cards/cobalt/cobalt-debug.md`, then `CB-32` |
| **Deployment** | `CB-26` + `concept-cards/cobalt/{deployment-github-pages,deployment-gitlab-ci,self-hosted-deployment}.md` |
| **Programmatic / Rust extension** | `CB-27`…`CB-31` + `concept-cards/cobalt/{cobalt-config-struct,liquid-parser,liquid-template-object,liquid-value-system,objectview-valueview-traits}.md` + relevant rustdoc under `sources/html/liquid*/` |
| **Refactoring / audit** | `CB-32` first, then topic-specific patterns |

## Workflow

### For Scaffolding a New Site

1. **Install**: `cargo install cobalt-bin` (`CB-01`). The crate on crates.io is
   `cobalt-bin`; the binary is `cobalt`.
2. **Init**: `cobalt init` in an empty directory (`CB-02`) — scaffolds
   `_cobalt.yml`, `_layouts/`, `_includes/`, `_defaults/`, `posts/`,
   `index.liquid`.
3. **Understand the convention**: underscore-prefixed directories are
   generation resources (not copied to output). `posts/` has **no**
   underscore — this differs from Jekyll (`CB-03`, `CB-32`).
4. **Iterate**: `cobalt serve` for live-reload local dev; `cobalt build` for
   production output to `_site/` (`CB-04`).
5. **Add your first post**: `cobalt new --kind post "My First Post"` (`CB-05`)
   — generates slug + frontmatter from `_defaults/posts.md`.

### For Authoring Content

1. **Decide page vs. post**: posts live in `posts/`, get `published_date`,
   appear in `collection.posts`, support draft/publish (`CB-06`).
2. **Frontmatter discipline**: YAML between `---` delimiters at the top of
   the file; close the block (`CB-08`, `CB-32`). Frontmatter keys you rely on
   most often: `title`, `description`, `permalink`, `layout`, `published_date`,
   `is_draft`, `tags`, `categories`, `excerpt`.
3. **Draft workflow**: posts start with `is_draft: true` (per defaults); use
   `cobalt publish posts/my-post.md` to flip it and stamp `published_date`
   (`CB-07`).
4. **Permalinks**: set a site-wide default in `_cobalt.yml`; override per
   page with `permalink:` in frontmatter. Omit the extension for pretty URLs;
   must start with `/` (`CB-09`).
5. **Know the pipeline**: Liquid runs *first*, then Markdown, then layout,
   then write to `_site/` (`CB-10`). Liquid cannot read the rendered HTML;
   Markdown cannot emit Liquid expressions.

### For Writing Liquid Templates

1. **Two delimiter families**: `{{ expr }}` prints a value; `{% tag %}`
   executes logic. They are not interchangeable (`CB-11`).
2. **Three globals**: `site`, `page`, `collection`. Dot-notation for access
   (`{{ page.title }}`, `{{ site.base_url }}`) (`CB-14`).
3. **Iteration**: `{% for post in collection.posts %}…{% endfor %}` —
   `forloop.first`, `forloop.last`, `forloop.index` are available inside
   (`CB-15`).
4. **Control flow**: `if`/`unless`/`elsif`/`else`/`endif`, `case`/`when`
   (`CB-16`). Liquid's truthiness: only `false` and `nil` are falsy.
5. **Filters**: `|` pipes a value through a transformation.
   `{{ page.title | upcase }}`, `{{ post.published_date | date: "%Y-%m-%d" }}`,
   `{{ body | strip_html | truncate: 160 }}` (`CB-17`).
6. **Local variables**: `{% assign x = … %}` for single values; `{% capture
   x %}…{% endcapture %}` when you need to build a string from multiple
   pieces (`CB-18`).
7. **Layouts**: every layout must render `{{ page.content }}` somewhere
   (`CB-12`). `{{ page.content }}` is **empty inside page bodies** — it only
   exists in layouts (`CB-32`).
8. **Includes**: `{% include "header.liquid" %}` for reusable partials;
   variables propagate into the include (`CB-13`).

### For Configuring the Site

1. **`_cobalt.yml` is optional** — every setting has a sensible default
   (`CB-19`). Add it when you need to override.
2. **Minimum viable config** fields to know: `source`, `destination`,
   `site.title`, `site.base_url`, `posts.permalink`, `posts.rss`,
   `syntax_highlight.enabled`, `sass`.
3. **RSS**: four mandatory fields for a valid 2.0 feed — `posts.rss.path`,
   `site.title`, `site.description`, `site.base_url` (`CB-20`).
4. **Pagination**: configure on the *collection* (`posts.pagination.per_page`),
   then paginate-iterate in the template via `paginator.pages` (`CB-23`).
5. **Data files**: drop YAML/JSON/TOML into `_data/`; read from templates as
   `{{ site.data.filename.key }}` (`CB-21`).

### For Debugging

1. **Load `CB-25` + `CB-32`**.
2. **Why was a file excluded?** `cobalt debug files --trace` reports every
   file considered and the rule that dropped it.
3. **Why did a permalink resolve that way?** Inspect with `cobalt debug
   files`; cross-check against `CB-09` (permalink must start with `/`).
4. **Why is `page.content` empty?** Because the template renders in a page
   body, not a layout (`CB-32`).
5. **Which syntax-highlight themes are available?** `cobalt debug highlight
   themes` / `cobalt debug highlight syntaxes`.
6. **Why did Liquid swallow my Markdown?** The pipeline order is Liquid →
   Markdown (`CB-10`). Markdown cannot produce Liquid expressions; if you
   need Liquid output to be rendered as Markdown-styled HTML, emit Markdown
   from the Liquid itself.

### For Deployment

1. **GitHub Pages**: `cobalt build --destination ./docs` + commit the
   output, or wire a GitHub Actions workflow that runs `cobalt build` and
   publishes `_site/` to the `gh-pages` branch (`CB-26`).
2. **GitLab CI**: use the `cobalt-org/cobalt-gitlab` template or a bare
   `cobalt build` job that uploads `_site/` as a `pages` artifact.
3. **Self-hosted**: `cobalt build` → rsync/upload `_site/` to any static
   host (S3 + CloudFront, Netlify, Nginx, Caddy).

### For Extending Cobalt in Rust

1. **Load `CB-27`…`CB-31`** plus the rustdoc under `sources/html/liquid*/`.
2. **Parse templates**: `liquid::ParserBuilder::with_stdlib().build()?`
   (`CB-27`) — always call `.with_stdlib()` or you lose every standard tag
   and filter.
3. **Render**: `parser.parse(template_src)?.render(&globals)?`, where
   `globals: &dyn ObjectView` (`CB-28`).
4. **Build the data model**: `liquid::object!({ "page": …, "site": … })` or
   `Object::new()` + `insert` (`CB-29`). Every terminal value is a
   `liquid::model::Value`.
5. **Zero-copy rendering for large data**: implement `ObjectView` and
   `ValueView` on your own types instead of cloning into `Object`/`Value`
   (`CB-30`).
6. **Programmatic builds**: `cobalt::Config::from_config(yaml)` then
   `cobalt::build(config)` (`CB-31`). Use `from_config` — constructing
   `Config` directly skips default resolution logic.
7. **Custom filters/tags**: implement `liquid_core::Filter` or
   `liquid_core::ParseTag`; register via
   `ParserBuilder::filter(MyFilter::new())` / `.tag(MyTag)`.

### For Refactoring / Audit

1. **Walk `CB-32`** on every file. The four evergreen regressions:
   - `_posts/` instead of `posts/`
   - `page.content` in a page body rather than a layout
   - Missing closing `---` on frontmatter
   - Building without publishing drafts
2. **Walk the permalink policy** — every permalink starts with `/`, omits
   the file extension, and resolves to a unique URL (`CB-09`).
3. **Walk the layout chain** — every layout renders `{{ page.content }}`
   exactly once (`CB-12`).
4. **Reference pattern IDs** in commit messages:
   `fix(posts): publish draft before build (CB-07, CB-32)`.

## Critical Rules (Always Apply)

These rules hold for every Cobalt + Liquid project without needing to load
the full guide.

### Directory Convention (Underscore Discipline)

```yaml
# Bad — Jekyll-style _posts directory
_posts/
  my-post.md

# Good — Cobalt uses posts/ (no underscore)
posts/
  my-post.md

# Generation resources all live under _-prefixed dirs (not copied to output)
_layouts/  _includes/  _data/  _sass/  _defaults/
```

### Frontmatter Discipline

```markdown
<!-- Bad — missing closing delimiter; YAML swallows the body -->
---
title: Broken
body goes here but is parsed as YAML

<!-- Good — paired --- delimiters, YAML inside, Markdown below -->
---
title: My Page
description: A short summary
permalink: /pages/my-page/
---
Markdown body starts here. {{ page.title }} still works because Liquid runs
before Markdown.
```

### Processing Pipeline (Order Matters)

```
source.md  →  Liquid  →  Markdown  →  Layout  →  _site/output.html
            (1st)       (2nd)       (3rd)         (4th)
```

```markdown
<!-- Good — Liquid output becomes Markdown input -->
{{ "**bold from Liquid**" }}   <!-- Liquid emits **bold**, Markdown renders it -->

<!-- Bad — Markdown cannot feed Liquid; Liquid is already done -->
Some **{{ missing_var }}**     <!-- `{{ missing_var }}` expands to "",
                                    not to a Liquid expression you can then
                                    post-process -->
```

### Liquid Delimiters Are Not Interchangeable

```liquid
{# Bad — {% %} prints nothing #}
{% page.title %}

{# Bad — {{ }} cannot drive control flow #}
{{ if page.published }}yes{{ endif }}

{# Good — {{ }} outputs, {% %} executes #}
{{ page.title }}
{% if page.published %}yes{% endif %}
```

### Layouts Must Render `{{ page.content }}`

```liquid
{# Bad — layout forgets to render the page body #}
<!doctype html><html><body>
  <h1>{{ page.title }}</h1>
  {# page.content missing — every page renders with only the title #}
</body></html>

{# Good — the layout's one mandatory job is {{ page.content }} #}
<!doctype html><html><body>
  <h1>{{ page.title }}</h1>
  {{ page.content }}
</body></html>
```

### Permalinks

```yaml
# Bad — missing leading slash; no extension-free pretty URL
permalink: pages/my-page.html

# Good — starts with /, omits extension for pretty URL
permalink: /pages/my-page/
```

### Draft / Publish

```console
# Bad — build before publishing; drafts silently excluded from output
$ cobalt build

# Good — publish then build
$ cobalt publish posts/my-draft.md
$ cobalt build
```

### Liquid Parser (Rust Extension)

```rust
// Bad — no stdlib; losing every standard tag and filter
let parser = liquid::ParserBuilder::new().build()?;

// Good — stdlib first, then custom additions
let parser = liquid::ParserBuilder::with_stdlib()
    .filter(MyFilter::new())
    .tag(MyTag)
    .build()?;

// Programmatic build — use from_config, not direct field assignment
let yaml = std::fs::read_to_string("_cobalt.yml")?;
let raw: cobalt_config::Config = serde_yaml::from_str(&yaml)?;
let config = cobalt::Config::from_config(raw)?;
cobalt::build(config)?;
```

## Pattern ID Reference

The guide uses a single prefix: every pattern is `CB-NN`.

| Prefix | Guide |
|--------|-------|
| `CB-NN` | `01-cobalt-static-site-generation.md` |

Patterns grouped by topic:

| Group | IDs | Theme |
|-------|-----|-------|
| **Install & scaffolding** | CB-01 … CB-05 | install, init, directory layout, build/serve, `cobalt new` |
| **Content model** | CB-06 … CB-09 | pages vs. posts, draft/publish, frontmatter, permalinks |
| **Processing** | CB-10 … CB-11 | pipeline order, Liquid syntax |
| **Templating** | CB-12 … CB-18 | layouts, includes, variables, for, control flow, filters, assign/capture |
| **Configuration** | CB-19 … CB-24 | `_cobalt.yml`, RSS, data files, highlighting, pagination, Sass |
| **Debugging & deployment** | CB-25 … CB-26 | `cobalt debug`, GitHub Pages |
| **Rust / programmatic extension** | CB-27 … CB-31 | `ParserBuilder`, `Template`, value system, `ObjectView`/`ValueView`, `cobalt::Config` |
| **Anti-patterns** | CB-32 | common pitfalls (summary of the most frequent regressions) |

## Strength Indicators

The guide uses a 4-level scale. `MUST` and `AVOID` are bright lines; `SHOULD`
is a strong convention; `CONSIDER` is context-dependent.

| Indicator | Meaning | Action |
|-----------|---------|--------|
| **MUST** | Required for correctness or interop | Always follow |
| **SHOULD** | Strong convention | Follow unless specific reason not to |
| **CONSIDER** | Context-dependent recommendation | Evaluate case by case |
| **AVOID** | Anti-pattern; listed thing is forbidden | Never write this |

## Example Usage

### Task: "Scaffold a blog and publish a first post"

1. Load: `01-cobalt-static-site-generation.md` (Summary Table), `CB-01`…
   `CB-09`, `CB-32`.
2. Apply:
   - **CB-01** `cargo install cobalt-bin` (not `cobalt`).
   - **CB-02** `cobalt init my-blog && cd my-blog`.
   - **CB-03** Recognise `_layouts/`, `_includes/`, `posts/`; do **not**
     rename `posts/` to `_posts/` (CB-32).
   - **CB-05** `cobalt new --kind post "Hello, world"` — generates
     `posts/hello-world.md` with `is_draft: true`.
   - **CB-07** Edit content, then `cobalt publish posts/hello-world.md` to
     stamp `published_date` and flip `is_draft`.
   - **CB-09** Verify the permalink in frontmatter or `_cobalt.yml` starts
     with `/` and omits the extension.
   - **CB-04** `cobalt serve` to iterate locally; `cobalt build` for
     production.

### Task: "Design a post layout with a date, tags, and an excerpt list on the index"

1. Load: `CB-10`…`CB-17`, concept cards `layout`, `include`,
   `for-block`, `date-filter`, `excerpt`.
2. Apply:
   - **CB-12** `_layouts/post.liquid` renders `{{ page.content }}` once,
     with `{{ page.title }}` and `{{ page.published_date | date: "%B %-d,
     %Y" }}` in the header.
   - **CB-13** Extract the header into `_includes/post-header.liquid`.
   - **CB-15** On `index.liquid`, iterate `collection.posts` and print
     `{{ post.title }}` + `{{ post.excerpt }}`.
   - **CB-17** Use `| date`, `| strip_html`, `| truncate: 200` to shape
     the excerpt.

### Task: "Set up RSS and pagination for the post archive"

1. Load: `CB-19`, `CB-20`, `CB-23`, concept cards `rss-feed`, `pagination`,
   `paginator-variable`.
2. Apply:
   - **CB-19** Add `site.title`, `site.description`, `site.base_url` to
     `_cobalt.yml`.
   - **CB-20** Add `posts.rss.path: /rss.xml` and ensure the four
     mandatory fields are populated.
   - **CB-23** Add `posts.pagination.per_page: 10` and iterate
     `paginator.pages` on the archive template; use
     `paginator.previous_link` / `paginator.next_link` for nav.

### Task: "Debug why a post is not appearing in the build output"

1. Load: `CB-25`, `CB-32`, concept card `cobalt-debug`.
2. Check (in order):
   - **CB-32** Is the file under `posts/` (not `_posts/`)?
   - **CB-32** Is frontmatter closed with a trailing `---`?
   - **CB-07** Is `is_draft: true`? Did you `cobalt publish`?
   - **CB-25** Run `cobalt debug files --trace path/to/post.md` to see the
     inclusion/exclusion trace.
   - **CB-09** Is the permalink malformed (missing leading `/`)?

### Task: "Deploy the site to GitHub Pages from a `main`-branch project"

1. Load: `CB-26`, concept card `deployment-github-pages`.
2. Apply:
   - **CB-26** Add a `.github/workflows/pages.yml` job: `cargo install
     cobalt-bin` → `cobalt build` → `actions/upload-pages-artifact` →
     `actions/deploy-pages`.
   - **CB-19** Set `site.base_url` in `_cobalt.yml` to the Pages URL
     (`https://<user>.github.io/<repo>`) so absolute links resolve.
   - Verify locally with `cobalt build --destination ./_site` and smoke-test
     the HTML before pushing.

### Task: "Render a Liquid template programmatically from Rust"

1. Load: `CB-27`…`CB-30`, concept cards `liquid-parser`,
   `liquid-template-object`, `liquid-value-system`,
   `objectview-valueview-traits`.
2. Apply:
   - **CB-27** `let parser = liquid::ParserBuilder::with_stdlib().build()?;`
   - **CB-28** `let tpl = parser.parse("Hello, {{ name }}!")?;`
   - **CB-29** `let globals = liquid::object!({ "name": "world" });`
   - **CB-28** `let out = tpl.render(&globals)?;` → `"Hello, world!"`.
   - **CB-30** If `globals` is built from a large, owned Rust data model
     that you'd rather not clone into `Object`/`Value`, implement
     `ObjectView`/`ValueView` on your model directly.

### Task: "Extend a programmatic build with a custom Liquid filter"

1. Load: `CB-27`, `CB-31`, concept cards `liquid-parser`,
   `cobalt-config-struct`; skim `sources/html/liquid_core/filter/` rustdoc.
2. Apply:
   - Implement `liquid_core::Filter` on a unit struct (`derive
     FilterReflection`, `derive ParseFilter`).
   - Register via `ParserBuilder::with_stdlib().filter(MyFilter)`.
   - Wire into a programmatic build: construct the parser, hand it to
     `cobalt::Config` (or use it standalone for non-Cobalt Liquid
     rendering).
   - **CB-31** If embedding in a full build, load YAML config, round-trip
     through `cobalt::Config::from_config`, then `cobalt::build(config)`.

### Task: "Refactor an aging Cobalt site for 0.19+"

1. Load: `CB-32` first, then topic-specific patterns for each regression
   you spot.
2. Apply the `CB-32` walk:
   - Rename `_posts/` to `posts/` (CB-03).
   - Move any `{{ page.content }}` uses out of page bodies and into
     `_layouts/` (CB-12).
   - Audit frontmatter delimiters — every `---` pairs (CB-08).
   - Normalise permalinks to start with `/` and omit the extension (CB-09).
   - Replace any `cobalt build` in CI that runs before `cobalt publish` on
     staged drafts (CB-07).

## Integration Notes

- **Code blocks** use the appropriate language tag: `liquid` for templates,
  `yaml` for `_cobalt.yml` and frontmatter, `console` for CLI sessions,
  `rust` for programmatic extension, and a bare block for directory trees.
- **Pattern IDs are `CB-NN`** with stable numbering (32 patterns). Re-runs
  of the extractor preserve the lower number on merges.
- **Cross-references** inside the guide use `**See also**: CB-08, CB-12`.
- **Liquid is the template language, not Cobalt's.** If you only need
  Liquid templating in a non-Cobalt context, the `CB-27`…`CB-30` patterns
  and the `liquid*` concept cards apply standalone — skip the Cobalt
  CLI/config patterns.
- **Cobalt-specific vs. Liquid-generic patterns**: CB-01…CB-09, CB-19…CB-26
  are Cobalt-specific. CB-11…CB-18, CB-27…CB-30 are generic Liquid. CB-10
  is the seam between them.
- **Concept cards** are the fastest entry point for a single-question
  lookup ("what does the `date` filter do?", "what fields does
  `_cobalt.yml` accept?"). Each card has a `concept:` frontmatter field,
  aliases, typed relationships (`prerequisites`, `extends`, `related`,
  `contrasts_with`), and competency questions.
- **rustdoc under `sources/html/liquid*/`** is the ground truth for the
  Rust API — use it before guessing a method signature.

## Quick Reference for Common Tasks

| I want to… | Read this |
|------------|-----------|
| Install Cobalt | `CB-01` |
| Scaffold a new site | `CB-02`, `CB-03` |
| Create a new page or post | `CB-05`, `CB-06` |
| Publish a draft | `CB-07` |
| Write correct frontmatter | `CB-08` |
| Set up pretty URLs | `CB-09` |
| Understand why Liquid runs before Markdown | `CB-10` |
| Write a layout | `CB-12` |
| Share a header/footer across pages | `CB-13` |
| Iterate posts in a template | `CB-15` |
| Use filters to format dates/strings | `CB-17` |
| Configure the site globally | `CB-19` |
| Emit an RSS feed | `CB-20` |
| Paginate the archive | `CB-23` |
| Enable syntax highlighting or Sass | `CB-22`, `CB-24` |
| Debug a missing or miscategorised file | `CB-25` + `CB-32` |
| Deploy to GitHub Pages | `CB-26` |
| Render a Liquid template from Rust | `CB-27`, `CB-28`, `CB-29` |
| Avoid cloning a big data model into `Object` | `CB-30` |
| Trigger a full Cobalt build from Rust | `CB-31` |
| Walk the most common pitfalls | `CB-32` |

## Related Skills

- **`rust-guidelines`** — load alongside this skill whenever you extend
  Cobalt or Liquid programmatically in Rust (custom filters, custom tags,
  full Rust-driven builds). In particular `01-core-idioms`, `02-api-design`,
  `03-error-handling`, and `12-project-structure` cover the Rust-side
  discipline.
- **`js-guidelines`** and **`go-guidelines`** — unrelated; load only when
  the task crosses ecosystems (e.g. a hybrid site with a JS-built widget
  consumed by Cobalt).

## External References

- [Cobalt Documentation](https://cobalt-org.github.io/) — official site
- [Cobalt GitHub Repository](https://github.com/cobalt-org/cobalt.rs)
- [`cobalt-bin` on crates.io](https://crates.io/crates/cobalt-bin)
- [`liquid` on crates.io](https://crates.io/crates/liquid)
- [Liquid Template Language Reference (Shopify)](https://shopify.github.io/liquid/)
