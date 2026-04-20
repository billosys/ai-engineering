---
title: "Responsive Web Design"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/responsive-web-design.html"
---

<div id="content">

<div id="doc">

Responsive web design

Responsive web design is a technique that allows web layouts to reflow to suit the scale and dimensions of the user’s screen (or *viewport*, in CSS <span class="no-hyphens">parlance).</span>

In this way, rather than trying to confect a one-size-fits-all layout, a web designer can specify changes for small screens (e.g. tall-format mobile phones) and large screens (e.g., wide-format desktop screens), and sizes in between. For instance, responsive design is used on many sites (including this one) to collapse a multi-column layout into a single column for mobile <span class="no-hyphens">devices.</span>

So many viewports, so little <span class="no-hyphens">time.</span>

A reasonable idea, as far as it goes. But in practice, designers hoping to solve their screen-size problem with responsive web design have discovered that they now have two <span class="no-hyphens">problems.</span>

The main challenge, of course, is getting the typography right. Early in the responsive web era, it was common to see layouts with navigation and images carefully engineered to scale up and down with the screen size. Meanwhile, the <a href="body-text.html" class="xref">body text</a> was largely ignored—set at a fixed <a href="point-size.html" class="xref">point size</a>, and allowed to reflow from edge to edge, regardless of the screen width. Not <span class="no-hyphens">good.</span>

Therefore, for those embarking on a responsive-design project, one key reminder: **the rules of good typography don’t change with screen size**.

In <a href="page-margins.html" class="xref">page margins</a>, I said that one shouldn’t treat the edges of a piece of paper as the boundaries of the text block. Likewise in responsive web design—the edges of the screen are not the end. Just the <span class="no-hyphens">beginning.</span>

1.  Start by considering <a href="line-length.html" class="xref">line length</a>, because it’s the hardest to manage in a responsive layout. Regardless of screen width, the optimal line length is still 45-90 characters. As you test your layout, make sure that text elements stay within this <span class="no-hyphens">range.</span>

2.  The easiest way to maintain consistent line length is by scaling the <a href="point-size.html" class="xref">point size</a> and element width at the same rate. These days, this is especially easy thanks to the `vw` unit in CSS, which lets you specify measurements as a fraction of the current viewport <span class="no-hyphens">width.</span>

    What about the `ch` unit in CSS, which supposedly corresponds to character width? Skip it. Contrary to the name, it simply denotes the [width of the zero](https://drafts.csswg.org/css-values-3/#ch) in the font. No, the zero’s width is [not a useful proxy](https://matthewbutterick.com/chron/the-comparative-copyfitting-factor.html) for average characters per <span class="no-hyphens">line.</span>

3.  Or, if you want text to reflow inside a layout element, include a `max-width` CSS property on that element to ensure that the line length is bounded. As above, the `vw` unit is your <span class="no-hyphens">friend.</span>

4.  Be careful tying mobile layouts to [CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries) based on pixel width. As mobile phones have gotten bigger, many sites are setting this threshold higher. (I’ve seen it as high as 1400 pixels.) The problem is that this causes the mobile layout to show up even in reasonably sized desktop browser <span class="no-hyphens">windows.</span>

    Unfortunately, CSS media queries can’t distinguish desktop from mobile devices. If you really want to serve a mobile layout to large mobile devices, consider using JavaScript rather than media queries to detect mobile vs. desktop and load an appropriate <span class="no-hyphens">stylesheet.</span>

This last suggestion will cause certain responsive-design purists to squeal in horror. But due to differences in reading distance, a pixel on a desktop display and a pixel on a mobile screen are not the same. See <a href="screen-reading-considerations.html" class="xref">screen-reading considerations</a>.

<div class="btw">

<div class="btw-title">

by the way

</div>

- Starting in 2004, a number of web designers proposed the idea of responsive web design, including [Cameron Adams](http://www.themaninblue.com/experiment/ResolutionLayout/) and [Marc van den Dobbelsteen](https://alistapart.com/article/switchymclayout) (who dubbed the technique “Switchy McLayout”). But the technique didn’t take off until around 2010, when browser support for [CSS media queries](https://caniuse.com/#feat=css-mediaqueries)—the key mechanism for specifying layout changes—became <span class="no-hyphens">widespread.</span>

- On this site, I use JavaScript to serve different weights of the body-text font to devices based on their typical rasterization characteristics. For instance, Windows users get a slightly heavier version than Mac users, to account for lighter screen <span class="no-hyphens">rasterization.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="screen-reading-considerations.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="how-to-work-with-a-designer.html" class="nav"></a>

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
