def city_country(city, country):
    return f"{city.title()}, {country.title()}"

cities = []
cities.append(city_country('vienna', 'austria'))
cities.append(city_country('sydney', 'australia'))
cities.append(city_country('london', 'england'))

for city in cities:
    print(city)