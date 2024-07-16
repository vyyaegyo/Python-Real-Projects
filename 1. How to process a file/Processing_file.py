# Reading text from a file

from pathlib import Path
directory = Path('/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/1. How to process a file')
filename = 'fruits.txt'
file_path = directory / filename

print("Constructed file path:", file_path)
try:
    with open(file_path, 'r') as myfile:
        contents = myfile.read()
        print(contents)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except IOError as e:
    print(f"Error reading file: {e}")

# Cursor concept. If you want to print the concent many times
from pathlib import Path
directory = Path('/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/1. How to process a file')
filename = 'fruits.txt'
file_path = directory / filename
with open(file_path, 'a') as myfile:
    myfile.write("grape")
    myfile.seek(0)
    contents = myfile.read()
    print(contents)
    
