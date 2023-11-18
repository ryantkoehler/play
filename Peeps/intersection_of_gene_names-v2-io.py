#!/usr/bin/env python

"""
Emily Koehler 11-19-23

File: intersection_of_gene_names.py

This script takes two .txt files and returns the number of common genes found 
between the two and outputs a file containing the commonn genes

INPUT: 2 .txt files that are tab delimited, Genes in first col

OUTPUT: intersection_output.txt

"""

# XXX needed?
#import argparse
import assignment4.io_utils as io_utils
# XXX needed
#from collections import Counter


# Hardcoded filenames
#CAT_FNAME = '/Users/emilykoehler/Downloads/chr21_genes.txt'
#DESC_FNAME = '/Users/emilykoehler/Downloads/HUGO_genes.txt'

CAT_FNAME = 'INPUT/chr21_genes.txt'
DESC_FNAME = 'INPUT/HUGO_genes.txt'

OUT_FNAME = "OUTPUT/common_genes-v2-io.txt"


def list_to_lower(in_list):
    """Cast all list items to lower case

    Return list
    """
    out_list = []
    for s in in_list:
        out_list.append(s.lower())
    return out_list


def find_common_genes():

    # Load lists of genes from first col of tab delim files
    chr21_genes = io_utils.get_data_file_col(CAT_FNAME, col=1, sep='\t')
    hugo_genes = io_utils.get_data_file_col(DESC_FNAME, col=1, sep='\t')

    # Set all genes are lowercase
    # Ignore first list elements as these are from input file header
    chr21_genes = list_to_lower(chr21_genes[1:])
    hugo_genes = list_to_lower(hugo_genes[1:])

    # Convert lists to sets and intersect
    chr12_set = set(chr21_genes)
    hugo_set = set(hugo_genes)
    # Intersect = logical 'And' = amperstand operator
    both_set = chr12_set & hugo_set

    # Counts of inputs and intersected list
    chr21_gene_counts = len(chr21_genes)
    hugo_gene_counts = len(hugo_genes)
    both_gene_counts = len(both_set)

    # Sort the common gene symbols in ascending order
    common_genes_sorted = sorted(both_set)

    # Write the common genes to an output file called intersection_output.txt
    with open(OUT_FNAME, 'w') as OUTFILE:
        for gene_symbol in common_genes_sorted:
            print(gene_symbol, file=OUTFILE)

    # Print story, including how many common genes were found
    print(f'Number of chr21 gene symbols found:  {chr21_gene_counts}')
    print(f'Number of HUGO gene symbols found:   {hugo_gene_counts}')
    print(f'Number of common gene symbols found: {both_gene_counts}')
    print(f"Common genes have been written to {OUT_FNAME}")

if __name__ == "__main__":
    find_common_genes()

