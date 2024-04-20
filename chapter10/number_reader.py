from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
# print(type(contents))
numbers = json.loads(contents)

# print(type(numbers))
print(numbers)