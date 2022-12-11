"""
Python pathlib current file
The __file__ gives the path to the current running program.

"""

from pathlib import Path

p = Path(__file__)
print(p)
