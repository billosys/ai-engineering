# Slice05 source comparison and model evidence

SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`. This evidence packet covers the seven assigned windows. The complete inventory, corrected local pairs, exact rational model, one current action registry and future Arc03 handoff follow. Values are models rather than browser observations.

## Primary source comparison

| ID | Source and exact inspected scope | Supports | Limit retained |
|---|---|---|---|
| CV | [CSS Values and Units Level 4, Working Draft 12 Mar 2024](https://www.w3.org/TR/2024/WD-css-values-4-20240312/): full §6.1.1 rem and user minimum-font notes; §6.1.2 intro and all §6.1.2.2 variants; complete §10.2 comparison functions. | `rem` equals computed `em` on root; minimum-font preference may affect used values without changing font-relative resolution; `vi` is 1% of the applicable viewport variant on the element inline axis; `clamp` clamps central value and favors minimum if bounds conflict. | Normative definitions do not predict browser/user setting outcomes for these pages or accessibility conformance. Draft is identified as work in progress. |
| WC | [WCAG 2.2 Recommendation 12 Dec 2024](https://www.w3.org/TR/2024/REC-WCAG22-20241212/): complete normative SC 1.4.4 and 1.4.10, including notes/exceptions. | AA SC 1.4.4 requires text (except captions/images of text) resizable to 200% without loss; AA SC 1.4.10 addresses no loss and no two-dimensional scroll at 320 CSS px width for vertical-scroll content or 256 CSS px height for horizontal-scroll content, except content requiring 2-D layout for use/meaning. | Neither criterion is satisfied by unit choice alone; requires content/functionality testing. |
| RT | [Understanding SC 1.4.4](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html): complete criterion/intent, all three intent notes and guidance through resize mechanisms. | Informative guidance says at least one supported user-agent text-scaling mechanism can suffice; intermediate offered steps must preserve content/functionality; page zoom, text-only, and text-size settings are distinct possible methods. | Understanding is informative, not the normative SC; not every mechanism is mandated. |
| RF | [Understanding SC 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html): criterion/notes/intent, full Basic text reflow and reflowing-site sections. | Horizontal languages reflow at width 320; vertical-language sections at height 256; 2-D-use exceptions remain, while table cells still need reflow. | Informative explanation and examples are not runtime evidence or conformance checks. |
| F94 | [Failure F94](https://www.w3.org/WAI/WCAG22/Techniques/failures/F94): complete technique body, examples, test procedure and expected result; page reports update 9 Mar 2026. | Viewport units used as primary text-size method are likely to fail 1.4.4; some uses may not prevent adjustment; media queries/author controls can be alternatives. | Failure technique has qualifications and alternatives; it does not show all mixed rem/vi clamps fail or ban viewport units. |
| UT | [Utopia calculator](https://utopia.fyi/type/calculator/): complete 66-line returned text, default inputs and complete generated CSS. | Current returned default displays min 360px / 18px / 1.2 and max 1240px / 20px / 1.25; generated CSS uses `vw`. | A live calculator state, not a historical capture, author attribution, universal configuration or evidence of accessibility. Dynamic UI not exercised. |

## Literal coefficient model: all 144 evaluations

Each row binds one formula × R × I × z key (4×3×3×4). It reports F(R,I), its branch, F(R,I/z), its branch, assumed apparent zF and ratio to baseline. Formula coefficients are exact decimals parsed from SOURCE declarations; zoom fixes R and reduces I.

```json
{"formula_coefficients":[{"formula_id":"SK195","source_path":"knowledge/design/SKILL.md","source_line":195,"declaration":"--step-0: clamp(1rem, 0.9015rem + 0.4924vi, 1.3337rem);","token":"step-0","minimum_root":"1","preferred_root":"0.9015","viewport_coefficient":"0.4924","maximum_root":"1.3337"},{"formula_id":"SK196","source_path":"knowledge/design/SKILL.md","source_line":196,"declaration":"--step-1: clamp(1.2rem, 1.0534rem + 0.7331vi, 1.7783rem);","token":"step-1","minimum_root":"1.2","preferred_root":"1.0534","viewport_coefficient":"0.7331","maximum_root":"1.7783"},{"formula_id":"SK200","source_path":"knowledge/design/SKILL.md","source_line":200,"declaration":"--space-m: clamp(1.5rem, 1.3523rem + 0.7385vi, 2.0006rem);","token":"space-m","minimum_root":"1.5","preferred_root":"1.3523","viewport_coefficient":"0.7385","maximum_root":"2.0006"},{"formula_id":"SK203","source_path":"knowledge/design/SKILL.md","source_line":203,"declaration":"--space-s-l: clamp(1rem, 0.5038rem + 2.4808vi, 2.6674rem);","token":"space-s-l","minimum_root":"1","preferred_root":"0.5038","viewport_coefficient":"2.4808","maximum_root":"2.6674"}],"evaluations":[{"formula_id":"SK195","R":"16","I":"360","z":"1","F_R_I":"101229/6250","F_R_I_branch":"inside","F_R_I_over_z":"101229/6250","F_R_I_over_z_branch":"inside","apparent_zF":"101229/6250","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK195","R":"16","I":"360","z":"5/4","F_R_I":"101229/6250","F_R_I_branch":"inside","F_R_I_over_z":"16","F_R_I_over_z_branch":"lower","apparent_zF":"20","apparent_ratio_to_F_R_I":"125000/101229"},{"formula_id":"SK195","R":"16","I":"360","z":"2","F_R_I":"101229/6250","F_R_I_branch":"inside","F_R_I_over_z":"16","F_R_I_over_z_branch":"lower","apparent_zF":"32","apparent_ratio_to_F_R_I":"200000/101229"},{"formula_id":"SK195","R":"16","I":"360","z":"4","F_R_I":"101229/6250","F_R_I_branch":"inside","F_R_I_over_z":"16","F_R_I_over_z_branch":"lower","apparent_zF":"64","apparent_ratio_to_F_R_I":"400000/101229"},{"formula_id":"SK195","R":"16","I":"800","z":"1","F_R_I":"11477/625","F_R_I_branch":"inside","F_R_I_over_z":"11477/625","F_R_I_over_z_branch":"inside","apparent_zF":"11477/625","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK195","R":"16","I":"800","z":"5/4","F_R_I":"11477/625","F_R_I_branch":"inside","F_R_I_over_z":"54923/3125","F_R_I_over_z_branch":"inside","apparent_zF":"54923/2500","apparent_ratio_to_F_R_I":"54923/45908"},{"formula_id":"SK195","R":"16","I":"800","z":"2","F_R_I":"11477/625","F_R_I_branch":"inside","F_R_I_over_z":"10246/625","F_R_I_over_z_branch":"inside","apparent_zF":"20492/625","apparent_ratio_to_F_R_I":"20492/11477"},{"formula_id":"SK195","R":"16","I":"800","z":"4","F_R_I":"11477/625","F_R_I_branch":"inside","F_R_I_over_z":"16","F_R_I_over_z_branch":"lower","apparent_zF":"64","apparent_ratio_to_F_R_I":"40000/11477"},{"formula_id":"SK195","R":"16","I":"1440","z":"1","F_R_I":"13337/625","F_R_I_branch":"upper","F_R_I_over_z":"13337/625","F_R_I_over_z_branch":"upper","apparent_zF":"13337/625","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK195","R":"16","I":"1440","z":"5/4","F_R_I":"13337/625","F_R_I_branch":"upper","F_R_I_over_z":"314007/15625","F_R_I_over_z_branch":"inside","apparent_zF":"314007/12500","apparent_ratio_to_F_R_I":"314007/266740"},{"formula_id":"SK195","R":"16","I":"1440","z":"2","F_R_I":"13337/625","F_R_I_branch":"upper","F_R_I_over_z":"56154/3125","F_R_I_over_z_branch":"inside","apparent_zF":"112308/3125","apparent_ratio_to_F_R_I":"112308/66685"},{"formula_id":"SK195","R":"16","I":"1440","z":"4","F_R_I":"13337/625","F_R_I_branch":"upper","F_R_I_over_z":"101229/6250","F_R_I_over_z_branch":"inside","apparent_zF":"202458/3125","apparent_ratio_to_F_R_I":"202458/66685"},{"formula_id":"SK195","R":"20","I":"360","z":"1","F_R_I":"20","F_R_I_branch":"lower","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"20","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK195","R":"20","I":"360","z":"5/4","F_R_I":"20","F_R_I_branch":"lower","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"25","apparent_ratio_to_F_R_I":"5/4"},{"formula_id":"SK195","R":"20","I":"360","z":"2","F_R_I":"20","F_R_I_branch":"lower","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"40","apparent_ratio_to_F_R_I":"2"},{"formula_id":"SK195","R":"20","I":"360","z":"4","F_R_I":"20","F_R_I_branch":"lower","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"80","apparent_ratio_to_F_R_I":"4"},{"formula_id":"SK195","R":"20","I":"800","z":"1","F_R_I":"54923/2500","F_R_I_branch":"inside","F_R_I_over_z":"54923/2500","F_R_I_over_z_branch":"inside","apparent_zF":"54923/2500","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK195","R":"20","I":"800","z":"5/4","F_R_I":"54923/2500","F_R_I_branch":"inside","F_R_I_over_z":"264767/12500","F_R_I_over_z_branch":"inside","apparent_zF":"264767/10000","apparent_ratio_to_F_R_I":"264767/219692"},{"formula_id":"SK195","R":"20","I":"800","z":"2","F_R_I":"54923/2500","F_R_I_branch":"inside","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"40","apparent_ratio_to_F_R_I":"100000/54923"},{"formula_id":"SK195","R":"20","I":"800","z":"4","F_R_I":"54923/2500","F_R_I_branch":"inside","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"80","apparent_ratio_to_F_R_I":"200000/54923"},{"formula_id":"SK195","R":"20","I":"1440","z":"1","F_R_I":"314007/12500","F_R_I_branch":"inside","F_R_I_over_z":"314007/12500","F_R_I_over_z_branch":"inside","apparent_zF":"314007/12500","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK195","R":"20","I":"1440","z":"5/4","F_R_I":"314007/12500","F_R_I_branch":"inside","F_R_I_over_z":"1481403/62500","F_R_I_over_z_branch":"inside","apparent_zF":"1481403/50000","apparent_ratio_to_F_R_I":"493801/418676"},{"formula_id":"SK195","R":"20","I":"1440","z":"2","F_R_I":"314007/12500","F_R_I_branch":"inside","F_R_I_over_z":"269691/12500","F_R_I_over_z_branch":"inside","apparent_zF":"269691/6250","apparent_ratio_to_F_R_I":"179794/104669"},{"formula_id":"SK195","R":"20","I":"1440","z":"4","F_R_I":"314007/12500","F_R_I_branch":"inside","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"80","apparent_ratio_to_F_R_I":"1000000/314007"},{"formula_id":"SK195","R":"32","I":"360","z":"1","F_R_I":"32","F_R_I_branch":"lower","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"32","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK195","R":"32","I":"360","z":"5/4","F_R_I":"32","F_R_I_branch":"lower","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"40","apparent_ratio_to_F_R_I":"5/4"},{"formula_id":"SK195","R":"32","I":"360","z":"2","F_R_I":"32","F_R_I_branch":"lower","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"64","apparent_ratio_to_F_R_I":"2"},{"formula_id":"SK195","R":"32","I":"360","z":"4","F_R_I":"32","F_R_I_branch":"lower","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"128","apparent_ratio_to_F_R_I":"4"},{"formula_id":"SK195","R":"32","I":"800","z":"1","F_R_I":"20492/625","F_R_I_branch":"inside","F_R_I_over_z":"20492/625","F_R_I_over_z_branch":"inside","apparent_zF":"20492/625","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK195","R":"32","I":"800","z":"5/4","F_R_I":"20492/625","F_R_I_branch":"inside","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"40","apparent_ratio_to_F_R_I":"6250/5123"},{"formula_id":"SK195","R":"32","I":"800","z":"2","F_R_I":"20492/625","F_R_I_branch":"inside","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"64","apparent_ratio_to_F_R_I":"10000/5123"},{"formula_id":"SK195","R":"32","I":"800","z":"4","F_R_I":"20492/625","F_R_I_branch":"inside","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"128","apparent_ratio_to_F_R_I":"20000/5123"},{"formula_id":"SK195","R":"32","I":"1440","z":"1","F_R_I":"112308/3125","F_R_I_branch":"inside","F_R_I_over_z":"112308/3125","F_R_I_over_z_branch":"inside","apparent_zF":"112308/3125","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK195","R":"32","I":"1440","z":"5/4","F_R_I":"112308/3125","F_R_I_branch":"inside","F_R_I_over_z":"539382/15625","F_R_I_over_z_branch":"inside","apparent_zF":"269691/6250","apparent_ratio_to_F_R_I":"89897/74872"},{"formula_id":"SK195","R":"32","I":"1440","z":"2","F_R_I":"112308/3125","F_R_I_branch":"inside","F_R_I_over_z":"101229/3125","F_R_I_over_z_branch":"inside","apparent_zF":"202458/3125","apparent_ratio_to_F_R_I":"33743/18718"},{"formula_id":"SK195","R":"32","I":"1440","z":"4","F_R_I":"112308/3125","F_R_I_branch":"inside","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"128","apparent_ratio_to_F_R_I":"100000/28077"},{"formula_id":"SK196","R":"16","I":"360","z":"1","F_R_I":"487339/25000","F_R_I_branch":"inside","F_R_I_over_z":"487339/25000","F_R_I_over_z_branch":"inside","apparent_zF":"487339/25000","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK196","R":"16","I":"360","z":"5/4","F_R_I":"487339/25000","F_R_I_branch":"inside","F_R_I_over_z":"96/5","F_R_I_over_z_branch":"lower","apparent_zF":"24","apparent_ratio_to_F_R_I":"600000/487339"},{"formula_id":"SK196","R":"16","I":"360","z":"2","F_R_I":"487339/25000","F_R_I_branch":"inside","F_R_I_over_z":"96/5","F_R_I_over_z_branch":"lower","apparent_zF":"192/5","apparent_ratio_to_F_R_I":"960000/487339"},{"formula_id":"SK196","R":"16","I":"360","z":"4","F_R_I":"487339/25000","F_R_I_branch":"inside","F_R_I_over_z":"96/5","F_R_I_over_z_branch":"lower","apparent_zF":"384/5","apparent_ratio_to_F_R_I":"1920000/487339"},{"formula_id":"SK196","R":"16","I":"800","z":"1","F_R_I":"28399/1250","F_R_I_branch":"inside","F_R_I_over_z":"28399/1250","F_R_I_over_z_branch":"inside","apparent_zF":"28399/1250","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK196","R":"16","I":"800","z":"5/4","F_R_I":"28399/1250","F_R_I_branch":"inside","F_R_I_over_z":"67332/3125","F_R_I_over_z_branch":"inside","apparent_zF":"16833/625","apparent_ratio_to_F_R_I":"33666/28399"},{"formula_id":"SK196","R":"16","I":"800","z":"2","F_R_I":"28399/1250","F_R_I_branch":"inside","F_R_I_over_z":"49467/2500","F_R_I_over_z_branch":"inside","apparent_zF":"49467/1250","apparent_ratio_to_F_R_I":"49467/28399"},{"formula_id":"SK196","R":"16","I":"800","z":"4","F_R_I":"28399/1250","F_R_I_branch":"inside","F_R_I_over_z":"96/5","F_R_I_over_z_branch":"lower","apparent_zF":"384/5","apparent_ratio_to_F_R_I":"96000/28399"},{"formula_id":"SK196","R":"16","I":"1440","z":"1","F_R_I":"171319/6250","F_R_I_branch":"inside","F_R_I_over_z":"171319/6250","F_R_I_over_z_branch":"inside","apparent_zF":"171319/6250","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK196","R":"16","I":"1440","z":"5/4","F_R_I":"171319/6250","F_R_I_branch":"inside","F_R_I_over_z":"395308/15625","F_R_I_over_z_branch":"inside","apparent_zF":"98827/3125","apparent_ratio_to_F_R_I":"197654/171319"},{"formula_id":"SK196","R":"16","I":"1440","z":"2","F_R_I":"171319/6250","F_R_I_branch":"inside","F_R_I_over_z":"276659/12500","F_R_I_over_z_branch":"inside","apparent_zF":"276659/6250","apparent_ratio_to_F_R_I":"276659/171319"},{"formula_id":"SK196","R":"16","I":"1440","z":"4","F_R_I":"171319/6250","F_R_I_branch":"inside","F_R_I_over_z":"487339/25000","F_R_I_over_z_branch":"inside","apparent_zF":"487339/6250","apparent_ratio_to_F_R_I":"487339/171319"},{"formula_id":"SK196","R":"20","I":"360","z":"1","F_R_I":"24","F_R_I_branch":"lower","F_R_I_over_z":"24","F_R_I_over_z_branch":"lower","apparent_zF":"24","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK196","R":"20","I":"360","z":"5/4","F_R_I":"24","F_R_I_branch":"lower","F_R_I_over_z":"24","F_R_I_over_z_branch":"lower","apparent_zF":"30","apparent_ratio_to_F_R_I":"5/4"},{"formula_id":"SK196","R":"20","I":"360","z":"2","F_R_I":"24","F_R_I_branch":"lower","F_R_I_over_z":"24","F_R_I_over_z_branch":"lower","apparent_zF":"48","apparent_ratio_to_F_R_I":"2"},{"formula_id":"SK196","R":"20","I":"360","z":"4","F_R_I":"24","F_R_I_branch":"lower","F_R_I_over_z":"24","F_R_I_over_z_branch":"lower","apparent_zF":"96","apparent_ratio_to_F_R_I":"4"},{"formula_id":"SK196","R":"20","I":"800","z":"1","F_R_I":"16833/625","F_R_I_branch":"inside","F_R_I_over_z":"16833/625","F_R_I_over_z_branch":"inside","apparent_zF":"16833/625","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK196","R":"20","I":"800","z":"5/4","F_R_I":"16833/625","F_R_I_branch":"inside","F_R_I_over_z":"160999/6250","F_R_I_over_z_branch":"inside","apparent_zF":"160999/5000","apparent_ratio_to_F_R_I":"160999/134664"},{"formula_id":"SK196","R":"20","I":"800","z":"2","F_R_I":"16833/625","F_R_I_branch":"inside","F_R_I_over_z":"60001/2500","F_R_I_over_z_branch":"inside","apparent_zF":"60001/1250","apparent_ratio_to_F_R_I":"60001/33666"},{"formula_id":"SK196","R":"20","I":"800","z":"4","F_R_I":"16833/625","F_R_I_branch":"inside","F_R_I_over_z":"24","F_R_I_over_z_branch":"lower","apparent_zF":"96","apparent_ratio_to_F_R_I":"20000/5611"},{"formula_id":"SK196","R":"20","I":"1440","z":"1","F_R_I":"98827/3125","F_R_I_branch":"inside","F_R_I_over_z":"98827/3125","F_R_I_over_z_branch":"inside","apparent_zF":"98827/3125","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK196","R":"20","I":"1440","z":"5/4","F_R_I":"98827/3125","F_R_I_branch":"inside","F_R_I_over_z":"922291/31250","F_R_I_over_z_branch":"inside","apparent_zF":"922291/25000","apparent_ratio_to_F_R_I":"922291/790616"},{"formula_id":"SK196","R":"20","I":"1440","z":"2","F_R_I":"98827/3125","F_R_I_branch":"inside","F_R_I_over_z":"329329/12500","F_R_I_over_z_branch":"inside","apparent_zF":"329329/6250","apparent_ratio_to_F_R_I":"329329/197654"},{"formula_id":"SK196","R":"20","I":"1440","z":"4","F_R_I":"98827/3125","F_R_I_branch":"inside","F_R_I_over_z":"24","F_R_I_over_z_branch":"lower","apparent_zF":"96","apparent_ratio_to_F_R_I":"300000/98827"},{"formula_id":"SK196","R":"32","I":"360","z":"1","F_R_I":"192/5","F_R_I_branch":"lower","F_R_I_over_z":"192/5","F_R_I_over_z_branch":"lower","apparent_zF":"192/5","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK196","R":"32","I":"360","z":"5/4","F_R_I":"192/5","F_R_I_branch":"lower","F_R_I_over_z":"192/5","F_R_I_over_z_branch":"lower","apparent_zF":"48","apparent_ratio_to_F_R_I":"5/4"},{"formula_id":"SK196","R":"32","I":"360","z":"2","F_R_I":"192/5","F_R_I_branch":"lower","F_R_I_over_z":"192/5","F_R_I_over_z_branch":"lower","apparent_zF":"384/5","apparent_ratio_to_F_R_I":"2"},{"formula_id":"SK196","R":"32","I":"360","z":"4","F_R_I":"192/5","F_R_I_branch":"lower","F_R_I_over_z":"192/5","F_R_I_over_z_branch":"lower","apparent_zF":"768/5","apparent_ratio_to_F_R_I":"4"},{"formula_id":"SK196","R":"32","I":"800","z":"1","F_R_I":"49467/1250","F_R_I_branch":"inside","F_R_I_over_z":"49467/1250","F_R_I_over_z_branch":"inside","apparent_zF":"49467/1250","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK196","R":"32","I":"800","z":"5/4","F_R_I":"49467/1250","F_R_I_branch":"inside","F_R_I_over_z":"120002/3125","F_R_I_over_z_branch":"inside","apparent_zF":"60001/1250","apparent_ratio_to_F_R_I":"60001/49467"},{"formula_id":"SK196","R":"32","I":"800","z":"2","F_R_I":"49467/1250","F_R_I_branch":"inside","F_R_I_over_z":"192/5","F_R_I_over_z_branch":"lower","apparent_zF":"384/5","apparent_ratio_to_F_R_I":"32000/16489"},{"formula_id":"SK196","R":"32","I":"800","z":"4","F_R_I":"49467/1250","F_R_I_branch":"inside","F_R_I_over_z":"192/5","F_R_I_over_z_branch":"lower","apparent_zF":"768/5","apparent_ratio_to_F_R_I":"64000/16489"},{"formula_id":"SK196","R":"32","I":"1440","z":"1","F_R_I":"276659/6250","F_R_I_branch":"inside","F_R_I_over_z":"276659/6250","F_R_I_over_z_branch":"inside","apparent_zF":"276659/6250","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK196","R":"32","I":"1440","z":"5/4","F_R_I":"276659/6250","F_R_I_branch":"inside","F_R_I_over_z":"658658/15625","F_R_I_over_z_branch":"inside","apparent_zF":"329329/6250","apparent_ratio_to_F_R_I":"329329/276659"},{"formula_id":"SK196","R":"32","I":"1440","z":"2","F_R_I":"276659/6250","F_R_I_branch":"inside","F_R_I_over_z":"487339/12500","F_R_I_over_z_branch":"inside","apparent_zF":"487339/6250","apparent_ratio_to_F_R_I":"487339/276659"},{"formula_id":"SK196","R":"32","I":"1440","z":"4","F_R_I":"276659/6250","F_R_I_branch":"inside","F_R_I_over_z":"192/5","F_R_I_over_z_branch":"lower","apparent_zF":"768/5","apparent_ratio_to_F_R_I":"960000/276659"},{"formula_id":"SK200","R":"16","I":"360","z":"1","F_R_I":"121477/5000","F_R_I_branch":"inside","F_R_I_over_z":"121477/5000","F_R_I_over_z_branch":"inside","apparent_zF":"121477/5000","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK200","R":"16","I":"360","z":"5/4","F_R_I":"121477/5000","F_R_I_branch":"inside","F_R_I_over_z":"24","F_R_I_over_z_branch":"lower","apparent_zF":"30","apparent_ratio_to_F_R_I":"150000/121477"},{"formula_id":"SK200","R":"16","I":"360","z":"2","F_R_I":"121477/5000","F_R_I_branch":"inside","F_R_I_over_z":"24","F_R_I_over_z_branch":"lower","apparent_zF":"48","apparent_ratio_to_F_R_I":"240000/121477"},{"formula_id":"SK200","R":"16","I":"360","z":"4","F_R_I":"121477/5000","F_R_I_branch":"inside","F_R_I_over_z":"24","F_R_I_over_z_branch":"lower","apparent_zF":"96","apparent_ratio_to_F_R_I":"480000/121477"},{"formula_id":"SK200","R":"16","I":"800","z":"1","F_R_I":"34431/1250","F_R_I_branch":"inside","F_R_I_over_z":"34431/1250","F_R_I_over_z_branch":"inside","apparent_zF":"34431/1250","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK200","R":"16","I":"800","z":"5/4","F_R_I":"34431/1250","F_R_I_branch":"inside","F_R_I_over_z":"16477/625","F_R_I_over_z_branch":"inside","apparent_zF":"16477/500","apparent_ratio_to_F_R_I":"82385/68862"},{"formula_id":"SK200","R":"16","I":"800","z":"2","F_R_I":"34431/1250","F_R_I_branch":"inside","F_R_I_over_z":"61477/2500","F_R_I_over_z_branch":"inside","apparent_zF":"61477/1250","apparent_ratio_to_F_R_I":"61477/34431"},{"formula_id":"SK200","R":"16","I":"800","z":"4","F_R_I":"34431/1250","F_R_I_branch":"inside","F_R_I_over_z":"24","F_R_I_over_z_branch":"lower","apparent_zF":"96","apparent_ratio_to_F_R_I":"40000/11477"},{"formula_id":"SK200","R":"16","I":"1440","z":"1","F_R_I":"20006/625","F_R_I_branch":"upper","F_R_I_over_z":"20006/625","F_R_I_over_z_branch":"upper","apparent_zF":"20006/625","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK200","R":"16","I":"1440","z":"5/4","F_R_I":"20006/625","F_R_I_branch":"upper","F_R_I_over_z":"94201/3125","F_R_I_over_z_branch":"inside","apparent_zF":"94201/2500","apparent_ratio_to_F_R_I":"94201/80024"},{"formula_id":"SK200","R":"16","I":"1440","z":"2","F_R_I":"20006/625","F_R_I_branch":"upper","F_R_I_over_z":"13477/500","F_R_I_over_z_branch":"inside","apparent_zF":"13477/250","apparent_ratio_to_F_R_I":"67385/40012"},{"formula_id":"SK200","R":"16","I":"1440","z":"4","F_R_I":"20006/625","F_R_I_branch":"upper","F_R_I_over_z":"121477/5000","F_R_I_over_z_branch":"inside","apparent_zF":"121477/1250","apparent_ratio_to_F_R_I":"121477/40012"},{"formula_id":"SK200","R":"20","I":"360","z":"1","F_R_I":"30","F_R_I_branch":"lower","F_R_I_over_z":"30","F_R_I_over_z_branch":"lower","apparent_zF":"30","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK200","R":"20","I":"360","z":"5/4","F_R_I":"30","F_R_I_branch":"lower","F_R_I_over_z":"30","F_R_I_over_z_branch":"lower","apparent_zF":"75/2","apparent_ratio_to_F_R_I":"5/4"},{"formula_id":"SK200","R":"20","I":"360","z":"2","F_R_I":"30","F_R_I_branch":"lower","F_R_I_over_z":"30","F_R_I_over_z_branch":"lower","apparent_zF":"60","apparent_ratio_to_F_R_I":"2"},{"formula_id":"SK200","R":"20","I":"360","z":"4","F_R_I":"30","F_R_I_branch":"lower","F_R_I_over_z":"30","F_R_I_over_z_branch":"lower","apparent_zF":"120","apparent_ratio_to_F_R_I":"4"},{"formula_id":"SK200","R":"20","I":"800","z":"1","F_R_I":"16477/500","F_R_I_branch":"inside","F_R_I_over_z":"16477/500","F_R_I_over_z_branch":"inside","apparent_zF":"16477/500","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK200","R":"20","I":"800","z":"5/4","F_R_I":"16477/500","F_R_I_branch":"inside","F_R_I_over_z":"79431/2500","F_R_I_over_z_branch":"inside","apparent_zF":"79431/2000","apparent_ratio_to_F_R_I":"79431/65908"},{"formula_id":"SK200","R":"20","I":"800","z":"2","F_R_I":"16477/500","F_R_I_branch":"inside","F_R_I_over_z":"30","F_R_I_over_z_branch":"inside","apparent_zF":"60","apparent_ratio_to_F_R_I":"30000/16477"},{"formula_id":"SK200","R":"20","I":"800","z":"4","F_R_I":"16477/500","F_R_I_branch":"inside","F_R_I_over_z":"30","F_R_I_over_z_branch":"lower","apparent_zF":"120","apparent_ratio_to_F_R_I":"60000/16477"},{"formula_id":"SK200","R":"20","I":"1440","z":"1","F_R_I":"94201/2500","F_R_I_branch":"inside","F_R_I_over_z":"94201/2500","F_R_I_over_z_branch":"inside","apparent_zF":"94201/2500","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK200","R":"20","I":"1440","z":"5/4","F_R_I":"94201/2500","F_R_I_branch":"inside","F_R_I_over_z":"444419/12500","F_R_I_over_z_branch":"inside","apparent_zF":"444419/10000","apparent_ratio_to_F_R_I":"444419/376804"},{"formula_id":"SK200","R":"20","I":"1440","z":"2","F_R_I":"94201/2500","F_R_I_branch":"inside","F_R_I_over_z":"20227/625","F_R_I_over_z_branch":"inside","apparent_zF":"40454/625","apparent_ratio_to_F_R_I":"161816/94201"},{"formula_id":"SK200","R":"20","I":"1440","z":"4","F_R_I":"94201/2500","F_R_I_branch":"inside","F_R_I_over_z":"30","F_R_I_over_z_branch":"lower","apparent_zF":"120","apparent_ratio_to_F_R_I":"300000/94201"},{"formula_id":"SK200","R":"32","I":"360","z":"1","F_R_I":"48","F_R_I_branch":"lower","F_R_I_over_z":"48","F_R_I_over_z_branch":"lower","apparent_zF":"48","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK200","R":"32","I":"360","z":"5/4","F_R_I":"48","F_R_I_branch":"lower","F_R_I_over_z":"48","F_R_I_over_z_branch":"lower","apparent_zF":"60","apparent_ratio_to_F_R_I":"5/4"},{"formula_id":"SK200","R":"32","I":"360","z":"2","F_R_I":"48","F_R_I_branch":"lower","F_R_I_over_z":"48","F_R_I_over_z_branch":"lower","apparent_zF":"96","apparent_ratio_to_F_R_I":"2"},{"formula_id":"SK200","R":"32","I":"360","z":"4","F_R_I":"48","F_R_I_branch":"lower","F_R_I_over_z":"48","F_R_I_over_z_branch":"lower","apparent_zF":"192","apparent_ratio_to_F_R_I":"4"},{"formula_id":"SK200","R":"32","I":"800","z":"1","F_R_I":"61477/1250","F_R_I_branch":"inside","F_R_I_over_z":"61477/1250","F_R_I_over_z_branch":"inside","apparent_zF":"61477/1250","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK200","R":"32","I":"800","z":"5/4","F_R_I":"61477/1250","F_R_I_branch":"inside","F_R_I_over_z":"48","F_R_I_over_z_branch":"inside","apparent_zF":"60","apparent_ratio_to_F_R_I":"75000/61477"},{"formula_id":"SK200","R":"32","I":"800","z":"2","F_R_I":"61477/1250","F_R_I_branch":"inside","F_R_I_over_z":"48","F_R_I_over_z_branch":"lower","apparent_zF":"96","apparent_ratio_to_F_R_I":"120000/61477"},{"formula_id":"SK200","R":"32","I":"800","z":"4","F_R_I":"61477/1250","F_R_I_branch":"inside","F_R_I_over_z":"48","F_R_I_over_z_branch":"lower","apparent_zF":"192","apparent_ratio_to_F_R_I":"240000/61477"},{"formula_id":"SK200","R":"32","I":"1440","z":"1","F_R_I":"13477/250","F_R_I_branch":"inside","F_R_I_over_z":"13477/250","F_R_I_over_z_branch":"inside","apparent_zF":"13477/250","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK200","R":"32","I":"1440","z":"5/4","F_R_I":"13477/250","F_R_I_branch":"inside","F_R_I_over_z":"161816/3125","F_R_I_over_z_branch":"inside","apparent_zF":"40454/625","apparent_ratio_to_F_R_I":"80908/67385"},{"formula_id":"SK200","R":"32","I":"1440","z":"2","F_R_I":"13477/250","F_R_I_branch":"inside","F_R_I_over_z":"121477/2500","F_R_I_over_z_branch":"inside","apparent_zF":"121477/1250","apparent_ratio_to_F_R_I":"121477/67385"},{"formula_id":"SK200","R":"32","I":"1440","z":"4","F_R_I":"13477/250","F_R_I_branch":"inside","F_R_I_over_z":"48","F_R_I_over_z_branch":"lower","apparent_zF":"192","apparent_ratio_to_F_R_I":"48000/13477"},{"formula_id":"SK203","R":"16","I":"360","z":"1","F_R_I":"53099/3125","F_R_I_branch":"inside","F_R_I_over_z":"53099/3125","F_R_I_over_z_branch":"inside","apparent_zF":"53099/3125","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK203","R":"16","I":"360","z":"5/4","F_R_I":"53099/3125","F_R_I_branch":"inside","F_R_I_over_z":"16","F_R_I_over_z_branch":"lower","apparent_zF":"20","apparent_ratio_to_F_R_I":"62500/53099"},{"formula_id":"SK203","R":"16","I":"360","z":"2","F_R_I":"53099/3125","F_R_I_branch":"inside","F_R_I_over_z":"16","F_R_I_over_z_branch":"lower","apparent_zF":"32","apparent_ratio_to_F_R_I":"100000/53099"},{"formula_id":"SK203","R":"16","I":"360","z":"4","F_R_I":"53099/3125","F_R_I_branch":"inside","F_R_I_over_z":"16","F_R_I_over_z_branch":"lower","apparent_zF":"64","apparent_ratio_to_F_R_I":"200000/53099"},{"formula_id":"SK203","R":"16","I":"800","z":"1","F_R_I":"17442/625","F_R_I_branch":"inside","F_R_I_over_z":"17442/625","F_R_I_over_z_branch":"inside","apparent_zF":"17442/625","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK203","R":"16","I":"800","z":"5/4","F_R_I":"17442/625","F_R_I_branch":"inside","F_R_I_over_z":"74806/3125","F_R_I_over_z_branch":"inside","apparent_zF":"37403/1250","apparent_ratio_to_F_R_I":"37403/34884"},{"formula_id":"SK203","R":"16","I":"800","z":"2","F_R_I":"17442/625","F_R_I_branch":"inside","F_R_I_over_z":"2248/125","F_R_I_over_z_branch":"inside","apparent_zF":"4496/125","apparent_ratio_to_F_R_I":"11240/8721"},{"formula_id":"SK203","R":"16","I":"800","z":"4","F_R_I":"17442/625","F_R_I_branch":"inside","F_R_I_over_z":"16","F_R_I_over_z_branch":"lower","apparent_zF":"64","apparent_ratio_to_F_R_I":"20000/8721"},{"formula_id":"SK203","R":"16","I":"1440","z":"1","F_R_I":"26674/625","F_R_I_branch":"upper","F_R_I_over_z":"26674/625","F_R_I_over_z_branch":"upper","apparent_zF":"26674/625","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK203","R":"16","I":"1440","z":"5/4","F_R_I":"26674/625","F_R_I_branch":"upper","F_R_I_over_z":"572494/15625","F_R_I_over_z_branch":"inside","apparent_zF":"286247/6250","apparent_ratio_to_F_R_I":"286247/266740"},{"formula_id":"SK203","R":"16","I":"1440","z":"2","F_R_I":"26674/625","F_R_I_branch":"upper","F_R_I_over_z":"81008/3125","F_R_I_over_z_branch":"inside","apparent_zF":"162016/3125","apparent_ratio_to_F_R_I":"81008/66685"},{"formula_id":"SK203","R":"16","I":"1440","z":"4","F_R_I":"26674/625","F_R_I_branch":"upper","F_R_I_over_z":"53099/3125","F_R_I_over_z_branch":"inside","apparent_zF":"212396/3125","apparent_ratio_to_F_R_I":"106198/66685"},{"formula_id":"SK203","R":"20","I":"360","z":"1","F_R_I":"20","F_R_I_branch":"lower","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"20","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK203","R":"20","I":"360","z":"5/4","F_R_I":"20","F_R_I_branch":"lower","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"25","apparent_ratio_to_F_R_I":"5/4"},{"formula_id":"SK203","R":"20","I":"360","z":"2","F_R_I":"20","F_R_I_branch":"lower","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"40","apparent_ratio_to_F_R_I":"2"},{"formula_id":"SK203","R":"20","I":"360","z":"4","F_R_I":"20","F_R_I_branch":"lower","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"80","apparent_ratio_to_F_R_I":"4"},{"formula_id":"SK203","R":"20","I":"800","z":"1","F_R_I":"37403/1250","F_R_I_branch":"inside","F_R_I_over_z":"37403/1250","F_R_I_over_z_branch":"inside","apparent_zF":"37403/1250","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK203","R":"20","I":"800","z":"5/4","F_R_I":"37403/1250","F_R_I_branch":"inside","F_R_I_over_z":"162207/6250","F_R_I_over_z_branch":"inside","apparent_zF":"162207/5000","apparent_ratio_to_F_R_I":"162207/149612"},{"formula_id":"SK203","R":"20","I":"800","z":"2","F_R_I":"37403/1250","F_R_I_branch":"inside","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"40","apparent_ratio_to_F_R_I":"50000/37403"},{"formula_id":"SK203","R":"20","I":"800","z":"4","F_R_I":"37403/1250","F_R_I_branch":"inside","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"80","apparent_ratio_to_F_R_I":"100000/37403"},{"formula_id":"SK203","R":"20","I":"1440","z":"1","F_R_I":"286247/6250","F_R_I_branch":"inside","F_R_I_over_z":"286247/6250","F_R_I_over_z_branch":"inside","apparent_zF":"286247/6250","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK203","R":"20","I":"1440","z":"5/4","F_R_I":"286247/6250","F_R_I_branch":"inside","F_R_I_over_z":"1207963/31250","F_R_I_over_z_branch":"inside","apparent_zF":"1207963/25000","apparent_ratio_to_F_R_I":"1207963/1144988"},{"formula_id":"SK203","R":"20","I":"1440","z":"2","F_R_I":"286247/6250","F_R_I_branch":"inside","F_R_I_over_z":"174611/6250","F_R_I_over_z_branch":"inside","apparent_zF":"174611/3125","apparent_ratio_to_F_R_I":"349222/286247"},{"formula_id":"SK203","R":"20","I":"1440","z":"4","F_R_I":"286247/6250","F_R_I_branch":"inside","F_R_I_over_z":"20","F_R_I_over_z_branch":"lower","apparent_zF":"80","apparent_ratio_to_F_R_I":"500000/286247"},{"formula_id":"SK203","R":"32","I":"360","z":"1","F_R_I":"32","F_R_I_branch":"lower","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"32","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK203","R":"32","I":"360","z":"5/4","F_R_I":"32","F_R_I_branch":"lower","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"40","apparent_ratio_to_F_R_I":"5/4"},{"formula_id":"SK203","R":"32","I":"360","z":"2","F_R_I":"32","F_R_I_branch":"lower","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"64","apparent_ratio_to_F_R_I":"2"},{"formula_id":"SK203","R":"32","I":"360","z":"4","F_R_I":"32","F_R_I_branch":"lower","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"128","apparent_ratio_to_F_R_I":"4"},{"formula_id":"SK203","R":"32","I":"800","z":"1","F_R_I":"4496/125","F_R_I_branch":"inside","F_R_I_over_z":"4496/125","F_R_I_over_z_branch":"inside","apparent_zF":"4496/125","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK203","R":"32","I":"800","z":"5/4","F_R_I":"4496/125","F_R_I_branch":"inside","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"40","apparent_ratio_to_F_R_I":"625/562"},{"formula_id":"SK203","R":"32","I":"800","z":"2","F_R_I":"4496/125","F_R_I_branch":"inside","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"64","apparent_ratio_to_F_R_I":"500/281"},{"formula_id":"SK203","R":"32","I":"800","z":"4","F_R_I":"4496/125","F_R_I_branch":"inside","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"128","apparent_ratio_to_F_R_I":"1000/281"},{"formula_id":"SK203","R":"32","I":"1440","z":"1","F_R_I":"162016/3125","F_R_I_branch":"inside","F_R_I_over_z":"162016/3125","F_R_I_over_z_branch":"inside","apparent_zF":"162016/3125","apparent_ratio_to_F_R_I":"1"},{"formula_id":"SK203","R":"32","I":"1440","z":"5/4","F_R_I":"162016/3125","F_R_I_branch":"inside","F_R_I_over_z":"698444/15625","F_R_I_over_z_branch":"inside","apparent_zF":"174611/3125","apparent_ratio_to_F_R_I":"174611/162016"},{"formula_id":"SK203","R":"32","I":"1440","z":"2","F_R_I":"162016/3125","F_R_I_branch":"inside","F_R_I_over_z":"106198/3125","F_R_I_over_z_branch":"inside","apparent_zF":"212396/3125","apparent_ratio_to_F_R_I":"53099/40504"},{"formula_id":"SK203","R":"32","I":"1440","z":"4","F_R_I":"162016/3125","F_R_I_branch":"inside","F_R_I_over_z":"32","F_R_I_over_z_branch":"lower","apparent_zF":"128","apparent_ratio_to_F_R_I":"12500/5063"}],"toy_witnesses":{"mixed":{"formula":"clamp(1rem, .5rem + 2vi, 2rem)","R":"16","I":"800","z":"2","baseline_F":"24","zoomed_F_R_I_over_z":"16","apparent_zF":"32","ratio":"4/3","changed_root_R32_F":"32"},"pure_vi":{"formula":"2vi","I":"800","z":"2","CSS_value":"16","apparent_zF":"16"},"lower_clamp":{"formula":"clamp(1rem, .5rem + 2vi, 2rem)","R":"16","I":"100","F":"16","branch":"lower"},"upper_clamp":{"formula":"clamp(1rem, .5rem + 2vi, 2rem)","R":"16","I":"2000","F":"32","branch":"upper"}},"axis_witnesses":[{"writing_mode":"horizontal-tb","viewport_css_px":[800,600],"inline_axis":"width","vi_css_px":"8","vw_css_px":"8"},{"writing_mode":"vertical-rl","viewport_css_px":[800,600],"inline_axis":"height","vi_css_px":"6","vw_css_px":"8"}],"assumptions":["exact decimal Fractions","zoom holds R fixed, computes I/z and reports zF","vi is 1% of selected inline axis","no browser observation or conformance inference"]}
```

Equality at a bound is inside. This model is not browser or conformance evidence.

### Human-readable witnesses

- Mixed toy `clamp(1rem, .5rem + 2vi, 2rem)`: R=16/I=800 gives24; stipulated z=2 gives F=16, apparent32, ratio4/3; separately changing R to32 gives32. Pure `2vi` gives16 and apparent16 under z=2. I=100/2000 reaches lower16/upper32.
- At 800×600 CSS px, horizontal writing yields vi/vw 8/8; vertical writing yields 6/8. Axis selection does not demonstrate enlargement.

### Complete inventory and retained boundaries

Seven unchanged source windows, 98 lines, five file hashes and complete selected texts. Updated independent projections enumerate Q units plus the literal retained-boundary and markup records below. Byte offsets address the full pinned UTF-8 source.

```json
{
  "retained_substantive": [
    {
      "boundary_id": "B01",
      "predecessor_ids": [
        "B01"
      ],
      "window_id": "W01",
      "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
      "path": "knowledge/design/SKILL.md",
      "line_span": [
        68,
        68
      ],
      "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
      "byte_offsets": [
        5812,
        6012
      ],
      "literal_subject": "| I | **Multiply, Never Add** | All scales (type, space, colour lightness) must be geometric, not arithmetic. | A spacing value that's \"4px more than the last one\" instead of \"1.333× the last one.\" |",
      "disposition": "retained; not separately assessed",
      "reason": "general scale universal remains T/L",
      "owner": "Arc02 remaining T/L; Arc04 composition"
    },
    {
      "boundary_id": "B02",
      "predecessor_ids": [
        "B02"
      ],
      "window_id": "W01",
      "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
      "path": "knowledge/design/SKILL.md",
      "line_span": [
        70,
        70
      ],
      "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
      "byte_offsets": [
        6227,
        6459
      ],
      "literal_subject": "| III | **Name the Role, Not the Value** | Three-tier tokens: primitive → semantic → component. Never use `var(--brand-700)` in a component. | `background: var(--brand-700)` instead of `background: var(--interactive-primary)`. |",
      "disposition": "retained; not separately assessed",
      "reason": "token-layer/Slice03 scope",
      "owner": "Arc02 remaining T/L; Arc04 composition"
    },
    {
      "boundary_id": "B03",
      "predecessor_ids": [
        "B03"
      ],
      "window_id": "W01",
      "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
      "path": "knowledge/design/SKILL.md",
      "line_span": [
        71,
        71
      ],
      "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
      "byte_offsets": [
        6460,
        6664
      ],
      "literal_subject": "| IV | **Constraint Liberates** | Small, well-chosen palettes (3 fonts, 9 space tokens, 1 accent hue per site) produce better outcomes than infinite options. | \"I'll just pick whatever looks good here.\" |",
      "disposition": "retained; not separately assessed",
      "reason": "remaining T/L outcome claim",
      "owner": "Arc02 remaining T/L; Arc04 composition"
    },
    {
      "boundary_id": "B04",
      "predecessor_ids": [
        "B04"
      ],
      "window_id": "W01",
      "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
      "path": "knowledge/design/SKILL.md",
      "line_span": [
        72,
        72
      ],
      "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
      "byte_offsets": [
        6665,
        6867
      ],
      "literal_subject": "| V | **Unity Is Not Uniformity** | Shared mathematical structure, site-specific expression. Same skeleton, different posture. | Three sites that look identical, or three sites with nothing in common. |",
      "disposition": "retained; not separately assessed",
      "reason": "cross-site identity remains T/L",
      "owner": "Arc02 remaining T/L; Arc04 composition"
    },
    {
      "boundary_id": "B05",
      "predecessor_ids": [
        "B05"
      ],
      "window_id": "W01",
      "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
      "path": "knowledge/design/SKILL.md",
      "line_span": [
        73,
        73
      ],
      "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
      "byte_offsets": [
        6868,
        7066
      ],
      "literal_subject": "| VI | **Proximity Carries Meaning** | Intra-group spacing < inter-group spacing. Always. Uniform spacing destroys information. | Same `16px` gap inside cards, between cards, and between sections. |",
      "disposition": "retained; not separately assessed",
      "reason": "spatial/perceptual universal remains T/L",
      "owner": "Arc02 remaining T/L; Arc04 composition"
    },
    {
      "boundary_id": "B06",
      "predecessor_ids": [
        "B06"
      ],
      "window_id": "W01",
      "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
      "path": "knowledge/design/SKILL.md",
      "line_span": [
        74,
        74
      ],
      "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
      "byte_offsets": [
        7067,
        7288
      ],
      "literal_subject": "| VII | **Design the Invariants** | Define relationships (ratios, mappings, axioms), not individual values. The system generates instances. | Hand-picking a font size for one specific heading instead of using the scale. |",
      "disposition": "retained; not separately assessed",
      "reason": "general design method remains T/L",
      "owner": "Arc02 remaining T/L; Arc04 composition"
    },
    {
      "boundary_id": "B07",
      "predecessor_ids": [
        "B07"
      ],
      "window_id": "W03",
      "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
      "path": "knowledge/design/guides/layout.md",
      "line_span": [
        112,
        115
      ],
      "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
      "byte_offsets": [
        4609,
        4883
      ],
      "literal_subject": "The **Units** chapter makes the case against pixels with precision. The\nvalue of `1px` is not what it seems --- it varies across devices, zoom\nlevels, and display densities. More importantly, pixels create *no\nrelationship* between the value and the content it measures.",
      "disposition": "retained; not separately assessed",
      "reason": "pixel/content relation, separate from rem preference",
      "owner": "Arc02 remaining T/L; Arc04 composition"
    },
    {
      "boundary_id": "B08",
      "predecessor_ids": [
        "B08"
      ],
      "window_id": "W03",
      "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
      "path": "knowledge/design/guides/layout.md",
      "line_span": [
        115,
        118
      ],
      "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
      "byte_offsets": [
        4884,
        5039
      ],
      "literal_subject": "The `ch`\nunit, by contrast, is defined by the font\\'s own geometry: `60ch` is\nalways roughly 60 characters wide, regardless of font size or screen\ndensity.",
      "disposition": "retained; not separately assessed",
      "reason": "ch glyph measure is not arbitrary character count",
      "owner": "Arc02 remaining T/L; Arc04 composition"
    },
    {
      "boundary_id": "B09",
      "predecessor_ids": [
        "B09"
      ],
      "window_id": "W03",
      "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
      "path": "knowledge/design/guides/layout.md",
      "line_span": [
        119,
        122
      ],
      "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
      "byte_offsets": [
        5145,
        5356
      ],
      "literal_subject": "The `em` unit creates local\nproportional relationships, so that a child element scales with its\nparent. Each unit encodes a *kind of relationship*, and choosing the\nright unit is choosing the right relationship.",
      "disposition": "retained; not separately assessed",
      "reason": "em mechanics and generic unit maxim",
      "owner": "Arc02 remaining T/L; Arc04 composition"
    },
    {
      "boundary_id": "B11",
      "predecessor_ids": [
        "B11"
      ],
      "window_id": "W06",
      "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
      "path": "knowledge/design/guides/design.md",
      "line_span": [
        151,
        152
      ],
      "source_sha256": "e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b",
      "byte_offsets": [
        5651,
        5727
      ],
      "literal_subject": "Every unit of\nmeasurement should describe the experience, not the mechanism.",
      "disposition": "retained; not separately assessed",
      "reason": "general unit maxim",
      "owner": "Arc02 remaining T/L; Arc04 composition"
    },
    {
      "boundary_id": "B12",
      "predecessor_ids": [
        "C12"
      ],
      "window_id": "W05",
      "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
      "path": "knowledge/design/guides/breaking-the-layout-monoculture.md",
      "line_span": [
        206,
        211
      ],
      "source_sha256": "76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845",
      "byte_offsets": [
        7847,
        8218
      ],
      "literal_subject": "Space tokens derived from the same modular scale as typography create\nwhat Massimo Vignelli called \\\"syntactical consistency\\\" --- spacing and\ntype as a unified mathematical system. When the type scale is built on\nmusical interval ratios (perfect fourth at 4:3, perfect fifth at 3:2,\nmajor third at 5:4), the space system inherits that proportional harmony\nautomatically.",
      "disposition": "retained; not separately assessed",
      "reason": "Vignelli/music/harmony retained",
      "owner": "Arc02 remaining T/L; Arc04 composition"
    },
    {
      "boundary_id": "B13",
      "predecessor_ids": [
        "C15"
      ],
      "window_id": "W07",
      "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
      "path": "knowledge/design/guides/type.md",
      "line_span": [
        476,
        478
      ],
      "source_sha256": "8a9f1ab35dee3373ebbf1460416e334adffcd908f095463fa015c6ef0a5f5d7c",
      "byte_offsets": [
        18228,
        18356
      ],
      "literal_subject": "Bringhurst\\'s principle that\ndisplay type needs more air, and text type needs more density,\nimplemented in pure CSS mathematics.",
      "disposition": "retained; not separately assessed",
      "reason": "Bringhurst attribution/perception retained",
      "owner": "Arc02 remaining T/L; Arc04 composition"
    }
  ],
  "markup": [
    {
      "boundary_id": "M01",
      "predecessor_id": "M01",
      "window_id": "W01",
      "path": "knowledge/design/SKILL.md",
      "literal_subject": "Markdown table structure",
      "disposition": "markup only; representation retained"
    },
    {
      "boundary_id": "M02",
      "predecessor_id": "M02",
      "window_id": "W02",
      "path": "knowledge/design/SKILL.md",
      "literal_subject": "heading and fenced CSS delimiters",
      "disposition": "markup only; representation retained"
    },
    {
      "boundary_id": "M03",
      "predecessor_id": "M03",
      "window_id": "W04",
      "path": "knowledge/design/guides/layout.md",
      "literal_subject": "::: prose delimiters",
      "disposition": "markup only; representation retained"
    },
    {
      "boundary_id": "M04",
      "predecessor_id": "M04",
      "window_id": "W05",
      "path": "knowledge/design/guides/breaking-the-layout-monoculture.md",
      "literal_subject": "heading anchor, ::: prose and fixed-column table",
      "disposition": "markup only; representation retained"
    }
  ]
}
```

### Paired originals

- Q10↔Q22 are rem/root preference originals; Q12↔Q19 are vi/zoom/WCAG originals. Each pair is exact, reciprocal and independently assessed. Both pairs repeat, rather than contradict, the local inference.
- Q02↔Q23 preserves the 1.2/1.25 narrow endpoint conflict. Q11/Q21 compare inline-axis recommendations. Pairing does not establish truth.
- Card/graph/CQ review was not assigned.

Accepted Slice01 Clamp behavior/correction handoff remains separate. Q06–Q09 preserve literal coefficients, Q13 retains the bounded progression fact, and Q14 corrects the separate asymptote proposition. No proposal is installed; Arc04 owns composition.

## Current literal action registry

Strict complete registry; each of the 24 result IDs appears exactly once. Retain means the target bytes remain unchanged.

```json
[
  {
    "action_id": "A-Q01",
    "result_ids": [
      "Q01"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      69,
      69
    ],
    "byte_offsets": [
      6013,
      6226
    ],
    "literal_original": "| II | **Perception Is the Only Coordinate System** | Use OKLCH for colour, `rem`/`ch`/`vi` for sizing — units that describe experience, not mechanism. | Hex colours, `px` for type sizes, `vw` instead of `vi`. |",
    "replacement": "| II | **Perception Is the Only Coordinate System** | Use OKLCH for colour; choose `rem`, `ch` or `vi` for the sizing relationship required, then check user and content outcomes. | Choosing a unit without checking its basis or behavior. |",
    "replacement_sha256": "75f29f563bcbc275a351d53a1ca98f08c21eccb6d2672c886b5138be16414c32",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      238
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q01.P1",
        "byte_bounds": [
          0,
          238
        ],
        "text": "| II | **Perception Is the Only Coordinate System** | Use OKLCH for colour; choose `rem`, `ch` or `vi` for the sizing relationship required, then check user and content outcomes. | Choosing a unit without checking its basis or behavior. |",
        "sha256": "75f29f563bcbc275a351d53a1ca98f08c21eccb6d2672c886b5138be16414c32"
      }
    ]
  },
  {
    "action_id": "A-Q02",
    "result_ids": [
      "Q02"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      186,
      187
    ],
    "byte_offsets": [
      12207,
      12340
    ],
    "literal_original": "- **@min**: 360px viewport, 16px base, ratio 1.200 (minor third)\n- **@max**: 1440px viewport, 20px base, ratio 1.333 (perfect fourth)",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-Q03",
    "result_ids": [
      "Q03"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      191,
      191
    ],
    "byte_offsets": [
      12361,
      12423
    ],
    "literal_original": "Type, space, and grid are **one unified mathematical system**.",
    "replacement": "Type, space, and grid can share project-defined inputs.",
    "replacement_sha256": "6728c964affb20c429aeee7fb5b411e7e00befbd98db1ccdf8dd77f35ff65dee",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      55
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q03.P1",
        "byte_bounds": [
          0,
          55
        ],
        "text": "Type, space, and grid can share project-defined inputs.",
        "sha256": "6728c964affb20c429aeee7fb5b411e7e00befbd98db1ccdf8dd77f35ff65dee"
      }
    ]
  },
  {
    "action_id": "A-Q04",
    "result_ids": [
      "Q04"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      191,
      191
    ],
    "byte_offsets": [
      12424,
      12471
    ],
    "literal_original": "The base space token equals the base type size.",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-Q05",
    "result_ids": [
      "Q05"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      191,
      191
    ],
    "byte_offsets": [
      12472,
      12548
    ],
    "literal_original": "Space pairs (e.g., `--space-s-l`) interpolate steeply for component padding.",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-Q06",
    "result_ids": [
      "Q06"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      195,
      195
    ],
    "byte_offsets": [
      12574,
      12629
    ],
    "literal_original": "--step-0: clamp(1rem, 0.9015rem + 0.4924vi, 1.3337rem);",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-Q07",
    "result_ids": [
      "Q07"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      196,
      196
    ],
    "byte_offsets": [
      12630,
      12687
    ],
    "literal_original": "--step-1: clamp(1.2rem, 1.0534rem + 0.7331vi, 1.7783rem);",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-Q08",
    "result_ids": [
      "Q08"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      200,
      200
    ],
    "byte_offsets": [
      12753,
      12811
    ],
    "literal_original": "--space-m: clamp(1.5rem, 1.3523rem + 0.7385vi, 2.0006rem);",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-Q09",
    "result_ids": [
      "Q09"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      203,
      203
    ],
    "byte_offsets": [
      12855,
      12913
    ],
    "literal_original": "--space-s-l: clamp(1rem, 0.5038rem + 2.4808vi, 2.6674rem);",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-Q10",
    "result_ids": [
      "Q10"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "path": "knowledge/design/guides/layout.md",
    "line_span": [
      118,
      119
    ],
    "byte_offsets": [
      5040,
      5144
    ],
    "literal_original": "The `rem` unit anchors to the user\\'s chosen root font size,\nrespecting their accessibility preferences.",
    "replacement": "The `rem` unit uses the computed font-size of the root element. A user setting affects it only when it changes that computed size; verify enlargement and reflow separately.",
    "replacement_sha256": "768c9596e184597722608f402a7a60a5166af771484f89e82b15fdfa5507f347",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      172
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q10.P1",
        "byte_bounds": [
          0,
          172
        ],
        "text": "The `rem` unit uses the computed font-size of the root element. A user setting affects it only when it changes that computed size; verify enlargement and reflow separately.",
        "sha256": "768c9596e184597722608f402a7a60a5166af771484f89e82b15fdfa5507f347"
      }
    ]
  },
  {
    "action_id": "A-Q11",
    "result_ids": [
      "Q11"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "path": "knowledge/design/guides/layout.md",
    "line_span": [
      935,
      937
    ],
    "byte_offsets": [
      44599,
      44776
    ],
    "literal_original": "The fluid interpolation in Utopia\\'s `clamp()` declarations is a linear\nfunction: `y = mx + b`, where `m` is the slope between the min and max\nvalues and `b` is the y-intercept.",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 retains formula clause within accepted Slice01 bounded arithmetic scope",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-Q12",
    "result_ids": [
      "Q12"
    ],
    "disposition": "correct",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "path": "knowledge/design/guides/layout.md",
    "line_span": [
      937,
      940
    ],
    "byte_offsets": [
      44777,
      44969
    ],
    "literal_original": "The `vi` unit (viewport inline) is\nused instead of `vw` because it respects writing direction and,\ncritically, does not prevent browser zoom from scaling\ntext --- satisfying WCAG SC 1.4.4.",
    "replacement": "Choose `vi` when viewport sizing should follow the inline axis. Unit choice alone does not establish text enlargement or SC 1.4.4 conformance; verify required enlargement without loss in actual content.",
    "replacement_sha256": "9491131a027aff56a5afae5997055d37a194e0990aebfa29c5800e803dd7ad45",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      202
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q12.P1",
        "byte_bounds": [
          0,
          202
        ],
        "text": "Choose `vi` when viewport sizing should follow the inline axis. Unit choice alone does not establish text enlargement or SC 1.4.4 conformance; verify required enlargement without loss in actual content.",
        "sha256": "9491131a027aff56a5afae5997055d37a194e0990aebfa29c5800e803dd7ad45"
      }
    ]
  },
  {
    "action_id": "A-Q13",
    "result_ids": [
      "Q13"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "path": "knowledge/design/guides/layout.md",
    "line_span": [
      940,
      941
    ],
    "byte_offsets": [
      44970,
      45051
    ],
    "literal_original": "The modular scale itself is a\ngeometric progression: `size(n) = base × ratio^n`.",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-Q14",
    "result_ids": [
      "Q14"
    ],
    "disposition": "correct",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "path": "knowledge/design/guides/layout.md",
    "line_span": [
      941,
      944
    ],
    "byte_offsets": [
      45052,
      45208
    ],
    "literal_original": "Interpolating between\ntwo geometric progressions produces a family of curves, each\nasymptotically approaching the higher progression as the viewport\nwidens.",
    "replacement": "The finite clamp reaches and remains at its bound; it does not asymptotically approach it.",
    "replacement_sha256": "f0a7d0a2dac1e1e67aed3360e0ef92722d141b467a977cefabe00e56e0a84bb8",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      90
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q14.P1",
        "byte_bounds": [
          0,
          90
        ],
        "text": "The finite clamp reaches and remains at its bound; it does not asymptotically approach it.",
        "sha256": "f0a7d0a2dac1e1e67aed3360e0ef92722d141b467a977cefabe00e56e0a84bb8"
      }
    ]
  },
  {
    "action_id": "A-Q15",
    "result_ids": [
      "Q15"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "path": "knowledge/design/guides/layout.md",
    "line_span": [
      944,
      945
    ],
    "byte_offsets": [
      45209,
      45314
    ],
    "literal_original": "This is why the visual hierarchy intensifies on larger screens\nwithout any explicit instruction to do so.",
    "replacement": "The resulting visual hierarchy depends on selected values, typefaces and content; review it at intended sizes.",
    "replacement_sha256": "8cf776ad20abc9c1dcd6971cc4e823ef15a104b781d748aa69ac5fb81305d3be",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      110
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q15.P1",
        "byte_bounds": [
          0,
          110
        ],
        "text": "The resulting visual hierarchy depends on selected values, typefaces and content; review it at intended sizes.",
        "sha256": "8cf776ad20abc9c1dcd6971cc4e823ef15a104b781d748aa69ac5fb81305d3be"
      }
    ]
  },
  {
    "action_id": "A-Q16",
    "result_ids": [
      "Q16"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845",
    "path": "knowledge/design/guides/breaking-the-layout-monoculture.md",
    "line_span": [
      198,
      201
    ],
    "byte_offsets": [
      7406,
      7622
    ],
    "literal_original": "Utopia (James Gilyead and Trys Mudford) defines type and space at\nminimum and maximum viewport widths with different modular scale ratios,\nthen interpolates between them via `clamp()` with mixed `rem` and `vi`\nunits.",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-Q17",
    "result_ids": [
      "Q17"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845",
    "path": "knowledge/design/guides/breaking-the-layout-monoculture.md",
    "line_span": [
      201,
      201
    ],
    "byte_offsets": [
      7623,
      7682
    ],
    "literal_original": "The result: smooth, continuous type and spacing transitions",
    "replacement": "a given set of values should be checked for intended continuity.",
    "replacement_sha256": "ba7c69bd2f3cb6f136d27aac4cff4846d2da67463c8e0648c925996e5ae4ca9a",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      64
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q17.P1",
        "byte_bounds": [
          0,
          64
        ],
        "text": "a given set of values should be checked for intended continuity.",
        "sha256": "ba7c69bd2f3cb6f136d27aac4cff4846d2da67463c8e0648c925996e5ae4ca9a"
      }
    ]
  },
  {
    "action_id": "A-Q18",
    "result_ids": [
      "Q18"
    ],
    "disposition": "correct",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845",
    "path": "knowledge/design/guides/breaking-the-layout-monoculture.md",
    "line_span": [
      201,
      202
    ],
    "byte_offsets": [
      7683,
      7734
    ],
    "literal_original": "with\nno jarring layout shifts at any viewport size.",
    "replacement": " Evaluate layout stability in actual content and viewport range.",
    "replacement_sha256": "d0a2da12bb98721f47ea28ace695993074897c7769c7a24259c07c47816fd263",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      64
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q18.P1",
        "byte_bounds": [
          0,
          64
        ],
        "text": " Evaluate layout stability in actual content and viewport range.",
        "sha256": "d0a2da12bb98721f47ea28ace695993074897c7769c7a24259c07c47816fd263"
      }
    ]
  },
  {
    "action_id": "A-Q19",
    "result_ids": [
      "Q19"
    ],
    "disposition": "correct",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845",
    "path": "knowledge/design/guides/breaking-the-layout-monoculture.md",
    "line_span": [
      202,
      204
    ],
    "byte_offsets": [
      7735,
      7845
    ],
    "literal_original": "The use of `vi` (viewport\ninline) rather than `vw` preserves zoom accessibility, satisfying WCAG\nrequirements.",
    "replacement": "Using `vi` selects the viewport inline axis; it does not by itself establish text enlargement or reflow. Test required outcomes in actual content.",
    "replacement_sha256": "aff41731b1ed302c9eb2002e77cb8350cb46442d85f78b5af8fc5c420c319bc8",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      146
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q19.P1",
        "byte_bounds": [
          0,
          146
        ],
        "text": "Using `vi` selects the viewport inline axis; it does not by itself establish text enlargement or reflow. Test required outcomes in actual content.",
        "sha256": "aff41731b1ed302c9eb2002e77cb8350cb46442d85f78b5af8fc5c420c319bc8"
      }
    ]
  },
  {
    "action_id": "A-Q20",
    "result_ids": [
      "Q20"
    ],
    "disposition": "correct",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845",
    "path": "knowledge/design/guides/breaking-the-layout-monoculture.md",
    "line_span": [
      218,
      218
    ],
    "byte_offsets": [
      8535,
      8571
    ],
    "literal_original": "Breakpoint-free, modular, accessible",
    "replacement": "Test text resizing and reflow separately",
    "replacement_sha256": "af638d939fd4630c90ac86129110848c7b3334993fc5155fc3c05215c53ad88a",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      40
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q20.P1",
        "byte_bounds": [
          0,
          40
        ],
        "text": "Test text resizing and reflow separately",
        "sha256": "af638d939fd4630c90ac86129110848c7b3334993fc5155fc3c05215c53ad88a"
      }
    ]
  },
  {
    "action_id": "A-Q21",
    "result_ids": [
      "Q21"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b",
    "path": "knowledge/design/guides/design.md",
    "line_span": [
      148,
      150
    ],
    "byte_offsets": [
      5426,
      5562
    ],
    "literal_original": "Fluid type scales that\ninterpolate between viewport widths should use the `vi` unit (viewport\ninline), which respects writing direction.",
    "replacement": "Choose `vi` when the viewport inline axis is the intended sizing input; check target writing mode.",
    "replacement_sha256": "b37dd3e212b10914100fff54497b680d31ec191954c09398ddd1687ff06bd34e",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      98
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q21.P1",
        "byte_bounds": [
          0,
          98
        ],
        "text": "Choose `vi` when the viewport inline axis is the intended sizing input; check target writing mode.",
        "sha256": "b37dd3e212b10914100fff54497b680d31ec191954c09398ddd1687ff06bd34e"
      }
    ]
  },
  {
    "action_id": "A-Q22",
    "result_ids": [
      "Q22"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b",
    "path": "knowledge/design/guides/design.md",
    "line_span": [
      150,
      151
    ],
    "byte_offsets": [
      5563,
      5650
    ],
    "literal_original": "Spacing should be defined in\n`rem`, which scales with the user\\'s font size preference.",
    "replacement": "Spacing in `rem` follows computed root font-size; verify how author rules and user settings affect it.",
    "replacement_sha256": "461b281981ddccaca0edaeee95671e2af0c1929d462021d2038e0b0136ecddde",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      102
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q22.P1",
        "byte_bounds": [
          0,
          102
        ],
        "text": "Spacing in `rem` follows computed root font-size; verify how author rules and user settings affect it.",
        "sha256": "461b281981ddccaca0edaeee95671e2af0c1929d462021d2038e0b0136ecddde"
      }
    ]
  },
  {
    "action_id": "A-Q23",
    "result_ids": [
      "Q23"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "8a9f1ab35dee3373ebbf1460416e334adffcd908f095463fa015c6ef0a5f5d7c",
    "path": "knowledge/design/guides/type.md",
    "line_span": [
      473,
      475
    ],
    "byte_offsets": [
      18047,
      18138
    ],
    "literal_original": "At\n360px the effective ratio is 1.25 (major third); at 1440px it\\'s 1.333\n(perfect fourth).",
    "replacement": "At 360px, reconcile the printed 1.25 with Project10 baseline 1.2 before describing a project endpoint. The 1440px 1.333 value is approximate for 4/3.",
    "replacement_sha256": "63ba0133aeb44f38872b5a288c49faf475c1b657895fe0aa4ad61b9a00ea04ad",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      149
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q23.P1",
        "byte_bounds": [
          0,
          149
        ],
        "text": "At 360px, reconcile the printed 1.25 with Project10 baseline 1.2 before describing a project endpoint. The 1440px 1.333 value is approximate for 4/3.",
        "sha256": "63ba0133aeb44f38872b5a288c49faf475c1b657895fe0aa4ad61b9a00ea04ad"
      }
    ]
  },
  {
    "action_id": "A-Q24",
    "result_ids": [
      "Q24"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "8a9f1ab35dee3373ebbf1460416e334adffcd908f095463fa015c6ef0a5f5d7c",
    "path": "knowledge/design/guides/type.md",
    "line_span": [
      475,
      476
    ],
    "byte_offsets": [
      18139,
      18223
    ],
    "literal_original": "This means headings grow proportionally faster than\nbody text as the viewport widens",
    "replacement": "Whether headings grow proportionally faster than body text depends on selected values and content.",
    "replacement_sha256": "d311301841b61ffaa99da609b71adc152185385b1b1e811fffd15ecf3e8bd4d6",
    "owner": "Arc04 application; Arc03 behavior evidence",
    "replacement_bounds": [
      0,
      98
    ],
    "replacement_parts": [
      {
        "part_id": "A-Q24.P1",
        "byte_bounds": [
          0,
          98
        ],
        "text": "Whether headings grow proportionally faster than body text depends on selected values and content.",
        "sha256": "d311301841b61ffaa99da609b71adc152185385b1b1e811fffd15ecf3e8bd4d6"
      }
    ]
  }
]
```

## Arc03 behavior-test handoff

After Arc04 pins the composed content and source revision, test actual browser behavior and record browser/OS/version, CSS viewport, writing mode, computed root size, loaded fonts, user settings, baseline and enlarged rendered dimensions, mechanism, intermediate steps, overflow, clipping, overlap, content and function loss. A CSS unit, model row or screenshot is not conformance evidence.

**SC 1.4.4:** measure text enlargement to 200% without assistive technology and without loss of content/functionality; preserve exceptions for captions and images of text. Measure from actual baseline and report offered intermediate steps. Informative Resize Text guidance permits one supported user-agent scaling path; do not require every mechanism. State stronger local preference policy separately.

**SC 1.4.10:** measure at 320 CSS px width for vertical-scroll content or 256 CSS px height for horizontal-scroll content; record no-loss and two-dimensional scrolling separately. Preserve exception only for content whose use or meaning requires 2D layout. Check tables/cells, controls and surrounding content. Passing enlargement does not imply reflow.

Test baseline, available text-only resize, page zoom, root preference and author override as distinct cases, horizontal/vertical writing, expanded text, long tokens, controls, table and justified 2D content. Mark unavailable cases unrun. Arc03 owns protocol/results, Arc04 application. Repeat after relevant CSS/font/content/root changes. No runtime result is claimed here.
