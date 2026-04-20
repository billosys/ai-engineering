---
title: "Carriage Returns"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/carriage-returns.html"
---

<div id="content">

<div id="doc">

carriage returnsOnly when you want a new paragraph

On manual typewriters, the carriage was the part on top that held the paper and scooted leftward as you typed. At the end of each line, you’d push a lever to move the carriage to the beginning of the next line. On electric typewriters, this lever became the carriage return key, which you’d press at the end of each <span class="no-hyphens">line.</span>

The terminology has stayed with us, but on a word processor, you only use a carriage return to start a new paragraph. (In HTML, you use a formatting tag to denote a paragraph—a carriage return has no visible <span class="no-hyphens">effect.)</span>

|                 | Word   | Pages  | HTML         |
|-----------------|--------|--------|--------------|
| carriage return | return | return | `<p> … </p>` |

It’s fine to use multiple carriage returns to add vertical space in <a href="emails.html" class="xref">emails</a> because there’s no  
other way to do <span class="no-hyphens">it.</span>

As with the <a href="word-spaces.html" class="xref">word space</a>, use only one carriage return at a time. It’s common to see multiple carriage returns used to add vertical space between paragraphs. Bad idea. If you want vertical space after a paragraph, use <a href="space-between-paragraphs.html" class="xref">space between paragraphs</a>.

“But it’s so much easier to type two carriage returns.” I know. But in long, structured documents, extra carriage returns create unpredictable consequences as the document is edited. Whatever time you save with the shortcut will cost you <span class="no-hyphens">later.</span>

What if you get a document that’s already littered with double carriage returns? Search-and-replace works with <a href="white-space-characters.html" class="xref">white-space characters</a> <span class="no-hyphens">too.</span>

If the document has triple carriage returns or worse, you’ll have to run this replacement routine multiple times to eradicate them <span class="no-hyphens">all.</span>

<div class="howto">

<div class="howto-name">

How to replace double carriage returns

</div>

WordFind and Replace → Replace → More. Use the Special menu to put two Paragraph Marks in the Find what box, and one Paragraph Mark in the Replace with box. (Careful: you don’t want the Paragraph Character, which denotes the literal ¶ symbol.) Click Replace All.

Mac OS WordEdit → Find → Advanced Find and Replace → Replace → click triangle-shaped box in lower left to reveal the Special menu, and then continue as described <span class="no-hyphens">above.</span>

PagesOpen the Find panel (either Edit → Find → Find... or ⌘ + f). In the first box, type `\n\n`, and in the second, type `\n`. (`\n` is a special code representing one carriage return; `\n\n` represents two.) Click the right-pointing arrow in the lower right of the Find panel. Click Replace All.

</div>

<div class="btw">

<div class="btw-title">

by the way

</div>

- A common nonsense objection to <a href="one-space-between-sentences.html" class="xref">one space between sentences</a> is “muscle memory”: roughly, *I learned to type on a typewriter using two spaces, and my habit is too strong to change*. Of course, these same people successfully changed their habit of typing a carriage return after each line, as typewriters required, to only typing one after a paragraph. <span class="no-hyphens">Whatever.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="hard-line-breaks.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="hard-page-breaks.html" class="nav"></a>

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
