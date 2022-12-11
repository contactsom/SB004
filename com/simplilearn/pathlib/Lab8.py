"""
Path rename
The rename renames a file or directory.
"""
from pathlib import Path

path = Path('names.txt')

path.rename('mynames.txt')