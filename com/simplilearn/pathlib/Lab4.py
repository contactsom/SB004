"""
Path mkdir
A new directory is created with mkdir.
"""

from pathlib import Path

path = Path.cwd() / 'new'

path.mkdir()