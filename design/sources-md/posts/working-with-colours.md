<div id="post-245208" role="main">

<div class="mega-header">

<div class="tags">

<a href="https://css-tricks.com/tag/accessibility/" rel="tag">accessibility</a> <a href="https://css-tricks.com/tag/color/" rel="tag">color</a> <a href="https://css-tricks.com/tag/generative-color/" rel="tag">generative color</a> <a href="https://css-tricks.com/tag/hex-values/" rel="tag">hex values</a> <a href="https://css-tricks.com/tag/hsl/" rel="tag">hsl</a> <a href="https://css-tricks.com/tag/web-colors/" rel="tag">web colors</a>

</div>

# Working With Colors Guide

<div class="author-row">

<img src="https://secure.gravatar.com/avatar/49e5183e81a9feacc62fd1d1c7e0501650020fc42379813c4744b2fad84a0da2?s=80&amp;d=retro&amp;r=pg" style="border-radius: 50%;" />

<div>

<a href="https://css-tricks.com/author/sdrasner/" class="author-name">Sarah Drasner</a> on Sep 12, 2016 <span class="modified-date">Updated on Aug 12, 2024 </span>

</div>

</div>

</div>

<div class="article-sponsor">

<div id="bsa-custom-01">

</div>

</div>

<div class="article-content">

There are a lot of ways to work with color on the web. I think it’s helpful to understand the mechanics behind what you’re using, and color is no exception. Let’s delve into some of the technical details of color on the web.

<span id="more-245208"></span>

### <a href="#aa-color-mixing" id="aa-color-mixing" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Color mixing

A huge part of working with color is understanding that the way that you used color as a child doesn’t work the same as how you use color on a computer because of color mixing. As a child, you’re working with paint. Paint and inks from a printer have tiny particles called pigments that mix together and reflect to present color to your eye. **This is subtractive color mixing**. The more colors you add to it, the darker it becomes, until we get brown. Primaries are close to what you’re used to: red, yellow, blue. But when you mix these colors with subtractive color mixing, you arrive at brown.

<div class="wp-block-image">

<figure class="alignright size-large is-resized">
<img src="https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/pigment.jpg?resize=396%2C396&amp;ssl=1" class="wp-image-245210" data-recalc-dims="1" data-fetchpriority="high" decoding="async" srcset="https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/pigment.jpg?w=600&amp;ssl=1 600w, https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/pigment.jpg?resize=300%2C300&amp;ssl=1 300w, https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/pigment.jpg?resize=150%2C150&amp;ssl=1 150w, https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/pigment.jpg?resize=100%2C100&amp;ssl=1 100w" sizes="(min-width: 735px) 864px, 96vw" width="396" height="396" />
</figure>

</div>

On a computer (or any monitor), we’re working with *light*. Which means that when all of the colors mix together, they make *white*. Before <a href="http://www.college-optometrists.org/en/college/museyeum/online_exhibitions/observatory/newton.cfm" rel="noopener">Isaac Newton’s famous prism color experiment</a>, color was believed to be contained within objects rather than reflected and absorbed from the object. Isaac Newton used a prism to prove his theory that sunlight or bright white light was in fact several colors by using the prism to split apart the colors to make a rainbow, and then subsequently using a prism to attempt to further split the blue. The blue did not split, showing that the color wasn’t within the prism, but rather that the prism was splitting the light. This means that in **additive color mixing**, the type of color mixing you get in a monitor, red green and blue can be used to produce all colors, or rgb. In this type of mixing, red and green create yellow.

<figure class="wp-block-image size-large is-resized">
<img src="https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/color-mixing-1024x564.jpg?resize=616%2C339&amp;ssl=1" class="wp-image-245211" data-recalc-dims="1" decoding="async" srcset="https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/color-mixing.jpg?resize=1024%2C564&amp;ssl=1 1024w, https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/color-mixing.jpg?resize=300%2C165&amp;ssl=1 300w, https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/color-mixing.jpg?resize=768%2C423&amp;ssl=1 768w, https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/color-mixing.jpg?resize=1000%2C550&amp;ssl=1 1000w, https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/color-mixing.jpg?w=1410&amp;ssl=1 1410w" sizes="(min-width: 735px) 864px, 96vw" width="616" height="339" />
</figure>

