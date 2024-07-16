# Built in modules: import sys - sys.builtin_module_names - import time - dir(time) - help(time.sleep)
import time
import os

while True:
    if os.path.exists("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/2. Modules/fruits.txt")
    with open("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/2. Modules/fruits.txt") as file:
         print(file.read())
else:
    print{'File does not exist'}

time.sleep(10)

# Standard Python modules
import time
import os
import pandas

while True:
    if os.path.exists("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/2. Modules/temps_today.csv"):
        data = pandas.read_csv("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/2. Modules/temps_today.csv")
        print(data.mean())
    else:
        print("File does not exist.")
time.sleep(3)

