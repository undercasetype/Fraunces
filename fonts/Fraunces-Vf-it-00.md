## Fontbakery report

Fontbakery version: 0.7.29

<details>
<summary><b>[5] Fraunces-Italic[SOFT,WONK,opsz,wght].ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: TYPOGRAPHIC_SUBFAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/typographicsubfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicsubfamilyname)

* 🔥 **FAIL** TYPOGRAPHIC_SUBFAMILY_NAME for Win "144pt S100 Black Italic" is incorrect. It must be "Black Italic". [code: bad-typo-win]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check variable font instances have correct names</summary>

* [com.google.fonts/check/varfont_instance_names](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_instance_names)

* 🔥 **FAIL** Following instances are not supported: 
	- 9pt S000 Thin Italic
	- 9pt S000 Light Italic
	- 9pt S000 Italic
	- 9pt S000 SemiBold Italic
	- 9pt S000 Bold Italic
	- 9pt S000 Black Italic
	- 9pt S050 Thin Italic
	- 9pt S050 Light Italic
	- 9pt S050 Italic
	- 9pt S050 SemiBold Italic
	- 9pt S050 Bold Italic
	- 9pt S050 Black Italic
	- 9pt S100 Thin Italic
	- 9pt S100 Light Italic
	- 9pt S100 Italic
	- 9pt S100 SemiBold Italic
	- 9pt S100 Bold Italic
	- 9pt S100 Black Italic
	- 72pt S000 Thin Italic
	- 72pt S000 Light Italic
	- 72pt S000 Italic
	- 72pt S000 SemiBold Italic
	- 72pt S000 Bold Italic
	- 72pt S000 Black Italic
	- 72pt S050 Thin Italic
	- 72pt S050 Light Italic
	- 72pt S050 Italic
	- 72pt S050 SemiBold Italic
	- 72pt S050 Bold Italic
	- 72pt S050 Black Italic
	- 72pt S100 Thin Italic
	- 72pt S100 Light Italic
	- 72pt S100 Italic
	- 72pt S100 SemiBold Italic
	- 72pt S100 Bold Italic
	- 72pt S100 Black Italic
	- 144pt S000 Thin Italic
	- 144pt S000 Light Italic
	- 144pt S000 Italic
	- 144pt S000 SemiBold Italic
	- 144pt S000 Bold Italic
	- 144pt S000 Black Italic
	- 144pt S050 Thin Italic
	- 144pt S050 Light Italic
	- 144pt S050 Italic
	- 144pt S050 SemiBold Italic
	- 144pt S050 Bold Italic
	- 144pt S050 Black Italic
	- 144pt S100 Thin Italic
	- 144pt S100 Light Italic
	- 144pt S100 Italic
	- 144pt S100 SemiBold Italic
	- 144pt S100 Bold Italic
	- 144pt S100 Black Italic

Further info can be found in our spec https://github.com/googlefonts/gf-docs/tree/master/Spec#fvar-instances [code: bad-instance-names]

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
<summary>⚠ <b>WARN:</b> Font has **proper** whitespace glyph names?</summary>

* [com.google.fonts/check/whitespace_glyphnames](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames)
<pre>--- Rationale ---

This check enforces adherence to recommended whitespace (codepoints 0020 and
00A0) glyph names according to the Adobe Glyph List.


</pre>

* ⚠ **WARN** Glyph 0x0020 is called "uni0020": Change to "space" [code: not-recommended-0020]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 2 | 3 | 82 | 8 | 82 | 0 |
| 0% | 1% | 2% | 46% | 5% | 46% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
