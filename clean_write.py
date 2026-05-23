"""
Modules for cleaning up lines and writing to file
"""
#import

def write_to(line):
    """
    Clean line of superfluous spaces (two or end of line).
    Write line to file.
    Args:
        line (str): line to be cleaned and written
        filename (str): file to write to
    """
    clean = clean_spaces(line)
    return clean

def clean_spaces(line):
    """
    Clean line of superfluous spaces (two or end of line).
    Args:
        line (str): line to be cleaned    
    """
    #split on spaces and rejoin with single spaces (also removes leading and trailing spaces)
    line = ' '.join(line.split(' '))
    return line
    
def simple_split_percent(line, cutout, cleanout):
    """
    Write to file when first % in line is start of comment
    Args:
        line (str): line to be treated
        cutout (str): filename where comment part of line is written to
        cleanout (str): filename where non-comment part of line is written to
    """
    #parts[0] is text to keep, parts[1] is commented
    parts = line.split('%', 2)
    #write parts to two files
    cutout.write(parts[1])
#    l = clean_spaces(parts[0])
#    print(l)
    cleanout.write(parts[0])

def split_loc_percent(line, loc, cutout, cleanout):
    """
    Write to file when first % in line is not start of comment (\\%)
    Args:
        line (str): line to be treated
        loc (int): location of first '%' (not '\\%')
        cutout (str): filename where comment part of line is written to
        cleanout (str): filename where non-comment part of line is written to
    """
    #parts[0] is text to keep, parts[1] is commented
    parts = (line[:loc], line[loc:])
    #write parts to two files
    cutout.write(parts[1])
#    l = clean_spaces(parts[0])
#    print(l)
    cleanout.write(parts[0])

