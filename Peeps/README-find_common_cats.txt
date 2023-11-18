2023-11-17 RTK

Notes and fixes for script "find_common_cats.py"

In-code notes are marked with XXX

General things

    Does this script need more than one input file?
    Does it need argparse or could it be hardcoded?
        For argpase, make help as helpful as you can; More details, etc
    Does this supposed to use an "assignment4/io_utils" module?
        If yes, I wrote this ... not included in what was sent
        I created a script version that uses this too
    Style-wise, do not be scared to make more (blank) space to clarify things
    
Specific issues

    First line must start "#!/usr/bin/env" not "#!usr/bin/env" 
    Created in INPUT dir to hold input data files.
    Added try / except blocks for file line parsing; When the splitting of data 
        into parts fails, it report "Problem" but ignores line and continues.
    Added line counter to skip the header and also report any problem line
    The strings in "category_descriptions" included non-asci characters; 
        This is from cut-and-paste. Should test such things out in Jupyter, etc to find and fix bogus chars.
    The output directory has to be created before you can write to it.
        File open cannot create directories, just files.

Call:

    find_common_cats-v2.py -i1 INPUT/HUGO_genes.txt -i2 INPUT/chr21_genes.txt

    find_common_cats-v2-io.py -i1 INPUT/HUGO_genes.txt -i2 INPUT/chr21_genes.txt

Compare outputs (with / without use of io_utils):

    diff OUTPUT/categories-v2-io.txt OUTPUT/categories-v2.txt

