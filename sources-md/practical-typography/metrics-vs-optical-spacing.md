---
title: "Metrics Vs Optical Spacing"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/metrics-vs-optical-spacing.html"
---

<div id="content">

<div id="doc">

metrics vs. optical spacingMetrics always; optical for emergencies

If you use Adobe InDesign—and if you don’t, you can ignore this page—you might have noticed the popup menu that gives you a choice between “metrics” and “optical” font <span class="no-hyphens">spacing.</span>

Despite the benign-sounding name, optical spacing will mangle your font. It is akin to putting your finest cashmere sweater in the washing machine. So always use the “metrics” <span class="no-hyphens">option.</span>

This setting controls the way InDesign lays out your <span class="no-hyphens">type:</span>

- *Metrics spacing* relies on the character-spacing information inside the font—that is, the information about character widths and <a href="kerning.html" class="xref">kerning</a> pairs that the font designer put there. When you use metrics spacing, you’re seeing the font the way the designer <span class="no-hyphens">intended.</span>

- *Optical spacing* completely junks all this character-spacing information. Instead, it applies a [patented spacing algorithm](https://patents.google.com/patent/US5803629) that guesses what the width and kerning of every character should be. To no one’s surprise, it often guesses <span class="no-hyphens">wrong.</span>

In this type designer’s opinion, the spacing of a font—that is, the design of the white spaces—is far more consequential to its appearance than the design of the black shapes. If you buy a professional font (see <a href="font-recommendations.html" class="xref">font recommendations</a>), and then run it through the optical-spacing wringer, you’re throwing away most of what you paid <span class="no-hyphens">for.</span>

Still, don’t take my word for it. Compare these samples, showing with metrics spacing on top, and optical spacing on the <span class="no-hyphens">bottom:</span>

<div class="gap" style="height:1em">

</div>

- In metrics spacing, the spaces between *nu* and *un* are visually balanced. But in optical spacing, the *u* is pushed to the left, so *nu* looks tighter than *un*.

- In metrics spacing, the spaces between *un* and *no* are visually balanced. But in optical spacing, the *o* (and all rounded letters) are squished closer to flat letters like *n*.

- In metrics spacing, the *t* has the space it needs on the left, so that a combo like *ntit* looks even. In optical spacing, the space within *nt* and *it* shrinks, becoming darker than the *ti* <span class="no-hyphens">space.</span>

- “The optical-spacing row on the bottom looks OK to me.” I’ve enlarged these 11 letters to convince you that spacing differences exist. But yes, in a headline, these differences are less bothersome, because there’s still plenty of space between each pair. The real problem arises when you return to ordinary <a href="point-size.html" class="xref">point size</a>. These asymmetries accumulate across hundreds of letter pairs, resulting in <a href="body-text.html" class="xref">body text</a> that’s jittery and <span class="no-hyphens">uneven.</span>

The goal of spacing letters in a font is to give typeset text an even color, minimizing dark and light spots. Optical spacing does well enough with letters that are symmetric—say, an uppercase *H* or lowercase *n*.

But those are easy. As we can see above, achieving the same evenness is harder with asymmetric letters like lowercase *a* or *r* or *t*. But it’s also vital, because these letters occur so frequently in text. This is why humans outperform the machine on font <span class="no-hyphens">spacing.</span>

“So what is optical spacing good for?” Optical is the emergency option if you find yourself working <span class="no-hyphens">with:</span>

1.  A font that has bad spacing (for instance, the client has insisted on such-and-such <a href="free-fonts.html" class="xref">free font</a>) <span class="no-hyphens">or;</span>

2.  A font that’s being pressed into service beyond its designed capacity (for instance, a body-text font being used for a <span class="no-hyphens">headline).</span>

If such an emergency arises, break the glass. Try optical spacing. Judge with your eyes whether it <span class="no-hyphens">helps.</span>

Otherwise—metrics.

<div class="btw">

<div class="btw-title">

by the way

</div>

- Why do these spacing differences matter more at small point sizes than large? Our eyes perceive light and dark differently as type reaches the lower limit of our ability to detect visual detail. See <a href="screen-reading-considerations.html" class="xref">screen-reading considerations</a>.

- Abuse of optical spacing is especially pronounced among American book designers. Magazine and newspaper designers tend to use metrics spacing. But this isn’t surprising—books have smaller design budgets, most of which is spent on the cover, not the <span class="no-hyphens">interior.</span>

- I’ve tried to track down, so far fruitlessly, the origin of the “optical spacing is better” cargo cult. For instance, was there a popular graphic-design book that first propagated the urban legend, which then became entrenched? (One graphic-designer colleague theorized that Adobe trainers spread the myth.) <a href="contact.html" class="xref">Contact</a> me if you have clues to <span class="no-hyphens">share.</span>

- Still, I blame Adobe for coining the misleading names “metrics spacing” and “optical spacing” in the first place. If these options had been named accurately—e.g., “original spacing” and “synthetic spacing”, or “nice spacing” and “shitty spacing”—InDesign users would likely have made better <span class="no-hyphens">choices.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="opentype-features.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="font-recommendations.html" class="nav"></a>

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
