# CC — Slice02 real LFE colour-role implementation

Read Project11 project-plan.md→Arc01 arc-plan.md→this slice plan/ledger first.
Operator-selected AM covers this arc only; CC OpenAI gpt-6-luna/high implements,
CDC/root independently reviews. You are sole LFE source/index/build writer until
immutable return. CDC owns only the loopback browser observation, pauses it during
your build and will independently exercise the returned artifact. No other agents.

## Pins, actual baseline and authority

P=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
Project=project11-unified-design-practice; arc=arc01-framing-and-first-workflow.
W=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/lfe-design-practice-arc01
branch codex/design-practice-arc01, HEAD036e231b09c48966da26d2227bccb4fa3b295df9.
AI=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/design-practice-arc01
accepted2bc2ff0b8bd1859b9016ed178663576a0e6e38f0, read-only in this slice.
Original site /Users/oubiwann/lab/lfe/lfe.github.io has unrelated dirty Makefile/
Rust files and untracked CC brief: do not edit/copy/revert any. W's only existing
tracked delta is generated src/css/site.css from CDC's successful baseline build;
it is expressly authorized for regeneration/adoption here. No push/PR/deploy/CI,
new dependencies/tool upgrades, content/IA rewrite or new arc. LFE main pushes
would deploy Pages. Local exact-scope commits are authorized.

Read source AGENTS.md, P Project11 AGENTS.md, project/arc/slice plans+ledgers,
S01 accepted workflow/case and CDC verification. Load current framework3.0.1,
engineering AM/intake, PM wayfinder/record/iteration sections, work-verification.
Load installed visual-design-system (or current AI design SKILL/colour/layout)
and Cobalt/Tailwind skills from the Operator's profile skills directory. Relevant
Cobalt CB10/12/13/19: actual pipeline, layouts/content and shared includes. Relevant
Tailwind theme/inline/dark guidance: local binary is4.3.0; older skill version
examples do not authorize installing anything. Read whole tailwind/site.css,
all exact templates you change, _cobalt.yml, Makefile build/validate paths and
actual generated site/pagefind/pagefind-component-ui.css variable/state selectors.
Read primaries https://tailwindcss.com/docs/theme#referencing-other-variables and
W3C contrast-minimum/non-text-contrast understanding pages for applicable pairing
checks, not whole-site conformance. Pagefind's theming URL failed for CDC; use
actual versioned generated vendor CSS, do not invent APIs. Record compact actual
coverage, structured-query scope (none unless needed) and contract readback before
edits in the one batch record. Recover truncated required passages.

## Binding result and worked implementation direction

Apply S01 Language Workbench to a useful neutral/gold light/dark foundation;
retain artwork, local Newsreader/system intent and all actual content/code/URLs.
Only colour class/value consumption and a brand-plate class are in scope. Do not
change geometry, JS, headings/labels/content, font choices or source data now.

Actual loaded path: css.liquid→site.css generated from tailwind/site.css;
legacy Sass lfe.css is not linked. Tailwind utilities in templates currently
compete with global rules. Current About nav-active computes gray in light mode.
Pagefind component CSS is loaded AFTER site.css, redefines :root --pf-* and uses
high specificity internal selectors. Current inline result background is60%white
and artwork shows through. Root aliases alone do not fix this. blog-search.liquid
also repeats the component stylesheet. Use component-scoped --pf-* adapters for
all actual searchbox/input/results/summary elements, solid opaque surfaces and
explicit focus/selection/mark/placeholder roles. Remove duplicate load if needed
and order vendor stylesheet before site overrides; don't edit vendor generated CSS.
No broad !important override fight or invented property names.

Recommended local mechanism: :root semantic --lfe-* values, .dark role overrides;
@theme inline --color-lfe-... aliases only where template utilities consume them.
Keep spacing/layout @apply; replace scattered neutral/gold consumer colours with
roles. Do not merely redefine Tailwind's entire gray palette or leave competing
legacy dark utility classes on changed elements. Existing primitive gold ramp may
remain local implementation material; do not impose a universal3tier rule.

Starting palette is a design proposal to test on actual consumers, not measured
browser evidence or a default for the generic skill. Refine within the same warm
light/ink dark/gold identity if a real pair/state fails; explain that refinement.

|Role|Light|Dark|
|---|---|---|
|canvas|#fcfaf5|#151c24|
|panel / raised|#ffffff / #f1ede4|#1d2732 / #263440|
|hover surface|#eae5da|#304252|
|primary / secondary / muted text|#252b33 / #51565d / #575f68|#f1efe7 / #c3c7ca / #aab2ba|
|link / hover / visited|#705406 / #533e04 / #694c77|#e9ca66 / #f6d977 / #d6b4e6|
|action / on-action / hover|#e2ba35 / #282311 / #f0cb53|#e4bf4b / #252014 / #f6d977|
|strong boundary / focus|#8a8173 / #705406|#8190a2 / #e9ca66|
|brand plate (both)|#fffaf0|#fffaf0|

