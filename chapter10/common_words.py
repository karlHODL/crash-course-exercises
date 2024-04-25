from pathlib import Path
import re 

texts = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

def count_words(path):
    """Count the words in a specified text based on its provided path"""
    file = Path(path)
    try:   
        contents = file.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"The file {path} does not exist.")
    except UnicodeDecodeError:
        print(f"Error decoding the file {path}")
    else:
        pattern = r'\bthe\b'
        count = len(re.findall(pattern, contents.lower()))
        print(f"The word 'the' appears {count} in {path}.")

for text in texts:
    count_words(text)