Monitors are many combinations of small bits of light combined that resonate to create a myriad of colors. Resolution refers to the number of individual dots of color, known as pixels, contained on a display. Before we had monitors, artists were using this type of light frequency. Seurat and the Pointillists used red and green to create yellow in paintings like *“La Grande Jatte”* (though he preferred the term chromo-luminarism. Others called it <a href="https://en.wikipedia.org/wiki/Divisionism" rel="noopener">divisionism</a>) This type of painting was created under the belief that optical mixing created more pure resonance in your eye that traditional subtractive pigment color mixing.

<div class="wp-block-image">

<figure class="alignright size-large is-resized">
<img src="https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/seurat-detail.jpg?resize=267%2C330&amp;ssl=1" class="wp-image-245212" data-recalc-dims="1" decoding="async" srcset="https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/seurat-detail.jpg?w=246&amp;ssl=1 246w, https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/seurat-detail.jpg?resize=243%2C300&amp;ssl=1 243w" sizes="(min-width: 735px) 864px, 96vw" width="267" height="330" />
</figure>

</div>

Monitors are made in a few different display modes that change the way we perceive color through them. We express this the term “color bit depth”. The number of colors that can be displayed at one time is determined by this color bit depth. If we have a bit depth of 1, we can produce two colors, or monochrome. Bit depth of two levels creates 4, and so on until we reach a bit-depth of 32, though commonly monitors that project the web have 24 bit-depth density and 16,777,216 colors which is True Color and Alpha Channel.

We call this **True Color** because our human eyes can discern 10,000,000 unique colors, so 24-bit depth will certainly allow for this. In this 24-bit depth, 8 bits are dedicated to red, green, and blue. The rest are used for transparency or alpha channels.

Let’s use this information to unpack our available color properties on the web.

### <a href="#aa-color-values" id="aa-color-values" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Color values

#### <a href="#aa-rgb-values" id="aa-rgb-values" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>RGB Values

The last section illustrates what `rbga(x, x, x, y);` communicates, but let’s break that down a bit more, and show some other properties and their uses. In terms of web color values in an RGB channel, we specify color on a range from 0-255.

``` wp-block-csstricks-code-block
x is a number from 0-255
y is a number from 0.0 to 1.0
rgb(x, x, x); or rgba(x, x, x, y);

Example: rbga(150, 150, 150, 0.5);
```

#### <a href="#aa-hex-values" id="aa-hex-values" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Hex Values

Hex colors are a slightly different format to represent the values in the same way. Hex values are probably the most common way developers designate color on the web.

If you recall that a **byte is 8 bits**, each Hex color or number represents a byte. A color is specified according to the intensity of its red, green and blue components, so we call it a triplet, with each expressed in two places. One byte represents a number in the range 00 to FF (in hexadecimal notation), or 0 to 255 in decimal notation. Byte 1 is Red, byte 2 is green, and byte 3 is blue. **Hexadecimal** is named this because it uses a **base 16 system**. The values use ranges from 0-9 and A-F, 0 being the lowest value and F being the highest, or `#00000` being black and `#FFFFFF` being white.

For triplets with repeated values, you can eliminate the repetition by writing in shorthand, for instance, `#00FFFF` becomes `#0FF`. This system is easy for computers to understand, and it pretty short to write, which makes it useful for quick copy paste and designation in programming. If you’re going to work with colors in a more involved way, though, HSL is a little bit more human-readable.

#### <a href="#aa-hsl-values" id="aa-hsl-values" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>HSL Values

Hsl values work with similar semantics and ranges as rgb, but rather than working with values as the monitor interprets the colors, hsl values work with hue, saturation, lightness values. This looks syntactically similar to rgb values but the ranges are different. This system is based on a <a href="https://en.wikipedia.org/wiki/Munsell_color_system" rel="noopener">Munsell color system</a> (he was the first to separate out color into these three channels, or create a three dimensional system based on mathematical principles tied to actual human vision).

<figure class="wp-block-image align-right media-245213">
<img src="https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/Munsell_1929_color_solid.png?ssl=1" data-recalc-dims="1" decoding="async" />
<figcaption>Hue, Saturation and Lightness can be represented as a three-dimensional model.</figcaption>
</figure>

Hue rotates in 360 degrees, a full circle, while saturation and lightness are percentages from 0 to 100.

