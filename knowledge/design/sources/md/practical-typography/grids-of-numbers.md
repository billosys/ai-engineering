---
title: "Grids Of Numbers"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/grids-of-numbers.html"
---

<div id="content">

<div id="doc">

grids of numbersVertical alignment is the key

With grids of numbers, the typographic logic must follow the numerical logic. If it doesn’t, your typography is likely to confuse or mislead your readers about the meaning of the <span class="no-hyphens">numbers.</span>

<div id="not-all-numbers-are-alike" class="subhead">

[Not all numbers are alike](#not-all-numbers-are-alike)

</div>

If you remember everything from sixth-grade math class, you can skip this section. If not, then <span class="no-hyphens">don’t.</span>

Numbers work differently from words. A word is a sequence of characters. The whole sequence has meaning, but the individual characters do not. This isn’t so with numbers. A digit in a number has independent meaning based on its position relative to the decimal point (which may be implied). That’s how we can tell that the digits in .49 represent a number that’s smaller than 49. Also unlike words, different types of numbers have different rules about how they can be combined and <span class="no-hyphens">compared.</span>

Even though it has a special symbol, a percentage is not a quantity. It’s just an alternate way of writing a decimal <span class="no-hyphens">multiplier.</span>

Numbers that are associated with a unit are called quantities. The meaning of a quantity depends on the unit. For instance, if I asked which is bigger—5 or 10—you’d give one answer. But if I asked which is bigger—5 feet or 10 inches—you’d give a different answer. But quantities can be compared only if the units are commensurable. So if I asked which is bigger—5 feet or 10 square inches—the question would be unanswerable. One represents length; the other, <span class="no-hyphens">area.</span>

Not all numbers are quantities, of course. Ordinal numbers denote position in a series, like college rankings. <a href="ordinals.html" class="xref">Ordinals</a> can be compared relatively—8 precedes \#10. But even though 8 is 20% less than 10, a ranking of \#8 cannot be said to be “20% better” than \#10. Ordinals don’t work that <span class="no-hyphens">way.</span>

Nominal numbers are arbitrary identifiers like zip codes or phone numbers. Nominal numbers can’t be compared or combined arithmetically, but they may still have an interior structural logic. For instance, if we’re told that 3235551212 and 3235551 represent phone numbers, we still know they’re different, because phone numbers build from right to <span class="no-hyphens">left.</span>

<div id="and-here-the-typography-restarts" class="subhead">

[and here the typography restarts](#and-here-the-typography-restarts)

</div>

Your goal when typesetting grids of numbers is to make sure the typography reflects the underlying meaning of the number. To do this, there is one golden rule: **in any column, digits with the same meaning must be vertically aligned with each other.** This means that you shouldn’t merely select everything and apply the same formatting to everything. Different kinds of numbers need different <span class="no-hyphens">typography.</span>

Important caveat: the figures in your font will only line up with each other if they’re tabular figures. For more about these, see <a href="alternate-figures.html" class="xref">alternate figures</a>.

<a href="samples/number-grid-before.pdf" class="sample-document"></a>

<div id="before" class="subhead">

[Before](#before)

</div>

1.  Numbers improperly <span class="no-hyphens">aligned.</span>

2.  Garish <a href="color.html" class="xref">color</a> <span class="no-hyphens">scheme.</span>

3.  <a href="tables.html" class="xref">Table</a> cell margins too <span class="no-hyphens">small.</span>

4.  Needlessly thick <a href="rules-and-borders.html" class="xref">rules and borders</a>.

5.  <a href="line-spacing.html" class="xref">Line spacing</a> <span class="no-hyphens">uneven.</span>

6.  Inapt <a href="system-fonts.html" class="xref">system font</a> <span class="no-hyphens">(Calibri).</span>

<a href="samples/number-grid-after.pdf" class="sample-document"></a>

<div id="after" class="subhead">

[After](#after)

</div>

1.  Invoice numbers (nominal numbers) aligned <span class="no-hyphens">right.</span>

2.  Net-worth values (quantities) have currency symbols, commas, and cents. Then they are aligned right, so cents and dollars line up. If a quantity is between 0 and 1, add a leading zero for <span class="no-hyphens">clarity.</span>

3.  Weights aligned with decimal tabs (see <a href="tabs-and-tab-stops.html" class="xref">tabs and tab stops</a>) so full pounds and fractional pounds line up.

4.  Zip codes are aligned left, so five- and nine-digit zip codes line up properly. (Phone numbers would need to be aligned <span class="no-hyphens">right.)</span>

5.  Unnecessary colors and borders <span class="no-hyphens">removed.</span>

6.  Line spacing <span class="no-hyphens">even.</span>

7.  Better font ().

As for the column labels, format those after you take care of the numbers. Sometimes you might need to make an inconsistent formatting choice to make them look right. For instance, in the revised example, the label “Weight” is centered, even though the numbers underneath are not. Did you notice? No. Readers won’t <span class="no-hyphens">either.</span>

<div class="btw">

<div class="btw-title">

by the way

</div>

- “If you padded out the dollar quantities to make them line up, why not do the same to the weights?” Tempting, but don’t. Unlike amounts of money, physical quantities communicate not only magnitude but also precision. Therefore, the measurement 98.000 pounds is not the same as 98 pounds. The extra zeroes denote precision to a thousandth of a pound, which the second measurement does not claim (e.g., it might actually be 98.27 <span class="no-hyphens">pounds).</span>

- In a number less than 10,000, putting a comma after the thousands digit is generally a matter of style. For instance, both \$6736 and \$6,736 are fine. But if those numbers are in a column (as in the example above ), the comma becomes mandatory. Without it, \$6736 won’t quite line up with \$16,736.

  I’ll leave the choice of lining vs. oldstyle figures to you (see <a href="alternate-figures.html" class="xref">alternate figures</a>). In a grid, however, I prefer the look of lining figures, because of their vertical <span class="no-hyphens">consistency.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="business-cards.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="presentations.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="sample-documents.html" class="box-link">chapter</a>

</div>

</div>

</div>
