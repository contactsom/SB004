"""
Counting files by extension
"""

from pathlib import Path
path = Path('words.txt')
content = path.read_text()
print(content)


