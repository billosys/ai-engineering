# Slice02 CDC verification

## Initial return — source a6c19f4d / planning30bf31d8

Sofie/root independently reviewed CC /root/p11_arc01_cc. Initial prompt f232e713;
**current verdict: bounded correction required, S02-01/02 open; S02-03/04 done at
this inspected scope.** No slice close or successor authorization.

Read full actual CSS delta, template diffs and CC return/batch/ledger. Independently
reran sequential make build/validate: both pass,147sitemapURLs; Pagefind reports
316pages/7502words and the existing whole-body fallback notice. No tool upgrade.
23source paths and3return paths exact; all templates except deliberate stylesheet
order/dedupe are class-only (including removed whole body colour attributes).
All content/data/assets/config/tooling protected by exact Git object/diff scope;
source and return have both parsed adjacent coauthors, whitespace passes, AI2bc2ff0b
and its accepted package inputs unchanged. An initial class-strip check falsely
flagged removed class attributes; the corrected predicate passes unchanged source.

CDC inspected home/About/welcome article in light/dark at1280x720 and390x844:
12actual DOM/computed-style viewport conditions, with representative screenshots,
plus actual inline and standalone Pagefind search. No whole-page horizontal overflow
in those checks; mobile subnav search remains visibly crowded (owned by S03).
Direct keyboard/pointer checks covered code focus, current download focus/hover,
three download foregrounds, About's underlined location, theme changes and live
search selection. Pointer placement used context-click/Escape without following
external links. All47sampled actual visible text pairs pass4.5; examples:

|Actual consumer|Light|Dark|
|---|---:|---:|
|Current download rest|8.4473|9.1501|
|Fixed code description/tab rest|8.5980|8.5980|
|Fixed code active|9.1289|9.1289|
|Footer text|10.1653|12.6479|
|Article metadata|6.477|7.048|
|Selected search excerpt|5.8888|6.0897|
|Selected search mark|5.6487|6.4658|

Code focus is visibly2px bright with2px offset (9.1289against fixed code surface);
download focus uses the surrounding panel (9.438dark), not the action's own fill.
The same relative-luminance calculation rejects #aaa/white at2.3231. Source values
and actual measured consumers are distinct. An empty Pagefind wrapper computes
CanvasText/black but its visible title/excerpt children use the correct roles;
CDC refined its sampling target and did not report a false unreadable-result bug.
Visited styling is source-pair evidence; browser privacy prevents claiming a
computed visited-state measurement. Bitmap brand and image-specific overlays are
visual/contextual checks, not a numeric CSS-text conformance claim. No AT/native
zoom/other-browser/full-site conformance or user preference result.

During implementation, CDC found page-ink roles on fixed-dark code, parsed nested
paragraph consumption, footer foreground and download-selector issues; CC repaired
these before the first candidate. Those joins now reproduce correctly. One actual
browser discrepancy remains, to be fixed in Iteration01:

**F01 — hover role loses to utilities.** On nav social/theme links, `.nav-hover-gold:hover`
is in components while base text-lfe-primary/secondary is in utilities. Even with
:hover=true, the light GitHub link computes #252b33 rather than intended #533e04.
Contrast is sufficient, but the declared contextual hover consumer is ineffective.
Add the existing hover:text-lfe-link-hover utility to those4links; do not redesign.

**F02 — qualify the brand table.** CC's13.7121wordmark table row calculates a nominal
CSS foreground; that property does not recolour raster logo pixels. Label it as a
nominal CSS pairing, not bitmap text measurement. Real supplied logo remains unchanged
and was visually inspected against its light plate.

Rows03/04 done for the actual initial checks/scope; retain them at their pin unless
new changes invalidate them. Rows01/02 await actual repaired consumer/record review.
The scoped artefact is only batch-record.md; no hidden new inventory or snapshots.
Broader reading/keyboard remains S03. Full search works by typing; its existing?q=
hydration did not populate the field in this test, so do not claim it works. The
inline-search reading flow remains viable; hand the broader deep-link/state issue
to Arc02 rather than silently broadening this colour slice. Original P10 fidelity,
project capabilities, main integration and release remain open. No push/deployment.
