---
title: "Optional Hyphens"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/optional-hyphens.html"
---

<div id="content">

<div id="doc">

optional hyphensMark a hyphenation location

The optional hyphen, also known as the soft hyphen, is usually invisible. The optional hyphen marks where a word should be hyphenated if the word lands at the end of a line. You can put multiple optional hyphens in a <span class="no-hyphens">word.</span>

Why would you want to do this? Some words bedevil hyphenation engines. For instance, TrueType will often get hyphenated as Tru-  
eType, as in the example below, from a rival typography <span class="no-hyphens">book:</span>

To prevent this, I put an optional hyphen in the middle (True~Type). Then it will be hyphenated <span class="no-hyphens">correctly.</span>

How do you know if a word won’t be hyphenated correctly? The problem usually afflicts words that aren’t in a standard hyphenation dictionary, like jargon words, unusual proper names, and words with nonstandard spellings, like trade names. As Justice [Potter Stewart](http://en.wikipedia.org/wiki/I_know_it_when_I_see_it) might have said, you’ll know it when you see <span class="no-hyphens">it.</span>

<div class="howto">

<div class="howto-name">

How to insert an optional hyphen

</div>

WordInsert → Symbols panel → Symbol → More Symbols → Special Characters → Optional <span class="no-hyphens">Hyphen</span>

Mac OS WordInsert menu → Advanced Symbol → Special Characters → Optional <span class="no-hyphens">Hyphen</span>

PagesEdit menu → Emoji & Symbols → Punctuation → Soft <span class="no-hyphens">Hyphen</span>

HTML`` (that’s `s` for soft, `hy` for <span class="no-hyphens">hyphen)</span>

</div>

<div class="btw">

<div class="btw-title">

by the way

</div>

- Even though you type a key to insert an optional hyphen, you won’t see it until it’s needed. And obviously, if your automatic hyphenation is turned off, you’ll never see <span class="no-hyphens">it.</span>

- For the <a href="hyphenation.html" class="xref">hyphenation</a> in this book, I used [Frank Liang’s hyphenation algorithm](http://tug.org/interviews/liang.pdf) to insert optional hyphens when each page is generated. (I’ve [released this code](http://github.com/mbutterick/hyphenate) as an open-source hyphenation module for Racket.) Though CSS notionally supports hyphenation with the `hyphen` property, it’s [not supported as well](http://caniuse.com/#search=hyphen) as the optional <span class="no-hyphens">hyphen.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="hard-page-breaks.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="math-symbols.html" class="nav"></a>

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
