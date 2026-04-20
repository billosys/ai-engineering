---
title: "Hierarchical Headings"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/hierarchical-headings.html"
---

<div id="content">

<div id="doc">

hierarchical headingsConsider tiered numbers

Traditionally, hierarchical headings start with roman numerals at the top level (I, II, III); then switch to capital letters (A, B, C); then numerals (1, 2, 3); then lowercase letters (a, b, c); then romanettes (i, ii, iii); and then variations of the above using two parentheses instead of one, or other barely visible <span class="no-hyphens">changes.</span>

This is a terrible way to label hierarchical <span class="no-hyphens">headings.</span>

1.  Yes, that’s what they’re called—romanettes.

    Roman numerals and romanettes stink. They’re difficult to read. (Quick, what number is XLIX?) They’re easy to confuse at a glance. (II vs. III, IV vs. VI, XXI vs. XII.) If what we mean by I, II, III is 1, 2, 3, then let’s just say <span class="no-hyphens">so.</span>

2.  Letters aren’t much better. Though we immediately recognize A, B, C as equivalent to 1, 2, 3, the letter-to-number correlation gets weaker as we go past F, G, H. (Quick, what number is T?) If what we mean by J, K, L is 10, 11, 12, then let’s just say <span class="no-hyphens">so.</span>

3.  Mixing roman numerals and letters results in ambiguous references—when you see a lowercase *i*, does it denote the first item or the ninth item? Does a lowercase *v* denote the fifth item or the 22nd <span class="no-hyphens">item?</span>

4.  By using only one index on each header, it’s easy to lose track of where you are in the hierarchy. If I’m at subheading *d*, is that *d* under superheading 2 or <span class="no-hyphens">3?</span>

If you need to write a document with hierarchical headings, take a cue from technical writers, who solved this problem long ago—by using tiered numbers as indexes for hierarchical <span class="no-hyphens">headings.</span>

So instead <span class="no-hyphens">of:</span>

<div style="margin-right:4rem">

<div class="indented">

</div>

</div>

You’d <span class="no-hyphens">have:</span>

<div style="margin-right:4rem">

<div class="indented">

</div>

</div>

To my eyes, this system is more understandable—because it only uses numbers, it avoids ambiguity or miscues. It’s also more navigable—because every tiered number is unique, it’s always clear where you are in the hierarchy. And every word processor can automatically produce tiered numbering. Consider <span class="no-hyphens">it.</span>

<div class="btw">

<div class="btw-title">

by the way

</div>

- CSS will produce numbered headings by default if you use the `<ol>` (ordered list) tag, but tiered numbers require a little extra work—investigate the `counter-increment` <span class="no-hyphens">property.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="small-caps.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="mixing-fonts.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="text-formatting.html" class="box-link">chapter</a>

</div>

</div>

</div>
