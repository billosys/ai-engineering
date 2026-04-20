---
title: "Small Caps"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/small-caps.html"
---

<div id="content">

<div id="doc">

small capsUse real small caps; avoid fakes

Small caps are short capital letters designed to blend with lowercase text. They’re usually slightly taller than lowercase letters. <span class="no-hyphens"></span>

I’m a big fan of small caps. They look great and they’re very useful as an alternative to <a href="bold-or-italic.html" class="xref">bold or italic</a> or <a href="all-caps.html" class="xref">all caps</a>.

But most people have never seen real small caps. They’ve only seen the ersatz small caps that word processors and web browsers generate when small-cap formatting is <span class="no-hyphens">used.</span>

<table class="example">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="font-size: 190%"><span class="fake-small-caps"><span>W</span><span class="shrink"><span>itness</span></span><span> P</span><span class="shrink"><span>rotection</span></span></span></td>
<td>fake</td>
</tr>
<tr>
<td style="font-size: 190%"><span class="real-small-caps"><span>Witness Protection</span></span></td>
<td>real</td>
</tr>
<tr>
<td style="font-size: 190%"><div style="font-size:60%;font-family:equity-text">
<span>Trixie Argon, </span><em><span>Ways to Be Wicked</span></em><span>, in</span><br />
<span class="fake-small-caps"><span>C</span><span class="shrink"><span>onjuring</span></span><span> </span><span class="shrink"><span>for</span></span><span> B</span><span class="shrink"><span>eginners</span></span></span><span>, at 137–39</span><br />
<span>(London, Quid Pro Books, 2004).</span>
</div></td>
<td>fake</td>
</tr>
<tr>
<td style="font-size: 190%"><div style="font-size:60%;font-family:equity-text">
<span>Trixie Argon, </span><em><span>Ways to Be Wicked</span></em><span>, in</span><br />
<span class="real-small-caps"><span>Conjuring for Beginners</span></span><span>, at 137–39</span><br />
<span>(London, Quid Pro Books, 2004).</span>
</div></td>
<td>real</td>
</tr>
</tbody>
</table>

Typographers use the word <a href="color.html" class="xref">color</a> to refer to how light or dark a text block appears on a page (even if all the characters are <span class="no-hyphens">black).</span>

Small-cap formatting works by scaling down regular caps. But compared to the other characters in the font, the fake small caps that result are too tall, and their vertical strokes are too light. The <a href="color.html" class="xref">color</a> and height of real small caps have been calibrated to blend well with the normal uppercase and lowercase <span class="no-hyphens">letters.</span>

Therefore, two rules for small <span class="no-hyphens">caps:</span>

1.  Don’t click on the small-cap formatting box in your word processor. Ever. This option does not produce small caps. It produces inferior counterfeits. (Even when you’re using a font with real small <span class="no-hyphens">caps.)</span>

2.  The rules for <a href="all-caps.html" class="xref">all caps</a> also apply to small caps: use small caps sparingly, add <a href="letterspacing.html" class="xref">letterspacing</a>, and turn on <a href="kerning.html" class="xref">kerning</a>.

Now for the bad news. If you want real small caps, you’ll have to buy them—they’re not included with <a href="times-new-roman-alternatives.html" class="xref">Times New Roman</a> or any other <a href="system-fonts.html" class="xref">system font</a>.

Sometimes, small caps come in their own font file that shows up separately in the font menu. When you want small caps, you format the text with the small-cap font. Other times, small caps are included in the main font file as an <a href="opentype-features.html" class="xref">OpenType feature</a> (named `smcp`). But either way, you can also use <a href="paragraph-and-character-styles.html" class="xref">paragraph and character styles</a> to apply small caps, and eliminate the tedium of finding <span class="no-hyphens">them.</span>

<div class="btw">

<div class="btw-title">

by the way

</div>

- With small caps, it’s up to you whether to use regular capital letters at the beginning of capitalized words. I prefer not <span class="no-hyphens">to.</span>

- I deliver my fonts (see <a href="mb-fonts.html" class="xref">mb fonts</a>) with separate sets of small-caps fonts with the letterspacing already baked in. This saves labor. It also allows you to get properly spaced small caps in any program, even those that don’t support OpenType features or letterspacing. (Including web browsers—see <a href="letterspacing.html" class="xref">letterspacing</a> for <span class="no-hyphens">more.)</span>

- After years in the wilderness, the CSS property `font-variant: small-caps` is now [safe to use.](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-caps) By default, it will access the OpenType small caps in the font—if they exist. Otherwise, you’ll get the same old inferior <span class="no-hyphens">counterfeits.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="emails.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="hierarchical-headings.html" class="nav"></a>

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
