"""
Path names
We refer to files with their absolute file paths or relative paths.
The paths have different representations; Windows uses different file paths than Linux.
The first one is the Windows file path.
The second one is an URI style.
The third one is the POSIX style.
"""
from pathlib import Path

path = Path('/Users/om/SB004/com/simplilearn/pathlib/path.txt')
print("******")
home = Path.home()

relative = path.relative_to(home)
print(relative)