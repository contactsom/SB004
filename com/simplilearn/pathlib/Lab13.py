"""
Path globbing
"""
from pathlib import Path

path = Path('/Users/om/SB004/com/simplilearn/')
print("_____________________________")
for e in path.rglob('*.py'):
    print(e)