``` wp-block-csstricks-code-block
x is a number from 0 - 360
y is a percentage from 0% to 100%
z is a number from 0.0 to 1.0
hsl(x, y, y); or hsla(x, y, y, z);

Example: hsla(150, 50%, 50%, 0.5);
```

It’s a relatively easy change (around 11 lines of code, to be precise) for the browsers to exchange between rgb and hsl values, but for us humans, the use of hsl can be a lot easier to interpret. Imagine a wheel, with dense and saturated content at the center. <a href="http://www.workwithcolor.com/hsl-color-picker-01.htm" rel="noopener">This demo</a> does a pretty good job of showing how it’s expressed.

<figure class="wp-block-image align-none media-245462">
<img src="https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/hsla.gif?ssl=1" data-recalc-dims="1" decoding="async" />
<figcaption>Chris also made a nifty tool a few years back called the hsla explorer, which you can <a href="https://css-tricks.com/examples/HSLaExplorer/">check out here</a>.</figcaption>
</figure>

If you don’t feel particularly skilled working with color, hsla() allows for some pretty simple rules to create nice effects for developers. We cover more about this in the generative color section below.

#### <a href="#aa-named-colors" id="aa-named-colors" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Named Colors

Named colors are also available to us as developers. Named colors, though, have a reputation for being difficult to work with due to their imprecision. The most notable and “famous” examples are that dark grey is actually lighter than grey and lime and limegreen are totally different colors. There’s even a <a href="http://codepo8.github.io/css-colour-names/" rel="noopener">game where you can try to guess named colors on the web</a>, made by <a href="https://twitter.com/codepo8" rel="noopener">Chris Heilmann</a>. Back in the old days, <a href="http://stackoverflow.com/questions/8318911/why-does-html-think-chucknorris-is-a-color" rel="noopener"><code>chucknorris</code> was a blood red color</a> (it’s only supported in HTML now as far as I can tell), but that was my favorite. Named colors can be useful for demonstrating color use quickly, but typically developers use Sass or other preprocessors to store color values by hex, rgba, or hsla and map them to color names used within the company.

#### <a href="#aa-color-variables" id="aa-color-variables" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Color Variables

A good practice is to store color variables and **never use them directly**, mapping them instead to other variables with more semantic naming schemes. CSS has native variables, like:

``` wp-block-csstricks-code-block
:root {
  --brandColor: red;
}

body {
  background: var(--brandColor);
}
```

But they are fairly new and <a href="http://caniuse.com/#feat=css-variables" rel="noopener">haven’t made their way</a> into Microsoft browsers at the time of this writing.

CSS preprocessors also support variables, so you can set up variables like `$brandPrimary` to use through your code base. Or <a href="https://www.sitepoint.com/using-sass-maps/" rel="noopener">a map</a>:

``` wp-block-csstricks-code-block
$colors: (
  mainBrand: #FA6ACC,
  secondaryBrand: #F02A52,
  highlight: #09A6E4
);

@function color($key) {
  @if map-has-key($colors, $key) {
    @return map-get($colors, $key);
  }

  @warn "Unknown `#{$key}` in $colors.";
  @return null;
}

