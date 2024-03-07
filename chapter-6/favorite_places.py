favorite_places = {
    'jen': ['paris','rome','london'],
    'sarah': ['new york'],
    'edward': ['tokyo','seoul'],
    'phil': ['sydney','melbourne'],
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{name.title()}'s favorite places are:")
    else:
        print(f"\n{name.title()}'s favorite place is:")
    for place in places:
        print(f"\t{place.title()}")