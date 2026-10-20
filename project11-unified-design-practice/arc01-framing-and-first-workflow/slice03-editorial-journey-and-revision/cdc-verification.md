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
