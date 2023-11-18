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

OUT_FNAME = "OUTPUT/common_genes-v2.txt"


def find_common_genes():
    chr21_genes = []
    hugo_genes = []

    # Read gene symbols from chr21_genes.txt file
    #with open('/Users/emilykoehler/Downloads/chr21_genes.txt', 'r') as chr21_file:
    with open(CAT_FNAME, 'r') as chr21_file:
        n_line = 0
        for line in chr21_file:
            n_line += 1

            # Skip the header line
            if n_line < 2:
                continue

            columns = line.strip().split('\t')  # Assuming tab-separated columns
            if len(columns) >= 1:  # Ensure there is at least one column
                gene_symbol = columns[0].strip().lower()  # Extract the gene symbol from the first column
                chr21_genes.append(gene_symbol)

    # Read gene symbols from HUGO_genes.txt
    #with open('/Users/emilykoehler/Downloads/HUGO_genes.txt', 'r') as hugo_file:
    with open(DESC_FNAME, 'r') as hugo_file:
        n_line = 0
        for line in hugo_file:
            n_line += 1

            # Skip the header line
            if n_line < 2:
                continue

            columns = line.strip().split('\t')  # Assuming tab-separated columns
            if len(columns) >= 1:  # Ensure there is at least one column
                gene_symbol = columns[0].strip().lower()  # Extract the gene symbol from the first column
                hugo_genes.append(gene_symbol)


    # Debugging: Print gene symbols from both files
    #    print("Gene symbols in chr21_genes.txt:")
    #    print(chr21_genes)
    #    print("Gene symbols in HUGO_genes.txt:")
    #    print(hugo_genes)


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