// _component.scss
.element {
  background-color: color(highlight); // #09A6E4
}
```

Remember that naming is important here. Abstract naming is sometimes useful so that if you change a variable that was representing a blue color to an orange color, you don’t have to go through and rename all of your color values. Or worse yet, put up a sign that says “*\$blue is orange now.*” \*sad trombone noise\*

#### <a href="#aa-currentcolor" id="aa-currentcolor" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>currentColor

`currentColor` is an incredibly useful value. It respects the cascade, and is useful for extending a color value to things like box shadows, outlines, borders, or even backgrounds.

Let’s say you have created a div and then inside it another div. This would create orange borders for the internal div:

``` wp-block-csstricks-code-block
.div-external { color: orange; }
.div-internal { border: 1px solid currentColor; }
```

This is incredibly useful for icon systems, either SVG icons for icon fonts. You can set `currentColor` as the default for the fill, stroke, or color, and then use semantically appropriate CSS classes to style the sucker.

#### <a href="#aa-preprocessors" id="aa-preprocessors" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Preprocessors

CSS preprocessors are great for tweaking colors. Here’s some links to different preprocessors documentation on color functions:

- <a href="http://sass-lang.com/documentation/Sass/Script/Functions.html" rel="noopener">Sass functions</a>
- <a href="http://lesscss.org/functions/#color-operations" rel="noopener">Less functions</a>
- <a href="http://stylus-lang.com/docs/bifs.html" rel="noopener">Stylus functions</a>
- <a href="https://github.com/postcss/postcss-color-function" rel="noopener">Example PostCSS plugin</a> for color functions

Here are a few of the cool things we can specifically with Sass:

``` wp-block-csstricks-code-block
mix($color1, $color2, [$weight])
adjust-hue($color, $degrees)
lighten($color, $amount)
darken($color, $amount)
saturate($color, $amount)
```

There are truthfully dozens of ways to programmatically mix and alter colors with preprocessors, and we won’t go into depth for all of them, but here’s a <a href="http://jackiebalzer.com/color" rel="noopener">great interactive resource</a> for more in-depth information.

### <a href="#aa-color-properties" id="aa-color-properties" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Color Properties

Color, as a CSS property, refers to font color. If you’re setting a color on a large area, you would use `background-color`, unless it’s an SVG element in which case you would use `fill`. Border is the border around an HTML element, while `stroke` is it’s SVG counterpart.

#### <a href="#aa-box-and-text-shadows" id="aa-box-and-text-shadows" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Box and Text Shadows

The `box-shadow` and `text-shadow` properties accept a color value. Text shadows accept 2-3 values, h-shadow (horizontal shadow), v-shadow (vertical shadow), and an optional blur-radius. Box shadows take 2-4 values, h-shadow, v-shadow, optional blur distance, and optional spread distance. You can also designate inset at the start to create an inverted shadow. This site has a <a href="http://www.cssmatic.com/box-shadow" rel="noopener">great demo</a> with easy, pasteable code.

#### <a href="#aa-gradients" id="aa-gradients" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Gradients

Linear gradients work by designating a direction. From/to (depending on the browser prefix) top, bottom, left, right, degrees, or radial-gradients. We then specify color stops and the color we want at each stop. These can accept transparency too.

Here’s an example:

<div class="wp-block-cp-codepen-gutenberg-embed-block cp_embed_wrapper">

CodePen Embed Fallback

</div>

Most of the syntax of gradients isn’t all that difficult to write, but I really enjoy working with this <a href="http://www.colorzilla.com/gradient-editor/" rel="noopener">online gradient generator</a>, because it also creates the complicated filter property for IE6-9 support. Here is also a really beautiful <a href="http://uigradients.com/" rel="noopener">UI gradient creator</a>. This one is pretty cool and it is open source and you can contribute to it.

Gradients are similarly easy to create in SVG. We define a block that you reference with an id. We can optionally define a surface area for the gradient as well.

``` wp-block-csstricks-code-block
<linearGradient id="Gradient">
  <stop id="stop1" offset="0" stop-color="white" stop-opacity="0" />
  <stop id="stop2" offset="0.3" stop-color="black" stop-opacity="1" />
