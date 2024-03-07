pet_0 = {
    'type': 'dog',
    'owner': 'ally',
}

pet_1 = {
    'type': 'cat',
    'owner': 'mike',
}

pet_2 = {
    'type': 'bird',
    'owner': 'james',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"\n{pet['owner'].title()} has a {pet['type']}.")