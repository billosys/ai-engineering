---
title: "Ligatures In Programming Fonts Hell No"
source: "Butterick's Practical Typography"
author: "Matthew Butterick"
url: "https://practicaltypography.com/ligatures-in-programming-fonts-hell-no.html"
---

<div id="content">

<div id="doc">

Ligatures in programming fonts:  
hell no

Ligatures in programming fonts—a misguided trend I was hoping would collapse under its own illogic. But it persists. Let me save you some <span class="no-hyphens">time—</span>

Ligatures in programming fonts are a terrible <span class="no-hyphens">idea.</span>

And not because I’m a purist or a grump. (Some days, but not today.) Programming code has special semantic considerations. Ligatures in programming fonts are likely to either misrepresent the meaning of the code, or cause miscues among readers. So in the end, even if they’re cute, the risk of error isn’t worth <span class="no-hyphens">it.</span>

First, what are ligatures? <a href="ligatures.html" class="xref">Ligatures</a> are special characters in a font that combine two (or more) troublesome characters into one. For instance, in serifed text faces, the lowercase *f* often collides with the lowercase *i* and *l*. To fix this, the *fi* and *fl* are often combined into a single shape (what pros would call a *glyph*).

|  |  |
|----|----|
| <span style="font-family: concourse-t3">fi fj fl *ffi gg gy*</span> | ok |
| <span style="font-variant-ligatures: none;">fi fj fl *ffi gg gy*</span> | wrong |
| <span style="font-feature-settings: 'liga';">fi fj fl *ffi gg gy*</span> | right |

In this type designer’s opinion, a good ligature doesn’t draw attention to itself: it simply resolves whatever collision would’ve happened. Ideally, you don’t even notice it’s there. Conversely, this is why I loathe the *Th* ligature that is the default in many Adobe fonts: it resolves nothing, and always draws attention to <span class="no-hyphens">itself.</span>

