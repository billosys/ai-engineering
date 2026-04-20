---
title: "Screen Reading Considerations"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/screen-reading-considerations.html"
---

<div id="content">

<div id="doc">

<div style="display:none">

Screen-reading considerations

</div>

<div class="qa">

How does screen reading affect typographic <span class="no-hyphens">choices?</span>

Less and <span class="no-hyphens">less.</span>

</div>

Over the last 30 years, the quintessential problem of digital typography has been how to make fonts look good not only on high-end publishing equipment, but also coarser devices like laser printers and personal-computer <span class="no-hyphens">screens.</span>

These days, the hardware differences between these devices have largely disappeared. Thus, with screens becoming more paper-like than ever, there’s declining need to make special accommodations for screen <span class="no-hyphens">reading.</span>

<div id="how-digital-type-works" class="subhead">

[How digital type works](#how-digital-type-works)

</div>

Whether it’s displayed on screen or printed, the computer draws a digital letterform the same way: by scaling a glyph shape to a certain size and activating the pixels that are inside the shape. Thus, the quality of rendered digital type depends on two factors: <span class="no-hyphens"></span>

1.  The number of pixels available (known as *resolution*, usually measured in dots per <span class="no-hyphens">inch)</span>

2.  The number of colors each pixel can display (known as *color depth*, measured in possible colors per <span class="no-hyphens">pixel).</span>

When filling a digital letterform, the darkness of each pixel is determined by how much of its area falls within the letter. From Beat Stamm, [Raster <span class="no-hyphens">Tragedy</span>](http://rastertragedy.com/)

If we assume we can see a pixel that’s one arcminute wide, the calculation of pixels per inch visible at a certain distance is equal to the number of arcminutes that fit into an inch at that <span class="no-hyphens">radius.</span>

So for a screen 24″ away, we divide the number of arcminutes in a circle (360 × 60 = 21600) by the circumference at radius 24″ (2π × 24″ = 150.80″). Then 21600 / 150.80″ = <span class="no-hyphens">143.24.</span>

But more pixels aren’t always better. At the high end, all reading is constrained by the physiology of the human eye. The eye’s limit of perceivable detail is usually estimated to be 1–2 arcminutes. (An arcminute is 1/60th of an angular degree in the field of vision.) Therefore, pixels smaller than one arcminute are superfluous, because we can’t resolve differences that <span class="no-hyphens">small.</span>

Because this limit is an angular measure, perceivable detail varies in direct proportion to reading distance. For instance, my desktop monitor is about 24″ away, which means I can see about 143 dots per inch. But on a tablet or phone held at 12″, I can see twice that, or 286 dots per inch (which becomes four times as many pixels per unit of area).

<div id="a-short-history-of-display-hardware" class="subhead">

[A short history of display hardware](#a-short-history-of-display-hardware)

</div>

For the first 20 years of digital typography, computer screens barely improved. They were stuck—yuck—in the range of 75 dots per inch. During that time, companies like Apple, Microsoft, and Adobe developed technologies that were meant to make digital fonts look better on screen. During the desktop-publishing era of the late ’80s, the big jump was from *bitmap* fonts (which only look good at one certain size) to *outline* fonts (which can be scaled to any size). Still, screen typography was mostly an <span class="no-hyphens">afterthought.</span>

The project of improving screen type became more urgent with the advent of the web. Some of the best-known fonts emerging from these efforts were Microsoft’s Verdana, Georgia, and Calibri, all of which were heavily optimized for screen reading. At the turn of this century, it was true that certain fonts looked better on screen, and others looked better in print. These fonts became the starting point for those designing onscreen <span class="no-hyphens">typography.</span>

But since 2010, screen hardware has been making up for lost time. High-resolution screens first emerged in smartphones, then spread to tablets, laptops, and now desktops. For instance, my smartphone display has a resolution of 326 dots per inch, and my desktop monitors have a resolution of 185 dots per inch, both of which exceed the limits of human vision. (By the way, if you haven’t upgraded to a 4K desktop monitor, it’s well worth it. See <a href="the-infinite-pixel-screen.html" class="xref">the infinite-pixel screen</a>.)

<div id="what-does-this-mean-for-screen-typography" class="subhead">

[What does this mean for screen typography?](#what-does-this-mean-for-screen-typography)

</div>

See also <a href="georgia-alternatives.html" class="xref">Georgia alternatives</a> and <a href="calibri-alternatives.html" class="xref">Calibri alternatives</a>.

For font choice, it means you should use whatever font you’d prefer on the printed page. Those traditional “screen-optimized fonts” of the ’90s were optimized for screens of what we will soon consider a more primitive era. Fonts like Georgia and Calibri have no special legibility benefit on today’s screens. (Like all <a href="system-fonts.html" class="xref">system fonts</a>, they still have the benefit of being installed on nearly every computer, however, so they’re still useful for sharing draft documents with <span class="no-hyphens">colleagues.)</span>

As for <a href="page-layout.html" class="xref">page layout</a>, most screens are smaller in height and width than the traditional 8.5″ × 11″ printed page. So if you’re certain that a document will only be read on screen, it could make sense to shrink the <a href="page-margins.html" class="xref">page margins</a> and raise the <a href="point-size.html" class="xref">point size</a> to adjust for this difference. But if a document could also be printed—most downloadable PDFs would fall into this category—then it’s best to stick with a print-optimized <span class="no-hyphens">layout.</span>

<div class="btw">

<div class="btw-title">

by the way

</div>

- The definitive article on this subject is Beat Stamm’s [*Raster Tragedy*,](http://rastertragedy.com/) which has been updated steadily since its original release in 1997. Perfect for those still in the hunt for their ultimate font-nerd <span class="no-hyphens">badge.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="bibliography.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="responsive-web-design.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="appendix.html" class="box-link">chapter</a>

</div>

</div>

</div>
