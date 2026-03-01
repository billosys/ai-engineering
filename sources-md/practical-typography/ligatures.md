---
title: "Ligatures"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/ligatures.html"
---

<div id="content">

<div id="doc">

ligaturesOptional unless the letters f and i collide

Ligatures were invented to solve a practical typesetting problem. In the days of metal fonts, certain characters had features that physically collided with other characters. To fix this, font foundries cast ligatures, which combined the troublesome letters into one piece of <span class="no-hyphens">type.</span>

The most common ligatures involve the lowercase f because of its overhanging shape. Other ligatures also exist—some practical, some decorative, some <span class="no-hyphens">ridiculous.</span>

Digital fonts don’t have physical collisions, of course. But certain letter combinations might still overlap visually. The only time ligatures are mandatory is when you have an actual overlap between the letters f and i. Check this combination in the bold and italic styles <span class="no-hyphens">too.</span>

|  |  |
|----|----|
| <span style="font-family: concourse-t3">fi fj fl *ffi gg gy*</span> | ok |
| <span style="font-variant-ligatures: none;">fi fj fl *ffi gg gy*</span> | wrong |
| <span style="font-feature-settings: 'liga';">fi fj fl *ffi gg gy*</span> | right |

The font in the first row, , has an fi combination that doesn’t collide. That font will work fine without ligatures. But , in the second row, has fi (and other) collisions. Turn on ligatures to correct these collisions, as seen in the third <span class="no-hyphens">row.</span>

Beyond that, ligatures are largely a stylistic choice. To my eye, they can make <a href="body-text.html" class="xref">body text</a> look somewhat quaint or old-fashioned. If you like that look, great. I don’t. So unless characters are actually colliding, I generally keep ligatures turned <span class="no-hyphens">off.</span>

<div class="howto">

<div class="howto-name">

How to turn on ligatures

</div>

WordRight-click in the text and select Font from the menu. Click the Advanced tab. Next to Ligatures, select Standard Only (or one of the more elaborate <span class="no-hyphens">options).</span>

PagesView → Show Toolbar (or option + ⌘ + t) → Document button → Document pane → Ligatures

CSSEnable the OpenType feature liga, or use the shorthand property `text-rendering: optimizeLegibility` (or better still, <span class="no-hyphens">both)</span>

</div>

<div class="btw">

<div class="btw-title">

by the way

</div>

- Is it possible to insert ligatures manually? Yes. You can either insert them as you type from a character palette, or you can search and replace at the end. In HTML, you can enter the escape codes for the ligature glyphs. But I don’t recommend this. Manual ligatures can confuse spelling checkers, <a href="hyphenation.html" class="xref">hyphenation</a> engines, and search indexers, and generally cause more problems than they <span class="no-hyphens">solve.</span>

- Despite the name, ligatures don’t always connect two glyphs—sometimes they create separation, as in the italic gy <span class="no-hyphens">ligature.</span>

- Why?

  I mentioned ridiculous ligatures—at the top of my list is the Th ligature included among the default ligatures in certain Adobe fonts, like Minion. It’s frippery, amputating two perfectly good letters to make one ungainly hybrid. Worse, because Th is such a common letter combination, this ligature shows up all the time in <a href="body-text.html" class="xref">body text</a>. Just say no. (To the ligature, but also to Minion—see <a href="minion-alternatives.html" class="xref">Minion alternatives</a>.)

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="math-symbols.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="text-formatting.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="type-composition.html" class="box-link">chapter</a>

</div>

</div>

</div>