Ligatures in programming fonts follow a similar idea. But instead of fixing the odd troublesome combination, well-intentioned amateur ligaturists are adding dozens of new & strange ligatures. For instance, these come from [Fira Code,](https://github.com/tonsky/FiraCode) a heavily ligatured spinoff of the open-source [Fira <span class="no-hyphens">Mono.</span>](https://mozilla.github.io/Fira/)

So what’s the problem with programming <span class="no-hyphens">ligatures?</span>

1.  **They contradict Unicode.** [Unicode](http://unicode.org/standard/standard.html) is a standardized system—used by all modern fonts—that identifies each character uniquely. This way, software programs don’t have to worry that things like the Greek letter `Δ` (= uppercase Delta) might be stashed in some special place in the font. Instead, Unicode designates a unique [name and number](http://www.fileformat.info/info/unicode/char/0394/) for each character, called a [*code point*.](http://unicode.org/glossary/#code_point) If you have a `Δ` in your font, you associate it with its designated Unicode code point, which is `0x0394`. In addition to alphabetic characters, Unicode assigns code points to thousands of symbols (including <span class="no-hyphens">emoji).</span>

    The problem? Many of the programming ligatures shown above are easily confused with existing Unicode symbols. Suppose you’re looking at a code fragment that uses Unicode characters and see the symbol `≠`. Are you looking at a `!=` ligature that’s shaped like `≠`? Or the actual [Unicode character `0x2260`,](http://www.fileformat.info/info/unicode/char/2260/) which also looks like `≠`? The ligature introduces an ambiguity that wasn’t there <span class="no-hyphens">before.</span>

2.  Even the maker of Fira Code’s ligatures concedes this point: he says that ligatures [“almost never”](https://twitter.com/nikitonsky/status/1473666840937312257) go wrong, which is the glass-half-full way of saying that they sometimes definitely <span class="no-hyphens">do.</span>

    **They’re guaranteed to be wrong sometimes.** There are a lot of ways for a given sequence of characters, like `!=`, to end up in a source file. Depending on context, it doesn’t always mean the same <span class="no-hyphens">thing.</span>

    The problem is that ligature substitution is “dumb” in the sense that it only considers whether certain characters appear in a certain order. It’s not aware of the semantic context. Therefore, any global ligature substitution is guaranteed to be semantically wrong part of the <span class="no-hyphens">time.</span>

When we’re using a serifed text font in ordinary <a href="body-text.html" class="xref">body text</a>, we don’t have the same considerations. An *fi* ligature always means *f* followed by *i*. In that case, ligature substitution that ignores context doesn’t change the <span class="no-hyphens">meaning.</span>

Still, some typographic transformations in body text can be semantically wrong. For instance, <a href="foot-and-inch-marks.html" class="xref">foot and inch marks</a> are often typed with the same characters as quotation marks. (See <a href="straight-and-curly-quotes.html" class="xref">straight and curly quotes</a>.) But whereas quotation marks want to be curly, foot and inch marks want to be straight (or slanted slightly to the upper right). So if we apply automatic smart (aka curly) quotes, we have to be careful not to capture foot and inch marks in the <span class="no-hyphens">transformation.</span>

Does that mean programmers can never have nice things? It’s totally fine to redesign individual characters to distinguish them from others. For instance, in <a href="triplicate.html" class="xref">Triplicate,</a> I include a special “Code” variant that includes redesigned versions of certain characters that are easily <span class="no-hyphens">confused.</span>

`` `$te_fl{1234*567~890} `` Regular  
`` `$te_fl{1234*567~890} `` Code

But in this case, the point is disambiguation: we don’t want the lowercase *l* to look like the digit *1*, nor the zero to look like a cap *O*. Whereas ligatures are going the opposite direction: making distinct characters appear to be <span class="no-hyphens">others.</span>

Bottom line: this isn’t a matter of taste. In programming code, every character in the file has a special semantic role to play. Therefore, any kind of “prettifying” that makes one character look like another—including ligatures—leads to a swamp of despair. If you don’t believe me, try it for 10 or 15 <span class="no-hyphens">years.</span>

—Matthew Butterick  
29 March <span class="no-hyphens">2019</span>

<div class="btw">

<div class="btw-title">

by the way

</div>

- Yes, I do a [lot of <span class="no-hyphens">programming.</span>](https://beautifulracket.com)

- “What do you mean, it’s not a matter of taste? I like using ligatures when I code.” Great! In so many ways, I don’t care what you do in private. Although I predict you will eventually burn yourself on this hot mess, my main concern is typography that faces other human beings. So if you’re preparing your code for others to read—whether on screen or on paper—skip the ligatures. Not least because you won’t even know when they go wrong. See <a href="trademark-and-copyright-symbols.html" class="xref">trademark and copyright symbols</a> for a related cautionary <span class="no-hyphens">tale.</span>

- One inspiration for this piece was the LaTeX crowd, who would routinely write me to insist their typography was infallible. And yet. I kept seeing LaTeX-prepared books that incorrectly substituted curly quotes for backticks. For instance, the example below is from Kent Dybvig, *The Scheme Programming Language*, 4th ed. In this chunk of Scheme code, the opening-quote marks are supposed to be backticks; the closing-quote mark is supposed to be a single straight <span class="no-hyphens">quote:</span>

  “But code samples like these aren’t really ambiguous, because everyone knows that you don’t type the curly quotes.” A sloppy argument, though it may be true for languages that only accept ASCII input. But many of today’s programming languages (e.g., [Racket](https://racket-lang.org)) accept UTF-8 input. In that case, curly quotes can legitimately be part of the input stream. So ambiguity is a real possibility. Same problem with <span class="no-hyphens">ligatures.</span>

- The other inspiration for this piece were the people who repeatedly asked me when would get ligatures, Powerline characters, and so on. Answer, as nicely as possible: <span class="no-hyphens">never.</span>

</div>

</div>

<span id="links"></span>

<div class="gap" style="height:1em">

</div>

</div>

<a href="are-two-spaces-better-than-one.html" class="nav"></a>

<div id="prev" class="side">

</div>

<a href="typography-2020.html" class="nav"></a>

<div id="next" class="side">

</div>

<div id="switcher" onmousedown="drag_switcher(event, this)">

<span id="switcher_undock" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_move" class="switcher_icon"><span class="icon"></span></span> <span id="switcher_info" class="switcher_icon" onclick="handle_font_info_click(this)" onmousedown="event.stopPropagation()"><span class="icon"></span></span> <span id="switcher_hide" class="switcher_icon" onclick="move_switcher_inside_toolbar()" onmousedown="event.stopPropagation()"><span class="icon"></span></span>

</div>

<div id="toolbar">

<div id="navtable">

<div class="center">

<a href="commentary.html" class="box-link">chapter</a>

</div>

</div>

</div>
