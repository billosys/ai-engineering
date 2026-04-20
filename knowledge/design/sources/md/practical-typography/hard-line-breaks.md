---
title: "Hard Line Breaks"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/hard-line-breaks.html"
---

<div id="content">

<div id="doc">

hard line breaksSame paragraph, different line

The hard line break moves the next word to the beginning of a new line without starting a new <span class="no-hyphens">paragraph.</span>

|                 | Word           | Pages          | HTML     |
|-----------------|----------------|----------------|----------|
| hard line break | shift + return | shift + return | `<br />` |

A hard line break can help control text flow when a <a href="carriage-returns.html" class="xref">carriage return</a> won’t work. For instance, this <a href="headings.html" class="xref">heading</a> breaks <span class="no-hyphens">awkwardly:</span>

<table class="example">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td style="font-size: 120%"><span>4. The project is scheduled to be finished in<br />
May.</span></td>
</tr>
</tbody>
</table>

Suppose you want the line to break before finished. That way, the first line will end in a more logical place and the two lines will be balanced. If you use a <a href="carriage-returns.html" class="xref">carriage return</a>, you’ll <span class="no-hyphens">get:</span>

<table class="example">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="font-size: 120%"><span>4. The project is scheduled to be<br />
5. finished in May.</span></td>
<td>wrong</td>
</tr>
</tbody>
</table>

Not what you want. Instead, put a hard line break after to be:

<table class="example">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="font-size: 120%"><span>4. The project is scheduled to be<br />
finished in May.</span></td>
<td>right</td>
</tr>
</tbody>
</table>

Hard line breaks are also useful for separating the lines of an address (for instance, on <a href="letterhead.html" class="xref">letterhead</a>). See <a href="centered-text.html" class="xref">centered text</a> for another example of the hard line break in <span class="no-hyphens">use.</span>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="tabs-and-tab-stops.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="carriage-returns.html" class="nav"></a>

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
