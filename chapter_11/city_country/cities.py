from city_functions import get_formatted_location

while True:
    city = input("\nPlease give me a city name: ")
    if city == 'q':
        break
    country = input("Please give me a country name: ")
    if country == 'q':
        break
    population = input("Please give me a population: ")
    if population == 'q':
        break
    formatted_location = get_formatted_location(city, country, population)
    print(f"\tNeatly formatted location: {formatted_location}")