# !/bin/bash

gftools packager \
    mastering/googlefonts/upstream.yaml \
    /Users/stephennixon/type-repos/google-font-repos/fonts \
    # yes, update the files in fonts/ofl/fraunces
    --force
    # --branch Fraunces 144pt ExtraSoft Black