## Fontbakery report

Fontbakery version: 0.7.29

<details>
<summary><b>[12] Fraunces[SOFT,WONK,opsz,wght].ttf</b></summary>
<details>
<summary>💔 <b>ERROR:</b> Each font in set of sibling families must have the same set of vertical metrics values.</summary>

* [com.google.fonts/check/superfamily/vertical_metrics](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/superfamily/vertical_metrics)
<pre>--- Rationale ---

We may want all fonts within a super-family (all sibling families) to have the
same vertical metrics so their line spacing is consistent across the
super-family.

This is an experimental extended version of
com.google.fonts/check/superfamily/vertical_metrics and for now it will only
result in WARNs.


</pre>

* 💔 **ERROR** The check <FontBakeryCheck:com.google.fonts/check/superfamily/vertical_metrics> had an error: FailedConditionError: The condition <FontBakeryCondition:superfamily_ttFonts> had an error: TTLibError: Not a TrueType or OpenType font (not enough data)

</details>
<details>
<summary>🔥 <b>FAIL:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering?</summary>

* [com.google.fonts/check/gasp](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp)
<pre>--- Rationale ---

Traditionally version 0 &#x27;gasp&#x27; tables were set so that font sizes below 8 ppem
had no grid fitting but did have antialiasing. From 9-16 ppem, just grid
fitting. And fonts above 17ppem had both antialiasing and grid fitting toggled
on. The use of accelerated graphics cards and higher resolution screens make
this approach obsolete. Microsoft&#x27;s DirectWrite pushed this even further with
much improved rendering built into the OS and apps.

In this scenario it makes sense to simply toggle all 4 flags ON for all font
sizes.


</pre>

* 🔥 **FAIL** Font is missing the 'gasp' table. Try exporting the font with autohinting enabled.
If you are dealing with an unhinted font, it can be fixed by running the fonts through the command 'gftools fix-nonhinting'
GFTools is available at https://pypi.org/project/gftools/ [code: lacks-gasp]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: TYPOGRAPHIC_SUBFAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/typographicsubfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicsubfamilyname)

* 🔥 **FAIL** TYPOGRAPHIC_SUBFAMILY_NAME for Win "144pt S100 Black" is incorrect. It must be "Black". [code: bad-typo-win]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Font enables smart dropout control in "prep" table instructions?</summary>

* [com.google.fonts/check/smart_dropout](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/smart_dropout)
<pre>--- Rationale ---

This setup is meant to ensure consistent rendering quality for fonts across all
devices (with different rendering/hinting capabilities).

Below is the snippet of instructions we expect to see in the fonts:
B8 01 FF    PUSHW 0x01FF
85          SCANCTRL (unconditinally turn on
                      dropout control mode)
B0 04       PUSHB 0x04
8D          SCANTYPE (enable smart dropout control)

&quot;Smart dropout control&quot; means activating rules 1, 2 and 5:
Rule 1: If a pixel&#x27;s center falls within the glyph outline,
        that pixel is turned on.
Rule 2: If a contour falls exactly on a pixel&#x27;s center,
        that pixel is turned on.
Rule 5: If a scan line between two adjacent pixel centers
        (either vertical or horizontal) is intersected
        by both an on-Transition contour and an off-Transition
        contour and neither of the pixels was already turned on
        by rules 1 and 2, turn on the pixel which is closer to
        the midpoint between the on-Transition contour and
        off-Transition contour. This is &quot;Smart&quot; dropout control.

For more detailed info (such as other rules not enabled in this snippet),
please refer to the TrueType Instruction Set documentation.


</pre>

* 🔥 **FAIL** The 'prep' table does not contain TrueType instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the `gftools fix-nonhinting` script. [code: lacks-smart-dropout]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check variable font instances have correct names</summary>

* [com.google.fonts/check/varfont_instance_names](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_instance_names)

