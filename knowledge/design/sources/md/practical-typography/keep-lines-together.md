---
title: "Keep Lines Together"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/keep-lines-together.html"
---

<div id="content">

<div id="doc">

keep lines togetherAlways use with headings

Keep lines together ensures that all lines in a paragraph appear on the same page. If the last line of the paragraph won’t fit on the current page, the whole paragraph will be moved to the next <span class="no-hyphens">page.</span>

Use this option with <a href="headings.html" class="xref">headings</a> to prevent them from starting at the bottom of one page and continuing at the top of the next. That looks <span class="no-hyphens">bad.</span>

Like <a href="widow-and-orphan-control.html" class="xref">widow and orphan control</a>, keeping lines together will create gaps at the bottom of pages. But unlike widow and orphan control, you only want to keep lines together in special situations, not as part of your default text <span class="no-hyphens">formatting.</span>

Why? Keeping lines together is a blunter technique. It only works on whole paragraphs, so the longer the paragraph, the bigger the <span class="no-hyphens">gap.</span>

If you need to make groups of elements stick together, the keep-lines-together option works well with <a href="hard-line-breaks.html" class="xref">hard line breaks</a>. Recall that hard line breaks don’t create a new paragraph, but rather a set of lines. Keeping lines together will ensure this set of lines appears on a single <span class="no-hyphens">page.</span>

For instance, it’s helpful to keep lines together in signature <span class="no-hyphens">blocks:</span>

<div class="indented">

<table class="sigblock">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>May 19, 2026       </td>
<td>Boxer Bedley &amp; Ball<br />
__________________<br />
Violet Manganese<br />
Auditor for MegaCorp</td>
</tr>
</tbody>
</table>

</div>

Here, you’d put a hard line break at the end of each line. Then you’d set the whole signature block—which is a single paragraph—to keep lines together. That way, you’ll never have to worry that half the block will end up on one page and half on the next. All of it travels <span class="no-hyphens">together.</span>

<div class="howto">

<div class="howto-name">

How to keep lines together

</div>

WordRight-click in the text and select Paragraph → Line and Page Breaks → check Keep lines <span class="no-hyphens">together</span>

PagesView → Show Toolbar (or option + ⌘ + t) → Format button → More pane → check Keep lines on same <span class="no-hyphens">page</span>

CSSNot <span class="no-hyphens">applicable</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="widow-and-orphan-control.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="keep-with-next-paragraph.html" class="nav"></a>

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
