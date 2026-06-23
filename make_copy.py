"""
Subroutines for saving copies of files in standard named sudirectories.
"""

import shutil
import os
import sys

def save_to_directory(direct, filename):
    """
    Create path for new file in subdirectory of current directory.
    Args:
        direct (str): subdirectory file will be saved in
        filename (str): name of file (no path)
    (Used in copy_with_date and writing_cut_text.)
    """
    #get path of current working directory
    this_dir = os.getcwd()
    dest_dir = os.path.join(this_dir, direct)
    # Create destination directory as subdirectory of current if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    #create path for new file to be saved as
    new_file = os.path.join(dest_dir, filename)
    return new_file

def copy_with_date(source_file_stem, do_date):
    """
    Copy file to `Old_Source_Versions'
    source: https://pythonguides.com/python-copy-file/
    Args:
        source_file_stem (str): Source file name stem
        do_date (str) : date of copy/reference
    """
    try:
        direct_to_save_to = "Old_Source_Versions"
        # file names (including new with path)
        source_file = source_file_stem+".tex"
        new_name = source_file_stem+"-"+do_date+".tex"

        new_file = save_to_directory(direct_to_save_to, new_name)

        #copy file
        shutil.copy(source_file, new_file)

        print(f"Copy of old version saved as {new_name} in folder {direct_to_save_to}.")

    except Exception as e:
        print(f"Error during copy operation: {e}")

def keep_copy_or_not(source_file_stem, today):
    """
    Prompt behaviour - new file or replace (keep old version with comments  or not).
    repeated until y/n (or q for quit) received
    use tolower(input) so don't worry about caps.
    """
    while True:
        keep_copy = input("Keep copy of old version with comments in place? (y/n; q to quit) ")
        if keep_copy.lower() == 'y':
            #print("Creating copy of old version with comments in place.")
            copy_with_date(source_file_stem, today)
            break
        if keep_copy.lower() == 'n':
            print("Not creating a copy of the old version with comments in place.")
            break
        if keep_copy.lower() == "q":
            print("Quitting.")
            sys.exit()
        else:
            print("Invalid input. Enter y (create copy), n (don't create copy), or q (quit).")

def preserve_double_percents():
    """
    Prompt behaviour - keep lines starting with %% (i.e., things likely to switch on or off)
    repeated until y/n received
    use tolower(input) so don't worry about caps.
    """
    while True:
        keep_doubles = input("Keep comment lines starting with %%? (y/n; q to quit) ").lower()
        if keep_doubles == 'y':
            print("Comment lines starting with %% are being retained.")
            break
        if keep_doubles == 'n':
            print("Comment lines starting with %% are being deleted.")
            break
        else:
            print("Invalid input. Enter y (keep lines starting %%), n (delete lines starting %%)")
    return keep_doubles
