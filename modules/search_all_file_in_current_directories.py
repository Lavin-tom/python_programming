#! /usr/bin/python3

# search all file in current directory

from pathlib import Path

path = Path()
for file in path.glob('*.py'):              # find all .py file from the directories
    print(file)
