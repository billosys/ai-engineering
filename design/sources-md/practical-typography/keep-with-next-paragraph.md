---
title: "Keep With Next Paragraph"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/keep-with-next-paragraph.html"
---

<div id="content">

<div id="doc">

keep with next paragraphAlways use with headings

Keep with next paragraph binds the last line of a paragraph to the first line of the next. It ensures no page break happens between the two paragraphs. It’s like <a href="keep-lines-together.html" class="xref">keep lines together</a>, except it works between paragraphs instead of within a <span class="no-hyphens">paragraph.</span>

Always use this option with <a href="headings.html" class="xref">headings</a>. It looks bad if a heading appears at the bottom of a page and the text it’s introducing starts on the next page. Keeping with the next paragraph prevents <span class="no-hyphens">this.</span>

The keep-with-next-paragraph option is a little boring on its own. It gets more interesting when used with its friend, the keep-lines-together option. For instance, I once had to prepare a jury-instruction form with many entries like <span class="no-hyphens">this:</span>

<div class="indented">

**<span class="font-feature-settings:case">CACI 204.</span> Willful suppression of evidence**  
\_\_\_\_\_ Given as proposed  
\_\_\_\_\_ Given as modified  
\_\_\_\_\_ Refused  
\_\_\_\_\_ Withdrawn

</div>

Here, the name of the jury instruction is one paragraph, and the four choices below are a second paragraph. The four choices won’t get separated from each other because they’re glued together with the keep-lines-together option. But we don’t want the instruction name getting separated from the choices either. By setting the instruction name to keep with next paragraph, all five lines will move as a <span class="no-hyphens">unit.</span>

<div class="howto">

<div class="howto-name">

How to keep with next paragraph

</div>

WordRight-click in the text and select Paragraph → Line and Page Breaks → check Keep with <span class="no-hyphens">next</span>

PagesView → Show Toolbar (or option + ⌘ + t) → Format button → More pane → check Keep with next <span class="no-hyphens">paragraph</span>

CSSNot <span class="no-hyphens">applicable</span>

</div>

<div class="btw">

<div class="btw-title">

by the way

</div>

- Why didn’t I make the whole block one paragraph? So I could apply a separate paragraph style to the names of the instructions, and reformat all of them as a group. (See <a href="paragraph-and-character-styles.html" class="xref">paragraph and character styles</a>.)

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="keep-lines-together.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="page-break-before.html" class="nav"></a>

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
