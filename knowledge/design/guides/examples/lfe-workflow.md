# Optional case: an LFE homepage direction

This project-specific example applies the [brief-to-design workflow](../design-workflow.md)
to the Lisp Flavoured Erlang homepage. It is optional teaching material, not a
default layout, colour preset, token system or dependency for other design
work. The package contains this case but does not contain a copy of the LFE
site or its data.

## Source and limits

The baseline site context was pinned to commit
`036e231b09c48966da26d2227bccb4fa3b295df9` in the isolated LFE worktree
`codex/design-practice-arc01`. The inspected source includes `_cobalt.yml`,
`src/index.md`, `src/about.md`, the home/page/post layouts, `src/_includes/nav.liquid`,
`src/_includes/css.liquid`, the home partials and data, `src/_data/site.yml`,
and `tailwind/site.css` lines 1–175. A pre-existing dirty generated
`src/css/site.css` was excluded from those baseline-source claims. The later
local implementation is separately pinned at
`1a64666cd7273ee97380bff163ed7642d13356df` on
`codex/design-practice-arc01`; it is not published and the package contains no
copy of the LFE site or its data. Browser observations below are attributed to
CDC. No user study or visitor preference is represented.

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
| Directly observed | The home layout orders a masthead with selectable code excerpts and a Learn More link, then feature cards, “Build It with LFE”, books, videos, and closing Discord/xkcd callouts. The nav has Learn, Use, Community, About, Blog and a Download menu, plus GitHub, Mastodon and light/dark controls. The home data names excerpts REPL, Simple Types, Compound Types, Records, Functions, Macros, Erlang Interop and OTP. The nav links to `/learn/`; the masthead data supplies `/learn`. CDC later checked both routes and reports that they reach the same Learn page. These are source observations and a bounded local check, not evidence of visitor preferences. |
| Content and identity | Keep the supplied gold wordmark, masthead mark and alien mascot imagery, code examples, feature/build/book/video content, existing labels and destinations. The home source points to `/learn/`, `/use/`, `/community/`, `/about/` and `/blog/`; download URLs are formed from the repository and release values in `src/_data/site.yml`. |
| Assumed tasks | A newcomer may want to understand what LFE is and where to start; a practitioner may need a current release or a path to the reference material; a reader may want to read an article and return to its topic. These are planning assumptions inferred from the source, not researched user needs. |
| Constraints | Work with the existing Cobalt Liquid layouts/includes, content, navigation, URLs, supplied identity and light/dark mechanism. Preserve the supplied material and treat revisions as local until separately reviewed and integrated. |
| Priorities | First clarify the language and provide a direct learning or use route; keep current downloads findable; retain routes into deeper editorial and community material. |
| Planned and checked tasks | CDC later checked Learn and Use, the current download, code tabs, mobile navigation, search-to-article-to-topic return, and reading at narrow and wide sizes. Actual revision observations and adaptation limits are recorded below; they are not participant findings. |
| Credible failures | A dense opening delays the first route; code tabs obscure that examples can be selected; the Download menu blends with navigation; editorial material is visually undifferentiated from quick-start actions; a state relies on colour alone. |
| Unknown and next check | The local check confirmed that Learn More `/learn` and header `/learn/` reach the same Learn page, and that Use resolves. Which route matters most to actual newcomers and practitioners, and which visual differences help them, remain unknown without research with those audiences. |

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
actions legible while preserving the editorial resources below. It began as a
source-based proposal, not a tested visitor preference; the isolated revision
and its actual review are recorded below. Retain the Community Journal's quieter
treatment for the article reading path, where continuous text and context can
take priority.

The earlier token critique is visible in the live style source. The root defines a
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

These role questions framed the earlier token-focused work. Arc01 Slice02 owns
its separate measured-pair evidence and verification; this example does not
repeat those measurements or treat a screenshot as a pixel-level colour test.

| Role to inspect | Existing consumers or questions |
|---|---|
| Page and raised surfaces | Which page, card, code-example, dropdown and search-result backgrounds occur in each mode? How do slate utility backgrounds layer or gradient? |
| Primary and secondary text | Which body, nav, heading, metadata and muted text utilities are used on each resolved surface? |
| Links and current location | How do ordinary links, `.nav-active`, hover and visited states differ when colour is removed? |
| Actions and selection | What foreground/background pairs and focus states do `.cta-gold`, `.tab-gold` and the three Download choices use? |
| Boundaries and keyboard focus | Which borders, separators, focus rings and offsets remain visible beside their real background? |
| Search and status | Which Pagefind input, result, selected, mark, skeleton and focus roles are present? Which warning/status colours must preserve meaning beyond hue? |

## Implemented revision and recheck

**Baseline and choice.** The pinned source supplied a code-first homepage, its
identity, existing content and routes. The two directions above were alternatives
for ordering those same materials. Language Workbench was selected provisionally
because it extended the source's code and action sequence; Community Journal
remained useful for the long-form reading path. No audience preference was
inferred.

**Critique.** In CDC's first browser review of the local revision at
`4fba8807e63467e79c20ee030d47e2190f6dee36`, the Build It CTA still nested a
button inside a link and paragraphed content, actual About and blog paragraph
type differed, storage denial prevented a second theme toggle, and resizing
could lose focus. After those repairs, CDC's authored 200% text checks exposed
desktop navigation using two rows, a nested Discord button, and horizontal
overflow in feature, closing and reading content. A later visual scroll showed
that removing overflow alone had squeezed the feature heading into an 88px
column and left the About quotation only 198px wide. These were failures against
the agreed task and adaptation recipe, not evidence of user preference.

**Revision.** Four local commits produced the final site pin above. The first
implemented the content hierarchy, skip link, native tabs, disclosure, theme
control, and reading treatment while preserving supplied copy, data, imagery,
labels and destinations. CDC's concrete critique led to focused corrections for
valid native links, actual prose typography, storage-independent theme state,
focus recovery, compact desktop navigation, grid and closing-row sizing, and
long-token wrapping. The final correction made feature headings wrap below
their icons when both no longer fit and used scoped fluid inline padding for
feature cards and the About quotation. Generic design guidance and the LFE case
remain separate: these local values are not package defaults.

**Recheck.** CDC reports the final 390px/root32px feature heading at 230.8125px
with “Technology” on one line below its icon, and the About quotation at 302px
with 12px inline padding and readable multiword lines. All nine authored home,
About and technical-article adaptation copies had scrollWidth 390 and the
requested text, spacing and fallback properties. These are authored adaptation
simulations, not native browser zoom or failed network-font tests. CDC also
reports 16 normal viewport/theme/page conditions at earlier commit
`72c28e305efa9955605d21e7aa3d1fdc48bad05e`, retained only after checking their
applicability; they were not all rerun at the final pin. At the final source,
CDC retested the home/article paths, the mobile Download and Escape sequence,
tab wrapping, 320px home overflow, and the search → article → category → Blog
keyboard route. Learn More and header Learn reach the same page, and Use
resolves. Browser measurements and task outcomes are CDC observations, not CC
browser checks: the CC tool surface did not expose the assigned browser.

The local Cobalt build and validator passed after each scoped site handback;
Pagefind indexed 316 pages and 7,502 words, with its existing whole-body
fallback notice. A package-only build contains this optional example, not the
site. Search-query hydration, full contrast recertification, actual assistive
technology, native zoom, other browsers, failed-network font behavior, user
research, Project10 source fidelity, main-branch integration and publication
remain unverified and belong to their later owners. The local task branch is
not a public release.
