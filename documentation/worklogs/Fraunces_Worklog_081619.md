# Fraunces Worklog - August 16th - Spencer

## _ital_ Axis

Today, I'm going to see if I can get the _ital_ axis working in the browser, so that the font files can have the same family name. Currently, I was using a different family name for each style (Fraunces and Fraunces Italic). My impression, for Variable Fonts, is that the ital axis was created to handle this difference.

In order to build a VF, all masters need to be interpolatable... but an italic axis supposedly should toggle between different forms. How is this supposed to be set up?? Do I have to create .alt glyphs for ALL my italic characters? This seems like an absurd approach.

Supposedly, the italic axis is a binary axis that is supposed to allow for _true_ italics, yet I'm not seeing any actual implementations of this. Am I crazy??

So, my question: How does the ital axis work with two separate VF files? With static .ttf files, Style Mapping is used to link a Regular to an Italic. 

Currently, I have my family names set as Fraunces and Fraunces Italic. 

All the implementations I'm seeing of the ital axis on [v-fonts.com](https://www.v-fonts.com) seem to be a slant axis, with a few substitutions made. 

Okay, so I think I found the answer to my questions [here!](https://github.com/TypeNetwork/Amstelvar/issues/35)

It seems like the way I have it set up, with Fraunces and Fraunces Italic as seperate files is the way to go. We will use the STAT table to link these together (which I assume is how the _ital_ axis works)

## _WONK_ Axis

So now that I have the italic situation more or less settled (I opened an issue in the repo just to confirm that this approach is the way to go), how do I incorporate a _WONK_ axis, without duplicating masters for the entire design space? 

I think I figured this out! I reinserted the masters (so the masters are all doubled up). I'm going to try a VF build and see if this works. Here are the rules I inserted into my .designspace file for future reference:

```
  <rules>
    <rule name="wonk">
      <conditionset>
        <condition name="optical" minimum="9" maximum="18"/>
        <condition name="weight" minimum="100" maximum="900"/>
      </conditionset>
      <conditionset>
        <condition name="wonk" minimum="0" maximum="0.49"/>
      </conditionset>
      <sub name="b" with="b.alt"/>
      <sub name="h" with="h.alt"/>
      <sub name="v" with="v.alt"/>
      <sub name="ampersand" with="ampersand.alt"/>
    </rule>
  </rules>
 ```

I built and tested in the browser, and it works beautifully! Doubling up these additional masters does seem to increase file size however from around 50kb –> 60kb, which is like a 20% gain. Not sure if this is ideal. I'll post this as a solution to the repo and see if Dave thinks this is a good solution.