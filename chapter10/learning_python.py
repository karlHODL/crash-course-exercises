from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text().strip()
print(contents)

print("\n")
for line in contents.splitlines():
    print(line.replace('Python', 'C'))