"""
Python pathlib copy file
With the help of the shutil module, we copy a file.
"""
from pathlib import Path
from shutil import copyfile

source = Path('words.txt')
destination = Path('words_bck.txt')

copyfile(source, destination)