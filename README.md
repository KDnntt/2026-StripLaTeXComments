Little python file that removes comment lines (starting with %)
and comments (from % to end of line) from LaTeX (.tex) files.

Developed on Linux (Ubuntu) with python3
Runs from terminal/command line.

Saves .tex file with comments removed and dated file with removed comments in directory 'Cut_stuff' (created if not already present).

NotDone.txt are some notes for potential additional features.

## Basic usage

.tex and .py files in same directory (folder):
python3 Strip_LaTeX_Comments.py file_to_clean.tex

from directory with .tex file to remove comments from:
python3 /path_to/Strip_LaTeX_Comments.py file_to_clean.tex

as bash alias:
in directory with .tex file to remove comments from:
alias_name filename.tex
with
alias alias_name='python3 /path_to/Strip_LaTeX_Comments.py'
in .bash_aliases or .bashrc


## Prompts

1. Keep copy of old version with comments in place? (y/n; q to quit)
Saves dated copy of the version before clean up in directory
'Old_Source_Versions' (directory created if not already present)

2. Keep comment lines starting with %%? (y/n; q to quit)
Allows multiple %%s (at least two, with out spaces) to be kept
- useful for, e.g., commands that may be redefined late in working.


## Suggested user adaptations

Edit the relevant name definitions in if the standard names do not suit:
- Directory name for 'Old_Source_Versions' (in make_copy.py).
- Directory name for 'Cut_stuff' (in Strip_LaTeX_Comments.py).
- File names for 'Cut_date.tex' in 'Cut_stuff' (in Strip_LaTeX_Comments.py).
