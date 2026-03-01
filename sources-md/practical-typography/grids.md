---
title: "Grids"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/grids.html"
---

<div id="content">

<div id="doc">

gridsA guide, not a panacea

A *grid* is a system of horizontal and vertical lines that can guide layout choices. Grids have been part of page layout since the Gutenberg Bible. The pages below use a grid of four vertical and two horizontal <span class="no-hyphens">lines.</span>

In moderation, grids can be useful. But in the words of Dutch designer Wim Crouwel, “The grid is like the lines on a football field. You can play a great game in the grid or a lousy game.” The grid might be the starting point. But the eye must always be the final <span class="no-hyphens">judge.</span>

Grids are helpful when they encourage consistency. They make it easier to relate elements on the page to existing ones (a principle suggested in <a href="maxims-of-page-layout.html" class="xref">maxims of page layout</a>). If your layout seems messy or aimless, move elements onto the <span class="no-hyphens">grid.</span>

Grids are not helpful when they create a false sense of security—*I aligned everything to my grid, therefore my layout is solid.* For instance, a few years ago, web designers were fixated on the [960 grid system.](https://960.gs/) If it got people curious about grids, OK. But it also proved that if you take ugly shit and align it to a grid—it’s still ugly <span class="no-hyphens">shit.</span>

A few tips for using grids <span class="no-hyphens">effectively:</span>

1.  Grids can guide positioning (= where an element goes on a page), sizing (= the height and width of an element), or alignment (= how two elements relate to each other). Grids can apply to visible elements (say, a text block) and invisible ones (say, <a href="page-margins.html" class="xref">page margins</a>, <a href="space-between-paragraphs.html" class="xref">space between paragraphs</a>, or <a href="first-line-indents.html" class="xref">first-line indents</a>).

2.  A coarser, simpler grid encourages more consistency, because there are fewer ways to align items. A complicated grid, by contrast, might as well be no grid at <span class="no-hyphens">all.</span>

3.  Grids don’t have to be rigid or symmetric—in fact it’s usually better if they’re not. For instance, in the Gutenberg spread above, the columns of text are the same height and width. But the margins within each page are all <span class="no-hyphens">different.</span>

    Corollary: if you want to use mathematical ratios to set up your grid, fine. But these ratios don’t guarantee a good layout on their own. Rely on your eyes, not your <span class="no-hyphens">calculator.</span>

4.  A grid can emerge from experimentation rather than being defined in advance. For instance, all the <a href="sample-documents.html" class="xref">sample documents</a> are built around simple grids. This is a consequence of organizing elements more consistently. But I don’t emphasize the grid-ness because I want readers to focus on typographic consistency (which is the end goal), not grids per se (which are merely a means to that <span class="no-hyphens">end).</span>

5.  Because I like web layouts that scale, I often start with a grid of `1rem` (tied to the viewport with a media query) or `1vw`.

    Not everything needs to go on the grid. For instance, with print or PDF projects, I often start with a pica grid (one pica = 12 pts). I use this to derive a coarser grid that controls the position and size of the text blocks. But if it turns out that a certain set of indents look right at 2.5 picas, I’m not going to freak <span class="no-hyphens">out.</span>

<div class="btw">

<div class="btw-title">

by the way

</div>

- A baseline grid is a special grid that restricts where the baseline of a line of text can appear. These grids are typically used in wide multi-column layouts (imagine a newspaper page) where uneven baselines would be distracting. In book or website layouts, however, I think baseline grids impose too much rigidity (and too much work) for too little benefit. I don’t use <span class="no-hyphens">them.</span>

- Fans of mathematical ratios in grids (also known as modular scales) sometimes compare them to music. For instance, Robert Bringhurst says “a modular scale, like a musical scale, is a prearranged set of harmonious proportions”. (*The Elements of Typographic Style*, <span class="no-hyphens">p. 166.)</span>

  As a musician, I find this metaphor incomplete. Sure, music is written on a grid of harmony and rhythm. But performers don’t rigidly adhere to these grids. Indeed, music that was locked perfectly to a grid would sound sterile and boring. Just as the performer’s ear is the ultimate judge of the music, the typographer’s eye is the ultimate judge of the <span class="no-hyphens">page.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="columns.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="paragraph-and-character-styles.html" class="nav"></a>

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
