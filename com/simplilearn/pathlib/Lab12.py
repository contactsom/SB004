"""
Path list directories
The iterdir yields path objects of the directory contents.
"""
from pathlib import Path

path = Path('/Users/om/SB004/com/simplilearn/')
print("_____________________________")
dirs = [e for e in path.iterdir() if e.is_dir()]
print(dirs)