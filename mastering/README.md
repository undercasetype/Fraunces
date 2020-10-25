# Mastering

## Making a GitHub release

It is useful to make zips for [GitHub Releases](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/managing-releases-in-a-repository) if/when you make updates to the font.

To prepare a new release, use:

```bash
mastering/make-github-release/make-release.sh
```

(This assumes you have already built with the correct version numbering in `fonts/Fraunces[SOFT,WONK,opsz,wght].ttf`. To check this, you can use [font-v](https://github.com/source-foundry/font-v/), or view `name ID 5` with `ttx -t name -o- fonts/Fraunces[SOFT,WONK,opsz,wght].ttf`.)

It will copy files to a folder like `UnderCaseType_Fraunces_1.001` and output a zip like `UnderCaseType_Fraunces_1.001.zip`.

You can then drag-and-drop this zip into your release notes.

NOTE: To edit the recommendations in the `README.md` included with releases, update `mastering/make-github-release/data/release-notes--all.md`, which is copied into release zips.


## Making PRs to google/fonts for updates

You can use `mastering/googlefonts/gftools-packager-fraunces.sh` to make PRs to [google/fonts](https://github.com/google/fonts). However, this tool may evolve. Also, you need push access to google/fonts for this to work.