</linearGradient>
```

These gradients also support opacity so we can have some nice effects and layer effects like animate them as as a mask.

<div class="wp-block-cp-codepen-gutenberg-embed-block cp_embed_wrapper">

CodePen Embed Fallback

</div>

Gradient text is also possible in webkit only, we have a really a nice code snippet for that [here on CSS-Tricks](https://css-tricks.com/snippets/css/gradient-text/).

### <a href="#aa-generative-color" id="aa-generative-color" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Generative Color

There are a few cool ways to drum up a lot of staggering colors at once. I find these to be really fun to play with when creating generative art or UI elements with code.

As long as you stay within the ranges designated in the last sections, you can use `for` loops in either Sass (or any CSS preprocessor) or JavaScript, or `Math.Random()` with `Math.floor()` to retrieve color values. We need `Math.floor()` or `Math.ceil()` here because if we don’t return full integers, we’ll get an error and do not get a color value.

A good rule of thumb is that you shouldn’t update all three values. I’ve had good luck with a lot of deviation in one range of values, a smaller deviation in the second set of values, and no deviation for the third, not necessarily in that order. For instance, **hsl is very easy to work with to step through color** because you know that looping through the hue from 0 to 360 will give you a full range. Another nice grace of hue-rotate in degrees is that because it’s a full circle, you don’t need to stick to ranges of 0 – 360, even -480 or 600 is still a value a browser can interpret.

#### <a href="#aa-sass" id="aa-sass" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Sass

``` wp-block-csstricks-code-block
@mixin colors($max, $color-frequency) {
  $color: 300/$max;
  
  @for $i from 1 through $max {
    .s#{$i} {
      border: 1px solid hsl(($i - 10)*($color*1.25), ($i - 1)*($color / $color-frequency), 40%);
     }
  }
} 
.demo {
  @include colors(20,2);
}
```

I use that to make fruit loop colors in this demo:

<div class="wp-block-cp-codepen-gutenberg-embed-block cp_embed_wrapper">

CodePen Embed Fallback

</div>

As well as this one, with a different range (**scroll inside the list really fast**):

<div class="wp-block-cp-codepen-gutenberg-embed-block cp_embed_wrapper">

CodePen Embed Fallback

</div>

In the code below, I’m using `Math.random()` within rgb values to drum up a lot of color within the same range. This demo is creating a three-dimensional VR experience with React. I could have stepped through it with a for loop as well, but I wanted the color to be randomized to reflect the movement. Sky’s the limit on this one.

<figure class="wp-block-image align-right media-245215">
<a href="https://sdras.github.io/react-aframe-demo1/" rel="noopener"><img src="https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/2932663-react-aframe.jpg?ssl=1" data-recalc-dims="1" decoding="async" /></a>
<figcaption>Click on the image to see the full demo.</figcaption>
</figure>

#### <a href="#aa-javascript" id="aa-javascript" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>JavaScript

``` wp-block-csstricks-code-block
class App extends React.Component {
  render () {
    const items = [],
          amt1 = 5,
          amt2 = 7;
    for (let i = 0; i < 30; i++) {
     let rando = Math.floor(Math.random() * (amt2 - 0 + 1)) + 0,
          addColor1 = parseInt(rando * i),
          addColor2 = 255 - parseInt(7 * i),
          updateColor = `rgb(200, ${addColor1}, ${addColor2})`;
      items.push(
        // ...
        );
    }
    return (
      
       // ...
       {items}
      
    );
  }
}
```

<a href="http://greensock.com/" rel="noopener">GreenSock</a> came out with a tool that allows you to animate relative color values, which is useful because it means you can grab a lot of elements at once and animate them relative to their current color coordinates. Here are some turtles that demonstrate the idea:

<div class="wp-block-cp-codepen-gutenberg-embed-block cp_embed_wrapper">

CodePen Embed Fallback

</div>

``` wp-block-csstricks-code-block
TweenMax.to(".turtle2 path, .turtle2 circle, .turtle2 ellipse", 1.5, {fill:"hsl(+=0, +=50%, +=0%)"});
```

### <a href="#aa-other-nice-color-effects" id="aa-other-nice-color-effects" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Other Nice Color Effects

#### <a href="#aa-mix-blend-modes-and-background-blend-modes" id="aa-mix-blend-modes-and-background-blend-modes" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Mix Blend Modes and Background Blend Modes

If you’ve used layer effects in Photoshop, you’re probably familiar with mix blend modes. Almost every site in the 90s used them (mine did. \*blush\*). Mix and background blend modes composite two different layered images together, and there are 16 modes available. Going through each is beyond the scope of this article, but here are some key examples.

The top image or color is called the `source`, and the bottom layer is called the `destination`. The area between the two is where the blending magic happens and is called the `backdrop`. We’re mixing both according to fairly simple mathematical formulas.

<figure class="wp-block-image align-right media-245216">
<img src="https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/mixblend.jpg?ssl=1" data-recalc-dims="1" decoding="async" />
</figure>

If you want to get really nerdy with me, the color formulas for the blend modes depend on the type of effect used. For instance, multiply is `destination × source = backdrop`. Other effects are variations of simple math using subtraction, multiplication, addition, and division. Linear is `A+B−1`, while Color Burn is `1−(1−B)÷A`. You don’t really need to know any of these to use them, though.

Here is some [more extensive documentation](https://css-tricks.com/almanac/properties/m/mix-blend-mode/), and here’s a very simple demo to illustrate color working with some of these effects:

<div class="wp-block-cp-codepen-gutenberg-embed-block cp_embed_wrapper">

CodePen Embed Fallback

</div>

This great article by Robin demonstrates some really complex and impressive effects you can achieve from [layering multiple blend modes](https://css-tricks.com/chaining-multiple-blend-modes/) as well. Below we’ll cover mixing them with filters. There’s really a lot you can do in the browser these days.

#### <a href="#aa-filters" id="aa-filters" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Filters

CSS Filters provide a lot of cool color effects, as well as the ability to take a colored image and make it greyscale. We have a [great resource here on CSS-Tricks](https://css-tricks.com/almanac/properties/f/filter/) that shows how these work, and the browser support is pretty high now. Bennett Feely also has this <a href="http://bennettfeely.com/filters-gallery/" rel="noopener">nice filter gallery</a> if you’re feeling explorative.

Filters and Blur modes can work together! Una Kravets created this cool tool called <a href="http://una.im/CSSgram/" rel="noopener">CSS Gram</a> combining some effects to create typical instagram filters, she has some nice documentation at the bottom.

#### <a href="#aa-fecolormatrix" id="aa-fecolormatrix" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>feColorMatrix

<a href="http://alistapart.com/article/finessing-fecolormatrix" rel="noopener">Una has another article</a> exploring the creation of these images with `feColorMatrix` instead, which is a filter primitive in SVG that can be applied to HTML elements as well. It’s very powerful, and allows you to fine-tune and finesse color. As the name implies, the base markup of `feColorMatrix` uses a matrix of values, and we apply it using it’s relative id.

``` wp-block-csstricks-code-block
<filter id="imInTheMatrix">
    <feColorMatrix in="SourceGraphic"
      type="matrix"
      values="0 0 0 0 0
              1 1 1 1 0
              0 0 0 0 0
              0 0 0 1 0" />
  </filter>

  <path filter="url(#imInTheMatrix)"  … />