* 🔥 **FAIL** Following instances are not supported: 
	- 9pt S000 Thin
	- 9pt S000 Light
	- 9pt S000 Regular
	- 9pt S000 SemiBold
	- 9pt S000 Bold
	- 9pt S000 Black
	- 9pt S050 Thin
	- 9pt S050 Light
	- 9pt S050 Regular
	- 9pt S050 SemiBold
	- 9pt S050 Bold
	- 9pt S050 Black
	- 9pt S100 Thin
	- 9pt S100 Light
	- 9pt S100 Regular
	- 9pt S100 SemiBold
	- 9pt S100 Bold
	- 9pt S100 Black
	- 72pt S000 Thin
	- 72pt S000 Light
	- 72pt S000 Regular
	- 72pt S000 SemiBold
	- 72pt S000 Bold
	- 72pt S000 Black
	- 72pt S050 Thin
	- 72pt S050 Light
	- 72pt S050 Regular
	- 72pt S050 SemiBold
	- 72pt S050 Bold
	- 72pt S050 Black
	- 72pt S100 Thin
	- 72pt S100 Light
	- 72pt S100 Regular
	- 72pt S100 SemiBold
	- 72pt S100 Bold
	- 72pt S100 Black
	- 144pt S000 Thin
	- 144pt S000 Light
	- 144pt S000 Regular
	- 144pt S000 SemiBold
	- 144pt S000 Bold
	- 144pt S000 Black
	- 144pt S050 Thin
	- 144pt S050 Light
	- 144pt S050 Regular
	- 144pt S050 SemiBold
	- 144pt S050 Bold
	- 144pt S050 Black

Further info can be found in our spec https://github.com/googlefonts/gf-docs/tree/master/Spec#fvar-instances [code: bad-instance-names]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Are there unwanted tables?</summary>

* [com.google.fonts/check/unwanted_tables](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unwanted_tables)
<pre>--- Rationale ---

Some font editors store source data in their own SFNT tables, and these can
sometimes sneak into final release files, which should only have OpenType spec
tables.


</pre>

* 🔥 **FAIL** The following unwanted font tables were found:
Table: MVAR
Reason: Produces a bug in DirectWrite which causes https://bugzilla.mozilla.org/show_bug.cgi?id=1492477, https://github.com/google/fonts/issues/2085

They can be removed with the gftools fix-unwanted-tables script.

</details>
<details>
<summary>🔥 <b>FAIL:</b> Does the font have a DSIG table?</summary>

* [com.google.fonts/check/dsig](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/dsig.html#com.google.fonts/check/dsig)
<pre>--- Rationale ---

Microsoft Office 2013 and below products expect fonts to have a digital
signature declared in a DSIG table in order to implement OpenType features. The
EOL date for Microsoft Office 2013 products is 4/11/2023. This issue does not
impact Microsoft Office 2016 and above products. 

This checks verifies that this signature is available in the font.

A fake signature is enough to address this issue. If needed, a dummy table can
be added to the font with the `gftools fix-dsig` script available at
https://github.com/googlefonts/gftools

Reference: https://github.com/googlefonts/fontbakery/issues/1845


</pre>

* 🔥 **FAIL** This font lacks a digital signature (DSIG table). Some applications may require one (even if only a dummy placeholder) in order to work properly. You can add a DSIG table by running the `gftools fix-dsig` script. [code: lacks-signature]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---

All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.

If using GlyphsApp, ligature carets can be set directly on canvas by accessing
the `Glyph -&gt; Set Anchors` menu option or by pressing the `Cmd+U` keyboard
shortcut.


</pre>

* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---

Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).


</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- uni0066 + uni0066
	- uni0066 + uni0069
	- uni0069 + uni0066
	- uni0066 + uni006C
	- uni006C + uni0066
	- uni0069 + uni006C

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---

According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.

After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.

[1]
https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179


</pre>

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Fraunces 144pt S100 Black' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has **proper** whitespace glyph names?</summary>

* [com.google.fonts/check/whitespace_glyphnames](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames)
<pre>--- Rationale ---

This check enforces adherence to recommended whitespace (codepoints 0020 and
00A0) glyph names according to the Adobe Glyph List.


</pre>

* ⚠ **WARN** Glyph 0x0020 is called "uni0020": Change to "space" [code: not-recommended-0020]

</details>
<details>
<summary>⚠ <b>WARN:</b> The variable font 'opsz' (Optical Size) axis coordinate should be between 9 and 13 on the 'Regular' instance.</summary>

* [com.google.fonts/check/varfont/regular_opsz_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_opsz_coord)
<pre>--- Rationale ---

According to the Open-Type spec&#x27;s registered design-variation tag &#x27;opsz&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_opsz

If a variable font has a &#x27;opsz&#x27; (Optical Size) axis, then the coordinate of its
&#x27;Regular&#x27; instance is recommended to be a value in the range 9 to 13.


</pre>

* ⚠ **WARN** The "opsz" (Optical Size) coordinate on the "Regular" instance is recommended to be a value in the range 9 to 13. Got 144.0 instead. [code: out-of-range]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 1 | 6 | 5 | 78 | 7 | 80 | 0 |
| 1% | 3% | 3% | 44% | 4% | 45% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
