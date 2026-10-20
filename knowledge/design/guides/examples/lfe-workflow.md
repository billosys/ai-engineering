# Optional case: an LFE homepage direction

This project-specific example applies the [brief-to-design workflow](../design-workflow.md)
to the Lisp Flavoured Erlang homepage. It is optional teaching material, not a
default layout, colour preset, token system or dependency for other design
work. The package contains this case but does not contain a copy of the LFE
site or its data.

## Source and limits

The read-only site context was pinned to commit
`036e231b09c48966da26d2227bccb4fa3b295df9` in the isolated LFE worktree
`codex/design-practice-arc01`. The inspected source includes `_cobalt.yml`,
`src/index.md`, `src/about.md`, the home/page/post layouts, `src/_includes/nav.liquid`,
`src/_includes/css.liquid`, the home partials and data, `src/_data/site.yml`,
and `tailwind/site.css` lines 1–175. A pre-existing dirty generated
`src/css/site.css` was excluded from the pinned-source claims. No site change,
build, browser inspection, contrast measurement or user study is represented
here.

The site already supplies its gold header wordmark
(`/images/logo_developer@2x.png`), a masthead mark
(`/images/LFE-logo-abbr-6.2.png`) and alien/Lisp mascot imagery including
`/images/lisplogo-alien-tech-grey.png`. Its local type assets include
Newsreader variable and italic faces with a system fallback elsewhere. These
assets and the LFE name remain part of either direction; this example does not
turn them into defaults for another project.

## A brief from the existing page

| Field | LFE-specific reading |
|---|---|
| Task | Give a visitor a clear first route into LFE, show enough of the language to make its character concrete, and let an existing practitioner find learning, use and download routes. |
| Directly observed | The home layout orders a masthead with selectable code excerpts and a Learn More link, then feature cards, “Build It with LFE”, books, videos, and closing Discord/xkcd callouts. The nav has Learn, Use, Community, About, Blog and a Download menu, plus GitHub, Mastodon and light/dark controls. The home data names excerpts REPL, Simple Types, Compound Types, Records, Functions, Macros, Erlang Interop and OTP. The nav links to `/learn/`; the masthead data supplies `/learn` for its Learn More link, so confirm both resolve as intended before changing route presentation. These are source observations, not evidence of visitor preferences. |
| Content and identity | Keep the supplied gold wordmark, masthead mark and alien mascot imagery, code examples, feature/build/book/video content, existing labels and destinations. The home source points to `/learn/`, `/use/`, `/community/`, `/about/` and `/blog/`; download URLs are formed from the repository and release values in `src/_data/site.yml`. |
| Assumed tasks | A newcomer may want to understand what LFE is and where to start; a practitioner may need a current release or a path to the reference material; a reader may want to read an article and return to its topic. These are planning assumptions inferred from the source, not researched user needs. |
| Constraints | Work with the existing Cobalt Liquid layouts/includes, content, navigation, URLs, supplied identity and light/dark mechanism. Preserve working content and do not assume this slice changes the site. |
| Priorities | First clarify the language and provide a direct learning or use route; keep current downloads findable; retain routes into deeper editorial and community material. |
| Planned observations | Walk the page at narrow and wide widths: identify what LFE is, find Learn and Use, find the current download label, and locate a route to longer reading. Check tab and menu operation with keyboard and confirm the current item is understandable without colour alone. These are planned checks; no result has been collected. |
| Credible failures | A dense opening delays the first route; code tabs obscure that examples can be selected; the Download menu blends with navigation; editorial material is visually undifferentiated from quick-start actions; a state relies on colour alone. |
| Unknown and next check | Which route matters most to actual newcomers and practitioners, and which visual differences help them? Do both Learn URLs resolve to the intended destination? Next, inspect a prototype using those stated tasks, verify the routes, and ask site maintainers or intended readers to try it. Do not fill the gap with analytics or participant claims that were not supplied. |

## Two directions against the same brief

Both concepts keep the supplied gold wordmark and alien mascot imagery,
Newsreader/system type assets, current content, labels, URLs, code and
light/dark capability. They differ in what the homepage asks a visitor to
notice first and how it groups the same material.

