---
title: "Page Break Before"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/page-break-before.html"
---

<div id="content">

<div id="doc">

page break beforeAlternative to hard page breaks

Page break before forces a paragraph to start at the top of a new page. Visually, there’s no difference between using the page-break-before option and typing a <a href="hard-page-breaks.html" class="xref">hard page break</a> in front of the paragraph. But that’s only efficient for the occasional <span class="no-hyphens">paragraph.</span>

The page-break-before option is intended to be incorporated into <a href="paragraph-and-character-styles.html" class="xref">paragraph and character styles</a> so all paragraphs of a particular style will start at the top of a new page. For instance, you might apply it to your top-level <a href="headings.html" class="xref">heading</a> style. In a long document, typing hard page breaks in front of each heading would be <span class="no-hyphens">tedious.</span>

<div class="howto">

<div class="howto-name">

How to use page break before

</div>

WordRight-click in the text and select Paragraph → Line and Page Breaks check Page break <span class="no-hyphens">before</span>

PagesView → Show Toolbar (or option + ⌘ + t) → Format button → More pane → check Start paragraph on a new <span class="no-hyphens">page</span>

CSSNot <span class="no-hyphens">applicable</span>

</div>

<div class="btw">

<div class="btw-title">

by the way

</div>

- A small wrinkle arises when you use page break before with headings that have <a href="space-above-and-below.html" class="xref">space above and below</a>. Your word processor, trying to be helpful, will ignore the space-above setting if the heading is the first thing on the page. If that’s what you want, great. But if it’s not, you’ll have to devise a suitable <span class="no-hyphens">workaround.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="keep-with-next-paragraph.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="columns.html" class="nav"></a>

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
