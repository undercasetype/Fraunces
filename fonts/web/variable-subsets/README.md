# Self-hosting subset fonts

Fonts are subset with the expectation that multiple font files will be used along with the CSS property `unicode-range` to specify unicodes present in each file. This enables a website browser to automatically download **only** the fonts needed to display text on a given site, and [works in all modern browsers](https://caniuse.com/font-unicode-range).

To support only "Latin Basic" characters, you can use just the `latin_basic` font file. To use "Latin Extended" characters, you should use *both* `latin_basic` *and* `latin_ext` font files (this makes sure basic punctuation isn’t left out). For Vietnamese, you must use `latin_basic` *and* `vietnamese` subsets at minimum, but may wish to also use `latin_ext`.

Files are provided along with example CSS to provide an example of how this works. Feel free to copy the fonts.css to jump-start your own projects!
