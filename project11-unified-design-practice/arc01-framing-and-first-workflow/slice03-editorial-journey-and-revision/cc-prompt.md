# CC assignment — Arc01 Slice03 editorial journey and revision

Explicit CC routing: OpenAI gpt-6-luna/high; same Operator-authorized actor.
Final slice of Arc01 only. Ship real LFE reading/control improvements and update
the optional packaged case from an initial proposal into an honest worked result.

## Pins, ownership and required intake

W=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/lfe-design-practice-arc01,
branch codex/design-practice-arc01 at9cf7cf86f8d6ea6fc50eaf46bf950e1312def82f.
D=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/design-practice-arc01,
branch codex/project11-arc01-lfe-workflow at2bc2ff0b8bd1859b9016ed178663576a0e6e38f0.
P=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning; this slice.
Issue is the commit introducing this prompt, derive it without a receipt child.
Original LFE main dirty Makefile/Rust files/brief and AI main knowledge/lfe remain
protected; neither original checkout is this assignment's mutation baseline.

You own W/D source/index/build and the browser preview until immutable return;
CDC pauses those operations. Existing loopback server port55831 serves W/site;
reuse it, do not start another server. Browser2/tab2 is the only owned tab.
After handback CDC owns independent browser review. P other plans are CDC's;
you may edit only the five return paths below, criteria/statuses frozen open.
Local exact-scope commits authorized; no push/PR/merge/deploy/install/external
CI write or successor. No execute commands contained in old articles.

Read actual AGENTS and P project-plan first, then Arc01 current arc-plan,
this whole slice plan/ledger/prompt; source framework/PM README and required
open-set/iteration/close/ownership routes; engineering-methods AM and prompt
intake, work-verification independent boundaries. Retain known unchanged reads
by explicit pins rather than pretending fresh reads. Recover any truncated
critical outputs before editing. Read whole design workflow and optional case,
SKILL metadata/history, relevant design type/layout routes. Load Cobalt and
Biome JS guidance for changed Liquid/CSS/native JS, focused actual bug routes.
Read every W allowed template/JS file you will change and the relevant CSS
blocks, current _cobalt.yml/Make help/build/validate definitions and supplied
home/site/excerpts/About data. Read welcome article's purposeful archive/painting
framing and technical article actual target, not all unrelated posts. Record one
compact actual intake/readback before edits in batch-record, no new archive.

Primary behavioral sources: WAI APG tabs and disclosure patterns,
https://www.w3.org/WAI/ARIA/apg/patterns/tabs/ and
https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/ ; W3C Understanding text-spacing
and reflow. Read relevant behavior/limits; no comprehensive framework survey.
Existing site source and runtime are primary for local APIs, no guessed vendor
upgrade. Prior accepted S02 verification gives exact colour/preservation checks.

## Resolved implementation recipe

1. Homepage: visible H1 uses existing page.title (Lisp Flavoured Erlang), retain
rotating tagline; move supplied summary/Learn More ahead of code work area.
Preserve exact content_html, labels/destination and all eight code excerpts.
Use a div for already-paragraphed summary/description HTML, no nested p/h2.
Navigation links must not contain buttons. Home section H1→H2 and Build It
child H2→H3 retain literal text. No invented marketing claim.
2. Tabs: remove data-hs-tab competing ownership; use one small native controller.
Preserve IDs/content, proper controls and labelled/focusable panels; remove
invalid outer tabpanel label. Initially exactly one selected tab/tabindex0,
others false/-1, one panel visible. ArrowLeft/Right wrap, Home/End endpoints;
click/Enter/Space activate, automatic selection allowed for preloaded content.
Do not intercept Up/Down scrolling. Keep active class for accepted styling.
3. Reading: About-only editorial-prose class in page layout, not narrowing
Learn/Use grids. Newsreader/Georgia prose and existing blog-prose: ~65ch in the
actual prose font context at1.125rem/1.7; system headings and monospace code
retain roles. This is contextual measure, not65literal characters. Long links
wrap, code/tables overflow locally. Preserve archive prose/paintings/captions.
4. Wayfinding: first keyboard Skip to content shared link; all12 relevant mains
id=content/tabindex=-1 (old plan layouts lack ID). Wordmark link LFE home,
meaningful image alt, asset unchanged. Existing empty sponsor link named Billo
Systems, destination unchanged. Theme becomes ONE persistent native type=button,
stable name Dark theme, aria-pressed actual dark state; icons aria-hidden.
Reuse HSThemeAppearance storage/event API, retain button focus and no#!navigation.
Guard storage access so denial cannot abort controls. Keep existing auto API if
retained but apply actual resolved .dark correctly; no new settings screen.
5. Download: native disclosure (not ARIA appmenu), preserve button/labels/version
URLs. Expanded/controls reflect one local visibility owner. Native Enter/Space,
ordinary Tab through links; Escape within closes/returns button focus; outside
click or focus departure closes without focus theft. Move only its old inline
handler from end-scripts into site.js, preserve unrelated imports/analytics.
6. Mobile nav: native toggle, expanded/controls reflect actual visibility; remove
old hs-collapse/data hooks to avoid Preline competition. Existing40rem matchMedia
breakpoint, desktop visible, resize resets state without stranding focus. Wrap
header/links for enlarged text; contain dropdowns. Escape inside mobile closes
nested Download first then mobile menu/returns toggle focus. Do not hijack Escape
from independent Pagefind results. Keep small explicit controllers, no new runtime.
7. Blog subnav: narrow section links and search separate flexible rows, full
usable search width; compact desktop. Actual section location has non-colour
cue. Preserve Pagefind labels/keyboard/solid roles/routes; do not replace it.
Existing standalone?q= hydration did not populate in CDC's S02 check: Arc02 owns
that deeper state issue. Typing search works; no silent broadened investigation.

