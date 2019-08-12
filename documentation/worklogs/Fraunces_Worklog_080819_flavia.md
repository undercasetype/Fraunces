# Fraunces Worklog: August 8th - Flavia

Worked on generating new Variable Fonts inserting the Goofy Axis for both Roman and Italic. Currently the Goofy Axis is a "hack" to prove the concept, so we can get it approved by Google before streamlining the process. 

For now, we are proceeding as it follows:

1. Duplicate the existing masters and rename including the Goofy poles. 
More delicate forms means minimum Goofy, more chunky/roundness means maximum Goofy.
Fraunces-Black OpMax GoofMin
Fraunces-Black OpMin GoofMax
Fraunces-Light OpMax GoofMin
Fraunces-Light OpMin GoofMax

2. Create the new masters via interpolation
Use the Frances2 Superpolator file, reload the masters there were renamed.
Generate the new masters:
Fraunces-Black OptMax GoofMax: weight 1000, optical 48
Fraunces-Light OptMax GoofMax: weight 100, optical 48
Fraunces-Light OptMin GoofMin: weight 1000, optical 24
Fraunces-Black OptMin GoofMin: weight 1000, optical 24

3. Make manual edits on both Black and Light OptMax GoofMax masters
Re-scale lowercase to match x-height values from OptMax GoofMin (Black: 94.6%, Light: 94%).
Raise back ascender and descenders.
Tight the spacing up to make it look more display: about 10units for Black, 20units for Light — Maybe we could also follow OptMaxGoofMax spacing?

4. Create the DesigSpace file (if not yet)
Fraunces_GoofyAxis.sp3

4. Prepolator and VarFont prep
Make sure everything is compatible.

6. Add rules for Optical Axis manually in the DesignSpace file (via TextEdt).
<axis tag="opsz" name="optical" minimum="9" maximum="144" default="9">
      <labelname xml:lang="en">Optical Size</labelname>
      <map input="9" output="9"/>
      <map input="18" output="24"/>
      <map input="24" output="48"/>
      <map input="36" output="72"/>
      <map input="48" output="100"/>
      <map input="72" output="130"/>
      <map input="96" output="138"/>
      <map input="122" output="142"/>
      <map input="144" output="144"/>
    </axis>
    <axis tag="goof" name="goofy" minimum="1" maximum="100" default="1"/>
    <axis tag="wght" name="weight" minimum="100" maximum="1000" default="100"/>
  </axes>
  <rules>
    <rule name="wonk">
      <conditionset>
        <condition name="optical" minimum="9" maximum="18"/>
        <condition name="goofy" minimum="1" maximum="100"/>
        <condition name="weight" minimum="100" maximum="1000"/>
      </conditionset>
      <sub name="h" with="h.alt"/>
      <sub name="m" with="m.alt"/>
      <sub name="n" with="n.alt"/>
      <sub name="s" with="s.alt"/>
    </rule> 

7. Generate Variable_ttf
Open hacker mode, and cross your fingers!

** Repeat for Italic
Scaling values will change (Black: 96.3%, Light: 96%).



