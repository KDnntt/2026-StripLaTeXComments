"""
Author: K. Dunnett
Date started: 2026-05-23

Checks .tex file;
Saves a copy with date in 'Old_Source_Versions' if wanted
Opens .tex file and removes:
    - any line starting with % (i.e. entirely a comment);
    - from % (but not '\\%') to end of line (i.e. commented text):
Writes removed text/lines to new file ('Cut'+ date.tex; moved at end to 'Cut_stuff' directory);
Replaces old .tex with version without comments (and with extra spaces removed) 

Alias will be (something like) CleanLatex filename.tex
    (for python Strip_LaTeX_Comments.py filename.tex)
"""
#import python libraries etc
import sys
import re
import shutil
from datetime import date
import os
#import my modules
import make_copy as mcp
import clean_write as clwr

# Read in name of file to clean up (remove commented lines etc. from)
FILE_TO_CLEAN = str(sys.argv[1])

# Check file extension is .tex; quit if not
if not FILE_TO_CLEAN.endswith(".tex"):
    print("Filename ", FILE_TO_CLEAN, "not named as a LaTeX file (does not end '.tex')")
    sys.exit()

# strip ending off filename; get the day's date (ISO)
source_file_stem = FILE_TO_CLEAN[:-4]
today = str(date.today())

#create copy of old version (dated) if requested
mcp.keep_copy_or_not(source_file_stem, today)
keep_doubles = mcp.preserve_double_percents()

print(keep_doubles)

cut_filename = "Cut-"+today+".tex"
clean_filename = "new_"+FILE_TO_CLEAN #replace old file with new

cutout = open(cut_filename, 'a')
cleanout = open(clean_filename, 'w')

with open(FILE_TO_CLEAN, 'r') as filein:
    for line in filein:
        if "%" not in line:
            l = clwr.clean_spaces(line)
            cleanout.write(l)
        elif line.startswith("%%"): #keep double comments
            if keep_doubles == "y":
                l = clwr.clean_spaces(line)
                cleanout.write(l)           
            else:
                cutout.write(line)
        elif line.startswith("%"):
            #print("comment line")
            cutout.write(line)
        elif "%" in line:
            percentat = line.index("%") #location of first %
            if line[percentat-1] != "\\":
            #if first % is not \% - split:
                clwr.simple_split_percent(line, cutout, cleanout)
            else:
                #first % is \%; go through carefully
                p = re.compile("%")
                q = re.compile("\\\\%")
                if len(p.findall(line)) == len(q.findall(line)):
                    #if only percentages are '\\%'
                    l = clwr.clean_spaces(line)
                    cleanout.write(l)
                else:
                    #print("there's a comment", line)
                    for m in p.finditer(line):
                        #find first % that's not \% -> start of comment
                        if line[m.start()-1] != "\\":
                            #split and print line
                            clwr.split_loc_percent(line, m.start(), cutout, cleanout)

cutout.close()
cleanout.close()

#move file of cut stuff to directory "Cut_stuff"
cut_dir = "Cut_stuff"
new_file = mcp.save_to_directory(cut_dir, cut_filename)
shutil.move(cut_filename, new_file)

#rename cleaned file as original filename
os.rename(clean_filename, FILE_TO_CLEAN)
