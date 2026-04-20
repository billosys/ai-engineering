---
title: "Columns"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/columns.html"
---

<div id="content">

<div id="doc">

columnsFine in print, not on the web

They’re unusual in word-processor layouts, but I don’t object to columns in a long document. Columns are an easy way to get a shorter and more legible <a href="line-length.html" class="xref">line length</a> without using large <a href="page-margins.html" class="xref">page margins</a>. On a standard 8.5″ × 11″ page, two or three columns are fine. Four is too <span class="no-hyphens">many.</span>

<div class="howto">

<div class="howto-name">

How to use columns

</div>

WordPage Layout → Page Setup panel → Columns

Mac OS WordLayout tab → Text Layout panel → Columns

PagesView → Show Toolbar (or option + ⌘ + t) → Format button → Layout pane → Columns

CSS`columns:` \[number of <span class="no-hyphens">columns\]</span>

</div>

Usually columns look neatest when the rows of text are aligned vertically between columns (i.e., as if they were sitting on the same baseline). Look at a decent newspaper for an example. Getting this result takes a little extra effort. Note your <a href="line-spacing.html" class="xref">line spacing</a> and make sure any <a href="space-between-paragraphs.html" class="xref">space between paragraphs</a> works out to a whole multiple of the line spacing. The two most common options: set space between paragraphs to zero, or set it to be the same as the line <span class="no-hyphens">spacing.</span>

On the web, though most of today’s web browsers support CSS-based columns, as a design tool they’re not that useful. Practically speaking, columns need to fit inside a fixed vertical space. But by its nature, a web page has an indefinite bottom edge. Still, columns can be useful in situations where you have a small amount of text or a list of links that can fit on a browser single screen. See <a href="system-fonts.html" class="xref">system fonts</a> for an example of this <span class="no-hyphens">technique.</span>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="page-break-before.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="grids.html" class="nav"></a>

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
