2023-11-17 RTK

Notes and fixes for script "intersection_of_gene_names.py"

In-code notes are marked with XXX

General things

    No need for argparse since inputs hardcoded
    No need for Counter; Using set logic. Specifically, logical AND which uses
        the '&' operator to find the intersection of sets
    Does this supposed to use an "assignment4/io_utils" module?
        If yes, I wrote this ... not included in what was sent
        I created a version that uses this too.
    
Specific issues

    First line must start "#!/usr/bin/env" not "#!usr/bin/env" 
    Created in INPUT dir to hold input data files.
        Updated INPUT and OUTPUT filenames
    Added line counters to skip header in inputs (also added to io_utils)

Calls:

    intersection_of_gene_names-v2.py

    intersection_of_gene_names-v2-io.py

Compare outputs (with / without use of io_utils):

    diff OUTPUT/common_genes-v2.txt OUTPUT/common_genes-v2-io.txt

