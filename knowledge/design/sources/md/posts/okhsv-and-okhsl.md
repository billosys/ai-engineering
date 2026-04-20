<div class="container is-max-desktop" role="main">

<div class="content is-medium">

# 

Okhsv and Okhsl

#### Two new color spaces for color picking <a href="#two-new-color-spaces-for-color-picking" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

> *This post has an accompanying [interactive comparison of color pickers](http://bottosson.github.io/misc/colorpicker)*.
>
> *I would recommend checking out the interactive demo first, then return if you are interested in the background and technical details.*

Picking colors is a common operation in many applications and over the years color pickers have become fairly standardized. Ubiquitous today are color pickers based on [HSL and HSV](https://en.wikipedia.org/wiki/HSL_and_HSV). They are simple transformations of RGB values to alternative coordinates chosen to better correlate with perceptual qualities.

Here are two common variants of color pickers built on HSL and HSV:

<div class="columns">

<div class="column has-background-white-ter is-one-third">

<img src="/img/colorpicker/hsv-picker.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 337px) min(calc(var(--main-width) * 0.8397626112759644), 283px);" decoding="async" loading="lazy" width="337" height="283" alt="HSV Color Picker" />

A HSV color picker.

</div>

<div class="column has-background-white-ter is-one-third">

<img src="/img/colorpicker/hsl-picker.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 342px) min(calc(var(--main-width) * 0.827485380116959), 283px);" decoding="async" loading="lazy" width="342" height="283" alt="HSL Color Picker" />

A HSL color picker.

</div>

</div>

Despite color picking playing a big role in a lot of applications, the design of color pickers isn’t a particularly well researched topic. While some variation exist in the widgets themselves, the choice of HSL or HSV is mostly taken for granted, with only a few exceptions.

Is their dominance well deserved or would it be possible to create better alternatives? I at least think that this question deserves to be explored and that color picker design should be an active research topic. With this post I hope to contribute to the exploration of what a better color picker could and should be, and hopefully inspire others to do the same!

The main focus here will be on the choice of color space, rather than the design of the UI widget used for navigating the color space.

> This rest of this post is organized as follow:
>
> - A brief history of color picking
> - What are meaningful properties of color spaces for color picking?
> - What options exist already and how do they perform?
> - Introducing two new color spaces: Okhsl and Okhsv
> - Ideas for future work

## Color picking before computers <a href="#color-picking-before-computers" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

<div style="float:right;width:300px;padding:15px">

<div class="box has-background-white-ter">

<img src="/img/colorpicker/846px-Munsell_color-tree_hg.jpg" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 846px) min(calc(var(--main-width) * 0.9078014184397163), 768px);" decoding="async" loading="lazy" width="846" height="768" alt="Munsell Color System" />

Munsell Color System. Photo by Hannes Grobe, license [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

</div>

<div class="box has-background-white-ter">

<img src="/img/colorpicker/ncs_color_picker.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 1241px) min(calc(var(--main-width) * 1.2224012892828364), 1517px);" decoding="async" loading="lazy" width="1241" height="1517" alt="Natural Color System" />

Example of NCS color picker. Screenshot from NCS Navigator in the [Colourpin](https://ncscolour.com/colourpin/) app.

</div>

</div>

Categorizing, describing and picking colors is an old problem and predates computers by many centuries. Over the years countless artists and scientists have worked to understand how humans perceive colors and used that knowledge to try and create practical systems for describing colors. Many different color ordering systems have been created over the years based on mixing properties of paints, light or on perceptual qualities.

During the 20th century two important color systems emerged. The [Munsell Color System](https://en.wikipedia.org/wiki/Munsell_color_system) and the [Natural Color System (NCS)](https://en.wikipedia.org/wiki/Natural_Color_System). Both of them are based on human perception and were derived using experiments, but with different approaches. The two systems are used in many practical applications today still.

In the Munsell color system, colors are described with three parameters, designed to match the perceived appearance of colors: Hue, Chroma and Value. The parameters are designed to be independent and each have a uniform scale. This results in a color solid with an irregular shape. Modern color spaces and models, such as [CIELAB](https://en.wikipedia.org/wiki/CIELAB_color_space), [Cam16](https://en.wikipedia.org/wiki/Color_appearance_model#CAM16) and my own [Oklab](https://bottosson.github.io/posts/oklab/), are very similar in their construction.

The Natural Color System takes a different approach, and is designed to make it easy to describe colors, rather than to match perceptual qualities. It does this by describing colors by their similarity to six primary colors: white, black, yellow, red, green and blue. The yellow, red, green and blue colors are used to determine the hue. The final color is described by a color triangle with the corners white, black and the most saturated color of the given hue. A position in the triangle is described with the parameters whiteness, blackness, chromaticness. Any two of those parameters are sufficient, since they sum to one.

For more information about historical color systems, this is a great resource: [colorsystem.com](http://www.colorsystem.com/?lang=en).

## What makes a good color picker? <a href="#what-makes-a-good-color-picker%3F" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

Before diving into how color pickers have evolved in the digital era, let’s look a bit further at what considerations can be relevant when designing a color space for color picking. This part assumes familiarity with color appearance concepts such as [lightness](https://en.wikipedia.org/wiki/Lightness), [chroma, saturation](https://en.wikipedia.org/wiki/Colorfulness) and [hue](https://en.wikipedia.org/wiki/Hue).

In this post the focus will be on what is today the most common case, picking colors in the [sRGB](https://en.wikipedia.org/wiki/sRGB) gamut. Wide gamut and HDR displays are becoming more common and will be increasingly important, so wide gamut and HDR color picking is definitely a topic for further research and development, but it will not be considered here.

Here’s an attempt at capturing useful properties for color spaces designed for picking colors:

- **Orthogonal Lightness** - Hue/Chroma/Saturation can be altered, while keeping perceived Lightness constant
- **Orthogonal Chroma** - Lightness/Hue can be altered, while keeping perceived Chroma constant
- **Orthogonal Saturation** - Lightness/Hue can be altered, while keeping perceived Saturation constant
- **Orthogonal Hue** - Lightness/Chroma/Saturation can be altered, while keeping perceived Hue constant
- **Simple Geometrical Shape** - Fit the target gamut into a cylinder or other simple shape, so that parameters can be altered independently without resulting in colors outside the target gamut. Could also be a swept triangle like NCS, since it is simple to map back and forth to a cylinder.
- **Max Chroma at edge** - Make it easy to find the strongest color of a given hue, by placing the strongest color on edge of the color volume.
- **Varies Smoothly** - Vary smoothly with each parameter. No discontinuous or abrupt changes.
- **Varies Evenly** - The perceived magnitude of the change in color caused by changing a parameter should be uniform for all values of the parameter.

**Note:** These properties are in conflict, so designing a color space for color picking is a about finding which tradeoffs to make. In particular, independent control of hue, lightness and chroma can not be achieved in a color space that also maps sRGB to a simple geometrical shape.

## Color spaces for color picking <a href="#color-spaces-for-color-picking" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

By far the most used color spaces today for color picking are [HSL and HSV](https://en.wikipedia.org/wiki/HSL_and_HSV), two representations introduced in the classic 1978 paper [“Color Spaces for Computer Graphics”](https://doi.org/10.1145/800248.807362). HSL and HSV designed to roughly correlate with perceptual color properties while being very simple and cheap to compute.

Worth noting is that HSL and HSV are not quite color spaces on their own, they are transformations from a source RGB color space. For each set of RGB primaries and transfer functions, the transformation to HSL and HSV produces unique color spaces. Today HSL and HSV are most commonly used together with the sRGB color space, so that is what we will look at here and we will here use HSL and HSV to refer to HSL and HSV for the sRGB color space.

Also useful to note is that HSL and HSV are not continuously differentiable, so that limits their use with numerical optimization and machine learning.

### HSV <a href="#hsv" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

HSV describes colors with three parameters:

- **"Hue"** - Roughly corresponds to perceived hue, but it has quite severe distortions.
- **"Saturation"** - Roughly corresponds to saturation relative to maximum possible saturation in sRGB of the same hue.
- **"Value"** - A bit hard to define. Can be seen as how much to mix the color with black, with 100% being no black and 0% completely black. “Value” is sometimes also referred to as Brightness.

HSV is quite similar to the Natural Color System in its structure and it’s possible to transform it to have parameters more similar to NCS, then referred to as [hue, whiteness and blackness (HWB)](https://en.wikipedia.org/wiki/HWB_color_model). After that transformation the largest difference compared with NCS are:

- NCS is derived based on research into the appearance of colors and does a good job at matching human perception
- HWB/HSV has a simple construction, not taking research into color appearance into account and is not matching perception closely. Hue is the most problematic.
- NCS has a gamut designed to contain pigments realizable in paint/print
- HWB/HSV has a gamut based on the RGB color space it is constructed from (most commonly sRGB)

<div class="columns">

<div class="column has-background-white-ter is-one-third">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsv_blue.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 257px) min(calc(var(--main-width) * 1), 257px);" decoding="async" loading="lazy" width="257" height="257" alt="HSV Blue Plot" />

</div>

Example of hue distortion for deep blue colors. Notice the purple shift as saturation decreases.

</div>

</div>

### HSL <a href="#hsl" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

HSV describes colors with three parameters:

- **"Hue"** - Identical to “hue” in HSV, with the same issues.
- **"Saturation"** - Roughly the chroma of the color relative to the most colorful color with the same “lightness” and “hue”. Confusingly referred to as saturation, which it is not comparable to. In the original paper it was referred to as “relative chroma”, which is more accurate. Not the same as “saturation” in HSV.
- **"Lightness"** - Some correlation with the perception of lightness, with 0% corresponding to black and 100% to white. Does not match the perception of lightness well at all for saturated colors. Referred to as “Intensity” in the original paper.

<div class="columns">

<div class="column has-background-white-ter is-one-third">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_blue.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 257px) min(calc(var(--main-width) * 1), 257px);" decoding="async" loading="lazy" width="257" height="257" alt="HSL Blue Plot" />

</div>

Example of hue distortion for deep blue colors.

</div>

<div class="column has-background-white-ter is-one-third">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_ligthness.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 257px) min(calc(var(--main-width) * 1), 257px);" decoding="async" loading="lazy" width="257" height="257" alt="HSL Constant Lightness" />

</div>

Example of colors HSL considers to have the same lightness.

</div>

</div>

### HSLuv <a href="#hsluv" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

[HSLuv](https://www.hsluv.org/) is a recent development to tackle some of the shortcomings of HSL. It is based on [CIELChuv](https://en.wikipedia.org/wiki/CIELUV), a cylindrical form of 1976 CIE color space CIELUV. CIELChuv is constructed so that for a given hue, all colors of that hue can be constructed by additive blending of white and a saturated color of that hue (and in general, additive blending of light forms straight lines in CIELuv).

HSLuv describes colors with three parameters:

- **"Hue"** - Same as hue in CIELChuv. Does not match the perception of hue fully due to the [Abney effect](https://en.wikipedia.org/wiki/Abney_effect): the perception of hue does not correspond to additive blending.
- **"Saturation"** - Based on chroma as defined in CIELChuv, but rescaled to be relative to the most saturated sRGB color of the same “lightness” and “hue”.
- **"Lightness"** - Same as lightness in CIELChuv. Does a good job at matching perceived lightness.

Two drawback with HSLuv are:

- Does not match perception of hue. This is particularly obvious for deep blue and purple colors.
- The way “Saturation” is defined, it does not vary smoothly due to the uneven shape of the sRGB gamut. E.g. by keeping “Saturation” constant and changing hue, the perceived chroma can change drastically and abruptly.

<div class="has-background-white-ter columns">

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsluv_blue.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 257px) min(calc(var(--main-width) * 1), 257px);" decoding="async" loading="lazy" width="257" height="257" alt="HSLuv Blue Plot" />

</div>

Example of hue distortion for blue colors. The distortion in HSLuv is different from that in sRGB and is caused by the [Abney effect](https://en.wikipedia.org/wiki/Abney_effect).

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsluv_uneven_s_circle.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 257px) min(calc(var(--main-width) * 1), 257px);" decoding="async" loading="lazy" width="257" height="257" alt="HSLuv Constant Lightness" />

</div>

Example of constant lightness in HSLuv, with low “saturation” close to the center of the circle and maximum “saturation” at the edge. Notice how the blue and red hues are much more saturated than surrounding colors.

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsluv_uneven_s_slice.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 257px) min(calc(var(--main-width) * 1), 257px);" decoding="async" loading="lazy" width="257" height="257" alt="HSLuv Constant Saturation" />

</div>

Slice of colors with constant “saturation” in HSLuv. The scaling to match the uneven shape of the sRGB gamut makes the perceived chroma vary unevenly.

</div>

</div>

### Color spaces modelling color appearance <a href="#color-spaces-modelling-color-appearance" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

While there is a limited amount of research done regarding color picking, a lot of work has been done to create color models that are able to predict color appearance. These continue in the tradition of the Munsell color model discussed above, but use more modern color science and mathematical models to better model the appearance of color. One of the most famous of these is [CIELab](https://en.wikipedia.org/wiki/CIELAB_color_space), but there are today several new models that perform better.

Comparing all the color models is beyond the scope of this post, the important conclusion here is that these models can model the perception of Lightness, Hue and Chroma much better than all the previously discussed options. For a brief overview of some of the more recent models, see my previous post [“A perceptual color space for image processing”](https://bottosson.github.io/posts/oklab/). Since then another color model has also appeared: [ZCAM](https://doi.org/10.1364/OE.413659). For a much deeper overview of modern color science and different attempts at modeling color appearance, I recommend the book [“Color Appearance Models”](http://markfairchild.org/CAM.html) by Mark D. Fairchild.

The main drawback of using these models directly for color picking is that the sRGB gamut has a quite irregular shape in these color spaces. As a result, changing one parameter, such as hue, can easily create a color outside the target gamut, making them quite tedious to use. Several color pickers have been made using either CIELab or more modern lab-like color spaces. From what I can tell they have only seen limited use compared with the more common HSV and HSL color pickers however.

I would think that the reason that they haven’t caught on is that their drawbacks outweigh their benefits: using a space with parameters that don’t match the our perception of hue, lightness and chroma is easier than using one with an irregular shape. That is certainly my personal experience.

For the more advanced models an additional complication is that they have several parameters meant to be adjusted based on the viewing conditions. When used for color picking they seem to mostly be set to match some kind of average viewing conditions though.

Here are a couple of examples of the irregular shape of the sRGB gamut in a perceptual color space:

<div class="columns">

<div class="column has-background-white-ter is-one-third">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/oklrab_blue.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 257px) min(calc(var(--main-width) * 1), 257px);" decoding="async" loading="lazy" width="257" height="257" alt="Oklrab Blue" />

</div>

A slice of the gamut with a constant blue hue.

</div>

<div class="column has-background-white-ter is-one-third">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/oklrab_yellow.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 257px) min(calc(var(--main-width) * 1), 257px);" decoding="async" loading="lazy" width="257" height="257" alt="Oklrab Yellow" />

</div>

A slice of the gamut with a constant yellow hue.

</div>

</div>

It is unfortunately also common to see CIELab based color pickers showing colors outside the target gamut and often they are mapped back by simply clamping individual RGB components. This creates severe distortions in hue, lightness and chroma, in would would otherwise be a fairly uniform color space.

### Summary <a href="#summary" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

These are the color spaces I am aware of that are relevant, but please reach out if you are aware of any more color spaces useful for color picking.

To summarize, here is a table of the different color spaces discussed and how they match the different desirable properties. This is definitely a bit subjective, but will hopefully give a decent overview.

|                          | HSV     | HSL     | HSLuv   | Lab-like\* | NCS      |
|--------------------------|---------|---------|---------|------------|----------|
| Orthogonal Lightness     | no      | no      | yes     | yes        | no       |
| Orthogonal Chroma        | no      | no      | no      | yes        | partial  |
| Orthogonal Saturation    | partial | no      | no      | no\*\*     | no       |
| Orthogonal Hue           | partial | partial | partial | yes        | yes      |
| Simple Geometrical Shape | yes     | yes     | yes     | no         | no\*\*\* |
| Max Chroma at Edge       | yes     | no      | no      | yes        | no       |
| Varies Smoothly          | yes     | yes     | no      | yes        | yes      |
| Varies Evenly            | no      | no      | no      | yes        | partial  |

> *\*) This of course depends on which Lab-like color space. This is the best possible an appearance modelling color space could achieve.*  
> *\*\*) If desirable, saturation can be used instead of Chroma, and then this would be a yes and “Orthogonal Chroma” a no.*  
> *\*\*\*) NCS has a simple geometrical shape, but it does not match the sRGB gamut.*

## Finding a better tradeoff <a href="#finding-a-better-tradeoff" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

One of the main advantages of HSL and HSV over the different Lab color spaces is that they map the sRGB gamut to a cylinder. This makes them easy to use since all parameters can be changed independently, without the risk of creating colors outside of the target gamut.

The main drawback on the other hand is that their properties don’t match human perception particularly well. Reconciling these conflicting goals perfectly isn’t possible, but given that HSV and HSL don’t use anything derived from experiments relating to human perception, creating something that makes a better tradeoff does not seem unreasonable.

We will attempt to do just that by creating new color spaces similar to HSL and HSV but that better match perception. This will be done by leveraging the Oklab color space. Using Oklab here over more advanced models such as CAM16 is useful because working out the math becomes a lot simpler. It also means that it won’t be a full color model able to adapt to different viewing conditions, but that is probably also desirable here since it is more practical.

For consistency with the naming of Oklab, these new color spaces will be called Okhsl and Okhsv. The parameters will also be referred to as <span class="katex"><span class="katex-mathml">$`h`$</span></span>, <span class="katex"><span class="katex-mathml">$`s`$</span></span> and <span class="katex"><span class="katex-mathml">$`l`$</span></span> and <span class="katex"><span class="katex-mathml">$`h`$</span></span>, <span class="katex"><span class="katex-mathml">$`s`$</span></span> and <span class="katex"><span class="katex-mathml">$`v`$</span></span> respectively. Those names are a bit confusing but I think making the new spaces easy to adopt for someone used to HSL and HSV is more important than trying to establish new names.

## Intermission - a new lightness estimate for Oklab <a href="#intermission---a-new-lightness-estimate-for-oklab" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

One design decision with Oklab is to use a design that is scale independent. That is, Oklab has no concept of reference white, unlike CIELab for example. In many cases this is an advantage, since it makes dealing with larger dynamic ranges easier.

However, in the context of a color picker with well defined dynamic range and a clear reference white luminance it reduces Oklab’s ability to predict lightness. Therefore, an additional lightness estimate is needed to better handle these cases. With a reference white luminance of <span class="katex"><span class="katex-mathml">$`Y=1`$</span></span>, the new lightness estimate <span class="katex"><span class="katex-mathml">$`L_r`$</span></span> is defined as:

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`k_1 = 0.206 ,\qquad k_2 = 0.03 ,\qquad k_3 = \frac{1+k_1}{1+k_2}`$</span></span></span>

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`L_r = \frac{k_3 L - k_1 + \sqrt{(k_3 L - k_1)^2 + 4 k_2 k_3 L}} 2`$</span></span></span>

With the inversion:

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`L = \frac{L_r (L_r + k_1)}{k_3 (L_r + k_2)}`$</span></span></span>

This new lightness estimate closely matches the lightness estimate of CIELab overall and is nearly equal at 50% lightness (Y for CIELab L is 0.18406, and <span class="katex"><span class="katex-mathml">$`L_r`$</span></span> 0.18419) which is useful for compatibility. Worth noting is that it is not possible to have a lightness scale that is perfectly uniform independent of viewing conditions and background color. This new lightness function is however a better tradeoff for cases with a well defined reference white.

<div class="columns">

<div class="column has-background-white-ter is-half">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/lightness_cielab_lr_l.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 0.75), 384px);" decoding="async" loading="lazy" width="512" height="384" alt="Lightness comparison" />

</div>

From top to bottom: CIELab <span class="katex"><span class="katex-mathml">$`L`$</span></span>, Oklab <span class="katex"><span class="katex-mathml">$`L_r`$</span></span>, Oklab <span class="katex"><span class="katex-mathml">$`L`$</span></span>.

</div>

</div>

## Introducing two new color spaces: Okhsv and Okhsl <a href="#introducing-two-new-color-spaces%3A-okhsv-and-okhsl" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

With this new lightness estimate, we are ready to look into the construction of Okhsv and Okhsl. Here is a rough overview of the general idea behind Okhsv and Okhsl and their construction. Some details are glossed over here, for all the details check out the source code [below](#source-code).

### Okhsv <a href="#okhsv" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

To derive Okhsv, we will start with OkLCh, use its estimate for hue, <span class="katex"><span class="katex-mathml">$`h`$</span></span>, as is and introduce <span class="katex"><span class="katex-mathml">$`s`$</span></span> and <span class="katex"><span class="katex-mathml">$`v`$</span></span> parameters that are calculated based on lightness, <span class="katex"><span class="katex-mathml">$`L_r`$</span></span>, and chroma, <span class="katex"><span class="katex-mathml">$`C`$</span></span>. To keep the triangular shape when using <span class="katex"><span class="katex-mathml">$`L_r`$</span></span> we also scale <span class="katex"><span class="katex-mathml">$`C`$</span></span> by <span class="katex"><span class="katex-mathml">$`L_r/L`$</span></span>.

Here is the sRGB gamut plotted for set of hues, with <span class="katex"><span class="katex-mathml">$`L_r`$</span></span> on the y-axis and <span class="katex"><span class="katex-mathml">$`C L_r/L`$</span></span> on the x-axis:

<div class="has-background-white-ter columns">

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsv_1_sv_7.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Yellow" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsv_1_sv_16.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Blue" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsv_1_sv_22.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Magenta" />

</div>

</div>

</div>

To create a HSV-like color space, we want to find a mapping so that the cusp of the triangle is in <span class="katex"><span class="katex-mathml">$`s=1`$</span></span> and <span class="katex"><span class="katex-mathml">$`v=1`$</span></span>. We also want to change the triangle shape into a square, by stretching the lower part of the triangle.

To find the cusp we can use the same method as in my previous post about [sRGB gamut clipping](https://bottosson.github.io/posts/gamutclipping/).

If we perform this remapping we get the following result:

<div class="has-background-white-ter columns">

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsv_3_sv_7.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Yellow" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsv_3_sv_16.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Blue" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsv_3_sv_22.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Magenta" />

</div>

</div>

</div>

Remaining now is a small curve at the top, that we also have to remove. This is done by scaling <span class="katex"><span class="katex-mathml">$`v`$</span></span> to compensate. This step makes the space less uniform perceptually, but is needed to fit the sRGB gamut to a cylinder exactly. The change is quite small however. This gives the following result:

<div class="has-background-white-ter columns">

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsv_4_sv_7.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Yellow" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsv_4_sv_16.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Blue" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsv_4_sv_22.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Magenta" />

</div>

</div>

</div>

As an additional step we adjust saturation to be more uniform for low saturation colors. This makes it easier to compare saturation values for different colors, when saturation is low. The effect of this is subtle.

<div class="has-background-white-ter columns">

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsv_5_sv_7.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Yellow" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsv_5_sv_16.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Blue" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsv_5_sv_22.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Magenta" />

</div>

</div>

</div>

This gives us a new model with a simple geometrical shape and a hue parameter that closely matches perception. Overall the space will be very familiar to someone who is used to HSV, but with improved perceptual uniformity.

#### Okhwb <a href="#okhwb" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

If desired, Okhsv can also be converted to a HWB (hue, whiteness and blackness) form.

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`w = (1-s) v`$</span></span></span>

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`b = 1-v`$</span></span></span>

With the inverse:

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`s = 1-\frac{w}{1-b}`$</span></span></span>

<span class="katex-display"><span class="katex"><span class="katex-mathml">$`v = 1-b`$</span></span></span>

### Okhsl <a href="#okhsl" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

To derive Okhsl we also start with OkLCh. <span class="katex"><span class="katex-mathml">$`L_r`$</span></span> and <span class="katex"><span class="katex-mathml">$`h`$</span></span> are kept as is, with <span class="katex"><span class="katex-mathml">$`L_r`$</span></span> referred to as <span class="katex"><span class="katex-mathml">$`l`$</span></span> instead for consistency.

For <span class="katex"><span class="katex-mathml">$`s`$</span></span> we want to somehow remap <span class="katex"><span class="katex-mathml">$`C`$</span></span> so that the sRGB gamut nicely fits into a cylinder.

The simplest way to do this is to simply scale it by the maximum chroma inside the sRGB gamut for a given value of <span class="katex"><span class="katex-mathml">$`l`$</span></span> and <span class="katex"><span class="katex-mathml">$`h`$</span></span>, <span class="katex"><span class="katex-mathml">$`C_{max}(h, l)`$</span></span>, which is what HSLuv does. As we have seen with HSLuv though, the unevenness of the shape of the gamut will affect the interior of the entire space resulting in an uneven scale for the <span class="katex"><span class="katex-mathml">$`s`$</span></span> component.

Instead it would be good if we could find a way to keep the unevenness local to colors close to the edge of the gamut, leaving the interior less affected. This is the key idea behind Okhsl.

One way to solve this would be to solve it as a boundary value problem, finding <span class="katex"><span class="katex-mathml">$`C = f(h, s, l)`$</span></span>, with a boundary condition that <span class="katex"><span class="katex-mathml">$`C = C_{max}(h, l)`$</span></span> and some set of differential equation that keeps the interior smooth. This approach could definitely give a good result and would be interesting to explore, but is likely to only have a numerical solution, which would make it hard to use practically to construct a color space.

Instead Okhsl uses a fairly ad-hoc approach to create a smoothly varying interior, since that makes it efficient to run and easy to invert.

Instead of scaling <span class="katex"><span class="katex-mathml">$`s`$</span></span> by a single value for <span class="katex"><span class="katex-mathml">$`C`$</span></span>, the max possible value in the gamut, three different values are used, one for low values of <span class="katex"><span class="katex-mathml">$`s`$</span></span>, <span class="katex"><span class="katex-mathml">$`C_0`$</span></span>, one for midrange values of <span class="katex"><span class="katex-mathml">$`s`$</span></span>, <span class="katex"><span class="katex-mathml">$`C_{mid}`$</span></span> and one for large values, <span class="katex"><span class="katex-mathml">$`C_{max}`$</span></span>. These are constructed the following way:

- <span class="katex"><span class="katex-mathml">$`C_0(l)`$</span></span> is constructed to be independent of hue, this way creating continuity for colors close to the <span class="katex"><span class="katex-mathml">$`s=0`$</span></span> axis.
- <span class="katex"><span class="katex-mathml">$`C_{mid}(h, l)`$</span></span> is constructed to be closer in shape to <span class="katex"><span class="katex-mathml">$`C_max`$</span></span>, but still much smoother and has been constructed using an optimization process. See the source code for more details and the exact computation.
- <span class="katex"><span class="katex-mathml">$`C_{max}(h, l)`$</span></span> is the maximum possible value for <span class="katex"><span class="katex-mathml">$`C`$</span></span> in the sRGB gamut for the given values of <span class="katex"><span class="katex-mathml">$`l`$</span></span> and <span class="katex"><span class="katex-mathml">$`h`$</span></span>

To get an understanding of <span class="katex"><span class="katex-mathml">$`C_0`$</span></span>, <span class="katex"><span class="katex-mathml">$`C_{mid}`$</span></span> and <span class="katex"><span class="katex-mathml">$`C_{max}`$</span></span>, here are a few hue slices where <span class="katex"><span class="katex-mathml">$`C`$</span></span> is computed <span class="katex"><span class="katex-mathml">$`C = s C_0`$</span></span>, <span class="katex"><span class="katex-mathml">$`C = s C_{mid}`$</span></span> and <span class="katex"><span class="katex-mathml">$`C = s C_{max}`$</span></span> respectively.

<div class="has-background-white-ter columns">

<div class="column">

**<span class="katex"><span class="katex-mathml">$`C_0`$</span></span>**

</div>

<div class="column">

**<span class="katex"><span class="katex-mathml">$`C_{mid}`$</span></span>**

</div>

<div class="column">

**<span class="katex"><span class="katex-mathml">$`C_{max}`$</span></span>**

</div>

</div>

<div class="has-background-white-ter columns">

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_c_0_sv_7.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Yellow C_0" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_c_mid_sv_7.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Yellow C_mid" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_c_max_sv_7.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Yellow C_max" />

</div>

</div>

</div>

<div class="has-background-white-ter columns">

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_c_0_sv_16.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Blue C_0" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_c_mid_sv_16.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Blue C_mid" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_c_max_sv_16.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Blue C_max" />

</div>

</div>

</div>

<div class="has-background-white-ter columns">

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_c_0_sv_22.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Magenta C_0" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_c_mid_sv_22.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Magenta C_mid" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_c_max_sv_22.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Magenta C_max" />

</div>

</div>

</div>

To create the full Okhsl model, the values are interpolated so that:

- At <span class="katex"><span class="katex-mathml">$`s=0`$</span></span>: <span class="katex"><span class="katex-mathml">$`\frac{\partial C}{\partial s} = C_0`$</span></span>, <span class="katex"><span class="katex-mathml">$`C=0`$</span></span>
- At <span class="katex"><span class="katex-mathml">$`s=0.8`$</span></span>: <span class="katex"><span class="katex-mathml">$`C=C_{mid}`$</span></span>
- At <span class="katex"><span class="katex-mathml">$`s=1.0`$</span></span>: <span class="katex"><span class="katex-mathml">$`C=C_{max}`$</span></span>

This gives the final Okhsl model:

<div class="has-background-white-ter columns">

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_sv_7.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Yellow" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_sv_16.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Blue" />

</div>

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/hsl_sv_22.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 512px) min(calc(var(--main-width) * 1), 512px);" decoding="async" loading="lazy" width="512" height="512" alt="Magenta" />

</div>

</div>

</div>

Altogether this gives a model with a simple geometrical shape that has parameters for lightness and hue that closely match perception. The model is quite different from regular HSL, in order to achieve a better lightness estimate. I believe Okhsl delivers a better overall compromise, and keeps many of the benefits of Lab-like color spaces, without the complexity of an irregular shape.

Here are a few examples of slices Okhsl, with constant lightness and saturation:

<div class="has-background-white-ter columns">

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/okhsl_circle.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 257px) min(calc(var(--main-width) * 1), 257px);" decoding="async" loading="lazy" width="257" height="257" alt="Okhsl Constant Lightness" />

</div>

Example of constant “lightness” in Okhsl.

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/okhsl_s_slice.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 257px) min(calc(var(--main-width) * 1), 257px);" decoding="async" loading="lazy" width="257" height="257" alt="Okhsl Constant Saturation" />

</div>

Slice of colors with constant “saturation” in Okhsl. While not matching perceived chroma fully it is smoothly varying.

</div>

<div class="column">

<div class="box has-background-grey-light">

<img src="/img/colorpicker/okhsl_s_slice_100.png" style="background-size:cover;contain-intrinsic-size: min(var(--main-width), 257px) min(calc(var(--main-width) * 1), 257px);" decoding="async" loading="lazy" width="257" height="257" alt="Okhsl Constant Saturation" />

</div>

For 100% ‘saturation’ the variation in perceived chroma is larger, due to the shape of the sRGB gamut.

</div>

</div>

### Summary <a href="#summary-2" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

For completeness, here is a table of how Okhsv and Okhsl match the desired properties from earlier. Again, this is definitely a bit subjective. A better way to judge the performance is to just [try the results yourself](http://bottosson.github.io/misc/colorpicker).

|                          | Okhsv   | Okhsl |
|--------------------------|---------|-------|
| Orthogonal Lightness     | no      | yes   |
| Orthogonal Chroma        | no      | no    |
| Orthogonal Saturation    | partial | no    |
| Orthogonal Hue           | yes     | yes   |
| Simple Geometrical Shape | yes     | yes   |
| Max Chroma at Edge       | yes     | no    |
| Varies Smoothly          | yes     | yes   |
| Varies Evenly            | no      | no    |

## Ideas for future work <a href="#ideas-for-future-work" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

Okhsv and Okhsl are my attempts at making better color pickers for the sRGB gamut. I would love to see more experimentation overall with color picker design and in the next few years, color pickers for wide gamut and HDR will be more and more important and need a lot of research. They both offer their own new challenges.

Wide gamut is challenging since we are seeing an increased variety of different gamuts. At least for a while, target color spaces will be much more varied and applications for authoring colors will have to either settle for common subset or have to deal with this complexity. This of course will have a big impact on what color pickers look like and how they behave.

One interesting avenue to pursue would be to more automatically create color spaces like Okhsv and Okhsl for a given color gamut. This would likely need to use a bit of a different approach, maybe using lookup tables and numerical solutions in order to not need as much handcrafted logic.

HDR also has the issue of not being quite standardized, but an added complexity is the increased dynamic range and variation is absolute brightness. In the past color pickers have been able to mostly ignore how the eye adapts to different luminance levels, but this does not work as well with HDR. So far the approaches I’ve seen are to use regular SDR color pickers, but with and added exposure/intensity control. Is this the best approach or are there new ways we should be working with HDR color pickers?

An additional thing to explore is what spacing of hues would be the best. Okhsl and Okhsv simply inherit their spacing from Oklab. A different option could be to do a remapping similar to NCS, which would make the parameter vary less evenly, but could make it easier to use by mapping the different axes to more familiar colors.

## Source Code <a href="#source-code" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

Here is the Source Code for conversion between sRGB, HSL and HSV. This code depends on the code from my previous post [sRGB gamut clipping](https://bottosson.github.io/posts/gamutclipping/), which is not included here. You can find the source for both posts combined [here](http://bottosson.github.io/misc/ok_color.h) as a C++ header.

The [interactive comparison of color pickers](http://bottosson.github.io/misc/colorpicker) also has an implementation of this in JavaScript. The source is available [here](https://github.com/bottosson/bottosson.github.io/tree/master/misc/colorpicker).

### License <a href="#license" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

All the source code on this page is provided under the MIT license:

    Copyright (c) 2021 Björn Ottosson

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
    of the Software, and to permit persons to whom the Software is furnished to do
    so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

### Common code <a href="#common-code" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

``` language-cpp
struct HSV { float h; float s; float v; };
struct HSL { float h; float s; float l; };
struct LC { float L; float C; };

// Alternative representation of (L_cusp, C_cusp)
// Encoded so S = C_cusp/L_cusp and T = C_cusp/(1-L_cusp) 
// The maximum value for C in the triangle is then found as fmin(S*L, T*(1-L)), for a given L
struct ST { float S; float T; };

// toe function for L_r
float toe(float x)
{
   constexpr float k_1 = 0.206f;
    constexpr float k_2 = 0.03f;
 constexpr float k_3 = (1.f + k_1) / (1.f + k_2);
   return 0.5f * (k_3 * x - k_1 + sqrtf((k_3 * x - k_1) * (k_3 * x - k_1) + 4 * k_2 * k_3 * x));
}

// inverse toe function for L_r
float toe_inv(float x)
{
 constexpr float k_1 = 0.206f;
    constexpr float k_2 = 0.03f;
 constexpr float k_3 = (1.f + k_1) / (1.f + k_2);
   return (x * x + k_1 * x) / (k_3 * (x + k_2));
}

ST to_ST(LC cusp)
{
    float L = cusp.L;
  float C = cusp.C;
  return { C / L, C / (1 - L) };
}
```

### HSV <a href="#hsv-2" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

This code converts between sRGB (not linear) and Okhsv.

``` language-cpp
struct HSV { float h; float s; float v; };
RGB okhsv_to_srgb(HSV hsv)
{
   float h = hsv.h;
   float s = hsv.s;
   float v = hsv.v;

   float a_ = cosf(2.f * pi * h);
    float b_ = sinf(2.f * pi * h);
    
    LC cusp = find_cusp(a_, b_);
    ST ST_max = to_ST(cusp);
   float S_max = ST_max.S;
    float T_max = ST_max.T;
    float S_0 = 0.5f;
   float k = 1 - S_0 / S_max;

  // first we compute L and V as if the gamut is a perfect triangle:

   // L, C when v==1:
   float L_v = 1     - s * S_0 / (S_0 + T_max - T_max * k * s);
  float C_v = s * T_max * S_0 / (S_0 + T_max - T_max * k * s);

    float L = v * L_v;
    float C = v * C_v;

    // then we compensate for both toe and the curved top part of the triangle:
  float L_vt = toe_inv(L_v);
  float C_vt = C_v * L_vt / L_v;

    float L_new = toe_inv(L);
   C = C * L_new / L;
   L = L_new;

   RGB rgb_scale = oklab_to_linear_srgb({ L_vt, a_ * C_vt, b_ * C_vt });
  float scale_L = cbrtf(1.f / fmax(fmax(rgb_scale.r, rgb_scale.g), fmax(rgb_scale.b, 0.f)));

  L = L * scale_L;
 C = C * scale_L;

 RGB rgb = oklab_to_linear_srgb({ L, C * a_, C * b_ });
 return {
      srgb_transfer_function(rgb.r),
      srgb_transfer_function(rgb.g),
      srgb_transfer_function(rgb.b),
  };
}

HSV srgb_to_okhsv(RGB rgb)
{
    Lab lab = linear_srgb_to_oklab({
      srgb_transfer_function_inv(rgb.r),
      srgb_transfer_function_inv(rgb.g),
      srgb_transfer_function_inv(rgb.b)
      });

    float C = sqrtf(lab.a * lab.a + lab.b * lab.b);
 float a_ = lab.a / C;
  float b_ = lab.b / C;

  float L = lab.L;
   float h = 0.5f + 0.5f * atan2f(-lab.b, -lab.a) / pi;

   LC cusp = find_cusp(a_, b_);
    ST ST_max = to_ST(cusp);
   float S_max = ST_max.S;
    float T_max = ST_max.T;
    float S_0 = 0.5f;
   float k = 1 - S_0 / S_max;

  // first we find L_v, C_v, L_vt and C_vt

 float t = T_max / (C + L * T_max);
  float L_v = t * L;
    float C_v = t * C;

    float L_vt = toe_inv(L_v);
  float C_vt = C_v * L_vt / L_v;

    // we can then use these to invert the step that compensates for the toe and the curved top part of the triangle:
    RGB rgb_scale = oklab_to_linear_srgb({ L_vt, a_ * C_vt, b_ * C_vt });
  float scale_L = cbrtf(1.f / fmax(fmax(rgb_scale.r, rgb_scale.g), fmax(rgb_scale.b, 0.f)));

  L = L / scale_L;
 C = C / scale_L;

 C = C * toe(L) / L;
    L = toe(L);

    // we can now compute v and s:

   float v = L / L_v;
    float s = (S_0 + T_max) * C_v / ((T_max * S_0) + T_max * k * C_v);

  return { h, s, v };
}
```

### HSL <a href="#hsl-2" class="anchor-link"><span class="icon is-small"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA1MTIgNTEyIiB2ZXJzaW9uPSIxLjEiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48cGF0aCBkPSJNNDU5LjY1NCwyMzMuMzczbC05MC41MzEsOTAuNWMtNDkuOTY5LDUwLTEzMS4wMzEsNTAtMTgxLDBjLTcuODc1LTcuODQ0LTE0LjAzMS0xNi42ODgtMTkuNDM4LTI1LjgxMyAgbDQyLjA2My00Mi4wNjNjMi0yLjAxNiw0LjQ2OS0zLjE3Miw2LjgyOC00LjUzMWMyLjkwNiw5LjkzOCw3Ljk4NCwxOS4zNDQsMTUuNzk3LDI3LjE1NmMyNC45NTMsMjQuOTY5LDY1LjU2MywyNC45MzgsOTAuNSwwICBsOTAuNS05MC41YzI0Ljk2OS0yNC45NjksMjQuOTY5LTY1LjU2MywwLTkwLjUxNmMtMjQuOTM4LTI0Ljk1My02NS41MzEtMjQuOTUzLTkwLjUsMGwtMzIuMTg4LDMyLjIxOSAgYy0yNi4xMDktMTAuMTcyLTU0LjI1LTEyLjkwNi04MS42NDEtOC44OTFsNjguNTc4LTY4LjU3OGM1MC00OS45ODQsMTMxLjAzMS00OS45ODQsMTgxLjAzMSwwICBDNTA5LjYyMywxMDIuMzQyLDUwOS42MjMsMTgzLjM4OSw0NTkuNjU0LDIzMy4zNzN6IE0yMjAuMzI2LDM4Mi4xODZsLTMyLjIwMywzMi4yMTljLTI0Ljk1MywyNC45MzgtNjUuNTYzLDI0LjkzOC05MC41MTYsMCAgYy0yNC45NTMtMjQuOTY5LTI0Ljk1My02NS41NjMsMC05MC41MzFsOTAuNTE2LTkwLjVjMjQuOTY5LTI0Ljk2OSw2NS41NDctMjQuOTY5LDkwLjUsMGM3Ljc5Nyw3Ljc5NywxMi44NzUsMTcuMjAzLDE1LjgxMywyNy4xMjUgIGMyLjM3NS0xLjM3NSw0LjgxMy0yLjUsNi44MTMtNC41bDQyLjA2My00Mi4wNDdjLTUuMzc1LTkuMTU2LTExLjU2My0xNy45NjktMTkuNDM4LTI1LjgyOGMtNDkuOTY5LTQ5Ljk4NC0xMzEuMDMxLTQ5Ljk4NC0xODEuMDE2LDAgIGwtOTAuNSw5MC41Yy00OS45ODQsNTAtNDkuOTg0LDEzMS4wMzEsMCwxODEuMDMxYzQ5Ljk4NCw0OS45NjksMTMxLjAzMSw0OS45NjksMTgxLjAxNiwwbDY4LjU5NC02OC41OTQgIEMyNzQuNTYxLDM5NS4wOTIsMjQ2LjQyLDM5Mi4zNDIsMjIwLjMyNiwzODIuMTg2eiIgLz48L3N2Zz4=" /><span></span></span></a>

This code converts between sRGB (not linear) and Okhsl.

``` language-cpp
struct HSL { float h; float s; float l; };

// Returns a smooth approximation of the location of the cusp
// This polynomial was created by an optimization process
// It has been designed so that S_mid < S_max and T_mid < T_max
ST get_ST_mid(float a_, float b_)
{
   float S = 0.11516993f + 1.f / (
       +7.44778970f + 4.15901240f * b_
     + a_ * (-2.19557347f + 1.75198401f * b_
          + a_ * (-2.13704948f - 10.02301043f * b_
             + a_ * (-4.24894561f + 5.38770819f * b_ + 4.69891013f * a_
                 )))
        );

    float T = 0.11239642f + 1.f / (
       +1.61320320f - 0.68124379f * b_
     + a_ * (+0.40370612f + 0.90148123f * b_
          + a_ * (-0.27087943f + 0.61223990f * b_
              + a_ * (+0.00299215f - 0.45399568f * b_ - 0.14661872f * a_
                 )))
        );

    return { S, T };
}

struct Cs { float C_0; float C_mid; float C_max; };
Cs get_Cs(float L, float a_, float b_)
{
   LC cusp = find_cusp(a_, b_);

    float C_max = find_gamut_intersection(a_, b_, L, 1, L, cusp);
  ST ST_max = to_ST(cusp);
   
    // Scale factor to compensate for the curved part of gamut shape:
    float k = C_max / fmin((L * ST_max.S), (1 - L) * ST_max.T);

  float C_mid;
  {
        ST ST_mid = get_ST_mid(a_, b_);

     // Use a soft minimum function, instead of a sharp triangle shape to get a smooth value for chroma.
      float C_a = L * ST_mid.S;
      float C_b = (1.f - L) * ST_mid.T;
      C_mid = 0.9f * k * sqrtf(sqrtf(1.f / (1.f / (C_a * C_a * C_a * C_a) + 1.f / (C_b * C_b * C_b * C_b))));
    }

    float C_0;
    {
        // for C_0, the shape is independent of hue, so ST are constant. Values picked to roughly be the average values of ST.
       float C_a = L * 0.4f;
       float C_b = (1.f - L) * 0.8f;

       // Use a soft minimum function, instead of a sharp triangle shape to get a smooth value for chroma.
      C_0 = sqrtf(1.f / (1.f / (C_a * C_a) + 1.f / (C_b * C_b)));
    }

    return { C_0, C_mid, C_max };
}

RGB okhsl_to_srgb(HSL hsl)
{
 float h = hsl.h;
   float s = hsl.s;
   float l = hsl.l;

   if (l == 1.0f)
   {
        return { 1.f, 1.f, 1.f };
   }

    else if (l == 0.f)
    {
        return { 0.f, 0.f, 0.f };
   }

    float a_ = cosf(2.f * pi * h);
    float b_ = sinf(2.f * pi * h);
    float L = toe_inv(l);

   Cs cs = get_Cs(L, a_, b_);
   float C_0 = cs.C_0;
    float C_mid = cs.C_mid;
    float C_max = cs.C_max;

    // Interpolate the three values for C so that:
    // At s=0: dC/ds = C_0, C=0
    // At s=0.8: C=C_mid
    // At s=1.0: C=C_max

   float mid = 0.8f;
   float mid_inv = 1.25f;

  float C, t, k_0, k_1, k_2;

    if (s < mid)
    {
        t = mid_inv * s;

     k_1 = mid * C_0;
     k_2 = (1.f - k_1 / C_mid);

       C = t * k_1 / (1.f - k_2 * t);
   }
    else
 {
        t = (s - mid)/ (1 - mid);

      k_0 = C_mid;
     k_1 = (1.f - mid) * C_mid * C_mid * mid_inv * mid_inv / C_0;
     k_2 = (1.f - (k_1) / (C_max - C_mid));

       C = k_0 + t * k_1 / (1.f - k_2 * t);
 }

    RGB rgb = oklab_to_linear_srgb({ L, C * a_, C * b_ });
 return {
      srgb_transfer_function(rgb.r),
      srgb_transfer_function(rgb.g),
      srgb_transfer_function(rgb.b),
  };
}

HSL srgb_to_okhsl(RGB rgb)
{
    Lab lab = linear_srgb_to_oklab({
      srgb_transfer_function_inv(rgb.r),
      srgb_transfer_function_inv(rgb.g),
      srgb_transfer_function_inv(rgb.b)
      });

    float C = sqrtf(lab.a * lab.a + lab.b * lab.b);
 float a_ = lab.a / C;
  float b_ = lab.b / C;

  float L = lab.L;
   float h = 0.5f + 0.5f * atan2f(-lab.b, -lab.a) / pi;

   Cs cs = get_Cs(L, a_, b_);
   float C_0 = cs.C_0;
    float C_mid = cs.C_mid;
    float C_max = cs.C_max;

    // Inverse of the interpolation in okhsl_to_srgb:

    float mid = 0.8f;
   float mid_inv = 1.25f;

  float s;
  if (C < C_mid)
  {
        float k_1 = mid * C_0;
        float k_2 = (1.f - k_1 / C_mid);

      float t = C / (k_1 + k_2 * C);
      s = t * mid;
 }
    else
 {
        float k_0 = C_mid;
        float k_1 = (1.f - mid) * C_mid * C_mid * mid_inv * mid_inv / C_0;
        float k_2 = (1.f - (k_1) / (C_max - C_mid));

      float t = (C - k_0) / (k_1 + k_2 * (C - k_0));
      s = mid + (1.f - mid) * t;
   }

    float l = toe(L);
   return { h, s, l };
}
```

------------------------------------------------------------------------

If you liked this article, it would be great if you considered sharing it:

<div class="buttons">

<a href="https://twitter.com/intent/tweet/?text=Two%20new%20color%20spaces%20for%20color%20picking%20-%20Okhsv%20and%20Okhsl&amp;url=https%3A%2F%2Fbottosson.github.io%2Fposts%2Fcolorpicker%2F" class="is-small button resp-sharing-button--twitter" rel="noopener" target="_blank" aria-label="Share on Twitter"><span class="icon resp-sharing-button__icon resp-sharing-button__icon--solid"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgaGVpZ2h0PSIyNCIgd2lkdGg9IjI0Ij48cGF0aCBkPSJNMjMuNDQgNC44M2MtLjguMzctMS41LjM4LTIuMjIuMDIuOTMtLjU2Ljk4LS45NiAxLjMyLTIuMDItLjg4LjUyLTEuODYuOS0yLjkgMS4xLS44Mi0uODgtMi0xLjQzLTMuMy0xLjQzLTIuNSAwLTQuNTUgMi4wNC00LjU1IDQuNTQgMCAuMzYuMDMuNy4xIDEuMDQtMy43Ny0uMi03LjEyLTItOS4zNi00Ljc1LS40LjY3LS42IDEuNDUtLjYgMi4zIDAgMS41Ni44IDIuOTUgMiAzLjc3LS43NC0uMDMtMS40NC0uMjMtMi4wNS0uNTd2LjA2YzAgMi4yIDEuNTYgNC4wMyAzLjY0IDQuNDQtLjY3LjItMS4zNy4yLTIuMDYuMDguNTggMS44IDIuMjYgMy4xMiA0LjI1IDMuMTZDNS43OCAxOC4xIDMuMzcgMTguNzQgMSAxOC40NmMyIDEuMyA0LjQgMi4wNCA2Ljk3IDIuMDQgOC4zNSAwIDEyLjkyLTYuOTIgMTIuOTItMTIuOTMgMC0uMiAwLS40LS4wMi0uNi45LS42MyAxLjk2LTEuMjIgMi41Ni0yLjE0eiIgLz48L3N2Zz4=" /> </span></a><a href="mailto:?subject=Two%20new%20color%20spaces%20for%20color%20picking%20-%20Okhsv%20and%20Okhsl&amp;body=https%3A%2F%2Fbottosson.github.io%2Fposts%2Fcolorpicker%2F" class="is-small button resp-sharing-button--email" rel="noopener" target="_self" aria-label="Share by E-Mail"><span class="icon resp-sharing-button__icon resp-sharing-button__icon--solid"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgaGVpZ2h0PSIyNCIgd2lkdGg9IjI0Ij48cGF0aCBkPSJNMjIgNEgyQy45IDQgMCA0LjkgMCA2djEyYzAgMS4xLjkgMiAyIDJoMjBjMS4xIDAgMi0uOSAyLTJWNmMwLTEuMS0uOS0yLTItMnpNNy4yNSAxNC40M2wtMy41IDJjLS4wOC4wNS0uMTcuMDctLjI1LjA3LS4xNyAwLS4zNC0uMS0uNDMtLjI1LS4xNC0uMjQtLjA2LS41NS4xOC0uNjhsMy41LTJjLjI0LS4xNC41NS0uMDYuNjguMTguMTQuMjQuMDYuNTUtLjE4LjY4em00Ljc1LjA3Yy0uMSAwLS4yLS4wMy0uMjctLjA4bC04LjUtNS41Yy0uMjMtLjE1LS4zLS40Ni0uMTUtLjcuMTUtLjIyLjQ2LS4zLjctLjE0TDEyIDEzLjRsOC4yMy01LjMyYy4yMy0uMTUuNTQtLjA4LjcuMTUuMTQuMjMuMDcuNTQtLjE2LjdsLTguNSA1LjVjLS4wOC4wNC0uMTcuMDctLjI3LjA3em04LjkzIDEuNzVjLS4xLjE2LS4yNi4yNS0uNDMuMjUtLjA4IDAtLjE3LS4wMi0uMjUtLjA3bC0zLjUtMmMtLjI0LS4xMy0uMzItLjQ0LS4xOC0uNjhzLjQ0LS4zMi42OC0uMThsMy41IDJjLjI0LjEzLjMyLjQ0LjE4LjY4eiIgLz48L3N2Zz4=" /> </span></a><a href="https://reddit.com/submit/?url=https%3A%2F%2Fbottosson.github.io%2Fposts%2Fcolorpicker%2F&amp;resubmit=true&amp;title=Two%20new%20color%20spaces%20for%20color%20picking%20-%20Okhsv%20and%20Okhsl" class="is-small button resp-sharing-button--reddit" rel="noopener" target="_blank" aria-label="Share on Reddit"><span class="icon resp-sharing-button__icon resp-sharing-button__icon--solid"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgaGVpZ2h0PSIyNCIgd2lkdGg9IjI0Ij48cGF0aCBkPSJNMjQgMTEuNWMwLTEuNjUtMS4zNS0zLTMtMy0uOTYgMC0xLjg2LjQ4LTIuNDIgMS4yNC0xLjY0LTEtMy43NS0xLjY0LTYuMDctMS43Mi4wOC0xLjEuNC0zLjA1IDEuNTItMy43LjcyLS40IDEuNzMtLjI0IDMgLjVDMTcuMiA2LjMgMTguNDYgNy41IDIwIDcuNWMxLjY1IDAgMy0xLjM1IDMtM3MtMS4zNS0zLTMtM2MtMS4zOCAwLTIuNTQuOTQtMi44OCAyLjIyLTEuNDMtLjcyLTIuNjQtLjgtMy42LS4yNS0xLjY0Ljk0LTEuOTUgMy40Ny0yIDQuNTUtMi4zMy4wOC00LjQ1LjctNi4xIDEuNzJDNC44NiA4Ljk4IDMuOTYgOC41IDMgOC41Yy0xLjY1IDAtMyAxLjM1LTMgMyAwIDEuMzIuODQgMi40NCAyLjA1IDIuODQtLjAzLjIyLS4wNS40NC0uMDUuNjYgMCAzLjg2IDQuNSA3IDEwIDdzMTAtMy4xNCAxMC03YzAtLjIyLS4wMi0uNDQtLjA1LS42NiAxLjItLjQgMi4wNS0xLjU0IDIuMDUtMi44NHpNMi4zIDEzLjM3QzEuNSAxMy4wNyAxIDEyLjM1IDEgMTEuNWMwLTEuMS45LTIgMi0yIC42NCAwIDEuMjIuMzIgMS42LjgyLTEuMS44NS0xLjkyIDEuOS0yLjMgMy4wNXptMy43LjEzYzAtMS4xLjktMiAyLTJzMiAuOSAyIDItLjkgMi0yIDItMi0uOS0yLTJ6bTkuOCA0LjhjLTEuMDguNjMtMi40Mi45Ni0zLjguOTYtMS40IDAtMi43NC0uMzQtMy44LS45NS0uMjQtLjEzLS4zMi0uNDQtLjItLjY4LjE1LS4yNC40Ni0uMzIuNy0uMTggMS44MyAxLjA2IDQuNzYgMS4wNiA2LjYgMCAuMjMtLjEzLjUzLS4wNS42Ny4yLjE0LjIzLjA2LjU0LS4xOC42N3ptLjItMi44Yy0xLjEgMC0yLS45LTItMnMuOS0yIDItMiAyIC45IDIgMi0uOSAyLTIgMnptNS43LTIuMTNjLS4zOC0xLjE2LTEuMi0yLjItMi4zLTMuMDUuMzgtLjUuOTctLjgyIDEuNi0uODIgMS4xIDAgMiAuOSAyIDIgMCAuODQtLjUzIDEuNTctMS4zIDEuODd6IiAvPjwvc3ZnPg==" /> </span></a><a href="https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbottosson.github.io%2Fposts%2Fcolorpicker%2F&amp;t=Two%20new%20color%20spaces%20for%20color%20picking%20-%20Okhsv%20and%20Okhsl" class="is-small button resp-sharing-button--hackernews" rel="noopener" target="_blank" aria-label="Share on Hacker News"><span class="icon resp-sharing-button__icon resp-sharing-button__icon--solid"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQwIDE0MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBoZWlnaHQ9IjI0IiB3aWR0aD0iMjQiPjxwYXRoIGQ9Ik02MC45NCA4Mi4zMTRMMTcgMGgyMC4wOGwyNS44NSA1Mi4wOTNjLjM5Ny45MjcuODYgMS44ODggMS4zOSAyLjg4My41My45OTQuOTk1IDIuMDIgMS4zOTMgMy4wOC4yNjUuNC40NjMuNzY0LjU5NiAxLjA5NS4xMy4zMzQuMjYyLjYzLjM5NS44OTguNjYyIDEuMzI1IDEuMjYgMi42MTggMS43OSAzLjg3Ny41MyAxLjI2Ljk5MyAyLjQyIDEuMzkgMy40OCAxLjA2LTIuMjU0IDIuMjItNC42NzMgMy40OC03LjI1OCAxLjI2LTIuNTg1IDIuNTUyLTUuMjcgMy44NzctOC4wNTJMMTAzLjQ5IDBoMTguNjlMNzcuODQgODMuMzA4djUzLjA4N2gtMTYuOXYtNTQuMDh6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+PC9zdmc+" /> </span></a><a href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Fbottosson.github.io%2Fposts%2Fcolorpicker%2F&amp;title=Two%20new%20color%20spaces%20for%20color%20picking%20-%20Okhsv%20and%20Okhsl&amp;source=https%3A%2F%2Fbottosson.github.io%2Fposts%2Fcolorpicker%2F" class="is-small button resp-sharing-button--linkedin" rel="noopener" target="_blank" aria-label="Share on LinkedIn"><span class="icon resp-sharing-button__icon resp-sharing-button__icon--solid"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgaGVpZ2h0PSIyNCIgd2lkdGg9IjI0Ij48cGF0aCBkPSJNNi41IDIxLjVoLTV2LTEzaDV2MTN6TTQgNi41QzIuNSA2LjUgMS41IDUuMyAxLjUgNHMxLTIuNCAyLjUtMi40YzEuNiAwIDIuNSAxIDIuNiAyLjUgMCAxLjQtMSAyLjUtMi42IDIuNXptMTEuNSA2Yy0xIDAtMiAxLTIgMnY3aC01di0xM2g1VjEwczEuNi0xLjUgNC0xLjVjMyAwIDUgMi4yIDUgNi4zdjYuN2gtNXYtN2MwLTEtMS0yLTItMnoiIC8+PC9zdmc+" /> </span></a><a href="https://facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbottosson.github.io%2Fposts%2Fcolorpicker%2F" class="is-small button resp-sharing-button--facebook" rel="noopener" target="_blank" aria-label="Share on Facebook"><span class="icon resp-sharing-button__icon resp-sharing-button__icon--solid"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgaGVpZ2h0PSIyNCIgd2lkdGg9IjI0Ij48cGF0aCBkPSJNMTguNzcgNy40NkgxNC41di0xLjljMC0uOS42LTEuMSAxLTEuMWgzVi41aC00LjMzQzEwLjI0LjUgOS41IDMuNDQgOS41IDUuMzJ2Mi4xNWgtM3Y0aDN2MTJoNXYtMTJoMy44NWwuNDItNHoiIC8+PC9zdmc+" /></span></a>

</div>

For discussions and feedback, <a href="https://twitter.com/bjornornorn" rel="noopener" target="_blank">ping me on Twitter.</a>

Published 08 Sep 2021

</div>

</div>
