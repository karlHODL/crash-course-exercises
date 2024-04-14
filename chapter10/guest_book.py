from pathlib import Path

path = Path('guest_book.txt')

contents = ''

while True:
    first_name = input("First name: ")
    last_name = input("Last name: ")
    full_name = f"{first_name} {last_name}"
    print(f"Hello, {full_name.title()}!")
    contents += full_name.title() + "\n"
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        path.write_text(contents)
        break
    else:
        continue

