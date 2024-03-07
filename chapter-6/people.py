person_0 = {
    'first_name': 'Brett',
    'last_name': 'Heatley',
    'city': 'Los Angeles',
}

person_1 = {
    'first_name': 'Ben',
    'last_name': 'Murphey',
    'city': 'Port Orange',
}

person_2 = {
    'first_name': 'Nick',
    'last_name': 'Stroupe',
    'city': 'Tampa',
}

people = [person_0, person_1, person_2]

for person in people:
    print(f"\n{person['first_name']} {person['last_name']} lives in {person['city']}.")