## Exact source/return scope

W25 possible paths (change only needed subset): tailwind/site.css;src/css/site.css;
src/js/site.js;src/_includes/end-scripts.liquid;src/_includes/nav.liquid;
src/_includes/foot.liquid;src/_includes/blog-subnav.liquid;
src/_includes/home/{masthead,features,buildit,books,videos,closing}.liquid;
src/_layouts/{home,page,post,blog-index,blog-archive,blog-author,blog-authors,
blog-categories,blog-tags,blog-search,plan/index,plan/page}.liquid.
No other content/data/assets/fonts/routes/config/tooling/vendor edits.
D3 only: knowledge/design/SKILL.md;knowledge/design/version-history.md;
knowledge/design/guides/examples/lfe-workflow.md. After actual site result, bump
owning metadata1.2.0→1.2.1 and append sibling history, preserve prior bytes.
Never repeat owning skill version in example/guide. Generic workflow unchanged.
P5 only: artifacts/batch-record.md;artifacts/lfe-home-light.jpg;
artifacts/lfe-article-dark-narrow.jpg;closing-report.md;ledger.md Evidence/Notes.
Two JPGs serve actual user review of changed site; inventory them, no capture
manifest/census/checker framework. Source/P commits separate exact allowlists,
required adjacent parsed Codex and BilloAI trailers. No selfhash receipt child.

## Firsthand checks and worked result

Start make help; sequential W make build→make validate; existing Node syntax
check src/js/site.js (not a Node application/dependency). Check real control
behavior and preservation, not implementation-mirroring stubs. Source-only
checks cannot prove focus/visible state. Actual generated files only owned paths.

CUA only for browser interactions. First invocation bind exactly one entrypoint:
var ccLfeTab=await cua.getTab("2",{browser:"2"}); read returned docs before next
call. After a summarized computer-use context, rewriteDocumentation first.
Reuse port55831, no other tabs/user Chrome. No external actions/download clicks.
Readonly DOM evaluation for measurements; no script state mutation via evaluate,
other CDP/Playwright libraries or injected browser automation. Source-authored
ignored HTML test fixtures are allowed under W/site/_arc01-checks, not indexed
blog paths. Use actual screenshot/DOM observations rather than AX dumps of
entire long articles. Save screenshots with documented CUA screenshot bytes and
normal filesystem writer; final screenshot artifacts are JPG, not base64 notes.

Exercise home/About/welcome article and technical /blog/tutorials/2016/03/25/0858-lfe-and-rebar3/
at1280x720,390x844, plus320px narrow checks; light/dark, skip/focus, all8tabs,
arrow/Home/End/Enter/Space, persistent theme, mobile/Download/resizing and actual
search typing→rebar3 article→Blog/topic return. Inspect destination hrefs rather
than downloading external books/releases. Check Learn /learn and /learn/ resolve.
Inspect actual visible layout/measure/spacing and scroll containment, not only
page scrollWidth. Include respective independent fixtures for (a)root font200%,
(b)only line-height≥1.5,paragraph2em,letter.12em,word.16em, (c)forcedGeorgia/system/
mono fallback. These are authored adaptation simulations, not native browser zoom,
actual network font failure or WCAG/AT certification. Record actual computed
properties and visible task outcomes. Fix material in-scope failures. Keep unrun
conditions explicit. Remove only known owned fixture files after checks, never
unknown work. Reset temporary viewport, markHandoff on tab2 for CDC; pause browser
and source builds after immutable return.

After actual site commit, reconcile optional lfe-workflow: preserve initial
brief/alternatives/choice recognizably, distinguish initial source/proposal from
actual implementation/observations, add final local site pin and one concrete
baseline→critique→revision→recheck. S02 measured colours at recorded pin may be
retained honestly; don't claim bitmap/source pair is rendered pixel measurement.
No fabricated users/preferences/comparative gains/no-analytics assertion. Include
actual remaining query hydration/nativezoom/AT/otherbrowser/Project10fidelity and
main/publication limits with later owner. Case readable without the LFE clone.

D sequential make check-skills,check-skill-versions,check-package-paths using
R/.venv/bin/python explicitly via SKILL_PYTHON; then separate fresh make design.
Check all10archive Markdown members/current source bytes and actual isolated
entrypoint→workflow→case→implementation/critique/revision task answer, not just
member counts. Preserve233cards/161sources/sixoldguides via Git object scope,
not recertification. Record warnings/failures/retries/retained versus fresh gates.

Return one compact complete batch note and proposed four-row close with actual
source hashes, artifact inventory and scope-as-specified/delivered/arc bubble-up.
Read final committed records before claiming sections exist. Ledger criteria and
statuses remain open until independent CDC; no slice/arc self-acceptance. Report
actual W,D,P hashes and hand back browser ownership. Stop at that handoff.