Use quieter decorative separators if helpful, but input/required visual boundaries
and focus need their actual adjacent-pair checks. Keep active nav/tab location
underlined or bordered as well as distinct colour. Ordinary prose links retain
underlines. Focus-visible outlines use the focus role with a visible offset;
remove competing focus:outline-none/ring colour utilities in allowed templates.
CTA gold uses dark on-action text, not low-contrast white. Download choices must
retain Current/Previous/Development labels; use semantic action/secondary-action
roles rather than relying on green/blue/gold hue meanings. .download foreground
must work on all three actual backgrounds at rest/hover/focus in both modes.

Give wordmark's existing wrapper an always-light brand-plate class; preserve the
image file and image URL. Fixed dark code/syntax contexts need their own readable
on-code roles in BOTH modes; don't invert syntax assets or recolour code tokens.
Book/video CTA blues/reds, imagery overlays and category art can remain purposeful
component exceptions with checked text. Current gold announcement gradient and
news gradient/white-opacity text can fail: use opaque readable category-label
foreground and darker gradient endpoints if needed (e.g announcements #705406→
#916f10 withwhite; news #075e57→#0e637d withwhite), testing the lightest endpoint.
Preserve art/cover aspect/crop and content. Keep neutral/info/warning version
banners distinct by text/labels as well as hue, mapped to contextual foreground/
surface/border roles. Suggested pairs light info #16416f/#e9f1ff and warning
#6b450c/#fff3d6; dark info #c0d9f7/#192f47 and warning #f2d49a/#362a19.
The blog's existing quiet long-form and painterly artwork intent survives.

## Exact mutation scope

W23allowed paths (commit changed subset only, no unrelated generation):
tailwind/site.css; src/css/site.css; src/_includes/css.liquid;
src/_includes/nav.liquid; src/_includes/foot.liquid;
src/_includes/home/masthead.liquid; src/_includes/home/features.liquid;
src/_includes/home/buildit.liquid; src/_includes/home/books.liquid;
src/_includes/home/videos.liquid; src/_includes/home/closing.liquid;
src/_layouts/home.liquid; src/_layouts/page.liquid; src/_layouts/post.liquid;
src/_layouts/blog-index.liquid; src/_layouts/blog-archive.liquid;
src/_layouts/blog-author.liquid; src/_layouts/blog-authors.liquid;
src/_layouts/blog-categories.liquid; src/_layouts/blog-tags.liquid;
src/_layouts/blog-search.liquid; src/_layouts/plan/index.liquid;
src/_layouts/plan/page.liquid.
Only colour classes/value adapters, duplicate style-load removal/reordering and
brand-plate class here. Other template text, href/src/alt/data, code, structure,
content, sources, fonts/assets, configs and Rust/Makefile remain unchanged.

P3return paths in this slice: artifacts/batch-record.md, closing-report.md,
ledger.md Evidence/Notes only. All4criteria/statuses stay open for CDC review.
No AI source/package edits/version bump; last accepted package remains applicable
because its inputs are unchanged. Do not manufacture a package rebuild claim.

## Checks and immutable return

Start make help in W; sequential make build then make validate. Existing binaries
lfesite5.2.0, cached Tailwind4.3.0, Cobalt and Pagefind1.5.2 are available. No clean
(it uninstalls tooling) or install. Await each actual build before the next.
Inspect generated/loaded CSS consumption, not just token names. Compute applicable
candidate sRGB text pairs (normal text target4.5:1; applicable nontext3:1), including
hover/focus/selected/search/status/code/gradient weakest endpoint; no rounded pass
at a threshold. Low-contrast negative (#aaa onwhite) must be rejected by that same
calculation. Distinguish decorative/logo exceptions from actionable controls.
CDC will independently inspect actual rendered consumers after your immutable
return at home, About, real welcome article and search in light/dark wide/narrow;
you must not claim browser results you did not perform. Mobile search crowding,
reading measure and control-label/keyboard fixes remain S03, not hidden as done.

Check exact changed subset, protected content/assets/data/URLs/code/config/tooling
and original main untouched. Template diffs should be colour-class-only apart
from explicit stylesheet ordering/duplication; explain any exception before work.
Run git diff --check, preserve final newlines, inspect actual commit trees/trailers.
Write one compact batch note with decisions/coverage/checks/failures/limits and
source pair table; full4row proposed walk+artifact inventory+named Bubble-up to
arc in closing report. Do not say a section exists without inspecting final bytes.
No new corpus/inventory/replay checker or self-hash receipt commits.
Commit exact W changed allowlist, then P only3returns. Both messages end with:

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>

Report both actual final hashes and release ownership. Do not close/open slices,
change criteria/statuses, push/deploy or authorize main integration.
