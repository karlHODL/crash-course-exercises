person = {
    'first_name': 'Brett',
    'last_name': 'Heatley',
    'city': 'Los Angeles',
}

first_name = person.get('first_name', 'No first name assigned.')
last_name = person.get('last_name', 'No last name assigned.')
city = person.get('city', 'No city assigned.')

print(f"{first_name.title()} {last_name.title()} lives in {city.title()}.")