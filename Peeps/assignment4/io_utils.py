#
#


def get_filehandle(fname, mode='r'):
    """Attempt to open given file with mode

    Return file handle or None
    """
    try:
        handle = open(fname, mode=mode)
    except Exception as e:
        print(f"Problem opening file; {e}")
        handle = None
    return handle
        

def get_data_file_col(fname, col=1, sep='\t'):
    """Get list of data from column in data file
    
    fname = file name to read
    col = 1-based column to get data from
    sep = data column separators

    Return list
    """
    data_col = []
    INFILE = get_filehandle(fname)

    if INFILE is not None:
        for line in INFILE:
            parts = line.strip().split(sep)
            # Save col if have enough
            if len(parts) >= col:
                data_col.append(parts[col-1])
            # Else... could report or break?

        # Close file
        INFILE.close()

    return data_col
    