```

We can also extend this matrix and adjust the hue, saturation, etc, of these values:

``` wp-block-csstricks-code-block
<filter id="imInTheHueMatrix">
  <feColorMatrix in="SourceGraphic"
    type="hueRotate"
    values="150" />
</filter>
```

Una’s article goes into depth exploring all of the capabilities here, but you can get even more information on this and a lot of other crazy SVG colors and gradient tools with Amelia Belamy-Royd’s O’Reilly Book, <a href="http://shop.oreilly.com/product/0636920043065.do" rel="noopener">SVG Colors, Patterns &amp; Gradients</a> or <a href="http://codepen.io/mullany/full/qJCDk/" rel="noopener">Mike Mullany’s exploratory demo</a>.

<figure class="wp-block-image">
<img src="https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/context-color.jpg?ssl=1" data-recalc-dims="1" decoding="async" />
</figure>

### <a href="#aa-accessibility-and-other-things-to-note-about-color" id="aa-accessibility-and-other-things-to-note-about-color" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Accessibility and Other Things to Note about Color

A color is only a color in reference to another color. This is part of what makes color so difficult. You’re probably a little familiar with this in terms of accessibility. A light green on a black may be accessible, but when you change it to a white background it no longer is.

Accessibility in color can be measured with a number of tools. Here are some of my favorites:

- <a href="http://jxnblk.com/colorable/demos/text/" rel="noopener">Colorable</a>
- <a href="http://www.brandwood.com/a11y/" rel="noopener">Text on a background image a11y check</a>
- <a href="http://dasplankton.de/ContrastA/" rel="noopener">Contrast-A</a>
- <a href="http://accessible-colors.com/" rel="noopener">Accessible Colors</a>

It’s also really nice to set up your palette for accessibility from the start. <a href="http://colorsafe.co/" rel="noopener">Color Safe</a> is a great tool that helps with that. Once you’re all set up, <a href="http://wave.webaim.org/" rel="noopener">WAVE (Web Accessibility Tool)</a> will help you evaluate your web page:

#### <a href="#aa-color-and-atmosphere" id="aa-color-and-atmosphere" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Color and Atmosphere

Color is affected by atmosphere, which is a pretty important thing to know if you’re going to create any kind of illusion of depth. Things that are closer to you are in higher saturation, and in more contrast. Things that are further away from you are going to look blurrier.

<figure class="wp-block-image align-right media-245244">
<img src="https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/landscape.jpg?ssl=1" data-recalc-dims="1" decoding="async" />
<figcaption>Landscape showing color contrasts from things closer and farther away</figcaption>
</figure>

#### <a href="#aa-shadows" id="aa-shadows" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Shadows

Shadows are not grey, they are the compliment of the color of the light. If the light you shine on your hand has a yellow cast, the shadow will appear purple. This is useful knowledge if you’re making any super hip long shadows.

<figure class="wp-block-image align-right media-245219">
<img src="https://i0.wp.com/css-tricks.com/wp-content/uploads/2016/09/shadow-color.jpg?ssl=1" data-recalc-dims="1" decoding="async" alt="Shadow is the compliment of the color" />
</figure>

#### <a href="#aa-native-color-inputs" id="aa-native-color-inputs" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Native Color Inputs

There is a native browser color selector that you can employ to help your users select colors dynamically. You can write or if you’d like to start off with color hinting. It’s that simple to use. Good job, browsers. One thing to keep in mind is that the way that it will appear will vary slightly from browser to browser, just like any other native controls. <a href="http://codepen.io/noahblon/pen/ZbjmbK/" rel="noopener">This pen from Noah Blon</a> shows how to use that in tandem with a hue CSS color filter to dynamically select portions of an image to change the color of. The rest of image is greyscale, so it’s not affected. Pretty clever.

### <a href="#aa-fun-developer-stuff-and-other-resources" id="aa-fun-developer-stuff-and-other-resources" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Fun Developer Stuff and Other Resources

- The <a href="https://packagecontrol.io/packages/Color%20Highlighter" rel="noopener">Color Highlighter Plugin for Sublime Text</a> is what I use to easily see what color the browser is going to interpret. I like to use `{"ha_style": "outlined"}` but I know from <a href="http://wesbos.com/highlight-css-colours-in-sublime-text/" rel="noopener">this article</a> that Wes Bos prefers “filled”.
- There are some different traditional palette combinations, and online web resources that can help you drum these up. For the more scientific, <a href="http://paletton.com/" rel="noopener">Paletton</a> or <a href="https://color.adobe.com/create/color-wheel/" rel="noopener">Adobe Color</a>. Benjamin Knight <a href="http://codepen.io/benknight/pen/nADpy" rel="noopener">recreated Adobe’s color tool in d3 on CodePen</a>, which is pretty badass and worth checking out. If you want the web to do the heavy lifting for you (who doesn’t?), <a href="https://coolors.co/" rel="noopener">Coolors</a> is as simple as can be.
- If you need help interpreting colors, and want a quick simple tool to exchange types of color properties for you, <a href="http://www.colorhexa.com/" rel="noopener">Colorhexa</a> has you covered in pretty much every type of color exchange you can think of.
- For the nerdiest of color nerds, you can even have your console output in colors to you. Here’s <a href="http://codepen.io/jscottsmith/pen/VLzMLo/" rel="noopener">a great Pen</a> showing how that works.
- <a href="https://supercolorpalette.com" rel="noopener">Super Color Palette</a> is a little playground for creating color combinations with a variety of controls and the ability to export colors in differnt image formats, including SVG, JPG, and PNG. It’s a free project with a Discord channel to share your color palettes and talk color nerdery.

### <a href="#aa-conclusion" id="aa-conclusion" class="aal_anchor" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFhbF9zdmciIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTQgOWgxdjFINGMtMS41IDAtMy0xLjY5LTMtMy41UzIuNTUgMyA0IDNoNGMxLjQ1IDAgMyAxLjY5IDMgMy41IDAgMS40MS0uOTEgMi43Mi0yIDMuMjVWOC41OWMuNTgtLjQ1IDEtMS4yNyAxLTIuMDlDMTAgNS4yMiA4Ljk4IDQgOCA0SDRjLS45OCAwLTIgMS4yMi0yIDIuNVMzIDkgNCA5em05LTNoLTF2MWgxYzEgMCAyIDEuMjIgMiAyLjVTMTMuOTggMTIgMTMgMTJIOWMtLjk4IDAtMi0xLjIyLTItMi41IDAtLjgzLjQyLTEuNjQgMS0yLjA5VjYuMjVjLTEuMDkuNTMtMiAxLjg0LTIgMy4yNUM2IDExLjMxIDcuNTUgMTMgOSAxM2g0YzEuNDUgMCAzLTEuNjkgMy0zLjVTMTQuNSA2IDEzIDZ6IiAvPjwvc3ZnPg==" class="aal_svg" /></a>Conclusion

The scope of this article is rather large, and the web has a lot of color to delve into, but hopefully this short article gives you a jumping off point for some experimentation and understanding.

</div>

</div>
