from pathlib import Path

path = Path('guest.txt')

first_name = input("First name: ")
last_name = input("Last name: ")
full_name = f"{first_name} {last_name}"

path.write_text(full_name.title())