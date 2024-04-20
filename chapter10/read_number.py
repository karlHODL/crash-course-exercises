from pathlib import Path
import json

# define the path the file is located
path = Path('favorite_number.json')

# read in the text contents from the file
contents = path.read_text()

# convert the json object to a python object
number = json.loads(contents)

# print the number
print(f"I know your favorite number! It's {number}!")