"""
Path touch
The touch creates a new empty file; it is an equivalent of the Linux touch command
"""
from pathlib import Path

Path('myfile.txt').touch()