from pathlib import Path
import json

path = Path('number_remembered.json')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}!")
else:
    number = int(input("What is your favorite number? "))
    contents = json.dumps(number)
    path.write_text(contents)
    print("Your favorite number has been saved!")