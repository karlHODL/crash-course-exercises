rivers = {'nile': 'egypt', 'mississippi': 'united states', 'amazon': 'brazil'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers:")
for river in rivers.keys():
    print(river.title())

print("\nCountries:")
for country in set(rivers.values()):
    print(country.title())