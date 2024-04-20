from pathlib import Path
import json

# get favorite number
number = int(input("What is your favorite number? "))

# get file path
path = Path('favorite_number.json')

# convert int to json object
contents = json.dumps(number)

# write json object to file
path.write_text(contents)