---
title: "Nonbreaking Spaces"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/nonbreaking-spaces.html"
---

<div id="content">

<div id="doc">

nonbreaking spacesPrevent awkward breaks

Your word processor assumes that a word space marks a safe place to flow text onto a new line or page. A *nonbreaking space* is the same width as a word space, but it prevents the text from flowing to a new line or page. It’s like invisible glue between the words on either <span class="no-hyphens">side.</span>

|  | Word | Pages | HTML |
|----|----|----|----|
| nonbreaking space | control (option on Mac) + shift + space bar | option + space bar | `&nbsp;` |

Put a nonbreaking space before any numeric or alphabetic reference to prevent awkward breaks. Recall this example from <a href="paragraph-and-section-marks.html" class="xref">paragraph and section marks</a>:

<table class="example">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="font-size: 120%"><span>The seller can, under Business Law §<br />
1782, offer a full refund to buyers. But ¶<br />
49 of the contract offers another option.</span></td>
<td>wrong</td>
</tr>
<tr>
<td style="font-size: 120%"><span>The seller can, under Business Law<br />
§ 1782, offer a full refund to buyers. But<br />
¶ 49 of the contract offers another option.</span></td>
<td>right</td>
</tr>
</tbody>
</table>

In the top example, normal word spaces come after the § and ¶ symbols, and the numeric references incorrectly appear on the next <span class="no-hyphens">line.</span>

In the bottom example, nonbreaking spaces come after the § and ¶ symbols. This time, the symbols and the numeric references stay <span class="no-hyphens">together.</span>

An example ripped from the <span class="no-hyphens">headlines:</span>

Also use a nonbreaking space after other abbreviated reference marks (Ex. A, Fig. 23), honorifics and titles (Sgt. Rock, Ms. Marvel), and <a href="trademark-and-copyright-symbols.html" class="xref">trademark and copyright symbols</a>.

<div id="nonbreaking-spaces-in-html" class="subhead">

[Nonbreaking spaces in HTML](#nonbreaking-spaces-in-html)

</div>

Nonbreaking spaces can be inserted into HTML documents either with an escape code (`&nbsp;`) or by typing a nonbreaking space character (using whatever key shortcut is assigned to it in your text <span class="no-hyphens">editor).</span>

If you believe in the principle that source code should be optimized for readability—I do—then you should use the `&nbsp;` escape code, as it makes the nonbreaking space visible and <span class="no-hyphens">explicit.</span>

<div class="btw">

<div class="btw-title">

by the way

</div>

- Why isn’t there a standard key shortcut for the nonbreaking space? Beats <span class="no-hyphens">me.</span>

- Unlike other white space in HTML, a sequence of nonbreaking spaces is not collapsed into a single word space. So theoretically, you can make larger spaces out of nonbreaking spaces. But as with any <a href="white-space-characters.html" class="xref">white-space characters</a>, this is bad policy—like fixing a flat tire with duct <span class="no-hyphens">tape.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="word-spaces.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="tabs-and-tab-stops.html" class="nav"></a>

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
