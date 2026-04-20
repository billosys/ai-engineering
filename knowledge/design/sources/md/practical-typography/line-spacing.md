---
title: "Line Spacing"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/line-spacing.html"
---

<div id="content">

<div id="doc">

line spacing120–145% of the point size

Line spacing is the vertical distance between lines of text. Most writers use either double-spaced lines or single-spaced lines—nothing in between—because those are the options presented by word <span class="no-hyphens">processors.</span>

These habits are obsolete <a href="typewriter-habits.html" class="xref">typewriter habits</a>. Originally, a typewriter’s platen could only move the paper vertically in units of a single line. Therefore, line-spacing choices were limited to one, two, or more lines at a time. Single-spaced typewritten text is dense and hard to read. But double-spacing is still looser than <span class="no-hyphens">optimal.</span>

The traditional term for line spacing is leading (rhymes with bedding), so named because traditional print shops put strips of lead between lines of type to increase vertical space. Sometimes you see this term in typesetting <span class="no-hyphens">software.</span>

<div class="indented">

For most text, the optimal line spacing is between 120% and 145% of the point size. Most word processors, as well as CSS, let you define line spacing as a multiple. Or you can do the math—multiply your point size by the percentage. (The text in this paragraph has line spacing of 110%. It’s too <span class="no-hyphens">tight.)</span>

</div>

<div class="indented">

For most text, the optimal line spacing is between 120% and 145% of the point size. Most word processors, as well as CSS, let you define line spacing as a multiple. Or you can do the math—multiply your point size by the percentage. (The text in this paragraph has line spacing of 135%. It looks fine.)

</div>

<div class="indented">

For most text, the optimal line spacing is between 120% and 145% of the point size. Most word processors, as well as CSS, let you define line spacing as a multiple. Or you can do the math—multiply your point size by the percentage. (The text in this paragraph has line spacing of 170%. It’s too <span class="no-hyphens">loose.)</span>

</div>

Word processors have a bewildering number of ways to set line spacing. Don’t be thrown off—it all comes back to the same <span class="no-hyphens">thing.</span>

If you prefer setting line height in inches rather than points, divide the point measurement by 72 (there are 72 points to an <span class="no-hyphens">inch).</span>

<div class="howto">

<div class="howto-name">

How to set line spacing

</div>

WordRight-click in the text and select Paragraph from the menu. Go to the menu under Line spacing. Exactly is best—enter a fixed measurement. Single, 1.5 lines, and Double are equivalent to about 117%, 175%, and 233% line spacing, contrary to what their names suggest. Don’t use these—they miss the target zone of 120–145%. Multiple is also acceptable—enter line spacing as a decimal. To get line spacing in the 120–145% range, use a Multiple value of 1.03–1.24. (Not 1.20–1.45—as noted above, Word uses peculiar line-spacing math.) Never use At least, because that gives Word permission to adjust your line spacing <span class="no-hyphens">unpredictably.</span>

PagesView → Show Toolbar (or option + ⌘ + t) → Format button → Style pane → under Spacing, there’s a popup menu. Exactly is best—enter a fixed measurement. You can also use the Lines option, but like Word, it adds extra space—about 17%. Therefore, to get line spacing in the 120–145% range, use a Lines value of 1.03–1.29. Avoid the other <span class="no-hyphens">options.</span>

CSSUse the `line-height` property, preferably without units [(here’s <span class="no-hyphens">why)</span>](http://stackoverflow.com/a/20818206/1486915)

</div>

<div class="btw">

<div class="btw-title">

by the way

</div>

- Recall that different fonts set at the same point size may not appear the same size on the page. (See <a href="point-size.html" class="xref">point size</a> for why.) A side effect is that fonts that run small will need less line spacing, and vice <span class="no-hyphens">versa.</span>

- Line spacing affects the length of a document more than point size. If you need to fit a document onto a certain number of pages, try adjusting the line spacing <span class="no-hyphens">first.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="space-between-paragraphs.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="line-length.html" class="nav"></a>

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
