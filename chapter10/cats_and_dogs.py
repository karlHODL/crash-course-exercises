from pathlib import Path

def read_file(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"The file {path} does not exist.")
        pass
    else:
        print(contents)

filenames = ['cats.txt', 'marsupials.txt', 'dogs.txt']

for filename in filenames:
    file_path = Path(filename)
    read_file(file_path)