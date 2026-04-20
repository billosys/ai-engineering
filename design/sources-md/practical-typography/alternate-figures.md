---
title: "Alternate Figures"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/alternate-figures.html"
---

<div id="content">

<div id="doc">

alternate figuresConsider the context

Though we think of a font as a set of characters with a uniform visual appearance, the genesis of these characters is anything but uniform. Our writing system brings together characters that were originally handwritten by people in different countries, in different centuries. To achieve a uniform appearance, a type designer has to harmonize these disparate <span class="no-hyphens">forms.</span>

I can’t explain why typographers adopted the term figures rather than the perfectly good numerals. But that’s how it <span class="no-hyphens">is.</span>

Our uppercase alphabet came from the inscriptional capitals of the Romans. Our lowercase alphabet came from the European uncial alphabets of the Middle Ages, which themselves evolved from scribal approximations of the uppercase <span class="no-hyphens">alphabet.</span>

But our figures were invented in India. They spread westward through the influence of Persian and Arab mathematicians. Traditionally they were known as Arabic numerals, but latterly as Hindu–Arabic numerals. Indic and Arabic languages, of course, look very different from European languages. Thus, figures have always presented a challenge for type designers, as they rely on shapes that are found nowhere in the uppercase and lowercase <span class="no-hyphens">alphabets.</span>

Type designers have met this challenge by devising sets of alternate figures, intended for different typographic contexts. Three things to know in <span class="no-hyphens">advance:</span>

1.  It’s never wrong to use the default figures in your font—namely, the ones you get when typing the keys 0–9. Those are put in the default position because they’re intended to work well across a range of <span class="no-hyphens">contexts.</span>

2.  Not every font has every set of alternate figures listed here. Alternate figures are added based on the type designer’s impression of how the font will be used, and whether the alternates will be <span class="no-hyphens">useful.</span>

3.  If alternate figures are included in your font, they’ll be implemented as <a href="opentype-features.html" class="xref">OpenType features</a>. Those caveats also apply, especially pertaining to application <span class="no-hyphens">support.</span>

<div id="lining-figures" class="subhead">

[Lining figures](#lining-figures)

</div>

Lining figures are usually the same height as caps, but not always. Some fonts have lining figures that fall between lowercase and cap height (for instance, ).

These are the most common figures. They’re also the ones you’re most likely to find in the default position of a font. Lining refers to the fact that figures “line up” at the top and bottom. Lining figures can be used in any situation. Lining figures are always preferred for <a href="all-caps.html" class="xref">all caps</a> text because they come closest to cap <span class="no-hyphens">height.</span>

|                |        |
|----------------|--------|
| 0123456789     | lining |
| top 40 in 1987 | right  |
| TOP 40 IN 1987 | right  |

<div id="oldstyle-figures" class="subhead">

[Oldstyle figures](#oldstyle-figures)

</div>

“Oldstyle” is a curious term for these, because the oldest figures—the original Hindu–Arabic numerals of the first century—look more like lining figures. They’re also sometimes called lowercase or medieval <span class="no-hyphens">figures.</span>

Unlike lining figures, oldstyle figures are designed to look more like lowercase letters. The ones in (shown below) are typical—some are short, some descend below the baseline, and some ascend. You won’t be surprised to hear that oldstyle figures work best in lowercase body <span class="no-hyphens">text.</span>

|                |          |
|----------------|----------|
| 0123456789     | oldstyle |
| top 40 in 1987 | right    |
| TOP 40 IN 1987 | wrong    |

Still, I won’t say that they’re inherently better than lining figures for that purpose. As with <a href="justified-text.html" class="xref">justified text</a>, you’ll see it done both ways in professional typography. And in context, oldstyle figures sometimes look a little, well, old. So the choice is <span class="no-hyphens">yours.</span>

With caps, however, you should not use oldstyle figures. They look <span class="no-hyphens">wrong.</span>

<div id="tabular-and-proportional-figures" class="subhead">

[Tabular & proportional figures](#tabular-and-proportional-figures)

</div>

Tabular figures are set on a fixed width. That way, each figure occupies the same horizontal space on the page (somewhat like a <a href="monospaced-fonts.html" class="xref">monospaced font</a>). Proportional figures are not likewise uniform: the figures are set on varying widths that suit the shape of the <span class="no-hyphens">figure.</span>

<table class="example">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="font-size: 220%"><span><span>$11,234.16</span><br />
<span>$80,765.00</span></span></td>
<td>proportional</td>
</tr>
<tr>
<td style="font-size: 220%"><span><span><span>$</span><span>11</span><span>,</span><span>234</span><span>.</span><span>16</span></span><br />
<span><span>$</span><span>80</span><span>,</span><span>765</span><span>.</span><span>00</span></span></span></td>
<td>tabular</td>
</tr>
</tbody>
</table>

Note that whether figures are lining or oldstyle is separate from whether they’re tabular or proportional. In fact, some fonts (like ) have all four possible combinations—lining proportional, lining tabular, oldstyle proportional, and oldstyle <span class="no-hyphens">tabular.</span>

In <a href="body-text.html" class="xref">body text</a>, proportional figures are preferred because they tend to have more even spacing and a more consistent appearance. But tabular figures are essential for one purpose: vertically aligned columns, like you find in <a href="grids-of-numbers.html" class="xref">grids of numbers</a>.

That said, the default figures on many fonts—especially <a href="system-fonts.html" class="xref">system fonts</a>—are tabular lining figures, so they can move easily from your word-processing document to your spreadsheet. To check if your font has tabular figures, type a line of zeroes above a line of ones. If they’re the same length, then your font has tabular <span class="no-hyphens">figures.</span>

<table class="example">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="font-size: 220%"><span>00000000000</span><br />
<span>11111111111</span></td>
<td>tabular</td>
</tr>
<tr>
<td style="font-size: 220%"><span><span>00000000000</span><br />
<span>11111111111</span></span></td>
<td>not tabular</td>
</tr>
</tbody>
</table>

<div class="btw">

<div class="btw-title">

by the way

</div>

- No version of Microsoft Excel supports OpenType features. So if you want tabular figures in your Excel spreadsheet—and I think you do—you must limit yourself to fonts with tabular figures in the default figure positions. If you’re considering the purchase of a professional font to use in Excel, you should investigate this before you buy. (Numbers on the Mac supports OpenType features, so this caveat does not <span class="no-hyphens">apply.)</span>

- High-end professional fonts include even more alternate figures as OpenType features: superiors, inferiors, ordinals, vertical fractions, diagonal fractions, and more. They’re beyond the scope of this book. But when you’re ready, they’ll be <span class="no-hyphens">waiting.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="color.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="ordinals.html" class="nav"></a>

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
