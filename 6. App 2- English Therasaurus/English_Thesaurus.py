import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


try:
    with open("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/6. App 2- English Therasaurus/data.json") as file:
        data = json.load(file)
except FileNotFoundError:
    print("The data file was not found.")
    data = {}

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys()) [0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys()) [0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
    
word = input("Enter word: ")  # Get user input first

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output) 





