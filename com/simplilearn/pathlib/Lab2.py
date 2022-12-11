"""
Path cwd and home
We get the current working directory with cwd and the home directory with home.
"""

from pathlib import Path

print(f"Current directory: {Path.cwd()}")
print(f"Home directory: {Path.home()}")