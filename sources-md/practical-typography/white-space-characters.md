---
title: "White Space Characters"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/white-space-characters.html"
---

<div id="content">

<div id="doc">

white-space charactersFor control and predictability

You’re now familiar with the essential alphabetic, numeric, and symbol characters. We turn to the frequently overlooked white-space characters—the keyboard characters that put blank space between point A and point <span class="no-hyphens">B.</span>

Why are they overlooked? For one thing, they’re invisible. As you learn to use white-space characters, you’ll find it helpful to make them visible. That way, you can verify that you’re typing them correctly and that they’re having the intended effect. Later, you’ll find it useful to see them while diagnosing formatting <span class="no-hyphens">problems.</span>

If I have to work on a document from an outside source, one of the first things I do is display white-space characters, to reveal lurking <span class="no-hyphens">horrors.</span>

<div class="howto">

<div class="howto-name">

How to display white-space characters

</div>

WordHome → Paragraph panel → ¶ button (or control + shift + <span class="no-hyphens">8)</span>

Mac OS Word¶ button (or ⌘ + <span class="no-hyphens">8)</span>

PagesView → Show Invisibles (or ⌘ + shift + <span class="no-hyphens">i)</span>

HTMLView the HTML source in an external text editor that can show invisible characters (the exact name of the command will <span class="no-hyphens">vary)</span>

</div>

There are six important white-space characters: the <a href="word-spaces.html" class="xref">word space</a>, the <a href="nonbreaking-spaces.html" class="xref">nonbreaking space</a>, the <a href="tabs-and-tab-stops.html" class="xref">tab</a>, the <a href="hard-line-breaks.html" class="xref">hard line break</a>, the <a href="carriage-returns.html" class="xref">carriage return</a>, and the <a href="hard-page-breaks.html" class="xref">hard page break</a>. Each white-space character has a distinct function. Use the right tool for the <span class="no-hyphens">job.</span>

“But if all white space looks the same when printed, why should I care?” Two reasons: *control* and *predictability*.

*Control* means you get the intended result with the fewest keystrokes. Suppose you need a paragraph to start at the top of the next page. What to do? If you use a hard page break rather than a sequence of carriage returns, you can get the job done with one <span class="no-hyphens">keystroke.</span>

*Predictability* means that as you edit and reformat, you’ll get consistent results. When you approximate a hard page break with carriage returns, your text will eventually reflow, and you’ll get a large gap where you intended a page break. Then you’ll have a new problem to diagnose and fix. But a hard page break will always do the right <span class="no-hyphens">thing.</span>

The time you invest in learning the white-space characters will be paid back in layouts that snap together faster and require less <span class="no-hyphens">fiddling.</span>

<div id="white-space-characters-in-html" class="subhead">

[White-space characters in HTML](#white-space-characters-in-html)

</div>

A word processor aims to simulate a printed layout, so each white-space character has a visible effect. An HTML document, by contrast, is a series of formatting tags. So white space is handled more like it would be in a programming language: except for nonbreaking spaces, any sequence of white space in HTML is collapsed to a single word space when the document is rendered in a browser. To achieve visible effects with white space, you need to use explicit HTML formatting <span class="no-hyphens">tags.</span>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="foot-and-inch-marks.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="word-spaces.html" class="nav"></a>

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
