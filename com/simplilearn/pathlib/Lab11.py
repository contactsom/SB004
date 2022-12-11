"""
Path parts
Path consists of subelements, such as drive or root.
"""
from pathlib import Path

path = Path('/Users/om/SB004/com/simplilearn/pathlib/path.txt')
print("_____________________________")
print(f"The Parts is: {path.parts}")
print(f"The Drive is: {path.drive}")
print(f"The Root is: {path.root}")
print("_____________________________")
print(f"The stem is: {path.stem}")
print(f"The name is: {path.name}")
print(f"The suffix is: {path.suffix}")
print(f"The anchor is: {path.anchor}")