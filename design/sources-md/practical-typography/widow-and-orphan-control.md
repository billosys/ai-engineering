---
title: "Widow And Orphan Control"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/widow-and-orphan-control.html"
---

<div id="content">

<div id="doc">

widow and orphan controlYour call

Picture a paragraph that starts at the bottom of one page and continues at the top of the next. When only the last line of the paragraph appears at the top of the second page, that line is called a widow. When only the first line of the paragraph appears at the bottom of the first page, that line is called an orphan.

Widow and orphan control prevents both. Orphans are moved to the next page with the rest of the paragraph. To cure widows, lines are moved from the bottom of one page to the top of the next. It’s a little more complicated than it sounds, because curing a widow cannot create a new orphan, nor vice <span class="no-hyphens">versa.</span>

Be aware that if you use widow and orphan control, you will frequently see blank lines at the bottom of your pages. This is normal, since lines must be transplanted to cure the <span class="no-hyphens">problem.</span>

Widow and orphan control in a word processor is all-or-nothing. You can’t control widows and orphans separately, even though widows are more distracting. Why? Orphans appear at the beginning of a paragraph, so they’re at least a full line. But widows can be any length, even a single word, because they appear at the end of a <span class="no-hyphens">paragraph.</span>

Do you need widow and orphan control? Try it. See how it looks. In my own work, I approach widow and orphan control the same way I approach <a href="ligatures.html" class="xref">ligatures</a>—I only use it if widows and orphans are causing a visible problem. Otherwise, I find that the blank lines at the bottom of the page are more annoying than the widows and <span class="no-hyphens">orphans.</span>

<div class="howto">

<div class="howto-name">

How to turn on widow & orphan control

</div>

WordRight-click in the text and select Paragraph → Line and Page Breaks → check Widow / Orphan <span class="no-hyphens">control</span>

PagesView → Show Toolbar (or option + ⌘ + t) → Format button → More pane → check Prevent widow & orphan <span class="no-hyphens">lines</span>

CSSNot <span class="no-hyphens">applicable</span>

</div>

<div class="btw">

<div class="btw-title">

by the way

</div>

- You can also cure isolated widows and orphans with some judicious editing. But don’t use a <a href="hard-line-breaks.html" class="xref">hard line break</a> or <a href="carriage-returns.html" class="xref">carriage return</a>.

- Widows & orphans aren’t typically an issue on the web, because web content doesn’t naturally span multiple pages. Browsers, however, are happy to put a small word alone on the last line of a paragraph, which always looks bad. You can fix this with a <a href="nonbreaking-spaces.html" class="xref">nonbreaking space</a> and a little clever <span class="no-hyphens">programming.</span>

- Here in the 21st century, the *widow* and *orphan* terminology lands on the questionable side of quaint. I favor coining a new term for this typographic condition. One word should suffice—it’s the same problem, just at different edges of the page. Maybe *stragglers* and thus *straggler control?* Nominations <span class="no-hyphens">welcome.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="space-above-and-below.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="keep-lines-together.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="page-layout.html" class="box-link">chapter</a>

</div>

</div>

</div>
