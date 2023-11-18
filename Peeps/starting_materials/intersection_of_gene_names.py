#!usr/bin/env python

"""
Emily Koehler 11-19-23

File: intersection_of_gene_names.py

This script takes two .txt files and returns the number of common genes found between the two and outputs a file containing the commonn genes

INPUT: 2 .txt files that are tab delimited

OUTPUT: intersection_output.txt

"""

import argparse
import assignment4.io_utils as io_utils
from collections import Counter

def find_common_genes():
    chr21_genes = []
    hugo_genes = []

    # Read gene symbols from chr21_genes.txt file
    with open('/Users/emilykoehler/Downloads/chr21_genes.txt', 'r') as chr21_file:
        for line in chr21_file:
            columns = line.strip().split('\t')  # Assuming tab-separated columns
            if len(columns) >= 1:  # Ensure there is at least one column
                gene_symbol = columns[0].strip().lower()  # Extract the gene symbol from the first column
                chr21_genes.append(gene_symbol)

    # Read gene symbols from HUGO_genes.txt
    hugo_genes = set()  # Initialize set for hugo_genes
    with open('/Users/emilykoehler/Downloads/HUGO_genes.txt', 'r') as hugo_file:
        for line in hugo_file:
            columns = line.strip().split('\t')  # Assuming tab-separated columns
            if len(columns) >= 1:  # Ensure there is at least one column
                gene_symbol = columns[0].strip().lower()  # Extract the gene symbol from the first column
                hugo_genes.add(gene_symbol)


# Debugging: Print gene symbols from both files
#    print("Gene symbols in chr21_genes.txt:")
#    print(chr21_genes)
#    print("Gene symbols in HUGO_genes.txt:")
#    print(hugo_genes)

    # Count gene symbols in both lists
    chr21_gene_counts = Counter(chr21_genes)
    hugo_gene_counts = Counter(hugo_genes)

    # Find common gene symbols by taking the minimum count
    common_genes = []
    for gene_symbol, count in chr21_gene_counts.items():
        if gene_symbol in hugo_gene_counts:
            common_genes.extend([gene_symbol] * min(count, hugo_gene_counts[gene_symbol]))

    # Sort the common gene symbols in ascending order
    common_genes_sorted = sorted(common_genes)

    # Write the common genes to an output file called intersection_output.txt
    output_file_path = 'OUTPUT/intersection_output.txt'
    with open(output_file_path, 'w') as output_file:
        for gene_symbol in common_genes_sorted:
            output_file.write(gene_symbol + '\n')

    # Print how many common genes were found
    print(f'Number of common gene symbols found: {len(common_genes_sorted)}')

if __name__ == "__main__":
    find_common_genes()

