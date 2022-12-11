"""
Python pathlib change directory
We go inside another directory with os' chdir.
"""

from pathlib import Path
from os import chdir

path = Path('..')

print(f'Current working directory: {path.cwd()}')

chdir(path)

print(f'Current working directory: {path.cwd()}')

chdir('..')

print(f'Current working directory: {path.cwd()}')