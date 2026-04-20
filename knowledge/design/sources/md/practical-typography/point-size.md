---
title: "Point Size"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/point-size.html"
---

<div id="content">

<div id="doc">

point sizeSmaller on paper; bigger on screen

In print, the optimal point size for <a href="body-text.html" class="xref">body text</a> is 10–12 point. On the web, the optimal size is 15–25 <span class="no-hyphens">pixels.</span>

<div id="point-size-in-print" class="subhead">

[Point size in print](#point-size-in-print)

</div>

Though 12 point has become the default size in digital word processing—and also the basis of many institutional document-formatting rules—that’s mostly due to the typewriter tradition. It’s not the most comfortable size for reading. Nearly every book, newspaper, and magazine is set smaller than 12 point. (One major reason is cost: bigger point sizes require more <span class="no-hyphens">paper.)</span>

There are 72 *points* to an inch. Word lets you specify point sizes in half-point increments. Pages allows finer increments of one-tenth of a point. CSS allows any size, but browsers will typically round to the nearest whole <span class="no-hyphens">point.</span>

If you’re not required to use 12 point, don’t. Try sizes down to 10 point, including intermediate sizes like 10.5 and 11.5 point—half-point differences are meaningful at this <span class="no-hyphens">scale.</span>

But I can’t guarantee 12 point will always look too big. That’s because the point-size system is not absolute—different fonts set at the same point size won’t necessarily appear the same on the <span class="no-hyphens">page.</span>

That means you need to let your eyes be the judge. Don’t just rely on the point size. For instance, the three fonts below—Sabon, <a href="times-new-roman-alternatives.html" class="xref">Times New Roman</a>, and Arno—are set at 12 point, but they’re not the same size <span class="no-hyphens">visually.</span>

You can match the length of two fonts by setting a block of text twice: once in the old font and once in the new font, both at the same point size. Adjust the point size of the new font until each line of text breaks in roughly the same place. (You won’t be able to match them exactly.) Below, the point sizes of Sabon and Arno have been adjusted so they occupy the same space as Times New <span class="no-hyphens">Roman.</span>

Point size can be even smaller in professionally typeset materials like publications and stationery. Text on <a href="business-cards.html" class="xref">business cards</a> is often only 6–8 points. At these sizes, <a href="all-caps.html" class="xref">all caps</a> text and lowercase are equally <span class="no-hyphens">legible.</span>

<div id="point-size-as-emphasis" class="subhead">

[Point size as emphasis](#point-size-as-emphasis)

</div>

It’s fine to emphasize text with a larger point size (or de-emphasize it with a smaller point size). But use the subtlety that point-size adjustments offer. If your body text is set at 11 point, no need to jump to 14 point for emphasis. Start with a smaller increase—say, half a point—and move up in half-point increments until you get the emphasis you need. It’ll be less than you think.

<div id="point-size-on-the-web" class="subhead">

[Point size on the web](#point-size-on-the-web)

</div>

You don’t have to use pixels as the sizing unit in your CSS (and indeed, most prefer not to). But the pixel is the least ambiguous CSS unit. Also, all CSS measurements are eventually converted to pixels in the <span class="no-hyphens">browser.</span>

For websites, I recommend body text of 15–25 pixels. As with print, you’ll need to fine-tune based on the particular font you’re <span class="no-hyphens">using.</span>

Why? Two reasons. First, we typically read screens from further away than we read printed material, so larger point sizes help compensate. Second, screen fonts are rendered with a relatively small number of pixels, so each extra row of pixels improves the quality. (See also <a href="screen-reading-considerations.html" class="xref">screen-reading considerations</a>.)

Yes, I know the web has a long tradition of teeny fonts. It’s time to let it go. This habit arose because the 14-inch monitors common in the 1990s had relatively coarse resolution. It persisted because web designers considered it virtuous to keep accommodating people who refused to upgrade those 14-inch monitors. But now, it’s merely <span class="no-hyphens">silly.</span>

Also silly is the web’s tradition of enormous point sizes for headings. This habit started with the default formatting of `<h1>` tags in browsers, which is about 200% of the default point size of body text. There is no typographic universe in which you need to double the point size to achieve emphasis. See <a href="headings.html" class="xref">headings</a> for subtler <span class="no-hyphens">techniques.</span>

For more about the entrenched typographic habits of the web, see <a href="websites.html" class="xref">websites</a>.

<div class="btw">

<div class="btw-title">

by the way

</div>

- In <a href="hyphens-and-dashes.html" class="xref">hyphens and dashes</a>, I mentioned that *em* refers to a typographer’s measurement, not the letter M. The em size of a font is the same as its point size. Fonts are no longer made of metal, but the em concept persists. Digital fonts are drawn inside a rectangle called the em. To render a font on screen, your computer scales the em to match the current point size. Two fonts set at the same point size will appear to be different sizes if one occupies less space on its <span class="no-hyphens">em.</span>

- Can you determine the point size of a font by measuring it? No. Because of the differences in apparent sizing between fonts, there’s nothing you can measure that would be conclusive. The only way to figure it out is to set the same text, in the same font, with the same <a href="line-length.html" class="xref">line length</a>. Then adjust the point size so it matches the reference <span class="no-hyphens">sample.</span>

- As you reduce point size, also reduce <a href="line-spacing.html" class="xref">line spacing</a> and <a href="line-length.html" class="xref">line length</a>. For instance, newspaper fonts are quite small, but remain legible because they have snug line spacing and short line <span class="no-hyphens">length.</span>

- Organizations that need to control the length of documents (e.g., courts, colleges) usually do so with limits on point size and page length. In the typewriter age, this worked because typewriter output was standardized. In the digital age, it makes less sense, since artful formatting and layout can make documents appear longer or shorter as necessary. Anyone who needs to set standards for document length would be better off putting these rules in terms of word count. Unlike typewriters, all word processors have a word-count function. Compared to page limits, word counts are harder to evade. To be fair, they’re also harder to <span class="no-hyphens">verify.</span>

- In 2012, a dispute about [point size](http://online.wsj.com/article/SB10000872396390444840104577549202116809114.html) reached the Michigan Supreme Court. One side argued—contrary to 400 years of typographic custom—that a law calling for “14-point type” on a ballot meant that the uppercase letters of the font had to be at least 14 points tall. Fortunately the court did not adopt this interpretation. As a matter of law, it would’ve redefined the meaning of point size within <span class="no-hyphens">Michigan.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="all-caps.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="headings.html" class="nav"></a>

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
