#! /usr/bin/python3

# path lib Module

from pathlib import Path

path = Path("sum.py")
print(path.exists())            # to find the file exist in the directory or not
path = Path("emails")
print(path.exists())
print(path.mkdir())               # to make a folder if not available it create it

path = Path("emails")
print(path.rmdir())
