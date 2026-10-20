# Slice03 CDC verification

## Initial W handback — correction required

Sofie/root independently read actual W4fba8807 changes (25allowed paths), full
190-line site.js, changed templates/CSS and relevant unchanged blog-prose rules.
Adjacent trailers/source scope correct, CC fresh build/validate/syntax passing
is attestation at this point. D is still unchanged2bc2ff0b; no completed P return.
All four criteria remain open. This is an interim review, not slice acceptance.

Actual CUA at W4fba8807: one visible homepage H1, supplied summary before code;
all8tab click selections show one correct panel, right wrap reaches REPL, native
Space/Enter/Home/End actions exercised. Persistent theme toggles both ways with
storage available, retains theme-toggle focus and adds no fragment. Skip Enter
focuses main#content. Download Enter/Space opens; Tab reaches exact current2.2.0
URL; Escape returns Download focus; outside theme click closes without stealing
focus. At390px nested Escape first closes Download, then mobile nav. At320px
technical article: search288px on separate row, section links fit, local code
scrolls and no page-wide overflow; representative screenshot inspected. These
are bounded observations, not complete S03 adaptation/contrast/conformance.

F01: Build It still contains anchor role=button wrapping a native button plus
already-paragraphed build.content_html inside p. Initial recipe explicitly
required native links and no nested paragraph markup; masthead was repaired but
this other consumer was missed. Preserve every literal label/data/URL, replace
only these wrappers with a single styled native link and valid div content.

F02: actual About wrapper18px/30.6px Newsreader (wide643.5px), but visible p is
16px/24px due global text-base rule. Blog wrapper remains16px/27.2px system sans
(wide655.078125px), while its visible p is18px/27px Newsreader. Thus65ch is still
calculated in a different context from the reading text. Align both wrappers
and actual prose p/li at1.125rem/1.7 in Newsreader/Georgia, explicitly keep all
headings system and code monospace. Long links wrap; both prose contexts' tables
and pre must scroll locally, not merely About's new table rule. No global grid
narrowing or blanket font replacement.

F03: authored ignored storage-denial page copies current home and throws from
window.localStorage getter before site.js. First theme click gives dark/pressed
true; second stays dark/true. Navigation initializes, but getAppearance rereads
default after denied persistence, so toggle cannot round-trip. Keep requested
appearance in memory independently of persistence; preserve existing API/auto
resolution, use resolved current state for the persistent button. No new UI.

F04: resize handler closes/hides controls without a focus recovery decision.
CDC's focused desktop theme button loses focus to body when shrinking390px;
returning to desktop can similarly hide the focused mobile toggle. Preserve a
logical visible focus destination only when the resize hides the current target
(nav→mobile toggle, hidden mobile toggle→visible home/nav; closed download link
→its visible controlling button). Do not steal focus from article/search/tab.

These are the existing explicit source recipe, not new capability scope. I02
bundles four concrete repairs in existing4source paths, then CDC rechecks before
CC may claim actual case results. Existing search?q issue remains Arc02. No
package/AT/native zoom/otherbrowser/user-preference or public result claimed.


## I02 W handback — targeted repairs pass; adaptation correction required

W72c28e30, exact4allowed paths/adjacent trailers, full delta read. Actual denied
storage click sequence now dark→default→dark, matching pressed state with same
focused button. About and both articles now actual parent/p18px/30.6px Newsreader,
wide643.5px; About no blanket Learn/Use narrowing. Build It has four native link
CTAs, no nested buttons. Resize theme→narrow toggle and widened→Learn focus pass
after actual state settles (an immediate pre-media-event read initially saw body;
AX/current reread confirms correct visible Learn focus, not another source failure).

CDC sampled all4pages ×2modes ×2widths1280/390 =16 viewport/theme DOM/computed
conditions, representative visual screenshots, no whole-page overflow in those
normal cases. Separate authored home/About/technical article text200%, spacing,
fallback copies are outside indexed blog paths; actual fonts/spacing read, not
native zoom/network failure claims. Spacing/fallback have no page-wide overflow.
Enlarged text exposes real additional consumers below, so no complete pass yet.

F05: normal1280 header is124px/two rows despite ample room: base basis-full utility
wins over components flex auto after wrapping was enabled. Add responsive auto
basis to actual collapse consumer so normal desktop stays compact and can wrap
when genuinely needed. The closing Discord Go CTA still nests button in anchor;
make it one native styled link, literal text/destination retained. Its old h1 CSS
consumer also needs to target the new h2 rather than silently becoming dead.

F06: actual390px/root32px authored enlarged-text copy has home scrollWidth578,
About417 and technical article482. Offenders: feature header flex-shrink-0/auto
min grid sizing (Core Erlang Foundation right578); closing .join-us row/Go
right405; About blockquote's198px interior contains programming/Erlang321px
unbroken text; article inline code `(include-lib "clj/include/compose.lfe")`
extends to482. Fix intrinsic shrink/wrap for feature headers/grid and closing
row, prose/inline-code long-token wrapping, preserve pre local horizontal scroll,
assets/data/content. Do not clip overflow or shrink text to hide the failure.
Header enlargement itself wraps its logo/toggle; no claim all238px tall header
is a conformance defect. Recheck actual usable body and controls, not width alone.

