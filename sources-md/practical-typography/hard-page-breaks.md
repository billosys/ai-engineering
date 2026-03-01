---
title: "Hard Page Breaks"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/hard-page-breaks.html"
---

<div id="content">

<div id="doc">

hard page breaksMove to the top of the next page

The hard page break puts the next word at the top of a new <span class="no-hyphens">page.</span>

|                 | Word            | Pages                   | HTML           |
|-----------------|-----------------|-------------------------|----------------|
| hard page break | control + enter | control + num-pad enter | not applicable |

To move text to the next page, use one hard page break, not multiple <a href="carriage-returns.html" class="xref">carriage returns</a>. If you use carriage returns, your document will become impossible to edit—as soon as you change anything before the page break, the text will go out of alignment. The hard page break guarantees consistent <span class="no-hyphens">behavior.</span>

<div class="howto">

<div class="howto-name">

How to insert a hard page break (alternate method)

</div>

WordPage Layout → Page Setup panel → Breaks → Page or Insert → Pages panel → Page <span class="no-hyphens">Break</span>

Mac OS WordInsert → Break → Page <span class="no-hyphens">Break</span>

PagesInsert → Page <span class="no-hyphens">Break</span>

</div>

<div class="btw">

<div class="btw-title">

by the way

</div>

- Hard page breaks can be built into paragraph styles to ensure that classes of paragraphs (e.g., major section headings) always start at the top of a new page. See <a href="page-break-before.html" class="xref">page break before</a>.

- Strictly speaking, CSS does support a set of page-break tags, but they’re only meaningful when the document is printed. In practice, they are neither common nor useful. If you want your text to jump to the beginning of a new HTML page, you’ll need to find another <span class="no-hyphens">way.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="carriage-returns.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="optional-hyphens.html" class="nav"></a>

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
