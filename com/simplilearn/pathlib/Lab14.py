"""
Counting files by extension
"""


import collections
from pathlib import Path

docs = Path.home() / 'SB004/com/simplilearn/pathlib'
print(docs)


files = [path.suffix for path in docs.iterdir() if path.is_file() and path.suffix]
data = collections.Counter(files)

print(data)

for key, val in data.items():
    print(f'{key}: {val}')