The planned adaptations found these, not new scope. I03 narrows repair to5initial
allowlist paths; JS unchanged, I02 behavior evidence may be retained if valid.
Remaining actual search/route/read adaptation tasks still pending. No D/package
completion, browser conformance/expert/user research or slice closure claim.


## I03 W handback — overflow fixed, positive reading check still fails

AtW50fb3491 actual narrow200% copies now all scrollWidth390; no nested buttons;
normal1280 header72px with actual auto basis. I03 delta5paths exact, JS unchanged.
Actual search keyboard typing rebar3→ArrowDown→Enter reaches the technical article,
then Tutorials category and mobile Blog return work; current Categories/Blog both
underlined with aria-current. First transformed-uppercase Tutorials role query
matched nothing; observed href selector worked. No external release followed.

All9authored adaptation copies have actual intended properties: text root32px,
prose36px/61.2; spacing .12em/.16em/2em, fallback Georgia. Skip links operate in
all9. First body PageDown locator failed; focusable main and actual CUA scroll
worked. No native zoom/failed-font/AT claim. Source CSS declarations alone were
not promoted; actual viewport and representative reading screenshots inspected.

F07: width equality is necessary but insufficient. Actual scroll to enlarged
feature cards shows heading column88px, with Technology split Tech/nolo/gy;
three-column-like icon/header pairing and doubled inner padding survive despite
no overflow. About quotation has198px text interior and almost one word per line.
These are poor reading outcomes under the promised adaptation. Use a wrapping
feature header that gives its text a meaningful full line when icon+heading do
not fit, and scoped fluid card/quotation inline padding that preserves content
width at enlargement. Preserve supplied text/icon; don't shrink text/hide overflow.
A minimal example is wrap-able header with a text flex basis and clamped local
padding; exact implementation remains CC's. Recheck actual words/reading, not
scrollWidth alone. This is completion of F06's usable adaptation, not new scope.
I04 only3paths; root still withholds case results until actual readability passes.


## I04 — actual site result accepted, final case/package return pending

Current W1a64666cd7273ee97380bff163ed7642d13356df. Root read exact3path delta:
scoped padding outside layers reaches actual utility consumers, wrapping header
text basis, all data/icon/copy preserved; source clean, trailers correct.
Actual390px/root32px feature headings now230.8125px (was88), Technology fits
as a whole word below icon; quotation p302px (was198),12px inline padding;
actual CUA scroll screenshots show readable multiword quotation lines. All9
separate home/About/technical copies rerun at final source: scrollWidth390 and
actual intended text/spacing/fallback values. Font200% is root32px/prose36px/61.2;
spacing only body descendants1.5/.12em/.16em and p2em; fallback actual Georgia
prose/system/mono declarations. These are authored adaptations, not native zoom
or failed network requests. Visible enlarged reading—not width alone—passes.
Native CUA scroll worked; an earlier body press locator deadline was recovered
with actual scroll/focusable main. Optional FontFaceSet iteration wasn't supported
by the read-only bridge; no font-download/single-face or failure-network claim.

At final site, Learning More /learn redirects to/learn/, header/learn/ matches;
Use also resolves and neither gets the About-only prose wrapper. Native mobile
Download Tab/Enter/Escape, nested Escape and tab End→right wrap retested; 320px
home has no overflow. The complete8tab/normal theme/skip/resize/storage findings
above remain applicable: current JS equals accepted I02; final CSS changes only
feature/quotation padding and header basis, not controllers or colour roles.
Normal4page×2mode×2width16conditions at72c retained after actual deltas and final
home/article rechecks; don't relabel all16 as freshly run at1a. Fixed code and
S02 role values unchanged; original47foreground/12condition evidence stays at
its own pins, not a new full-site colour certification.

Root independently reran sequential make build→validate at1a after removing only
10owned ignored fixture copies outside indexed blog paths: both exit0, no tracked
drift. Validator13data/11content/4layouts; Pagefind316pages/7502words with retained
whole-body fallback notice. No tool update. Earlier CC native gates are separate
attestation. No external download clicked, article commands never executed.

Root-authored actual proof JPGs in artifacts: lfe-home-light.jpg (1280x720) and
lfe-article-dark-narrow.jpg (390x844), both final1a source. Their consumer is the
Operator's visual review. Viewport reset and existing tab marked for handoff.
No screenshot manifest/new maintained checker. Site result is ready for CC to
reconcile its optional case, commit owning version/history and fresh package;
all4ledger statuses remain open until that final authored return is independently
reviewed. Search?q hydration, actual AT/nativezoom/otherbrowsers, human evidence,
P10 fidelity/main integration and final2.0 remain explicitly outside this pass.