### Language Workbench

Lead with the supplied LFE mark and a concise explanation, then keep the code
excerpt tabs and the Learn More route together as the first working area. Place
Learn, Use and Download near that opening; group the existing feature cards and
“Build It with LFE” paths next, with books and videos as deeper resources and
community callouts after them. The rhythm moves from a short orientation into
code and action, then into larger resource groups. The code and route hierarchy
make the language and its next action the first focus; the trade-off is that
books and community material sit farther down the page.

### Community Journal

Lead with the LFE story and a quieter editorial reading column, then give a
featured article or selected long-form piece the largest uninterrupted block.
Arrange books, videos and community material as related reading and listening
collections, with a compact Learn/Use/Download rail kept visible as a return
route. The rhythm is longer and more continuous, with less card-by-card
interruption. It gives editorial context more attention; the trade-off is that
the code examples and quick-start routes become secondary to reading.

Neither direction changes the supplied identity. The choice is about ordering,
grouping and reading rhythm, not replacing the LFE brand with a new visual
theme.

## Provisional choice and critique

Choose **Language Workbench** for the current homepage task. The actual source
already opens with selectable code excerpts, a concise language explanation
and a Learn More route, and its nav exposes Learn, Use and versioned downloads.
This direction extends that existing code-first structure and makes its next
actions legible while preserving the editorial resources below. It is a
source-based design proposal, not a tested visitor preference or an implemented
homepage. Retain the Community Journal's quieter treatment for the article
reading path, where continuous text and context can take priority.

One concrete critique is visible in the live style source. The root defines a
gold primitive ramp (`--gold-50` through `--gold-950`) and assigns some values
to `.nav-active`, `.nav-hover-gold`, `.tab-gold`, `.cta-gold` and
`.download-dev`. At the same time, the live Tailwind source uses scattered
slate/gray utilities for navigation, surfaces, text, borders and focus
offsets. Pagefind has a separate variable adapter: focus/outline/mark roles
appear at root, while dark-mode text, background, border, hover and skeleton
values are set in `.dark`. Naming a gold role does not establish that its
rendered pair works, and the Pagefind properties need to be considered with
their actual component surfaces. The legacy Sass noted in this project is not
the live token authority; follow the loaded Tailwind stylesheet and the
Pagefind include path when checking consumption.

The proposal is to review these role questions in the next token-focused work,
not to claim that new values have already been selected:

| Role to inspect | Existing consumers or questions |
|---|---|
| Page and raised surfaces | Which page, card, code-example, dropdown and search-result backgrounds occur in each mode? How do slate utility backgrounds layer or gradient? |
| Primary and secondary text | Which body, nav, heading, metadata and muted text utilities are used on each resolved surface? |
| Links and current location | How do ordinary links, `.nav-active`, hover and visited states differ when colour is removed? |
| Actions and selection | What foreground/background pairs and focus states do `.cta-gold`, `.tab-gold` and the three Download choices use? |
| Boundaries and keyboard focus | Which borders, separators, focus rings and offsets remain visible beside their real background? |
| Search and status | Which Pagefind input, result, selected, mark, skeleton and focus roles are present? Which warning/status colours must preserve meaning beyond hue? |

Before revision, enumerate the live Tailwind utilities, custom gold classes and
Pagefind variables consumed by the header, masthead tabs/CTA, downloads,
content cards and search UI. Capture each actual foreground, resolved
background and relevant normal, hover, focus, selected or inactive state in
light and dark modes. After a proposed role mapping, repeat that same consumer
walk, inspect computed styles and test the same interactions. Check applicable
text and non-text contrast separately, labels that do not depend on colour,
keyboard focus, and any alpha, gradient or overlay compositing. Record failed
and unrun pairs. A source value or a successful site build alone cannot stand
in for those rendered checks.

The next concrete check is to implement and build the approved role changes in
the isolated site worktree, then compare the homepage, an ordinary page, a blog
article and Pagefind in both modes against this consumer list. That work is
outside this example's evidence: the values, implementation, build, rendered
states and downstream repairs remain unverified here.
