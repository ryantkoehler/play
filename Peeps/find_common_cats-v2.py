#!/usr/bin/env python

#Emily Koehler 11-19-23

#File: find_common_cats.py

#This script counts how many genes are in each category of a .txt file and returns a .txt file with the count and categories in ascending order 


OUT_FNAME = "OUTPUT/categories-v2.txt"


# XXX Needed? Just operating on fixed files?
import argparse
# XXX Not used?
# import assignment4.io_utils as io_utils

#input_file_path = '/Users/emilykoehler/Downloads/chr21_genes.txt'

# Define a dictionary to store category descriptions of gene categories
category_descriptions = {
    "1.1": "Genes with 100% identity over a complete cDNA with defined functional association (for example, transcription factor, kinase)",
    "1.2": "Genes with 100% identity over a complete cDNA corresponding to a gene of unknown function (for example, some of the KIAA series of large cDNAs).",
    "2.1": "Genes showing similarity or homology to a characterized cDNA from any organism (25-100% amino-acid identity). This class defines new members of human gene families, as well as new human homologues or orthologues of genes from yeast, Caenorhabditis elegans, Drosophila, mouse and so on",
    "2.2": "Genes with similarity to a putative ORF predicted in silico from the genomic sequence of any organism but which currently lacks experimental verification.",
    "3.1": "Genes with amino-acid similarity confined to a protein region specifying a functional domain (for example, zinc fingers, immunoglobulin domains)",
    "3.2": "Genes with amino-acid similarity confined to regions of a known protein without known functional association.",
    "4.1": "Predicted genes composed of a pattern of two or more consistent exons (located within <20 kb) and supported by spliced EST match(es)",
    "4.2": "Predicted genes corresponding to spliced EST(s) but which failed to be recognized by exon prediction programs",
    "4.3": "Predicted genes composed only of a pattern of consistent exons without any matches to ETS(s) or cDNA. Intuitively, predicted genes from subcategory 4.1 are considered to have stronger coding potential than those of subcategory 4.3",
    "5": "Pseudogenes may be regarded as gene-derived DNA sequences that are no longer capable of being expressed as protein products. They were defined as predicted polypeptides with strong similarity to a known gene, but showing at least one of the following features: lack of introns when the source gene is known to have an intron/exon structure, occurence of in-frame stop codons, insertions and/or deletions that disrupt the ORF or truncated matches. Generally, this was an unambiguous classification."
}


def get_category_description(category):
    # Lookup and return the category description from the dictionary
    return category_descriptions.get(category, "Unknown")


def main():
    parser = argparse.ArgumentParser(description='Combine on gene name and count the category occurrence')
    # XXX Make help more useful
    parser.add_argument('-i1', '--infile1', 
        required=True, 
        help='Gene description file; <gene> <desc> per line; e.g. HUGO_genes.txt"'
        )
    parser.add_argument('-i2', '--infile2', 
        required=True, 
        help='Gene category file; <gene> <desc> <cat> per line; e.g. chr21_genes.txt'
        )

    args = parser.parse_args()

    # Initialize a dictionary to store the category counts
    category_counts = {}

    # Read the category information from the specified file (infile2)
    # XXX This file has 3 values per line; Cat in col 3 
    with open(args.infile2, 'r') as category_file:
        n_line = 0
        for line in category_file:
            n_line += 1

            # Skip the header line
            if n_line < 2:
                continue

            # In case data line doesn't have three cols
            try:
                gene, desc, cat = line.strip().split('\t')
                if cat in category_counts:
                    category_counts[cat] += 1
                else:
                    category_counts[cat] = 0
            except Exception as e:
                print(f"Problem 3-col line [{n_line}]: {line}")

    # Read the gene data from the specified file (infile1)
    # XXX This file has 2 values per line; Needed?
    with open(args.infile1, 'r') as gene_file:
        n_line = 0
        for line in gene_file:
            n_line += 1

            # Skip the header line
            if n_line < 2:
                continue

            # In case data line doesn't have two cols
            try:
                gene, description = line.strip().split('\t')
            except Exception as e:
                print(f"Problem 2-col line [{n_line}]: {line}")


    # Sort the categories in ascending order
    sorted_categories = sorted(category_counts.keys())

    # Write the results to the output file
    with open(OUT_FNAME, 'w') as OUTFILE:
        print("Category\tOccurrence\tDescription", file=OUTFILE)
        for category in sorted_categories:
            description = get_category_description(category)
            occurrence = category_counts[category]
            print(f"{category}\t{occurrence}\t{description}", file=OUTFILE)

    print(f"Counts have been written to {OUT_FNAME}")


if __name__ == "__main__":
    main()
