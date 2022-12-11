"""
Joining paths
Paths can be joined with the / operator or the joinpath method.
"""
from pathlib import Path

path = Path.home()
print(path)

docs = path / 'Documents'
pictures = path / 'Pictures'

print(docs)
print(pictures)