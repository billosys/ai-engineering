# Image Composition and Accessible Exploration

Images can establish a page's subject, set a pace, or help someone find a story. Choose their size, crop, caption, alternative text and links from the actual task and image meaning. A dramatic frame is useful only while the content remains understandable and reachable.

Use this guide for an image-led article, collection or editorial sequence. It does not prescribe an image style, aspect ratio, palette, font, carousel or asset pipeline. Keep the adopting project's supplied identity and assets in charge. For a text-based worked case, see [Using the skill: image composition](using-the-skill.md#image-composition). The runnable LFE specimen is preserved outside the skill package.

## Start with the image's job

Before styling, inspect the actual image and ask what it contributes in this place:

- What subject or idea does it make visible?
- Which part matters at the smallest intended frame?
- Does nearby text already provide the same information?
- Is the image itself a control, or does it open the original at full size?
- What remains useful when the image or stylesheet is unavailable?

Use the answers to choose its role. The [WAI Images tutorial](https://www.w3.org/WAI/tutorials/images/) distinguishes informative, decorative, functional and complex images, among other cases. Its [alt decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/) asks about text in the image, link or button function, meaning in context, redundancy and decoration. This is a context decision: the same file can need different alternatives in different uses.

For an informative illustration, write a brief alternative that conveys the relevant visible subject. If it adds no information and is only decoration, use an empty `alt`. If the image is the only content of a link or button, name that link's destination or action. If it carries complex data or relationships, provide the information in nearby text as well; a short alternative alone cannot replace it. When nearby text already states the image's useful meaning, consider whether repeating that meaning in the alternative adds anything.

Keep the image's **alternative**, its **caption**, and any **link name** distinct. The alternative supports the image's role for people who do not see it; the caption can connect it to a story or explain its place in the collection; a link name describes what will happen. Do not make a caption carry an unstated control name, or repeat a long caption word for word in `alt` without a reason.

The [Microsoft Inclusive Design principles](https://inclusive.microsoft.design/) offer useful questions: recognize where a design may exclude, learn from diverse perspectives, and solve for one while extending to many. Apply those questions by checking image meaning, text alternatives, link purpose and fallback behavior. They are a method prompt, not evidence that this example was validated with participants; no participant research is claimed here.

## Frame the image without losing its subject

Treat the source image, frame and visible subject as separate things. A crop chooses which source pixels appear in a box. It does not change the original file. `object-fit: cover` preserves the image's aspect ratio while filling the frame, so some edges may be clipped. `contain` preserves the whole image inside the frame and may leave unused space. Intrinsic sizing (`width: 100%; height: auto`) keeps an image's full proportions when no crop is needed. These behaviors are defined in [CSS Images Module Level 3, §4.5](https://www.w3.org/TR/css-images-3/#the-object-fit).

Use `object-position` to align the image within a crop. Its default is centered; a value such as `60% 50%` shifts the alignment according to the concrete image size and frame. It is a starting choice, not a guarantee that the important subject stays visible at every size. See [CSS Images Module Level 3, §4.6](https://www.w3.org/TR/css-images-3/#the-object-position). The linked specification is a Candidate Recommendation Draft, so check its current status and the target browser when relying on changing or less common behavior.

For each intended frame, identify the subject's **safe area**: the region that must remain visible for this story to make sense. Compare the source and rendered crop at the actual narrow and wide sizes. If the subject shifts, revise the frame, focal position or layout. Do not cover it with text whose position depends on an image's variable composition. Offer an ordinary full-image link when a crop removes meaningful context, and make its link name clear.

An illustration can be art-directed as a prominent lead while later images remain quiet, intact features. A responsive ratio can support that contrast, but no ratio is inherently editorial or accessible. Let the page's content spacing and available room decide whether image and text sit beside each other or stack. Preserve the source reading order when columns wrap; do not reverse the visual sequence away from the document sequence.

**Do not crop a technical diagram just to imitate an illustrative frame.** If every label, connection or data point matters, keep the complete diagram available and supply a nearby text explanation or data equivalent. A good crop for atmosphere may be a bad crop for information.

## Let other visual material carry meaning

Shape, line and texture can group a story or distinguish a section. Use them where they clarify a real relationship: a rule may separate two pieces, a repeated edge may mark a shared group, and texture may remain part of an illustration. Check that the relationship is still clear without color alone. A purely ornamental shape should not resemble an unlabeled control or add a competing focal point.

Use an icon when its function or subject is clearer than text alone, and provide the accessible name from its actual role. A functional icon control needs a name for its action; a decorative icon beside the same visible label can often be hidden from assistive technology. Do not force icons or new decoration into an image-led page that already has clear text and supplied artwork.

## Check the complete reading path

Keep the document meaningful before styling: a page title, a visible text index, story headings in sequence, article summaries, dates and ordinary links. Use native anchors for in-page navigation, and make fragment destinations programmatically focusable when needed so keyboard users can continue from the destination. Keep visible focus. Make a skip link useful when the page introduces repeated navigation or a long preamble.

For every story, keep the image near the title and summary it illustrates. Use a caption to make the relationship explicit where it may not be obvious. Keep the article link separate from a link to the full illustration, and use names that distinguish those destinations. Never make hover, animation, a carousel, or an image load the only way to reach essential text or controls.

Test the authored page at the widths and content scale that matter. Check that the intended subject remains visible, the source order remains coherent, captions and alternatives do different work, index and return links move focus as expected, and longer text can wrap or stack. Then check a missing-image case and a no-styles case: titles, summaries, dates and article links should still form a useful path. Intrinsic images may exceed a narrow viewport when CSS is absent; if unstyled responsive fit is required, add an explicit fallback and test it instead of implying that intrinsic sizing guarantees it.

When local project images are reused, preserve their supplied bytes and record their source in the example. Do not infer an artist, license or external distribution permission from a local file. The LFE runtime specimen used byte-for-byte copies supplied in its source checkout for local use; that historical statement does not resolve what rights permit. The copies are removed from the skill. This Markdown package neither redistributes nor depends on the artwork; any separate publication of those images needs its own rights disposition.
