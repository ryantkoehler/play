
def split_attributes(s):
    """Returns a dictionary of GTF/GFF file attributes

    s = string with gtf column 9 data, i.e. attributes. For example:
        'gene_id "ENSG00000188976"; gene_version "10"; transcript_id "ENST00000327044"; ...'

    Return dict
    """
    # Break into space-stripped key val strings
    att_list = [p.strip() for p in s.strip().split("; ")]
    # Keys = first space-delimited token
    att_keys = [a.split(" ")[0] for a in att_list]
    # Values = remaining text
    att_values = [a.split(" ", 1)[1] for a in att_list]
    # Attributes may or may not be quoted; Remove this and strip end space or semicolon
    att_values = [a.replace('"', "").strip().strip(";") for a in att_values]

    return dict(zip(att_keys, att_values))


def get_attribute(s, att_key):
    """Look for attribute value by key in attributes string

    Creates dict of attribute fields then looks in that for value
    (Not the most efficient way to process ... but works with pandas df apply)

    Return attribute value if found
    """
    att_value = ""
    try:
        att_value = split_attributes(s)[att_key]
    except Exception:
        pass
    return att_value


def get_one_att_value(att_string, att_key):
    """Attempt to get value for one attribute with given key

    att_string = "Attribues" data from gtf line; i.e. col 9
    Attributes are semicolon-separated key "value" pairs, like:
        'gene_id "Vmn2r116l-ps30"; transcript_id "";  ...  ; db_xref "GeneID:102552844"; '

    Return str
    """
    att_key += " "
    if att_string.startswith(att_key):
        start_index = len(att_key)
    else:
        index = att_string.find("; " + att_key)
        if index < 0:
            return ""
        start_index = index + len(att_key) + 2

    # End of key-value ... No error if not found (bogus format)
    end_index = att_string.find(";", start_index)
    if end_index < 0:
        return ""

    # Get rid of quotes and any trailing spaces
    return att_string[start_index:end_index].replace('"', "").strip()




"""

    gtf_gene_combined.loc[:, "gene_id"] = gtf_gene_combined.Attributes.apply(
        lambda s: get_attribute(s, "gene_id")
    )


    # Create a dictionary from genes to exons
    exon_gene_ids = gtf_exon_combined.Attributes.apply(
        lambda s: get_attribute(s, "gene_id")
    ).values

    # Add gene_id col then make mappings to that
    gtf_gene_combined["gene_id"] = gtf_gene_combined["Attributes"].apply(
        lambda s: get_attribute(s, "gene_id")
    )

    gene_id_to_gene_names = dict(
        zip(
            gtf_gene_combined["gene_id"].values,
            gtf_gene_combined["Attributes"].apply(
                lambda s: get_attribute(s, "gene_name")
            ),
        )
    )

"""
