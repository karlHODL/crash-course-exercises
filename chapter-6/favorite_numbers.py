favorite_numbers = {
    'jen': 3,
    'sarah': 7,
    'edward': 9,
    'phil': 2,
    'james': 5,
}

print(f"Jen's favorite number is {favorite_numbers['jen']}.")
print(f"Sarah's favorite number is {favorite_numbers['sarah']}.")
print(f"Edward's favorite number is {favorite_numbers['edward']}.")
print(f"Phil's favorite number is {favorite_numbers['phil']}.")
print(f"James's favorite number is {favorite_numbers['james']}.")

favorite_numberss = {
    'jen': [3, 7],
    'sarah': [7, 9],
    'edward': [9],
    'phil': [2, 5],
    'james': [5, 3],
}

for name, numbers in favorite_numberss.items():
    if len(numbers) > 1:
        print(f"\n{name.title()}'s favorite numbers are:")
    else:
        print(f"\n{name.title()}'s favorite number is:")
    for number in numbers:
        print(f"\t{number}")