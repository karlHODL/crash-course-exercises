cities = {
    'new york': {
        'country': 'united states',
        'population': '8.4 million',
        'fact': 'The first American chess tournament was held in New York in 1843.',
    },
    'los angeles': {
        'country': 'united states',
        'population': '3.9 million',
        'fact': 'The full name of Los Angeles is "El Pueblo de Nuestra Senora la Reina de los Angeles de Porciuncula".',
    },
    'chicago': {
        'country': 'united states',
        'population': '2.7 million',
        'fact': 'The first nuclear chain reaction was achieved in Chicago in 1942.',
    },
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']
    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  Fun fact: {fact}")