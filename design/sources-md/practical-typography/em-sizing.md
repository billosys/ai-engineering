---
title: "Em Sizing"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/em-sizing.html"
---

<div id="content">

<div id="doc">

<div style="display:none">

Em sizing

</div>

<div class="qa">

Why can’t we directly measure the point size of a printed <span class="no-hyphens">font?</span>

Em <span class="no-hyphens">sizing.</span>

</div>

Some typography concepts have evolved in response to changes in technology. For instance, in the digital age, a <a href="carriage-returns.html" class="xref">carriage return</a> gets inserted at the end of a paragraph, whereas on a typewriter it was used at the end of a line. And today, the word font has largely absorbed the traditional meaning of typeface.

the em on a piece of metal <span class="no-hyphens">type</span>

But other concepts have been surprisingly durable, like the em. In <a href="hyphens-and-dashes.html" class="xref">hyphens and dashes</a>, I mentioned that the word em denotes a typographer’s measurement, not the letter M. The em size of a font is the same as its <a href="point-size.html" class="xref">point size</a>. This was true for hundreds of years of metal <span class="no-hyphens">type.</span>

It’s remained true in the digital era. Today, the em is implemented in software rather than metal. But it still represents the same thing: the maximum vertical size of the letters in the font. Then and now, two fonts set at the same point size will appear to be different sizes if one occupies less space on its <span class="no-hyphens">em.</span>

“But why not just make the point size equal to something specific, like the height of the capital H?” Not a bad idea, but since fonts vary widely in their design, there’s no character you could pick that would always be consistent. Nor can you simply scale everything to fit the em—it’s clear from the illustration above that if the capital H occupied the whole em, descending letters (like g j p q y) wouldn’t <span class="no-hyphens">fit.</span>

Instead, by relying on maximum size, the em-sizing system can be applied to any font. This ends up being a useful convention for automated typesetting. But as you learned in the previous section, it’s also why you can’t determine the point size of a font by measuring it <span class="no-hyphens">directly.</span>

If you think that’s merely nerdy trivia, you’d be wrong. A [2012 case](http://typo.la/mscd) in the Michigan Supreme Court turned largely on the meaning of point size. Michigan state law requires certain ballot measures to be “printed in capital letters in 14-point boldfaced type”. One citizen’s group had collected enough signatures to put their measure on the ballot, setting their font to 14 point in the usual way. But a second group challenged the validity of the measure, arguing that the 14-point requirement applied to the size of the “capital letters”, not the “type”, and thus the ballot measure had not been printed large <span class="no-hyphens">enough.</span>

As a typographer, it was clear that this case should’ve been resolved swiftly. Point size has had a consistent meaning for hundreds of years. It’s never had anything to do with the size of capital <span class="no-hyphens">letters.</span>

Moreover, as a lawyer, it was clear that if this fact weren’t automatically clear from the plain meaning, it could’ve been established by citation to authority (this book is just one of many options), expert testimony, or even good old judicial notice. What was left to argue <span class="no-hyphens">about?</span>

A lot, apparently. The appeals court ruled that “14 point” mandated the size of the capital letters, not the overall type. Fortunately the Michigan Supreme Court reversed this decision—adopting the correct definition of point size—though the [vote was alarmingly <span class="no-hyphens">close.</span>](http://typo.la/mscd)

Why alarming? None of the justices seemed alert to the potential consequences of Michigan’s highest court redefining point size as a matter of law. Had it done so, point size would have meant something different in Michigan than it does elsewhere. It would have been like the court saying “π is such a long number—we hereby order it to be <span class="no-hyphens">3.”</span>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="identifying-fonts.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="bibliography.html" class="nav"></a>

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
