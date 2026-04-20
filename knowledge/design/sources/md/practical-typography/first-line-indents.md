---
title: "First Line Indents"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/first-line-indents.html"
---

<div id="content">

<div id="doc">

first-line indentsBetween one and four times the point size

A first-line indent is the most common way to signal the start of a new paragraph. The other common way is with <a href="space-between-paragraphs.html" class="xref">space between paragraphs</a>.

First-line indents and space between paragraphs have the same relationship as belts and suspenders. You only need one to get the job done. Using both is a mistake. If you use a first-line indent on a paragraph, don’t use space between. And vice <span class="no-hyphens">versa.</span>

A first-line indent on the first paragraph of any text is optional, because it’s obvious where the paragraph <span class="no-hyphens">starts.</span>

Typically, a first-line indent should be no smaller than the current <a href="point-size.html" class="xref">point size</a>, or else it’ll be hard to notice. It should be no bigger than four times the point size, or else the first line will seem disconnected from the left edge. So a paragraph set in 12 point should have a first-line indent of 12–48 points. (Recall that there are 72 points to an inch, so this works out to <span class="no-hyphens">0.17–0.67″.)</span>

But use your judgment—consider the width of the text block when setting the first-line indent. For instance, narrow text blocks (3″ or less) should have first-line indents toward the low end of this range. Wider text blocks should have bigger <span class="no-hyphens">indents.</span>

<table class="example">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="font-size: 120%"><div style="text-indent:0.3em">
<span>The skateboarder was denied entry</span><br />
<span>to the applicant's home in the gated</span><br />
<span>community known as Luxuria.</span>
</div></td>
<td>wrong</td>
</tr>
<tr>
<td style="font-size: 120%"><div style="text-indent:2.5em">
<span>The skateboarder was denied</span><br />
<span>entry to the applicant's home in the</span><br />
<span>gated community known as Luxuria.</span>
</div></td>
<td>wrong</td>
</tr>
<tr>
<td style="font-size: 120%"><div style="text-indent:1em">
<span>The skateboarder was denied entry</span><br />
<span>to the applicant's home in the gated</span><br />
<span>community known as Luxuria.</span>
</div></td>
<td>right</td>
</tr>
</tbody>
</table>

Don’t use <a href="word-spaces.html" class="xref">word spaces</a> or <a href="tabs-and-tab-stops.html" class="xref">tabs</a> to indent the first line—as you recall from <a href="white-space-characters.html" class="xref">white-space characters</a>, that’s not what they’re for. Paragraphs indented with word spaces or tabs are hard to keep consistent and waste far more time than they save. Use the right tool for the <span class="no-hyphens">job.</span>

<div class="howto">

<div class="howto-name">

How to set a first-line indent

</div>

WordRight-click in the text and select Paragraph → Indents and Spacing. Under Indentation, from the popup menu labeled Special, select First line and enter the measurement in the adjacent <span class="no-hyphens">box.</span>

PagesView → Show Toolbar (or option + ⌘ + t) → Format button → Layout pane → under Indents, in the box labeled First, enter the <span class="no-hyphens">measurement.</span>

CSSUse the `text-indent` <span class="no-hyphens">property</span>

</div>

<div class="btw">

<div class="btw-title">

by the way

</div>

- It’s possible to set a negative first-line indent, or *hanging indent*. Hanging indents are used in lists to create a rectangular text block with a list bullet that dangles off to the left. (Like this one.) Avoid using a hanging indent without a bullet—your text block should not resemble Oklahoma. Text should only be indented <span class="no-hyphens">inward.</span>

- *rop caps* are, in theory, another option for the first paragraph—the first letter of the paragraph is enlarged so it descends three or four lines. In certain decorative contexts, they’re tolerable. But if you’re just using the drop-cap function in your word processor, forget it. It looks <span class="no-hyphens">bad.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="justified-text.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="space-between-paragraphs.html" class="nav"></a>

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
